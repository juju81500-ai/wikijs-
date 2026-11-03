---
title: "Déployer Bitdefender GravityZone ou Kaspersky Endpoint Security"
description: "Installer la console de gestion, créer les politiques et déployer les agents de manière contrôlée. Les deux produits sont distincts : leurs consoles, paquets et paramètres ne sont pas interchangeables."
published: true
date: 2026-11-03T09:36:14Z
tags: ["bitdefender", "gravityzone", "kaspersky", "endpoint-security", "antimalware"]
editor: markdown
dateCreated: 2026-11-03T09:36:14Z
dateModified: 2026-11-03T09:36:14Z
---

# Déployer Bitdefender GravityZone ou Kaspersky Endpoint Security

- **OS / Version** : Windows, Linux, macOS selon produit
- **Type de fiche** : Installation/Déploiement
- **Environnement** : Parc géré avec console centrale
- **Machine ciblée** : Postes et serveurs
- **Catégorie** : Sécurité des terminaux / antimalware
- **Tags** : `bitdefender`, `gravityzone`, `kaspersky`, `endpoint-security`, `antimalware`

## 1. Périmètre

Installer la console de gestion, créer les politiques et déployer les agents de manière contrôlée. Les deux produits sont distincts : leurs consoles, paquets et paramètres ne sont pas interchangeables.

## 2. Prérequis

- Licence valide et compte de la console ou du serveur d'administration.
- Version cible compatible avec les OS du parc; vérifier les OS supportés.
- Compte de déploiement dédié, avec droits limités, et ports/flux ouverts entre console et clients selon la doc.
- Désinstallation planifiée des anciens antivirus pour éviter les conflits.
- Groupe pilote et sauvegarde/instantané des serveurs critiques avant installation.
- Avant toute décision d'achat ou de maintien, évaluer le risque réglementaire et fournisseur propre à votre organisation (certaines administrations ont émis des recommandations sur certains éditeurs); consulter l'[[Glossary:ANSSI]]/RSSI.
- Produit commercial : la console, les droits d'accès au portail éditeur et la licence sont des prérequis. Aucune commande générique n'est donnée quand elle dépend de la console ou de la version; suivre la documentation de la version exacte.

## 3. Variantes éditeur à distinguer

| Produit | Gestion | Déploiement de l'agent |
|---|---|---|
| Bitdefender GravityZone | Control Center cloud ou appliance virtuelle on-premises | Paquets d'installation générés dans la console, rôle « relais » pour les réseaux segmentés |
| Kaspersky Endpoint Security | Kaspersky Security Center (installé sur Windows ou Linux selon version) | Paquets d'installation et tâches de déploiement du Security Center |

Les noms de rôles, groupes et politiques sont propres à chaque produit.

## 4. Étapes vérifiables

### 4.1 Installer ou ouvrir la console

GravityZone : créer l'instance cloud ou déployer l'appliance on-premises depuis le portail éditeur. Kaspersky : installer Security Center sur le serveur dédié en suivant le guide de la version choisie, avec base de données prise en charge.

### 4.2 Créer la structure et les politiques

Créer les groupes (serveurs, postes, pilote), une politique pilote en mode détection si possible et des exclusions documentées uniquement pour des besoins applicatifs justifiés.

### 4.3 Préparer les paquets

Générer ou télécharger les paquets d'installation depuis la console; vérifier leur provenance et leur intégrité (signature ou empreinte publiée par l'éditeur).

### 4.4 Déployer sur le pilote

Utiliser la tâche de déploiement à distance de la console ou l'outil existant ([[Glossary:GPO]], Intune, Ansible). Ne pas stocker de jetons dans un dépôt.

### 4.5 Vérifier et généraliser

Contrôler dans la console version, politique, bases de signatures et dernier contact; élargir par vagues, puis activer les rapports et alertes.

### 4.6 Mises à jour

Planifier les mises à jour des signatures, de l'agent et de la console selon les notes de version.

## 5. Validation

- Les clients pilotes apparaissent comme gérés et à jour.
- Un fichier de test inoffensif standard déclenche une détection.
- Les tâches d'analyse et de mise à jour s'exécutent.
- Aucun conflit avec d'autres agents de sécurité.

## 6. Retour arrière

- Retirer le poste de la politique ou passer en détection seule.
- Désinstaller l'agent par la tâche de la console ou la procédure officielle (mot de passe de désinstallation éventuel).
- Restaurer l'instantané ou la sauvegarde d'un serveur en cas de défaillance.

## 7. Limites de version et de licence

- Noms d'options et fonctions dépendent de la version et de la licence.
- Les agents Linux/macOS ont un périmètre de fonctions plus restreint que Windows.
- Aucune commande universelle : utiliser les paquets et paramètres du portail.

## 8. Verdict historique

**Non testé sur plateforme cible.** Cette fiche est une synthèse documentaire des sources officielles; aucune exécution n'a été réalisée sur les produits, versions ou licences visés. Valider en laboratoire isolé avant production.

## Sources

- [Bitdefender GravityZone — documentation](https://www.bitdefender.com/business/support/en/77209-125277-gravityzone.html)
- [Kaspersky Security Center — aide en ligne](https://support.kaspersky.com/help/KSC/)
- [Kaspersky Endpoint Security — aide](https://support.kaspersky.com/KESWin)
- [ANSSI — publications](https://cyber.gouv.fr/)