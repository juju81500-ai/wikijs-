---
title: "Assistance avec GLPI"
description: "- Solliciter la DSI via un canal structuré (web, mail, téléphone…)"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# Assistance avec GLPI
## 🎫 Le ticket : base de l’assistance

### Rôles

- Solliciter la DSI via un canal structuré (web, mail, téléphone…)
- Centraliser les demandes et incidents
- Suivre l’état d’avancement et la résolution
- Fournir des **indicateurs** pour la supervision et les statistiques

### Avantages

- Traçabilité complète
- Répartition équitable des tâches
- Communication fluide avec l’utilisateur
- Détection de problèmes récurrents

---

## 🔁 Cycle de vie d’un ticket dans GLPI

|Statut|Description|
|---|---|
|**Nouveau**|Ticket créé, non attribué|
|**En attente**|En attente d’informations, modification manuelle|
|**En cours attribué**|Assigné à un technicien ou groupe|
|**En cours planifié**|Tâche planifiée|
|**Résolu**|Solution apportée|
|**Clos**|Solution validée par le demandeur|

---

## 👤 Gestion des acteurs d’un ticket

### Attribution

- Techniciens ou groupes chargés du traitement
- Peut être manuel ou automatique selon critères
- Sert à gérer les **escalades fonctionnelles**

### Observateurs

- Ne traitent pas le ticket mais sont informés
- Ajout manuel ou automatique
- Utiles pour les **escalades hiérarchiques**

### Validation

- Par un **valideur** (profil spécifique)
- Peut être requise automatiquement ou manuellement
- Non bloquant, mais suivi important

---

## ⚙️ Traitement du ticket

Dans l’onglet **Traitement**, on peut :

- Ajouter un **suivi** (communication)
- Créer une **tâche** (planifiée)
- Renseigner une **solution**
- Joindre des **documents**

### Clôture

- Réalisée par le demandeur ou le technicien
- Peut être planifiée ou immédiate après résolution
- Motif obligatoire en cas de refus de clôture

---

## 🔗 Liaisons et CMDB

- Un ticket peut être lié à un ou plusieurs **CI** (Configuration Item)
- Cela facilite :
    - Le **diagnostic technique**
    - Les **statistiques d’incidents** par matériel ou logiciel
- Requiert une **CMDB bien tenue et à jour**

---

## 📚 Base de connaissances et FAQ

### Objectifs

- Partager les solutions entre techniciens
- Fournir une **FAQ** publique pour les utilisateurs

### Caractéristiques

|Élément|Description|
|---|---|
|**Articles**|Informations techniques internes ou publiques|
|**Cibles**|Définissent qui peut lire l’article (entité, profil, groupe, utilisateur)|
|**Validation**|Relecture, approbation, publication|
|**Liaison avec tickets**|Articles liés à des incidents/résolutions|

### FAQ

- Interface simplifiée pour les utilisateurs
- Accès rapide aux articles publics classés par catégories

---

## ✅ À retenir pour les révisions

- Le **ticket** est l’unité centrale de gestion des demandes/incidents
- Chaque ticket a un **cycle de vie**, des **acteurs**, et des **règles de traitement**
- L’**attribution** oriente le travail ; les **observateurs** suivent sans intervenir
- La **base de connaissances** permet de limiter les sollicitations inutiles

---

## 📌 Bonnes pratiques professionnelles

- Bien **renseigner chaque ticket** dès sa création (contexte, CI, type, priorité)
- Respecter les **SLA définis** pour les délais de traitement
- Associer les tickets aux **éléments du parc** pour une meilleure analyse
- Alimenter la **base de connaissances** dès qu’une solution utile est identifiée
- Utiliser la **FAQ** pour décharger le support niveau 1
- Réviser régulièrement les **tickets clos** pour enrichir la documentation