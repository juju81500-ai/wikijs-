# 📄 Fiche_Simple_-_Appliance_OPNsense_Securite_Admin_HTTPS.md

- **Environnement** : OPNsense sur VM Proxmox VE ou appliance dédiée, avec un réseau de gestion distinct du LAN utilisateurs
- **OS / Version** : OPNsense (base FreeBSD) - Toutes-versions (libellés de menu à vérifier sur la version déployée)
- **Catégorie** : Sécurité / Accès d'administration

---

## 🎯 Problème précis à résoudre
Restreindre l'interface web et l'accès SSH d'OPNsense à un réseau d'administration, imposer HTTPS et l'authentification par clé SSH, sans se verrouiller hors de l'appliance.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Passer l'interface web en HTTPS et limiter son écoute à l'interface d'administration :
   `System > Settings > Administration` : Protocol = `HTTPS`, TCP port = `443`, Listen Interfaces = `<interface_gestion>`
   👉 Explication : Supprime l'écoute HTTP en clair et empêche l'interface web d'écouter sur les interfaces utilisateurs.
2. Créer un alias du réseau d'administration :
   `Firewall > Aliases` puis Add : Name = `ADMIN_NET`, Type = `Network(s)`, Content = `<reseau_gestion>/<prefixe>`
   👉 Explication : Un alias unique se modifie en un seul point et sert dans toutes les règles d'administration.
3. Autoriser le réseau d'administration vers This Firewall :
   `Firewall > Rules > LAN` puis Add : Action = `Pass`, Source = `ADMIN_NET`, Destination = `This Firewall`, Destination port = `443`
   👉 Explication : Place la règle en tête de liste pour que seul ADMIN_NET atteigne l'interface web.
4. Ajouter une règle pour les postes utilisateurs avant de restreindre la règle par défaut :
   `Firewall > Rules > LAN` : Action = `Pass`, Source = `LAN net`, Destination = `any`
   👉 Explication : Évite de couper Internet aux postes utilisateurs lorsque la règle `Default allow LAN to any rule` est restreinte.
5. Tester depuis deux postes (un dans ADMIN_NET, un hors ADMIN_NET) :
   `curl -kI -m 5 https://<adresse_ip_opnsense>/`
   👉 Explication : Depuis ADMIN_NET, la réponse HTTP arrive ; ailleurs, la requête expire. Garder une session console ouverte pendant les tests.
6. Vérifier les ports en écoute depuis la console (option 8 Shell) :
   `sockstat -4 -6 -l | grep -E ':(80|443) '`
   👉 Explication : Seul le port 443 doit apparaître pour l'interface web.

---

## ⚡ 2. Production — Façon Simplifiée
1. Importer un certificat signé par l'autorité interne :
   `System > Trust > Certificates` (importer ou créer le certificat), puis `System > Settings > Administration` : SSL Certificate = `<certificat_admin>`
   👉 Explication : Les postes administrateurs n'affichent plus d'avertissement de certificat.
2. Activer SSH avec clé et sans connexion root par mot de passe :
   `System > Settings > Administration` (section Secure Shell) : Enable Secure Shell = coché, Permit root user login = `No`, Permit password login = `No` (à vérifier sur la version déployée)
   👉 Explication : Seules les clés déposées peuvent ouvrir une session SSH.
3. Déposer la clé publique de l'administrateur :
   `System > Access > Users` : éditer `<utilisateur_admin>`, champ Authorized keys = contenu de `<cle_publique>.pub`
   👉 Explication : La clé est associée au compte et utilisée par sshd.
4. Tester la connexion par clé :
   `ssh -i ~/.ssh/<cle_admin> <utilisateur_admin>@<adresse_ip_opnsense>`
   👉 Explication : Valide l'accès avant de fermer la session console de secours.

---

## 🔒 3. Production — Façon Sécurisée
1. Créer un compte administrateur nominatif et un groupe dédié :
   `System > Access > Users` : compte `<admin_nominatif>` ; `System > Access > Groups` : groupe `<groupe_admins>` avec le privilège administration
   👉 Explication : Assure la traçabilité et évite l'usage du compte root.
2. Vérifier qu'aucune règle n'expose l'administration sur WAN :
   `Firewall > Rules > WAN` : aucune règle Pass vers `This Firewall` sur les ports 22 ou 443
   👉 Explication : L'administration reste strictement interne.
3. Contrôler les règles réellement chargées depuis le shell :
   `pfctl -sr | grep -E 'ssh|https|22|443'`
   👉 Explication : Compare les règles actives avec celles de l'interface.
4. Envoyer les journaux d'administration vers un syslog distant (voir la fiche Supervision_Syslog) :
   `System > Settings > Logging / targets`
   👉 Explication : Les événements d'authentification sont conservés hors de l'appliance.