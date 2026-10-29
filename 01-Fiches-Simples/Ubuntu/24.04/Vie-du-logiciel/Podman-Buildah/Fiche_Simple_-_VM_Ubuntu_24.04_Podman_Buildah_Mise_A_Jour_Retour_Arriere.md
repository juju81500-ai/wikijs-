# Fiche_Simple_-_VM_Ubuntu_24.04_Podman_Buildah_Mise_A_Jour_Retour_Arriere

- **Environnement** : VM Ubuntu 24.04 LTS de laboratoire, utilisateur sudoer et compte de service dédié
- **OS / Version** : Ubuntu 24.04 LTS
- **Catégorie** : conteneurs
- **Tags** : `ubuntu2404`, `podman`, `buildah`, `conteneurs`, `rootless`, `oci`

---

## Problème précis à résoudre

Mettre à jour Podman/Buildah et les images, puis revenir en arrière.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder (fiche Sauvegarder_Restaurer) puis lister les versions :
   ```bash
   apt-cache policy podman buildah
   ```
   👉 Explication : prépare le retour arrière.

2. Mettre à jour et figer ensuite si besoin :
   ```bash
   sudo apt update
   sudo apt install --only-upgrade podman buildah
   sudo apt-mark hold podman buildah
   ```
   👉 Explication : met à jour les deux paquets ; `apt-mark unhold` pour lever le gel.

3. Contrôler après mise à jour :
   ```bash
   podman --version
   buildah --version
   podman system migrate
   systemctl --user restart APPLICATION.service
   ```
   👉 Explication : `podman system migrate` est recommandé par la documentation après certaines mises à jour pour reprendre les conteneurs existants ; vérifier les notes de version.

4. Mettre à jour une image applicative : changer `VERSION_FIXE` dans le fichier `.container`, `daemon-reload`, redémarrer.
   👉 Explication : évite `latest` et conserve l'ancienne version pour revenir.

5. Retour arrière des paquets (VERSION_APT et VERSION_BUILDAH à remplacer) :
   ```bash
   sudo apt install podman=VERSION_APT buildah=VERSION_BUILDAH
   ```
   👉 Explication : possible seulement si la version est encore publiée (`apt-cache madison podman`) ; sinon réinstaller les `.deb` archivés.

## 2. Production — Contrôles

Tester sur pilote et lire les notes de version Podman avant chaque montée. Commandes établies d'après la documentation officielle et non testées dans ce pack : à valider en lab avant toute production.

## 3. Production — Sécurité

- Ne mettre à jour que depuis le dépôt de la distribution approuvé.

## Validation et retour arrière

- **Validation** : les versions attendues sont actives et les services redémarrent.
- **Retour arrière** : rétrograder les paquets puis restaurer configuration et volumes.

## Si le problème n'est pas résolu

- [Notes de version Podman](https://github.com/containers/podman/releases)
- [Fiche connexe — Prerequis Limites](Fiche_Simple_-_VM_Ubuntu_24.04_Podman_Buildah_Prerequis_Limites.md)
