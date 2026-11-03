---
title: "Administrer Google Workspace : mise en service, sécurité, SSO et messagerie"
description: "- Couvre l'administration d'un tenant Google Workspace via la console d'administration. Google Cloud Platform (projets, IAM) est un produit distinct."
published: true
date: 2026-11-03T09:36:14Z
tags: ["google-workspace", "saas", "sso", "gmail", "2sv"]
editor: markdown
dateCreated: 2026-11-03T09:36:14Z
dateModified: 2026-11-03T09:36:14Z
---

# Administrer Google Workspace : mise en service, sécurité, SSO et messagerie

- **OS / Version** : Tenant Google Workspace (SaaS)
- **Type de fiche** : Installation/Déploiement
- **Périmètre** : Création et vérification du domaine, administrateurs, unités organisationnelles, 2SV, SSO SAML, messagerie (MX, SPF, DKIM, DMARC), provisionnement
- **Catégorie** : Collaboration / identité
- **Tags** : `google-workspace`,`saas`,`sso`,`gmail`,`2sv`

## 1. Portée, hypothèses et licences

- Couvre l'administration d'un tenant **Google Workspace** via la console d'administration. Google Cloud Platform (projets, IAM) est un produit distinct.
- **Souscription requise** : Google Workspace est payant par utilisateur (éditions Business, Enterprise, Education, etc.). Les fonctionnalités (SSO avec fournisseur tiers, audit avancé, DLP) dépendent de l'édition : vérifier la comparaison d'éditions en cours.
- Hypothèses : un domaine DNS contrôlé, une adresse de secours pour le super-administrateur, un rôle de responsable de la conformité pour les rétentions et les exports.

## 2. Prérequis

- Accès DNS au domaine (enregistrements TXT et MX).
- Deux comptes super-administrateurs nominatifs maximum, avec clés de sécurité physiques ; un compte de secours dont les identifiants sont conservés dans un coffre.
- Inventaire des utilisateurs, groupes, unités organisationnelles (OU) et applications tierces.
- Si SSO : un fournisseur d'identité (IdP) compatible SAML 2.0 et ses métadonnées.

## 3. Création et vérification du domaine

1. Créer le compte depuis le parcours officiel Google Workspace et ouvrir la console `admin.google.com`.
2. Vérifier la propriété du domaine avec l'enregistrement TXT fourni dans l'assistant, puis contrôler la propagation :

```bash
dig +short TXT exemple.fr
```

3. Ne jamais utiliser le compte super-administrateur pour l'usage quotidien ; créer des rôles d'administrateur délégués (Comptes > Rôles d'administrateur).

## 4. Structure organisationnelle

- Créer les OU (par site, fonction ou niveau de risque) et les groupes ; appliquer les paramètres au niveau le plus adapté plutôt qu'à la racine.
- Créer les utilisateurs manuellement, par import CSV ou par synchronisation d'annuaire (Google Cloud Directory Sync pour Active Directory/LDAP, ou provisionnement SCIM selon la prise en charge de votre IdP). Toute synchronisation s'essaie d'abord en mode simulation dans l'outil.

## 5. Sécurité

1. Sécurité > Authentification > Validation en deux étapes : activer la 2SV, imposer son enregistrement avec une période de grâce, privilégier les clés de sécurité pour les administrateurs.
2. Politiques de mots de passe, appareils mobiles gérés, contrôle d'accès aux applications tierces et API (Sécurité > Contrôle des accès et des données).
3. SSO SAML : dans Sécurité > Authentification > SSO avec un fournisseur d'identité tiers, charger les métadonnées/certificat de l'IdP, définir l'URL de connexion, appliquer le SSO à une OU de test avant le domaine entier. Conserver une OU d'urgence sans SSO pour le compte de secours.
4. Activer l'export des journaux d'audit selon l'édition vers un SIEM ou BigQuery si disponible.

## 6. Messagerie

1. Enregistrements MX : utiliser les valeurs affichées par la documentation Google actuelle (« Set up MX records for Gmail ») ; elles ont évolué dans le temps. Réduire le TTL avant la bascule.
2. SPF : publier un unique enregistrement TXT incluant Google (valeur dans la documentation), en tenant compte des autres expéditeurs.
3. DKIM : Applications > Google Workspace > Gmail > Authentifier les e-mails, générer la clé, publier l'enregistrement TXT puis démarrer l'authentification.
4. DMARC : commencer par `p=none` avec adresse de rapport, puis durcir.

```bash
dig +short MX exemple.fr
dig +short TXT exemple.fr
dig +short TXT <selecteur>._domainkey.exemple.fr
```

5. Migration depuis un autre système via l'outil de migration de données de Google, par lots pilotes.

## 7. Outils en ligne de commande

Des outils communautaires (par exemple GAM) existent mais ne sont pas publiés par Google : leur usage exige une revue de sécurité et un compte de service dédié. Ne pas diffuser de jetons d'API dans des scripts.

## 8. Validation

- Domaine « vérifié » ; MX conformes à la documentation ; SPF, DKIM et DMARC valides sur un message de test (en-têtes « Authentication-Results »).
- 2SV imposée à l'OU pilote ; connexion SSO réussie avec un utilisateur de test, et accès de secours testé.
- Journaux d'audit consultables ; rôles d'administration vérifiés.

## 9. Retour arrière

- Rétablir les anciens MX (TTL court conservé) ; désactiver le SSO au niveau de l'OU pilote, ou utiliser le compte de secours pour retirer la configuration.
- Suspendre (et non supprimer) les utilisateurs de test ; la suppression d'un utilisateur ou d'une OU a des délais de récupération limités fixés par Google.
- Conserver un export des paramètres (captures, rapports) avant modification.

## Sources officielles

- [Aide de l'administrateur Google Workspace](https://support.google.com/a)
- [Vérifier la propriété du domaine](https://support.google.com/a/answer/60216)
- [Valider en deux étapes](https://support.google.com/a/answer/175197)
- [Configurer le SSO avec un IdP tiers](https://support.google.com/a/answer/6087519)
- [Google Cloud Directory Sync](https://support.google.com/a/answer/106368)

Aucun tenant Google Workspace n'a été utilisé pendant la rédaction ; les chemins de menu et valeurs DNS doivent être vérifiés dans l'aide en vigueur.

## Historique

| Date | Version | Changement | Statut de test |
|---|---|---|---|
| 2026-10-31 | 1.0 | Création de la fiche à partir de la documentation éditeur | Non testé sur plateforme cible |