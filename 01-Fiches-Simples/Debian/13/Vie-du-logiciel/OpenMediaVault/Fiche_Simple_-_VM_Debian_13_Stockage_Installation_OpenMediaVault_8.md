# Fiche simple — Debian 13 : installer OpenMediaVault 8

- **OS / Version** : VM ou serveur dédié Debian 13 Trixie minimal
- **Catégorie** : Stockage / NAS / SMB
- **Tags** : `[debian13]`, `[openmediavault8]`, `[omv]`, `[nas]`, `[smb]`, `[stockage]`

## Avant de commencer

Cette installation prend la main sur plusieurs services Debian, notamment le réseau, SSH, Nginx et Samba. L'utiliser sur un hôte dédié, sans environnement graphique ni serveur Web existant, avec accès console et sauvegarde. OpenMediaVault n'est pas pris en charge dans LXC.

Prévoir un disque système et des disques de données distincts. Identifier les disques par numéro de série; ne rien effacer avant d'avoir confirmé le périphérique et sauvegardé son contenu.

## Installer OMV 8

Confirmer Debian 13 et le DNS, installer `systemd-resolved` et la clé APT officielle, puis ajouter le dépôt stable `synchrony` selon la documentation OMV :

```bash
cat /etc/os-release
getent hosts packages.openmediavault.org
sudo apt install --yes systemd-resolved psmisc gnupg
sudo systemctl enable --now systemd-resolved.service
```
   👉 Explication : contrôle l'OS (Debian 13), la résolution du dépôt OMV et installe les prérequis.

Installer la clé depuis `https://packages.openmediavault.io/archive.key` dans `/usr/share/keyrings/openmediavault-archive-keyring.gpg`, ajouter le dépôt signé `synchrony main`, puis installer `openmediavault` avec la commande officielle et ses options `dpkg`.

Après l'installation :

```bash
sudo omv-confdbadm populate
sudo omv-firstaid
```
   👉 Explication : initialise la base de configuration OMV; `omv-firstaid` ouvre l'assistant de réparation réseau.

Utiliser la console pendant la première configuration réseau : l'adresse IP peut changer à l'application. Changer les identifiants initiaux de l'interface Web et limiter l'accès à un réseau d'administration.

## Intégrer le disque et créer un partage

```bash
lsblk -o NAME,SIZE,MODEL,SERIAL,FSTYPE,MOUNTPOINTS
```
   👉 Explication : liste les disques par modèle et numéro de série pour choisir le bon avant de créer un système de fichiers.

Dans l'interface OMV, créer ou monter le système de fichiers du disque de données sous `Storage | File Systems`, puis créer un dossier partagé. Configurer les utilisateurs et permissions dans OMV avant d'activer SMB/CIFS. Appliquer les changements en attente et tester avec un client pilote, y compris un compte non autorisé qui doit être refusé.

Ne pas ajouter les montages ou les partages dans les fichiers gérés d'OMV. Ne pas traiter RAID comme une sauvegarde.

## Vérification et retour arrière

Vérifier l'adresse IP, l'accès Web, le montage et les journaux après redémarrage. Avant toute mise à niveau, confirmer une sauvegarde de données restaurable sur un autre support. Si l'installation ou le réseau échoue, utiliser la console locale et `omv-firstaid`; ne pas effacer les disques pour corriger un problème logiciel.

## Source

- [OpenMediaVault 8 — Installation sur Debian](https://docs.openmediavault.org/en/latest/installation/on_debian.html)
- Guide complet : `02-Fiches-Completes/Debian-13/Installation-Deploiement/66_Deploiement_OpenMediaVault_8_Debian_13.md`