---
title: "Fiche Simple - VM Linux Keepalived HAProxy Tester Basculement"
description: "Vérifier que l'IP virtuelle bascule correctement."
published: true
date: 2026-10-29T19:45:07Z
tags: ["ha", "keepalived", "vrrp", "haproxy", "linux"]
editor: markdown
dateCreated: 2026-10-29T19:45:07Z
dateModified: 2026-10-29T19:45:07Z
---

# Fiche_Simple_-_VM_Linux_Keepalived_HAProxy_Tester_Basculement.md

- **Environnement** : Deux nœuds Linux sur le même segment L2, serveurs applicatifs redondés
- **OS / Version** : Linux (Debian/Ubuntu); HAProxy et Keepalived des dépôts de la distribution
- **Catégorie** : haute disponibilité / réseau
- **Tags** : `ha`, `keepalived`, `vrrp`, `haproxy`, `linux`

---

## Problème précis à résoudre

Vérifier que l'IP virtuelle bascule correctement.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier le service par l'IP virtuelle (remplacer 192.0.2.10 par la vôtre) :
   ```bash
   curl -I http://192.0.2.10/
   ```
   👉 Explication : doit répondre via HAProxy.

2. Simuler l'arrêt de HAProxy sur le nœud actif, en fenêtre contrôlée :
   ```bash
   sudo systemctl stop haproxy
   ```
   👉 Explication : la sonde doit déplacer l'IP vers l'autre nœud.

3. Confirmer le déplacement et lire les journaux :
   ```bash
   ip addr show
   sudo journalctl -u keepalived --since "10 minutes ago"
   ```
   👉 Explication : montre quel nœud porte l'IP et pourquoi.

4. Rétablir HAProxy puis simuler la perte du nœud (arrêt de Keepalived) séparément :
   ```bash
   sudo systemctl start haproxy
   sudo systemctl stop keepalived
   ```
   👉 Explication : teste les deux scénarios séparément.

5. Redémarrer Keepalived et observer le retour au primaire selon le comportement voulu.
   ```bash
   sudo systemctl start keepalived
   ```
   👉 Explication : vérifie connexions existantes et préemption.

## 2. Production — Contrôles

Réaliser les essais dans une fenêtre approuvée avec console accessible.

## 3. Production — Sécurité

- Pas d'essai sur un service de production sans validation.

## Validation et retour arrière

- **Validation** : l'IP se déplace et revient comme prévu, service continu.
- **Retour arrière** : redémarrer `haproxy` et `keepalived` sur les deux nœuds.

## Si le problème n'est pas résolu

- [Keepalived — documentation](https://keepalived.readthedocs.io/en/latest/)
- [Keepalived — documentation](https://keepalived.readthedocs.io/en/latest/)
- [Guide complet](/02-fiches-completes/transverses/multi-os/autres/08-haute-disponibilite-keepalived-vrrp-haproxy#4-tester-le-basculement)