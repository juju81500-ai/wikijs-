---
title: "Fiche Simple - Windows Client 11 WireGuard Securiser"
description: "Protéger le tunnel et le poste."
published: true
date: 2026-10-29T21:01:00Z
tags: ["wireguard", "windows11", "vie-du-logiciel", "securiser"]
editor: markdown
dateCreated: 2026-10-29T21:01:00Z
dateModified: 2026-10-29T21:01:00Z
---

# Fiche_Simple_-_Windows_Client_11_WireGuard_Securiser

- **Environnement** : Poste Windows 11 (client WireGuard)
- **OS / Version** : Windows 11; version du client à vérifier sur la page officielle
- **Catégorie** : WireGuard client / sécuriser
- **Tags** : `wireguard`, `windows11`, `vie-du-logiciel`, `securiser`

---

## Problème précis à résoudre

Protéger le tunnel et le poste.

## 1. Hors-Production (Lab / Test / POC)

1. Éviter le full-tunnel non validé : vérifier AllowedIPs.
   👉 Explication : 0.0.0.0/0 redirige tout le trafic; à n'utiliser que si l'architecture le prévoit.

2. Contrôler le pare-feu Windows :
   ```powershell
   Get-NetFirewallProfile | Select-Object Name,Enabled
   ```
   👉 Explication : Les trois profils doivent être activés.

3. Limiter les droits : ne pas donner le droit de gérer les tunnels aux utilisateurs standard.
   👉 Explication : Les configurations sont stockées chiffrées pour le compte système; ne pas exporter les fichiers en clair.

## 2. Production — Contrôles

Activer BitLocker; en cas de perte du poste, demander le retrait du pair côté serveur.

## 3. Production — Sécurité

- Pas d'export de configuration contenant la clé privée sur support non chiffré.

## Validation et retour arrière

- **Validation** : Pare-feu actif, AllowedIPs conformes.
- **Retour arrière** : Rétablir les valeurs d'origine du tunnel.

## Si le problème n'est pas résolu

- [Étape suivante du guide](/01-fiches-simples/windows/client-11/vie-du-logiciel/wireguard/fiche-simple-windows-client-11-wireguard-valider)
- [Fiche d'entrée du logiciel](/01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-wireguard)
- [WireGuard — installation officielle](https://www.wireguard.com/install/)
- [WireGuard pour Windows — documentation](https://git.zx2c4.com/wireguard-windows/about/)