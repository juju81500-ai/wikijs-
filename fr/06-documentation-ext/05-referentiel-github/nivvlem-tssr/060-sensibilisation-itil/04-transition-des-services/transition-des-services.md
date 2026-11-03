---
title: "Transition des services"
description: "- Assurer la mise en production des services nouveaux ou modifiés"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# Transition des services
## 🧩 Rôle de la transition des services

- Assurer la **mise en production** des services nouveaux ou modifiés
- Gérer les **ressources**, respecter les **délais**, les **coûts**, et la **qualité**
- Intégrer les services conçus tout en assurant leur **continuité** et leur **exploitation**
- Produire la **documentation**, former les utilisateurs et assurer la surveillance

---

## 🔧 Processus de la transition des services

### 1. Gestion des changements (Change Management)

#### Objectifs

- Traiter les changements efficacement
- Réduire les interruptions et maximiser la valeur fournie
- Mettre à jour les CI dans le CMS

#### Définition d’un changement

> Ajout, modification ou retrait d’un ou plusieurs **Configuration Items** (CI)

#### Origines possibles :

- Événements, incidents, problèmes
- Évolutions métiers, légales, techniques

#### Les 7 R du changement

- **Raised** – qui a fait la demande ?
- **Reason** – pourquoi ?
- **Return** – résultats attendus
- **Risks** – risques associés
- **Resources** – ressources nécessaires
- **Responsible** – responsable du changement
- **Relationship** – dépendances avec d’autres changements

#### Types de changement

|Type|Description|
|---|---|
|**Standard**|Répétitif, documenté, préapprouvé|
|**Normal**|Évaluation complète + validation par le **CAB**|
|**Urgent**|Validé en urgence par **ECAB**, court-circuite les procédures|

#### Priorisation des changements

Basée sur **Impact × Urgence** (5 niveaux de priorité)

---

## 🧱 Configuration et actifs de services

### CI (Configuration Item)

- Élément contribuant à la fourniture d’un ou plusieurs services
- Doit être **identifiable**, **documenté**, et **lié** à d’autres CI

### CMS (Configuration Management System)

- Ensemble d’outils regroupant toutes les données CI
- Peut intégrer plusieurs **CMDB** (bases de données de configuration)

### DML (Definitive Media Library)

- Référentiel sécurisé pour les logiciels, médias, licences

#### Activités clés

- Identification, étiquetage, enregistrement des CI
- Contrôle, vérification, audits
- Rapports d’état, mise à jour continue

---

## 🚀 Déploiement et mise en production

### Objectifs

- Planifier et exécuter le **déploiement** en garantissant la valeur métier
- Fournir la documentation nécessaire
- Former les utilisateurs finaux

### Modes de déploiement

|Mode|Description|
|---|---|
|**Manuel**|Déploiement supervisé par la DSI|
|**Automatique**|Déploiement sans intervention humaine|
|**Push**|Initié par un serveur central|
|**Pull**|L’utilisateur déclenche le déploiement|
|**Big bang**|Tout d’un coup|
|**Par phase**|Par lot ou service|

---

## 📈 Autres processus associés

### Gestion de la validation et des tests

- Garantir la conformité des services
- Créer des PV de recette (fonctionnelle, performance, etc.)

### Évaluation des changements

- Analyser les résultats via le **PIR** (Post Implementation Review)

### Planification et support

- Organiser le changement, gérer les ressources

---

## 🧠 Gestion de la connaissance

### Objectifs

- Fournir **l’information utile** à tout moment du cycle de vie
- Structurer une base de connaissances **efficace et accessible** (SKMS)

### Bonne utilisation

- Une base utile est **consultée et exploitée**
- Nécessite **promotion, formation, documentation**

---

## ✅ À retenir pour les révisions

- La **transition** met en œuvre ce qui a été conçu, en assurant la qualité et la continuité de service
- Les **changements** sont formalisés par des **RFC**, évalués par **CAB/ECAB**, et suivis dans le **CMS**
- La **CMDB** contient tous les CI ; la **DML** stocke les logiciels
- Le **déploiement** peut être manuel, automatique, push/pull, big bang ou par phases
- La **gestion de la connaissance** est centrale pour l’efficience et la réutilisation des savoirs

---

## 📌 Bonnes pratiques professionnelles

- Formaliser chaque demande de changement avec une **RFC complète**
- Prioriser les changements selon **impact × urgence**
- Mettre à jour **CMDB et CMS** à chaque modification
- Utiliser un **mode de déploiement adapté** aux contraintes
- Créer des PV de recette systématiques pour tout déploiement
- Maintenir une base de connaissance **vivante, utilisée, mise à jour**