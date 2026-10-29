# 📄 VM_Debian_12_Journaux_Journald-Logrotate.md

- **Environnement** : VM (Proxmox VE / KVM)
- **OS / Version** : Debian 12 (Bookworm) - Famille Debian
- **Catégorie** : Supervision & Journaux / Rétention et rotation

## 🎯 Problème précis à résoudre
Rendre le journal systemd persistant sur Debian 12 avec une taille et une durée de rétention bornées, et mettre en place la rotation des journaux des applications via `logrotate`, afin de conserver l'historique sans saturer le disque.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Consultation de l'espace occupé par le journal :
   `journalctl --disk-usage`
   👉 Explication : Affiche la taille actuelle des journaux systemd (`/var/log/journal` ou `/run/log/journal`).
2. Vérification de la persistance :
   `ls -ld /var/log/journal`
   👉 Explication : Si le dossier est absent, les journaux sont perdus à chaque redémarrage.
3. Simulation de la rotation système :
   `sudo logrotate --debug /etc/logrotate.conf`
   👉 Explication : Affiche les actions prévues par `logrotate` sans modifier aucun fichier.

---

## ⚡ 2. Production — Façon Simplifiée
1. Création du stockage persistant :
   `sudo mkdir -p /var/log/journal && sudo systemd-tmpfiles --create --prefix /var/log/journal`
   👉 Explication : Crée le répertoire et applique les droits attendus par systemd-journald.
2. Définition des bornes de rétention :
   `sudoedit /etc/systemd/journald.conf`
   👉 Explication : Dans la section `[Journal]`, définir `Storage=persistent`, `SystemMaxUse=1G` et `MaxRetentionSec=1month`.
3. Application de la configuration :
   `sudo systemctl restart systemd-journald`
   👉 Explication : Recharge `journald` avec les nouvelles bornes ; vérifier ensuite avec `journalctl --disk-usage`.

---

## 🔒 3. Production — Façon Sécurisée (Rotation applicative & Test)
1. Déclaration de la rotation d'une application :
   `sudoedit /etc/logrotate.d/<nom_application>`
   👉 Explication : Pour `/var/log/<nom_application>/*.log`, utiliser `weekly`, `rotate 8`, `compress`, `delaycompress`, `missingok`, `notifempty` et `create 0640 <compte_service> adm`, avec un `postrotate` qui envoie `SIGHUP` au service.
2. Test de la règle sans effet de bord :
   `sudo logrotate --debug /etc/logrotate.d/<nom_application>`
   👉 Explication : Valide la syntaxe et montre la prochaine rotation prévue, sans déplacer de fichier.
3. Rotation forcée et contrôle du résultat :
   `sudo logrotate -f /etc/logrotate.d/<nom_application> && ls -l /var/log/<nom_application>/`
   👉 Explication : Force une rotation immédiate pour vérifier la création des fichiers `.1` ou compressés et les droits `0640`.