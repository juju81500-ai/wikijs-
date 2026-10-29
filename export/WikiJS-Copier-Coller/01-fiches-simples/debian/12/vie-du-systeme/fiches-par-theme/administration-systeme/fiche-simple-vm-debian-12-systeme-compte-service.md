# 📄 VM_Debian_12_Systeme_Compte-Service.md

- **Environnement** : VM (Proxmox VE / KVM)
- **OS / Version** : Debian 12 (Bookworm) - Famille Debian
- **Catégorie** : Sécurité & Comptes / Comptes de service isolés

## 🎯 Problème précis à résoudre
Créer un compte système dédié à une application sur Debian 12, sans shell interactif ni mot de passe, avec un répertoire de travail isolé, et l'exécuter via une unité systemd durcie.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Vérification de l'absence du compte cible :
   `getent passwd <compte_service>`
   👉 Explication : Ne doit rien renvoyer ; sinon le nom est déjà utilisé et il faut choisir un autre identifiant.
2. Création du compte système :
   `sudo useradd --system --home-dir /var/lib/<compte_service> --shell /usr/sbin/nologin <compte_service>`
   👉 Explication : Crée un compte d'UID inférieur à 1000, sans répertoire personnel automatique, avec le shell `nologin` qui refuse toute session interactive.
3. Test d'identité du compte :
   `sudo -u <compte_service> id`
   👉 Explication : Confirme que le processus peut être lancé sous ce compte, même sans shell de connexion.

---

## ⚡ 2. Production — Façon Simplifiée
1. Création du répertoire de travail avec propriétaire dédié :
   `sudo install -d -o <compte_service> -g <compte_service> -m 750 /var/lib/<compte_service>`
   👉 Explication : Crée `/var/lib/<compte_service>` appartenant au compte de service, lisible uniquement par lui et son groupe.
2. Contrôle de l'entrée dans la base des comptes :
   `sudo grep '^<compte_service>:' /etc/passwd`
   👉 Explication : La sixième colonne doit être `/usr/sbin/nologin`.

---

## 🔒 3. Production — Façon Sécurisée (Verrouillage & Unité systemd durcie)
1. Verrouillage du mot de passe :
   `sudo passwd -l <compte_service>`
   👉 Explication : Empêche toute authentification par mot de passe sur ce compte, en complément du shell `nologin`.
2. Durcissement de l'unité systemd du service applicatif :
   `sudo systemctl edit <nom_du_service>`
   👉 Explication : Ajouter dans la surcharge `[Service]` les directives `User=<compte_service>`, `NoNewPrivileges=yes`, `ProtectSystem=strict`, `ProtectHome=yes` et `ReadWritePaths=/var/lib/<compte_service>`.
3. Analyse du niveau de sécurité de l'unité :
   `systemd-analyze security <nom_du_service>`
   👉 Explication : Attribue un score d'exposition à l'unité et liste les directives manquantes pour l'améliorer.