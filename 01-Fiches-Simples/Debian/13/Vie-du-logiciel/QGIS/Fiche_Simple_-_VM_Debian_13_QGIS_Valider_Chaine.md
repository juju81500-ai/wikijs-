# Fiche_Simple_-_VM_Debian_13_QGIS_Valider_Chaine.md

- **Environnement** : QGIS Desktop sur Debian 13 amd64
- **OS / Version** : Debian 13; QGIS 3.44 LTR
- **Catégorie** : SIG / validation
- **Tags** : `debian13`, `qgis`, `validation`, `pdf`, `mise-en-page`

---

## Problème précis à résoudre

Valider de bout en bout projet, données et export PDF.

## 1. Hors-Production (Lab / Test / POC)

1. Charger la couche test et confirmer l'absence d'avertissement de source manquante ou de CRS non résolu.
   👉 Explication : Contrôle visuel du rendu.

2. Sauvegarder (**Projet > Enregistrer**), fermer, puis rouvrir depuis l'emplacement final.
   👉 Explication : Vérifie que les couches restent valides.

3. Ouvrir la table attributaire : **clic droit sur la couche > Ouvrir la table d'attributs**.
   👉 Explication : Les valeurs doivent correspondre à la source.

4. Créer une mise en page : **Projet > Nouvelle mise en page**, ajouter titre, échelle, légende, sources, puis **Mise en page > Exporter en PDF** dans `exports/`.
   👉 Explication : Livrable reproductible.

5. Contrôler l'export :
   ```bash
   ls -l ~/SIG/projet/exports/
   ```
   👉 Explication : Remplacer le chemin par votre dossier; le PDF doit exister.

## 2. Production — Contrôles

Consigner auteur, version de QGIS, données, CRS et date; revue par un second opérateur pour toute modification de données maîtresses.

## 3. Production — Sécurité

- Travailler sur une copie des données maîtresses.
- La validation ne prouve ni l'exactitude métier ni la validité juridique d'une carte.

## Validation et retour arrière

- **Validation** : CRS, emprise et attributs concordent entre source et sortie.
- **Retour arrière** : supprimer les exports de test; la source n'a pas été modifiée.

## Si le problème n'est pas résolu

- [QGIS — installation Linux](https://qgis.org/resources/installation-guide/)
- [QGIS — guide utilisateur 3.44](https://docs.qgis.org/3.44/en/docs/user_manual/)
- [Guide complet QGIS Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/75_Deploiement_QGIS_3.44_LTR_Debian_13.md#6-verifier-la-chaine-projet-donnees-sortie)
