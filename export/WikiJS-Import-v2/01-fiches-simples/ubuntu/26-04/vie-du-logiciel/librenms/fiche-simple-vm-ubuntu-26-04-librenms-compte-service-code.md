---
title: "Fiche Simple - VM Ubuntu 26.04 LibreNMS Compte Service Code"
description: "Créer l'utilisateur librenms, récupérer le code et poser les permissions."
published: true
date: 2026-10-29T20:14:10Z
tags: ["ubuntu2604", "librenms", "snmpv3", "nginx", "mariadb"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Ubuntu_26.04_LibreNMS_Compte_Service_Code.md

- **Environnement** : VM Ubuntu Server 26.04 dédiée à LibreNMS (Nginx, PHP-FPM, MariaDB, SNMP)
- **OS / Version** : Ubuntu Server 26.04 LTS; LibreNMS 26.10.2; PHP 8.5
- **Catégorie** : supervision / installation
- **Tags** : `ubuntu2604`, `librenms`, `snmpv3`, `nginx`, `mariadb`

---

## Problème précis à résoudre

Créer l'utilisateur `librenms`, récupérer le code et poser les permissions.

## 1. Hors-Production (Lab / Test / POC)

1. Créer le compte de service :
   ```bash
   sudo useradd librenms -d /opt/librenms -M -r -s "$(which bash)"
   ```
   👉 Explication : Crée un compte système sans répertoire personnel pour exécuter LibreNMS (non root).

2. Cloner le code :
   ```bash
   cd /opt
   sudo git clone --branch 26.10.2 --depth 1 https://github.com/librenms/librenms.git
   ```
   👉 Explication : Récupère la version figée 26.10.2 du code.

3. Poser propriétaire et droits :
   ```bash
   sudo chown -R librenms:librenms /opt/librenms
   sudo chmod 771 /opt/librenms
   ```
   👉 Explication : Donne la propriété du dossier au compte de service.

4. Définir les ACL :
   ```bash
   sudo setfacl -d -m g::rwx /opt/librenms/rrd /opt/librenms/logs \
     /opt/librenms/bootstrap/cache /opt/librenms/storage
   sudo setfacl -R -m g::rwx /opt/librenms/rrd /opt/librenms/logs \
     /opt/librenms/bootstrap/cache /opt/librenms/storage
   ```
   👉 Explication : Autorise le groupe à écrire dans les répertoires de données.

5. Installer les dépendances PHP :
   ```bash
   sudo -u librenms /opt/librenms/scripts/composer_wrapper.php install --no-dev
   ```
   👉 Explication : Installe les dépendances PHP avec le compte non-root.

## 2. Production — Contrôles

Garder la version 26.10.2 figée; consigner le commit déployé.

## 3. Production — Sécurité

- Ne jamais exécuter composer ni l'application en root.

## Validation et retour arrière

- **Validation** : `/opt/librenms` appartient à `librenms` et composer termine sans erreur.
- **Retour arrière** : `sudo rm -rf /opt/librenms` et `sudo userdel librenms` si l'installation est abandonnée (vérifier le chemin avant), ou restaurer le snapshot.

## Si le problème n'est pas résolu

- [LibreNMS — Installation](https://docs.librenms.org/Installation/Install-LibreNMS/)
- [Guide complet — étape 3](/02-fiches-completes/ubuntu/26-04/installation-deploiement/46-deploiement-librenms-26-10-2-ubuntu-26-04#3-creer-le-compte-de-service-et-installer-le-code)