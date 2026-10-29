---
title: "Fiche Simple - Appliance OPNsense Installation Assistant Initial"
description: "Terminer l'assistant web avec des paramètres approuvés et mettre à jour le système."
published: true
date: 2026-10-29T20:22:42Z
tags: ["opnsense", "installation", "pare-feu", "wan", "lan"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# Fiche_Simple_-_Appliance_OPNsense_Installation_Assistant_Initial.md

- **Environnement** : Appliance physique ou VM dédiée avec interfaces réseau identifiées
- **OS / Version** : OPNsense Community ou Business Edition, release maintenue compatible avec la plateforme
- **Catégorie** : pare-feu / configuration initiale
- **Tags** : `opnsense`, `installation`, `pare-feu`, `wan`, `lan`

---

## Problème précis à résoudre

Terminer l'assistant web avec des paramètres approuvés et mettre à jour le système.

## 1. Hors-Production (Lab / Test / POC)

1. Depuis un poste d'administration dédié, ouvrir **https://adresse-LAN** (adresse LAN à remplacer) puis lancer l'assistant **System > Wizard > General setup**.
   👉 Explication : ouvre l'interface web d'administration.

2. Définir un mot de passe administrateur unique, le nom d'hôte, le domaine, la zone horaire, les DNS, le type d'adressage WAN et le plan IP LAN.
   👉 Explication : remplace les paramètres temporaires par ceux approuvés; vérifier l'absence de conflit d'adresse.

3. Lire les notes de version puis **System > Firmware > Status > Check for updates** et appliquer la mise à jour.
   👉 Explication : passe sur une version maintenue avant toute exposition externe.

4. Exporter la configuration : **System > Configuration > Backups > Download configuration**, avec chiffrement par mot de passe.
   👉 Explication : première sauvegarde protégée dès que l'administration est stable.

5. Vérifier la version :
   ```sh
   opnsense-version
   ```
   👉 Explication : Dans le shell de la console, affiche la version installée.

## 2. Production — Contrôles

Valider le plan IP et le mot de passe dans le coffre.

## 3. Production — Sécurité

- Mot de passe unique saisi dans l'interface, jamais en argument.
- Protéger le fichier de configuration exporté (il contient des secrets).

## Validation et retour arrière

- **Validation** : assistant terminé, version à jour, configuration exportée.
- **Retour arrière** : restaurer la configuration exportée via **System > Configuration > Backups > Restore** ou revenir au snapshot.

## Si le problème n'est pas résolu

- [OPNsense — Installation](https://docs.opnsense.org/manual/install.html)
- [OPNsense — Configuration initiale](https://docs.opnsense.org/manual/setup.html)
- [Guide complet — étape 3](/02-fiches-completes/opnsense/toutes-versions/installation-deploiement/33-installation-appliance-opnsense-production#3-effectuer-lassistant-initial)