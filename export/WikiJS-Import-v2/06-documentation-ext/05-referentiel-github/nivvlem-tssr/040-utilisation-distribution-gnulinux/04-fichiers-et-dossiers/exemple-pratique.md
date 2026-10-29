---
title: "TP 1 – Manipulation de fichiers et dossiers sous Linux"
description: "pwd"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# TP 1 – Manipulation de fichiers et dossiers sous Linux

## 🧱 Étapes détaillées

### 📍 1. Vérifier le répertoire courant

```bash
pwd
```

### 📁 2. Vérifier le contenu du répertoire (y compris fichiers cachés)

```bash
ls -A
```

### 📄 3. Créer un fichier vide nommé `MonPremierFichier`

```bash
touch MonPremierFichier
```

### 🔐 4. Afficher les permissions et propriétaires du fichier

```bash
ls -l MonPremierFichier
```

### ⚙️ 5. Afficher tous les fichiers `.conf` dans `/etc`

```bash
ls /etc/*.conf
```

### 🧾 6. Afficher les attributs du répertoire `/tmp` (sans lister le contenu)

```bash
ls -ld /tmp
```

---

## ✅ À retenir pour les révisions

- `pwd` indique le répertoire courant
- `ls -A` liste tous les fichiers sauf `.` et `..`
- `touch` crée un fichier vide ou met à jour un fichier
- `ls -l` affiche les droits, propriétaires et taille

---

## 📌 Bonnes pratiques professionnelles

- Vérifier le chemin courant avant d’exécuter des commandes sensibles
- Systématiquement consulter les options via `man` ou `--help`
- Ne jamais supprimer ou manipuler un fichier système sans certitude

---

# TP 2 – Métacaractères et arborescence avancée

## 🧱 Étapes détaillées

### 🔎 1. Afficher les éléments de `/etc` commençant par a, b, c ou d

```bash
ls -d /etc/[a-d]*
```

### 🏗️ 2. Créer une arborescence complète

```bash
mkdir -p bin Tp/{Bourne,KornShell,Divers/{Sources,lib,Executables}}
```

### 📌 3. Créer un fichier contenant un astérisque dans le nom

```bash
cd Tp/Divers/Sources/
touch fic\*ier
```

### ❌ 4. Tenter de supprimer un répertoire non vide avec `rmdir`

```bash
rmdir Tp/Divers/Sources/  # Échoue car répertoire non vide
```

### 🧹 5. Supprimer un répertoire avec `rm`

```bash
rm -r Tp/Divers/
```

### 🧮 6. Afficher des fichiers très spécifiques dans `/etc`

```bash
cd ~
ls -ld /etc/[!aeiouyAEIOUY][a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z][f-sF-S].conf
```

---

## ✅ À retenir pour les révisions

- `*` = tout caractère, `?` = un seul caractère, `[]` = liste, `[!...]` = exclusion
- `mkdir -p` crée une hiérarchie complète
- Pour manipuler des noms contenant des caractères spéciaux, il faut les échapper (`\*`)
- `rm -r` permet de supprimer un répertoire non vide

---

## 📌 Bonnes pratiques professionnelles

- Toujours tester avec `ls` avant de faire un `rm` ou `mv`
- Éviter les noms de fichiers contenant des caractères spéciaux sauf si nécessaire
- Nettoyer les arborescences de test après usage
- Utiliser des noms cohérents et explicites

---

## 🔗 Ressources utiles

- [LinuxCommand.org – Wildcards](http://linuxcommand.org/lc3_lts0080.php)