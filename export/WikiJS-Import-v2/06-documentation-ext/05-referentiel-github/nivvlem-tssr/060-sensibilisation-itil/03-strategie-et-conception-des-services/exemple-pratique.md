---
title: "TP – Stratégie et conception des services"
description: "Décrire la mise en œuvre d’un nouveau service d’accueil pour un salarié commercial itinérant, selon les processus ITIL liés à la stratégie et à la conception des services."
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# TP – Stratégie et conception des services

## 🧠 Objectif du TP

Décrire la mise en œuvre d’un nouveau service d’**accueil pour un salarié commercial itinérant**, selon les **processus ITIL** liés à la **stratégie** et à la **conception** des services.

---

## 🧾 Contexte global

### Objectifs stratégiques

- Identifier les éléments nécessaires à la mise à disposition du poste de travail.
- S’assurer que les besoins du client interne sont couverts (valeur, qualité, maîtrise des coûts).
- Structurer une offre de service cohérente avec le catalogue et le portefeuille de services.

### Objectifs de conception

- Définir une procédure de déploiement reproductible.
- Anticiper les contraintes matérielles, logicielles, organisationnelles.
- Produire des livrables clairs (CMS, documentation, indicateurs).

---

## 🔍 Vue processus ITIL

### 📌 Phase de stratégie des services

#### Analyse de la demande (Gestion des demandes)

- Le besoin provient d’un onboarding RH pour un poste de commercial itinérant.
- Les équipements sont adaptés au profil (mobilité, communication à distance, outils bureautiques).

#### Référencement dans le portefeuille des services

- Ajout du service dans la **liste des services récurrents** pour les profils commerciaux.
- Alignement avec les **objectifs métiers** et stratégie IT (mobilité, sécurité, autonomie).

#### Calcul de la valeur (ROI/TCO)

- Évaluation du coût global de déploiement (matériel, licences, temps IT).
- Estimation du **retour sur investissement** par la productivité attendue.

#### Validation des priorités

- Service considéré comme prioritaire (intégration d’un salarié).
- Validation rapide par les métiers (client interne).

---

### 📌 Phase de conception des services

#### Définition de la solution cible

|Domaine|Détail|
|---|---|
|**Matériel**|PC portable, dock, écran, téléphone IP, smartphone|
|**Comptes**|AD, M365, GLPI, téléphonie, badge|
|**Connectivité**|Prises réseau, ports switch, alimentation|
|**Support**|CMS, documentation d’installation, image système normalisée|

#### Préparation des livrables

- Création d’une image de déploiement personnalisée (Win11 + Office365).
- Mise à jour du **CMS (GLPI/CMDB)** à chaque étape.
- Rédaction des scripts de déploiement et fiches de procédures pour industrialisation.

#### Gestion des contraintes

- Environnement inconnu => architecture réseau et services à valider.
- Délais à respecter (poste opérationnel le jour de l’arrivée).

#### Choix des options techniques

- Déploiement **via PXE** (automatisé, stable, rapide).
- Attribution IP téléphonie **via IPBX** avec identifiant unique.
- Accès VPN + sécurité renforcée pour un usage externe sécurisé.

#### Définition des indicateurs

- Taux de conformité à la procédure
- Délai moyen de mise à disposition
- Satisfaction utilisateur (enquête onboarding)

---

## ✅ À retenir pour les révisions

- La **stratégie des services** vise à aligner les services IT sur les besoins métiers tout en maîtrisant les coûts et en apportant de la valeur.
- La **conception** transforme cette stratégie en une solution concrète : outils, processus, documentation, et indicateurs.
- La structuration en processus ITIL permet une **réutilisabilité** et une **qualité de service cohérente**.

---

## 📌 Bonnes pratiques professionnelles

- Utiliser des **images système préconfigurées** pour automatiser les déploiements.
- Maintenir un **catalogue de services actualisé** et conforme aux besoins métiers.
- Mettre à jour systématiquement le **CMS (GLPI/CMDB)** dès qu’un équipement est installé, déplacé ou configuré.
- Formaliser une **procédure d’intégration** pour chaque profil métier récurrent.
- Utiliser des **indicateurs de performance** pour évaluer et améliorer les services fournis.
- Prévoir une **phase de test utilisateur** avant la mise en production effective.
- Documenter les contraintes connues (ex : absence d’infos infra) dans un **registre des risques projet**.