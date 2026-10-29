# Déployer Minikube avec le driver Docker sur Debian 13

- **OS / Version** : Debian 13 Trixie, architecture amd64 ou arm64, Docker Engine déjà installé
- **Type de fiche** : Installation/Déploiement
- **Périmètre** : Cluster Kubernetes mono-nœud de laboratoire ou de développement. Ne convient pas à la production ni à la haute disponibilité (voir le guide [K3s](14_Orchestration_Cluster_K3s_Kubernetes_Debian_13.md) et le guide [kubeadm](89_Deploiement_Cluster_Kubernetes_kubeadm_Debian_13.md)).
- **Catégorie** : Conteneurs / Kubernetes
- **Tags** : `minikube`, `kubernetes`, `debian13`, `docker`, `lab`, `kubectl`

## 1. Prérequis

Fiche simple : [vérifier les prérequis Minikube](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Minikube/Fiche_Simple_-_VM_Debian_13_Minikube_Prerequis.md).

- Docker Engine installé selon la [documentation officielle Docker](https://docs.docker.com/engine/install/debian/), version 18.09 minimum et 20.10 ou plus recommandée selon la page du driver Docker de Minikube. Appliquer aussi le durcissement de l'hôte du guide 32.
- Compte non-root autorisé à utiliser Docker. Attention : l'appartenance au groupe `docker` équivaut à des droits root sur l'hôte ; utiliser une VM de laboratoire dédiée.
- CPU, mémoire et disque adaptés à la charge : dimensionner explicitement avec `--cpus` et `--memory` plutôt que se fier aux valeurs par défaut.
- Accès sortant vers les registres d'images nécessaires, ou miroir interne.

Limites : un seul nœud, pas de tolérance de panne ; les restrictions de sécurité du runtime Docker listées dans la page du driver (options non supportées) peuvent empêcher le démarrage ; l'exposition réseau passe par les mécanismes Minikube, pas par une configuration de production.

## 2. Sauvegarde préalable

Fiche simple : [sauvegarder l'existant avant Minikube](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Minikube/Fiche_Simple_-_VM_Debian_13_Minikube_Sauvegarde_Prealable.md).

Minikube peut recréer son état, mais il faut protéger l'existant :

```bash
docker ps -a --format '{{.Names}}\t{{.Image}}' > ~/docker-avant-minikube.txt
cp -a ~/.kube ~/.kube.bak.$(date +%F) 2>/dev/null || true
```

Exporter les manifests utiles d'un cluster précédent avant de le supprimer.

## 3. Installer Minikube

Fiche simple : [installer Minikube](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Minikube/Fiche_Simple_-_VM_Debian_13_Minikube_Installer.md).

Le paquet officiel Debian est téléchargé depuis le stockage du projet. Pour une installation contrôlée, télécharger, vérifier la provenance (page de versions GitHub) et épingler la version retenue plutôt que d'employer aveuglément la dernière.

```bash
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube_latest_amd64.deb
sudo dpkg -i minikube_latest_amd64.deb
minikube version
```

Sur arm64 utiliser le fichier `minikube_latest_arm64.deb` indiqué par la page officielle. `kubectl` peut être installé séparément ou appelé via `minikube kubectl --`.

## 4. Démarrer le cluster

Fiche simple : [démarrer le cluster Minikube](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Minikube/Fiche_Simple_-_VM_Debian_13_Minikube_Demarrer.md).

```bash
minikube start --driver=docker --cpus=<n> --memory=<mo>
```

Pour fixer la version de Kubernetes, ajouter `--kubernetes-version=<version>` après avoir contrôlé les versions acceptées par votre version de Minikube (`minikube start --help`). Pour garder Docker comme driver par défaut : `minikube config set driver docker`. Utiliser `--profile <nom>` pour isoler plusieurs environnements.

## 5. Validation

Fiche simple : [valider le cluster Minikube](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Minikube/Fiche_Simple_-_VM_Debian_13_Minikube_Valider.md).

```bash
minikube status
minikube kubectl -- get nodes -o wide
minikube kubectl -- get pods -A
minikube kubectl -- create deployment test-nginx --image=<registre>/<image>:<version>
minikube kubectl -- rollout status deployment/test-nginx
minikube kubectl -- delete deployment test-nginx
```

Le nœud doit être `Ready` et les pods système en `Running`. En cas d'échec, relancer avec `--alsologtostderr -v=1` (option de diagnostic documentée) et consulter `minikube logs`.

## 6. Add-ons et exposition

Fiche simple : [gérer les add-ons et l'exposition](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Minikube/Fiche_Simple_-_VM_Debian_13_Minikube_Addons.md).

```bash
minikube addons list
minikube addons enable <addon>
```

N'activer que les add-ons nécessaires. Les add-ons `ingress` et `ingress-dns` ne sont supportés qu'en Linux avec le driver Docker selon la documentation du driver. Ne pas publier l'API ou les services de laboratoire sur un réseau non maîtrisé ; pour accéder à un service : `minikube service <nom> --url`.

## 7. Retour arrière, arrêt et suppression

Fiche simple : [retour arrière, arrêt et suppression](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Minikube/Fiche_Simple_-_VM_Debian_13_Minikube_Retour_Arriere.md).

```bash
minikube stop
minikube delete --profile <nom>
```

`minikube stop` conserve l'état ; `minikube delete` supprime le cluster et ses données, donc exporter d'abord les manifests et données utiles. Pour revenir en arrière après une mise à jour de Minikube, réinstaller le `.deb` de la version précédente conservé, puis recréer le profil si nécessaire. Restaurer `~/.kube` depuis la sauvegarde de la section 2 si le contexte `kubectl` a été modifié.

## Sources

- [Minikube — Get Started](https://minikube.sigs.k8s.io/docs/start/)
- [Minikube — Driver Docker](https://minikube.sigs.k8s.io/docs/drivers/docker/)
- [Docker — Installer Docker Engine sur Debian](https://docs.docker.com/engine/install/debian/)
