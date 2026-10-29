# Fiche_Simple_-_VM_Debian_13_QGIS_Valider_Projet.md

- **Environnement** : QGIS 3.44 LTR sur Debian 13, jeu de données de test
- **OS / Version** : Debian 13 Trixie amd64
- **Catégorie** : SIG / cartographie

---

## Problème précis à résoudre

Valider qu'un projet QGIS retrouve ses données, interprète les CRS correctement et produit une sortie reproductible.

## 1. Hors-Production (Lab / Test / POC)

1. Confirmer la version et la branche LTR :
   ```bash
   qgis --version
   apt-cache policy qgis
   ```
   👉 Explication : la version doit être la branche LTR prévue.

2. Ouvrir un jeu de données de test autorisé : **Couche > Ajouter une couche > Ajouter une couche vecteur**, puis clic droit sur la couche > **Propriétés > Information** et **Table d'attributs** (F6).
   👉 Explication : vérifier CRS déclaré, étendue, champs et quelques entités.

3. Régler le CRS du projet : **Projet > Propriétés > SCR** (ou le bouton en bas à droite).
   👉 Explication : ne pas confondre « définir le SCR de la couche » (attribution) et « Exporter > Sauvegarder sous... » (reprojection).

4. Enregistrer en `.qgz` : **Projet > Enregistrer sous...**, puis **Projet > Propriétés > Général > Chemins : Relatifs**; fermer et rouvrir : **Projet > Ouvrir**.
   👉 Explication : chemins relatifs pour que le dossier reste déplaçable.

5. Exporter une carte PDF : **Projet > Nouvelle mise en page d'impression**, ajouter carte, légende, échelle, puis **Mise en page > Exporter au format PDF**.
   👉 Explication : vérifier échelle, légende, sources et rendu.

## 2. Production — Contrôles

Avant le livrable, consigner la version QGIS, les sources et dates des données, les CRS source et projet, l'opération de transformation utilisée, l'emprise, le responsable et la revue métier.

## 3. Production — Sécurité

- N'utiliser que des données autorisées et respecter leur niveau de confidentialité et de redistribution.
- Ne pas activer les macros de projets inconnus; examiner plugins et scripts avant installation ou exécution.
- Ne pas stocker de secrets dans le projet ou les chemins de données; protéger le coffre d'authentification QGIS.
- Sauvegarder le projet et les données externes nécessaires; tester la réouverture depuis une copie restaurée.

## Validation et retour arrière

- **Validation** : pas de couche manquante, CRS compris, projet rouvert, attributs cohérents et export rendu.
- **Retour arrière** : conserver le projet original et les données sources; annuler les modifications sur la copie de travail.

## Si le problème n'est pas résolu

- [QGIS — aide officielle](https://qgis.org/resources/hub/)
- [QGIS 3.44 — gestion des projets](https://docs.qgis.org/3.44/en/docs/user_manual/introduction/project_files.html)
- [QGIS 3.44 — projections](https://docs.qgis.org/3.44/en/docs/user_manual/working_with_projections/working_with_projections.html)
- [Guide complet QGIS 3.44 LTR Debian 13](/02-fiches-completes/debian/13/installation-deploiement/75-deploiement-qgis-3-44-ltr-debian-13)