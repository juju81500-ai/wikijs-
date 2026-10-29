# Fiche_Simple_-_VM_Rocky_9_Buildah_Construire_Image.md

- **Environnement** : VM Rocky Linux 9 de build, compte non privilégié dédié
- **OS / Version** : Rocky Linux 9; paquet Buildah des dépôts de la distribution
- **Catégorie** : conteneurs / chaîne de build
- **Tags** : `buildah`, `oci`, `rocky9`, `rootless`, `containerfile`, `registre`

---

## Problème précis à résoudre

Construire une image OCI à partir d'un Containerfile versionné.

## 1. Hors-Production (Lab / Test / POC)

1. Placer un `Containerfile` versionné dans un dépôt avec un contexte minimal, et un `.containerignore` excluant secrets, `.git` et fichiers inutiles.
   👉 Explication : on réduit le contexte et le risque de fuite.

2. Exemple de Containerfile (REGISTRE, IMAGE_DE_BASE, VERSION_FIXE, COMMANDES_DE_INSTALLATION et UTILISATEUR_NON_ROOT sont à remplacer par vos valeurs) :
   ```dockerfile
   FROM REGISTRE/IMAGE_DE_BASE:VERSION_FIXE
   RUN COMMANDES_DE_INSTALLATION
   USER UTILISATEUR_NON_ROOT
   ```
   👉 Explication : image de base épinglée par version ou digest, jamais `latest`; aucun secret dans le fichier ni dans les arguments de build.

3. Construire puis inspecter (APPLICATION et VERSION à remplacer) :
   ```bash
   buildah build --format oci -t localhost/APPLICATION:VERSION -f Containerfile .
   buildah images
   buildah inspect localhost/APPLICATION:VERSION
   ```
   👉 Explication : `buildah build` lit le Containerfile et le contexte `.`.

## 2. Production — Contrôles

Pour un contrôle fin, la méthode scriptée (`buildah from`, `buildah run`, `buildah commit`) existe : la documenter dans le dépôt pour la rendre rejouable.

## 3. Production — Sécurité

- Pas de secret dans le Containerfile ni dans les arguments (visibles dans l'historique de l'image).
- Épingler les images de base.

## Validation et retour arrière

- **Validation** : Image construite depuis un dépôt propre et listée par `buildah images`.
- **Retour arrière** : Supprimer l'image de test avec `buildah rmi localhost/APPLICATION:VERSION`.

## Si le problème n'est pas résolu

- [Buildah — Installation](https://github.com/containers/buildah/blob/main/install.md)
- [Buildah — buildah-build](https://github.com/containers/buildah/blob/main/docs/buildah-build.1.md)
- [Guide complet Buildah Rocky Linux 9](../../../../../02-Fiches-Completes/Rocky-Linux/9/Installation-Deploiement/87_Construction_Images_OCI_Buildah_Rocky_Linux_9.md#4-construire-une-image-reproductible)
