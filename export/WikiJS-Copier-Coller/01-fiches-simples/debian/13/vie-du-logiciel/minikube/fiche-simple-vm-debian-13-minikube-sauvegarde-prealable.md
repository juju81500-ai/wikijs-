# Fiche_Simple_-_VM_Debian_13_Minikube_Sauvegarde_Prealable.md

- **Environnement** : VM Debian 13 de laboratoire avec Docker Engine, Minikube mono-nœud
- **OS / Version** : Debian 13 Trixie; Minikube (driver Docker)
- **Catégorie** : conteneurs / Kubernetes de laboratoire

---

## Problème précis à résoudre

Conserver l'état Docker et la configuration kubectl existants avant d'installer Minikube.

## 1. Hors-Production (Lab / Test / POC)

1. Lister les conteneurs existants :
   ```bash
   docker ps -a --format '{{.Names}}\t{{.Image}}' > ~/docker-avant-minikube.txt
   ```
   👉 Explication : garde une trace de l'état avant intervention.

2. Copier la configuration kubectl :
   ```bash
   cp -a ~/.kube ~/.kube.bak.$(date +%F) 2>/dev/null || true
   ```
   👉 Explication : permet de restaurer le contexte si Minikube le modifie.

3. Exporter les manifests utiles d'un cluster précédent avant de le supprimer (exemple pour le namespace `default`) :
   ```bash
   kubectl get all -n default -o yaml > ~/manifests-default.yaml
   ```
   👉 Explication : un `minikube delete` ultérieur supprimerait ces ressources.

## 2. Production — Contrôles

Stocker les sauvegardes hors de la VM si elles contiennent des éléments utiles.

## 3. Production — Sécurité

- Les manifests exportés peuvent contenir des données sensibles : protéger les fichiers.
- Ne pas exporter de Secrets vers un emplacement partagé.

## Validation et retour arrière

- **Validation** : Les fichiers de sauvegarde existent et sont lisibles.
- **Retour arrière** : Supprimer les copies créées si elles sont inutiles.

## Si le problème n'est pas résolu

- [Minikube — Get Started](https://minikube.sigs.k8s.io/docs/start/)
- [Guide complet Minikube Docker Debian 13](/02-fiches-completes/debian/13/installation-deploiement/88-deploiement-minikube-docker-driver-debian-13#2-sauvegarde-prealable)