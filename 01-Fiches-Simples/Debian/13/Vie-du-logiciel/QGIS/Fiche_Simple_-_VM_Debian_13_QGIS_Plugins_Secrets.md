# Fiche_Simple_-_VM_Debian_13_QGIS_Plugins_Secrets.md

- **Environnement** : QGIS Desktop sur Debian 13 amd64
- **OS / Version** : Debian 13; QGIS 3.44 LTR
- **Catégorie** : SIG / sécurité
- **Tags** : `debian13`, `qgis`, `plugins`, `macros`, `authentification`

---

## Problème précis à résoudre

Limiter les plugins et macros et protéger les secrets de connexion.

## 1. Hors-Production (Lab / Test / POC)

1. Installer uniquement les plugins approuvés : **Extensions > Installer/Gérer les extensions**.
   👉 Explication : Consigner versions et responsables.

2. Garder la demande d'autorisation des macros : **Projet > Propriétés > Macros**, option **Demander** (ou équivalent restrictif).
   👉 Explication : Évite d'exécuter le code d'un projet inconnu.

3. Enregistrer les connexions sensibles dans le gestionnaire d'authentification : **Préférences > Options > Authentification**.
   👉 Explication : Définir un mot de passe principal et le sauvegarder séparément.

4. Chercher des secrets en clair dans un projet décompressé :
   ```bash
   unzip -p projet.qgz '*.qgs' | grep -i -E 'password|token' || echo "aucun secret apparent"
   ```
   👉 Explication : Remplacer `projet.qgz` par votre fichier; contrôle rapide.

## 2. Production — Contrôles

Respecter licences, confidentialité et restrictions de redistribution des données, fonds de carte et plugins.

## 3. Production — Sécurité

- Aucun mot de passe ni token en clair dans projets, chemins ou scripts.
- Ne pas ouvrir un projet inconnu avec macros Python autorisées.

## Validation et retour arrière

- **Validation** : plugins listés, macros restrictives, aucun secret en clair.
- **Retour arrière** : désinstaller le plugin concerné dans le gestionnaire d'extensions.

## Si le problème n'est pas résolu

- [QGIS — installation Linux](https://qgis.org/resources/installation-guide/)
- [QGIS — guide utilisateur 3.44](https://docs.qgis.org/3.44/en/docs/user_manual/)
- [Guide complet QGIS Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/75_Deploiement_QGIS_3.44_LTR_Debian_13.md#5-controler-plugins-scripts-et-secrets)
