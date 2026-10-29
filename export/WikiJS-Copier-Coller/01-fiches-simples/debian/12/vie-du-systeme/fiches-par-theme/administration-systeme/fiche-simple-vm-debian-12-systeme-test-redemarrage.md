# 📄 VM_Debian_12_Systeme_Test-Redemarrage.md

- **Environnement** : VM (Proxmox VE / KVM)
- **OS / Version** : Debian 12 (Bookworm) - Famille Debian
- **Catégorie** : Système & Exploitation / Test de persistance au redémarrage

## 🎯 Problème précis à résoudre
Vérifier qu'un serveur Debian 12 redémarre proprement et que tous ses éléments persistants reviennent seuls : montages `/etc/fstab`, pile réseau, horloge, pare-feu, SSH et services métier, sans unité systemd en échec.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. État du système avant redémarrage :
   `systemctl is-system-running`
   👉 Explication : Doit renvoyer `running`. Une valeur `degraded` signifie qu'une unité est déjà en échec et doit être corrigée avant le test.
2. Vérification des unités en échec :
   `systemctl --failed`
   👉 Explication : Établit la référence de départ pour comparer après le redémarrage.
3. Contrôle du fichier de montages :
   `sudo findmnt --verify --verbose`
   👉 Explication : Détecte une ligne `fstab` erronée avant qu'elle ne bloque le démarrage.

---

## ⚡ 2. Production — Façon Simplifiée
1. Redémarrage propre de la machine :
   `sudo systemctl reboot`
   👉 Explication : Demande un arrêt ordonné de tous les services puis redémarre le système.
2. Contrôle de l'heure du dernier démarrage :
   `uptime -s`
   👉 Explication : Confirme que la machine a bien redémarré à l'heure attendue.
3. Contrôle des unités en échec après démarrage :
   `systemctl --failed`
   👉 Explication : Doit afficher `0 loaded units listed`, comme avant le test.

---

## 🔒 3. Production — Façon Sécurisée (Fenêtre de maintenance & Services métier)
1. Redémarrage planifié avec préavis :
   `sudo shutdown -r +2 "Redémarrage de test planifié"`
   👉 Explication : Laisse deux minutes aux utilisateurs connectés ; prérequis : sauvegarde récente vérifiée et accès console disponible.
2. Contrôle des services critiques après redémarrage :
   `systemctl is-active ssh nftables chrony`
   👉 Explication : Chaque service doit afficher `active`. Adapter la liste aux services réellement déployés sur la machine.
3. Contrôle des montages et de la durée de démarrage :
   `findmnt -t ext4,xfs,tmpfs -o TARGET,SOURCE,OPTIONS && systemd-analyze time`
   👉 Explication : Vérifie que les systèmes de fichiers attendus sont montés avec leurs options et mesure le temps de démarrage pour détecter une régression.