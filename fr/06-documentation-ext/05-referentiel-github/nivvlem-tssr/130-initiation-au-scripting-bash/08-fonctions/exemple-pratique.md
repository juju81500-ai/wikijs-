---
title: "TP – Fonctions Bash : sauvegarde, suppression et affichage"
description: "Créer deux fichiers :"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# TP – Fonctions Bash : sauvegarde, suppression et affichage

## 📄 Énoncé

Créer deux fichiers :

- `fonctions.sh` : le script principal interactif
- `fonctions.fonc` : contient toutes les fonctions utilisées dans le script principal

### Le menu de `fonctions.sh` doit proposer :

1. Sauvegarder tous les fichiers `.sh` du répertoire courant (les dupliquer en `.save`)
2. Supprimer tous les fichiers `.save`
3. Lister :
    - les fichiers `.sh` **ayant une sauvegarde** (affichage en **vert**)
    - les fichiers `.sh` **sans sauvegarde** (affichage en **rouge**)
4. Quitter

---

## ✅ Contenu de `fonctions.fonc`

```bash
func_sauvegarder() {
  for fic in *.sh; do
    cp "$fic" "$fic.save"
  done
  echo "Sauvegarde terminée."
}

func_supprimer() {
  rm -f *.save
  echo "Fichiers .save supprimés."
}

func_lister() {
  for fic in *.sh; do
    if [[ -f "$fic.save" ]]; then
      echo -e "\033[1;32m$fic sauvegardé\033[0m"
    else
      echo -e "\033[1;31m$fic non sauvegardé\033[0m"
    fi
  done
}
```

---

## ✅ Contenu de `fonctions.sh`

```bash
#!/bin/bash

# Chargement des fonctions
source ./fonctions.fonc

# Boucle principale du menu
while true; do
  echo "-------------------------"
  echo " MENU GESTION DE FICHIERS"
  echo "-------------------------"
  echo "1 - Sauvegarder les fichiers .sh"
  echo "2 - Supprimer les fichiers .save"
  echo "3 - Lister les fichiers et leur sauvegarde"
  echo "4 - Quitter"
  echo
  read -p "Votre choix : " choix

  case $choix in
    1) func_sauvegarder ;;
    2) func_supprimer ;;
    3) func_lister ;;
    4) echo "Au revoir."; break ;;
    *) echo -e "\033[41mChoix invalide\033[0m" ;;
  esac
  echo
  read -p "Appuyez sur Entrée pour continuer..."
  clear

done
```

---

## 🧠 Bonnes pratiques appliquées

- Le script principal (`fonctions.sh`) reste **simple et lisible**.
- Les fonctions sont séparées dans `fonctions.fonc`, ce qui permet de :
    - **réutiliser** ces fonctions dans d’autres scripts,
    - **tester ou déboguer** les blocs indépendamment.
- Affichage coloré (vert pour OK, rouge pour KO).
- Utilisation de `source` pour importer un fichier Bash (même comportement que `. fichier`).

---

## ✅ À retenir pour les révisions

- Une fonction doit être **déclarée avant d’être appelée**.
- Un fichier externe contenant des fonctions peut être importé avec `source` ou `.`.
- On peut **modulariser** ses scripts pour une meilleure maintenance.
- Utiliser des **codes couleur ANSI** pour rendre l’affichage plus intuitif.