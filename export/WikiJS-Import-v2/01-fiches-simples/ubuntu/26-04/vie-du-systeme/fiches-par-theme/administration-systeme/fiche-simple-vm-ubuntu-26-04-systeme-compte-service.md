---
title: "Fiche Simple - VM Ubuntu 26.04 Systeme Compte Service"
description: "Créer un compte système dédié, sans shell interactif et sans mot de passe, pour exécuter un service (par exemple une application web) avec les privilèges minimum, au lieu de le lancer sous root ou sous un compte personnel."
published: true
date: 2026-10-29T20:22:42Z
tags: ["ubuntu2604", "useradd", "nologin", "service-account", "systemd", "moindre-privilege"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# 📄 Fiche_Simple_-_VM_Ubuntu_26.04_Systeme_Compte_Service

- **Environnement** : VM ou serveur Ubuntu hébergeant une application ou un service dédié
- **OS / Version** : Ubuntu Server 26.04 LTS
- **Catégorie** : Système / Comptes et isolation des services
- **Tags** : `ubuntu2604`, `useradd`, `nologin`, `service-account`, `systemd`, `moindre-privilege`

---

## 🎯 Problème précis à résoudre

Créer un compte système dédié, sans shell interactif et sans mot de passe, pour exécuter un service (par exemple une application web) avec les privilèges minimum, au lieu de le lancer sous root ou sous un compte personnel.

## 🧪 1. Hors-Production (Lab / Test / POC)

1. Créer le compte système :
```bash
sudo useradd --system --no-create-home --home-dir /var/lib/<compte_service> --shell /usr/sbin/nologin <compte_service>
```
👉 Explication : `--system` attribue un UID de la plage système, `--no-create-home` évite de créer un répertoire personnel, `/usr/sbin/nologin` refuse toute ouverture de shell. Sur Ubuntu 26.04, le chemin `/usr/sbin/nologin` est identique à 24.04.

2. Créer le répertoire de données avec les droits du service :
```bash
sudo install -d -o <compte_service> -g <compte_service> -m 750 /var/lib/<compte_service>
```
👉 Explication : Seul le compte de service et root peuvent lire ou écrire dans ce répertoire ; les autres utilisateurs du système sont exclus.

3. Vérifier le compte créé :
```bash
getent passwd <compte_service>
id <compte_service>
```
👉 Explication : Le champ shell de `getent` doit valoir `/usr/sbin/nologin`. `id` confirme l'UID système et le groupe créé.

## ⚡ 2. Production — Façon Simplifiée

1. Lancer le service sous ce compte via un override systemd :
```bash
sudo systemctl edit <nom_du_service>
```
Contenu à ajouter :
```text
[Service]
User=<compte_service>
Group=<compte_service>
```
👉 Explication : `systemctl edit` crée un fichier dans `/etc/systemd/system/<nom_du_service>.service.d/` sans modifier l'unité d'origine. Les mises à jour du paquet ne l'écrasent donc pas.

2. Recharger et redémarrer le service :
```bash
sudo systemctl daemon-reload
sudo systemctl restart <nom_du_service>
systemctl status <nom_du_service> --no-pager
```
👉 Explication : Le processus doit tourner sous `<compte_service>` ; vérifier avec `ps -o user,pid,cmd -C <nom_du_processus>`.

## 🔒 3. Production — Façon Sécurisée

1. Ajouter des protections systemd dans le même override :
```text
[Service]
User=<compte_service>
Group=<compte_service>
NoNewPrivileges=yes
ProtectSystem=strict
ProtectHome=yes
PrivateTmp=yes
ReadWritePaths=/var/lib/<compte_service>
```
👉 Explication : `ProtectSystem=strict` rend le système de fichiers en lecture seule sauf les chemins listés dans `ReadWritePaths`. `NoNewPrivileges` interdit l'élévation de privilèges par setuid. Tester le service après chaque ajout : une écriture hors du chemin autorisé échouera.

2. Vérifier le score de sécurité de l'unité :
```bash
systemd-analyze security <nom_du_service>
```
👉 Explication : Affiche un score d'exposition (0 = très restreint, 10 = exposé) et les directives manquantes. Sert de référence pour comparer les durcissements.

3. Interdire les connexions interactives du compte :
```bash
sudo passwd -l <compte_service>
sudo -u <compte_service> -i
```
👉 Explication : `passwd -l` verrouille le mot de passe. Le second appel doit échouer avec le message « This account is currently not available. », `nologin` refusant l'ouverture d'un shell interactif.

## ✅ Validation et retour arrière

- **Précontrôles** : sauvegarde de l'unité systemd, identification de tous les fichiers que le service lit et écrit.
- **Validation** : `ps -o user -C <nom_du_processus>` affiche `<compte_service>` ; le service répond ; `getent passwd <compte_service>` affiche `nologin`.
- **Retour arrière** : `sudo systemctl revert <nom_du_service>` supprime l'override ; `sudo systemctl daemon-reload` puis `sudo systemctl restart <nom_du_service>`.