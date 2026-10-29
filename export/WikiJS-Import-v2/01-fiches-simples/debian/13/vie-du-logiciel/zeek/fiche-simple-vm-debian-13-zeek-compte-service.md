---
title: "Fiche Simple - VM Debian 13 Zeek Compte Service"
description: "Faire tourner Zeek sans root avec un compte dédié et des capacités de capture minimales."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "zeek", "zeekctl", "af-packet", "network-monitoring"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_Zeek_Compte_Service.md

- **Environnement** : VM Debian 13 capteur passif Zeek standalone sur interface miroir approuvée
- **OS / Version** : Debian 13 Trixie; Zeek 8.0 LTS (dépôt OBS officiel)
- **Catégorie** : supervision / analyse passive du trafic
- **Tags** : `debian13`, `zeek`, `zeekctl`, `af-packet`, `network-monitoring`

---

## Problème précis à résoudre

Faire tourner Zeek sans root avec un compte dédié et des capacités de capture minimales.

## 1. Hors-Production (Lab / Test / POC)

1. Créer le compte système et ses répertoires :
   ```bash
   sudo adduser --system --group --home /opt/zeek zeek
   sudo install -d -o zeek -g zeek -m 0750 /opt/zeek/logs /opt/zeek/spool
   ```
   👉 Explication : le compte `zeek` écrit seulement dans `logs` et `spool`.

2. Donner au binaire les capacités nécessaires à AF_PACKET et les vérifier :
   ```bash
   sudo setcap cap_net_raw,cap_net_admin=+eip /opt/zeek/bin/zeek
   getcap /opt/zeek/bin/zeek
   ```
   👉 Explication : évite de lancer Zeek en root; les capacités peuvent être effacées par une mise à jour, à re-vérifier après chaque mise à niveau.

3. Contrôler l'état de l'interface de capture :
   ```bash
   ip -br address
   ip -d link show
   ```
   👉 Explication : identifier le nom exact de l'interface miroir, son lien et ses adresses.

## 2. Production — Contrôles

Documenter le compte, les chemins réels (adapter si le préfixe diffère de `/opt/zeek`) et la vérification des capacités après chaque mise à jour.

## 3. Production — Sécurité

- Ne pas rendre `/opt/zeek` globalement inscriptible.
- Ne pas basculer le capteur en root comme contournement permanent.

## Validation et retour arrière

- **Validation** : `getcap` affiche les capacités et `zeek` possède `logs` et `spool`.
- **Retour arrière** : `sudo setcap -r /opt/zeek/bin/zeek` puis `sudo deluser zeek` si le compte n'est plus utile.

## Si le problème n'est pas résolu

- [Zeek — installation](https://docs.zeek.org/en/stable/install.html)
- [Guide complet Zeek 8 LTS Debian 13](/02-fiches-completes/debian/13/installation-deploiement/72-deploiement-zeek-8-lts-debian-13#3-creer-un-compte-de-service-et-verifier-linterface)