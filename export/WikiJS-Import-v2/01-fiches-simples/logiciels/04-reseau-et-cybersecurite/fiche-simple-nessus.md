---
title: "Nessus"
description: "Installer Nessus sur Debian 12, l'activer avec un code de licence, vérifier que le moteur répond et que les plugins sont chargés, puis le durcir (interface restreinte, comptes nominatifs, sauvegarde). Ne lancer des analyses que sur des cibles autorisées par écrit, uniquement sur votre réseau de test"
published: true
date: 2026-10-29T12:25:20Z
tags: ["[debian-12]", "[nessus]", "[tenable]", "[scan-vulnerabilites]", "[hardening]"]
editor: markdown
dateCreated: 2026-10-29T12:25:20Z
dateModified: 2026-10-29T12:25:20Z
---

# 📄 Nessus

- **Environnement** : VM (Debian 12)
- **OS / Version** : Debian 12 (bookworm)
- **Version** : Nessus 10.x (paquet .deb Tenable, numéro exact à vérifier sur la version déployée)
- **Catégorie** : Réseau et cybersécurité
- **Tags** : `[debian-12]`, `[nessus]`, `[tenable]`, `[scan-vulnerabilites]`, `[hardening]`

## 🎯 Objectif
Installer Nessus sur Debian 12, l'activer avec un code de licence, vérifier que le moteur répond et que les plugins sont chargés, puis le durcir (interface restreinte, comptes nominatifs, sauvegarde). Ne lancer des analyses que sur des cibles autorisées par écrit, uniquement sur votre réseau de test ou sur le périmètre validé par le responsable sécurité.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Téléchargement du paquet depuis le portail Tenable puis installation :
```bash
cd /tmp
sudo apt update
sudo apt install -y curl
sudo dpkg -i /tmp/Nessus-10.8.3-debian10_amd64.deb
```
👉 Explication : Installe le paquet téléchargé depuis le portail Tenable (nom et version à vérifier, le fichier doit être présent dans `/tmp`). Le paquet `debian10` est la version de build utilisée sur Debian 12. Les dépendances manquantes s'installent avec `sudo apt -f install`.

2. Démarrage du service et contrôle de son état :
```bash
sudo systemctl enable nessusd
sudo systemctl start nessusd
systemctl status nessusd --no-pager
```
👉 Explication : Active le démarrage automatique, lance le démon `nessusd` et affiche son état. La ligne `Active: active (running)` est attendue.

3. Activation avec le code de licence (Essentials ou Professional) :
```bash
sudo /opt/nessus/sbin/nessuscli fetch --register <code_activation_tenable>
```
👉 Explication : Enregistre l'installation auprès de Tenable. `<code_activation_tenable>` est le code reçu lors de l'inscription, à ne pas partager. Sans cette étape, l'interface reste bloquée.

4. Téléchargement des plugins (long, plusieurs centaines de Mo) puis contrôle de l'accès web :
```bash
sudo /opt/nessus/sbin/nessuscli update --all
curl -k -I https://127.0.0.1:8834/
```
👉 Explication : Charge les plugins de détection. La commande `curl` vérifie que l'interface répond sur le port 8834 (`HTTP/1.1 200 OK` attendu). Dans un navigateur, ouvrir `https://127.0.0.1:8834` et créer le compte administrateur demandé à la première connexion.

---

## ⚡ 2. Production — Façon Simplifiée
1. Ouverture du port de l'interface pour le poste d'administration uniquement :
```bash
sudo apt install -y ufw
sudo ufw allow from <adresse_ip_admin> to any port 22 proto tcp
sudo ufw allow from <adresse_ip_admin> to any port 8834 proto tcp
sudo ufw enable
sudo ufw status verbose
```
👉 Explication : Le port 8834 n'est ouvert que pour le poste d'administration. Autoriser SSH avant `ufw enable` évite de perdre l'accès.

2. Création d'un compte d'analyse nominatif :
```bash
sudo /opt/nessus/sbin/nessuscli adduser
```
👉 Explication : La commande demande interactivement le nom du compte, son mot de passe et son rôle. Créer un compte par opérateur plutôt qu'un compte partagé, pour garder la traçabilité des analyses.

3. Mise à jour régulière des plugins :
```bash
sudo /opt/nessus/sbin/nessuscli update --all
sudo systemctl restart nessusd
```
👉 Explication : Met à jour les plugins puis relance le démon. À planifier au moins une fois par semaine, par exemple avec une tâche cron.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Restriction des droits sur le répertoire d'installation :
```bash
sudo chmod 750 /opt/nessus
ls -ld /opt/nessus
```
👉 Explication : Seul root et le groupe propriétaire accèdent à l'installation, qui contient la configuration et les identifiants.

2. Contrôle de l'interface d'écoute :
```bash
sudo ss -tlnp | grep 8834
sudo /opt/nessus/sbin/nessuscli fix --list
```
👉 Explication : Vérifie que `nessusd` n'écoute que sur l'interface prévue. `fix --list` affiche les paramètres modifiables via `nessuscli fix --set <nom>=<valeur>`, à vérifier sur la version déployée.

3. Vérification des comptes et suppression des comptes de test :
```bash
sudo /opt/nessus/sbin/nessuscli lspasswd
```
👉 Explication : Liste les comptes locaux. Tout compte de test ou inutilisé doit être supprimé avec `sudo /opt/nessus/sbin/nessuscli rmuser <nom_compte>`. Le mot de passe administrateur initial doit être remplacé par un mot de passe fort.

4. Sauvegarde de la configuration avant toute mise à jour :
```bash
sudo tar czf /root/nessus-conf-$(date +%F).tgz /opt/nessus/etc/nessus
sudo ls -l /root/nessus-conf-*.tgz
```
👉 Explication : Archive la configuration de Nessus avec les comptes et les paramètres. Stocker l'archive hors du serveur, dans un coffre-fort (voir la fiche Passbolt ou Vaultwarden du pack), avec une lecture restreinte.

---