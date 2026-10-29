---
title: "Sauvegarder et restaurer Ubuntu Server avec Restic"
description: "Fiche simple : [définir les données et le dépôt](../../../../01-Fiches-Simples/Ubuntu/Toutes-versions/Vie-du-logiciel/Restic/FicheSimple-VMUbuntuResticDefinirDonneesDepot.md)."
published: true
date: 2026-10-29T20:14:10Z
tags: ["ubuntu-server", "ubuntu-24.04", "ubuntu-26.04", "restic", "sauvegarde", "restauration"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Sauvegarder et restaurer Ubuntu Server avec Restic

- **Type de fiche** : Autres — sauvegarde / reprise
- **Environnement** : VM ou serveur dédié avec dépôt de sauvegarde hors hôte
- **OS / Version** : Ubuntu Server 24.04 LTS ou 26.04 LTS
- **Rôle** : Mettre en place des sauvegardes chiffrées, vérifiables et restaurables
- **Tags** : `ubuntu-server`, `ubuntu-24.04`, `ubuntu-26.04`, `restic`, `sauvegarde`, `restauration`

## 1. Définir les données et le dépôt

Fiche simple : [définir les données et le dépôt](/01-fiches-simples/ubuntu/toutes-versions/vie-du-logiciel/restic/fiche-simple-vm-ubuntu-restic-definir-donnees-depot).

Lister les chemins nécessaires, les bases de données, les données applicatives et les règles de rétention. Utiliser une destination indépendante du serveur (SFTP, stockage objet ou volume distant protégé); un autre répertoire du même disque ne constitue pas une sauvegarde.

Pour PostgreSQL/MariaDB, produire d'abord un dump cohérent avec les outils de la base. Pour les applications qui écrivent activement dans des fichiers, utiliser leur méthode de sauvegarde ou arrêter proprement le service pendant la capture.

## 2. Installer Restic et protéger le secret

Fiche simple : [installer Restic et protéger le secret](/01-fiches-simples/ubuntu/toutes-versions/vie-du-logiciel/restic/fiche-simple-vm-ubuntu-restic-installer-proteger-secret).

```bash
sudo apt update
apt-cache policy restic
sudo apt install restic
sudo -i
install -d -m 0700 /root/.config/restic
umask 077
openssl rand -base64 48 > /root/.config/restic/password
chmod 0600 /root/.config/restic/password
```

Vérifier que le paquet vient des dépôts approuvés. Garder une copie sécurisée du mot de passe dans le coffre de secrets : sans lui, les données chiffrées sont irrécupérables.

## 3. Initialiser le dépôt

Fiche simple : [initialiser le dépôt](/01-fiches-simples/ubuntu/toutes-versions/vie-du-logiciel/restic/fiche-simple-vm-ubuntu-restic-initialiser-depot).

Dans la session root, définir les valeurs correspondant au backend et à son secret d'accès :

```bash
export RESTIC_REPOSITORY=/mnt/backup/restic-ubuntu
export RESTIC_PASSWORD_FILE=/root/.config/restic/password
restic init
restic snapshots
```

N'exécuter `restic init` qu'une seule fois sur un dépôt neuf. Pour SFTP ou stockage objet, suivre la documentation Restic du backend choisi et isoler ses identifiants du mot de passe du dépôt.

## 4. Effectuer une sauvegarde

Fiche simple : [effectuer une sauvegarde](/01-fiches-simples/ubuntu/toutes-versions/vie-du-logiciel/restic/fiche-simple-vm-ubuntu-restic-effectuer-sauvegarde).

Vérifier le montage de destination, l'espace disponible et les dumps de bases. Sauvegarder les chemins validés sans inclure les pseudo-systèmes, les caches, les secrets temporaires ou un volume de base en cours d'écriture.

```bash
mountpoint -q /mnt/backup
df -h /mnt/backup
restic backup /etc /home /srv /var/backups --tag ubuntu-server
restic snapshots
```

Adapter les chemins au serveur; cette commande ne sauvegarde pas automatiquement toutes les données d'une application installée ailleurs.

## 5. Rétention et contrôle d'intégrité

Fiche simple : [appliquer rétention et contrôle d'intégrité](/01-fiches-simples/ubuntu/toutes-versions/vie-du-logiciel/restic/fiche-simple-vm-ubuntu-restic-retention-integrite).

Après avoir vérifié que plusieurs sauvegardes récentes existent et que la politique est conforme, appliquer une rétention documentée :

```bash
restic forget --tag ubuntu-server --keep-daily 7 --keep-weekly 5 --keep-monthly 12 --prune
restic check
```

`forget --prune` supprime des données devenues inutiles : planifier son exécution, suivre le résultat et conserver une rétention protégée contre l'altération si le backend le permet.

## 6. Restaurer sans écraser

Fiche simple : [restaurer sans écraser](/01-fiches-simples/ubuntu/toutes-versions/vie-du-logiciel/restic/fiche-simple-vm-ubuntu-restic-restaurer-sans-ecraser).

Lister les snapshots, choisir l'identifiant et restaurer d'abord vers une zone temporaire :

```bash
restic snapshots
restic restore <ID_SNAPSHOT> --target /mnt/restore-test
```

Contrôler propriétaires, permissions, complétude, cohérence des dumps et ouverture des fichiers. Restaurer ensuite les données en production avec le service arrêté et le plan de retour arrière préparé.

## 7. Exercices et exploitation

Fiche simple : [planifier exercices et exploitation](/01-fiches-simples/ubuntu/toutes-versions/vie-du-logiciel/restic/fiche-simple-vm-ubuntu-restic-exercices-exploitation).

- Planifier la sauvegarde après montage du backend et alerter sur échec, durée, taille et ancienneté du dernier snapshot.
- Tester une restauration complète d'un service en VM isolée à intervalles réguliers.
- Consigner dépôt, backend, mot de passe coffre, exclusions, rétention, opérateur et résultat.

## Sources

- [Restic — Documentation officielle](https://restic.readthedocs.io/en/stable/)
- [Ubuntu — Documentation serveur](https://documentation.ubuntu.com/server/)