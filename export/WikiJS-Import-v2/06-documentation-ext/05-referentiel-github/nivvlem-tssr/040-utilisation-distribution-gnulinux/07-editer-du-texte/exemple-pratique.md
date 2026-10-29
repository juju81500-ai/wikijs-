---
title: "TP – Utilisation de Vi"
description: "vim Edition"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# TP – Utilisation de Vi 

## 🧱 Étapes détaillées

### 📝 1. Ouvrir le fichier `Edition`

```bash
vim Edition
```

### 🔎 2. Rechercher et modifier

- Chercher « Dupont Jean » :

```bash
/Dupont Jean
```

- Sur le `n` de Jean :

```vim
a-Jacques <Échap>
```

### ✍️ 3. Modifier « Dupont Pierre » → « Jean-Pierre »

```vim
/Dupont Pierre
w
iJean- <Échap>
```

### ⬆️ 4. Début du fichier

```vim
gg
```

### ➕ 5. Ajouter votre nom avant le premier « Dupont »

```vim
/Dupont
ODesflaches Melvin <Échap>
```

### ➕ 6. Ajouter un voisin après le dernier Dupont

```vim
G
?Dupont
oDesflaches Azusa <Échap>
```

### 💾 7. Enregistrer et quitter

```vim
:wq
```

---

## 🧠 Recherches et remplacements

### 🔁 8. Remplacer « Dupont Jean » par « Merlin-Duval Jean »

```vim
/Dupont Jean
n
cwMerlin-Duval <Échap>
```

### ❌ 9. Supprimer la ligne « Couteau Jean »

```vim
/Couteau Jean
dd
```

### 🔁 10. Remplacer tous les « Dupont » par « Durand »

```vim
:g/Dupont/s//Durand/g
```

### 🔀 11. Déplacer toutes les lignes contenant « Durand » à la fin

```vim
:g/Durand/m$
```

### ➕ 12. Dupliquer la ligne contenant « Ben Raf »

```vim
/Ben Raf
yy
p
```

### ⏱️ 13. Afficher l'heure sans quitter

```vim
:!date
```

---

## ⚙️ 14. Créer un fichier `.vimrc`

```bash
vim ~/.vimrc
```

Contenu :

```vim
set number
set tabstop=5
set nocompatible
```

---

## 🔁 15. Recherches globales et substitutions

### Remplacer tous les « Durand » par « Dupont »

```vim
:g/Durand/s//Dupont/g
```

### Ajouter « -Paul » à chaque « Jean »

```vim
:g/Jean /s/Jean/&-Paul
```

### Mettre « Jean » en majuscules sans l’écrire deux fois

```vim
:g/\(Jean\)/s//\U\1/
```

### Remettre « JEAN » en « Jean » (modification du séparateur)

```vim
:g/JEAN/s//Jean/
```

### Remplacer chaque « Jean » par « Jean-Jean »

```vim
:%s/Jean/Jean-Jean/g
```

### Ajouter (033) devant chaque numéro en fin de ligne commençant par 1,2 ou 3

```vim
:%s/\<[1-3]/(033)&/g
```

### Ajouter 0 à la fin de chaque ligne commençant par F

```vim
:g/^F/s/$/0/
```

---

## ✅ À retenir pour les révisions

- `gg`, `G`, `/motif`, `n`, `N`, `dd`, `cw`, `yy`, `p`, `:!cmd`, `:wq`, etc.
- `:g/motif/s//remplacement/g` = recherche/remplacement global
- `.vimrc` permet de personnaliser l’expérience Vim

---

## 📌 Bonnes pratiques professionnelles

- Toujours sauvegarder avant une manipulation en masse
- Utiliser les commandes de recherche pas à pas avec `n`/`N`
- Tester les remplacements avec une seule occurrence avant globalisation
- Conserver un `.vimrc` standardisé pour son environnement utilisateur

---

## 🔗 Ressources utiles

- [Vim Help](https://vimhelp.org/)
- [Cheat.sh – Vim](https://cheat.sh/vim)