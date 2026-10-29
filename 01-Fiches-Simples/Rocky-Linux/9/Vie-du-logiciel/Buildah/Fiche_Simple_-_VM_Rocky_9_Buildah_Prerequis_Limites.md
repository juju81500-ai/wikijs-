# Fiche_Simple_-_VM_Rocky_9_Buildah_Prerequis_Limites.md

- **Environnement** : VM Rocky Linux 9 de build, compte non privilégié dédié
- **OS / Version** : Rocky Linux 9; paquet Buildah des dépôts de la distribution
- **Catégorie** : conteneurs / chaîne de build
- **Tags** : `buildah`, `oci`, `rocky9`, `rootless`, `containerfile`, `registre`

---

## Problème précis à résoudre

Contrôler que l'hôte et le compte de build conviennent avant d'installer Buildah.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler la version du système et l'espace disque du stockage d'images :
   ```bash
   cat /etc/rocky-release
   df -h "$HOME"
   ```
   👉 Explication : le stockage rootless est dans `~/.local/share/containers`.

2. Vérifier les plages d'identifiants du compte de build :
   ```bash
   grep "^$USER:" /etc/subuid /etc/subgid
   ```
   👉 Explication : des plages `subuid`/`subgid` doivent exister pour le mode rootless.

3. Vérifier l'accès au registre interne (ou public autorisé) pour récupérer les images de base.
   👉 Explication : sans registre joignable, le build échouera.

4. Noter les limites : ni CI, ni signature avancée de chaîne d'approvisionnement, ni Kubernetes; les options varient selon la version (`buildah --version`, `man buildah-build`).
   👉 Explication : on évite d'utiliser une option absente de la version installée.

## 2. Production — Contrôles

Utiliser un compte de build dédié non privilégié; sudo uniquement pour l'installation.

## 3. Production — Sécurité

- Podman n'est pas obligatoire : Buildah ne gère pas le cycle de vie des conteneurs en production.

## Validation et retour arrière

- **Validation** : Compte, espace, plages subuid/subgid et registre confirmés.
- **Retour arrière** : Aucune modification; rien à annuler.

## Si le problème n'est pas résolu

- [Buildah — Installation](https://github.com/containers/buildah/blob/main/install.md)
- [Buildah — buildah-build](https://github.com/containers/buildah/blob/main/docs/buildah-build.1.md)
- [Guide complet Buildah Rocky Linux 9](../../../../../02-Fiches-Completes/Rocky-Linux/9/Installation-Deploiement/87_Construction_Images_OCI_Buildah_Rocky_Linux_9.md#1-prerequis-et-limites)
