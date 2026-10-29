---
title: "Fiche Simple - VM Debian 13 Snort Configurer"
description: "Configurer le capteur en détection uniquement et avec le réseau HOMENET approuvé."
published: true
date: 2026-10-29T20:38:44Z
tags: ["snort", "debian13", "vie-du-logiciel", "configurer"]
editor: markdown
dateCreated: 2026-10-29T20:38:44Z
dateModified: 2026-10-29T20:38:44Z
---

# Fiche_Simple_-_VM_Debian_13_Snort_Configurer

- **Environnement** : VM Debian 13 dédiée à Snort IDS passif
- **OS / Version** : Debian 13 Trixie; version des dépôts à vérifier sur l’hôte
- **Catégorie** : Snort IDS passif / configurer
- **Tags** : `snort`, `debian13`, `vie-du-logiciel`, `configurer`

---

## Problème précis à résoudre

Configurer le capteur en détection uniquement et avec le réseau HOME_NET approuvé.

## 1. Hors-Production (Lab / Test / POC)

1. Identifier le fichier installé et en faire une copie avant édition :
   ```bash
   SNORT_CONFIG=/ETC/SNORT/SNORT.CONF
   sudo cp -a "$SNORT_CONFIG" "$SNORT_CONFIG.before-change"
   sudoedit "$SNORT_CONFIG"
   ```
   👉 Explication : Remplacer SNORT_CONFIG par le chemin découvert avec dpkg-query; selon la branche il peut s’agir de snort.conf ou snort.lua.

2. Régler HOME_NET et le chargement des règles locales dans le format de la version installée.
   👉 Explication : Ne conserver que les réseaux autorisés et des règles approuvées; ne pas ajouter de mode inline ni de blocage.

3. Valider la syntaxe avec le chemin réellement identifié :
   ```bash
   SNORT_CONFIG=/ETC/SNORT/SNORT.CONF
   sudo snort -T -c "$SNORT_CONFIG"
   ```
   👉 Explication : Remplacer la valeur de SNORT_CONFIG par le chemin local. Le test doit terminer sans erreur.

## 2. Production — Contrôles

Faire relire HOME_NET, règles et sortie d’alerte par le propriétaire; vérifier les options supportées par la branche détectée.

## 3. Production — Sécurité

- Séparer interfaces de gestion/capture et conserver une configuration passive; désactiver toute action automatique.

## Validation et retour arrière

- **Validation** : Configuration testée; capteur non démarré.
- **Retour arrière** : restaurer la configuration antérieure vérifiée et arrêter le service ou la capture si la recette échoue; consigner le changement.

## Si le problème n’est pas résolu

- [Snort IDS passif — documentation officielle](https://www.snort.org/documents)
- [Étape suivante du guide](/01-fiches-simples/debian/13/vie-du-logiciel/snort/fiche-simple-vm-debian-13-snort-securiser)