# 📄 Fiche_Simple_-_TrueNAS_SCALE_25.10_Securite_Admin_SSH.md

- **Environnement** : TrueNAS SCALE 25.10 (Goldeye), NAS de lab ou de production sur réseau de gestion
- **OS / Version** : TrueNAS SCALE 25.10 Goldeye (base Debian)
- **Catégorie** : Sécurité / Comptes et accès SSH
- **Tags** : `truenas`, `scale2510`, `debian`, `ssh`, `sudo`, `hardening`

---

## 🎯 Problème précis à résoudre
Créer un compte administrateur nominatif, déposer sa clé SSH, désactiver la connexion root par mot de passe et vérifier la configuration effective de sshd, sans perdre l'accès à l'interface web.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Créer un compte administrateur nominatif :
   `Credentials > Local Users > Add` : Username = `<admin_nominatif>`, Auxiliary Groups = `builtin_administrators`, Allow all sudo commands = coché (libellés à vérifier sur la version déployée)
   👉 Explication : Un compte personnel assure la traçabilité ; le compte root n'est plus utilisé au quotidien.
2. Déposer la clé publique de l'administrateur :
   `Credentials > Local Users > <admin_nominatif> > Edit` : champ SSH Public Key = contenu de `<cle_publique>.pub`
   👉 Explication : La clé est écrite dans le fichier authorized_keys géré par TrueNAS.
3. Activer le service SSH :
   `System Settings > Services > SSH` : Running = activé, Start Automatically = activé
   👉 Explication : Démarre sshd et le relance après redémarrage.
4. Tester la connexion par clé :
   `ssh -i ~/.ssh/<cle_admin> <admin_nominatif>@<adresse_ip_truenas>`
   👉 Explication : Valide l'accès avant toute modification de la méthode d'authentification.
5. Lire la configuration effective de sshd :
   `sudo sshd -T | grep -E '^(port|permitrootlogin|passwordauthentication) '`
   👉 Explication : Affiche la configuration réellement chargée, et non le fichier modifié à la main (le fichier /etc/ssh/sshd_config est régénéré par TrueNAS).

---

## ⚡ 2. Production — Façon Simplifiée
1. Désactiver la connexion root par mot de passe :
   `System Settings > Services > SSH` (paramètres) : Log in as Root with Password = désactivé
   👉 Explication : Le root ne peut plus se connecter avec un mot de passe ; seul l'accès par clé ou via le compte nominatif reste possible.
2. Restreindre le port et les interfaces d'écoute SSH :
   `System Settings > Services > SSH` : TCP Port = `22`, Bind Interfaces = `<interface_gestion>`
   👉 Explication : sshd n'écoute que sur le réseau de gestion.
3. Vérifier la configuration appliquée :
   `midclt call ssh.config`
   👉 Explication : Interroge le middleware TrueNAS et renvoie les paramètres SSH enregistrés.

---

## 🔒 3. Production — Façon Sécurisée
1. Désactiver l'authentification par mot de passe pour tous les comptes :
   `System Settings > Services > SSH` : Allow Password Authentication = désactivé, Password Login Groups = vide
   👉 Explication : Seules les clés déposées peuvent ouvrir une session SSH.
2. Limiter l'interface web au réseau de gestion et forcer HTTPS :
   `System Settings > General > GUI` : Web Interface IPv4 Address = `<adresse_ip_gestion>`, Web Interface HTTP -> HTTPS Redirect = activé (libellés à vérifier sur la version déployée)
   👉 Explication : Empêche l'accès au Web UI depuis les réseaux utilisateurs et évite l'échange de mots de passe en clair.
3. Vérifier qu'aucun accès SSH n'est ouvert depuis l'extérieur :
   `sudo ss -tlnp | grep ':22 '` (sur TrueNAS) et règle pare-feu amont limitée à `<reseau_gestion>`
   👉 Explication : Confirme l'écoute locale et le filtrage par le pare-feu périphérique.
4. Garder un compte de secours hors bande :
   `System Settings > Services > IPMI` ou console BMC `<acces_bmc>` (si disponible)
   👉 Explication : Permet de rétablir l'accès si la configuration SSH ou réseau est erronée.
