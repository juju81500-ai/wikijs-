---
title: "TP – Sécurisation d’un tenant Microsoft 365 (MFA)"
description: "- URL : [https://admin.microsoft.com](https://admin.microsoft.com/)"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# TP – Sécurisation d’un tenant Microsoft 365 (MFA)
## 🔐 Étapes de configuration de la MFA dans Microsoft 365

### 1. Connexion au Centre d’administration

- URL : [https://admin.microsoft.com](https://admin.microsoft.com/)
- Se connecter avec les **identifiants administrateur** créés précédemment

### 2. Activation MFA pour un utilisateur spécifique

- Aller dans **Utilisateurs > Utilisateurs actifs**
- Cliquer sur **Gérer l’authentification multifacteur** (bouton en haut ou menu contextuel)
- Sélectionner l’utilisateur concerné
- Cliquer sur **Activer > Activer l’authentification multifacteur**

### 3. Forcer le reparamétrage MFA

- Dans **Paramètres de l’utilisateur** :
    - Cocher : `Exiger que l'utilisateur configure à nouveau ses méthodes d'authentification`
    - Enregistrer


### 4. Connexion test avec cet utilisateur

- Déconnecter la session administrateur
- Se connecter avec l’utilisateur MFA activé
- À la première connexion : configuration MFA obligatoire

### 5. Choix des méthodes d’authentification

- **Méthode recommandée** : Microsoft Authenticator (QR Code à scanner)
- Alternatives possibles :
    - Téléphone (appel vocal ou code SMS)
    - Clé de sécurité (matériel compatible FIDO2)

### 6. Finalisation

- Une fois le QR Code scanné, saisir le **code à usage unique** affiché
- Connexion réussie ➜ MFA actif et opérationnel

---

## 📢 Généralisation de la MFA à tout le tenant

### Méthode 1 : Utilisation du paramétrage MFA par utilisateur

- Répéter l’activation utilisateur par utilisateur
- Peu adaptée à grande échelle

### Méthode 2 : Activation de la stratégie de sécurité par défaut

- Centre d’administration Azure Active Directory : [https://aad.portal.azure.com](https://aad.portal.azure.com/)
- Menu **Propriétés > Gérer les paramètres de sécurité par défaut**
- Activer la stratégie
- Cela impose automatiquement la MFA pour tous les comptes dès la première connexion (admin et utilisateurs)

> ⚠️ Cette méthode ne permet pas de personnaliser la granularité (pas de MFA exclue).

---

## ✅ À retenir pour les révisions

- MFA = sécurité essentielle contre le **piratage de compte**
- Le déploiement peut être fait par **utilisateur** ou **globalement** via Azure AD
- L’application **Microsoft Authenticator** est recommandée (rapide et sécurisée)
- La configuration MFA s’impose à la **prochaine connexion** de l’utilisateur concerné

---

## 📌 Bonnes pratiques professionnelles

- Activer la MFA **en priorité sur tous les comptes administrateurs**
- Sensibiliser les utilisateurs sur la procédure MFA (QR code, téléphone…)
- Garder un **compte break-glass** (admin sans MFA, stocké offline et surveillé)
- Utiliser des **groupes conditionnels** et **politiques d’accès conditionnel** (licences AAD P1/P2)
- Vérifier l’activation via **Rapports MFA** dans le portail Azure AD