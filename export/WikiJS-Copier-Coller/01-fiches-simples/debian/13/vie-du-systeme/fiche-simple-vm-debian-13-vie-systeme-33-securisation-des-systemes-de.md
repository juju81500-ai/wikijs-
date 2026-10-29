# Fiche_Simple_-_VM_Debian_13_Vie_Systeme_33_Securisation_Des_Systemes_De

- **Environnement** : VM Debian 13 « trixie » (serveur)
- **OS / Version** : Debian 13; étape 33 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Restreindre les montages.

## 1. Hors-Production (Lab / Test / POC)

1. Debian 13 monte `/tmp` en tmpfs (en mémoire, jusqu'à la moitié de la RAM) : contrôler l'état réel de `/tmp`, `/var/tmp` et `/dev/shm` :
   ```bash
   findmnt -no TARGET,FSTYPE,OPTIONS /tmp /var/tmp /dev/shm
   df -h /tmp
   ```
   👉 Explication : un `/tmp` en `tmpfs` est vidé à chaque redémarrage; un `/var/tmp` absent de la liste est sur le disque racine.

2. Ajouter les options restrictives : `/tmp` via un fichier de surcharge de l'unité de montage (tmpfs), le reste dans `/etc/fstab` :
   ```bash
   sudo systemctl edit tmp.mount
   sudoedit /etc/fstab
   ```
   👉 Explication : dans `tmp.mount`, sous `[Mount]`, mettre `Options=mode=1777,strictatime,nosuid,nodev,noexec`; dans `fstab`, ajouter `nodev,nosuid,noexec` à `/dev/shm` et `/var/tmp` si montés.

3. Tester sans redémarrer :
   ```bash
   sudo systemctl daemon-reload
   sudo mount -o remount /tmp
   sudo findmnt --verify
   ```
   👉 Explication : applique et vérifie; si `/tmp` est sur disque (mise à jour depuis Debian 12), `/tmp` reste un répertoire normal et seul `fstab` s'applique.

## 2. Production — Contrôles

Garder `/var/tmp` exécutable si une application l'exige; dimensionner la RAM pour le tmpfs `/tmp`.

## 3. Production — Sécurité

Une erreur dans `fstab` peut bloquer le démarrage : snapshot avant.

## Validation et retour arrière

- **Validation** : `findmnt --verify` sans erreur.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Debian 13](/01-fiches-simples/debian/13/vie-du-systeme/sommaire-vie-du-systeme-debian-13)
- [Documentation officielle](https://www.debian.org/doc/)