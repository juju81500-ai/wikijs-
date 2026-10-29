---
title: "Zenmap"
description: "Fiche défensive d’administration et de gouvernance. Elle ne remplace pas le guide éditeur spécifique à la version déployée et ne fournit pas de procédure offensive."
published: true
date: 2026-10-29T15:52:23Z
tags: ["logiciel", "04-Reseau-et-cybersecurite", "defensif-uniquement"]
editor: markdown
dateCreated: 2026-10-29T15:52:23Z
dateModified: 2026-10-29T15:52:23Z
---

# 📄 Zenmap

- **Catégorie** : Réseau et cybersécurité
- **Plateforme** : Multiplateforme
- **Produit (matrice)** : Nmap / Zenmap
- **Statut dans le pack** : Défensif uniquement
- **Tags** : `logiciel`, `04-Reseau-et-cybersecurite`, `defensif-uniquement`

## 📚 Couverture dans le pack

Fiche défensive d’administration et de gouvernance. Elle ne remplace pas le guide éditeur spécifique à la version déployée et ne fournit pas de procédure offensive.

## 🧭 Périmètre

Zenmap fournit une interface à un outil réseau à double usage. Cette fiche se limite à l’installation approuvée, à la gestion des postes opérateurs, à la conservation des profils et rapports et à la gouvernance d’une demande d’inventaire. Aucun profil, cible ou réglage d’exécution n’est recommandé. L’inventaire passif et les données de CMDB restent prioritaires; toute activité active exige une autorisation écrite précise et bornée.

## ✅ Autorisation et préparation

Avant toute modification, consigner le propriétaire du service, les actifs et utilisateurs concernés, le ticket de changement, l’approbateur, la fenêtre, les dépendances, les critères d’arrêt et la personne à contacter. Toute évaluation active ou action sur un terminal/équipement exige une autorisation écrite explicite, limitée au périmètre et à la durée approuvés. Sans accord, rester sur l’inventaire géré, les journaux et les contrôles de configuration passifs.

## 🔎 Validation

Vérifier l’identité de l’opérateur, la provenance officielle du logiciel et le stockage protégé des résultats. Confirmer avec le propriétaire du périmètre que l’autorisation couvre le besoin avant usage; interrompre selon le plan d’arrêt convenu. Révoquer les accès et supprimer les copies selon les règles de conservation. Vérifier aussi l’horodatage, la journalisation et l’absence de secrets dans les tickets ou exports; faire approuver le résultat par le propriétaire du service.

## ↩️ Retour arrière

Avant changement, conserver une sauvegarde ou un état de référence protégé, vérifier la possibilité réelle de restauration et garder un accès d’administration de secours approuvé. Si la validation échoue, interrompre le déploiement, restaurer la dernière configuration/package supporté selon la procédure éditeur, vérifier les services dépendants et consigner la cause. Ne pas improviser une procédure de restauration non documentée.

## 🚨 Alertes et remédiation

Préserver les journaux utiles, corréler avec les sources de supervision autorisées et ouvrir un incident/ticket attribué. Prioriser selon impact métier, exposition et avis éditeur; appliquer une correction supportée après validation, puis documenter le résultat. Toute action de confinement, révocation ou blocage doit suivre le plan d’incident approuvé et être traçable.

## 📚 Sources officielles

- [Nmap official documentation](https://nmap.org/book/zenmap.html) — choisir la version, l’édition et le modèle correspondant au déploiement réel.
- [CIS Controls — documentation officielle](https://www.cisecurity.org/controls) — repères de gouvernance et gestion des actifs; adapter au contexte.

> Aucun numéro de version, niveau de licence ni prérequis produit n’est présumé dans cette fiche. Vérifier ces éléments dans le portail éditeur et le contrat de l’organisation avant toute mise en œuvre.