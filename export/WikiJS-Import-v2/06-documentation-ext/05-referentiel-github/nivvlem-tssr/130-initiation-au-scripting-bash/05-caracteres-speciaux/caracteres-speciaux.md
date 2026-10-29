---
title: "Les caractères spéciaux du script Bash"
description: "Toutes les commandes sont exécutées l’une après l’autre, quel que soit le résultat de la précédente."
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# Les caractères spéciaux du script Bash

## 🔗 Enchaînement de commandes

### ➤ Inconditionnel : `;`

Toutes les commandes sont exécutées **l’une après l’autre**, quel que soit le résultat de la précédente.

```bash
mkdir /data ; touch /data/fichier.txt ; echo "Fichier créé"
```

> 📌 Dans un script, le `;` peut être remplacé par un **retour à la ligne** (exécution séquentielle).

### ➤ Conditionnel : `&&`

La commande suivante n’est exécutée **que si la précédente a réussi** (`$? = 0`).

```bash
mkdir ./data && touch ./data/fichier.txt
```

### ➤ Conditionnel inverse : `||`

La commande suivante n’est exécutée **que si la précédente a échoué** (`$? ≠ 0`).

```bash
mkdir ./data 2>/dev/null || echo "Erreur de création du répertoire."
```

> ✅ **Bonnes pratiques** : toujours vérifier le code retour d’une commande critique avec `&&` ou `||` pour sécuriser l’exécution.

---

## 📦 Regrouper plusieurs commandes

### ➤ Regroupement avec sous-shell : `(...)`

Exécute les commandes dans un **environnement isolé** (sous-shell).

```bash
(ls /bin ; ls /usr/bin) | wc -l
```

### ➤ Regroupement sans sous-shell : `{ ... ; }`

Toutes les commandes sont exécutées dans le **même shell**.

Syntaxe stricte à respecter :

- Point-virgule après la dernière commande,
- Espaces obligatoires autour des accolades.

```bash
{ echo "Début" ; date ; echo "Fin" ; }
```

> ⚠️ Attention à la syntaxe : **`{ cmd1 ; cmd2 ; }`** (le dernier `;` est obligatoire !)

---

## 🎨 Coloriser les sorties

### ➤ Codes ANSI pour les couleurs

|Couleur|Texte|Fond|
|---|---|---|
|Noir|30|40|
|Rouge|31|41|
|Vert|32|42|
|Jaune|33|43|
|Bleu|34|44|
|Magenta|35|45|
|Cyan|36|46|
|Gris clair|37|47|

|Attribut|Code|
|---|---|
|Aucun|0|
|Gras|1|
|Souligné|4|
|Inversé|7|
|Invisible|8|
|Barré|9|

### ➤ Exemple dans un script :

```bash
echo -e "Ce texte est en \033[1;32mvert\033[0m."
```

> 💡 `\033[0m` remet les attributs de texte par défaut.

---

## ✅ À retenir pour les révisions

- `;` : exécute la commande suivante sans condition.
- `&&` : exécute la commande suivante **si succès** de la précédente.
- `||` : exécute la commande suivante **si échec** de la précédente.
- `(...)` : exécution dans un **sous-shell**.
- `{ ... ; }` : regroupement dans le **même shell** (attention à la syntaxe).
- `\033[...m` : colorisation ANSI (affichage enrichi).

---

## 📌 Bonnes pratiques professionnelles

|Pratique recommandée|Pourquoi ?|
|---|---|
|Utiliser `&&` pour sécuriser les enchaînements|Évite d'exécuter des commandes si erreur précédente|
|Regrouper logiquement les blocs|Améliore la lisibilité et maintenabilité des scripts|
|Coloriser les messages importants|Facilite le support, le debug et l’usage utilisateur|
|Toujours tester les regroupements dans des sous-shell|Évite des effets de bord inattendus|