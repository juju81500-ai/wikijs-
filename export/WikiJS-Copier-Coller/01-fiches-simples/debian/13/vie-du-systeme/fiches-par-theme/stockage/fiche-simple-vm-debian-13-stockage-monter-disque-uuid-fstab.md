# 📄 Fiche_Simple_-_VM_Debian_13_Stockage_Monter_Disque_UUID_Fstab.md

- **Environnement** : VM ou serveur Debian; disque déjà présenté par l'hyperviseur
- **OS / Version** : Debian 13 (Trixie)
- **Catégorie** : Stockage / Configuration

## 🎯 Problème précis à résoudre
Formater une partition de données explicitement identifiée, la monter de façon persistante par UUID via `/etc/fstab`, puis vérifier la configuration avant redémarrage.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Repérer le disque et la partition; confirmer qu'ils ne contiennent pas de données à conserver :
   ```bash
   lsblk -f
   sudo blkid
   ```
2. **Uniquement sur une partition neuve ou dont l'effacement est autorisé**, créer un système de fichiers ext4 :
   ```bash
   sudo mkfs.ext4 /dev/<partition-de-donnees>
   ```
3. Créer le point de montage, relever l'UUID et monter la partition :
   ```bash
   sudo mkdir -p /srv/data
   sudo blkid /dev/<partition-de-donnees>
   sudo mount UUID=<uuid> /srv/data
   findmnt /srv/data
   ```
   👉 *Explication : `mkfs.ext4` détruit les données présentes sur la partition ciblée. Ne jamais copier le nom d'exemple sans vérifier `lsblk`.*

## ⚡ 2. Production — Façon Simplifiée
1. Sauvegarder les données, puis identifier avec certitude le disque et la partition à utiliser. S'il existe déjà un système de fichiers valide, ne pas le reformater.
2. Récupérer l'UUID et ajouter une ligne dédiée dans `/etc/fstab` :
   ```text
   UUID=<uuid-reel> /srv/data ext4 defaults 0 2
   ```
3. Valider le fichier puis monter les entrées déclarées :
   ```bash
   sudo findmnt --verify --verbose
   sudo mount -a
   findmnt /srv/data
   df -hT /srv/data
   ```
   👉 *Explication : l'UUID reste stable si le nom `/dev/sdX` change; le type `ext4` doit correspondre au système de fichiers réellement présent.*

## 🔒 3. Production — Façon Sécurisée
1. Ne pas appliquer `mkfs` sur un disque existant sans contrôle et sauvegarde restaurable.
2. Si une application dépend du montage, définir les permissions et le propriétaire attendus avant son démarrage; éviter `chmod 777`.
3. Ne pas ajouter `nofail` sans analyser le comportement de l'application si le disque manque au démarrage.

## ✅ Validation et retour arrière
- Confirmer `findmnt --verify`, `findmnt /srv/data` et l'espace avec `df -hT`.
- Pour annuler, sauvegarder puis retirer uniquement la ligne créée dans `/etc/fstab`, et démonter le volume après arrêt des processus qui l'utilisent.
- Ne pas redémarrer si `findmnt --verify` signale une erreur non comprise.