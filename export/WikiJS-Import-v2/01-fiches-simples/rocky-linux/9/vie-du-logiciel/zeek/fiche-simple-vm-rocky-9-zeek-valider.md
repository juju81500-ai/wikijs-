---
title: "Fiche Simple - VM Rocky 9 Zeek Valider"
description: "Recetter le capteur Zeek : processus, journaux et pertes de paquets."
published: true
date: 2026-10-29T20:59:32Z
tags: ["zeek", "rocky9", "vie-du-logiciel", "valider"]
editor: markdown
dateCreated: 2026-10-29T20:59:32Z
dateModified: 2026-10-29T20:59:32Z
---

# Fiche_Simple_-_VM_Rocky_9_Zeek_Valider

- **Environnement** : VM Rocky Linux 9 dédiée à Zeek
- **OS / Version** : Rocky Linux 9 (compatible RHEL 9); version des paquets à vérifier sur l’hôte
- **Catégorie** : Zeek / validation
- **Tags** : `zeek`, `rocky9`, `vie-du-logiciel`, `valider`

---

## Problème précis à résoudre

Recetter le capteur Zeek : processus, journaux et pertes de paquets.

## 1. Hors-Production (Lab / Test / POC)

1. Rejouer un pcap de recette autorisé :
   ```bash
   sudo podman run --rm -v /var/lib/zeek-lab/pcap:/pcap:ro,Z -v /var/lib/zeek-lab/logs:/logs:Z -w /logs docker.io/zeek/zeek:lts zeek -C -r /pcap/TICKET.pcap
   ```
   👉 Explication : Même chemin que la configuration, sans toucher au réseau.

2. Contrôler les journaux produits :
   ```bash
   sudo ls -l /var/lib/zeek-lab/logs
   sudo head -n 12 /var/lib/zeek-lab/logs/conn.log
   ```
   👉 Explication : Présence de conn.log avec des lignes non vides.

3. Vérifier l’absence de conteneur résiduel :
   ```bash
   sudo podman ps -a
   ```
   👉 Explication : Aucun conteneur Zeek ne doit rester actif sans besoin.

## 2. Production — Contrôles

Archiver version, date et extrait des journaux de recette.

## 3. Production — Sécurité

- Tests sur trafic autorisé uniquement.

## Validation et retour arrière

- **Validation** : Les journaux de connexion sont produits et cohérents avec le trafic de test.
- **Retour arrière** : Arrêter le capteur ou le conteneur de test et nettoyer les fichiers de test.

## Si le problème n’est pas résolu

- [Zeek — documentation officielle](https://docs.zeek.org/en/master/install.html)
- [Fiche d’entrée du logiciel](/01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-zeek)
- [Étape suivante du guide](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/zeek/fiche-simple-vm-rocky-9-zeek-sauvegarder-restaurer)
- [Étape précédente du guide](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/zeek/fiche-simple-vm-rocky-9-zeek-securiser)