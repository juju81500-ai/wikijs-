# Fiche_Simple_-_VM_Alpine_3.19_Vie_Systeme_15_Chargeur_D_Amorcage

- **Environnement** : VM Alpine Linux 3.19 (serveur)
- **OS / Version** : Alpine Linux 3.19; étape 15 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `alpine319`, `vie-du-systeme`, `cycle-de-vie`, `etape-15`

---

## Problème précis à résoudre

Vérifier le chargeur installé par `setup-disk` (syslinux en BIOS, GRUB en UEFI).

## 1. Hors-Production (Lab / Test / POC)

1. Repérer le chargeur et le noyau installés :
   ```sh
   ls /boot
   uname -r
   ls /sys/firmware/efi >/dev/null 2>&1 && echo UEFI || echo BIOS
   ```
   👉 Explication : montre les fichiers de démarrage, le noyau actif et le mode de firmware.

2. En BIOS (syslinux/extlinux), lire et régénérer la configuration :
   ```sh
   cat /etc/update-extlinux.conf
   update-extlinux
   ```
   👉 Explication : `default_kernel_opts` contient les options noyau; la commande réécrit `/boot/extlinux.conf`.

3. En UEFI (GRUB), contrôler les entrées et régénérer :
   ```sh
   apk add efibootmgr
   efibootmgr -v
   grub-mkconfig -o /boot/grub/grub.cfg
   ```
   👉 Explication : `efibootmgr` liste les entrées du firmware; `grub-mkconfig` régénère la configuration.

## 2. Production — Contrôles

Conserver la configuration du chargeur avec la documentation de la machine.

## 3. Production — Sécurité

Mettre un mot de passe GRUB sur le matériel physique accessible.

## Validation et retour arrière

- **Validation** : Le système redémarre sans intervention sur le noyau attendu.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Alpine Linux 3.19](./Sommaire_-_Vie_du_systeme_Alpine_3.19.md)
- [Documentation officielle](https://docs.alpinelinux.org/)
