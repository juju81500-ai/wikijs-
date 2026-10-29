---
title: "Fiche Simple - VM Linux Keepalived HAProxy Installer Valider HAProxy"
description: "Installer HAProxy et valider sa configuration avant activation."
published: true
date: 2026-10-29T19:45:07Z
tags: ["ha", "keepalived", "vrrp", "haproxy", "linux"]
editor: markdown
dateCreated: 2026-10-29T19:45:07Z
dateModified: 2026-10-29T19:45:07Z
---

# Fiche_Simple_-_VM_Linux_Keepalived_HAProxy_Installer_Valider_HAProxy.md

- **Environnement** : Deux nœuds Linux sur le même segment L2, serveurs applicatifs redondés
- **OS / Version** : Linux (Debian/Ubuntu); HAProxy et Keepalived des dépôts de la distribution
- **Catégorie** : haute disponibilité / réseau
- **Tags** : `ha`, `keepalived`, `vrrp`, `haproxy`, `linux`

---

## Problème précis à résoudre

Installer HAProxy et valider sa configuration avant activation.

## 1. Hors-Production (Lab / Test / POC)

1. Installer HAProxy depuis le dépôt de la distribution :
   ```bash
   sudo apt update
   sudo apt install haproxy
   ```
   👉 Explication : version maintenue par la distribution.

2. Éditer `/etc/haproxy/haproxy.cfg` : frontend sur l'adresse prévue, backends explicites et sonde sur un endpoint de santé réel.
   👉 Explication : limite la configuration au nécessaire.

3. Valider la syntaxe :
   ```bash
   sudo haproxy -c -f /etc/haproxy/haproxy.cfg
   ```
   👉 Explication : doit indiquer que la configuration est valide.

4. Activer et démarrer :
   ```bash
   sudo systemctl enable --now haproxy
   ```
   👉 Explication : démarre HAProxy au boot.

5. Contrôler l'état :
   ```bash
   sudo systemctl --no-pager status haproxy
   ```
   👉 Explication : le service doit être actif.

## 2. Production — Contrôles

Restreindre frontend, ports d'administration et métriques aux réseaux nécessaires.

## 3. Production — Sécurité

- Ne pas exposer la page de statistiques sans authentification et filtrage.

## Validation et retour arrière

- **Validation** : la configuration est valide et HAProxy répond sur le frontend.
- **Retour arrière** : restaurer la copie précédente de `haproxy.cfg` puis `sudo systemctl reload haproxy`.

## Si le problème n'est pas résolu

- [HAProxy — documentation](https://docs.haproxy.org/)
- [Keepalived — documentation](https://keepalived.readthedocs.io/en/latest/)
- [Guide complet](/02-fiches-completes/transverses/multi-os/autres/08-haute-disponibilite-keepalived-vrrp-haproxy#2-installer-et-valider-haproxy)