# Fiche_Simple_-_VM_Rocky_9_Zeek_Installer

- **Environnement** : VM Rocky Linux 9 dédiée à Zeek
- **OS / Version** : Rocky Linux 9 (compatible RHEL 9); version des paquets à vérifier sur l’hôte
- **Catégorie** : Zeek / installation

---

## Problème précis à résoudre

Installer Zeek 8.0 LTS sur VM Rocky Linux 9.

## 1. Hors-Production (Lab / Test / POC)

1. Installer Podman et vérifier la version :
   ```bash
   sudo dnf install podman
   podman --version
   ```
   👉 Explication : Podman est le moteur de conteneurs de Rocky; aucun daemon root requis.

2. Télécharger l’image LTS officielle :
   ```bash
   sudo podman pull docker.io/zeek/zeek:lts
   sudo podman image inspect docker.io/zeek/zeek:lts --format "{{.Id}} {{.Digest}}"
   ```
   👉 Explication : Le tag `lts` est documenté par l’éditeur; relever le digest pour figer la version déployée. Vérifier la ligne publiée.

3. Contrôler Zeek dans le conteneur :
   ```bash
   sudo podman run --rm docker.io/zeek/zeek:lts zeek --version
   sudo podman run --rm docker.io/zeek/zeek:lts zeek -N Zeek::AF_Packet
   ```
   👉 Explication : Confirme la version et la présence du plugin AF_PACKET.

## 2. Production — Contrôles

Figer la ligne LTS (ne pas utiliser la ligne roulante en production) et consigner la source.

## 3. Production — Sécurité

- Vérifier l’origine du paquet ou de l’image avant installation.
- Pas de secret dans les dépôts ou les variables.

## Validation et retour arrière

- **Validation** : La commande `zeek --version` affiche la version 8.0.x attendue.
- **Retour arrière** : Supprimer l’image : `sudo podman rmi docker.io/zeek/zeek:lts`.

## Si le problème n’est pas résolu

- [Zeek — documentation officielle](https://docs.zeek.org/en/master/install.html)
- [Fiche d’entrée du logiciel](/01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-zeek)
- [Étape suivante du guide](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/zeek/fiche-simple-vm-rocky-9-zeek-configurer)
- [Étape précédente du guide](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/zeek/fiche-simple-vm-rocky-9-zeek-prerequis-limites)