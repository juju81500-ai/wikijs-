---
title: "Fiche Simple - Windows Client 11 OpenVPN Mise A Jour Retour Arriere"
description: "Mettre à jour le client OpenVPN avec retour arrière."
published: true
date: 2026-10-29T20:59:58Z
tags: ["openvpn", "windows11", "vie-du-logiciel", "mise-a-jour-retour-arriere"]
editor: markdown
dateCreated: 2026-10-29T20:59:58Z
dateModified: 2026-10-29T20:59:58Z
---

# Fiche_Simple_-_Windows_Client_11_OpenVPN_Mise_A_Jour_Retour_Arriere

- **Environnement** : Poste Windows 11 (client OpenVPN Community)
- **OS / Version** : Windows 11; version du client à vérifier sur la page de téléchargement officielle
- **Catégorie** : OpenVPN Community client / mise à jour / retour arrière
- **Tags** : `openvpn`, `windows11`, `vie-du-logiciel`, `mise-a-jour-retour-arriere`

---

## Problème précis à résoudre

Mettre à jour le client OpenVPN avec retour arrière.

## 1. Hors-Production (Lab / Test / POC)

1. Noter la version actuelle (Paramètres > Applications > Applications installées > OpenVPN) et conserver le MSI actuel.
   👉 Explication : La version de référence sert au retour arrière.

2. Télécharger le nouveau MSI sur la page officielle, vérifier l'empreinte puis installer par-dessus :
   ```powershell
   Get-FileHash -Algorithm SHA256 .\FICHIER_MSI
   msiexec /i .\FICHIER_MSI /qb
   ```
   👉 Explication : FICHIER_MSI est le nouveau MSI (à remplacer); les profils existants sont conservés.

3. Retour arrière : désinstaller puis réinstaller la version précédente conservée :
   ```powershell
   msiexec /x .\FICHIER_MSI_NOUVEAU /qb
   msiexec /i .\FICHIER_MSI_ANCIEN /qb
   ```
   👉 Explication : FICHIER_MSI_NOUVEAU et FICHIER_MSI_ANCIEN sont les MSI correspondants (à remplacer); réimporter les profils si nécessaire.

## 2. Production — Contrôles

Tester sur un poste pilote avant le déploiement.

## 3. Production — Sécurité

- Source unique : openvpn.net.

## Validation et retour arrière

- **Validation** : Nouvelle version installée et connexion fonctionnelle.
- **Retour arrière** : Réinstaller la version précédente comme à l'étape 3.

## Si le problème n'est pas résolu

- [Première étape du guide](/01-fiches-simples/windows/client-11/vie-du-logiciel/openvpn/fiche-simple-windows-client-11-openvpn-prerequis-limites)
- [Fiche d'entrée du logiciel](/01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-openvpn)
- [OpenVPN Community — téléchargements officiels](https://openvpn.net/community-downloads/)
- [OpenVPN Community — documentation officielle](https://openvpn.net/community-resources/)