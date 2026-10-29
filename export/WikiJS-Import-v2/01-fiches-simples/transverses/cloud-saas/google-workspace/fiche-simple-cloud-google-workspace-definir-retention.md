---
title: "Fiche Simple - Cloud Google Workspace Definir Retention"
description: "Définir la rétention des e-mails et des données Workspace."
published: true
date: 2026-10-29T20:32:32Z
tags: ["google-workspace", "gmail", "cloud-saas", "administration-defensive", "messagerie", "tssr"]
editor: markdown
dateCreated: 2026-10-29T20:32:32Z
dateModified: 2026-10-29T20:32:32Z
---

# Fiche_Simple_-_Cloud_Google_Workspace_Definir_Retention

- **Environnement** : Tenant Google Workspace (SaaS), administré via la console d'administration admin.google.com
- **OS / Version** : Cloud/SaaS — administration défensive (aucun OS à installer)
- **Catégorie** : messagerie et collaboratif
- **Tags** : `google-workspace`, `gmail`, `cloud-saas`, `administration-defensive`, `messagerie`, `tssr`

---

## Problème précis à résoudre

Définir la rétention des e-mails et des données Workspace.

## 1. Hors-Production (Lab / Test / POC)

1. Interface (édition incluant Vault) : console Google Vault > Rétention > Créer une règle de rétention pour le service Gmail, durée définie par l'organisation.
   👉 Explication : Vault dépend de l'édition ou d'une licence complémentaire; vérifier.

2. Pour un besoin juridique, créer un blocage (Vault > Affaires > Blocages) plutôt que d'allonger la rétention globale.
   👉 Explication : le blocage est limité à des utilisateurs précis et tracé.

3. Vérifier côté console : Applications > Google Workspace > Gmail > Paramètres pour la corbeille et conserver la configuration documentée.
   👉 Explication : la rétention de la corbeille utilisateur est distincte de Vault.

## 2. Production — Contrôles

Faire valider les durées par le juridique/DPO.

## 3. Production — Sécurité

- Restreindre les rôles Vault.
- Consulter le journal d'audit Vault.

## Validation et retour arrière

- **Validation** : La règle apparaît dans Vault avec l'état attendu.
- **Retour arrière** : Supprimer ou modifier la règle; noter qu'une suppression définitive de données peut être irréversible : tester sur une unité pilote.

## Si le problème n'est pas résolu

- [Règles de rétention Vault](https://support.google.com/vault/answer/2990828)
- [Centre d'aide Google Workspace Admin](https://support.google.com/a/)
- [Fiche d'entrée Google Workspace](/01-fiches-simples/logiciels/12-messagerie-et-collaboratif/fiche-logiciel-google-workspace)