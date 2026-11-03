---
title: "Cybersécurité – Sensibilisation, menaces, DICP et CNIL"
description: "- Réduire les risques sur les actifs de l’organisation"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# Cybersécurité – Sensibilisation, menaces, DICP et CNIL
## 🧠 Enjeux de la sécurité des SI

### Définition d’un SI

> Ensemble structuré de ressources (personnes, matériel, logiciels, réseaux) permettant de traiter l’information d’une organisation.

### Objectifs de la sécurité des SI

- Réduire les **risques** sur les actifs de l’organisation
- Préserver la **qualité de service**, la **confiance**, et **l’intégrité** des opérations
- Se conformer aux **exigences réglementaires** (RGPD, CNIL, etc.)

### Impacts potentiels d’une faille de sécurité

- Financier (vol, rançongiciel)
- Juridique (non-conformité, amendes)
- Organisationnel (interruption d’activité)
- Réputationnel (perte de confiance)

---

## 🔐 Notions fondamentales : DICP

|Critère|Objectif|
|---|---|
|**Disponibilité**|Bien accessible au bon moment aux bonnes personnes|
|**Intégrité**|Exactitude, complétude, non-altération du bien|
|**Confidentialité**|Limitation d’accès aux seules personnes habilitées|
|**Preuve**|Traçabilité, authentification, imputabilité (journalisation fiable)|

### Exemple d’analyse DICP : serveur web public

- Disponibilité : Très fort (doit être accessible à tout moment)
- Intégrité : Très fort (pas de contenu frauduleux)
- Confidentialité : Faible (contenu public)
- Preuve : Faible (pas d’interactions)

---

## ⚠️ Vulnérabilités, menaces, attaques

### Vulnérabilité

- Faiblesse d’un actif pouvant être exploitée (ex. : mot de passe faible, absence de patch)

### Menace

- Cause potentielle d’un incident (humain, technique, organisationnel)

### Attaque

- Concrétisation d’une menace par l’exploitation d’une vulnérabilité

---

## 📉 Panorama des menaces

### Hameçonnage / phishing

- Simulation de site ou mail légitime pour dérober des identifiants

### Ingénierie sociale

- Manipulation psychologique d’un utilisateur pour obtenir des accès

### Intrusion

- Accès illégitime à un SI par exploitation de failles (réseau, applicatif, humain)

### Fraude interne

- Détournement ou modification frauduleuse d’actions par un agent légitime

### Malware / Virus

- Chevaux de Troie, vers, ransomwares, etc. – introduits via mail, web, USB…

### DDoS

- Saturation d’un service cible via un botnet ou attaque en masse

---

## 🧩 Moyens de protection

|Mécanisme technique|Objectifs|
|---|---|
|**Chiffrement**|Confidentialité, intégrité, authentification|
|**Pare-feu**|Filtrage des flux réseau, segmentation|
|**Contrôle d’accès**|Gestion des droits (lecture, écriture, suppression…)|
|**Anti-virus**|Détection de logiciels malveillants connus|
|**Audit**|Vérification des journaux, vérifiabilité|

|Mécanisme organisationnel|Objectifs|
|---|---|
|**PSSI**|Politique formelle de sécurité|
|**Clauses contractuelles**|Encadrement des prestataires|
|**Formation / sensibilisation**|Responsabilisation des utilisateurs, diffusion des bonnes pratiques|

---

## 🏛️ Rôle de la CNIL (RGPD)

### Définitions clés

- **Donnée personnelle** : toute information permettant d’identifier une personne physique directement ou indirectement

### Champ d’application

- Traitements automatisés et non automatisés de données personnelles dans des fichiers, hors usages strictement personnels

### Responsabilités

- Déclaration des traitements
- Droit à l’oubli / rectification / portabilité
- Sécurité des données, confidentialité, traçabilité

---

## ✅ À retenir pour les révisions

- DICP = **4 piliers de la sécurité** : Disponibilité, Intégrité, Confidentialité, Preuve
- Une **attaque** = menace + vulnérabilité exploitée
- Les **menaces** sont de plus en plus organisées, ciblées, et lucratives
- La **CNIL** encadre la protection des données personnelles en France (RGPD)

---

## 📌 Bonnes pratiques professionnelles

- Appliquer la **sécurité en profondeur** : empilement de mécanismes défensifs
- Former régulièrement les utilisateurs à la **cyber-hygiène**
- Mettre en œuvre une **PSSI** validée et documentée
- S’assurer que tout accès est **tracé et justifiable** (preuve)
- Conserver des **mots de passe robustes** ou recourir à l’authentification forte (MFA)
- Réaliser des audits réguliers pour évaluer le niveau DICP des actifs