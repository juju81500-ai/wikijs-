# Fiche_Simple_-_VM_Debian_13_Minikube_Retour_Arriere.md

- **Environnement** : VM Debian 13 de laboratoire avec Docker Engine, Minikube mono-nœud
- **OS / Version** : Debian 13 Trixie; Minikube (driver Docker)
- **Catégorie** : conteneurs / Kubernetes de laboratoire
- **Tags** : `debian13`, `minikube`, `docker`, `kubernetes`, `lab`

---

## Problème précis à résoudre

Arrêter ou supprimer le cluster et restaurer l'état précédent sans perte involontaire.

## 1. Hors-Production (Lab / Test / POC)

1. Arrêter en conservant l'état :
   ```bash
   minikube stop
   ```
   👉 Explication : l'état du cluster est conservé.

2. Exporter les manifests et données utiles puis supprimer le profil (`lab1` est un nom d'exemple) :
   ```bash
   minikube delete --profile lab1
   ```
   👉 Explication : supprime le cluster et ses données : à faire seulement après export.

3. Restaurer la configuration kubectl depuis la sauvegarde (remplacer la date par celle de votre sauvegarde) :
   ```bash
   cp -a ~/.kube.bak.2026-01-01/. ~/.kube/
   ```
   👉 Explication : rétablit le contexte `kubectl` modifié par Minikube.

4. Revenir à une version précédente : réinstaller le `.deb` conservé puis recréer le profil si nécessaire :
   ```bash
   sudo dpkg -i minikube_ancienne_version_amd64.deb
   ```
   👉 Explication : le nom de fichier est un exemple à remplacer par celui conservé.

## 2. Production — Contrôles

Valider avec le responsable la suppression des données du cluster.

## 3. Production — Sécurité

- `minikube delete` est irréversible : exporter avant.

## Validation et retour arrière

- **Validation** : `minikube status` confirme l'arrêt ou l'absence du profil; `kubectl` pointe vers le bon contexte.
- **Retour arrière** : Recréer le profil avec `minikube start` et réappliquer les manifests exportés.

## Si le problème n'est pas résolu

- [Minikube — Get Started](https://minikube.sigs.k8s.io/docs/start/)
- [Guide complet Minikube Docker Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/88_Deploiement_Minikube_Docker_Driver_Debian_13.md#7-retour-arriere-arret-et-suppression)
