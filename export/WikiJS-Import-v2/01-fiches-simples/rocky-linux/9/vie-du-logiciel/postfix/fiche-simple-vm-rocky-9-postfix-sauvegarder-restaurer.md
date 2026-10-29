---
title: "Fiche Simple - VM Rocky 9 Postfix Sauvegarder Restaurer"
description: "Sauvegarder configuration de Postfix et tester restauration."
published: true
date: 2026-10-29T21:11:53Z
tags: ["postfix", "serveur", "vie-du-logiciel", "sauvegarder_restaurer"]
editor: markdown
dateCreated: 2026-10-29T21:11:53Z
dateModified: 2026-10-29T21:11:53Z
---

# Fiche_Simple_-_VM_Rocky_9_Postfix_Sauvegarder_Restaurer

- **Environnement** : VM Rocky Linux 9; Postfix depuis les dépôts de la distribution
- **OS / Version** : Rocky Linux 9
- **Catégorie** : Vie du logiciel / Postfix — Sauvegarder / restaurer
- **Tags** : `postfix`, `serveur`, `vie-du-logiciel`, `sauvegarder_restaurer`

---

## Problème précis à résoudre

Sauvegarder configuration de Postfix et tester restauration.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder / restaurer :
   ```bash
   sudo tar --xattrs -czf /root/postfix-config-$(date +%F).tgz /etc/postfix
sudo chmod 600 /root/postfix-config-*.tgz
   ```
   👉 Explication : Archive la configuration; chiffrer et copier hors hôte. Elle ne contient pas les courriels ni nécessairement la file de livraison.


## 2. Production — Contrôles

Dovecot : inclure boîtes et métadonnées selon backend; Postfix : traiter la file séparément si nécessaire. Définir RPO/RTO.

## 3. Production — Sécurité

Restreindre accès aux archives contenant secrets et clés.

## Validation et retour arrière

- **Validation** : Restauration de lab démarre le service et passe le contrôle de configuration.
- **Retour arrière** : Restaurer un snapshot cohérent service/configuration/données; downgrade de paquet isolé risqué.

## Si le problème n'est pas résolu

- [Prérequis et limites](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/postfix/fiche-simple-vm-rocky-9-postfix-prerequis-limites)
- [Installer](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/postfix/fiche-simple-vm-rocky-9-postfix-installer)
- [Configurer](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/postfix/fiche-simple-vm-rocky-9-postfix-configurer)
- [Sécuriser](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/postfix/fiche-simple-vm-rocky-9-postfix-securiser)
- [Valider (recette)](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/postfix/fiche-simple-vm-rocky-9-postfix-valider)
- [Mise à jour et retour arrière](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/postfix/fiche-simple-vm-rocky-9-postfix-mise-a-jour-retour-arriere)
- [Documentation officielle](https://www.postfix.org/documentation.html)