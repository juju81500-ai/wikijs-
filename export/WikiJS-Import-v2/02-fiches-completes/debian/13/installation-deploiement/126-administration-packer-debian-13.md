---
title: "Administrer HashiCorp Packer sur Debian 13"
description: "Fiche simple de cette étape : [cadrer le pilote Packer](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Packer/FicheSimple-PackerDebian13CadrerPilote.md)."
published: true
date: 2026-10-29T20:14:10Z
tags: ["packer", "hashicorp", "debian13", "hcl2", "docker", "image-builder"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Administrer HashiCorp Packer sur Debian 13

- **OS / Version** : Debian 13 Trixie; HashiCorp Packer installé depuis le dépôt APT officiel
- **Type de fiche** : Installation / automatisation d'images
- **Périmètre** : installation CLI, template HCL2 local, initialisation du plugin Docker, validation et construction d'une image pilote locale
- **Catégorie** : automatisation / image as code
- **Tags** : `packer`, `hashicorp`, `debian13`, `hcl2`, `docker`, `image-builder`

## 1. Cadrer le pilote et les accès nécessaires

Fiche simple de cette étape : [cadrer le pilote Packer](/01-fiches-simples/debian/13/vie-du-logiciel/packer/fiche-simple-packer-debian-13-cadrer-pilote).

Packer automatise la création d'images via des plugins de constructeurs. Cette fiche teste le constructeur Docker local sur un poste/VM de laboratoire; elle ne crée pas d'image de VM de production, de compte cloud ni de golden image Windows.

Prérequis : Debian 13 approuvé, accès Internet via dépôts autorisés, Docker installé et administré séparément, permission explicite d'utiliser le socket Docker et un registre de test. L'appartenance au groupe `docker` équivaut généralement à des privilèges root sur l'hôte; ne l'accorder qu'aux opérateurs approuvés. Utiliser uniquement des images de base et contenus non sensibles.

## 2. Installer Packer depuis le dépôt officiel

Fiche simple de cette étape : [installer Packer depuis le dépôt HashiCorp](/01-fiches-simples/debian/13/vie-du-logiciel/packer/fiche-simple-packer-debian-13-installer).

Télécharger la clé APT depuis HashiCorp, vérifier son empreinte avec la référence actuelle de la documentation officielle, puis configurer le dépôt `signed-by` correspondant à Debian 13. Installer `packer` selon la procédure de l'éditeur :

```bash
cd /tmp
curl --fail --silent --show-error --location \
  https://apt.releases.hashicorp.com/gpg -o hashicorp-archive-keyring.asc
gpg --show-keys --with-fingerprint ./hashicorp-archive-keyring.asc
```

Comparer l'empreinte affichée à la documentation officielle HashiCorp. Si elle correspond, installer la clé et configurer le dépôt :

```bash
gpg --dearmor < ./hashicorp-archive-keyring.asc \
  | sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg >/dev/null
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com trixie main" \
  | sudo tee /etc/apt/sources.list.d/hashicorp.list
sudo apt update
apt-cache policy packer
sudo apt install packer
packer version
```

Valider la provenance du paquet, enregistrer la version et maîtriser les mises à jour selon le processus de l'organisation. Ne pas importer de clé sans vérification, désactiver APT Secure ni utiliser un binaire issu d'un miroir inconnu.

## 3. Préparer un template HCL2 de laboratoire

Fiche simple de cette étape : [préparer un template Packer HCL2](/01-fiches-simples/debian/13/vie-du-logiciel/packer/fiche-simple-packer-debian-13-preparer-template).

Créer un répertoire isolé et un fichier `docker.pkr.hcl`. Exemple minimal de laboratoire :

```hcl
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
```

L'exemple utilise un tag Debian mobile uniquement pour un pilote jetable. Pour une chaîne reproductible ou de production, sélectionner une image approuvée et fixer son digest, maîtriser la version du plugin, documenter les paquets et sources, et revoir chaque provisioner. Ne mettre dans HCL ni mot de passe, token, clé privée ni donnée personnelle.

## 4. Initialiser et valider le template sans construire

Fiche simple de cette étape : [initialiser et valider un template Packer](/01-fiches-simples/debian/13/vie-du-logiciel/packer/fiche-simple-packer-debian-13-valider-template).

Depuis le répertoire du template :

```bash
packer init .
packer fmt -check .
packer validate .
```

`packer init` télécharge le plugin déclaré. Examiner le fichier `.packer.lock.hcl` créé et le conserver avec le template afin de contrôler les versions et empreintes des plugins. `packer validate` vérifie la configuration, mais ne prouve ni disponibilité des sources, ni qualité, ni sécurité de l'image produite.

En cas d'erreur, ne pas lancer de build; corriger HCL, versions et dépendances, puis répéter les contrôles.

## 5. Construire l'image Docker de laboratoire

Fiche simple de cette étape : [construire une image Packer locale](/01-fiches-simples/debian/13/vie-du-logiciel/packer/fiche-simple-packer-debian-13-build-local).

Vérifier Docker, l'espace disque et la cible locale avant toute construction :

```bash
docker info
docker image ls
packer build .
```

Cette commande utilise le démon Docker défini pour l'utilisateur courant et peut télécharger une image de base puis créer une image locale. Ne pas la lancer sur une machine ou un démon partagé sans autorisation. Ne pas utiliser `sudo packer build` pour contourner une permission : résoudre le contrôle d'accès selon la procédure approuvée.

Un échec de provisionnement doit conduire à examiner les journaux et l'image intermédiaire; ne pas relancer en boucle ni publier une image partiellement vérifiée.

## 6. Inspecter et promouvoir l'artefact

Fiche simple de cette étape : [inspecter et promouvoir un artefact Packer](/01-fiches-simples/debian/13/vie-du-logiciel/packer/fiche-simple-packer-debian-13-inspecter-artefact).

Identifier le résultat par son nom/ID, vérifier la présence du marqueur de test et inspecter les métadonnées :

```bash
docker image ls
docker image inspect <ID_IMAGE_AFFICHE_PAR_PACKER>
docker run --rm --entrypoint cat <ID_IMAGE_AFFICHE_PAR_PACKER> /etc/packer-pilot
```

Remplacer les placeholders par l'identifiant exact copié de la sortie Packer. Ne pas considérer la réussite de `packer build` comme une approbation. Vérifier le contenu, les paquets, l'utilisateur par défaut, les ports, les secrets résiduels, les vulnérabilités via les outils approuvés et la traçabilité du build. Une publication vers un registre nécessite un projet, des droits, une politique de signature et une revue distincts; non couverts ici.

## 7. Nettoyer et revenir à l'état initial

Fiche simple de cette étape : [nettoyer le pilote et préparer le retour arrière](/01-fiches-simples/debian/13/vie-du-logiciel/packer/fiche-simple-packer-debian-13-nettoyer-retour-arriere).

Conserver le template, le lock file, la version de Packer, les journaux utiles et le résultat approuvé. Supprimer l'image de pilote uniquement après confirmation qu'elle n'est utilisée par aucun conteneur :

```bash
docker ps -a --filter ancestor="$IMAGE_ID"
docker image rm "$IMAGE_ID"
```

Remplacer `IMAGE_ID` par l'identifiant exact copié de la sortie de Packer. Ne pas employer de suppression globale ou de prune sur un démon partagé. Pour revenir en arrière après une mise à niveau, restaurer le template, le lock file et la version de Packer du pilote, reconstruire une image temporaire et la valider avant toute promotion.

## Sources

- [HashiCorp — installation Packer](https://developer.hashicorp.com/packer/install)
- [HashiCorp — référence des blocs HCL2](https://developer.hashicorp.com/packer/docs/templates/hcl_templates/blocks)
- [HashiCorp — installer les plugins](https://developer.hashicorp.com/packer/docs/plugins/install)
- [HashiCorp — commande validate](https://developer.hashicorp.com/packer/docs/commands/validate)
- [HashiCorp — commande build](https://developer.hashicorp.com/packer/docs/commands/build)
- [HashiCorp — tutoriel construire une image Docker](https://developer.hashicorp.com/packer/tutorials/docker-get-started/docker-get-started-build-image)

Le guide ne publie aucune image et ne modifie aucun registre. Tester les sources, les plugins, le nettoyage et les politiques de promotion dans un environnement isolé avant usage opérationnel.