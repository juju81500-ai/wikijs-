# Fiche_Simple_-_VM_Ubuntu_26.04_Vie_Systeme_33_Securisation_Des_Systemes_De

- **Environnement** : VM Ubuntu Server 26.04 LTS
- **OS / Version** : Ubuntu 26.04; étape 33 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Restreindre les montages.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler et éditer `/etc/fstab` :
   ```bash
   findmnt -no TARGET,FSTYPE,OPTIONS /tmp /var/tmp /dev/shm
   sudoedit /etc/fstab
   ```
   👉 Explication : ajouter `nodev,nosuid,noexec` à `/dev/shm`, et si `/tmp` est sur le disque racine, une ligne `tmpfs /tmp tmpfs defaults,nodev,nosuid,noexec,mode=1777 0 0` (contenu vidé à chaque redémarrage).

2. Tester sans redémarrer :
   ```bash
   sudo systemctl daemon-reload
   sudo mount -o remount /dev/shm
   sudo findmnt --verify
   ```
   👉 Explication : applique et vérifie `fstab`.

## 2. Production — Contrôles

Garder `/var/tmp` exécutable si une application l'exige (installations de paquets).

## 3. Production — Sécurité

Une erreur dans `fstab` peut bloquer le démarrage : snapshot avant.

## Validation et retour arrière

- **Validation** : `findmnt --verify` sans erreur.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Ubuntu 26.04](/01-fiches-simples/ubuntu/26-04/vie-du-systeme/sommaire-vie-du-systeme-ubuntu-26-04)
- [Documentation officielle](https://documentation.ubuntu.com/server/)