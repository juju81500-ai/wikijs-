# Fiche_Simple_-_VM_Rocky_9_Buildah_Valider_Image.md

- **Environnement** : VM Rocky Linux 9 de build, compte non privilégié dédié
- **OS / Version** : Rocky Linux 9; paquet Buildah des dépôts de la distribution
- **Catégorie** : conteneurs / chaîne de build

---

## Problème précis à résoudre

Contrôler l'image avant publication.

## 1. Hors-Production (Lab / Test / POC)

1. Relire les métadonnées (utilisateur, ports, variables, point d'entrée, étiquettes) :
   ```bash
   buildah inspect localhost/APPLICATION:VERSION
   ```
   👉 Explication : APPLICATION et VERSION sont à remplacer; l'utilisateur ne doit pas être root.

2. Tester l'image dans un conteneur temporaire avec un outil d'exécution approuvé (par exemple Podman) avec volumes et ports restreints.
   👉 Explication : on valide le démarrage sans privilèges.

3. Passer le scanner de vulnérabilités de la politique interne avant publication.
   👉 Explication : on évite de publier une image vulnérable.

## 2. Production — Contrôles

Critère de réussite : build reproductible, image démarrée sans privilèges et sans secret embarqué.

## 3. Production — Sécurité

- Aucun secret embarqué dans l'image.

## Validation et retour arrière

- **Validation** : Métadonnées conformes, démarrage sans privilèges, scan accepté.
- **Retour arrière** : Ne pas publier; supprimer l'image locale non conforme.

## Si le problème n'est pas résolu

- [Buildah — Installation](https://github.com/containers/buildah/blob/main/install.md)
- [Buildah — buildah-build](https://github.com/containers/buildah/blob/main/docs/buildah-build.1.md)
- [Guide complet Buildah Rocky Linux 9](/02-fiches-completes/rocky-linux/9/installation-deploiement/87-construction-images-oci-buildah-rocky-linux-9#5-valider-limage)