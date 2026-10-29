---
title: "Fiche Simple - VM Rocky 9 OpenVPN Installer"
description: "Installer OpenVPN Community Edition et l'outil PKI depuis les dépôts de Rocky Linux 9 (EPEL) sans démarrer de service non configuré."
published: true
date: 2026-10-29T20:59:58Z
tags: ["openvpn", "rocky9", "vie-du-logiciel", "installer"]
editor: markdown
dateCreated: 2026-10-29T20:59:58Z
dateModified: 2026-10-29T20:59:58Z
---

# Fiche_Simple_-_VM_Rocky_9_OpenVPN_Installer

- **Environnement** : VM Rocky Linux 9 dédiée à OpenVPN Community Edition (serveur)
- **OS / Version** : Rocky Linux 9; paquets openvpn et easy-rsa issus d'EPEL, version à vérifier
- **Catégorie** : OpenVPN Community Edition / installer
- **Tags** : `openvpn`, `rocky9`, `vie-du-logiciel`, `installer`

---

## Problème précis à résoudre

Installer OpenVPN Community Edition et l'outil PKI depuis les dépôts de Rocky Linux 9 (EPEL) sans démarrer de service non configuré.

## 1. Hors-Production (Lab / Test / POC)

1. Installer les paquets :
   ```bash
   sudo dnf install epel-release
   dnf info openvpn easy-rsa
   sudo dnf install openvpn easy-rsa
   openvpn --version
   ```
   👉 Explication : Consigner la version installée; EPEL est un dépôt communautaire à faire approuver avant usage en production.

2. Identifier les unités systemd livrées :
   ```bash
   systemctl list-unit-files | grep -i openvpn
   ```
   👉 Explication : Les instances serveur se lancent avec openvpn-server@NOM.service (NOM = fichier NOM.conf du dossier /etc/openvpn/server); vérifier le nom exact sur l'hôte.

## 2. Production — Contrôles

Consigner version, dépôt d'origine et unités disponibles; prévoir un client pilote.

## 3. Production — Sécurité

- Ne pas activer ni démarrer l'unité avant d'avoir une configuration validée; conserver la clé de CA hors ligne.

## Validation et retour arrière

- **Validation** : openvpn --version répond et l'unité openvpn-server@.service est présente.
- **Retour arrière** : Désinstaller : sudo dnf remove openvpn easy-rsa (aucune configuration n'est encore créée).

## Si le problème n'est pas résolu

- [Étape suivante du guide](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/openvpn/fiche-simple-vm-rocky-9-openvpn-configurer)
- [Fiche d'entrée du logiciel](/01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-openvpn)
- [OpenVPN Community — documentation officielle](https://openvpn.net/community-resources/)
- [OpenVPN — manuel de référence 2.6](https://openvpn.net/community-resources/reference-manual-for-openvpn-2-6/)