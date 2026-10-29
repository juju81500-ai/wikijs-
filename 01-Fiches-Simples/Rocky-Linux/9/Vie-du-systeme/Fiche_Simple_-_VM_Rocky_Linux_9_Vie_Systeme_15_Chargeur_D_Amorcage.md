# Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_15_Chargeur_D_Amorcage

- **Environnement** : VM Rocky Linux 9 (serveur)
- **OS / Version** : Rocky Linux 9; étape 15 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `rocky9`, `vie-du-systeme`, `cycle-de-vie`, `etape-15`

---

## Problème précis à résoudre

Contrôler GRUB2 et l'amorçage.

## 1. Hors-Production (Lab / Test / POC)

1. Lister les noyaux et l'entrée par défaut :
   ```bash
   sudo grubby --default-kernel
   sudo grubby --info=ALL | grep -E '^(kernel|args)'
   ```
   👉 Explication : montre les noyaux installés et leurs arguments.

2. Régénérer la configuration si besoin :
   ```bash
   sudo grub2-mkconfig -o /boot/grub2/grub.cfg
   ```
   👉 Explication : en UEFI, le fichier est `/boot/efi/EFI/rocky/grub.cfg`.

3. Contrôler le mode UEFI :
   ```bash
   efibootmgr -v
   ```
   👉 Explication : confirme l'entrée de démarrage Rocky.

## 2. Production — Contrôles

Conserver au moins deux noyaux.

## 3. Production — Sécurité

Protéger GRUB par mot de passe (`grub2-setpassword`) sur du matériel physique.

## Validation et retour arrière

- **Validation** : La machine redémarre sur le noyau voulu.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Rocky Linux 9](./Sommaire_-_Vie_du_systeme_Rocky_Linux_9.md)
- [Documentation officielle](https://docs.rockylinux.org/)
