---
title: "Fichiers et dossiers sous Linux"
description: "- Une seule racine : /"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# Fichiers et dossiers sous Linux

## 🌲 Arborescence de fichiers sous Linux

### 🔗 Caractéristiques générales

- Une **seule racine** : `/`
- Tout est fichier (y compris périphériques et répertoires)
- Accès via chemins **absolus** ou **relatifs**

### 📂 Répertoires spéciaux

|Répertoire|Usage principal|
|---|---|
|`/home`|Répertoires utilisateurs (sauf root)|
|`/root`|Répertoire personnel du superutilisateur|
|`/etc`|Fichiers de configuration|
|`/bin`, `/usr/bin`|Commandes utilisateurs|
|`/sbin`, `/usr/sbin`|Commandes administratives|
|`/lib`, `/usr/lib`|Librairies système|
|`/var`, `/var/log`|Données variables, logs|
|`/media`, `/mnt`|Points de montage (disques, USB...)|
|`/proc`, `/sys`|Infos système, noyau et périphériques|

---

## 🚶 Navigation dans les dossiers

### Commandes utiles

```bash
cd <chemin>        # Se déplacer
cd ..              # Dossier parent
cd -              # Dossier précédent
cd ~              # Vers /home/utilisateur
pwd               # Affiche le répertoire courant
```

### Variables utiles

- `$HOME` : répertoire personnel
- `.` : dossier courant
- `..` : dossier parent

---

## 🧰 Gestion des dossiers

### Créer un dossier

```bash
mkdir nom_dossier
mkdir -p -v chemin/vers/sousdossier
```

### Supprimer un dossier

```bash
rmdir dossier_vide
rm -rv dossier_non_vide
rm -rf dossier_dangereux  # ⚠️ Supprime sans confirmation
```

---

## 📄 Manipulation de fichiers

### Créer un fichier vide ou modifier la date

```bash
touch fichier.txt
```

### Copier

```bash
cp source.txt destination.txt
cp -rpv source1 source2 dossier_cible/
```

### Déplacer / Renommer

```bash
mv fichier.txt /tmp/
mv ancien_nom.txt nouveau_nom.txt
```

### Supprimer

```bash
rm fichier.txt
rm -rf dossier/
```

---

## 📋 Affichage et listing

### Liste simple ou détaillée

```bash
ls                # Liste simple
ls -l             # Liste détaillée
ls -lh            # Tailles lisibles
ls -lt            # Tri par date
ls -A             # Inclut fichiers cachés (sauf . et ..)
ls -ld dossier    # Infos sur le dossier lui-même
```

### Types de fichiers

|Caractère|Type|
|---|---|
|`-`|Fichier normal|
|`d`|Dossier|
|`l`|Lien symbolique|
|`b`|Périphérique bloc|
|`c`|Périphérique caractère|
|`p`|Pipe|
|`s`|Socket|

---

## ✨ Métacaractères et expansions Bash

### 🧪 Métacaractères simples

|Caractère|Rôle|
|---|---|
|`*`|Remplace 0 ou plusieurs caractères|
|`?`|Remplace un seul caractère|
|`[abc]`|Un caractère parmi a, b ou c|
|`[a-z]`|Plage de caractères|
|`[^t]` ou `[!t]`|Exclut le caractère t|

### 🧪 Métacaractères étendus (extglob)

- `?(pattern)` : 0 ou 1 fois
- `*(pattern)` : 0 à n fois
- `+(pattern)` : 1 à n fois
- `@(pattern)` : exactement 1 fois
- `!(pattern)` : tout sauf

> 🔧 Activer extglob si besoin : `shopt -s extglob`

### 🧪 Accolades

```bash
mkdir -v {img,video,doc}
ls *.txt
ls tel20[0-9][0-9]
ls images/*.{jpg,png,gif}
```

### 🧪 Caractères spéciaux

|Caractère|Fonction|
|---|---|
|`'`|Ignore tout traitement spécial|
|`"`|Ignore sauf $, \ et `|
|`\`|Échappe un caractère|
|`$`|Référence une variable|
|`$(cmd)`|Résultat de la commande|
|`` `cmd` ``|Idem (déprécié)|

---

## ✅ À retenir pour les révisions

- L’arborescence Linux est standardisée : **FHS**
- Utilisez `pwd`, `cd`, `mkdir`, `rmdir`, `ls`, `touch`, `mv`, `cp`, `rm`
- Comprendre les métacaractères permet d’automatiser des tâches complexes
- Attention à `rm -rf`, commande très dangereuse ⚠️

---

## 📌 Bonnes pratiques professionnelles

- Toujours vérifier le chemin avant un `rm -rf`
- Utiliser `-i` (interactif) pour les suppressions sensibles
- Préférer `ls -lh` pour une lecture humaine
- Exploiter les métacaractères pour gagner du temps
- Tester les commandes de recherche avec `ls` avant de les appliquer avec `rm` ou `mv`

---

## 🔗 Liens utiles

- [FHS – Filesystem Hierarchy Standard](https://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html)