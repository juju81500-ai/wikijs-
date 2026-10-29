# Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_13_Partitionnement_Et_Systemes_De

- **Environnement** : VM Rocky Linux 9 (serveur)
- **OS / Version** : Rocky Linux 9; étape 13 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Découper le disque de façon extensible.

## 1. Hors-Production (Lab / Test / POC)

1. Dans anaconda, choisir un partitionnement personnalisé LVM avec XFS :
   👉 Explication : `/boot` (1 Gio), `/boot/efi` en UEFI, puis LVM pour `/`, `/var`, `/home`, swap.

2. Contrôler le résultat :
   ```bash
   lsblk -f
   sudo vgs
   sudo lvs
   df -hT
   ```
   👉 Explication : montre groupe de volumes, volumes logiques et système de fichiers XFS.

3. Laisser de l'espace libre dans le groupe de volumes :
   ```bash
   sudo vgs -o vg_name,vg_free
   ```
   👉 Explication : permet d'agrandir plus tard sans repartitionner.

## 2. Production — Contrôles

Séparer `/var` et les données; prévoir de la marge.

## 3. Production — Sécurité

Options `nodev,nosuid,noexec` sur les volumes de données quand c'est possible.

## Validation et retour arrière

- **Validation** : Disposition conforme et espace libre disponible.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Rocky Linux 9](/01-fiches-simples/rocky-linux/9/vie-du-systeme/sommaire-vie-du-systeme-rocky-linux-9)
- [Documentation officielle](https://docs.rockylinux.org/)