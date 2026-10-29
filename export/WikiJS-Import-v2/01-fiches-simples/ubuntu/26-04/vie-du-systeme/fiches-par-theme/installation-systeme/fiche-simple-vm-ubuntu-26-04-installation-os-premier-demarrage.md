---
title: "Fiche Simple - VM Ubuntu 26.04 Installation OS Premier Demarrage"
description: "Installer Ubuntu Server 26.04 LTS sur une nouvelle VM et vérifier les changements de base par rapport à 24.04 avant de reprendre une fiche ou un script plus ancien."
published: true
date: 2026-10-29T20:22:42Z
tags: ["[ubuntu26.04]", "[ubuntu]", "[resolute]", "[installation]", "[apt3]", "[systemd259]"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# 📄 Fiche_Simple_-_VM_Ubuntu_26.04_Installation_OS_Premier_Demarrage.md

- **Environnement** : VM ou serveur Ubuntu
- **OS / Version** : Ubuntu Server 26.04 LTS (Resolute Raccoon)
- **Catégorie** : Installation / Système / Compatibilité
- **Tags** : `[ubuntu26.04]`, `[ubuntu]`, `[resolute]`, `[installation]`, `[apt3]`, `[systemd259]`

## 🎯 Problème précis à résoudre
Installer Ubuntu Server 26.04 LTS sur une nouvelle VM et vérifier les changements de base par rapport à 24.04 avant de reprendre une fiche ou un script plus ancien.

> `26.04` est la série LTS. `.1`, `.2`, etc. désignent des images ponctuelles de la même série et ne changent pas le nom de suite APT.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Récupérer l'image Server officielle 26.04 LTS et vérifier l'empreinte publiée; vérifier aussi le support CPU de la VM.
2. Créer une VM avec firmware, disque et réseau adaptés au lab; l'installateur Subiquity peut configurer stockage, réseau et compte.
3. Après le premier démarrage, relever la base réellement installée :
   ```bash
   cat /etc/os-release
   uname -r
   python3 --version
   systemd --version
   apt --version
   netplan info
   apt-cache policy php-fpm postgresql nginx openssh-server chrony
   ```
4. Vérifier les services horaires et SSH :
   ```bash
   systemctl status chrony --no-pager
   systemctl list-unit-files 'ssh*'
   systemctl status ssh.socket ssh.service --no-pager
   ```
   👉 *Explication : sur une nouvelle installation Ubuntu 26.04, Chrony est le client NTP par défaut. La commande de statut SSH ne s'applique que si OpenSSH Server est installé; l'activation peut être gérée par socket.*

## ⚡ 2. Production — Façon Simplifiée
1. Confirmer l'image ponctuelle, l'architecture CPU, les pilotes, le stockage et le propriétaire cloud-init du réseau.
2. Appliquer les mises à jour de la suite `resolute`; ne pas reprendre d'anciens dépôts Noble ni mélanger `noble` et `resolute`.
3. Installer explicitement les versions requises par l'application (par exemple PHP 8.5 ou PostgreSQL 18 seulement si elles sont bien celles requises et proposées par les dépôts actifs).
4. Reprendre Netplan et systemd après vérification : Netplan 1.2, systemd 259, APT 3.1 et noyau GA 7.0 diffèrent de 24.04.

## 🔒 3. Production — Façon Sécurisée
1. Ne pas utiliser `apt-key`; APT 3 l'a supprimé. Pour un dépôt tiers indispensable, suivre la documentation actuelle avec une clé dédiée et `Signed-By`.
2. Tester les scripts sur APT 3 et les coreutils actualisés avant de les lancer en production; ne pas basculer les variantes coreutils sans test.
3. Ne pas supposer que les procédures 24.04 de Chrony, OpenLDAP, Postfix, Dovecot, Samba ou `initramfs-tools` s'appliquent telles quelles.

## ✅ Validation et retour arrière
- Confirmer suite APT `resolute`, versions système, réseau/DNS, Chrony, SSH, services et sécurité après redémarrage.
- Tester une restauration de VM en réseau isolé avant déploiement de données métier.
- En cas d'échec, restaurer la VM ou revenir à l'image/configuration précédente; ne pas rétrograder APT avec un mélange de suites.

## 🔗 Sources officielles
- [Ubuntu 26.04 LTS — résumé des changements](https://documentation.ubuntu.com/release-notes/26.04/summary-for-lts-users/)
- [Ubuntu 26.04 LTS — notes de version](https://documentation.ubuntu.com/release-notes/26.04/)