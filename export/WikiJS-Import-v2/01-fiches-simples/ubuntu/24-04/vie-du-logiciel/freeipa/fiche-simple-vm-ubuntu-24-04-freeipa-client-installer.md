---
title: "Fiche Simple - VM Ubuntu 24.04 FreeIPA Client Installer"
description: "Installer le client FreeIPA sur Ubuntu depuis les dépôts de la distribution."
published: true
date: 2026-10-29T21:02:28Z
tags: ["freeipa", "ubuntu24-04", "vie-du-logiciel", "installer"]
editor: markdown
dateCreated: 2026-10-29T21:02:28Z
dateModified: 2026-10-29T21:02:28Z
---

# Fiche_Simple_-_VM_Ubuntu_24.04_FreeIPA_Client_Installer

- **Environnement** : VM Ubuntu 24.04 cliente d'un domaine FreeIPA existant
- **OS / Version** : Ubuntu 24.04 LTS Noble; paquet freeipa-client des dépôts, version à vérifier
- **Catégorie** : FreeIPA client / installer
- **Tags** : `freeipa`, `ubuntu24-04`, `vie-du-logiciel`, `installer`

---

## Problème précis à résoudre

Installer le client FreeIPA sur Ubuntu depuis les dépôts de la distribution.

## 1. Hors-Production (Lab / Test / POC)

1. Installer le paquet :
   ```bash
   sudo apt update
   apt-cache policy freeipa-client
   sudo apt install freeipa-client
   ```
   👉 Explication : Le paquet installe ipa-client-install et les dépendances (SSSD, Kerberos); noter la version et vérifier qu'elle est compatible avec le serveur.

2. Contrôler la commande d'inscription :
   ```bash
   ipa-client-install --version
   ```
   👉 Explication : La commande doit répondre avant de poursuivre.

## 2. Production — Contrôles

Consigner version et origine du paquet.

## 3. Production — Sécurité

- Dépôts approuvés uniquement; ne pas inscrire l'hôte avant la fiche Configurer.

## Validation et retour arrière

- **Validation** : ipa-client-install --version répond.
- **Retour arrière** : sudo apt remove freeipa-client (aucune inscription n'a encore été faite).

## Si le problème n'est pas résolu

- [Étape suivante du guide](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/freeipa/fiche-simple-vm-ubuntu-24-04-freeipa-client-configurer)
- [Fiche d'entrée du logiciel](/01-fiches-simples/logiciels/05-systemes-annuaires-et-services/fiche-logiciel-freeipa)
- [FreeIPA — page Client](https://www.freeipa.org/page/Client)
- [FreeIPA — page Documentation](https://www.freeipa.org/page/Documentation)