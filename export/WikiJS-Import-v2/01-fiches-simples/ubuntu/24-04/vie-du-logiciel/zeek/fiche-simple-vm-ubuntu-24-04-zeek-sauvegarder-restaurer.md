---
title: "Fiche Simple - VM Ubuntu 24.04 Zeek Sauvegarder Restaurer"
description: "Sauvegarder et restaurer la configuration de Zeek."
published: true
date: 2026-10-29T20:59:32Z
tags: ["zeek", "ubuntu24.04", "vie-du-logiciel", "sauvegarder-restaurer"]
editor: markdown
dateCreated: 2026-10-29T20:59:32Z
dateModified: 2026-10-29T20:59:32Z
---

# Fiche_Simple_-_VM_Ubuntu_24.04_Zeek_Sauvegarder_Restaurer

- **Environnement** : VM Ubuntu Server 24.04 LTS dédiée à Zeek
- **OS / Version** : Ubuntu Server 24.04 LTS (Noble Numbat); version des paquets à vérifier sur l’hôte
- **Catégorie** : Zeek / sauvegarde et restauration
- **Tags** : `zeek`, `ubuntu24.04`, `vie-du-logiciel`, `sauvegarder-restaurer`

---

## Problème précis à résoudre

Sauvegarder et restaurer la configuration de Zeek.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder la configuration :
   ```bash
   sudo tar -czf /var/tmp/zeek-config-DATE.tar.gz /opt/zeek/etc /opt/zeek/share/zeek/site
   sudo chmod 0600 /var/tmp/zeek-config-DATE.tar.gz
   ```
   👉 Explication : Inclut `node.cfg`, `networks.cfg`, `zeekctl.cfg` et les scripts locaux; DATE est à remplacer. Les logs suivent la politique de rétention.

2. Restaurer :
   ```bash
   sudo /opt/zeek/bin/zeekctl stop
   sudo tar -xzf /var/tmp/zeek-config-DATE.tar.gz -C /
   sudo /opt/zeek/bin/zeekctl check
   sudo /opt/zeek/bin/zeekctl deploy
   ```
   👉 Explication : Remet la configuration puis la contrôle avant redéploiement.

## 2. Production — Contrôles

Tester la restauration en lab.

## 3. Production — Sécurité

- Archive en 0600, chiffrée hors VM.

## Validation et retour arrière

- **Validation** : `zeekctl check` réussit et `zeekctl status` indique running.
- **Retour arrière** : Restaurer l’archive précédente connue bonne.

## Si le problème n’est pas résolu

- [Zeek — documentation officielle](https://docs.zeek.org/en/master/install.html)
- [Fiche d’entrée du logiciel](/01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-zeek)
- [Étape suivante du guide](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/zeek/fiche-simple-vm-ubuntu-24-04-zeek-mise-a-jour-retour-arriere)
- [Étape précédente du guide](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/zeek/fiche-simple-vm-ubuntu-24-04-zeek-valider)