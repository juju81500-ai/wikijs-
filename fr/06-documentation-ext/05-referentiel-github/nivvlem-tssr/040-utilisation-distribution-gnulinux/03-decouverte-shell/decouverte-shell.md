---
title: "Découverte du shell et premières commandes"
description: "- Root = super-administrateur (privilèges absolus)"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# Découverte du shell et premières commandes

## 💻 La fenêtre Bash

### Structure d'une session Bash

|Élément|Description|
|---|---|
|Prompt|Invite de commande (ex: `user@host:~$`)|
|Zone de saisie|Là où l’utilisateur tape la commande|
|Résultats|Sortie texte suite à l’exécution|
|Nouveau prompt|Retour à l’attente de commande|

---

## 🔐 Le compte root

- Root = super-administrateur (privilèges absolus)
- Invite spécifique : `#` au lieu de `$`
- ⚠️ Connexion directe déconseillée pour des raisons de sécurité

### Sous Debian :

- L'accès direct à root est souvent désactivé par défaut
- Utiliser `sudo` depuis un utilisateur standard

---

## 🔎 Premières commandes d'information

|Commande|Description|
|---|---|
|`logname`|Nom de l’utilisateur courant|
|`id`|UID, GID, groupes|
|`id -u user`|UID d’un utilisateur spécifique|
|`who` / `who -H`|Liste des utilisateurs connectés|
|`who am i`|Infos sur la session actuelle|
|`passwd`|Changer son mot de passe|
|`passwd -S`|État du mot de passe|

---

## 📅 Informations temporelles et localisation

### Commandes utiles

|Commande|Usage|
|---|---|
|`date`|Affiche la date/heure système|
|`date "+%A %d %B %Y"`|Formatage personnalisé|
|`cal`|Affiche le calendrier|
|`tty`|Affiche le terminal utilisé|
|`pwd`|Affiche le répertoire courant|

---

## 📦 Les variables dans Bash

### Définir et lire une variable

```bash
prenom="Kafka"
echo $prenom
```

### Supprimer une variable

```bash
unset prenom
```

### Afficher toutes les variables

- `env` : variables d’environnement
- `set` : toutes les variables et fonctions

### Variables d’environnement courantes

|Variable|Rôle|
|---|---|
|`HOME`|Répertoire utilisateur|
|`PATH`|Répertoires de recherche des commandes|
|`USER`, `LOGNAME`|Nom utilisateur|
|`SHELL`|Shell courant|
|`LANG`|Langue et locale|
|`PWD`|Répertoire actuel|
|`PS1`|Format de l’invite Bash|

---

## ⚙️ Historique de commandes et productivité

### Historique

- Flèches ↑ ↓ pour naviguer
- `history` pour lister les commandes passées
- `!!` : dernière commande
- `!com` : dernière commande commençant par `com`
- `!?mot` : dernière commande contenant `mot`
- `!num` : commande par numéro historique

#### Fichier et variables liées

- `.bash_history` : fichier de l’historique
- `HISTFILE`, `HISTSIZE` : variables d’environnement

### Auto-complétion

- `TAB` : complète commandes, fichiers, variables
- Double `TAB` : liste les possibilités si ambiguïté

---

## ❓ Obtenir de l’aide dans Bash

### Méthodes disponibles

|Méthode|Usage|
|---|---|
|`commande --help`|Aide rapide sur une commande|
|`man commande`|Manuel complet|
|`help`|Aide sur les commandes internes de Bash|
|`man -k mot`|Rechercher dans tous les man|
|`LANG=C man`|Afficher en anglais (utile en cas de documentation limitée)|

### Astuces man

- `/mot` : rechercher mot dans la page
- `n`, `N` : navigation entre occurrences
- `q` : quitter

---

## ✅ À retenir pour les révisions

- Le shell Bash est une interface puissante, textuelle, et automatisable.
- `root` est à utiliser avec précaution ; privilégier `sudo`.
- Les commandes `logname`, `id`, `who`, `pwd` sont fondamentales.
- Les variables permettent de stocker et manipuler temporairement des données.
- L’historique (`history`, `!!`, `!com`) et l’autocomplétion (`TAB`) sont des outils puissants.
- `man`, `--help` et `help` sont les outils principaux d’aide intégrée.

---

## 📌 Bonnes pratiques professionnelles

- Toujours tester les commandes sur un compte utilisateur avant root
- Utiliser des noms explicites pour les variables
- Vérifier l’effet d’une commande avec `--help` avant usage
- Explorer les pages `man` pour mieux comprendre une commande
- Utiliser l’autocomplétion pour éviter les erreurs de frappe
- Exploiter l’historique pour gagner en efficacité

---

## 🔗 Liens utiles

- [TLDP - Guide Bash en anglais](https://tldp.org/LDP/Bash-Beginners-Guide/html/)
- [Cheat.sh - Aide rapide en ligne](https://cheat.sh/)
- `man`, `info`, `help` : disponibles directement dans le terminal