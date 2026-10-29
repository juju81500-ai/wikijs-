# 📄 Fiche_Simple_-_VM_Ubuntu_26.04_Stockage_Fstab_Options

- **Environnement** : VM ou serveur Ubuntu avec disque de données supplémentaire
- **OS / Version** : Ubuntu Server 26.04 LTS
- **Catégorie** : Stockage / Montages et options

---

## 🎯 Problème précis à résoudre

Monter un disque de données de façon persistante via son UUID dans `/etc/fstab`, avec des options de sécurité (`nodev`, `nosuid`, `noexec` selon l'usage) sans bloquer le démarrage si le disque est absent.

## 🧪 1. Hors-Production (Lab / Test / POC)

1. Identifier le disque et son UUID :
```bash
lsblk -f
```
👉 Explication : Affiche les partitions, leur système de fichiers et leur UUID. Repérer l'UUID du disque cible plutôt que `/dev/sdb1`, dont le nom peut changer au redémarrage.

2. Créer le système de fichiers si le disque est neuf (à ne faire que sur un disque vide) :
```bash
sudo mkfs.ext4 -L donnees /dev/<peripherique>
```
👉 Explication : Crée un ext4 étiqueté `donnees`. La commande détruit toutes les données du périphérique : ne jamais la lancer sur un disque utilisé.

3. Créer le point de montage et monter manuellement pour tester :
```bash
sudo mkdir -p /srv/donnees
sudo mount /dev/<peripherique> /srv/donnees
findmnt /srv/donnees
```
👉 Explication : Valide que le disque se monte avant toute modification du fichier `fstab`.

4. Ajouter la ligne persistante dans `/etc/fstab` :
```text
UUID=<uuid_du_disque>  /srv/donnees  ext4  defaults,nodev,nosuid,nofail  0  2
```
👉 Explication : `nodev` interdit les fichiers spéciaux, `nosuid` ignore les bits SUID. `nofail` permet au démarrage de continuer si le disque manque. Le dernier champ `2` demande une vérification fsck après la racine.

## ⚡ 2. Production — Façon Simplifiée

1. Vérifier la syntaxe du fichier avant tout redémarrage :
```bash
sudo findmnt --verify --verbose
```
👉 Explication : Contrôle chaque ligne de `/etc/fstab` (UUID existant, point de montage, options). Une erreur ici peut bloquer le démarrage en mode de secours.

2. Recharger systemd et monter tout le fstab :
```bash
sudo systemctl daemon-reload
sudo mount -a
```
👉 Explication : systemd génère les unités de montage depuis `fstab` ; sans `daemon-reload`, il affiche un avertissement et peut utiliser l'ancienne version. `mount -a` monte les entrées non encore montées.

## 🔒 3. Production — Façon Sécurisée

1. Durcir `/dev/shm` dans `/etc/fstab` (monté par défaut par systemd) :
```text
tmpfs  /dev/shm  tmpfs  defaults,nodev,nosuid,noexec  0  0
```
👉 Explication : Empêche l'exécution de binaires depuis la mémoire partagée, technique courante dans les charges utiles d'attaquants. Tester les applications qui utilisent `/dev/shm` (PostgreSQL, navigateurs headless) avant de l'appliquer.

2. Interdire l'exécution sur un répertoire de données qui ne contient que des fichiers :
```text
UUID=<uuid_du_disque>  /srv/donnees  ext4  defaults,nodev,nosuid,noexec,nofail  0  2
```
👉 Explication : `noexec` empêche de lancer un script déposé dans ce répertoire. Ne pas l'ajouter si l'application doit exécuter des binaires à partir de ce chemin.

3. Vérifier les options réellement appliquées :
```bash
findmnt -o TARGET,SOURCE,FSTYPE,OPTIONS /srv/donnees
```
👉 Explication : Les options affichées doivent contenir `nodev,nosuid,noexec`. Une option absente indique qu'une ligne fstab est ignorée ou remplacée.

## ✅ Validation et retour arrière

- **Précontrôles** : console de secours, UUID vérifié avec `lsblk -f`, copie de `/etc/fstab` (`sudo cp -a /etc/fstab /etc/fstab.bak-$(date +%F)`).
- **Validation** : `findmnt --verify` sans erreur ; `findmnt /srv/donnees` affiche les options attendues ; un redémarrage remonte le disque.
- **Retour arrière** : restaurer `/etc/fstab` depuis la copie, `sudo systemctl daemon-reload`, puis `sudo umount /srv/donnees` si nécessaire.