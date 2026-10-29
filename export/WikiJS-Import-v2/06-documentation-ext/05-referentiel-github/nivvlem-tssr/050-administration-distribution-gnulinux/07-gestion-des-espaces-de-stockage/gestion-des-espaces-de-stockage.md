---
title: "Gestion des espaces de stockage (Debian GNU/Linux)"
description: "- Taille max par partition : 2,2 To"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# Gestion des espaces de stockage (Debian GNU/Linux)

## 🧱 Concepts fondamentaux

### 🧭 MBR (Master Boot Record)

- **Ancien standard** limité à 4 partitions primaires (ou 3 + 1 étendue)
- Taille max par partition : **2,2 To**
- Table de partitions : 64 octets

### 🧭 GPT (GUID Partition Table)

- Nouveau standard remplaçant MBR
- Jusqu’à **128 partitions** (voire plus)
- Taille maximale théorique : **9,4 Zo**

---

## 📁 Nommage des disques sous Linux

- Disques SATA/SCSI/IDE : `/dev/sdX`
    - `/dev/sda` → premier disque
    - `/dev/sdb` → deuxième disque, etc.
- Partitions : `/dev/sdXN`
    - N = numéro de partition (1 à 4 = primaires/étendue, ≥ 5 = logiques)

### Exemple de partitionnement

```
/dev/sdb      → disque entier
/dev/sdb1     → partition principale
/dev/sdb2     → 2e partition principale
/dev/sdb3     → partition étendue
/dev/sdb5-7   → partitions logiques dans l’étendue
```

---

## ⚙️ Outil : `fdisk`

### 🔍 Lister la table de partition

```bash
fdisk -l /dev/sda
```

### ➕ Créer une nouvelle partition

```bash
fdisk /dev/sdb
```

Puis dans le menu interactif :

- `n` → nouvelle partition
- `p` → primaire ou `e` → étendue
- `1` → numéro de partition
- `+20G` → taille
- `t` → type (ex : `83` pour Linux, `8e` pour LVM)
- `w` → écrire la table et quitter

### 🔍 Aide dans fdisk

```bash
m  # affiche l’aide
```

---

## 🧾 Codes de type de partition (extraits)

|Code|Type|
|---|---|
|83|Linux standard|
|82|Partition swap|
|8e|Linux LVM|
|7|NTFS / exFAT / HPFS|

> Utiliser `t` dans `fdisk` pour modifier le type, `L` pour lister tous les codes

---

## ✅ À retenir pour les révisions

- Linux reconnaît automatiquement les disques via `/dev/sdX`
- Le standard **GPT** est à privilégier aujourd’hui, mais **fdisk** ne gère que le MBR
- Les **partitions logiques** commencent toujours à 5
- Utiliser `fdisk` avec précaution : les modifications sont prises en compte **seulement après `w`**

---

## 📌 Bonnes pratiques professionnelles

- Toujours sauvegarder avant de modifier une table de partition
- Préférer **`parted` ou `gparted`** pour les disques GPT (fdisk est limité)
- Documenter la structure de partitionnement d’un système serveur
- Penser à `mkfs`, `mount`, `blkid`, etc., pour compléter le travail de partitionnement

---

## 🔗 Commandes utiles

```bash
fdisk -l                     # Lister les partitions
fdisk /dev/sdX              # Modifier un disque
m                           # Affiche l’aide (dans fdisk)
t                           # Changer le type
w                           # Sauvegarder et quitter
```

## Ressources complémentaires

- [https://wiki.debian.org/Partitioning](https://wiki.debian.org/Partitioning)