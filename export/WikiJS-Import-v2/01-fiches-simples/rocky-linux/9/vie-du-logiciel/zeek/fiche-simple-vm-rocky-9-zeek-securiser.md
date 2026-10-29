---
title: "Fiche Simple - VM Rocky 9 Zeek Securiser"
description: "Durcir le capteur Zeek : droits, privilèges, journaux et exposition."
published: true
date: 2026-10-29T20:59:32Z
tags: ["zeek", "rocky9", "vie-du-logiciel", "securiser"]
editor: markdown
dateCreated: 2026-10-29T20:59:32Z
dateModified: 2026-10-29T20:59:32Z
---

# Fiche_Simple_-_VM_Rocky_9_Zeek_Securiser

- **Environnement** : VM Rocky Linux 9 dédiée à Zeek
- **OS / Version** : Rocky Linux 9 (compatible RHEL 9); version des paquets à vérifier sur l’hôte
- **Catégorie** : Zeek / sécurisation
- **Tags** : `zeek`, `rocky9`, `vie-du-logiciel`, `securiser`

---

## Problème précis à résoudre

Durcir le capteur Zeek : droits, privilèges, journaux et exposition.

## 1. Hors-Production (Lab / Test / POC)

1. Figer l’image par digest :
   ```bash
   sudo podman image inspect docker.io/zeek/zeek:lts --format "{{.Digest}}"
   ```
   👉 Explication : Déployer ensuite `docker.io/zeek/zeek@sha256:DIGEST_RELEVE` (à remplacer) pour éviter les changements imprévus.

2. Restreindre les logs :
   ```bash
   sudo chmod -R o-rwx /var/lib/zeek-lab
   sudo ls -ld /var/lib/zeek-lab/logs
   ```
   👉 Explication : Les journaux contiennent des métadonnées sensibles.

3. Contrôler les privilèges du conteneur :
   ```bash
   sudo podman ps --format "{{.Names}} {{.Command}}"
   ```
   👉 Explication : Ne donner que NET_RAW et NET_ADMIN; ne pas utiliser `--privileged`.

## 2. Production — Contrôles

Revue trimestrielle des comptes, des capacités et de la rétention.

## 3. Production — Sécurité

- Transmettre les journaux vers un collecteur approuvé par canal chiffré (non détaillé).
- Aucun secret en clair dans la configuration.
- SELinux : rester en Enforcing; en cas de refus, `sudo ausearch -m avc -ts recent`.

## Validation et retour arrière

- **Validation** : Droits restrictifs, aucun port ouvert, privilèges minimaux.
- **Retour arrière** : Restaurer permissions et appartenances consignées.

## Si le problème n’est pas résolu

- [Zeek — documentation officielle](https://docs.zeek.org/en/master/install.html)
- [Fiche d’entrée du logiciel](/01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-zeek)
- [Étape suivante du guide](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/zeek/fiche-simple-vm-rocky-9-zeek-valider)
- [Étape précédente du guide](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/zeek/fiche-simple-vm-rocky-9-zeek-configurer)