# 📄 Fiche_Simple_-_Docker_Snipe-IT_Importer_Actifs_CSV.md

- **Environnement** : Application Snipe-IT sur Docker Compose
- **OS / Version** : Snipe-IT 8.x, à confirmer dans `Admin > About`
- **Catégorie** : Gestion de parc / inventaire

---

## 🎯 Problème précis à résoudre

Importer un lot d'actifs sans créer d'assignations erronées ni écraser l'inventaire en production.

## 🧪 1. Hors-Production (Lab / Test / POC)

1. Préparer un CSV réduit (2 ou 3 actifs fictifs) et contrôler son encodage :
   ```bash
   file -i actifs.csv
   head -n 3 actifs.csv
   ```
   👉 Explication : l'encodage doit être `utf-8`; garder modèle et catégorie, créer avant les statuts, lieux et champs personnalisés dans l'interface.

2. Importer dans l'instance de test : **Assets > Import > Select File**, téléverser, **Import**, associer les colonnes, inspecter l'aperçu, lancer.
   👉 Explication : corriger les erreurs signalées avant de lancer.

3. Vérifier : **Assets > recherche du tag**, comparer modèle, catégorie, statut, emplacement au fichier source :
   ```bash
   docker compose logs --tail=50 snipeit
   ```
   👉 Explication : le service peut porter un autre nom dans votre `docker-compose.yml`.

## ⚡ 2. Production — Façon Simplifiée

1. Sauvegarder avant le lot : **Admin > Backups > Create Backup**, ou :
   ```bash
   docker compose exec snipeit php artisan snipeit:backup
   ```
   👉 Explication : archiver ensuite la sauvegarde hors hôte Docker.

2. Normaliser le CSV :
   ```bash
   file -i actifs.csv
   cut -d, -f1 actifs.csv | sort | uniq -d
   ```
   👉 Explication : UTF-8, en-tête stable, dates `YYYY-MM-DD`; la seconde commande liste les tags en double (colonne 1 : à adapter).

3. Importer sans checkout : **Assets > Import**, mapper, aperçu, lancer.
   👉 Explication : premier passage sans `Checkout Target`.

4. Réconcilier : **Assets > Import > Éléments traités**, puis journaux :
   ```bash
   docker compose exec snipeit tail -n 50 storage/logs/laravel.log
   ```
   👉 Explication : contrôler créés/modifiés, doublons et erreurs.

## 🔒 3. Production — Façon Sécurisée

- Commencer par un petit lot, puis augmenter progressivement la taille.
- Ne pas inclure `Checkout Target` dans le premier import. Si le checkout est nécessaire, tester d'abord les logins utilisateurs et les lieux; l'import peut créer des utilisateurs si les colonnes de checkout sont fournies.
- Les champs personnalisés doivent déjà exister et correspondre exactement à leur nom dans Snipe-IT; l'import ne crée pas les fieldsets.
- Protéger les CSV : ils peuvent contenir numéros de série, affectations et informations personnelles. Les supprimer des répertoires temporaires conformément à la politique.
- En cas de doublons ou de mauvais mapping, arrêter les imports suivants et restaurer la sauvegarde ou corriger les actifs via l'outil d'import de mise à jour après vérification des tags/IDs.

## ✅ Validation et retour arrière

- **Précontrôles** : sauvegarde restaurable, instance, version, modèle, statuts et tags uniques.
- **Validation** : échantillon avant/après, nombre de lignes traité, affectations et erreurs de validation.
- **Retour arrière** : restaurer la sauvegarde validée si le lot a modifié un grand nombre d'enregistrements de façon erronée.

## 🔗 Si le problème n'est pas résolu

- **Fiche de résolution complémentaire** : [[Docker_Snipe-IT_Import_CSV_Erreurs]]
- [Documentation officielle Snipe-IT — Importer des actifs](https://snipe-it.readme.io/docs/importing-assets)