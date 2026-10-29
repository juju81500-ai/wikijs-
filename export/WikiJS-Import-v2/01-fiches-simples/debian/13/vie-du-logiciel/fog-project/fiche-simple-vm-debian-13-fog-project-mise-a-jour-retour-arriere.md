---
title: "Fiche Simple - VM Debian 13 FOG Project Mise A Jour Retour Arriere"
description: "Mettre à jour FOG de façon contrôlée avec un retour arrière préparé."
published: true
date: 2026-10-29T20:39:58Z
tags: ["debian13", "fog-project", "mise-a-jour", "retour-arriere", "maintenance"]
editor: markdown
dateCreated: 2026-10-29T20:39:58Z
dateModified: 2026-10-29T20:39:58Z
---

# Fiche_Simple_-_VM_Debian_13_FOG_Project_Mise_A_Jour_Retour_Arriere

- **Environnement** : VM Debian 13 dédiée FOG Project (clonage/déploiement d'images), réseau de laboratoire isolé
- **OS / Version** : Debian 13 Trixie; FOG Project (version et support Debian 13 à vérifier)
- **Catégorie** : automatisation / déploiement
- **Tags** : `debian13`, `fog-project`, `mise-a-jour`, `retour-arriere`, `maintenance`

---

## Problème précis à résoudre

Mettre à jour FOG de façon contrôlée avec un retour arrière préparé.

## 1. Hors-Production (Lab / Test / POC)

1. Lire les notes de version FOG et vérifier la compatibilité avec Debian 13.
   👉 Explication : ne pas mettre à jour sans confirmation de compatibilité.

2. Sauvegarder (voir fiche Sauvegarder_Restaurer) et prendre un instantané de la VM.
   👉 Explication : point de retour obligatoire.

3. Récupérer et se placer sur l'étiquette cible (VERSION_FOG_CIBLE à remplacer) :
   ```bash
   cd ~/fogproject
   git fetch --tags
   git checkout VERSION_FOG_CIBLE
   ```
   👉 Explication : utiliser une étiquette de version publiée, pas une branche instable.

4. Relancer l'installeur en mode mise à jour :
   ```bash
   cd bin
   sudo ./installfog.sh
   ```
   👉 Explication : l'installeur détecte l'installation existante ; lire attentivement les invites.

5. Valider avec la fiche Valider sur le poste pilote.
   👉 Explication : vérifier démarrage PXE, capture et déploiement.

## 2. Production — Contrôles

Production : fenêtre de maintenance, déploiements suspendus, sauvegarde et instantané réalisés, communication aux équipes.

## 3. Production — Sécurité

- Ne pas mettre à jour pendant un déploiement actif.
- Vérifier l'origine du dépôt Git (HTTPS officiel).
- Conserver l'ancien jeu de sauvegardes jusqu'à validation.

## Validation et retour arrière

- **Validation** : version affichée dans l'interface conforme, services actifs, pilote réussi.
- **Retour arrière** : restaurer l'instantané de VM ; à défaut, réinstaller la version précédente et restaurer la base sauvegardée.

## Si le problème n'est pas résolu

- [Documentation officielle FOG Project](https://docs.fogproject.org/)
- [Dépôt officiel FOG Project](https://github.com/FOGProject/fogproject)
- [Fiche d'entrée FOG Project](/01-fiches-simples/logiciels/09-automatisation-deploiement-et-iac/fiche-logiciel-fog-project)
- [Fiche Sauvegarder_Restaurer](/01-fiches-simples/debian/13/vie-du-logiciel/fog-project/fiche-simple-vm-debian-13-fog-project-sauvegarder-restaurer)
- [Fiche Valider](/01-fiches-simples/debian/13/vie-du-logiciel/fog-project/fiche-simple-vm-debian-13-fog-project-valider)