---
title: "Fiche Simple - GitHub Compte"
description: "Sécuriser le compte GitHub, activer MFA et limiter les sessions et applications autorisées."
published: true
date: 2026-10-29T20:47:59Z
tags: ["github", "cloud-saas", "compte-securite", "mfa"]
editor: markdown
dateCreated: 2026-10-29T20:47:59Z
dateModified: 2026-10-29T20:47:59Z
---

# Fiche_Simple_-_GitHub_Compte

- **Environnement** : Navigateur récent, identité nominative et compte GitHub autorisé
- **OS / Version** : GitHub SaaS — interface évolutive
- **Catégorie** : Cloud SaaS / compte
- **Tags** : `github`, `cloud-saas`, `compte-securite`, `mfa`
---

## Problème précis à résoudre

Sécuriser le compte GitHub, activer MFA et limiter les sessions et applications autorisées.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir le domaine GitHub en saisissant l’adresse manuellement
   ```text
   Navigateur > saisir https://github.com/ > Sign in ou Sign up.
   ```
   👉 Explication : vérifier le domaine et utiliser une organisation approuvée.

2. Activer MFA depuis les paramètres du compte
   ```text
   Navigateur > ouvrir la documentation officielle : https://docs.github.com/account-and-profile/setting-up-and-managing-your-personal-account-on-github
   ```
   👉 Explication : activer la méthode approuvée et conserver les codes de récupération dans un emplacement protégé. Détail à confirmer dans la documentation officielle avant application : Avatar > Settings > Password and authentication > Two-factor authentication.

3. Réviser sessions et applications autorisées
   ```text
   Settings > Password and authentication; vérifier sessions et connexions d’applications OAuth.
   ```
   👉 Explication : révoquer les sessions ou applications inconnues et appliquer le moindre privilège.

## 2. Production — Contrôles

Appliquer le compte/organisation approuvé, rôles minimaux, revue des accès et procédure de récupération.

## 3. Production — Sécurité

- Ne jamais partager compte, code MFA, recovery codes ou token personnel.
- Activer MFA résistante au phishing si disponible et exigée.
- Révoquer immédiatement toute session ou application non reconnue.

## Validation et retour arrière

- **Validation** : Le compte est nominatif, MFA est active et sessions/applications sont comprises et autorisées.
- **Retour arrière** : Révoquer sessions suspectes et modifier les facteurs d’accès par le flux officiel.

## Si le problème n'est pas résolu

- [GitHub Docs — compte](https://docs.github.com/account-and-profile/setting-up-and-managing-your-personal-account-on-github)
- [GitHub Docs — clés SSH](https://docs.github.com/authentication/connecting-to-github-with-ssh)
- [GitHub Docs — secrets Actions](https://docs.github.com/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions)
- [Fiche connexe](</01-fiches-simples/transverses/cloud-saas/github/fiche-simple-github-cles-ssh>)