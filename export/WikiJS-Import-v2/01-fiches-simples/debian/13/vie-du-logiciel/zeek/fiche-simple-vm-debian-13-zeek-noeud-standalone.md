---
title: "Fiche Simple - VM Debian 13 Zeek Noeud Standalone"
description: "Configurer un nœud ZeekControl standalone sur l'interface miroir et les réseaux locaux autorisés."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "zeek", "zeekctl", "af-packet", "network-monitoring"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_Zeek_Noeud_Standalone.md

- **Environnement** : VM Debian 13 capteur passif Zeek standalone sur interface miroir approuvée
- **OS / Version** : Debian 13 Trixie; Zeek 8.0 LTS (dépôt OBS officiel)
- **Catégorie** : supervision / analyse passive du trafic
- **Tags** : `debian13`, `zeek`, `zeekctl`, `af-packet`, `network-monitoring`

---

## Problème précis à résoudre

Configurer un nœud ZeekControl standalone sur l'interface miroir et les réseaux locaux autorisés.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder les configurations :
   ```bash
   sudo cp -a /opt/zeek/etc/node.cfg /opt/zeek/etc/node.cfg.pre-lab
   sudo cp -a /opt/zeek/etc/networks.cfg /opt/zeek/etc/networks.cfg.pre-lab
   ```
   👉 Explication : permet le retour arrière.

2. Éditer `/opt/zeek/etc/node.cfg` : un seul nœud standalone, interface remplacée par l'interface miroir réelle (`enp2s0` est un exemple) :
   ```bash
   [zeek]
   type=standalone
   host=localhost
   interface=enp2s0
   ```
   👉 Explication : définit la capture sur la bonne interface.

3. Éditer `/opt/zeek/etc/networks.cfg` : remplacer les sous-réseaux privés par les CIDR réellement suivis.
   👉 Explication : Zeek s'en sert pour distinguer l'espace local; n'ajouter aucun réseau hors périmètre.

4. Dans `/opt/zeek/etc/zeekctl.cfg`, régler le contact opérationnel et la rétention des logs selon la politique de stockage.
   👉 Explication : évite le remplissage du disque.

## 2. Production — Contrôles

Revue de `node.cfg` et `networks.cfg` par un second administrateur.

## 3. Production — Sécurité

- Ne pas activer l'extraction de fichiers ni des scripts locaux non relus.
- Les logs contiennent des noms d'hôtes, adresses et métadonnées : restreindre leur accès.

## Validation et retour arrière

- **Validation** : Les trois fichiers sont cohérents avec le périmètre approuvé.
- **Retour arrière** : Restaurer : `sudo cp -a /opt/zeek/etc/node.cfg.pre-lab /opt/zeek/etc/node.cfg` (idem `networks.cfg`).

## Si le problème n'est pas résolu

- [Zeek — installation](https://docs.zeek.org/en/stable/install.html)
- [ZeekControl](https://github.com/zeek/zeekctl)
- [Guide complet Zeek 8 LTS Debian 13](/02-fiches-completes/debian/13/installation-deploiement/72-deploiement-zeek-8-lts-debian-13#4-configurer-un-nud-standalone)