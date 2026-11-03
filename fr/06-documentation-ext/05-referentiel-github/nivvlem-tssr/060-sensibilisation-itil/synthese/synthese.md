---
title: "📘 Synthèse – Sensibilisation à ITIL"
description: "- Cadre de bonnes pratiques pour la gestion des services IT"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# 📘 Synthèse – Sensibilisation à ITIL

## 🧱 Fondamentaux ITIL

### Qu’est-ce qu’ITIL ?

- Cadre de **bonnes pratiques** pour la gestion des services IT
- Objectif : **améliorer la qualité de service**, maîtriser les coûts, répondre aux besoins métiers
- ITIL 4 : approche modernisée intégrant **Agile**, **Lean** et **DevOps**

### Cadre de certification

- ITIL v3 : centré sur le **cycle de vie du service** (stratégie → conception → transition → exploitation → amélioration)
- ITIL 4 : basé sur les **4 dimensions** + **Système de valeur des services (SVS)**

---

## 📚 Cycle de vie des services ITIL (v3)

|Phase|Objectif principal|
|---|---|
|**Stratégie**|Aligner l’IT sur les besoins métiers|
|**Conception**|Formaliser la solution technique adaptée|
|**Transition**|Mettre en production sans perturber|
|**Exploitation**|Assurer la disponibilité et la qualité au quotidien|
|**Amélioration continue**|Optimiser durablement les services rendus|

---

## 🧩 Les fonctions et processus clés

### Fonctions (ITIL v3)

- **Centre de services (Service Desk)** : point de contact unique
- **Gestion technique** : infrastructures, réseaux, serveurs
- **Gestion des applications** : applicatifs métiers, support applicatif
- **Gestion des opérations** : ordonnancement, backups, impressions

### Processus principaux

- **Demande (requête)** : demandes standards, catalogue de services
- **Accès** : identifiants, mots de passe, droits
- **Incidents** : restauration rapide d’un service
- **Problèmes** : cause racine d’incidents récurrents, base des erreurs connues (KEDB)
- **Événements** : supervision technique, alertes, seuils

---

## 🧠 ITSM avec GLPI

### Ticketing

- Types : **incident** ou **demande**
- Cycle : **nouveau → en attente → attribué → planifié → résolu → clos**
- Acteurs : demandeur, technicien, observateur, valideur

### Outils intégrés

- CMDB (parc informatique)
- FAQ et base de connaissances
- Automatisations (attributions, escalades)
- Suivi de SLA

### Exploitation via TP

- Intégration complète d’un poste pour un salarié commercial : de la commande matériel à la clôture du ticket utilisateur

---

## 🧠 Soft skills & posture professionnelle

### Savoir – Connaissances

- Réseaux, systèmes, outils ITSM (GLPI, AD, O365)
- Documentation, veille, partage via base de connaissances

### Savoir-faire – Compétences

- Diagnostic, résolution technique
- Communication écrite et orale professionnelle
- Reformulation, écoute active, gestion de tickets

### Savoir-être – Aptitudes

- Empathie, patience, diplomatie
- Gestion des clients difficiles (agressifs, stressés, malhabiles)
- Adaptabilité, rigueur, esprit d’équipe

---

## ✅ À retenir pour les révisions

- ITIL est une **approche de gestion de service**, pas une méthode technique
- Le centre de services (service desk) est **le cœur de l’interaction utilisateur**
- **GLPI est un outil ITSM** conforme à ITIL, facilitant tickets, parc, documentation
- Chaque processus ITIL doit être **mesuré** (KPI, SLA, CSF)
- L'amélioration continue repose sur la **roue de Deming (PDCA)**

---

## 📌 Bonnes pratiques professionnelles

- Formaliser chaque demande via un ticket **complet et bien catégorisé**
- Lier systématiquement les **CI (matériel)** à chaque demande
- Alimenter la **base de connaissances** pour éviter les doublons
- Gérer les **droits et accès** dès l’arrivée d’un utilisateur
- Structurer la **documentation** (wiki, FAQ, modèles de tickets, etc.)
- Mesurer les délais, taux de satisfaction, taux de réouverture des tickets

---

## ❌ Pièges à éviter

- Confondre **incident** et **problème**
- Clôturer un ticket sans **validation utilisateur**
- Ignorer les suivis ou laisser des statuts incohérents dans GLPI
- Ne pas tenir à jour la CMDB (lieu, statut, affectation des CI)
- Oublier de documenter les solutions trouvées (perte de capital technique)