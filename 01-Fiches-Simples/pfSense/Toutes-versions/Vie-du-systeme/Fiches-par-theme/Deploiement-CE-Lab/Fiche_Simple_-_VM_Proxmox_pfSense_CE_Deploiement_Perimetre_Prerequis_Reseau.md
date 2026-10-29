# Fiche_Simple_-_VM_Proxmox_pfSense_CE_Deploiement_Perimetre_Prerequis_Reseau.md

- **Environnement** : VM pfSense CE en laboratoire sur Proxmox VE, deux interfaces (WAN et LAN isolés)
- **OS / Version** : pfSense Community Edition 2.9.0 (VM x86-64 sur Proxmox VE)
- **Catégorie** : pare-feu et routage
- **Tags** : `pfsense`, `ce`, `proxmox`, `firewall`, `lab`

---

## Problème précis à résoudre

Préparer un laboratoire pfSense CE isolé avant de créer la VM.

## 1. Hors-Production (Lab / Test / POC)

1. Dans Proxmox : **Datacenter > nœud > Système > Réseau > Créer > Linux Bridge**, créer `vmbr-pfsense-wan` puis `vmbr-pfsense-lan`.
   👉 Explication : deux ponts distincts: le LAN ne doit être relié ni au réseau de gestion Proxmox ni à un segment de production.

2. En ligne de commande sur l'hôte Proxmox, contrôler les ponts :
   ```bash
   ip -br link show type bridge
   ```
   👉 Explication : confirme que les deux ponts existent et sont actifs.

3. Vérifier que le sous-réseau LAN initial `192.168.1.0/24` ne chevauche aucun réseau de l'hôte ou du site :
   ```bash
   ip -br address
   ```
   👉 Explication : un chevauchement casserait l'accès; choisir un autre LAN de lab si nécessaire.

4. S'assurer d'un poste ou VM d'administration et d'un accès amont contrôlé sur le pont WAN pour l'installateur en ligne.
   👉 Explication : si le test n'a pas besoin d'Internet, isoler aussi le WAN après installation.

## 2. Production — Contrôles

Cette fiche ne remplace ni une conception de production, ni un guide d'appliance Netgate, ni la haute disponibilité; ouvrir un changement dédié pour la production.

## 3. Production — Sécurité

- Ne jamais brancher les deux interfaces de la VM sur le même réseau.
- Ne pas raccorder le laboratoire à un réseau de production.

## Validation et retour arrière

- **Validation** : deux ponts isolés existent et aucun chevauchement d'adresses n'est détecté.
- **Retour arrière** : supprimer les deux ponts de test dans **Réseau** s'ils ne portent aucune VM, puis appliquer la configuration réseau.

## Si le problème n'est pas résolu

- [Netgate — Proxmox VE](https://docs.netgate.com/pfsense/en/latest/recipes/virtualize-proxmox-ve.html)
- [Netgate — pfSense CE 2.9.0](https://docs.netgate.com/pfsense/en/latest/releases/2-9-0.html)
- [Guide complet](../../../../../../02-Fiches-Completes/pfSense/Toutes-versions/Installation-Deploiement/70_Deploiement_pfSense_CE_2.9.0_Proxmox_Lab.md#1-perimetre-prerequis-et-reseau)
