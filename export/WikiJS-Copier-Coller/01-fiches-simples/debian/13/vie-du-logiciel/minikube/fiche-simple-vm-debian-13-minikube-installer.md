# Fiche_Simple_-_VM_Debian_13_Minikube_Installer.md

- **Environnement** : VM Debian 13 de laboratoire avec Docker Engine, Minikube mono-nœud
- **OS / Version** : Debian 13 Trixie; Minikube (driver Docker)
- **Catégorie** : conteneurs / Kubernetes de laboratoire

---

## Problème précis à résoudre

Installer le paquet Debian officiel de Minikube et vérifier sa version.

## 1. Hors-Production (Lab / Test / POC)

1. Télécharger le paquet (vérifier la provenance sur la page de versions GitHub et épingler la version retenue) :
   ```bash
   curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube_latest_amd64.deb
   ```
   👉 Explication : récupère le `.deb` officiel pour amd64; sur arm64 utiliser `minikube_latest_arm64.deb`.

2. Installer le paquet et vérifier :
   ```bash
   sudo dpkg -i minikube_latest_amd64.deb
   minikube version
   ```
   👉 Explication : confirme la version installée; conserver le `.deb` pour un retour arrière.

3. Utiliser `kubectl` via Minikube si non installé :
   ```bash
   minikube kubectl -- version --client
   ```
   👉 Explication : évite d'installer `kubectl` séparément.

## 2. Production — Contrôles

Épingler et documenter la version de Minikube retenue.

## 3. Production — Sécurité

- Ne pas installer aveuglément la dernière version sans vérifier la provenance.

## Validation et retour arrière

- **Validation** : `minikube version` affiche la version attendue.
- **Retour arrière** : `sudo dpkg -r minikube` ou réinstaller le `.deb` de la version précédente.

## Si le problème n'est pas résolu

- [Minikube — Get Started](https://minikube.sigs.k8s.io/docs/start/)
- [Guide complet Minikube Docker Debian 13](/02-fiches-completes/debian/13/installation-deploiement/88-deploiement-minikube-docker-driver-debian-13#3-installer-minikube)