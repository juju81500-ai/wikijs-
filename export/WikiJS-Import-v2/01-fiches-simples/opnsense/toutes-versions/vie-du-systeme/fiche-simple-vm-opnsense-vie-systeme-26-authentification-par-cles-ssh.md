---
title: "Fiche Simple - VM OPNsense Vie Systeme 26 Authentification Par Cles Ssh"
description: "Remplacer le mot de passe par une clé pour l'accès SSH."
published: true
date: 2026-10-29T20:22:10Z
tags: ["opnsense", "vie-du-systeme", "cycle-de-vie", "etape-26"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_OPNsense_Vie_Systeme_26_Authentification_Par_Cles_Ssh

- **Environnement** : Pare-feu OPNsense (VM ou matériel)
- **OS / Version** : OPNsense; étape 26 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `opnsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-26`

---

## Problème précis à résoudre

Remplacer le mot de passe par une clé pour l'accès SSH.

## 1. Hors-Production (Lab / Test / POC)

1. Générer une clé sur le poste d'administration :
   ```sh
   ssh-keygen -t ed25519 -C "ADMIN01@fw01"
   cat ~/.ssh/id_ed25519.pub
   ```
   👉 Explication : crée la paire de clés; ne jamais transmettre le fichier privé.

2. Coller la clé publique dans Système > Accès > Utilisateurs > ADMIN01 > Clés SSH autorisées, puis Enregistrer.
   👉 Explication : la clé est déposée dans le compte du pare-feu.

3. Tester la connexion :
   ```sh
   ssh -i ~/.ssh/id_ed25519 ADMIN01@IP_LAN
   ```
   👉 Explication : doit ouvrir une session sans mot de passe.

## 2. Production — Contrôles

Une clé par administrateur, protégée par une phrase secrète.

## 3. Production — Sécurité

Retirer la clé dès qu'un administrateur quitte l'équipe.

## Validation et retour arrière

- **Validation** : La connexion par clé fonctionne.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire OPNsense](/01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/sommaire-vie-du-systeme-opnsense)
- [Documentation officielle](https://docs.opnsense.org/)