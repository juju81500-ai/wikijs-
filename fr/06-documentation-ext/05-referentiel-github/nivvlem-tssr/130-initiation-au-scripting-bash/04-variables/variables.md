---
title: "Les variables dans les scripts Bash"
description: "Les variables permettent de stocker temporairement des informations (textes, chemins, valeurs numériques...) utilisées par un script."
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# Les variables dans les scripts Bash

## 🧠 Pourquoi utiliser des variables ?

Les **variables** permettent de **stocker temporairement des informations** (textes, chemins, valeurs numériques...) utilisées par un script.

### Exemple simple :

```bash
prenom="Melvin"
echo "Bonjour $prenom"
```

> ✅ Bonne pratique : toujours entourer les appels de variables avec `"` pour éviter des effets inattendus.

---

## 📂 Types de variables

|Type|Description|Exemple|
|---|---|---|
|**Variables locales**|Accessibles uniquement dans le Shell courant|`fichier="/tmp/test.txt"`|
|**Variables d’environnement**|Transmises aux sous-shells|`export LANG=fr_FR.UTF-8`|
|**Variables réservées**|Définies par le Shell, ne pas les écraser|`$1`, `$?`, `$$`, `$#`, `$@`|
|**Constantes (read-only)**|Valeurs figées, non modifiables|`declare -r VERSION="1.0"`|

---

## 🧪 Manipuler des variables

### Affectation :

```bash
nom="Yukio"
```

### Utilisation :

```bash
echo "$nom"
```

### Réaffectation :

```bash
nom="Rin"
```

### Exportation :

```bash
export nom
export chemin="/usr/bin"
```

---

## 🔁 Variables réservées utiles

|Variable|Signification|
|---|---|
|`$0`|Nom du script|
|`$1` à `$9`|Paramètres passés au script (`$1` = 1er argument, etc.)|
|`$#`|Nombre d’arguments passés|
|`$@` ou `$*`|Liste des arguments|
|`$?`|Code retour de la dernière commande|
|`$$`|PID (ID du processus) courant|
|`$!`|PID du dernier processus lancé en arrière-plan (`&`)|

### Exemple :

```bash
./bonjour.sh Shiemi

# Dans le script
echo "Bonjour $1 $2"     # Bonjour Shiemi
echo "Il y a $# arguments."
```

---

## ⌨️ Lire une saisie utilisateur avec `read`

Permet de **stocker une saisie clavier dans une ou plusieurs variables**.

### Syntaxe :

```bash
read [options] variable1 variable2 ...
```

### Exemple simple :

```bash
read -p "Entrez votre nom : " nom
echo "Bonjour $nom"
```

### Exemple avec plusieurs mots :

```bash
read -p "Nom et prénom : " nom prenom
echo "Nom : $nom"
echo "Prénom : $prenom"
```

> ⚠️ Si plus de mots sont saisis que de variables, le dernier mot va tout contenir.

### Prévenir les débordements avec une variable tampon :

```bash
read -p "Nom et prénom : " nom prenom tampon
unset tampon
```

---

## ✅ À retenir pour les révisions

- Déclarer une variable : `var="valeur"`
- Utiliser une variable : `"$var"`
- Les variables d’environnement sont héritées par les sous-shells (`export`)
- Les variables réservées sont utiles pour les scripts complexes ou interactifs
- `read` permet de récupérer des saisies clavier en les assignant à des variables

## 📌 Bonnes pratiques professionnelles

| Pratique recommandée                       | Pourquoi ?                                                  |
| ------------------------------------------ | ----------------------------------------------------------- |
| Toujours entourer les variables de `""`    | Évite les erreurs dues aux espaces ou à l’absence de valeur |
| Utiliser des noms explicites en minuscules | Meilleure lisibilité et distinction avec variables système  |
| Exporter uniquement si nécessaire          | Évite la pollution de l’environnement global                |
| Préférer `read -p` à `echo + read`         | Scripts plus compacts et lisibles                           |
| Détruire les variables temporaires         | Libère la mémoire et évite les collisions (`unset`)         |
| Ne jamais écraser une variable réservée    | Risque de dysfonctionnement ou comportement inattendu       |