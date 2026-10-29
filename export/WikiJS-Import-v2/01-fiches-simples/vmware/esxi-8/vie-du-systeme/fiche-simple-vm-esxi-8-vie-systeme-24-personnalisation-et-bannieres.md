---
title: "Fiche Simple - VM ESXi 8 Vie Systeme 24 Personnalisation Et Bannieres"
description: "Afficher un avertissement légal à la connexion."
published: true
date: 2026-10-29T20:22:10Z
tags: ["esxi8", "vie-du-systeme", "cycle-de-vie", "etape-24"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_24_Personnalisation_Et_Bannieres

- **Environnement** : Hôte VMware ESXi 8 (hyperviseur)
- **OS / Version** : VMware ESXi 8; étape 24 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `esxi8`, `vie-du-systeme`, `cycle-de-vie`, `etape-24`

---

## Problème précis à résoudre

Afficher un avertissement légal à la connexion.

## 1. Hors-Production (Lab / Test / POC)

1. Host Client : **Gérer > Avancé > Rechercher `Annotations.WelcomeMessage`** pour la bannière du Host Client et de la DCUI. En ligne de commande :
   ```sh
   esxcli system settings advanced set -o /Annotations/WelcomeMessage -s "Accès réservé aux administrateurs autorisés. Toute connexion est journalisée."
   esxcli system settings advanced list -o /Annotations/WelcomeMessage
   ```
   👉 Explication : le message s'affiche avant la connexion.

2. Bannière SSH : éditer `/etc/issue` puis `/etc/ssh/sshd_config` (`Banner /etc/issue`), puis relancer SSH.
   ```sh
   cat /etc/issue
   ```
   👉 Explication : avertissement affiché avant l'authentification.

3. Vérifier que le navigateur d'objets MOB reste désactivé (Host Client : **Gérer > Avancé > Config.HostAgent.plugins.solo.enableMob**).
   ```sh
   esxcli system settings advanced list -o /Config/HostAgent/plugins/solo/enableMob
   ```
   👉 Explication : vérifie que le navigateur d'objets (MOB) est désactivé (valeur `false`).

## 2. Production — Contrôles

Texte validé par le service juridique.

## 3. Production — Sécurité

Ne pas indiquer de version dans la bannière.

## Validation et retour arrière

- **Validation** : La bannière s'affiche à la connexion.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire VMware ESXi 8](/01-fiches-simples/vmware/esxi-8/vie-du-systeme/sommaire-vie-du-systeme-esxi-8)
- [Documentation officielle](https://docs.vmware.com/)