---
title: "Fiche Simple - VM Ubuntu 24.04 Postfix Configurer"
description: "Configurer Postfix sans ouvrir un relais ou une authentification non maîtrisés."
published: true
date: 2026-10-29T21:11:53Z
tags: ["postfix", "serveur", "vie-du-logiciel", "configurer"]
editor: markdown
dateCreated: 2026-10-29T21:11:53Z
dateModified: 2026-10-29T21:11:53Z
---

# Fiche_Simple_-_VM_Ubuntu_24.04_Postfix_Configurer

- **Environnement** : VM Ubuntu Server 24.04; Postfix depuis les dépôts de la distribution
- **OS / Version** : Ubuntu Server 24.04
- **Catégorie** : Vie du logiciel / Postfix — Configurer
- **Tags** : `postfix`, `serveur`, `vie-du-logiciel`, `configurer`

---

## Problème précis à résoudre

Configurer Postfix sans ouvrir un relais ou une authentification non maîtrisés.

## 1. Hors-Production (Lab / Test / POC)

1. Configurer :
   ```bash
   sudo postconf -n
sudo cp -a /etc/postfix/main.cf /etc/postfix/main.cf.prechange
sudo postconf -e "myhostname = MAIL.EXAMPLE.NET"
sudo postconf -e "mynetworks = 127.0.0.0/8, [::1]/128"
sudo postfix check
   ```
   👉 Explication : Sauvegarde puis fixe le nom d’hôte et limite les réseaux de confiance à la boucle locale. `MAIL.EXAMPLE.NET` est à remplacer par le FQDN validé; contrôler chaque réglage selon la version installée.


## 2. Production — Contrôles

Tracer les paramètres, les domaines et les réseaux autorisés; contrôler la syntaxe avec `postfix check` avant rechargement.

## 3. Production — Sécurité

Postfix : garder `reject_unauth_destination` et limiter `mynetworks`. Dovecot : activer TLS selon la version et les protocoles utilisés.

## Validation et retour arrière

- **Validation** : `postfix check` réussit et le service reste actif après rechargement.
- **Retour arrière** : Restaurer la copie `.prechange`, relancer `postfix check` puis redémarrer postfix.

## Si le problème n'est pas résolu

- [Prérequis et limites](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/postfix/fiche-simple-vm-ubuntu-24-04-postfix-prerequis-limites)
- [Installer](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/postfix/fiche-simple-vm-ubuntu-24-04-postfix-installer)
- [Sécuriser](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/postfix/fiche-simple-vm-ubuntu-24-04-postfix-securiser)
- [Valider (recette)](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/postfix/fiche-simple-vm-ubuntu-24-04-postfix-valider)
- [Sauvegarder / restaurer](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/postfix/fiche-simple-vm-ubuntu-24-04-postfix-sauvegarder-restaurer)
- [Mise à jour et retour arrière](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/postfix/fiche-simple-vm-ubuntu-24-04-postfix-mise-a-jour-retour-arriere)
- [Documentation officielle](https://www.postfix.org/documentation.html)