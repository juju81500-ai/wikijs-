# Fiche_Simple_-_VM_Debian_13_Minikube_Addons.md

- **Environnement** : VM Debian 13 de laboratoire avec Docker Engine, Minikube mono-nœud
- **OS / Version** : Debian 13 Trixie; Minikube (driver Docker)
- **Catégorie** : conteneurs / Kubernetes de laboratoire
- **Tags** : `debian13`, `minikube`, `docker`, `kubernetes`, `lab`

---

## Problème précis à résoudre

Activer uniquement les add-ons nécessaires et exposer un service de façon contrôlée.

## 1. Hors-Production (Lab / Test / POC)

1. Lister les add-ons :
   ```bash
   minikube addons list
   ```
   👉 Explication : repère ceux disponibles et leur état.

2. Activer uniquement ce qui est nécessaire (`ingress` est un exemple) :
   ```bash
   minikube addons enable ingress
   ```
   👉 Explication : `ingress` et `ingress-dns` ne sont supportés qu'en Linux avec le driver Docker.

3. Accéder à un service de lab (`mon-service` est un nom d'exemple) :
   ```bash
   minikube service mon-service --url
   ```
   👉 Explication : donne une URL locale sans publier le service sur le réseau.

## 2. Production — Contrôles

Documenter les add-ons activés et leur justification.

## 3. Production — Sécurité

- Ne pas publier l'API ni les services de lab sur un réseau non maîtrisé.
- N'activer que les add-ons nécessaires.

## Validation et retour arrière

- **Validation** : Les add-ons attendus sont `enabled` et le service répond en local.
- **Retour arrière** : `minikube addons disable ingress` (add-on concerné).

## Si le problème n'est pas résolu

- [Minikube — Get Started](https://minikube.sigs.k8s.io/docs/start/)
- [Minikube — driver Docker](https://minikube.sigs.k8s.io/docs/drivers/docker/)
- [Guide complet Minikube Docker Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/88_Deploiement_Minikube_Docker_Driver_Debian_13.md#6-add-ons-et-exposition)
