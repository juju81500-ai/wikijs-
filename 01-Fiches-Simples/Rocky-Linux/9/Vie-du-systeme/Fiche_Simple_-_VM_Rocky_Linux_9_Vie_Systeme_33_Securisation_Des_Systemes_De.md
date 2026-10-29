# Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_33_Securisation_Des_Systemes_De

- **Environnement** : VM Rocky Linux 9 (serveur)
- **OS / Version** : Rocky Linux 9; étape 33 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `rocky9`, `vie-du-systeme`, `cycle-de-vie`, `etape-33`

---

## Problème précis à résoudre

Restreindre les montages.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler les options actuelles :
   ```bash
   findmnt -o TARGET,FSTYPE,OPTIONS /tmp /var /home
   ```
   👉 Explication : montre `nodev`, `nosuid`, `noexec`.

2. Ajouter des options dans `/etc/fstab` (exemple pour `/home`) :
   ```bash
   sudo cp /etc/fstab /etc/fstab.bak
   sudo sed -i '/ \/home /s/defaults/defaults,nodev,nosuid/' /etc/fstab
   sudo systemctl daemon-reload
   sudo mount -o remount /home
   ```
   👉 Explication : sauvegarde puis ajoute les options.

3. Vérifier la syntaxe :
   ```bash
   sudo findmnt --verify
   ```
   👉 Explication : détecte les erreurs avant le redémarrage.

## 2. Production — Contrôles

Tester le redémarrage avant de livrer.

## 3. Production — Sécurité

`/tmp` en `nodev,nosuid,noexec` quand les applications le permettent.

## Validation et retour arrière

- **Validation** : `findmnt --verify` ne renvoie aucune erreur.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Rocky Linux 9](./Sommaire_-_Vie_du_systeme_Rocky_Linux_9.md)
- [Documentation officielle](https://docs.rockylinux.org/)
