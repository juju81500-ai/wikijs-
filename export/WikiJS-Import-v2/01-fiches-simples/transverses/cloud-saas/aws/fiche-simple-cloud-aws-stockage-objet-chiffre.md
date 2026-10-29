---
title: "Fiche Simple - Cloud AWS Stockage Objet Chiffre"
description: "Stockage objet chiffré dans AWS en limitant les risques de sécurité, de disponibilité et de coût."
published: true
date: 2026-10-29T21:01:53Z
tags: ["aws", "stockage_objet_chiffre", "securite", "procedure"]
editor: markdown
dateCreated: 2026-10-29T21:01:53Z
dateModified: 2026-10-29T21:01:53Z
---

# Fiche_Simple_-_Cloud_AWS_Stockage_Objet_Chiffre

- **Environnement** : tenant/compte de laboratoire contrôlé ; accès d’administration autorisé
- **OS / Version** : Cloud/SaaS — AWS CLI v2
- **Catégorie** : cloud public / stockage objet chiffré
- **Tags** : `aws`, `stockage_objet_chiffre`, `securite`, `procedure`

---

## Problème précis à résoudre

Stockage objet chiffré dans AWS en limitant les risques de sécurité, de disponibilité et de coût.

Les valeurs écrites en MAJUSCULES sont des placeholders à remplacer par les valeurs validées de l’environnement. Ne coller aucun secret réel dans les commandes, les fiches ou l’historique shell.

## 1. Hors-Production (Lab / Test / POC)

1. Console : S3 → Buckets → Create bucket ; Properties → Default encryption ; Permissions → Block public access.
   👉 Explication : vérifier le compte/projet/abonnement et la région sélectionnés avant toute modification.
2. CLI officielle (AWS CLI v2) :
   ```bash
aws s3 mb s3://NOM_BUCKET_UNIQUE --region REGION
aws s3api put-public-access-block --bucket NOM_BUCKET_UNIQUE --public-access-block-configuration BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true
aws s3api put-bucket-encryption --bucket NOM_BUCKET_UNIQUE --server-side-encryption-configuration '{"Rules":[{"ApplyServerSideEncryptionByDefault":{"SSEAlgorithm":"AES256"}}]}'
aws s3api get-bucket-encryption --bucket NOM_BUCKET_UNIQUE
   ```
   👉 Explication : Activer le blocage d’accès public et le chiffrement par défaut SSE-S3 ou SSE-KMS selon la politique ; attribuer les droits par rôles et valider avant chargement.
3. Console et CLI : comparer la configuration affichée avec l’état attendu, puis valider sur une ressource pilote non sensible.
   👉 Explication : les interfaces évoluent ; vérifier l’aide/version officielle et les quotas/licences avant généralisation.

## 2. Production — Contrôles

Valider classification des données, région, rétention, versioning, coûts de requêtes et droits des rôles. Tester lecture/écriture et récupération.

## 3. Production — Sécurité

Interdire l’accès public, chiffrer au repos/en transit, limiter les accès, protéger les clés et appliquer les obligations de résidence/rétention. Aucun secret dans le nom ou les métadonnées.

## Validation et retour arrière

- **Validation** : Le chiffrement et les contrôles d’accès sont vérifiés par console/CLI ; un utilisateur non autorisé ne peut pas lire les objets.
- **Retour arrière** : Revenir à la dernière configuration approuvée ; préserver les sauvegardes et journaux. Ne supprimer la ressource de test qu’après validation des dépendances et du propriétaire.

## Si le problème n'est pas résolu

- [AWS — documentation officielle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html)
- [Référence et bonnes pratiques](https://docs.aws.amazon.com/AmazonS3/latest/userguide/serv-side-encryption.html)
- [Fiche d’entrée AWS](/01-fiches-simples/logiciels/10-cloud-public-et-hybride/fiche-logiciel-aws)