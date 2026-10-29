---
title: "Fiche Simple - VM Linux Keepalived HAProxy Preparer Architecture"
description: "Définir IP virtuelle, pairs, interface et backends avant de configurer HA."
published: true
date: 2026-10-29T19:45:07Z
tags: ["ha", "keepalived", "vrrp", "haproxy", "linux"]
editor: markdown
dateCreated: 2026-10-29T19:45:07Z
dateModified: 2026-10-29T19:45:07Z
---

# Fiche_Simple_-_VM_Linux_Keepalived_HAProxy_Preparer_Architecture.md

- **Environnement** : Deux nœuds Linux sur le même segment L2, serveurs applicatifs redondés
- **OS / Version** : Linux (Debian/Ubuntu); HAProxy et Keepalived des dépôts de la distribution
- **Catégorie** : haute disponibilité / réseau
- **Tags** : `ha`, `keepalived`, `vrrp`, `haproxy`, `linux`

---

## Problème précis à résoudre

Définir IP virtuelle, pairs, interface et backends avant de configurer HA.

## 1. Hors-Production (Lab / Test / POC)

1. Noter l'IP virtuelle (libre), les IP fixes des deux pairs, l'interface L2, les backends et les sondes de santé.
   👉 Explication : ces valeurs forment le plan; les adresses d'exemple doivent être remplacées par les vôtres.

2. Sur chaque nœud, vérifier interface et adresse :
   ```bash
   ip -br address
   ip route
   ```
   👉 Explication : confirme que les deux nœuds sont dans le même segment L2.

3. Vérifier que l'IP virtuelle (remplacer 192.0.2.10 par la vôtre) est libre :
   ```bash
   ping -c 2 192.0.2.10
   ```
   👉 Explication : aucune réponse attendue avant activation.

4. Vérifier avec le réseau/hyperviseur que VRRP (multicast ou unicast choisi) est autorisé entre les nœuds.
   👉 Explication : le commutateur ou l'hyperviseur peut le bloquer.

5. Retenir : une seule IP virtuelle ne remplace pas la redondance des backends, du stockage ni de la base.
   👉 Explication : évite de croire à une HA complète.

## 2. Production — Contrôles

Valider le plan avec les équipes réseau et système.

## 3. Production — Sécurité

- Réserver l'IP virtuelle pour éviter les conflits.

## Validation et retour arrière

- **Validation** : plan documenté, IP virtuelle libre, VRRP autorisé.
- **Retour arrière** : aucune modification n'est faite par cette fiche; rien à annuler.

## Si le problème n'est pas résolu

- [HAProxy — documentation](https://docs.haproxy.org/)
- [Keepalived — documentation](https://keepalived.readthedocs.io/en/latest/)
- [Guide complet](/02-fiches-completes/transverses/multi-os/autres/08-haute-disponibilite-keepalived-vrrp-haproxy#1-preparer-larchitecture)