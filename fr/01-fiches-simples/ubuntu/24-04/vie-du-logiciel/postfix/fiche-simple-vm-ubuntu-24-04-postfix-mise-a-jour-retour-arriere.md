---
title: "Fiche Simple - VM Ubuntu 24.04 Postfix Mise A Jour Retour Arriere"
description: "Mettre à jour Postfix depuis dépôts configurés."
published: true
date: 2026-11-03T14:22:28Z
tags: ["postfix", "serveur", "vie-du-logiciel", "mise-a-jour-retour-arriere"]
editor: markdown
dateCreated: 2026-11-03T14:22:28Z
dateModified: 2026-11-03T14:22:28Z
---

# Fiche_Simple_-_VM_Ubuntu_24.04_Postfix_Mise_A_Jour_Retour_Arriere

- **Environnement** : [[Glossary:VM]] Ubuntu Server 24-04; Postfix depuis les dépôts de la distribution
- **OS / Version** : Ubuntu Server 24-04
- **Catégorie** : Vie du logiciel / Postfix — Mise à jour et retour arrière
- **Tags** : `postfix`, `serveur`, `vie-du-logiciel`, `mise_a_jour_retour_arriere`

---

## Problème précis à résoudre

Mettre à jour Postfix depuis dépôts configurés.

## 1. Hors-Production (Lab / Test / POC)

1. Mise à jour et retour arrière :
   ```bash
   sudo apt update && apt list --upgradable 2>/dev/null | grep -E "postfix|^Listing"
sudo apt install --only-upgrade -y postfix
sudo systemctl restart postfix
sudo postfix check
   ```
   👉 Explication : Liste les paquets puis met à jour en lab; contrôler les notes de version et la syntaxe après redémarrage.


## 2. Production — Contrôles

Préparer sauvegarde restaurable, fenêtre, espace disque et compatibilité clients.

## 3. Production — Sécurité

Utiliser paquets signés des dépôts autorisés.

## Validation et retour arrière

- **Validation** : Version mise à jour consignée, service actif et contrôle syntaxique réussi.
- **Retour arrière** : Restaurer un snapshot cohérent plutôt qu’un downgrade de paquet isolé.

## Si le problème n'est pas résolu

- [Prérequis et limites](/fr/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/postfix/fiche-simple-vm-ubuntu-24-04-postfix-prerequis-limites)
- [Installer](/fr/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/postfix/fiche-simple-vm-ubuntu-24-04-postfix-installer)
- [Configurer](/fr/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/postfix/fiche-simple-vm-ubuntu-24-04-postfix-configurer)
- [Sécuriser](/fr/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/postfix/fiche-simple-vm-ubuntu-24-04-postfix-securiser)
- [Valider (recette)](/fr/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/postfix/fiche-simple-vm-ubuntu-24-04-postfix-valider)
- [Sauvegarder / restaurer](/fr/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/postfix/fiche-simple-vm-ubuntu-24-04-postfix-sauvegarder-restaurer)
- [Documentation officielle](https://www.postfix.org/documentation.html)