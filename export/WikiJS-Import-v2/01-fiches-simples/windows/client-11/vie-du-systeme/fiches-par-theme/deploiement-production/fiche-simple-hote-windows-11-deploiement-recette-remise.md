---
title: "Fiche Simple - Hote Windows 11 Deploiement Recette Remise"
description: "Valider le poste avant remise à l'utilisateur."
published: true
date: 2026-10-29T20:22:42Z
tags: ["windows11", "deploiement", "oobe", "bitlocker", "production"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# Fiche_Simple_-_Hote_Windows_11_Deploiement_Recette_Remise.md

- **Environnement** : Parc de postes utilisateur: poste physique ou VM de test
- **OS / Version** : Windows 11 Pro ou Enterprise selon la gestion prévue
- **Catégorie** : déploiement de poste de travail
- **Tags** : `windows11`, `deploiement`, `oobe`, `bitlocker`, `production`

---

## Problème précis à résoudre

Valider le poste avant remise à l'utilisateur.

## 1. Hors-Production (Lab / Test / POC)

1. Tester ouverture de session, réseau, DNS, VPN, applications, imprimantes/périphériques et outils de support.
   👉 Explication : valide l'usage quotidien.

2. Tester le DNS depuis le poste (remplacer `intranet.example.net` par un nom interne réel) :
   ```powershell
   Resolve-DnsName intranet.example.net
   ```
   👉 Explication : confirme la résolution des noms internes.

3. Vérifier la récupération des fichiers via OneDrive, l'historique des fichiers ou la solution de sauvegarde retenue.
   👉 Explication : garantit la restauration des données utilisateur.

4. Documenter nom de poste, utilisateur, build, état BitLocker et réception.
   👉 Explication : traçabilité de la remise.

## 2. Production — Contrôles

Remettre le poste avec un procès-verbal signé.

## 3. Production — Sécurité

- Ne jamais inscrire mot de passe ou clé de récupération dans le procès-verbal.

## Validation et retour arrière

- **Validation** : tous les tests de recette sont réussis et le PV est signé.
- **Retour arrière** : retenir le poste hors remise utilisateur jusqu'à correction.

## Si le problème n'est pas résolu

- [Microsoft Learn — déployer Windows 11](https://learn.microsoft.com/en-us/windows/deployment/)
- [Microsoft Learn — déployer Windows 11](https://learn.microsoft.com/en-us/windows/deployment/)
- [Guide complet](/02-fiches-completes/windows/client-11/installation-deploiement/25-deploiement-postes-windows-11-production#6-recette-et-remise)