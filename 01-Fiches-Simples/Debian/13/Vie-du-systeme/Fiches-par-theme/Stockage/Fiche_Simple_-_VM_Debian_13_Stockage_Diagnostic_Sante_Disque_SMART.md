# 📄 Fiche_Simple_-_VM_Debian_13_Stockage_Diagnostic_Sante_Disque_SMART.md

- **Environnement** : VM ou serveur physique; accès direct au périphérique requis
- **OS / Version** : Debian 13 (Trixie)
- **Catégorie** : Stockage / Maintenance
- **Tags** : `[debian13]`, `[debian]`, `[stockage]`, `[smartmontools]`, `[smart]`, `[maintenance]`

## 🎯 Problème précis à résoudre
Installer `smartmontools`, identifier un disque compatible et consulter ses informations de santé sous Debian 13, sans confondre un résultat SMART avec une garantie contre les pannes.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installer l'outil et inventorier les périphériques détectés :
   ```bash
   sudo apt update
   sudo apt install smartmontools
   sudo smartctl --scan-open
   ```
   👉 *Explication : La liste indique les chemins que le noyau expose à SMART; un disque virtuel peut ne pas fournir ces informations.*
2. Remplacer le chemin d'exemple par celui retourné par le scan :
   ```bash
   sudo smartctl --health /dev/sdX
   ```
   👉 *Explication : Cette commande demande le résumé de santé au disque; `/dev/sdX` est un exemple à ne pas copier sans identification.*

## ⚡ 2. Production — Façon Simplifiée
1. Identifier le périphérique stable et consulter les attributs :
   ```bash
   ls -l /dev/disk/by-id/
   sudo smartctl --all /dev/disk/by-id/<identifiant-du-disque>
   ```
2. Activer le démon de surveillance fourni par le paquet :
   ```bash
   sudo systemctl enable --now smartmontools
   sudo systemctl status smartmontools --no-pager
   ```
3. Examiner les journaux après le démarrage :
   ```bash
   sudo journalctl -u smartmontools --since today --no-pager
   ```
   👉 *Explication : Le démon applique les périphériques et contrôles définis dans `/etc/smartd.conf`; vérifier ce fichier et la documentation locale du paquet avant d'ajouter des options ou des alertes.*

## 🔒 3. Production — Façon Sécurisée
1. Ne pas lancer un test SMART long ou destructif pendant une période de forte charge; planifier les autotests et vérifier leur durée selon le modèle du disque.
2. Un état `PASSED` n'exclut pas une panne imminente. Conserver des sauvegardes testées et superviser l'espace, les erreurs d'E/S et les alertes du contrôleur.
3. Dans une VM, consulter également l'hyperviseur ou le stockage sous-jacent : les attributs SMART peuvent être masqués. Dans un LXC, ne pas exposer un disque hôte au conteneur uniquement pour ce diagnostic.

## ✅ Validation et retour arrière
- Comparer `smartctl --health` et `smartctl --all` avec l'identité réelle du disque; confirmer que le démon est actif.
- Si les périphériques ne sont pas exposés, ne pas forcer d'accès : poursuivre la supervision au niveau du matériel ou de l'hyperviseur.
- Pour arrêter la surveillance, utiliser `sudo systemctl disable --now smartmontools`; cela ne modifie pas les données du disque.

## 🔗 Si le problème n'est pas résolu
- Vérifier les messages du noyau avec `journalctl -k` et les erreurs remontées par l'hyperviseur ou le contrôleur de stockage.