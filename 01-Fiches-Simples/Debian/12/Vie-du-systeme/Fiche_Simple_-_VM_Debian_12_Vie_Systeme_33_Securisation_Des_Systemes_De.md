# Fiche_Simple_-_VM_Debian_12_Vie_Systeme_33_Securisation_Des_Systemes_De

- **Environnement** : VM Debian 12 « bookworm » (serveur)
- **OS / Version** : Debian 12; étape 33 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `debian12`, `vie-du-systeme`, `cycle-de-vie`, `etape-33`

---

## Problème précis à résoudre

Restreindre les montages.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler et éditer `/etc/fstab` :
   ```bash
   findmnt -no TARGET,OPTIONS /tmp /var/tmp /dev/shm
   sudoedit /etc/fstab
   ```
   👉 Explication : ajouter `nodev,nosuid,noexec` à `/tmp`, `/var/tmp`, `/dev/shm`.

2. Tester sans redémarrer :
   ```bash
   sudo mount -o remount /tmp
   sudo findmnt --verify
   ```
   👉 Explication : applique et vérifie `fstab`.

## 2. Production — Contrôles

Garder `/var/tmp` exécutable si une application l'exige.

## 3. Production — Sécurité

Une erreur dans `fstab` peut bloquer le démarrage : snapshot avant.

## Validation et retour arrière

- **Validation** : `findmnt --verify` sans erreur.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Debian 12](./Sommaire_-_Vie_du_systeme_Debian_12.md)
- [Documentation officielle](https://www.debian.org/doc/)
