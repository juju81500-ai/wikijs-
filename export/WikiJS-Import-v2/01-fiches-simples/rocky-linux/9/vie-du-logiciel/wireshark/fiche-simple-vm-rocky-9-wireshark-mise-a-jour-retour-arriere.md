---
title: "Fiche Simple - VM Rocky 9 Wireshark Mise A Jour Retour Arriere"
description: "Mettre à jour Wireshark/TShark et revenir en arrière si nécessaire."
published: true
date: 2026-10-29T20:58:07Z
tags: ["wireshark", "rocky9", "vie-du-logiciel", "mise-a-jour-retour-arriere"]
editor: markdown
dateCreated: 2026-10-29T20:58:07Z
dateModified: 2026-10-29T20:58:07Z
---

# Fiche_Simple_-_VM_Rocky_9_Wireshark_Mise_A_Jour_Retour_Arriere

- **Environnement** : VM Rocky Linux 9 dédiée à Wireshark
- **OS / Version** : Rocky Linux 9 (compatible RHEL 9); version des paquets à vérifier sur l’hôte
- **Catégorie** : Wireshark / mise à jour et retour arrière
- **Tags** : `wireshark`, `rocky9`, `vie-du-logiciel`, `mise-a-jour-retour-arriere`

---

## Problème précis à résoudre

Mettre à jour Wireshark/TShark et revenir en arrière si nécessaire.

## 1. Hors-Production (Lab / Test / POC)

1. Consigner la version :
   ```bash
   tshark --version | head -n 1
   ```
   👉 Explication : Référence avant changement.

2. Mettre à jour :
   ```bash
   sudo dnf check-update wireshark wireshark-cli
   sudo dnf upgrade wireshark wireshark-cli
   ```
   👉 Explication : Applique la version publiée par la distribution; lire les avis de sécurité.

3. Contrôler :
   ```bash
   tshark --version | head -n 1
   dumpcap -D
   ```
   👉 Explication : Vérifie le fonctionnement et les droits de capture, qui peuvent être réinitialisés par une mise à jour.

4. Retour arrière :
   ```bash
   dnf history list wireshark
   sudo dnf history undo ID_TRANSACTION
   ```
   👉 Explication : ID_TRANSACTION (à remplacer) est la transaction dnf à annuler; sinon `sudo dnf downgrade wireshark wireshark-cli` après vérification.

## 2. Production — Contrôles

Tester sur lab, sauvegarder le profil avant la mise à jour.

## 3. Production — Sécurité

- Mettre à jour rapidement les failles de dissecteurs.
- Contrôler à nouveau les permissions de dumpcap.

## Validation et retour arrière

- **Validation** : Version attendue et recette réussie.
- **Retour arrière** : Appliquer le retour arrière puis rejouer la recette.

## Si le problème n’est pas résolu

- [Wireshark — documentation officielle](https://www.wireshark.org/docs/)
- [Fiche d’entrée du logiciel](/01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-wireshark)
- [Étape précédente du guide](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/wireshark/fiche-simple-vm-rocky-9-wireshark-sauvegarder-restaurer)