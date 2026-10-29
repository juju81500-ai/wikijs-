---
title: "Fiche Simple - VM Ubuntu 24.04 OpenVPN Valider"
description: "Recetter le serveur avec un client pilote avant ouverture aux utilisateurs."
published: true
date: 2026-10-29T20:59:58Z
tags: ["openvpn", "ubuntu24-04", "vie-du-logiciel", "valider"]
editor: markdown
dateCreated: 2026-10-29T20:59:58Z
dateModified: 2026-10-29T20:59:58Z
---

# Fiche_Simple_-_VM_Ubuntu_24.04_OpenVPN_Valider

- **Environnement** : VM Ubuntu 24.04 dédiée à OpenVPN Community Edition (serveur)
- **OS / Version** : Ubuntu 24.04 LTS Noble; version des dépôts à vérifier sur l'hôte
- **Catégorie** : OpenVPN Community Edition / valider
- **Tags** : `openvpn`, `ubuntu24-04`, `vie-du-logiciel`, `valider`

---

## Problème précis à résoudre

Recetter le serveur avec un client pilote avant ouverture aux utilisateurs.

## 1. Hors-Production (Lab / Test / POC)

1. Démarrer l'instance et contrôler son état :
   ```bash
   sudo systemctl enable --now openvpn-server@server
   systemctl status openvpn-server@server --no-pager
   ip -br address show tun0
   ```
   👉 Explication : server est le nom du fichier server.conf (à adapter); l'interface tun0 doit exister (nom pouvant varier selon la configuration).

2. Vérifier l'écoute UDP :
   ```bash
   sudo ss -ulnp | grep openvpn
   ```
   👉 Explication : Le port VPN_UDP_PORT doit être à l'écoute.

3. Connecter un client pilote puis lire le journal :
   ```bash
   sudo journalctl -u openvpn-server@server -n 50 --no-pager
   ```
   👉 Explication : Confirmer la connexion TLS, l'authentification du certificat pilote et l'accès aux seules routes autorisées; tester aussi qu'un certificat révoqué est refusé.

## 2. Production — Contrôles

Consigner le résultat de la recette, l'heure et l'approbation du propriétaire du service.

## 3. Production — Sécurité

- Supprimer le client pilote et son certificat à la fin du test s'il n'est pas destiné à la production.

## Validation et retour arrière

- **Validation** : Client pilote connecté, routes conformes, certificat révoqué refusé.
- **Retour arrière** : sudo systemctl disable --now openvpn-server@server puis restaurer la configuration antérieure.

## Si le problème n'est pas résolu

- [Étape suivante du guide](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/openvpn/fiche-simple-vm-ubuntu-24-04-openvpn-sauvegarder-restaurer)
- [Fiche d'entrée du logiciel](/01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-openvpn)
- [OpenVPN Community — documentation officielle](https://openvpn.net/community-resources/)
- [OpenVPN — manuel de référence 2.6](https://openvpn.net/community-resources/reference-manual-for-openvpn-2-6/)