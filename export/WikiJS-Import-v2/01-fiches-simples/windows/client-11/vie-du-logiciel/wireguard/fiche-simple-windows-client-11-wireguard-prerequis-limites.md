---
title: "Fiche Simple - Windows Client 11 WireGuard Prerequis Limites"
description: "Valider le poste et les paramètres avant d'installer le client WireGuard."
published: true
date: 2026-10-29T21:01:00Z
tags: ["wireguard", "windows11", "vie-du-logiciel", "prerequis-limites"]
editor: markdown
dateCreated: 2026-10-29T21:01:00Z
dateModified: 2026-10-29T21:01:00Z
---

# Fiche_Simple_-_Windows_Client_11_WireGuard_Prerequis_Limites

- **Environnement** : Poste Windows 11 (client WireGuard)
- **OS / Version** : Windows 11; version du client à vérifier sur la page officielle
- **Catégorie** : WireGuard client / prérequis et limites
- **Tags** : `wireguard`, `windows11`, `vie-du-logiciel`, `prerequis-limites`

---

## Problème précis à résoudre

Valider le poste et les paramètres avant d'installer le client WireGuard.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier la version de Windows et les droits administrateur :
   ```powershell
   winver
   ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
   ```
   👉 Explication : GUI : touche Windows + R puis winver. L'installation exige un compte administrateur.

2. Recueillir les paramètres fournis par l'administrateur du serveur :
   👉 Explication : SERVER_PUBLIC_KEY (clé publique du serveur), SERVER_ENDPOINT:VPN_UDP_PORT (adresse et port), CLIENT_VPN_ADDRESS (adresse du client), ALLOWED_NETWORKS (réseaux à joindre). Valeurs en majuscules à remplacer; la clé privée du client est générée sur le poste, jamais reçue.

## 2. Production — Contrôles

Limite : pas de gestion centralisée des utilisateurs; l'administrateur doit enregistrer la clé publique du poste.

## 3. Production — Sécurité

- Ne jamais envoyer la clé privée du client; seule la clé publique est transmise.

## Validation et retour arrière

- **Validation** : Droits confirmés et paramètres du serveur reçus.
- **Retour arrière** : Aucun changement : rien à restaurer.

## Si le problème n'est pas résolu

- [Étape suivante du guide](/01-fiches-simples/windows/client-11/vie-du-logiciel/wireguard/fiche-simple-windows-client-11-wireguard-installer)
- [Fiche d'entrée du logiciel](/01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-wireguard)
- [WireGuard — installation officielle](https://www.wireguard.com/install/)
- [WireGuard pour Windows — documentation](https://git.zx2c4.com/wireguard-windows/about/)