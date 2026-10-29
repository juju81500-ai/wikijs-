---
title: "OpenVAS"
description: "Installer la plateforme OpenVAS (Greenbone) sur Debian 12, vérifier qu'elle démarre et que ses flux de vulnérabilités sont chargés, puis la durcir (interface accessible uniquement en interne, mot de passe administrateur changé). Ne lancer des analyses que sur des cibles autorisées par écrit, et uniq"
published: true
date: 2026-10-29T12:25:08Z
tags: ["[debian-12]", "[openvas]", "[gvm]", "[scan-vulnerabilites]", "[hardening]"]
editor: markdown
dateCreated: 2026-10-29T12:25:08Z
dateModified: 2026-10-29T12:25:08Z
---

# 📄 OpenVAS

- **Environnement** : VM (Debian 12)
- **OS / Version** : Debian 12 (bookworm)
- **Version** : Greenbone Vulnerability Management (paquet `gvm` des dépôts Debian 12, version à vérifier sur la version déployée)
- **Catégorie** : Réseau et cybersécurité
- **Tags** : `[debian-12]`, `[openvas]`, `[gvm]`, `[scan-vulnerabilites]`, `[hardening]`

## 🎯 Objectif
Installer la plateforme OpenVAS (Greenbone) sur Debian 12, vérifier qu'elle démarre et que ses flux de vulnérabilités sont chargés, puis la durcir (interface accessible uniquement en interne, mot de passe administrateur changé). Ne lancer des analyses que sur des cibles autorisées par écrit, et uniquement sur votre propre réseau de test ou sur le périmètre validé par le responsable sécurité.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation du paquet GVM :
```bash
sudo apt update
sudo apt install -y gvm
```
👉 Explication : Installe la plateforme (gvmd, interface web gsad, scanneur ospd-openvas) depuis les dépôts Debian 12. Le téléchargement est long et volumineux.

2. Initialisation automatique (certificats, base de données, flux) :
```bash
sudo gvm-setup
```
👉 Explication : Crée les certificats, la base PostgreSQL, l'utilisateur administrateur et télécharge les flux de vulnérabilités. À la fin, la commande affiche le mot de passe généré pour `admin` : le noter immédiatement, il n'est pas réaffiché.

3. Contrôle de l'installation :
```bash
sudo gvm-check-setup
```
👉 Explication : Vérifie les composants (gvmd, scanneur, flux, connexion web). Les lignes d'erreur indiquent le composant à corriger, à lire avant de passer à l'étape suivante.

4. Contrôle des services :
```bash
systemctl status gvmd --no-pager
systemctl status ospd-openvas --no-pager
systemctl status gsad --no-pager
```
👉 Explication : Confirme que les trois services sont `active (running)`. Les noms exacts des unités peuvent varier selon la version du paquet, à vérifier sur la version déployée.

5. Accès à l'interface web :
```bash
curl -k -I https://127.0.0.1:9392/
```
👉 Explication : Vérifie que l'interface répond sur le port 9392 (`HTTP/1.1 200 OK` attendu). Dans un navigateur, ouvrir `https://127.0.0.1:9392` et se connecter avec `admin` et le mot de passe noté à l'étape 2. L'option `-k` n'accepte que le certificat auto-signé du lab.

---

## ⚡ 2. Production — Façon Simplifiée
1. Ouverture du port de l'interface pour le poste d'administration uniquement :
```bash
sudo apt install -y ufw
sudo ufw allow from <adresse_ip_admin> to any port 22 proto tcp
sudo ufw allow from <adresse_ip_admin> to any port 9392 proto tcp
sudo ufw enable
sudo ufw status verbose
```
👉 Explication : Le port 9392 n'est ouvert que pour le poste d'administration. Autoriser SSH avant `ufw enable` évite de perdre l'accès.

2. Création d'un compte d'analyse dédié (sans droit administrateur) :
```bash
sudo runuser -u _gvm -- gvmd --create-user=scan_operateur --role=User
sudo runuser -u _gvm -- gvmd --user=scan_operateur --new-password='<mot_de_passe_fort>'
```
👉 Explication : Crée un compte `scan_operateur` avec le rôle `User` pour les analyses courantes, sans droits d'administration de la plateforme. `<mot_de_passe_fort>` est un mot de passe unique d'au moins 20 caractères, saisi depuis un gestionnaire de mots de passe.

3. Planification des flux de vulnérabilités :
```bash
sudo runuser -u _gvm -- greenbone-feed-sync --type GVMD_DATA
sudo runuser -u _gvm -- greenbone-feed-sync --type SCAP
sudo runuser -u _gvm -- greenbone-feed-sync --type CERT
```
👉 Explication : Met à jour les données de vulnérabilités. La commande `greenbone-feed-sync` et ses types de flux sont à vérifier sur la version déployée. Une mise à jour hebdomadaire via cron est recommandée.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Changement du mot de passe administrateur et désactivation des comptes inutiles :
```bash
sudo runuser -u _gvm -- gvmd --user=admin --new-password='<mot_de_passe_admin_fort>'
sudo runuser -u _gvm -- gvmd --get-users --verbose
```
👉 Explication : Remplace le mot de passe généré par un mot de passe fort conservé dans un coffre-fort. `--get-users` liste les comptes existants : tout compte de test doit être supprimé avec `gvmd --delete-user=<nom_compte>`.

2. Restriction de l'écoute de l'interface au seul reverse proxy ou à l'interface interne :
```bash
sudo ls /etc/default/gsad
sudo ss -tlnp | grep 9392
```
👉 Explication : Vérifie sur quelle interface gsad écoute (`ss` affiche l'adresse). Le port ne doit pas être ouvert vers Internet. La modification de l'adresse d'écoute se fait dans le fichier de configuration de gsad, à vérifier sur la version déployée.

3. Restriction des droits sur les certificats et la configuration :
```bash
sudo ls -l /var/lib/gvm/CA/ /var/lib/gvm/private/
sudo chmod 700 /var/lib/gvm/private
```
👉 Explication : Limite l'accès à la clé privée du serveur à son propriétaire. Une clé lisible par d'autres comptes compromettrait l'interface web.

4. Sauvegarde de la base avant mise à jour :
```bash
sudo runuser -u _gvm -- gvmd --backup
sudo ls -l /var/lib/gvm/backup/ 2>/dev/null
```
👉 Explication : Crée une sauvegarde des données de la plateforme. Le répertoire de sortie est à vérifier sur la version déployée. Les sauvegardes contiennent les résultats d'analyse et les identifiants : les stocker hors du serveur, dans un coffre-fort (voir la fiche Passbolt ou Vaultwarden du pack).

---