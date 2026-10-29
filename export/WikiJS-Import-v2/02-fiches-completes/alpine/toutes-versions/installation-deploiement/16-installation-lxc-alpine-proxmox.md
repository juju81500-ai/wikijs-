---
title: "Créer et installer un LXC Alpine sur Proxmox"
description: "Fiche simple : [cadrer l'architecture](../../../../01-Fiches-Simples/Alpine/Toutes-versions/Vie-du-systeme/Fiches-par-theme/Administration-systeme/FicheSimple-LXCAlpineProxmoxCadrerArchitecture.md)."
published: true
date: 2026-10-29T20:14:10Z
tags: ["alpine", "proxmox", "lxc", "installation", "template", "production"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Créer et installer un LXC Alpine sur Proxmox

- **Type de fiche** : Installation / Déploiement
- **Environnement** : Cluster ou nœud Proxmox VE
- **OS / Version** : Alpine Linux, template maintenu disponible dans Proxmox
- **Rôle** : Créer un conteneur léger prêt à recevoir un service
- **Tags** : `alpine`, `proxmox`, `lxc`, `installation`, `template`, `production`

## 1. Objectif et architecture

Fiche simple : [cadrer l'architecture](/01-fiches-simples/alpine/toutes-versions/vie-du-systeme/fiches-par-theme/administration-systeme/fiche-simple-lxc-alpine-proxmox-cadrer-architecture).

Créer un conteneur Alpine non privilégié, isolé sur le bridge/VLAN prévu, avec ressources, stockage, adresse et politique de sauvegarde cohérents avec son rôle. Un LXC partage le noyau de l'hôte; le noyau et une partie du filtrage restent sous responsabilité Proxmox.

## 2. Prérequis

Fiche simple : [vérifier les prérequis](/01-fiches-simples/alpine/toutes-versions/vie-du-systeme/fiches-par-theme/administration-systeme/fiche-simple-lxc-alpine-proxmox-verifier-prerequis).

- Nœud et stockage Proxmox opérationnels; accès administrateur et console de secours.
- Template Alpine maintenu et compatible avec la version de Proxmox. Ne pas utiliser Alpine 3.19 pour un nouveau service de production.
- ID CT libre, hostname, plan IP/DNS, bridge/VLAN, quota CPU/RAM/disque et sauvegarde définis.
- Réseau, points de montage, capacités et nesting justifiés par le service; éviter le CT privilégié.

## 3. Télécharger et créer le conteneur

Fiche simple : [télécharger le template et créer le CT](/01-fiches-simples/alpine/toutes-versions/vie-du-systeme/fiches-par-theme/administration-systeme/fiche-simple-lxc-alpine-proxmox-telecharger-creer).

Sur le nœud Proxmox, mettre à jour le catalogue et sélectionner une branche maintenue :

```bash
pveam update
pveam available | grep -i alpine
```

Télécharger le template choisi vers le stockage de templates du nœud :

```bash
pveam download <STOCKAGE_TEMPLATE> <NOM_TEMPLATE_ALPINE>
```

Dans l'interface Proxmox :

1. Cliquer **Créer CT** et saisir ID unique, hostname et compte initial.
2. Sélectionner le template Alpine téléchargé.
3. Définir stockage, taille disque, CPU et mémoire selon la charge prévue.
4. Activer **Unprivileged container**.
5. Choisir bridge, VLAN tag, adresse DHCP ou réservation statique, passerelle et DNS.
6. Laisser désactivés nesting, FUSE et périphériques hôte sauf besoin documenté.
7. Vérifier le résumé et créer le CT.

## 4. Premier démarrage et configuration

Fiche simple : [configurer le premier démarrage](/01-fiches-simples/alpine/toutes-versions/vie-du-systeme/fiches-par-theme/administration-systeme/fiche-simple-lxc-alpine-proxmox-premier-demarrage).

Démarrer depuis Proxmox et contrôler dans la console du CT :

```sh
cat /etc/alpine-release
ip -br addr
ip route
cat /etc/resolv.conf
rc-status
```

Mettre à jour la liste des paquets et appliquer les correctifs selon la politique du site :

```sh
apk update
apk upgrade
```

Créer un compte nominatif non-root, configurer `doas`, puis installer seulement les paquets liés au rôle. Configurer les services avec OpenRC et utiliser les fiches simples Alpine pour SSH, réseau, DNS et services.

## 5. Sécuriser et exposer le service

Fiche simple : [sécuriser l'exposition du service](/01-fiches-simples/alpine/toutes-versions/vie-du-systeme/fiches-par-theme/administration-systeme/fiche-simple-lxc-alpine-proxmox-securiser-exposition).

- Filtrer au niveau du firewall Proxmox/routeur ou du composant retenu par l'architecture; ne pas supposer qu'un LXC non privilégié peut charger ses propres règles noyau.
- N'ouvrir que les ports et sources nécessaires.
- Protéger les secrets, désactiver les services inutilisés et vérifier les capacités du conteneur.
- Documenter l'adresse et le rôle dans le DNS, la supervision et l'inventaire.

## 6. Vérification et mise en production

Fiche simple : [valider la mise en production](/01-fiches-simples/alpine/toutes-versions/vie-du-systeme/fiches-par-theme/administration-systeme/fiche-simple-lxc-alpine-proxmox-valider-mise-production).

Depuis le CT, vérifier version, paquets, services OpenRC, adresse, route, DNS et ports d'écoute. Depuis un client autorisé, tester le parcours applicatif; depuis une source non autorisée, vérifier le refus attendu.

Créer une tâche de sauvegarde vers PBS ou une cible indépendante, puis réaliser une restauration vers un ID temporaire et un réseau isolé.

## 7. Retour arrière et dépannage

Fiche simple : [préparer le retour arrière et diagnostiquer](/01-fiches-simples/alpine/toutes-versions/vie-du-systeme/fiches-par-theme/diagnostic/fiche-simple-lxc-alpine-proxmox-retour-arriere-diagnostic).

En cas de perte réseau, corriger bridge/VLAN/IP depuis la console Proxmox. Si le service ne démarre pas, consulter `rc-status` et les journaux du CT. Pour annuler le déploiement, arrêter le CT et ne supprimer son stockage qu'après vérification de l'ID, des sauvegardes et des données à conserver.

## Sources

- [Proxmox VE — Documentation](https://pve.proxmox.com/pve-docs/)
- [Alpine Linux — Documentation](https://docs.alpinelinux.org/)