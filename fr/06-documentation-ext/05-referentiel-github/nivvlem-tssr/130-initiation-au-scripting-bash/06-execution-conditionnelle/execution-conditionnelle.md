---
title: "Exécution conditionnelle dans les scripts Bash"
description: "if [[ condition ]]; then"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# Exécution conditionnelle dans les scripts Bash

## 🧠 Structures conditionnelles : `if` et `case`

### ✅ `if` : syntaxe de base

```bash
if [[ condition ]]; then
  # actions si condition vraie
elif [[ autre_condition ]]; then
  # actions si autre condition
else
  # actions si aucune condition n’est remplie
fi
```

### ✅ `case` : pour tester plusieurs valeurs possibles

```bash
case $variable in
  valeur1)
    commande1
    ;;
  valeur2)
    commande2
    ;;
  *)
    commande_par_defaut
    ;;
esac
```

---

## 🔍 Les tests (`[[ ]]`, `[ ]`, `test`)

|Syntaxe|Utilisation principale|
|---|---|
|`[[ ... ]]`|Test étendu (recommandé en Bash)|
|`[ ... ]`|Test POSIX, plus limité|
|`(( ... ))`|Test arithmétique|
|`test ...`|Équivalent POSIX de `[ ... ]`|

### Codes retour :

- `0` : vrai (succès)
- `1` : faux (échec)

---

## 🧮 Opérateurs de test

### Comparaison de **nombres**

|Opérateur|Signification|
|---|---|
|`-eq`|égal à|
|`-ne`|différent de|
|`-gt`|supérieur à|
|`-ge`|supérieur ou égal à|
|`-lt`|inférieur à|
|`-le`|inférieur ou égal à|

```bash
if [[ $nb -gt 5 ]]; then
  echo "Supérieur à 5"
fi
```

### Comparaison de **chaînes**

|Opérateur|Signification|
|---|---|
|`=`|égal à|
|`!=`|différent de|
|`-n`|non vide|
|`-z`|vide|

```bash
if [[ -z "$nom" ]]; then
  echo "Nom non renseigné"
fi
```

### Tests sur les **fichiers**

|Opérateur|Signification|
|---|---|
|`-f`|est un fichier régulier|
|`-d`|est un répertoire|
|`-r`|droit de lecture|
|`-w`|droit d’écriture|
|`-x`|droit d’exécution|
|`-s`|fichier non vide|

---

## 🔁 Combinaison de conditions

|Opérateur|Fonction|
|---|---|
|`&&`|ET logique|
|`||
|`!`|Négation|
|`( )`|Groupement|

```bash
if [[ -f $fic && -r $fic ]]; then
  echo "Le fichier existe et est lisible."
fi
```

---

## 🎯 Cas avancé : activer les motifs étendus

Pour des comparaisons avancées avec motifs comme `+([0-9])`, `@(oui|non)`, etc. :

```bash
shopt -s extglob
```

### Ex : tester si une chaîne est un entier signé

```bash
chaine="+123"
if [[ "$chaine" = ?([+-])+([0-9]) ]]; then
  echo "$chaine est un nombre valide"
fi
```

---

## ✅ À retenir pour les révisions

- Utiliser `[[ ... ]]` pour les tests conditionnels
- `if`, `elif`, `else`, `fi` = bloc conditionnel complet
- `case` pour des valeurs multiples possibles
- Toujours entourer les variables entre `"..."` dans les tests
- Utiliser `shopt -s extglob` pour les motifs complexes

---

## 📌 Bonnes pratiques professionnelles

|Pratique recommandée|Pourquoi ?|
|---|---|
|Utiliser `[[ ... ]]` au lieu de `[ ... ]`|Plus puissant, meilleure gestion des espaces et caractères spéciaux|
|Toujours entourer les variables avec `""`|Évite les erreurs si la variable est vide ou contient des espaces|
|Préférer `case` aux multiples `if` imbriqués|Pour améliorer la lisibilité quand on teste plusieurs valeurs|
|Vérifier les fichiers avec `-f`, `-r`, etc.|Avant d'agir sur des fichiers, éviter les erreurs inattendues|
|Utiliser des noms explicites dans les tests|Rend le script plus lisible et maintenable|