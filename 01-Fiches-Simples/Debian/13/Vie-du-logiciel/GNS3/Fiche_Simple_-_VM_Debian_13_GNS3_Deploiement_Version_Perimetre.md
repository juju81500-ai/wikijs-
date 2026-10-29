# Fiche_Simple_-_VM_Debian_13_GNS3_Deploiement_Version_Perimetre.md

- **Environnement** : Poste Debian 13 amd64 graphique avec virtualisation CPU
- **OS / Version** : Debian 13 Trixie amd64; GNS3 2.2.61 stable
- **Catégorie** : simulation reseau / cadrage
- **Tags** : `gns3`, `debian13`, `cadrage`, `lab`

---

## Problème précis à résoudre

Choisir la version stable et définir le périmètre d'un laboratoire isolé.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler l'architecture :
   ```bash
   dpkg --print-architecture
   ```
   👉 Explication : elle doit afficher `amd64`.

2. Vérifier que la virtualisation CPU est visible :
   ```bash
   grep -Ec '(vmx|svm)' /proc/cpuinfo
   ```
   👉 Explication : un résultat supérieur à 0 indique que VT-x/AMD-V est activé; sur VM, la virtualisation imbriquée doit être autorisée par l'hyperviseur.

3. Retenir GNS3 2.2.61 stable; la branche 3.1 alpha n'est pas utilisée.
   👉 Explication : GNS3 n'est pas un paquet APT Debian natif; l'installation se fait par `pipx`.

## 2. Production — Contrôles

Définir ressources (CPU, Go de RAM, disque), propriétaires des images et licences.

## 3. Production — Sécurité

- Aucun lien Cloud, NAT externe ni pont vers une carte physique.
- Images propriétaires uniquement depuis l'éditeur, selon leur licence.

## Validation et retour arrière

- **Validation** : Architecture, virtualisation et version cible confirmées.
- **Retour arrière** : Aucune modification n'a été faite à cette étape.

## Si le problème n'est pas résolu

- [GNS3 — téléchargement](https://www.gns3.com/software/download)
- [GNS3 — installation Linux](https://docs.gns3.com/docs/getting-started/installation/linux)
- [Guide complet GNS3 Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/77_Deploiement_GNS3_2.2.61_Debian_13.md#1-version-et-perimetre)
