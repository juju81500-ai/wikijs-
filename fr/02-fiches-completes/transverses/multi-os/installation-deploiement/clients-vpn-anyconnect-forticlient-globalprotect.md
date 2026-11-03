---
title: "Déployer les clients VPN Cisco AnyConnect/Secure Client, FortiClient et GlobalProtect"
description: "Déployer et valider les clients VPN d'une passerelle déjà en service. La configuration de la passerelle (ASA/FTD, FortiGate, PAN-OS) est hors périmètre et se trouve dans la fiche pare-feu associée."
published: true
date: 2026-11-03T09:36:14Z
tags: ["vpn", "anyconnect", "cisco-secure-client", "forticlient", "globalprotect", "nomades"]
editor: markdown
dateCreated: 2026-11-03T09:36:14Z
dateModified: 2026-11-03T09:36:14Z
---

# Déployer les clients VPN Cisco AnyConnect/Secure Client, FortiClient et GlobalProtect

- **OS / Version** : Windows, macOS, Linux (selon produit), iOS et Android
- **Type de fiche** : Installation/Déploiement
- **Environnement** : Parc nomade connecté à une passerelle VPN existante
- **Machine ciblée** : Postes clients
- **Catégorie** : Accès distant / VPN
- **Tags** : `vpn`, `anyconnect`, `cisco-secure-client`, `forticlient`, `globalprotect`, `nomades`

## 1. Périmètre

Déployer et valider les clients VPN d'une passerelle déjà en service. La configuration de la passerelle (ASA/FTD, FortiGate, PAN-OS) est hors périmètre et se trouve dans la fiche pare-feu associée.

## 2. Prérequis

- Passerelle VPN fonctionnelle, avec certificat serveur valide et authentification (annuaire, MFA, certificat).
- Licences clientes actives : AnyConnect/Secure Client et FortiClient (certaines fonctions) ou GlobalProtect (abonnement selon fonctions).
- Paquets obtenus sur les portails éditeurs ou sur la passerelle si le produit le permet.
- Outil de déploiement (Intune, GPO, MDM, Ansible).
- Politique d'accès : split tunnel ou tunnel complet, DNS, posture du poste.

## 3. Variantes éditeur à distinguer

| Client | Passerelle attendue | Distribution | Remarque |
|---|---|---|---|
| Cisco AnyConnect / Secure Client | Cisco ASA ou FTD, ISE pour la posture | Portail Cisco (droits contractuels) | AnyConnect est désormais renommé Cisco Secure Client dans les versions récentes |
| FortiClient | FortiGate | Portail Fortinet, profil via EMS en option | Le profil peut être poussé par FortiClient EMS |
| GlobalProtect | Palo Alto (portail et passerelle GlobalProtect) | Portail Palo Alto ou portail GlobalProtect | La configuration client est largement distribuée par la passerelle |

Les clients ne sont pas interchangeables avec les passerelles d'un autre éditeur.

## 4. Étapes vérifiables

### 4.1 Choisir la version

Consulter la matrice de compatibilité du client et de la passerelle; ne pas mettre à jour l'un sans vérifier l'autre.

### 4.2 Préparer le profil

Créer le profil ou la configuration côté passerelle ou console de gestion (adresse, méthode d'authentification, options de reconnexion).

### 4.3 Déployer le client

Distribuer le paquet officiel par l'outil de déploiement avec la procédure propre à l'OS et au produit; vérifier l'empreinte ou la signature.

### 4.4 Tester un pilote

Connecter un poste depuis un réseau externe et vérifier l'authentification, MFA, DNS, routes et accès aux ressources autorisées uniquement.

### 4.5 Déployer par vagues et former

Documenter le support utilisateur, les cas de pare-feu réseau hôtel/hôpital et la révocation des appareils perdus.

## 5. Validation

- Connexion et déconnexion réussies depuis un réseau externe.
- Seules les ressources prévues sont accessibles.
- Les journaux de la passerelle montrent l'utilisateur et l'adresse attribuée.
- Le certificat serveur est reconnu sans avertissement.

## 6. Retour arrière

- Désinstaller le client avec l'outil de déploiement ou la procédure de l'éditeur.
- Revenir à la version précédente du paquet si la compatibilité est rompue.
- Désactiver le profil ou le compte VPN en cas de compromission.

## 7. Limites de version et de licence

- Les fonctions de posture, ZTNA et MFA dépendent de la licence et de la version.
- Support de Linux limité selon produit.
- Aucune commande n'est donnée car l'installation dépend du paquet, de la plateforme et du profil.

## 8. Verdict historique

**Non testé sur plateforme cible.** Cette fiche est une synthèse documentaire des sources officielles; aucune exécution n'a été réalisée sur les produits, versions ou licences visés. Valider en laboratoire isolé avant production.

## Sources

- [Cisco — Secure Client (AnyConnect)](https://www.cisco.com/c/en/us/support/security/anyconnect-secure-mobility-client/series.html)
- [Fortinet — FortiClient](https://docs.fortinet.com/product/forticlient)
- [Palo Alto Networks — GlobalProtect](https://docs.paloaltonetworks.com/globalprotect)