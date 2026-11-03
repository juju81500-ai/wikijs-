---
title: "Choisir et déployer Keycloak, Authelia ou Authentik pour le SSO"
description: "Comparer les trois solutions, choisir selon le besoin, puis déployer de façon sécurisée. Chaque produit a son modèle de configuration; ne pas copier la configuration de l'un vers l'autre."
published: true
date: 2026-11-03T09:36:14Z
tags: ["keycloak", "authelia", "authentik", "sso", "oidc", "saml", "mfa"]
editor: markdown
dateCreated: 2026-11-03T09:36:14Z
dateModified: 2026-11-03T09:36:14Z
---

# Choisir et déployer Keycloak, Authelia ou Authentik pour le SSO

- **OS / Version** : Linux (conteneurs ou paquets selon produit)
- **Type de fiche** : Installation/Déploiement
- **Environnement** : [[Glossary:VM]] ou hôte conteneurisé avec HTTPS et base de données
- **Machine ciblée** : Fournisseur d'identité / portail [[Glossary:SSO]]
- **Catégorie** : Identité / SSO / [[Glossary:MFA]]
- **Tags** : `keycloak`, `authelia`, `authentik`, `sso`, `oidc`, `saml`, `mfa`

## 1. Périmètre

Comparer les trois solutions, choisir selon le besoin, puis déployer de façon sécurisée. Chaque produit a son modèle de configuration; ne pas copier la configuration de l'un vers l'autre.

## 2. Prérequis

- Nom [[Glossary:DNS]], certificat [[Glossary:TLS]] et reverse proxy.
- Base de données prise en charge, sauvegardée (PostgreSQL recommandé selon produit).
- Annuaire [[Glossary:LDAP]]/AD ou stockage de comptes local.
- Liste des applications à protéger et protocoles pris en charge ([[Glossary:OIDC]], [[Glossary:SAML]], forward-auth).
- Compte administrateur d'urgence et secrets en coffre.

## 3. Variantes éditeur à distinguer

| Produit | Positionnement | Protocoles | Remarque |
|---|---|---|---|
| Keycloak | [[Glossary:IAM]] complet, fédération d'identités, projet CNCF | OIDC, SAML, OAuth 2.0 | Plus riche mais plus lourd (Java), clustering possible |
| Authelia | Portail d'authentification léger derrière reverse proxy | Forward-auth, OIDC (selon version) | Configuration par fichier YAML |
| Authentik | Fournisseur d'identité avec interface d'administration | OIDC, SAML, LDAP, proxy | Dépend de PostgreSQL |

Les versions et fonctions évoluent vite : consulter la documentation de la version cible.

## 4. Étapes vérifiables

### 4.1 Choisir le produit

Retenir Keycloak pour les besoins SAML/fédération avancés, Authelia pour protéger des applications simples derrière un proxy, Authentik pour une solution intermédiaire avec interface d'administration. Valider sur les applications réelles.

### 4.2 Déployer en lab

Suivre le guide d'installation officiel de la version choisie (conteneurs ou paquets). Utiliser HTTPS et une base persistante; ne pas utiliser le mode de développement en production (par exemple celui de Keycloak).

### 4.3 Sécuriser l'administration

Remplacer les identifiants initiaux, activer le MFA pour les administrateurs, limiter l'accès à la console d'administration par réseau.

### 4.4 Raccorder l'annuaire et les applications

Configurer la fédération LDAP/AD, puis créer un client OIDC/SAML ou une règle de forward-auth par application, avec URL de redirection strictes.

### 4.5 Activer le MFA

Imposer [[Glossary:TOTP]] ou WebAuthn selon les capacités du produit, avec politique de récupération documentée.

### 4.6 Sauvegarder et superviser

Sauvegarder la base et la configuration, tester la restauration, surveiller le certificat et les journaux d'authentification.

## 5. Validation

- Connexion SSO réussie vers au moins deux applications de test.
- Le MFA est demandé aux utilisateurs concernés.
- Les URL de redirection non déclarées sont refusées.
- Restauration testée sur une instance isolée.

## 6. Retour arrière

- Conserver l'authentification locale des applications pendant la migration.
- Retirer la règle SSO d'une application pour revenir à son mode initial.
- Restaurer la base et la configuration d'avant mise à jour.

## 7. Limites de version et de licence

- Ne pas mettre à jour sans lire les notes de migration; les schémas et options changent.
- Le support OIDC d'Authelia dépend de la version.
- Un SSO devient un point unique de défaillance : prévoir la haute disponibilité si critique.

## 8. Verdict historique

**Non testé sur plateforme cible.** Cette fiche est une synthèse documentaire des sources officielles; aucune exécution n'a été réalisée sur les produits, versions ou licences visés. Valider en laboratoire isolé avant production.

## Sources

- [Keycloak — documentation](https://www.keycloak.org/documentation)
- [Authelia — documentation](https://www.authelia.com/overview/prologue/introduction/)
- [Authentik — documentation](https://docs.goauthentik.io/)