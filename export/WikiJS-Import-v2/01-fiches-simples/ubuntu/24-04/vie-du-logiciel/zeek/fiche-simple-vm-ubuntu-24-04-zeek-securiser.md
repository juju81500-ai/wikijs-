---
title: "Fiche Simple - VM Ubuntu 24.04 Zeek Securiser"
description: "Durcir le capteur Zeek : droits, privilèges, journaux et exposition."
published: true
date: 2026-10-29T20:59:32Z
tags: ["zeek", "ubuntu24.04", "vie-du-logiciel", "securiser"]
editor: markdown
dateCreated: 2026-10-29T20:59:32Z
dateModified: 2026-10-29T20:59:32Z
---

# Fiche_Simple_-_VM_Ubuntu_24.04_Zeek_Securiser

- **Environnement** : VM Ubuntu Server 24.04 LTS dédiée à Zeek
- **OS / Version** : Ubuntu Server 24.04 LTS (Noble Numbat); version des paquets à vérifier sur l’hôte
- **Catégorie** : Zeek / sécurisation
- **Tags** : `zeek`, `ubuntu24.04`, `vie-du-logiciel`, `securiser`

---

## Problème précis à résoudre

Durcir le capteur Zeek : droits, privilèges, journaux et exposition.

## 1. Hors-Production (Lab / Test / POC)

1. Créer un compte non privilégié pour consulter les logs :
   ```bash
   sudo groupadd --system zeeklogs
   sudo usermod -aG zeeklogs NOM_ANALYSTE
   sudo chgrp -R zeeklogs /opt/zeek/logs
   sudo chmod -R o-rwx /opt/zeek/logs
   ```
   👉 Explication : Séparation capture/lecture; NOM_ANALYSTE est à remplacer. Se reconnecter pour appliquer le groupe.

2. Limiter les capacités de capture :
   ```bash
   getcap /opt/zeek/bin/zeek /opt/zeek/bin/capstats 2>/dev/null
   ```
   👉 Explication : Les paquets OBS peuvent poser des capacités sur certains binaires; vérifier et documenter toute capacité (`libcap2-bin`), ne pas en ajouter sans besoin.

3. Vérifier l’absence d’écoute inutile :
   ```bash
   ss -tulpn | grep -i zeek || echo "aucun port zeek ouvert"
   ```
   👉 Explication : Un capteur standalone n’écoute pas.

## 2. Production — Contrôles

Revue trimestrielle des comptes, des capacités et de la rétention.

## 3. Production — Sécurité

- Transmettre les journaux vers un collecteur approuvé par canal chiffré (non détaillé).
- Aucun secret en clair dans la configuration.
- AppArmor : en cas de refus, `sudo journalctl -k | grep DENIED`.

## Validation et retour arrière

- **Validation** : Droits restrictifs, aucun port ouvert, privilèges minimaux.
- **Retour arrière** : Restaurer permissions et appartenances consignées.

## Si le problème n’est pas résolu

- [Zeek — documentation officielle](https://docs.zeek.org/en/master/install.html)
- [Fiche d’entrée du logiciel](/01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-zeek)
- [Étape suivante du guide](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/zeek/fiche-simple-vm-ubuntu-24-04-zeek-valider)
- [Étape précédente du guide](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/zeek/fiche-simple-vm-ubuntu-24-04-zeek-configurer)