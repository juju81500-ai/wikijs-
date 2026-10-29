# Fiche_Simple_-_VM_Debian_13_Podman_Buildah_Construire_Image_Buildah

- **Environnement** : VM Debian 13 de laboratoire, utilisateur sudoer et compte de service dédié
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : conteneurs
- **Tags** : `debian13`, `podman`, `buildah`, `conteneurs`, `rootless`, `oci`

---

## Problème précis à résoudre

Construire une image OCI reproductible avec Buildah à partir d'un Containerfile.

## 1. Hors-Production (Lab / Test / POC)

1. Préparer un contexte minimal avec un `.containerignore` excluant `.git`, secrets et fichiers inutiles.
   👉 Explication : réduit le contexte et le risque de fuite.

2. Écrire un Containerfile (REGISTRE, IMAGE_DE_BASE, VERSION_FIXE, COMMANDES_DE_INSTALLATION et UTILISATEUR_NON_ROOT sont à remplacer) :
   ```dockerfile
   FROM REGISTRE/IMAGE_DE_BASE:VERSION_FIXE
   RUN COMMANDES_DE_INSTALLATION
   USER UTILISATEUR_NON_ROOT
   ```
   👉 Explication : image de base épinglée, jamais `latest` ; aucun secret dans le fichier.

3. Construire puis inspecter (APPLICATION et VERSION à remplacer) :
   ```bash
   buildah build --format oci -t localhost/APPLICATION:VERSION -f Containerfile .
   buildah images
   buildah inspect localhost/APPLICATION:VERSION
   ```
   👉 Explication : `buildah build` lit le Containerfile ; le format OCI est choisi explicitement.

4. Tester l'image avec Podman :
   ```bash
   podman run --rm localhost/APPLICATION:VERSION
   ```
   👉 Explication : Podman et Buildah partagent le stockage du compte.

## 2. Production — Contrôles

Construire depuis un dépôt propre, avec une image de base approuvée. Commandes établies d'après la documentation officielle et non testées dans ce pack : à valider en lab avant toute production.

## 3. Production — Sécurité

- Aucun secret dans les arguments de build (visibles dans l'historique).
- Exécuter l'application sous un utilisateur non root.

## Validation et retour arrière

- **Validation** : l'image est listée par `buildah images` et démarre avec Podman.
- **Retour arrière** : `buildah rmi localhost/APPLICATION:VERSION`.

## Si le problème n'est pas résolu

- [Buildah — documentation](https://buildah.io/)
- [Buildah — buildah-build](https://github.com/containers/buildah/blob/main/docs/buildah-build.1.md)
- [Fiche connexe — Prerequis Limites](Fiche_Simple_-_VM_Debian_13_Podman_Buildah_Prerequis_Limites.md)
