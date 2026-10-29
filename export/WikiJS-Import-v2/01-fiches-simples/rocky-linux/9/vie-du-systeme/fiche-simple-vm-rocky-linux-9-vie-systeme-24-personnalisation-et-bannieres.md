---
title: "Fiche Simple - VM Rocky Linux 9 Vie Systeme 24 Personnalisation Et Bannieres"
description: "Afficher un avertissement légal."
published: true
date: 2026-10-29T20:22:10Z
tags: ["rocky9", "vie-du-systeme", "cycle-de-vie", "etape-24"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_24_Personnalisation_Et_Bannieres

- **Environnement** : VM Rocky Linux 9 (serveur)
- **OS / Version** : Rocky Linux 9; étape 24 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `rocky9`, `vie-du-systeme`, `cycle-de-vie`, `etape-24`

---

## Problème précis à résoudre

Afficher un avertissement légal.

## 1. Hors-Production (Lab / Test / POC)

1. Définir la bannière avant connexion :
   ```bash
   echo 'Accès réservé aux personnes autorisées. Les actions sont journalisées.' | sudo tee /etc/issue.net
   ```
   👉 Explication : texte affiché avant l'authentification SSH.

2. L'activer dans sshd :
   ```bash
   echo 'Banner /etc/issue.net' | sudo tee /etc/ssh/sshd_config.d/20-banner.conf
   sudo sshd -t && sudo systemctl reload sshd
   ```
   👉 Explication : recharge sshd après test de syntaxe.

3. Personnaliser le message du jour :
   ```bash
   echo 'SRV01 - Rocky Linux 9 - Production' | sudo tee /etc/motd
   ```
   👉 Explication : affiché après connexion.

## 2. Production — Contrôles

Faire valider le texte par le service juridique.

## 3. Production — Sécurité

Ne pas révéler la version ni l'architecture dans la bannière.

## Validation et retour arrière

- **Validation** : La bannière s'affiche à la connexion SSH.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Rocky Linux 9](/01-fiches-simples/rocky-linux/9/vie-du-systeme/sommaire-vie-du-systeme-rocky-linux-9)
- [Documentation officielle](https://docs.rockylinux.org/)