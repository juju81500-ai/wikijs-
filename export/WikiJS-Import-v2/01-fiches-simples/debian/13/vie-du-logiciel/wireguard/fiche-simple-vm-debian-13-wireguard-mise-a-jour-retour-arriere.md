---
title: "Fiche Simple - VM Debian 13 WireGuard Mise A Jour Retour Arriere"
description: "Mettre à jour outils/noyau sans perdre la connectivité d’administration."
published: true
date: 2026-10-29T20:35:43Z
tags: ["wireguard", "debian13", "vie-du-logiciel", "mise_a_jour_retour_arriere"]
editor: markdown
dateCreated: 2026-10-29T20:35:43Z
dateModified: 2026-10-29T20:35:43Z
---

# Fiche_Simple_-_VM_Debian_13_WireGuard_Mise_A_Jour_Retour_Arriere

- **Environnement** : VM Debian 13 dédiée à WireGuard natif
- **OS / Version** : Debian 13 Trixie; version des dépôts à vérifier sur l’hôte
- **Catégorie** : WireGuard natif / mise à jour et retour arrière
- **Tags** : `wireguard`, `debian13`, `vie-du-logiciel`, `mise_a_jour_retour_arriere`

---

## Problème précis à résoudre

Mettre à jour outils/noyau sans perdre la connectivité d’administration.

## 1. Hors-Production (Lab / Test / POC)

1. Consigner les paquets, versions candidates et noyau actif :
   ```bash
   dpkg-query -W wireguard wireguard-tools
   apt-cache policy wireguard wireguard-tools
   uname -r
   ```
   👉 Explication : Examiner avis Debian et impact d’une mise à jour noyau sur le module.

2. Sauvegarder /etc/wireguard et vérifier la console hors bande avant changement.
   👉 Explication : Un accès d’administration indépendant du tunnel est obligatoire.

3. Après approbation, mettre à jour puis contrôler l’unité :
   ```bash
   sudo apt update
   sudo apt install --only-upgrade wireguard wireguard-tools
   sudo systemctl restart wg-quick@wg0
   systemctl status wg-quick@wg0 --no-pager
   sudo wg show wg0
   ```
   👉 Explication : Confirmer unité et tester le handshake du pair pilote.

## 2. Production — Contrôles

Planifier la fenêtre, vérifier compatibilité noyau/module et préparer la restauration de configuration.

## 3. Production — Sécurité

- Ne pas revenir à une version vulnérable sans dérogation; conserver configurations et clés en dépôt protégé.

## Validation et retour arrière

- **Validation** : Version attendue, unité active, handshake récent et routes approuvées vérifiés.
- **Retour arrière** : restaurer la configuration antérieure vérifiée et arrêter le service ou la capture si la recette échoue; consigner le changement.

## Si le problème n’est pas résolu

- [WireGuard natif — documentation officielle](https://www.wireguard.com/quickstart/)
- [Étape suivante du guide](/01-fiches-simples/debian/13/vie-du-logiciel/wireguard/fiche-simple-vm-debian-13-wireguard-prerequis-limites)