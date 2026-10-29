---
title: "Fiche Simple - VM Rocky 9 WireGuard Mise A Jour Retour Arriere"
description: "Mettre à jour WireGuard en gardant un retour arrière."
published: true
date: 2026-10-29T21:01:00Z
tags: ["wireguard", "rocky9", "vie-du-logiciel", "mise-a-jour-retour-arriere"]
editor: markdown
dateCreated: 2026-10-29T21:01:00Z
dateModified: 2026-10-29T21:01:00Z
---

# Fiche_Simple_-_VM_Rocky_9_WireGuard_Mise_A_Jour_Retour_Arriere

- **Environnement** : VM Rocky Linux 9 dédiée à un serveur WireGuard natif
- **OS / Version** : Rocky Linux 9; wireguard-tools issu d'EPEL, module noyau à vérifier sur l'hôte
- **Catégorie** : WireGuard natif / mise à jour / retour arrière
- **Tags** : `wireguard`, `rocky9`, `vie-du-logiciel`, `mise-a-jour-retour-arriere`

---

## Problème précis à résoudre

Mettre à jour WireGuard en gardant un retour arrière.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder et noter la version :
   ```bash
   wg --version
   sudo install -d -m 0700 /var/backups/wireguard
   sudo tar czf /var/backups/wireguard/avant-maj-$(date +%F).tar.gz -C / etc/wireguard
   ```
   👉 Explication : La version et l'archive servent au retour arrière.

2. Mettre à jour les outils :
   ```bash
   sudo dnf check-update wireguard-tools
   sudo dnf upgrade wireguard-tools
   wg --version
   ```
   👉 Explication : Un nouveau noyau demande un redémarrage planifié.

3. Rejouer la recette : voir la fiche de validation.
   ```bash
   sudo systemctl restart wg-quick@wg0
   sudo wg show
   ```
   👉 Explication : Vérifier le handshake du pair pilote.

4. Retour arrière si la recette échoue :
   ```bash
   dnf history list | head -n 5
   sudo dnf history undo TRANSACTION_ID
   ```
   👉 Explication : VERSION_PRECEDENTE (ou TRANSACTION_ID) est la version ou la transaction notée avant la mise à jour (à remplacer); sinon restaurer le snapshot.

## 2. Production — Contrôles

Prévenir les utilisateurs et prendre un snapshot.

## 3. Production — Sécurité

- Dépôts approuvés uniquement.

## Validation et retour arrière

- **Validation** : Tunnel actif, version attendue.
- **Retour arrière** : Réinstaller la version précédente et restaurer avant-maj-DATE.tar.gz (DATE à remplacer).

## Si le problème n'est pas résolu

- [Première étape du guide](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/wireguard/fiche-simple-vm-rocky-9-wireguard-prerequis-limites)
- [Fiche d'entrée du logiciel](/01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-wireguard)
- [WireGuard — installation officielle](https://www.wireguard.com/install/)
- [WireGuard — démarrage rapide](https://www.wireguard.com/quickstart/)