---
title: "Fiche Simple - Ubuntu 24.04 Nakivo Transporter Securiser"
description: "Réduire l’exposition du serveur Ubuntu 24.04 utilisé par le Transporter et protéger les communications et les comptes de service."
published: true
date: 2026-10-29T21:11:01Z
tags: ["ubuntu-24.04", "nakivo", "transporter", "transporter-securiser"]
editor: markdown
dateCreated: 2026-10-29T21:11:01Z
dateModified: 2026-10-29T21:11:01Z
---

# Fiche_Simple_-_Ubuntu_24.04_Nakivo_Transporter_Securiser

- **Environnement** : Ubuntu Server 24.04 LTS x64; NAKIVO Backup & Replication Transporter
- **OS / Version** : Ubuntu Server 24.04 LTS — explicitement listé dans les exigences NAKIVO consultées; valider la version du produit
- **Catégorie** : sauvegarde / sécurité
- **Tags** : `ubuntu-24.04`, `nakivo`, `transporter`, `transporter-securiser`

---

## Problème précis à résoudre

Réduire l’exposition du serveur Ubuntu 24.04 utilisé par le Transporter et protéger les communications et les comptes de service.

## 1. Hors-Production (Lab / Test / POC)

1. Autoriser seulement les flux explicitement requis par la version NAKIVO et le mode de déploiement retenu.
   👉 Explication : ouvrir les ports strictement nécessaires entre les systèmes concernés; relever leurs numéros dans les exigences de déploiement de la version courante, sans déduire ceux du système protégé.

2. Utiliser un compte d’administration dédié avec les privilèges nécessaires; conserver les identifiants dans le coffre approuvé, jamais dans cette fiche.
   👉 Explication : l’accès SSH permet l’administration distante du serveur.

3. Éviter d’autoriser l’accès SSH root si un compte avec sudo répond aux exigences NAKIVO; si root est retenu, appliquer les exigences de l’éditeur et une restriction réseau renforcée.
   👉 Explication : certains parcours NAKIVO peuvent requérir des permissions précises; ne pas modifier la configuration SSH sans procédure de changement.

4. Maintenir Ubuntu et le produit NAKIVO à jour selon leurs guides respectifs; sauvegarder la configuration et vérifier les alertes.
   👉 Explication : la fiche ne fixe pas de cadence ni de commande de mise à jour non fournie par l’éditeur.

## 2. Production — Contrôles

Prévoir une fenêtre de changement, une sauvegarde de configuration, des règles réseau restreintes et un test de restauration avant l’usage en production.

## 3. Production — Sécurité

- Garder le système et le Transporter dans le périmètre de mises à jour approuvé.
- Ne pas exposer SSH ou l’interface NAKIVO sur Internet sans architecture de sécurité explicitement approuvée.
- Ne jamais copier de secrets ou de clés privées dans les fiches ou journaux partagés.

## Validation et retour arrière

**Validation** : filtrage des ports vérifié, accès nominatif documenté, comptes et clés protégés, journaux de sécurité contrôlés.
- **Retour arrière** : rétablir les règles réseau précédentes approuvées si un flux requis a été bloqué; réévaluer avant réouverture.

## Si le problème n’est pas résolu

- [NAKIVO — Deployment Requirements](https://helpcenter.nakivo.com/User-Guide/Content/Deployment/System-Requirements/Deployment-Requirements.htm)
- [Ubuntu — Security documentation](https://ubuntu.com/security)
- [Fiche d’entrée NAKIVO / Altaro](/01-fiches-simples/logiciels/07-sauvegarde-restauration-et-pra-pca/fiche-logiciel-nakivo-altaro)