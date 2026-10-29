---
title: "Fiche Simple - VM Ubuntu 26.04 Systeme Hostname FQDN"
description: "Donner au serveur un nom d'hôte court et un FQDN cohérents, résolus localement et stables après redémarrage, afin que SSH, la supervision, l'annuaire et les certificats identifient la machine de la même façon."
published: true
date: 2026-10-29T20:22:42Z
tags: ["ubuntu2604", "hostname", "fqdn", "hosts", "systemd", "cloud-init"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# 📄 Fiche_Simple_-_VM_Ubuntu_26.04_Systeme_Hostname_FQDN

- **Environnement** : VM ou serveur Ubuntu (installation Subiquity ou image cloud-init)
- **OS / Version** : Ubuntu Server 26.04 LTS
- **Catégorie** : Système / Identité de la machine
- **Tags** : `ubuntu2604`, `hostname`, `fqdn`, `hosts`, `systemd`, `cloud-init`

---

## 🎯 Problème précis à résoudre

Donner au serveur un nom d'hôte court et un FQDN cohérents, résolus localement et stables après redémarrage, afin que SSH, la supervision, l'annuaire et les certificats identifient la machine de la même façon.

## 🧪 1. Hors-Production (Lab / Test / POC)

1. Relever l'identité actuelle de la machine :
```bash
hostnamectl status
```
👉 Explication : Affiche le nom statique, le nom transitoire, le noyau et l'OS. Sous systemd 259 (Ubuntu 26.04), `hostnamectl` reste l'outil de référence pour l'identité.

2. Définir le nom d'hôte court :
```bash
sudo hostnamectl set-hostname <nom_du_serveur>
```
👉 Explication : Écrit le nom statique dans `/etc/hostname` et l'applique immédiatement, sans redémarrage.

3. Déclarer le FQDN dans la table d'hôtes locale avec un éditeur root :
```bash
sudo nano /etc/hosts
```
Ligne attendue :
```text
127.0.1.1   <nom_du_serveur>.<domaine>   <nom_du_serveur>
```
👉 Explication : Ubuntu associe le nom de la machine à `127.0.1.1`. Sans cette ligne, `hostname -f` ne renvoie pas le FQDN et certains services échouent à se résoudre eux-mêmes.

4. Vérifier le nom court et le nom complet :
```bash
hostname
hostname -f
```
👉 Explication : `hostname` doit afficher `<nom_du_serveur>` ; `hostname -f` doit afficher `<nom_du_serveur>.<domaine>`.

## ⚡ 2. Production — Façon Simplifiée

1. Contrôler si cloud-init réapplique un nom d'hôte au démarrage :
```bash
grep -rn "preserve_hostname" /etc/cloud/cloud.cfg /etc/cloud/cloud.cfg.d/ 2>/dev/null
```
👉 Explication : Sur une VM clonée ou une image cloud, cloud-init peut remettre son propre nom à chaque démarrage. Si aucune ligne n'apparaît, cloud-init n'est pas configuré pour conserver le nom.

2. Vérifier la résolution du FQDN par le DNS interne :
```bash
resolvectl query <nom_du_serveur>.<domaine>
```
👉 Explication : Interroge systemd-resolved, actif par défaut sur Ubuntu Server 26.04, et confirme que l'enregistrement A pointe vers l'adresse de la machine.

## 🔒 3. Production — Façon Sécurisée

1. Figer le nom d'hôte si cloud-init est présent, dans un fichier dédié :
```bash
sudo nano /etc/cloud/cloud.cfg.d/99-hostname.cfg
```
```yaml
preserve_hostname: true
```
👉 Explication : Le fichier `99-*` a priorité sur les fichiers par défaut. Le nom défini à l'installation n'est plus écrasé lors d'un redémarrage ou d'un clonage.

2. Contrôler l'enregistrement inverse (PTR) de l'adresse IP de la machine :
```bash
dig -x <IP_SERVEUR> +short
```
👉 Explication : Le PTR doit renvoyer `<nom_du_serveur>.<domaine>.`. Une incohérence entre A et PTR casse certaines authentifications et journaux de sécurité. La commande requiert le paquet `dnsutils`.

3. Sauvegarder `/etc/hosts` avant toute modification en production :
```bash
sudo cp -a /etc/hosts /etc/hosts.bak-$(date +%F)
```
👉 Explication : Permet un retour arrière immédiat si une erreur de syntaxe bloque la résolution locale.

## ✅ Validation et retour arrière

- **Précontrôles** : accès console hyperviseur, enregistrements DNS A et PTR prêts, sauvegarde de `/etc/hosts`.
- **Validation** : `hostnamectl status --static` affiche le nom court ; `hostname -f` affiche le FQDN ; redémarrer une fois et vérifier que le nom est identique.
- **Retour arrière** : `sudo hostnamectl set-hostname <ancien_nom>`, puis restaurer `/etc/hosts` depuis `/etc/hosts.bak-<date>`.