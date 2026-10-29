# Fiche_Simple_-_VM_Debian_13_QGIS_Projet_Reproductible.md

- **Environnement** : QGIS Desktop sur Debian 13 amd64
- **OS / Version** : Debian 13; QGIS 3.44 LTR
- **Catégorie** : SIG / projet

---

## Problème précis à résoudre

Créer un projet QGIS portable avec CRS maîtrisé.

## 1. Hors-Production (Lab / Test / POC)

1. Créer l'arborescence de travail (remplacer `~/SIG/projet` par votre dossier) :
   ```bash
   mkdir -p ~/SIG/projet/data ~/SIG/projet/exports
   ```
   👉 Explication : Sépare données et exports; garder les sources originales en lecture seule.

2. Lancer QGIS depuis le menu graphique, puis charger une copie de travail : **Couche > Ajouter une couche > Ajouter une couche vecteur**.
   👉 Explication : Utiliser un GeoPackage de test autorisé.

3. Vérifier CRS, étendue, champs et nombre d'entités : **clic droit sur la couche > Propriétés > Information**.
   👉 Explication : Contrôle avant toute analyse.

4. Définir le CRS du projet : **Projet > Propriétés > SCR**.
   👉 Explication : La reprojection à l'écran ne modifie pas les coordonnées de la source.

5. Enregistrer en `.qgz` avec chemins relatifs : **Projet > Propriétés > Général > Enregistrer les chemins : Relatifs**.
   👉 Explication : Facilite le déplacement contrôlé du dossier.

## 2. Production — Contrôles

Distinguer « définir le CRS source » de « reprojeter »; vérifier les grilles de transformation pour les opérations géodésiques.

## 3. Production — Sécurité

- Ne pas attribuer arbitrairement un EPSG à un CRS inconnu.

## Validation et retour arrière

- **Validation** : le projet se rouvre depuis son emplacement avec des couches valides.
- **Retour arrière** : supprimer le dossier de projet de test; les sources originales restent intactes.

## Si le problème n'est pas résolu

- [QGIS — installation Linux](https://qgis.org/resources/installation-guide/)
- [QGIS — guide utilisateur 3.44](https://docs.qgis.org/3.44/en/docs/user_manual/)
- [Guide complet QGIS Debian 13](/02-fiches-completes/debian/13/installation-deploiement/75-deploiement-qgis-3-44-ltr-debian-13#4-preparer-un-projet-reproductible)