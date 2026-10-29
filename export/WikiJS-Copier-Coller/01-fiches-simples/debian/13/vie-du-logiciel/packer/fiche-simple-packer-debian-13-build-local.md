# Fiche simple — Construire une image Packer locale

- **Environnement** : démon Docker de laboratoire dédié, autorisation opérateur vérifiée
- **OS / Version** : Debian 13; Packer avec plugin Docker
- **Catégorie** : automatisation / construction d'image

---

## Problème précis à résoudre

Construire une seule image locale à partir d'un template validé, sans publication vers un registre.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier Docker, les images existantes et l'espace :
   ```bash
   docker info | head -5
   docker image ls
   df -h /var/lib/docker
   ```
   👉 Explication : on s'assure de la cible locale avant toute construction.

2. Construire, avec l'utilisateur courant (jamais `sudo packer build`) :
   ```bash
   cd ~/packer-lab
   PACKER_LOG=0 packer build . 2>&1 | tee build.log
   ```
   👉 Explication : peut télécharger l'image de base et créer une image locale; ne pas lancer sur un démon partagé sans autorisation.

3. Noter l'identifiant de l'image affiché en fin de sortie :
   ```bash
   grep -i 'Imported Docker image\|Created image' build.log
   ```
   👉 Explication : en cas d'échec de provisionnement, examiner le journal; ne pas relancer en boucle ni publier une image partiellement vérifiée.

## 2. Production — Contrôles

Pour une chaîne d’images de production, approuver le builder, les images de base immuables, les plugins verrouillés, les provisioners, le contrôle des secrets, les scans, la traçabilité et les approbations avant publication. Le pilote Docker local ne constitue pas une chaîne de production.

## 3. Production — Sécurité

- L’accès au socket Docker équivaut généralement à des privilèges root; réserver le pilote aux opérateurs autorisés.
- Ne jamais intégrer de secret dans HCL, les variables commitées, les journaux ou les couches d’image.
- Ne pas publier l’image vers un registre ni exécuter de build sur un démon partagé sans approbation.
- Verrouiller et réviser les plugins et sources; rejeter tout artefact dont la provenance ou le contenu est incertain.

## Validation et retour arrière

- **Validation** : build local réussi, identifiant d'image enregistré et artefact inspecté.
- **Retour arrière** : ne pas relancer en boucle; retirer l'image uniquement après confirmation qu'aucun conteneur ne l'utilise.

## Si le problème n'est pas résolu

- [HashiCorp — commande build](https://developer.hashicorp.com/packer/docs/commands/build)
- [HashiCorp — tutoriel Docker](https://developer.hashicorp.com/packer/tutorials/docker-get-started/docker-get-started-build-image)
- [Guide complet Packer Debian 13](/02-fiches-completes/debian/13/installation-deploiement/126-administration-packer-debian-13#5-construire-limage-docker-de-laboratoire)