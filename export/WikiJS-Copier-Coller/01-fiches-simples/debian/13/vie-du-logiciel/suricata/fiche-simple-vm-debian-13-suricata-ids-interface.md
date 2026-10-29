# Fiche_Simple_-_VM_Debian_13_Suricata_IDS_Interface.md

- **Environnement** : VM Debian 13 avec une interface de capture
- **OS / Version** : Debian 13 Trixie; Suricata 8.0.7 et suricata-update (Debian Backports)
- **Catégorie** : detection reseau / interface

---

## Problème précis à résoudre

Repérer l'interface miroir et limiter ce qu'elle observe.

## 1. Hors-Production (Lab / Test / POC)

1. Lister les adresses et les propriétés des interfaces :
   ```bash
   ip -br address
   ip -d link show
   ```
   👉 Explication : on identifie l'interface de capture et on vérifie qu'elle est séparée de la gestion.

2. Documenter le sens du miroir et les VLAN visibles avec l'équipe réseau.
   👉 Explication : l'interface ne doit recevoir que le trafic approuvé; éviter les ports de gestion et d'hyperviseur.

3. Sur une VM, faire valider par l'équipe virtualisation que le pont ou vSwitch délivre le trafic miroir et autorise le mode promiscuous.
   👉 Explication : une interface virtuelle ne voit pas spontanément les flux des autres VM.

## 2. Production — Contrôles

Faire valider le schéma du miroir par le propriétaire du réseau et conserver ce schéma.

## 3. Production — Sécurité

- N'observer que le trafic approuvé.
- Ne pas capturer sur l'interface de gestion.

## Validation et retour arrière

- **Validation** : L'interface de capture est identifiée et distincte de la gestion.
- **Retour arrière** : Aucune modification; retirer le miroir côté réseau si la validation échoue.

## Si le problème n'est pas résolu

- [Suricata — AF_PACKET](https://docs.suricata.io/en/latest/capture-hardware/af-packet.html)
- [Suricata — démarrage rapide](https://docs.suricata.io/en/latest/quickstart.html)
- [Guide complet Suricata Debian 13](/02-fiches-completes/debian/13/installation-deploiement/71-deploiement-suricata-8-debian-13-backports#3-identifier-linterface-et-limiter-la-visibilite)