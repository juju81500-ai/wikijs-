---
title: "Spécificités du shell Bash"
description: "ls | grep .txt              # liste les fichiers contenant .txt"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# Spécificités du shell Bash

## 🔍 Recherches simples avec `grep`

### Enchaînement de commandes avec `|`

```bash
ls | grep .txt              # liste les fichiers contenant .txt
ls | grep .txt | wc -l      # compte les fichiers .txt
```

### Utilisation de `grep` dans des fichiers

```bash
grep -in "Reno" Edition
# Recherche insensible à la casse, avec numéros de lignes
```

### Options courantes de `grep`

|Option|Fonction|
|---|---|
|`-i`|Insensible à la casse|
|`-n`|Numérote les lignes|
|`-v`|Inverse la sélection|
|`-e`|Permet des motifs multiples|
|`-l`|Liste les fichiers correspondants|

---

## 📁 Recherches avancées avec `find`

### Syntaxe

```bash
find <chemin> [critères] [action]
```

### Critères les plus utilisés

|Critère|Description|
|---|---|
|`-name`|Nom avec joker (ex : "*.txt")|
|`-user`|Propriétaire du fichier|
|`-group`|Groupe du fichier|
|`-type`|Type (f, d, l, c, b, p)|
|`-size`|Taille (+500k, -100k)|
|`-mtime`|Dernière modif. (-1 = moins de 24h)|

### Exemples

```bash
find . -name "[Tt]el*"
find . -type d -name "*test*"
find dirtest01/ -size +500k
find dirtest01/ -type f -mtime -1
```

### Actions avec `find`

|Action|Description|
|---|---|
|`-print`|Affiche le chemin (défaut)|
|`-exec`|Exécute une commande : `{}` est remplacé par le fichier|
|`-ok`|Comme `-exec`, avec confirmation|

#### Exemple avec `-exec`

```bash
find . -type f -mtime -1 -exec ls -li {} \;
find . -type f -name "Edition" -exec cp -v {} /tmp/{}.txt \;
```

---

## 🧮 Introduction aux expressions régulières (regex)

### Qu’est-ce qu’une regex ?

- Une **expression rationnelle** est un motif décrivant des chaînes de caractères
- Utilisée avec `grep`, `sed`, `awk`, `vi`, etc.

### Quantificateurs

|Regex|Signification|
|---|---|
|`a*`|0 à n fois `a`|
|`a+`|1 à n fois `a` (avec `grep -E`)|
|`a?`|0 ou 1 fois `a`|
|`a{3}`|exactement 3 fois `a`|
|`a{1,3}`|1 à 3 fois `a`|
|`a{2,}`|au moins 2 fois `a`|

### Classes de caractères

|Classe POSIX|Signification|
|---|---|
|`[[:alpha:]]`|Lettre|
|`[[:digit:]]`|Chiffre|
|`[[:alnum:]]`|Lettre ou chiffre|
|`[[:upper:]]`|Majuscule|
|`[[:lower:]]`|Minuscule|
|`[[:space:]]`|Espace|

### Exemples

```bash
grep -E "^[[:upper:]]" fichier     # lignes commençant par majuscule
grep -E "[[:digit:]]$" fichier     # lignes finissant par un chiffre
```

---

## 🎯 Recherche de fichiers avec `locate`

### Présentation

- Utilise une **base indexée** : mise à jour avec `updatedb` (nécessite sudo)
- Très rapide, mais **pas en temps réel**

### Exemple d’utilisation

```bash
touch explocate
locate explocate   # peut ne rien afficher si updatedb pas encore fait
sudo updatedb
locate explocate   # doit maintenant apparaître
```

---

## ✅ À retenir pour les révisions

- `grep`, `find` et `locate` sont les outils clés de recherche dans Bash
- Les regex permettent de filtrer avec une très grande précision
- `find` + `-exec` permet d’enchaîner des actions puissantes
- `locate` est très rapide mais dépend d’une base à jour

---

## 📌 Bonnes pratiques professionnelles

- Toujours **tester une regex avec grep** avant de l’utiliser dans un script
- En cas de doute, utiliser `find … -print` avant `-exec` ou `-delete`
- Éviter `-exec rm` sans double vérification : danger !
- Mettre à jour régulièrement la base `locate` si on l’utilise souvent
- Documenter clairement les motifs regex complexes

---

## 🔗 Liens utiles

- [Regex101 (explication en ligne)](https://regex101.com/)
- [Cheat.sh – Regex Bash](https://cheat.sh/bash+regex)