---
title: "Gestion des utilisateurs et groupes (Debian GNU/Linux)"
description: "- Liste des groupes"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# Gestion des utilisateurs et groupes (Debian GNU/Linux)

## 👥 Types d’utilisateurs sous Linux

|Type|UID / GID|Description|
|---|---|---|
|root|UID 0, GID 0|Superutilisateur (droits complets)|
|daemon|UID/GID 1-999|Comptes systèmes pour services/applications|
|utilisateurs|UID/GID ≥ 1000|Comptes humains|

---

## 📁 Fichiers liés aux groupes

### `/etc/group`

- Liste des groupes
- Syntaxe : `nom:x:GID:membres`

### `/etc/gshadow`

- Informations complémentaires sécurisées (mots de passe groupés, administrateurs)
- Syntaxe : `nomgroupe:hash:admin:membres`

---

## 🔧 Commandes de gestion des groupes

|Commande|Fonction|
|---|---|
|`groupadd -g <GID> nom`|Créer un groupe|
|`groupmod -g <GID>`|Modifier un GID|
|`groupmod -n nouveau nom`|Renommer un groupe|
|`groupdel nom`|Supprimer un groupe vide|
|`gpasswd -a user groupe`|Ajouter un membre|
|`gpasswd -d user groupe`|Retirer un membre|

---

## 📁 Fichiers liés aux utilisateurs

### `/etc/passwd`

- Description de chaque utilisateur
- Syntaxe : `user:x:UID:GID:infos:/home/user:/bin/bash`

### `/etc/shadow`

- Mot de passe chiffré, politique de mot de passe
- Syntaxe : `user:$6$HASH:date:mini:max:warn:inact:expire:`

---

## 🔧 Commandes de gestion des utilisateurs

|Commande|Usage|
|---|---|
|`useradd -m -d /home/nom -u UID -g GID -G grp1,grp2 -s /bin/bash nom`|Créer un utilisateur|
|`usermod -d /home/nouveau -m -e AAAA-MM-JJ -f durée -g GID -G grp1 -a -s /bin/zsh`|Modifier un utilisateur|
|`userdel -r nom`|Supprimer un utilisateur + son home|
|`passwd nom`|Modifier le mot de passe|
|`passwd -e`|Forcer un changement au prochain login|
|`passwd -l / -u`|Verrouiller / déverrouiller le compte|

---

## 🆙 Élévation de privilèges

### `su`

- Passer à un autre utilisateur ou root :

```bash
su -          # Ouverture de session root complète
su - user     # Changement d’utilisateur
su -c 'commande'
```

### `sudo`

- Exécuter des commandes avec les droits root (ou d’un autre utilisateur)
- Configuration via `/etc/sudoers`
- Ajout d’un utilisateur au groupe `sudo` pour tous les droits

```bash
sudo commande
sudo -i       # session root
```

---

## ✅ À retenir pour les révisions

- UID = utilisateur, GID = groupe principal
- `passwd`, `useradd`, `usermod`, `groupadd`, `gpasswd` sont les commandes de base
- `/etc/passwd`, `/etc/shadow`, `/etc/group`, `/etc/gshadow` contiennent les données critiques
- `su` = changement d’identité, `sudo` = exécution avec droits supérieurs

---

## 📌 Bonnes pratiques professionnelles

- Ne jamais se connecter en root en interface graphique
- Utiliser `sudo` pour un usage ponctuel des droits admin
- Ne **jamais** éditer directement les fichiers sensibles (`passwd`, `shadow`) à la main
- Vérifier les effets des modifications de GID ou UID sur les fichiers existants

---

## 🔗 Commandes utiles

```bash
useradd, usermod, userdel
passwd, chage
groupadd, groupmod, groupdel
gpasswd, su, sudo
cat /etc/passwd, /etc/shadow, /etc/group, /etc/gshadow
```

## Ressources complémentaires

- [Debian Wiki – User Management](https://wiki.debian.org/UserManagement)