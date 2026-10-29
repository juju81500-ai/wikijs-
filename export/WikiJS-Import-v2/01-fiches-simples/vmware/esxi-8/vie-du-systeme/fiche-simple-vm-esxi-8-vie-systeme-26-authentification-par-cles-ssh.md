---
title: "Fiche Simple - VM ESXi 8 Vie Systeme 26 Authentification Par Cles Ssh"
description: "Remplacer le mot de passe SSH par des clés."
published: true
date: 2026-10-29T20:22:10Z
tags: ["esxi8", "vie-du-systeme", "cycle-de-vie", "etape-26"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_26_Authentification_Par_Cles_Ssh

- **Environnement** : Hôte VMware ESXi 8 (hyperviseur)
- **OS / Version** : VMware ESXi 8; étape 26 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `esxi8`, `vie-du-systeme`, `cycle-de-vie`, `etape-26`

---

## Problème précis à résoudre

Remplacer le mot de passe SSH par des clés.

## 1. Hors-Production (Lab / Test / POC)

1. Sur le poste d'administration, générer une clé :
   ```sh
   ssh-keygen -t ed25519 -C "admin1@poste"
   ```
   👉 Explication : crée la paire de clés; protéger la clé privée par phrase secrète.

2. Déposer la clé publique sur l'hôte (remplacer `IP_HOTE` et `CLE_PUBLIQUE`) :
   ```sh
   cat ~/.ssh/id_ed25519.pub | ssh root@IP_HOTE 'cat >> /etc/ssh/keys-root/authorized_keys'
   ```
   👉 Explication : sous ESXi, le fichier des clés de root est `/etc/ssh/keys-root/authorized_keys`.

3. Tester la connexion par clé dans une 2e session avant de désactiver le mot de passe.
   ```sh
   ssh root@IP_HOTE
   ```
   👉 Explication : évite de se verrouiller.

## 2. Production — Contrôles

Clés protégées par phrase secrète; une clé par administrateur.

## 3. Production — Sécurité

Interdire le mot de passe SSH à l'étape suivante.

## Validation et retour arrière

- **Validation** : Connexion par clé réussie.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire VMware ESXi 8](/01-fiches-simples/vmware/esxi-8/vie-du-systeme/sommaire-vie-du-systeme-esxi-8)
- [Documentation officielle](https://docs.vmware.com/)