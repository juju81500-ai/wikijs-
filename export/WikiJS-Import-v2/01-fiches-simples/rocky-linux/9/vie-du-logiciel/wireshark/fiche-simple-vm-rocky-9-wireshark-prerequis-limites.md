---
title: "Fiche Simple - VM Rocky 9 Wireshark Prerequis Limites"
description: "Cadrer l’usage autorisé de Wireshark/TShark sur VM Rocky Linux 9 : analyse de fichiers et captures bornées, sans capture non autorisée."
published: true
date: 2026-10-29T20:58:07Z
tags: ["wireshark", "rocky9", "vie-du-logiciel", "prerequis-limites"]
editor: markdown
dateCreated: 2026-10-29T20:58:07Z
dateModified: 2026-10-29T20:58:07Z
---

# Fiche_Simple_-_VM_Rocky_9_Wireshark_Prerequis_Limites

- **Environnement** : VM Rocky Linux 9 dédiée à Wireshark
- **OS / Version** : Rocky Linux 9 (compatible RHEL 9); version des paquets à vérifier sur l’hôte
- **Catégorie** : Wireshark / prérequis et limites
- **Tags** : `wireshark`, `rocky9`, `vie-du-logiciel`, `prerequis-limites`

---

## Problème précis à résoudre

Cadrer l’usage autorisé de Wireshark/TShark sur VM Rocky Linux 9 : analyse de fichiers et captures bornées, sans capture non autorisée.

## 1. Hors-Production (Lab / Test / POC)

1. Obtenir l’autorisation de capture ou d’analyse (ticket TICKET, propriétaire des données, durée, interface INTERFACE_AUTORISEE).
   👉 Explication : Une capture contient souvent des données personnelles ou des identifiants; TICKET et INTERFACE_AUTORISEE sont des placeholders à remplacer.

2. Contrôler les ressources et l’affichage :
   ```bash
   cat /etc/os-release
   free -h
   df -h /var/tmp
   echo "${XDG_SESSION_TYPE:-aucune session graphique}"
   ```
   👉 Explication : L’interface graphique demande une session X11/Wayland; sur un serveur sans bureau, utiliser TShark en ligne de commande. Le disque doit accueillir les captures.

3. Noter les limites.
   👉 Explication : Wireshark ne déchiffre pas TLS sans clés fournies légalement; une VM ne voit que le trafic de son vSwitch; les dissecteurs traitent des données non fiables, d’où la nécessité de rester à jour. La version fournie par Rocky 9 peut être plus ancienne que la version amont : vérifier la version publiée.

## 2. Production — Contrôles

Valider par écrit le périmètre, le lieu de stockage des .pcap et la durée de conservation.

## 3. Production — Sécurité

- Ne capturer que des réseaux autorisés.
- Ne pas ouvrir de capture d’origine inconnue sur un poste sensible.

## Validation et retour arrière

- **Validation** : Autorisation, ressources et limites consignées.
- **Retour arrière** : Aucune modification système; archiver les notes de cadrage.

## Si le problème n’est pas résolu

- [Wireshark — documentation officielle](https://www.wireshark.org/docs/)
- [Fiche d’entrée du logiciel](/01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-wireshark)
- [Étape suivante du guide](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/wireshark/fiche-simple-vm-rocky-9-wireshark-installer)