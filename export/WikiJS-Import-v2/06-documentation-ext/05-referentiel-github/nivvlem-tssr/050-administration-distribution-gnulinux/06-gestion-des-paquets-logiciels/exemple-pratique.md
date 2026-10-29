---
title: "TP – Gestion des paquets logiciels"
description: "- Vérifier les dépôts activés dans l’onglet Debian Software"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# TP – Gestion des paquets logiciels
# 🧱 Partie 1 – Avec interface graphique (Debian Desktop)

### 📋 1. Logiciel « Logiciels & mises à jour » (Software & Updates)

- Vérifier les dépôts activés dans l’onglet _Debian Software_
    - Activer/désactiver `main`, `contrib`, `non-free`
- Vérifier la présence des mises à jour dans l’onglet _Updates_ :
    - `bullseye-security`, `bullseye-updates`
- Désactiver le dépôt `cdrom` si présent

### 📁 2. Vérifier `/etc/apt/sources.list`

```bash
sudo vi /etc/apt/sources.list
```

- Lignes commençant par `deb` = paquets binaires
- Lignes `deb-src` = paquets sources (désactiver si inutiles)

Pour commenter toutes les sources :

```vim
:g/^deb-src/s/^/#
```

### 🔁 3. Mise à jour

```bash
sudo apt update
sudo apt upgrade
```

### 🧰 4. Installation de logiciels

```bash
sudo apt install vim terminator
sudo apt install openssh-server
```

### 📑 5. Informations sur les paquets

```bash
apt show <nom>
dpkg -L <nom>
```

### 🧳 6. Connexion depuis un autre poste

- Utiliser **PuTTY** : [https://the.earth.li/~sgtatham/putty/latest/w64/putty.exe](https://the.earth.li/~sgtatham/putty/latest/w64/putty.exe)
- Se connecter à l’IP de la VM

---

# 🧱 Partie 2 – Sans interface graphique (Debian Server)

### 📁 1. Modifier les dépôts dans `/etc/apt/sources.list`

```ini
deb http://ftp.fr.debian.org/debian/ bullseye main
deb http://ftp.fr.debian.org/debian/ bullseye-updates main
deb http://security.debian.org/debian-security bullseye-security main
```

### 🔄 2. Mise à jour et redémarrage si nécessaire

```bash
sudo apt update
sudo apt upgrade
```

### 🔧 3. Installer des outils complémentaires

```bash
sudo apt install vim cifs-utils
```

### 🎨 4. Configuration de vim

#### Modifier `/etc/vim/vimrc`

- Décommenter :

```vim
syntax on
```

#### Créer `/etc/vim/vimrc.local`

```vim
source /usr/share/vim/vim82/defaults.vim
let skip_defaults_vim = 1
if has('mouse')
  set mouse=r
endif
set paste
```

> 📌 Adapter `vim82` selon la version trouvée dans `/usr/share/vim/`

---

## ✅ À retenir pour les révisions

- `apt update`, `upgrade`, `install`, `show`, `purge`, `clean` sont les commandes de base
- `dpkg -L` liste les fichiers installés par paquet
- `sources.list` définit les dépôts utilisés
- Le dépôt CDROM est inutile une fois Debian installé
- Vim peut être adapté pour un confort maximal via `vimrc.local`

---

## 📌 Bonnes pratiques professionnelles

- Ne jamais modifier `sources.list` sans en garder une copie
- Toujours commenter les lignes inutiles (`deb-src`, `cdrom`…)
- Utiliser `apt search` pour identifier les paquets à installer
- Tester les services (SSH, partage CIFS) après installation

---

## 🔗 Commandes utiles

```bash
apt update && apt upgrade
apt install nom
apt show nom
apt search expression
apt clean

dpkg -L nom
vi /etc/apt/sources.list
vi /etc/vim/vimrc
vi /etc/vim/vimrc.local
```

## Ressources complémentaires

- [Cheat.sh – apt & dpkg](https://cheat.sh/apt)