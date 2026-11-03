---
title: "Gestion des paquets logiciels (Debian GNU/Linux)"
description: "Exemple :"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# Gestion des paquets logiciels (Debian GNU/Linux)

## 📦 Branches (releases) Debian

### Principales branches

|Nom|Description|
|---|---|
|stable|Version de production recommandée|
|testing|Future version stable (pré-prod)|
|unstable (sid)|Rolling release, instable|

### Branches secondaires

|Nom|Description|
|---|---|
|old-stable|Version stable précédente|
|old-old-stable|Encore plus ancienne|
|experimental|Développement, instable, partiel|

---

## 🌐 Dépôts Debian

### 📁 Fichier principal : `/etc/apt/sources.list`

Exemple :

```ini
deb http://ftp.fr.debian.org/debian/ buster main contrib
```

### Signification des champs

- `deb` / `deb-src` : paquets binaires / sources
- `http://` : protocole d’accès (http, ftp, file, cdrom)
- `buster` : branche (buster, stable, testing...)
- `main`, `contrib`, `non-free` : section

> Les fichiers additionnels peuvent être ajoutés dans `/etc/apt/sources.list.d/`

---

## 🔧 Commandes apt & apt-get

### 🔁 Mise à jour et montée en version

```bash
apt update               # Met à jour la liste des paquets
apt upgrade              # Met à jour les paquets installés
apt full-upgrade         # Idem + supprime obsolètes (≃ dist-upgrade)
```

### 📦 Installation et suppression

```bash
apt install nom-paquet
apt remove nom-paquet            # Supprime
apt purge nom-paquet             # Supprime + fichiers de config
```

### 🔍 Recherche et info

```bash
apt search regex
apt show nom-paquet
apt clean                        # Vide le cache local
```

---

## ⚙️ dpkg – gestion de bas niveau

### 🧰 Commandes utiles

```bash
dpkg -l '*ftp*'        # Liste les paquets installés filtrés

# Liste les fichiers installés par un paquet
 dpkg -L nom-paquet

# Retrouver quel paquet a installé un fichier
 dpkg -S /chemin/fichier
```

### 📁 Journaux système

|Outil|Fichier log|
|---|---|
|apt/apt-get|`/var/log/apt/history.log`|
|dpkg|`/var/log/dpkg.log`|

---

## 🛠️ Installer depuis les sources (compilation)

### 📦 Étapes typiques

1. Créer un dossier (ex : `/opt/sources/`)
2. Télécharger et extraire les sources
3. Lire le fichier `README` ou `INSTALL`
4. Exécuter les commandes :

```bash
./configure        # vérifie et prépare Makefile
make               # compile le programme
sudo make install  # installe dans /usr/local ou /opt
```

> À faire avec prudence, uniquement si nécessaire (ex : version non dispo via apt)

---

## ✅ À retenir pour les révisions

- `apt` est le gestionnaire de paquets de haut niveau, `dpkg` est le cœur système
- Le fichier `/etc/apt/sources.list` définit les dépôts actifs
- Utiliser `update`, `upgrade`, `full-upgrade` pour maintenir son système
- La compilation depuis sources doit être réservée à des usages maîtrisés

---

## 📌 Bonnes pratiques professionnelles

- Ne jamais modifier `sources.list` sans sauvegarde préalable
- Privilégier les paquets de la branche stable, sauf besoin spécifique
- Toujours lancer `apt update` avant une installation
- Éviter les suppressions avec `purge` sans comprendre leur impact
- Documenter toute installation depuis source (version, options de compilation…)

---

## 🔗 Commandes utiles

```bash
apt update && apt upgrade
apt install / remove / purge / show
apt search nom
apt clean

# dpkg
 dpkg -L nom-paquet
 dpkg -S /chemin

# Compilation
 ./configure && make && sudo make install
```