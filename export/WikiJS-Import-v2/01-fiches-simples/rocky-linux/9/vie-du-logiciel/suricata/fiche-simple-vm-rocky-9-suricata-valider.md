---
title: "Fiche Simple - VM Rocky 9 Suricata Valider"
description: "Recetter le capteur : moteur actif, règles chargées, événements écrits."
published: true
date: 2026-10-29T20:58:45Z
tags: ["suricata", "rocky9", "vie-du-logiciel", "valider"]
editor: markdown
dateCreated: 2026-10-29T20:58:45Z
dateModified: 2026-10-29T20:58:45Z
---

# Fiche_Simple_-_VM_Rocky_9_Suricata_Valider

- **Environnement** : VM Rocky Linux 9 dédiée à Suricata
- **OS / Version** : Rocky Linux 9 (compatible RHEL 9); version des paquets à vérifier sur l’hôte
- **Catégorie** : Suricata / validation
- **Tags** : `suricata`, `rocky9`, `vie-du-logiciel`, `valider`

---

## Problème précis à résoudre

Recetter le capteur : moteur actif, règles chargées, événements écrits.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler service et statistiques :
   ```bash
   systemctl is-active suricata
   sudo tail -n 5 /var/log/suricata/stats.log
   ```
   👉 Explication : Le service doit être actif et les compteurs de paquets doivent progresser.

2. Générer un événement de test sur un réseau autorisé :
   ```bash
   curl -s http://testmynids.org/uid/index.html -o /dev/null
   ```
   👉 Explication : Requête inoffensive vers un site de test d’IDS; elle ne doit être faite que si la sortie Internet est autorisée et si la règle de test est chargée. Sinon utiliser un serveur de test interne.

3. Lire l’alerte :
   ```bash
   sudo jq "select(.event_type==\"alert\")" /var/log/suricata/eve.json | tail -n 20
   ```
   👉 Explication : Affiche les alertes JSON; sans alerte, vérifier la position de la capture et les règles.

4. Rejouer un fichier pcap autorisé hors ligne (option) :
   ```bash
   mkdir -p /tmp/suri-test && sudo suricata -r /var/tmp/TICKET.pcap -l /tmp/suri-test -c /etc/suricata/suricata.yaml
   ```
   👉 Explication : Analyse un fichier sans toucher au réseau; TICKET est à remplacer.

## 2. Production — Contrôles

Archiver la preuve (version, alerte de test, horodatage).

## 3. Production — Sécurité

- Ne générer que des événements de test inoffensifs.

## Validation et retour arrière

- **Validation** : Service actif, statistiques en hausse, alerte de test présente dans eve.json.
- **Retour arrière** : Arrêter le service si nécessaire (`sudo systemctl stop suricata`) et nettoyer `/tmp/suri-test`.

## Si le problème n’est pas résolu

- [Suricata — documentation officielle](https://docs.suricata.io/en/latest/)
- [Fiche d’entrée du logiciel](/01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-suricata)
- [Étape suivante du guide](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/suricata/fiche-simple-vm-rocky-9-suricata-sauvegarder-restaurer)
- [Étape précédente du guide](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/suricata/fiche-simple-vm-rocky-9-suricata-securiser)