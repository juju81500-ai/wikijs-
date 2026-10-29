---
title: "Fiche Simple - VM Debian 13 Kea Limites"
description: "Savoir ce qui n'a pas été éprouvé et le valider dans le VLAN de test cible."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "kea", "dhcpv4", "isc", "reseau"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_Kea_Limites.md

- **Environnement** : VM Debian 13 serveur DHCPv4 sur un VLAN de test isolé
- **OS / Version** : Debian 13 Trixie x86-64; ISC Kea (canal stable)
- **Catégorie** : réseau / DHCP
- **Tags** : `debian13`, `kea`, `dhcpv4`, `isc`, `reseau`

---

## Problème précis à résoudre

Savoir ce qui n'a pas été éprouvé et le valider dans le VLAN de test cible.

## 1. Hors-Production (Lab / Test / POC)

1. Relire la liste des points à éprouver : installation Cloudsmith, attribution DHCP réelle, restauration des baux.
   👉 Explication : la procédure vient du manuel Kea et n'a pas été exécutée sur Debian 13 dans ce workspace.

2. Vérifier la version des paquets installés :
   ```bash
   dpkg -l | grep -i kea
   ```
   👉 Explication : confirme que les versions correspondent à celles du manuel consulté.

3. Rejouer l'attribution de bail dans le VLAN de test et consigner le résultat.
   👉 Explication : transforme les hypothèses en résultats vérifiés.

## 2. Production — Contrôles

Consigner dans le dossier de changement les tests effectués et les écarts.

## 3. Production — Sécurité

- Ne pas déclarer le service prêt pour la production sans test réel.
- Tester une restauration de baux hors production.

## Validation et retour arrière

- **Validation** : Résultats de test consignés pour chaque point listé.
- **Retour arrière** : Aucune modification à annuler.

## Si le problème n'est pas résolu

- [ISC Kea — Installation](https://kea.readthedocs.io/en/latest/arm/install.html)
- [ISC Kea — Serveur DHCPv4](https://kea.readthedocs.io/en/latest/arm/dhcp4-srv.html)
- [Guide complet Kea DHCPv4 Debian 13](/02-fiches-completes/debian/13/installation-deploiement/64-deploiement-kea-dhcpv4-debian-13#8-limites-de-validation)