# Fiche_Simple_-_VM_Debian_12_Vie_Systeme_15_Chargeur_D_Amorcage

- **Environnement** : VM Debian 12 « bookworm » (serveur)
- **OS / Version** : Debian 12; étape 15 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Vérifier GRUB.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler le chargeur :
   ```bash
   ls /boot/efi/EFI 2>/dev/null
   sudo grub-install --version
   grep -E 'GRUB_TIMEOUT|GRUB_CMDLINE' /etc/default/grub
   ```
   👉 Explication : montre l'entrée EFI et les options noyau.

2. Appliquer un changement de `/etc/default/grub` :
   ```bash
   sudo update-grub
   ```
   👉 Explication : régénère `/boot/grub/grub.cfg`.

## 2. Production — Contrôles

Garder une console de secours avant de modifier GRUB.

## 3. Production — Sécurité

Protéger GRUB par mot de passe si l'accès physique est possible.

## Validation et retour arrière

- **Validation** : Redémarrage réussi après `update-grub`.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Debian 12](/01-fiches-simples/debian/12/vie-du-systeme/sommaire-vie-du-systeme-debian-12)
- [Documentation officielle](https://www.debian.org/doc/)