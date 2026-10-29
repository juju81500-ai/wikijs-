---
title: "FreeRADIUS"
description: "Fiche défensive d’administration et de gouvernance. Elle ne remplace pas le guide éditeur spécifique à la version déployée et ne fournit pas de procédure offensive."
published: true
date: 2026-10-29T15:52:23Z
tags: ["logiciel", "04-Reseau-et-cybersecurite", "defensif", "administration", "gouvernance"]
editor: markdown
dateCreated: 2026-10-29T15:52:23Z
dateModified: 2026-10-29T15:52:23Z
---

# 📄 FreeRADIUS

- **Catégorie** : Réseau et cybersécurité
- **Plateforme** : Linux
- **Produit (matrice)** : FreeRADIUS
- **Statut dans le pack** : Documentation défensive — administration et gouvernance
- **Tags** : `logiciel`, `04-Reseau-et-cybersecurite`, `defensif`, `administration`, `gouvernance`

## 📚 Couverture dans le pack

Fiche défensive d’administration et de gouvernance. Elle ne remplace pas le guide éditeur spécifique à la version déployée et ne fournit pas de procédure offensive.

## 🧭 Périmètre

Complément à la fiche Debian existante. Déclarer uniquement les équipements réseau autorisés, attribuer un secret unique par équipement et le protéger; privilégier EAP-TLS/certificats pour les usages compatibles, protéger les clés et suivre leur renouvellement. Limiter les interfaces d’écoute et flux réseau aux besoins documentés, supprimer comptes de test et secrets par défaut, centraliser les journaux et protéger les données d’authentification.

## ✅ Autorisation et préparation

Avant toute modification, consigner le propriétaire du service, les actifs et utilisateurs concernés, le ticket de changement, l’approbateur, la fenêtre, les dépendances, les critères d’arrêt et la personne à contacter. Toute évaluation active ou action sur un terminal/équipement exige une autorisation écrite explicite, limitée au périmètre et à la durée approuvés. Sans accord, rester sur l’inventaire géré, les journaux et les contrôles de configuration passifs.

## 🔎 Validation

Valider syntaxe/configuration hors production, authentification d’un client pilote autorisé, rejet attendu des équipements non déclarés et réception des journaux. Pour rollback, restaurer la configuration sauvegardée avec permissions protégées; ne jamais recopier les secrets en clair dans un ticket. Vérifier aussi l’horodatage, la journalisation et l’absence de secrets dans les tickets ou exports; faire approuver le résultat par le propriétaire du service.

## ↩️ Retour arrière

Avant changement, conserver une sauvegarde ou un état de référence protégé, vérifier la possibilité réelle de restauration et garder un accès d’administration de secours approuvé. Si la validation échoue, interrompre le déploiement, restaurer la dernière configuration/package supporté selon la procédure éditeur, vérifier les services dépendants et consigner la cause. Ne pas improviser une procédure de restauration non documentée.

## 🚨 Alertes et remédiation

Préserver les journaux utiles, corréler avec les sources de supervision autorisées et ouvrir un incident/ticket attribué. Prioriser selon impact métier, exposition et avis éditeur; appliquer une correction supportée après validation, puis documenter le résultat. Toute action de confinement, révocation ou blocage doit suivre le plan d’incident approuvé et être traçable.

## 📚 Sources officielles

- [FreeRADIUS official documentation](https://www.freeradius.org/documentation/) — choisir la version, l’édition et le modèle correspondant au déploiement réel.
- [CIS Controls — documentation officielle](https://www.cisecurity.org/controls) — repères de gouvernance et gestion des actifs; adapter au contexte.

> Aucun numéro de version, niveau de licence ni prérequis produit n’est présumé dans cette fiche. Vérifier ces éléments dans le portail éditeur et le contrat de l’organisation avant toute mise en œuvre.