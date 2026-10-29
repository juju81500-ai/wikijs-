---
title: "Fiche Simple - Windows Server 2022 Nakivo Mettre A Jour Retour Arriere"
description: "Mettre à jour NAKIVO sans compromettre les jobs ou points de restauration et préparer un retour sûr."
published: true
date: 2026-10-29T20:47:51Z
tags: ["nakivo", "director", "transporter", "windows-server", "mise-a-jour", "retour-arriere"]
editor: markdown
dateCreated: 2026-10-29T20:47:51Z
dateModified: 2026-10-29T20:47:51Z
---

# Fiche_Simple_-_Windows_Server_2022_Nakivo_Mettre_A_Jour_Retour_Arriere

- **Environnement** : Windows Server 2022 exécutant NAKIVO Director et Transporter; fenêtre de maintenance approuvée
- **OS / Version** : Windows Server 2022; version NAKIVO à confirmer dans les notes officielles
- **Catégorie** : sauvegarde / maintenance
- **Tags** : `nakivo`, `director`, `transporter`, `windows-server`, `mise-a-jour`, `retour-arriere`

---

## Problème précis à résoudre

Mettre à jour NAKIVO sans compromettre les jobs ou points de restauration et préparer un retour sûr.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier dans **Activities** qu’aucun job n’est en cours; relever les versions Director, Transporter, dépôts et plateformes protégées.
   👉 Explication : l’ordre et la compatibilité des composants dépendent des notes de version.
2. Sauvegarder la configuration selon la procédure NAKIVO correspondant exactement à la version installée; vérifier que dépôts et sauvegardes restent accessibles.
   👉 Explication : copier le dossier d’installation ne garantit pas la restauration de la configuration.
3. Consulter le Help Center pour les prérequis, chemin de mise à niveau et éventuel retour arrière; télécharger uniquement depuis le portail officiel.
   👉 Explication : si la procédure de retour à la version précédente n’est pas documentée, arrêter avant le changement.
4. Dans une VM de test, suivre l’assistant graphique officiel; exécuter un job pilote puis une restauration de test.
   👉 Explication : aucun ordre universel des composants n’est présumé.
5. Consigner le résultat et conserver les preuves dans l’espace d’exploitation approuvé.
   👉 Explication : décider ensuite de poursuivre ou de suspendre le déploiement.

## 2. Production — Contrôles

- Prévoir fenêtre, capacité, dépendances, accès dépôt et procédure approuvée; suivre strictement les instructions éditeur.
- Ne pas restaurer une configuration ni interrompre un job en dehors d’une procédure documentée.

## 3. Production — Sécurité

- Utiliser des installateurs officiels et restreindre l’accès aux exports, journaux et dépôts.
- Ne jamais inclure secrets ou clés dans les comptes rendus.

## Validation et retour arrière

- **Validation** : Director et Transporters ont l’état attendu, un job pilote réussit et la restauration de test est vérifiée.
- **Retour arrière** : restaurer la configuration ou revenir à la version antérieure uniquement selon la procédure NAKIVO correspondant à cette version; à défaut, préserver dépôts et sauvegardes et contacter le support.

## Si le problème n'est pas résolu

- [NAKIVO — Help Center officiel](https://helpcenter.nakivo.com/)
- [NAKIVO — System Requirements](https://helpcenter.nakivo.com/display/NH/System+Requirements)
- [Fiche d’entrée du logiciel](/01-fiches-simples/logiciels/07-sauvegarde-restauration-et-pra-pca/fiche-logiciel-nakivo-altaro)