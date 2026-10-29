# 📄 VM_Debian_13_Automatisation_Configuration-Unattended-Upgrades.md

- **Environnement** : VM / LXC (Debian 13)
- **OS / Version** : Debian 13 (Trixie) - Famille Debian
- **Catégorie** : Maintenance & Automatisation / Updates

## 🎯 Problème précis à résoudre
Automatiser l'installation silencieuse des correctifs de sécurité critiques sous Debian 13 avec `unattended-upgrades`, configurer les notifications par e-mail et planifier les redémarrages automatiques contrôlés.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation du paquet unattended-upgrades :
   `apt-get update && apt-get install -y unattended-upgrades dpkg-dev`
   👉 Explication : Télécharge et installe le gestionnaire de mises à jour automatiques Debian.

2. Test à blanc de la procédure de mise à jour :
   `unattended-upgrade --dry-run --debug`
   👉 Explication : Simule l'exécution du processus pour vérifier les paquets éligibles sans modifier le système.

---

## ⚡ 2. Production — Façon Simplifiée
1. Activation de la planification automatique systemd :
   `dpkg-reconfigure -f noninteractive unattended-upgrades`
   👉 Explication : Activer le timer quotidien d'exécution des mises à jour de sécurité.

2. Restriction des canaux de mises à jour dans `/etc/apt/apt.conf.d/50unattended-upgrades` :
   `sed -i 's#//\s*"origin=Debian,codename=${distro_codename}-security";#"origin=Debian,codename=${distro_codename}-security";#' /etc/apt/apt.conf.d/50unattended-upgrades`
   👉 Explication : Limite les installations automatiques aux seuls correctifs de sécurité officiels Debian.

3. Contrôle du statut du timer système :
   `systemctl status apt-daily-upgrade.timer`
   👉 Explication : Confirme la bonne planification de l'exécution automatique.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Configuration des alertes mail et de la purge automatique des paquets inutilisés :
   `echo -e 'Unattended-Upgrade::Mail "admin@lab.local";\nUnattended-Upgrade::MailReport "on-change";\nUnattended-Upgrade::Remove-Unused-Dependencies "true";' >> /etc/apt/apt.conf.d/50unattended-upgrades`
   👉 Explication : Notifie l'équipe d'administration à chaque mise à jour et nettoye automatiquement les dépendances orphelines.

2. Planification des redémarrages automatiques contrôlés à 03h30 :
   `echo -e 'Unattended-Upgrade::Automatic-Reboot "true";\nUnattended-Upgrade::Automatic-Reboot-Time "03:30";' >> /etc/apt/apt.conf.d/50unattended-upgrades`
   👉 Explication : Applique les mises à jour de noyau et redémarre le serveur dans la fenêtre de maintenance nocturne.

3. Vérification des journaux d'exécution des mises à jour :
   `cat /var/log/unattended-upgrades/unattended-upgrades.log`
   👉 Explication : Permet de vérifier l'historique complet des paquets mis à jour et des redémarrages effectués.