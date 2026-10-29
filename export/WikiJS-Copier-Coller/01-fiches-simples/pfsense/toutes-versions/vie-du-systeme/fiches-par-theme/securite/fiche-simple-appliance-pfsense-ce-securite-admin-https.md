# 📄 Fiche_Simple_-_Appliance_pfSense_CE_Securite_Admin_HTTPS.md

- **Environnement** : pfSense CE sur VM Proxmox VE ou appliance dédiée, avec un réseau de gestion distinct du LAN utilisateurs
- **OS / Version** : pfSense CE 2.x (base FreeBSD) - Toutes-versions (libellés de menu en anglais par défaut)
- **Catégorie** : Sécurité / Accès d'administration

---

## 🎯 Problème précis à résoudre
Restreindre l'interface web (webConfigurator) et l'accès SSH de pfSense CE à un seul réseau d'administration, imposer HTTPS et l'authentification par clé SSH, sans se verrouiller hors de l'appliance.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Passer le protocole de l'interface web en HTTPS :
   `System > Advanced > Admin Access` : Protocol = `HTTPS`, TCP Port = `443`
   👉 Explication : Supprime l'écoute HTTP en clair. Le certificat par défaut est auto-signé et sera remplacé en section 2.
2. Créer un alias du réseau d'administration :
   `Firewall > Aliases > IP` puis Add : Name = `ADMIN_NET`, Type = `Network(s)`, Network = `<reseau_gestion>/<prefixe>`
   👉 Explication : Un alias unique évite de répéter l'adresse dans chaque règle et se modifie en un seul point.
3. Autoriser le réseau d'administration vers l'interface web, et seulement lui :
   `Firewall > Rules > LAN` puis Add : Action = `Pass`, Source = `ADMIN_NET`, Destination = `This Firewall`, Destination Port Range = `HTTPS (443)`
   👉 Explication : Place la règle en tête de liste. Le webConfigurator n'est alors joignable que depuis ADMIN_NET.
4. Ajouter une règle pour les postes utilisateurs avant de retirer la règle par défaut :
   `Firewall > Rules > LAN` : Action = `Pass`, Source = `LAN net`, Destination = `any`, puis désactiver `Default allow LAN to any rule`.
   👉 Explication : La règle par défaut autorise tout le LAN vers tout, y compris vers This Firewall. La retirer sans règle de remplacement coupe Internet aux postes utilisateurs.
5. Tester depuis un poste de ADMIN_NET puis depuis un poste hors ADMIN_NET :
   `curl -kI -m 5 https://<adresse_ip_pfsense>/`
   👉 Explication : Depuis ADMIN_NET, la réponse HTTP est reçue (200 ou 302). Depuis un autre poste, la requête expire. L'option -k accepte le certificat auto-signé et -m 5 limite le délai.
6. Vérifier depuis la console (option 8 Shell) que seul le port 443 écoute pour l'interface web :
   `sockstat -4 -6 -l | grep -E ':(80|443) '`
   👉 Explication : Liste les sockets en écoute. Le port 80 ne doit plus apparaître une fois le HTTPS activé.

---

## ⚡ 2. Production — Façon Simplifiée
1. Remplacer le certificat auto-signé par un certificat signé par l'autorité interne :
   `System > Cert. Manager` (créer le certificat signé), puis `System > Advanced > Admin Access` : SSL Certificate = `<certificat_admin>`
   👉 Explication : Les postes administrateurs valident le certificat sans avertissement navigateur.
2. Activer SSH et déposer la clé publique de l'administrateur :
   `System > Advanced > Admin Access > Secure Shell` : cocher `Enable Secure Shell`, SSH Port = `22`
   `System > User Manager > Users > <utilisateur_admin>` : champ `Authorized SSH Keys` = contenu de `<cle_publique>.pub`
   👉 Explication : Active sshd et enregistre la clé publique dans le profil de l'utilisateur, que pfSense reporte dans son fichier authorized_keys.
3. Tester la connexion par clé :
   `ssh -i ~/.ssh/<cle_admin> -p 22 <utilisateur_admin>@<adresse_ip_pfsense>`
   👉 Explication : Confirme que la clé fonctionne avant toute modification de la méthode d'authentification. Si l'option de connexion par clé seule est disponible sur la version déployée (à vérifier), vérifier qu'une tentative par mot de passe est refusée.
4. Activer la protection contre le brute-force SSH et GUI :
   `System > Advanced > Admin Access > Login Protection` (à vérifier sur la version déployée)
   👉 Explication : Bloque temporairement les adresses qui échouent trop de connexions.
5. Autoriser SSH uniquement depuis ADMIN_NET :
   `Firewall > Rules > LAN` : Action = `Pass`, Source = `ADMIN_NET`, Destination = `This Firewall`, Destination Port Range = `SSH (22)`
   👉 Explication : Le port 22 suit la même restriction que l'interface web.

---

## 🔒 3. Production — Façon Sécurisée
1. Créer un compte administrateur nominatif, membre du groupe `admins` :
   `System > User Manager > Users > Add` : Username = `<admin_nominatif>`, Group Memberships = `admins`, Authorized SSH Keys renseignée
   👉 Explication : Assure la traçabilité des actions. Le compte `admin` d'origine est conservé uniquement pour un accès de secours, avec son mot de passe dans le coffre-fort.
2. Vérifier qu'aucune règle n'ouvre l'administration sur WAN :
   `Firewall > Rules > WAN` : aucune règle Pass vers `This Firewall` sur les ports 22 ou 443
   👉 Explication : Le WAN reste bloqué par défaut ; l'administration ne doit jamais être exposée sur Internet.
3. Contrôler les règles réellement chargées depuis le shell :
   `pfctl -sr | grep -E 'ssh|https|22|443'`
   👉 Explication : Affiche les règles actives filtrant les ports d'administration, pour comparer avec l'interface.
4. Envoyer les journaux d'administration vers un serveur syslog distant :
   `Status > System Logs > Settings > Remote Logging Options` : Enable Remote Logging, Remote log servers = `<adresse_ip_syslog>:514`
   👉 Explication : Copie les événements d'authentification hors de l'appliance, pour détection et conservation (étape 42 du cycle de vie).
5. Vérifier l'état du service SSH :
   `service sshd status`
   👉 Explication : Confirme que sshd tourne et correspond à la configuration validée.