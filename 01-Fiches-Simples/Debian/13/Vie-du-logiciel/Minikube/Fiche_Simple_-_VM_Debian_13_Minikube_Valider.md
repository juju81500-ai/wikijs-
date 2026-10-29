# Fiche_Simple_-_VM_Debian_13_Minikube_Valider.md

- **Environnement** : VM Debian 13 de laboratoire avec Docker Engine, Minikube mono-nœud
- **OS / Version** : Debian 13 Trixie; Minikube (driver Docker)
- **Catégorie** : conteneurs / Kubernetes de laboratoire
- **Tags** : `debian13`, `minikube`, `docker`, `kubernetes`, `lab`

---

## Problème précis à résoudre

Vérifier que le nœud et les pods système sont sains avec un déploiement de test.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler l'état et les nœuds :
   ```bash
   minikube status
   minikube kubectl -- get nodes -o wide
   minikube kubectl -- get pods -A
   ```
   👉 Explication : le nœud doit être `Ready` et les pods système `Running`.

2. Créer un déploiement de test (image d'exemple à remplacer par une image autorisée de votre registre) :
   ```bash
   minikube kubectl -- create deployment test-nginx --image=docker.io/library/nginx:1.27
   minikube kubectl -- rollout status deployment/test-nginx
   ```
   👉 Explication : vérifie le téléchargement d'image et l'ordonnancement.

3. Supprimer le test :
   ```bash
   minikube kubectl -- delete deployment test-nginx
   ```
   👉 Explication : laisse le cluster propre.

4. En cas d'échec, relancer en diagnostic :
   ```bash
   minikube start --alsologtostderr -v=1
   minikube logs
   ```
   👉 Explication : les options de diagnostic documentées montrent la cause.

## 2. Production — Contrôles

Consigner le résultat de la recette et la version.

## 3. Production — Sécurité

- Utiliser une image d'un registre approuvé.

## Validation et retour arrière

- **Validation** : Nœud `Ready`, pods système `Running`, déploiement de test réussi.
- **Retour arrière** : Supprimer le déploiement de test.

## Si le problème n'est pas résolu

- [Minikube — Get Started](https://minikube.sigs.k8s.io/docs/start/)
- [Guide complet Minikube Docker Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/88_Deploiement_Minikube_Docker_Driver_Debian_13.md#5-validation)
