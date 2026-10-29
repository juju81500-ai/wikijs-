# Fiche simple — Cadrer un pilote Packer sur Debian 13

- **Environnement** : VM Debian 13 de laboratoire, démon Docker local isolé
- **OS / Version** : Debian 13 Trixie; HashiCorp Packer
- **Catégorie** : automatisation / construction d'images

---

## Problème précis à résoudre

Confirmer que le pilote Packer est autorisé, isolé et limité à une image Docker non sensible.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier Debian et Docker :
   ```bash
   grep PRETTY_NAME /etc/os-release
   docker version --format '{{.Server.Version}}'
   docker info | head -5
   ```
   👉 Explication : Docker est installé et administré séparément; le pilote n'utilise que le constructeur Docker local.

2. Vérifier l'accès au socket Docker :
   ```bash
   id -nG | tr ' ' '\n' | grep -x docker
   ```
   👉 Explication : appartenir au groupe `docker` équivaut à des droits root sur la machine; l'autorisation doit être explicite.

3. Vérifier l'espace disque :
   ```bash
   df -h /var/lib/docker
   ```
   👉 Explication : les images de base et construites consomment de l'espace.

4. Consigner le périmètre : aucune image de VM de production, aucun compte cloud, aucun registre autre que de test.
   👉 Explication : toute extension est une autre procédure approuvée.

## 2. Production — Contrôles

Pour une chaîne d’images de production, approuver le builder, les images de base immuables, les plugins verrouillés, les provisioners, le contrôle des secrets, les scans, la traçabilité et les approbations avant publication. Le pilote Docker local ne constitue pas une chaîne de production.

## 3. Production — Sécurité

- L’accès au socket Docker équivaut généralement à des privilèges root; réserver le pilote aux opérateurs autorisés.
- Ne jamais intégrer de secret dans HCL, les variables commitées, les journaux ou les couches d’image.
- Ne pas publier l’image vers un registre ni exécuter de build sur un démon partagé sans approbation.
- Verrouiller et réviser les plugins et sources; rejeter tout artefact dont la provenance ou le contenu est incertain.

## Validation et retour arrière

- **Validation** : périmètre, cible, approbateur et critères d'arrêt consignés.
- **Arrêt** : ne pas lancer Packer si l'accès au démon ou au registre n'est pas explicitement autorisé.

## Si le problème n'est pas résolu

- [HashiCorp — concepts Packer](https://developer.hashicorp.com/packer/docs)
- [Guide complet Packer Debian 13](/02-fiches-completes/debian/13/installation-deploiement/126-administration-packer-debian-13#1-cadrer-le-pilote-et-les-acces-necessaires)