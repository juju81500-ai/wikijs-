# Construire des images OCI avec Buildah sur Rocky Linux 9

- **OS / Version** : Rocky Linux 9, paquet Buildah des dépôts maintenus de la distribution
- **Type de fiche** : Installation/Déploiement
- **Périmètre** : Poste ou serveur de build rootless, construction locale, signature/publication d'images vers un registre interne de laboratoire. Complète le guide [Podman Quadlet](57_Deploiement_Podman_Quadlet_Rocky_Linux_9.md), qui traite l'exécution et non la construction.
- **Catégorie** : Conteneurs / chaîne de build
- **Tags** : `buildah`, `oci`, `rocky9`, `rootless`, `containerfile`, `conteneurs`, `registre`

## 1. Prérequis et limites

Fiche simple : [vérifier prérequis et limites](../../../../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/Buildah/Fiche_Simple_-_VM_Rocky_9_Buildah_Prerequis_Limites.md).

- Rocky Linux 9 à jour, compte de build non privilégié dédié, accès sudo uniquement pour l'installation.
- Podman n'est pas obligatoire : Buildah construit et manipule les images, il ne gère pas le cycle de vie des conteneurs en production.
- Espace disque dédié au stockage des images (`~/.local/share/containers` en rootless) et plages `subuid`/`subgid` disponibles pour le compte.
- Accès à un registre interne (ou à un registre public autorisé par la politique) pour récupérer les images de base.
- Limites : cette fiche ne couvre ni l'ordonnancement de builds (CI), ni la signature de chaîne d'approvisionnement avancée, ni Kubernetes. Les paquets et options varient selon la version de Buildah : vérifier `buildah --version` et `man buildah-build` sur l'hôte avant d'utiliser une option.

## 2. Sauvegarder l'état initial

Fiche simple : [sauvegarder l'état initial](../../../../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/Buildah/Fiche_Simple_-_VM_Rocky_9_Buildah_Sauvegarder_Etat_Initial.md).

Avant d'installer, noter les paquets de conteneurs déjà présents et conserver la configuration existante :

```bash
rpm -qa | grep -Ei 'buildah|podman|containers-common|skopeo' | sort | tee ~/etat-paquets-conteneurs.txt
sudo cp -a /etc/containers /root/etc-containers.$(date +%F).bak
```

Pour un compte qui contient déjà des images utiles, les exporter avant toute opération de nettoyage (`buildah push <image> oci-archive:/chemin/image.tar:<nom>:<tag>`).

## 3. Installer Buildah

Fiche simple : [installer Buildah](../../../../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/Buildah/Fiche_Simple_-_VM_Rocky_9_Buildah_Installer.md).

La documentation du projet indique l'installation par le gestionnaire de paquets de la distribution (`dnf` pour les familles Fedora/RHEL). Contrôler la version proposée puis installer :

```bash
dnf info buildah
sudo dnf install -y buildah
buildah --version
buildah info
```

Le paquet installe aussi `runc`/`crun` requis par `buildah run` et les instructions `RUN`; ne pas compiler depuis les sources en production sans besoin documenté.

Vérifier les plages d'identifiants du compte de build et ne pas les dupliquer :

```bash
grep "^$USER:" /etc/subuid /etc/subgid
```

Si elles manquent, utiliser les plages libres décidées par l'administrateur (voir `man subuid`), puis exécuter `podman system migrate` ou rouvrir la session si Podman est installé.

## 4. Construire une image reproductible

Fiche simple : [construire une image reproductible](../../../../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/Buildah/Fiche_Simple_-_VM_Rocky_9_Buildah_Construire_Image.md).

Placer un `Containerfile` versionné dans un dépôt avec un contexte minimal et un `.containerignore` pour exclure secrets, `.git` et fichiers inutiles.

```dockerfile
FROM <registre-interne>/<image-de-base>:<version-fixe>
RUN <commandes-de-installation-du-service>
USER <utilisateur-non-root>
```

Choisir une image de base officielle ou interne, épinglée par version ou digest, jamais `latest`. N'inclure aucun secret dans le Containerfile ni dans les arguments de build : ils restent lisibles dans l'historique de l'image.

```bash
buildah build --format oci -t localhost/<application>:<version> -f Containerfile .
buildah images
buildah inspect localhost/<application>:<version>
```

`buildah build` (alias `bud`) lit un Containerfile ou Dockerfile et un contexte de build. Pour un contrôle fin, la méthode scriptée existe (`buildah from`, `buildah run`, `buildah commit`) ; la documenter dans le dépôt avec ses entrées pour la rendre rejouable.

## 5. Valider l'image

Fiche simple : [valider l'image](../../../../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/Buildah/Fiche_Simple_-_VM_Rocky_9_Buildah_Valider_Image.md).

- Relire `buildah inspect` : utilisateur, ports exposés, variables d'environnement, point d'entrée, étiquettes de version.
- Tester l'image localement dans un conteneur temporaire avec un outil d'exécution approuvé (par exemple Podman, voir le guide 57) avec volumes et ports restreints.
- Contrôler les paquets et vulnérabilités avec le scanner de la politique interne avant publication.
- Critère de réussite : build reproductible à partir d'un dépôt propre, image démarrée sans privilèges et sans secret embarqué.

## 6. Publier et revenir en arrière

Fiche simple : [publier et revenir en arrière](../../../../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/Buildah/Fiche_Simple_-_VM_Rocky_9_Buildah_Publier_Retour_Arriere.md).

```bash
buildah login <registre-interne>
buildah push localhost/<application>:<version> docker://<registre-interne>/<projet>/<application>:<version>
```

Publier un tag immuable par version. Pour le retour arrière, redéployer le tag précédent ou son digest ; ne pas réécrire un tag déjà utilisé en production. Conserver au moins la version précédente dans le registre et une archive OCI de la version déployée.

## 7. Exploitation et nettoyage

Fiche simple : [exploiter et nettoyer](../../../../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/Buildah/Fiche_Simple_-_VM_Rocky_9_Buildah_Exploitation_Nettoyage.md).

```bash
buildah containers
buildah rm <conteneur-de-travail>
buildah rmi localhost/<application>:<version-obsolete>
```

Ne pas lancer de suppression globale (`buildah rm --all`, `buildah rmi --all`) sur un hôte partagé sans avoir vérifié les images à conserver. Surveiller l'espace disque, appliquer régulièrement les mises à jour du paquet et des images de base, puis reconstruire les images affectées. En cas d'échec après mise à jour de Buildah, réinstaller la version précédente disponible dans le dépôt interne et rétablir `/etc/containers` depuis la copie faite en section 2.

## Sources

- [Buildah — Installation Instructions](https://github.com/containers/buildah/blob/main/install.md)
- [Buildah — buildah-build](https://github.com/containers/buildah/blob/main/docs/buildah-build.1.md)
- [Buildah — site officiel](https://buildah.io/)
- [Rocky Linux — Documentation officielle](https://docs.rockylinux.org/)
