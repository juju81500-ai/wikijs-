---
title: "Fiche Simple - Ubuntu 24.04 Nakivo Transporter Prerequis"
description: "Vérifier qu’un hôte Ubuntu Server 24.04 LTS x64 remplit les prérequis publiés par NAKIVO pour héberger un Transporter Linux."
published: true
date: 2026-10-29T21:11:01Z
tags: ["ubuntu-24.04", "nakivo", "transporter", "transporter-prerequis"]
editor: markdown
dateCreated: 2026-10-29T21:11:01Z
dateModified: 2026-10-29T21:11:01Z
---

# Fiche_Simple_-_Ubuntu_24.04_Nakivo_Transporter_Prerequis

- **Environnement** : Ubuntu Server 24.04 LTS x64; NAKIVO Backup & Replication Transporter
- **OS / Version** : Ubuntu Server 24.04 LTS — explicitement listé dans les exigences NAKIVO consultées; valider la version du produit
- **Catégorie** : sauvegarde / prérequis
- **Tags** : `ubuntu-24.04`, `nakivo`, `transporter`, `transporter-prerequis`

---

## Problème précis à résoudre

Vérifier qu’un hôte Ubuntu Server 24.04 LTS x64 remplit les prérequis publiés par NAKIVO pour héberger un Transporter Linux.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier l’OS et l’architecture :
   ```bash
   . /etc/os-release && printf '%s %s\n' "$NAME" "$VERSION_ID"
   uname -m
   ```
   👉 Explication : la matrice NAKIVO de déploiement liste explicitement Ubuntu 24.04 Server LTS x64; `x86_64` est l’architecture attendue.

2. Vérifier la présence de SSH et l’accès réseau requis avant d’ajouter le Transporter :
   ```bash
   systemctl is-active ssh
   ```
   👉 Explication : vérifier le service SSH et les flux nécessaires au mode de déploiement retenu dans la documentation de la version courante.

3. Comparer les prérequis matériels, logiciels, ports et paquets requis à la page d’exigences NAKIVO de la version utilisée.
   👉 Explication : les exigences produit évoluent; ne pas appliquer une liste de paquets copiée d’une autre distribution.

4. Distinguer le système hébergeant le Transporter du système protégé par le job.
   👉 Explication : la matrice de déploiement NAKIVO supporte Ubuntu 24.04 Server LTS; consulter la fiche dédiée Debian 13 pour l’autre hôte supporté. La page « Supported Platforms » concerne séparément les systèmes physiques protégés et peut afficher des versions différentes.

## 2. Production — Contrôles

Prévoir une fenêtre de changement, une sauvegarde de configuration, des règles réseau restreintes et un test de restauration avant l’usage en production.

## 3. Production — Sécurité

- Garder le système et le Transporter dans le périmètre de mises à jour approuvé.
- Ne pas exposer SSH ou l’interface NAKIVO sur Internet sans architecture de sécurité explicitement approuvée.
- Ne jamais copier de secrets ou de clés privées dans les fiches ou journaux partagés.

## Validation et retour arrière

**Validation** : Ubuntu Server 24.04 LTS x64 apparaît dans la matrice de déploiement NAKIVO, SSH répond selon le plan réseau et les prérequis de la version sont consignés.
- **Retour arrière** : aucun changement n’est effectué.

## Si le problème n’est pas résolu

- [NAKIVO — Deployment Requirements (Director/Transporter platform)](https://helpcenter.nakivo.com/User-Guide/Content/Deployment/System-Requirements/Deployment-Requirements.htm)
- [NAKIVO — Installation on Linux](https://helpcenter.nakivo.com/User-Guide/Content/Deployment/Installing-NAKIVO-Backup-and-Replication/Installing-on-Linux/Installing-on-Linux.htm)
- [Fiche d’entrée NAKIVO / Altaro](/01-fiches-simples/logiciels/07-sauvegarde-restauration-et-pra-pca/fiche-logiciel-nakivo-altaro)