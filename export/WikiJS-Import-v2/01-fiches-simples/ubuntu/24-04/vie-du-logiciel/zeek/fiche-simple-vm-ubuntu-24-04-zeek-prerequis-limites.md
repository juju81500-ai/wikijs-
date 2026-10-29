---
title: "Fiche Simple - VM Ubuntu 24.04 Zeek Prerequis Limites"
description: "Cadrer un capteur Zeek passif (journaux de métadonnées réseau) sur VM Ubuntu Server 24.04 LTS dans un périmètre autorisé."
published: true
date: 2026-10-29T20:59:32Z
tags: ["zeek", "ubuntu24.04", "vie-du-logiciel", "prerequis-limites"]
editor: markdown
dateCreated: 2026-10-29T20:59:32Z
dateModified: 2026-10-29T20:59:32Z
---

# Fiche_Simple_-_VM_Ubuntu_24.04_Zeek_Prerequis_Limites

- **Environnement** : VM Ubuntu Server 24.04 LTS dédiée à Zeek
- **OS / Version** : Ubuntu Server 24.04 LTS (Noble Numbat); version des paquets à vérifier sur l’hôte
- **Catégorie** : Zeek / prérequis et limites
- **Tags** : `zeek`, `ubuntu24.04`, `vie-du-logiciel`, `prerequis-limites`

---

## Problème précis à résoudre

Cadrer un capteur Zeek passif (journaux de métadonnées réseau) sur VM Ubuntu Server 24.04 LTS dans un périmètre autorisé.

## 1. Hors-Production (Lab / Test / POC)

1. Obtenir l’autorisation d’analyse (propriétaire, interface INTERFACE_AUTORISEE, réseaux LOCAL_NET_AUTORISE, rétention des logs).
   👉 Explication : Zeek enregistre des métadonnées de connexions, DNS, HTTP, TLS; elles sont sensibles. Les valeurs en majuscules sont des placeholders à remplacer.

2. Contrôler les ressources :
   ```bash
   cat /etc/os-release
   nproc
   free -h
   ip -br link
   df -h /opt /var
   ```
   👉 Explication : Zeek est gourmand en CPU/RAM et disque selon le débit; prévoir une interface de capture dédiée.

3. Choisir le mode d’installation.
   👉 Explication : Ubuntu 24.04 : paquets binaires OBS de l’éditeur (ligne LTS `zeek-8.0`, préfixe `/opt/zeek`); vérifier la ligne publiée. Le dépôt Ubuntu peut contenir une version plus ancienne.

4. Noter les limites.
   👉 Explication : Mode traité : capteur standalone passif. Les clusters, la haute disponibilité et tout blocage ne sont pas couverts. Zeek ne déchiffre pas TLS. AppArmor : en cas de refus, `sudo journalctl -k | grep DENIED`.

## 2. Production — Contrôles

Faire valider architecture (SPAN/TAP), volumétrie et propriétaire des journaux.

## 3. Production — Sécurité

- Capture passive uniquement.
- Interface de capture sans IP de service si possible.

## Validation et retour arrière

- **Validation** : Autorisation tracée, mode d’installation choisi, limites comprises.
- **Retour arrière** : Aucun changement système à annuler.

## Si le problème n’est pas résolu

- [Zeek — documentation officielle](https://docs.zeek.org/en/master/install.html)
- [Fiche d’entrée du logiciel](/01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-zeek)
- [Étape suivante du guide](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/zeek/fiche-simple-vm-ubuntu-24-04-zeek-installer)