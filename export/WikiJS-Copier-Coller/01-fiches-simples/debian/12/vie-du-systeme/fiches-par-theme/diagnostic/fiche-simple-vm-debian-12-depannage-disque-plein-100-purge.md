# 📄 VM_Debian_12_Depannage_Disque-Plein-100-Purge.md

- **Environnement** : VM / LXC (Debian 12 / Ubuntu / Linux Universel)
- **OS / Version** : Debian 12 (Bookworm) - Famille Debian
- **Catégorie** : Dépannage & Maintenance / Stockage

## 🎯 Problème précis à résoudre
Diagnostiquer un disque système plein à 100%, identifier les répertoires volumineux, purger les journaux système de `systemd-journald` et les anciens noyaux pour rétablir le fonctionnement des services.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Vérification rapide du taux d'occupation des espaces disques :
   `df -h`
   👉 Explication : Affiche l'utilisation en pourcentage de chaque point de montage.
2. Identification immédiate du nombre d'inodes utilisés :
   `df -i`
   👉 Explication : Vérifie si la saturation est due au nombre maximal de fichiers (inodes).

---

## ⚡ 2. Production — Façon Simplifiée
1. Repérer le système de fichiers saturé et les répertoires consommateurs :
   ```bash
   df -hT
   df -i
   sudo du -xhd1 /var 2>/dev/null | sort -h
   ```
   👉 Explication : Distingue saturation de capacité et d'inodes, sans franchir les autres montages.
2. Identifier les fichiers supprimés encore utilisés et la taille des journaux :
   ```bash
   sudo lsof +L1
   journalctl --disk-usage
   ```
   👉 Explication : Recharger le service qui garde un fichier supprimé ouvert, après identification et selon la fenêtre adaptée.
3. Libérer uniquement le cache APT et examiner la simulation de suppression :
   ```bash
   sudo apt clean
   sudo apt autoremove --dry-run
   ```
   👉 Explication : Ne pas confirmer la suppression des paquets sans vérifier chaque élément proposé.
4. Si la rétention le permet, purger les journaux antérieurs à 14 jours puis mesurer de nouveau :
   ```bash
   sudo journalctl --vacuum-time=14d
   journalctl --disk-usage
   ```
   👉 Explication : Vérifier la politique de conservation avant toute purge. Ne jamais supprimer des fichiers inconnus de `/var/lib` ou d'une base de données.

---

## 🔒 3. Production — Prévention et reprise
1. Définir `SystemMaxUse` et `SystemKeepFree` dans la section `[Journal]` de `/etc/systemd/journald.conf`, avec des valeurs dimensionnées selon le volume et la rétention exigée. Sauvegarder le fichier avant édition.
2. Appliquer le changement après validation et contrôler la consommation :
   ```bash
   sudo systemctl restart systemd-journald
   journalctl --disk-usage
   ```
3. Mettre en place des alertes par point de montage et tester les sauvegardes. Une purge libère de l'espace mais ne corrige pas la cause de la croissance.