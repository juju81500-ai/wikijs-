# Fiche_Simple_-_Cloud_GCP_Stockage_Objet_Chiffre

- **Environnement** : tenant/compte de laboratoire contrôlé ; accès d’administration autorisé
- **OS / Version** : Cloud/SaaS — Google Cloud CLI (gcloud ; version publiée à vérifier)
- **Catégorie** : cloud public / stockage objet chiffré
- **Tags** : `gcp`, `stockage_objet_chiffre`, `securite`, `procedure`

---

## Problème précis à résoudre

Stockage objet chiffré dans Google Cloud Platform en limitant les risques de sécurité, de disponibilité et de coût.

Les valeurs écrites en MAJUSCULES sont des placeholders à remplacer par les valeurs validées de l’environnement. Ne coller aucun secret réel dans les commandes, les fiches ou l’historique shell.

## 1. Hors-Production (Lab / Test / POC)

1. Console : Cloud Storage → Buckets → Create ; choisir région/classe ; Protection → Public access prevention ; Configuration → Encryption.
   👉 Explication : vérifier le compte/projet/abonnement et la région sélectionnés avant toute modification.
2. CLI officielle (Google Cloud CLI (gcloud ; version publiée à vérifier)) :
   ```bash
   gcloud storage buckets create gs://NOM_BUCKET_UNIQUE --location=REGION --uniform-bucket-level-access --public-access-prevention
gcloud storage buckets describe gs://NOM_BUCKET_UNIQUE
   ```
   👉 Explication : Le chiffrement Google-managed est par défaut ; configurer CMEK si exigé et contrôler accès uniforme/prévention d’accès public, versioning, rétention et région avant dépôt.
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

- [Google Cloud Platform — documentation officielle](https://cloud.google.com/storage/docs/creating-buckets)
- [Référence et bonnes pratiques](https://cloud.google.com/storage/docs/encryption)
- [Fiche d’entrée Google Cloud Platform](../../../Logiciels/10-Cloud-public-et-hybride/Fiche_Logiciel_-_Google-Cloud-Platform.md)
