# Fiche_Simple_-_VM_Alpine_3.19_Vie_Systeme_13_Partitionnement_Et_Systemes_De

- **Environnement** : VM Alpine Linux 3.19 (serveur)
- **OS / Version** : Alpine Linux 3.19; étape 13 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Choisir le mode d'installation (sys, data, diskless) et préparer les disques (LVM, ext4).

## 1. Hors-Production (Lab / Test / POC)

1. Identifier le disque cible (remplacer `DISQUE`, par exemple `vda` ou `sda`) :
   ```sh
   lsblk -o NAME,SIZE,TYPE,MOUNTPOINT
   ```
   👉 Explication : repère le disque à effacer sans se tromper de périphérique.

2. Installer en mode `sys` sur LVM (opération destructrice pour DISQUE) :
   ```sh
   setup-disk -m sys -L /dev/DISQUE
   ```
   👉 Explication : `sys` installe le système sur disque avec persistance complète; `-L` crée des volumes LVM (racine, swap, `/boot` séparé); `data` ne ferait que préparer un disque de données et le mode `diskless` charge tout en RAM, avec `lbu` pour sauvegarder la configuration.

3. Vérifier les volumes et les systèmes de fichiers créés :
   ```sh
   pvs
   vgs
   lvs
   df -hT
   ```
   👉 Explication : montre le volume physique, le groupe, les volumes logiques et les types (`ext4`).

## 2. Production — Contrôles

Séparer les données applicatives sur un volume dédié, extensible avec LVM.

## 3. Production — Sécurité

Prévoir `nodev,nosuid,noexec` sur les volumes de données quand c'est possible (étape 33).

## Validation et retour arrière

- **Validation** : `lsblk` et `df -hT` correspondent au plan de partitionnement.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Alpine Linux 3.19](/01-fiches-simples/alpine/3-19/vie-du-systeme/sommaire-vie-du-systeme-alpine-3-19)
- [Documentation officielle](https://docs.alpinelinux.org/)