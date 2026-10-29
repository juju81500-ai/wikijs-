# Fiche simple — Préparer un template Packer HCL2

- **Environnement** : répertoire de travail isolé et démon Docker local autorisé
- **OS / Version** : Debian 13; HashiCorp Packer
- **Catégorie** : automatisation / template

---

## Problème précis à résoudre

Créer un template HCL2 minimal qui déclare explicitement un plugin et une source de construction de laboratoire.

## 1. Hors-Production (Lab / Test / POC)

1. Créer un répertoire isolé :
   ```bash
   mkdir -p ~/packer-lab && cd ~/packer-lab
   ```
   👉 Explication : tout reste dans un répertoire jetable.

2. Créer `docker.pkr.hcl` :
   ```bash
   cat > docker.pkr.hcl <<'EOF'
   packer {
     required_plugins {
       docker = {
         source  = "github.com/hashicorp/docker"
         version = ">= 1.0.8"
       }
     }
   }
   source "docker" "debian_pilote" {
     image  = "debian:13-slim"
     commit = true
   }
   build {
     name    = "debian-pilote"
     sources = ["source.docker.debian_pilote"]
     provisioner "shell" {
       inline = ["printf '%s\\n' 'Image Packer de laboratoire' > /etc/packer-pilot"]
     }
   }
   EOF
   ```
   👉 Explication : le tag mobile `debian:13-slim` n'est acceptable que pour un pilote jetable; en production, fixer le digest et la version du plugin.

3. Formater :
   ```bash
   packer fmt .
   ```
   👉 Explication : normalise le style HCL.

## 2. Production — Contrôles

Pour une chaîne d’images de production, approuver le builder, les images de base immuables, les plugins verrouillés, les provisioners, le contrôle des secrets, les scans, la traçabilité et les approbations avant publication. Le pilote Docker local ne constitue pas une chaîne de production.

## 3. Production — Sécurité

- L’accès au socket Docker équivaut généralement à des privilèges root; réserver le pilote aux opérateurs autorisés.
- Ne jamais intégrer de secret dans HCL, les variables commitées, les journaux ou les couches d’image.
- Ne pas publier l’image vers un registre ni exécuter de build sur un démon partagé sans approbation.
- Verrouiller et réviser les plugins et sources; rejeter tout artefact dont la provenance ou le contenu est incertain.

## Validation et retour arrière

- **Validation** : template HCL2 relisible, source et plugins identifiés, absence de secrets vérifiée.
- **Retour arrière** : revenir à une révision versionnée du template; ne pas réutiliser un template inconnu sans revue.

## Si le problème n'est pas résolu

- [HashiCorp — blocs HCL2](https://developer.hashicorp.com/packer/docs/templates/hcl_templates/blocks)
- [HashiCorp — blocs source](https://developer.hashicorp.com/packer/docs/templates/hcl_templates/blocks/source)
- [Guide complet Packer Debian 13](/02-fiches-completes/debian/13/installation-deploiement/126-administration-packer-debian-13#3-preparer-un-template-hcl2-de-laboratoire)