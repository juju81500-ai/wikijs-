# Fiche_Simple_-_VM_Rocky_9_Buildah_Sauvegarder_Etat_Initial.md

- **Environnement** : VM Rocky Linux 9 de build, compte non privilégié dédié
- **OS / Version** : Rocky Linux 9; paquet Buildah des dépôts de la distribution
- **Catégorie** : conteneurs / chaîne de build
- **Tags** : `buildah`, `oci`, `rocky9`, `rootless`, `containerfile`, `registre`

---

## Problème précis à résoudre

Conserver l'état des paquets et la configuration avant toute installation.

## 1. Hors-Production (Lab / Test / POC)

1. Noter les paquets de conteneurs présents :
   ```bash
   rpm -qa | grep -Ei 'buildah|podman|containers-common|skopeo' | sort | tee ~/etat-paquets-conteneurs.txt
   ```
   👉 Explication : la liste sert de point de comparaison.

2. Copier la configuration existante :
   ```bash
   sudo cp -a /etc/containers /root/etc-containers.$(date +%F).bak
   ```
   👉 Explication : permet de rétablir `/etc/containers` en cas de problème.

3. Exporter une image utile avant tout nettoyage (NOM_IMAGE, CHEMIN et TAG sont des exemples à remplacer) :
   ```bash
   buildah push NOM_IMAGE:TAG oci-archive:/chemin/image.tar:NOM_IMAGE:TAG
   ```
   👉 Explication : on garde une archive OCI des images à conserver.

## 2. Production — Contrôles

Conserver la copie de `/etc/containers` jusqu'à validation de l'installation.

## 3. Production — Sécurité

- Protéger les archives d'images (elles peuvent contenir des données sensibles).

## Validation et retour arrière

- **Validation** : Fichier d'état et copie de `/etc/containers` présents.
- **Retour arrière** : Supprimer les copies créées si elles ne sont plus utiles.

## Si le problème n'est pas résolu

- [Buildah — Installation](https://github.com/containers/buildah/blob/main/install.md)
- [Buildah — buildah-build](https://github.com/containers/buildah/blob/main/docs/buildah-build.1.md)
- [Guide complet Buildah Rocky Linux 9](../../../../../02-Fiches-Completes/Rocky-Linux/9/Installation-Deploiement/87_Construction_Images_OCI_Buildah_Rocky_Linux_9.md#2-sauvegarder-letat-initial)
