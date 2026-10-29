---
title: "Fiche Simple - Windows Client 11 WireGuard Mise A Jour Retour Arriere"
description: "Mettre à jour le client WireGuard avec retour arrière."
published: true
date: 2026-10-29T21:01:00Z
tags: ["wireguard", "windows11", "vie-du-logiciel", "mise-a-jour-retour-arriere"]
editor: markdown
dateCreated: 2026-10-29T21:01:00Z
dateModified: 2026-10-29T21:01:00Z
---

# Fiche_Simple_-_Windows_Client_11_WireGuard_Mise_A_Jour_Retour_Arriere

- **Environnement** : Poste Windows 11 (client WireGuard)
- **OS / Version** : Windows 11; version du client à vérifier sur la page officielle
- **Catégorie** : WireGuard client / mise à jour / retour arrière
- **Tags** : `wireguard`, `windows11`, `vie-du-logiciel`, `mise-a-jour-retour-arriere`

---

## Problème précis à résoudre

Mettre à jour le client WireGuard avec retour arrière.

## 1. Hors-Production (Lab / Test / POC)

1. Noter la version actuelle (Paramètres > Applications) et conserver l'installateur courant.
   👉 Explication : Sert au retour arrière.

2. Mettre à jour : exécuter le nouvel installateur officiel, ou en PowerShell élevé :
   ```powershell
   winget upgrade --id WireGuard.WireGuard -e
   ```
   👉 Explication : Vérifier l'identifiant comme à l'étape d'installation.

3. Retour arrière : désinstaller puis réinstaller l'installateur précédent conservé.
   👉 Explication : Recréer ou réimporter le tunnel si nécessaire.

## 2. Production — Contrôles

Tester sur un poste pilote.

## 3. Production — Sécurité

- Source officielle uniquement.

## Validation et retour arrière

- **Validation** : Nouvelle version active et tunnel fonctionnel.
- **Retour arrière** : Réinstaller la version précédente.

## Si le problème n'est pas résolu

- [Première étape du guide](/01-fiches-simples/windows/client-11/vie-du-logiciel/wireguard/fiche-simple-windows-client-11-wireguard-prerequis-limites)
- [Fiche d'entrée du logiciel](/01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-wireguard)
- [WireGuard — installation officielle](https://www.wireguard.com/install/)
- [WireGuard pour Windows — documentation](https://git.zx2c4.com/wireguard-windows/about/)