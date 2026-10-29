---
title: "Synthèse – Initiation au scripting Bash"
description: "- Toujours commencer par le shebang : #!/bin/bash"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# Synthèse – Initiation au scripting Bash

## 📌 Les grandes notions à retenir

### 📁 Organisation d’un script

- Toujours commencer par le **shebang** : `#!/bin/bash`
- Donner les **droits d’exécution** : `chmod +x monscript.sh`
- Utiliser des **commentaires clairs** (`#`) pour décrire chaque section
- Privilégier une **structure logique** : variables → fonctions → code principal

### 🗃️ Variables

- Affectation : `nom="valeur"`
- Appel : `echo "$nom"`
- Types : locales, d’environnement (`export`), réservées (`$1`, `$?`, `$@`, etc.)
- Lecture utilisateur : `read nom`, `read -p "message" var`

### 🔁 Structures de contrôle

- `if / elif / else` pour tester des conditions
- `case` pour tester plusieurs valeurs d’une variable
- Test de chaînes : `[[ -z "$var" ]]`, `[[ "$a" = "$b" ]]`
- Test de nombres : `-eq`, `-gt`, `-lt`, etc.
- Test de fichiers : `-f`, `-d`, `-r`, `-w`, `-x`, `-s`

### 🔂 Boucles

- `for` : sur une **liste** ou avec un **compteur**
- `while` : **tant que** condition vraie
- `until` : **jusqu’à ce que** condition vraie
- `while read` : lecture **ligne par ligne** d’un fichier

### 🔄 Fonctions

- Déclaration : `nom_fonction() { ... }`
- Appel : `nom_fonction "param1" "param2"`
- Passage de paramètres : `$1`, `$2`, ...
- Externalisation avec `source fichier_fonctions.sh`

---

## 🧰 Commandes et outils utiles

|Commande|Description|
|---|---|
|`echo`|Affiche du texte|
|`read`|Lit une saisie utilisateur|
|`test`, `[ ]`, `[[ ]]`|Permet de tester des conditions|
|`cal`|Affiche un calendrier|
|`date`|Récupère la date ou des infos temporelles|
|`find`|Recherche de fichiers|
|`grep`|Recherche dans un flux de texte|
|`ls`, `wc -l`|Lister, compter les lignes|
|`chmod`, `chown`|Modifier les permissions/prop. fichiers|
|`source`|Charge un fichier dans l’environnement courant|

---

## ⚠️ Pièges à éviter

- Oublier les **guillemets** autour des variables → risque avec les espaces ou valeurs nulles
- Utiliser = au lieu de `-eq` pour des **tests numériques**
- Écraser une variable réservée (ex : `PATH`, `UID`...)
- Ne pas vérifier la **présence d’arguments** dans un script (`$#`, `$1`)
- Lancer une boucle sans évolution de condition → **boucle infinie**
- Utiliser `for var in $(cat fichier)` → casse les lignes multi mots

---

## ✅ Bonnes pratiques professionnelles

| Pratique                                       | Pourquoi ?                                                    |
| ---------------------------------------------- | ------------------------------------------------------------- |
| Ajouter un **entête** avec date, auteur, usage | Clarifie le rôle du script et ses prérequis                   |
| Préfixer les noms de fonctions                 | Ex : `func_sauvegarde` → lisibilité accrue                    |
| Modulariser avec des **fonctions externes**    | Réutilisable, plus clair à maintenir                          |
| Vérifier les **entrées utilisateur**           | Validation stricte pour éviter des comportements indésirables |
| Documenter chaque bloc de code                 | Permet à d'autres (ou à toi) de comprendre plus tard          |
| Coloriser les messages                         | Facilite la lecture (succès/erreur)                           |
| Retourner un **code de sortie clair**          | `exit 0`, `exit 1`... pour diagnostic et automation           |
| Tester ses scripts en condition **réelle**     | Ex : VM, utilisateur non root, répertoires temporaires        |