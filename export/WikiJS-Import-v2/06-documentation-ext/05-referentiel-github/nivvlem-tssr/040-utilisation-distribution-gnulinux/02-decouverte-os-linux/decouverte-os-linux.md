---
title: "Découverte du système d’exploitation Linux"
description: "Un système d'exploitation (OS) est un ensemble de programmes assurant la gestion des ressources matérielles d’un ordinateur et leur mise à disposition pour les utilisateurs et les applications."
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# Découverte du système d’exploitation Linux

## 🖥️ Qu’est-ce qu’un système d’exploitation ?

Un **système d'exploitation** (OS) est un ensemble de programmes assurant la gestion des ressources matérielles d’un ordinateur et leur mise à disposition pour les utilisateurs et les applications.

### 📋 Types de systèmes d’exploitation

|Catégorie|Exemples|
|---|---|
|Systèmes propriétaires|OS400 (IBM)|
|Systèmes ouverts mono-poste/mono-tâche|DOS|
|Systèmes ouverts multi-tâche/multi-plateforme|UNIX, GNU/Linux, Windows, OS-X|

### 🧱 Composantes d’un système Linux

- **Matériel** (hardware)
- **Noyau (kernel)** : cœur du système, gestion des ressources
- **Shell** : interface entre l'utilisateur et le système
- **Applications** : programmes utilisateurs
- **Utilisateur(s)** : interacteurs avec le système

---

## 🧠 Le noyau Linux (kernel)

Le **noyau** est le programme principal chargé de :

- Gérer la mémoire, les périphériques, les processus
- Partager les ressources entre utilisateurs
- Ordonnancer l'exécution des tâches

🔹 En anglais : _kernel_

À noter : dans une vision large, on parle aussi de "noyau" pour désigner l'ensemble des composants essentiels du système Linux.

---

## 🧾 Le Shell

Le **shell** est un **interpréteur de commandes** qui permet à l'utilisateur d’interagir avec le système via la ligne de commande (**CLI** – _Command Line Interface_).

### 🔄 Flux standard dans le shell

|Type de flux|Description|Abréviation|Code|
|---|---|---|---|
|Entrée standard|Ce que tape l’utilisateur|stdin|0|
|Sortie standard|Résultat normal affiché|stdout|1|
|Sortie erreur|Message d’erreur|stderr|2|

#### Exemple :

```bash
user@linux:~$ echo "Bonjour le monde"
Bonjour le monde

user@linux:~$ ls Bonjour
ls: impossible d'accéder à 'Bonjour': Aucun fichier ou dossier de ce type
```

### 🐚 Exemples de shells

|Shell|Créateur|Particularités|
|---|---|---|
|sh (Bourne Shell)|Steve Bourne|Shell historique|
|csh / tcsh|Bill Joy|Syntaxe inspirée du langage C|
|ksh (KornShell)|David Korn|Compatible Bourne + fonctionnalités C|
|bash|Brian Fox (GNU)|Amélioré : historique, autocomplétion, alias|

---

## 📐 Syntaxe des commandes

### Principes de base

- **Sensible à la casse** : `echo` ≠ `Echo`
- Une commande commence toujours par le nom de la commande
- Suivie éventuellement d'**options** puis d'**arguments** (espacés)

#### Exemples :

```bash
who                         # sans argument
ls /etc                    # avec argument
head -n 5 /etc/pam.conf    # option + argument
cp /tmp/fic1 $HOME         # deux arguments
```

### Syntaxe complexe

```bash
tar xzvf archive.tar.gz    # 4 options + 1 argument
```

---

## 🔐 Connexion à un système Linux

### Moyens de connexion

- Console locale (accès direct à la machine)
- Interface graphique (GUI)
- Connexion distante via **SSH** (Secure Shell)

### Outils pour SSH sous Windows

|Logiciel|Particularités|
|---|---|
|**cmd.exe**|Utilisable directement (Windows récent)|
|**Putty**|Référence libre (MIT), intègre `pscp` et `psftp`|
|**Kitty**|Fork de Putty, commandes automatiques|
|**mRemoteNG**|Multi-protocoles, onglets multiples|
|**MobaXterm**|Multi-protocoles, interface graphique évoluée|

### 🔗 Liens utiles :

- [Putty](https://www.chiark.greenend.org.uk/~sgtatham/putty/)
- [Kitty](https://www.9bis.net/kitty/index.html#!index.md/)
- [mRemoteNG](https://mremoteng.org/)
- [MobaXterm](https://mobaxterm.mobatek.net/)

---

## 🔚 Se déconnecter proprement

|Méthode|Description|
|---|---|
|`exit`|Universelle, compatible avec Bash|
|`logout`|Disponible sur certains shells, comme Bash|
|`Ctrl+D`|Raccourci clavier, envoie EOF (End Of File)|

---

## ✅ À retenir pour les révisions

- Un OS gère les ressources et sert d’interface entre utilisateur et matériel
- Le **noyau** est le cœur technique du système
- Le **shell** permet d’interagir via des commandes textuelles (CLI)
- La **syntaxe des commandes** suit un ordre strict : commande > options > arguments
- Pour se connecter à distance, SSH est un standard sécurisé
- Toujours se **déconnecter proprement** d’un shell

---

## 📌 Bonnes pratiques professionnelles

- Utiliser Bash pour bénéficier des fonctionnalités avancées (historique, alias…)
- Respecter la casse des commandes et leur syntaxe stricte
- Favoriser l’usage de clients SSH modernes (Kitty, MobaXterm) pour plus de confort
- Documenter les commandes fréquentes et utiliser des alias si besoin
- Ne jamais laisser une session ouverte inutilement (risque de sécurité)