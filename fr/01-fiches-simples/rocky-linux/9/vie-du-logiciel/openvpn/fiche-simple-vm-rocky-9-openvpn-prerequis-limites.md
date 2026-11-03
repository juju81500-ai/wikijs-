---
title: "Fiche Simple - VM Rocky 9 OpenVPN Prerequis Limites"
description: "Valider le cadre avant d'installer un serveur OpenVPN Community Edition : OS, réseau, PKI, périmètre."
published: true
date: 2026-11-03T09:36:13Z
tags: ["openvpn", "rocky9", "vie-du-logiciel", "prerequis-limites"]
editor: markdown
dateCreated: 2026-11-03T09:36:13Z
dateModified: 2026-11-03T09:36:13Z
---

# Fiche_Simple_-_VM_Rocky_9_OpenVPN_Prerequis_Limites

- **Environnement** : [[Glossary:VM]] Rocky Linux 9 dédiée à OpenVPN Community Edition (serveur)
- **OS / Version** : Rocky Linux 9; paquets openvpn et easy-rsa issus d'EPEL, version à vérifier
- **Catégorie** : OpenVPN Community Edition / prérequis et limites
- **Tags** : `openvpn`, `rocky9`, `vie-du-logiciel`, `prerequis-limites`

---

## Problème précis à résoudre

Valider le cadre avant d'installer un serveur OpenVPN Community Edition : OS, réseau, [[Glossary:PKI]], périmètre.

## 1. Hors-Production (Lab / Test / POC)

1. Relever l'OS, le noyau et l'adresse [[Glossary:IP]] de l'hôte :
   ```bash
   cat /etc/os-release
   uname -r
   ip -br address
   ip route
   ```
   👉 Explication : Confirmer que l'OS est Rocky Linux 9 à jour, EPEL activable (le paquet openvpn n'est pas dans les dépôts de base : vérifier avec dnf info openvpn) et noter l'IP publique ou NATée à joindre depuis les clients.

2. Contrôler l'heure et le [[Glossary:DNS]] :
   ```bash
   timedatectl
   resolvectl status 2>/dev/null || cat /etc/resolv.conf
   ```
   👉 Explication : Les certificats dépendent de l'heure : [[Glossary:NTP]] synchronisé obligatoire.

3. Consigner les valeurs à décider avant de continuer :
   👉 Explication : VPN_NETWORK / VPN_NETMASK (réseau du tunnel), VPN_UDP_PORT (port [[Glossary:UDP]]), SERVER_FQDN (nom public du serveur), PKI approuvée ([[Glossary:CA]] hors ligne). Ces valeurs en majuscules sont à remplacer par le plan validé.

## 2. Production — Contrôles

Valider avec le propriétaire du service : utilisateurs, réseaux joignables, journalisation, fenêtre et accès de secours hors bande. Limites : édition Community uniquement (pas Access Server); pas de haute disponibilité ni de gestion de comptes intégrée.

## 3. Production — Sécurité

- La clé privée de la CA ne doit jamais résider sur le serveur [[Glossary:VPN]] exposé.
- Aucune ouverture de port avant la fin de la recette.

## Validation et retour arrière

- **Validation** : Le tableau de décisions (réseau, port, [[Glossary:FQDN]], PKI) est rempli et approuvé.
- **Retour arrière** : Aucun changement n'a été fait à ce stade : rien à restaurer.

## Si le problème n'est pas résolu

- [Étape suivante du guide](/fr/01-fiches-simples/rocky-linux/9/vie-du-logiciel/openvpn/fiche-simple-vm-rocky-9-openvpn-installer)
- [Fiche d'entrée du logiciel](/fr/01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-openvpn)
- [OpenVPN Community — documentation officielle](https://openvpn.net/community-resources/)
- [OpenVPN — manuel de référence 2.6](https://openvpn.net/community-resources/reference-manual-for-openvpn-2-6/)