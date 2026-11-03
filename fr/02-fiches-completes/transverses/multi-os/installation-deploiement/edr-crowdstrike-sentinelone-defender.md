---
title: "Déployer et gérer un EDR : CrowdStrike Falcon, SentinelOne ou Microsoft Defender for Endpoint"
description: "Préparer, piloter et exploiter le déploiement d'un agent EDR de manière défensive et autorisée, sur des machines dont l'organisation est propriétaire. Le parcours se fait par console propriétaire; les noms de paquets, jetons et paramètres d'installation sont fournis par le portail de l'éditeur et ne"
published: true
date: 2026-11-03T09:36:14Z
tags: ["edr", "crowdstrike", "falcon", "sentinelone", "defender-endpoint", "agent"]
editor: markdown
dateCreated: 2026-11-03T09:36:14Z
dateModified: 2026-11-03T09:36:14Z
---

# Déployer et gérer un EDR : CrowdStrike Falcon, SentinelOne ou Microsoft Defender for Endpoint

- **OS / Version** : Windows, Linux, macOS selon produit et version d'agent
- **Type de fiche** : Installation/Déploiement
- **Environnement** : Parc géré avec console cloud de l'éditeur
- **Machine ciblée** : Postes et serveurs
- **Catégorie** : Sécurité des terminaux / EDR
- **Tags** : `edr`, `crowdstrike`, `falcon`, `sentinelone`, `defender-endpoint`, `agent`

## 1. Périmètre

Préparer, piloter et exploiter le déploiement d'un agent EDR de manière défensive et autorisée, sur des machines dont l'organisation est propriétaire. Le parcours se fait par console propriétaire; les noms de paquets, jetons et paramètres d'installation sont fournis par le portail de l'éditeur et ne sont pas reproduits ici.

## 2. Prérequis

- Licence et tenant actifs (CrowdStrike Falcon, SentinelOne Singularity, ou licence Microsoft incluant Defender for Endpoint).
- Compte administrateur de la console avec rôles à moindre privilège et MFA.
- Liste d'OS et versions compatibles avec la version d'agent visée.
- Accès réseau sortant vers les domaines de l'éditeur, validé avec l'équipe réseau/proxy.
- Outil de déploiement existant (GPO, Intune, Configuration Manager, Ansible, MDM macOS...) et groupe pilote.
- Accord de la direction et information du personnel sur la collecte de télémétrie (cadre juridique/RGPD).
- Produit commercial : la console, les droits d'accès au portail éditeur et la licence sont des prérequis. Aucune commande générique n'est donnée quand elle dépend de la console ou de la version; suivre la documentation de la version exacte.

## 3. Variantes éditeur à distinguer

| Produit | Console | Obtention de l'agent | Particularités |
|---|---|---|---|
| CrowdStrike Falcon | Console Falcon (cloud) | Portail éditeur, accès soumis au contrat | Identifiant de client (CID) et politiques de prévention par groupes d'hôtes |
| SentinelOne | Management Console du tenant | Portail du tenant | Jeton de site, politiques par site/groupe |
| Defender for Endpoint | Portail Microsoft Defender | Onboarding via paquet généré dans le portail ou intégration Intune/Configuration Manager | Sur serveurs, la méthode dépend de la version Windows Server ou Linux |

Les trois produits ont leurs propres modèles de politique, de protection contre la désinstallation et de verbes d'API. Ne pas supposer des équivalences exactes.

## 4. Étapes vérifiables

### 4.1 Cadrer le pilote

Constituer un groupe pilote représentatif (types d'OS, rôles). Définir critères de réussite : couverture, performance, absence de blocage applicatif.

### 4.2 Configurer la politique en mode prudent

Dans la console, créer une politique dédiée au pilote, démarrer en mode détection/audit si l'éditeur le propose, définir les exclusions strictement nécessaires et documentées, activer la protection contre la désinstallation avec accès restreint au code.

### 4.3 Déployer l'agent

Télécharger le paquet depuis le portail et le pousser par l'outil de déploiement du parc, selon la procédure officielle de l'OS cible. Ne jamais publier le jeton/CID d'enrôlement dans un dépôt ou un ticket.

### 4.4 Vérifier l'enrôlement

Confirmer dans la console que chaque hôte pilote apparaît, avec version d'agent, politique et dernier contact. Utiliser l'outil d'état local fourni par l'éditeur pour la plateforme.

### 4.5 Étendre par vagues

Passer progressivement du mode détection à la prévention, traiter les faux positifs, puis élargir. Brancher les alertes sur le SIEM/ITSM et définir le processus de réponse à incident.

### 4.6 Maintenir

Planifier les mises à jour d'agent par anneaux, revoir les exclusions chaque trimestre et contrôler les hôtes inactifs.

## 5. Validation

- Tous les hôtes pilotes remontent dans la console avec la politique attendue.
- Un test de détection inoffensif fourni par l'éditeur ou un fichier de test standard génère une alerte, sans code malveillant réel.
- Aucun impact applicatif ni de performance inacceptable sur le pilote.
- Les alertes arrivent dans l'outil de supervision ou le SIEM.

## 6. Retour arrière

- Retirer l'hôte de la politique pilote ou le basculer en mode détection depuis la console.
- Désinstaller l'agent avec la procédure officielle, qui exige généralement un code ou jeton de maintenance obtenu dans la console.
- Conserver la protection antivirus native de l'OS active pendant tout retour arrière.

## 7. Limites de version et de licence

- Fonctions, noms de politiques et prérequis varient selon version d'agent, OS et licence.
- Les systèmes sans support éditeur ne sont pas garantis.
- Les EDR peuvent entrer en conflit avec d'autres antivirus : suivre les consignes de coexistence de l'éditeur.

## 8. Verdict historique

**Non testé sur plateforme cible.** Cette fiche est une synthèse documentaire des sources officielles; aucune exécution n'a été réalisée sur les produits, versions ou licences visés. Valider en laboratoire isolé avant production.

## Sources

- [Microsoft Learn — Defender for Endpoint](https://learn.microsoft.com/microsoft-365/security/defender-endpoint/)
- [SentinelOne — ressources et documentation (accès client)](https://www.sentinelone.com/)
- [CrowdStrike — documentation (accès client)](https://www.crowdstrike.com/)
- [CNIL — surveillance des salariés](https://www.cnil.fr/fr/la-surveillance-au-travail)