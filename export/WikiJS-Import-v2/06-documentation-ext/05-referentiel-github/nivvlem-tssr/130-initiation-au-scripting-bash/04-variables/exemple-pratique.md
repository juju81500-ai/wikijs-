---
title: "TP – Variables d’environnement et manipulation de fichiers"
description: "1. Utiliser les commandes suivantes pour afficher les variables du Shell courant :"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# TP – Variables d’environnement et manipulation de fichiers

## 📄 Énoncé

### Partie 1 – Analyse de l’environnement Shell

1. Utiliser les commandes suivantes pour afficher les variables du Shell courant :

```bash
set       # affiche les variables locales et d’environnement
printenv  # affiche uniquement les variables d’environnement
```

2. Identifier les variables suivantes :

- Variable contenant le chemin du fichier de l’historique : `HISTFILE`
- Variable(s) contenant les chemins de recherche des exécutables : `PATH`

---

### Partie 2 – Modifier le prompt du superutilisateur (root)

Objectif : remplacer le prompt `#` du superutilisateur par :

```
nom-de-la-machine#
```

### Étapes :

- Modifier (temporairement) la variable `PS1` :

```bash
export PS1="\h# "
```

- Pour que ce soit permanent, éditer le fichier `/root/.bashrc` et y ajouter la même ligne.

---

### Partie 3 – Script d’analyse de fichier `.txt`

Créer un script nommé `analyse_txt.sh` avec le contenu suivant (corrigé et commenté) :

```bash
#!/bin/bash

# Définition des variables
rep=$(pwd)
extension="txt"

# Affichage du répertoire de travail
echo "Répertoire de travail : $rep"
echo "Fichiers pouvant être traités :"

# Liste les fichiers avec l'extension .txt
ls "$rep"/*."$extension" 2>/dev/null

# Demande du fichier à traiter
read -p "Quel fichier voulez-vous traiter ? " fic

# Vérifie si le fichier existe
if [ ! -f "$fic" ]; then
  echo "Le fichier spécifié n'existe pas."
  exit 1
fi

# Nombre de lignes
nblign=$(wc -l < "$fic")

# Deux premières lignes
debut=$(head -n 2 "$fic")

# Deux dernières lignes
fin=$(tail -n 2 "$fic")

# Affichage des caractéristiques
echo "\nCARACTÉRISTIQUES de $fic"
echo "Nombre de lignes du fichier : $nblign"
echo -e "\nDébut du fichier :\n$debut"
echo -e "\nFin du fichier :\n$fin"
```

> 💡 Astuce : penser à rendre le script exécutable avec `chmod +x analyse_txt.sh`

---

## ✅ À retenir pour les révisions

- `PATH` permet de lancer des scripts sans indiquer leur chemin.
- `HISTFILE` contient le chemin vers l’historique des commandes.
- `PS1` permet de personnaliser le prompt du Shell.
- `read` récupère une saisie utilisateur.
- `head`, `tail`, `wc -l` sont essentiels pour analyser des fichiers texte.