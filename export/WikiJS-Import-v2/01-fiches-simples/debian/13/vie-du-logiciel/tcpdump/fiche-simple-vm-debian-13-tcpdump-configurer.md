---
title: "Fiche Simple - VM Debian 13 tcpdump Configurer"
description: "Réaliser une capture finie avec filtre, taille et stockage restreint."
published: true
date: 2026-10-29T20:35:43Z
tags: ["tcpdump", "debian13", "vie-du-logiciel", "configurer"]
editor: markdown
dateCreated: 2026-10-29T20:35:43Z
dateModified: 2026-10-29T20:35:43Z
---

# Fiche_Simple_-_VM_Debian_13_tcpdump_Configurer

- **Environnement** : VM Debian 13 dédiée à tcpdump
- **OS / Version** : Debian 13 Trixie; version des dépôts à vérifier sur l’hôte
- **Catégorie** : tcpdump / configurer
- **Tags** : `tcpdump`, `debian13`, `vie-du-logiciel`, `configurer`

---

## Problème précis à résoudre

Réaliser une capture finie avec filtre, taille et stockage restreint.

## 1. Hors-Production (Lab / Test / POC)

1. Créer un répertoire accessible à root uniquement :
   ```bash
   sudo install -d -o root -g root -m 0700 /var/tmp/tcpdump-lab
   ```
   👉 Explication : Utiliser un volume avec espace disponible et politique de conservation approuvée.

2. Capturer au plus 100 paquets pendant 60 secondes avec un filtre d’exemple :
   ```bash
   INTERFACE_CAPTURE=INTERFACE_CAPTURE
   sudo timeout --signal=INT 60 tcpdump -i "$INTERFACE_CAPTURE" -nn -s 96 -c 100 -w /var/tmp/tcpdump-lab/capture.pcap icmp or arp
   ```
   👉 Explication : Remplacer INTERFACE_CAPTURE par l’interface autorisée. Le filtre ICMP/ARP est un exemple à adapter; -s 96 limite les octets conservés.

3. Pour une observation limitée sans fichier, examiner quelques paquets :
   ```bash
   sudo tcpdump -i INTERFACE_CAPTURE -nn -c 20 tcp port 443
   ```
   👉 Explication : Remplacer INTERFACE_CAPTURE et le filtre; la commande s’arrête après 20 paquets.

## 2. Production — Contrôles

Toute capture persistante requiert fenêtre, stockage, rotation, quotas et propriétaire; préférer une capture finie.

## 3. Production — Sécurité

- Ne pas capturer des mots de passe ou charges utiles sans besoin documenté et autorisé.

## Validation et retour arrière

- **Validation** : Pcap produit dans le répertoire privé, capture terminée par durée/compte.
- **Retour arrière** : restaurer la configuration antérieure vérifiée et arrêter le service ou la capture si la recette échoue; consigner le changement.

## Si le problème n’est pas résolu

- [tcpdump — documentation officielle](https://www.tcpdump.org/manpages/tcpdump.1.html)
- [Étape suivante du guide](/01-fiches-simples/debian/13/vie-du-logiciel/tcpdump/fiche-simple-vm-debian-13-tcpdump-securiser)