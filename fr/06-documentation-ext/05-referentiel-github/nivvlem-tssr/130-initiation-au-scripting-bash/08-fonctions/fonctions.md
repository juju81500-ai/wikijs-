---
title: "Les fonctions dans les scripts Bash"
description: "- Pour éviter de répéter du code identique plusieurs fois dans un même script"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# Les fonctions dans les scripts Bash

## 🔁 Pourquoi utiliser des fonctions ?

- Pour **éviter de répéter du code** identique plusieurs fois dans un même script
- Pour **rendre les scripts plus lisibles** et **mieux structurés**
- Pour **réutiliser des blocs fonctionnels** dans d’autres scripts (via `source` ou `.`)

> 💡 Utilise un préfixe pour nommer tes fonctions, comme `func_` ou `function_`, pour les distinguer facilement des commandes Bash.

---

## 🔧 Déclarer et utiliser une fonction

### Syntaxe classique :

```bash
nom_fonction() {
  commandes
}
```

### Exemple :

```bash
#!/bin/bash

func_infos() {
  echo "Informations sur la distribution :"
  lsb_release -dric
}

# Appel de la fonction
func_infos
```

> ⚠️ Les fonctions doivent être **déclarées avant leur appel** dans le script.

---

## 📥 Passage de paramètres

Comme les scripts, une fonction peut recevoir des **paramètres** :

- `$1`, `$2`, ... pour les arguments
- `$#` pour le nombre d’arguments

### Exemple :

```bash
func_accueil() {
  echo "Bonjour $1 $2"
  echo "Bienvenue sur $(hostname)"
}

func_accueil "Renzo" "Shima"
```

---

## 🔄 Les variables dans les fonctions

Par défaut, une variable modifiée dans une fonction affecte l’extérieur (pas d’isolation).

### Exemple :

```bash
nbr=10

changer_valeur() {
  nbr=42
}

changer_valeur
echo $nbr  # affiche 42
```

> Pour éviter cela, utiliser `local` (cf. module arithmétique ou avancé)

---

## 📂 Externaliser les fonctions dans un fichier

Il est possible d’écrire les fonctions dans un fichier séparé :

### `mesfonctions.sh`

```bash
func_accueil() {
  echo "Bonjour $1 $2"
  echo "Bienvenue sur $(hostname)"
}
```

### Script principal :

```bash
#!/bin/bash
source ~/mesfonctions.sh

func_accueil "Izumo" "Kamiki"
```

> Le fichier source n’a **pas besoin d’être exécutable**, mais **doit avoir les droits de lecture**.

---

## ✅ À retenir pour les révisions

- Une fonction est définie avec `nom() { ... }`
- Elle doit être déclarée avant utilisation dans le script
- Elle peut recevoir des arguments (`$1`, `$2`, ...)
- Elle peut être externalisée via `source fichier`
- Les variables ne sont pas locales par défaut

---

## 📌 Bonnes pratiques professionnelles

|Bonne pratique|Pourquoi ?|
|---|---|
|Préfixer les noms de fonction (`func_`)|Évite les collisions avec des commandes natives ou systèmes|
|Grouper les fonctions au début ou dans un fichier|Améliore la lisibilité et la modularité|
|Documenter les fonctions avec un commentaire|Clarifie l’objectif et les paramètres attendus|
|Toujours tester les paramètres reçus|Rend la fonction plus robuste et adaptable|
|Ne pas déclarer de fonctions inutilisées|Allège le script et réduit les risques d’erreurs|