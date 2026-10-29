---
title: "Fiche Simple - VM Multi-OS Reseau Diagnostic Lien Interface"
description: "Confirmer que l'interface est active et identifier le gestionnaire réseau qui la pilote."
published: true
date: 2026-10-29T19:39:36Z
tags: ["reseau", "diagnostic", "multi-os", "depannage"]
editor: markdown
dateCreated: 2026-10-29T19:39:36Z
dateModified: 2026-10-29T19:39:36Z
---

# Fiche_Simple_-_VM_Multi-OS_Reseau_Diagnostic_Lien_Interface.md

- **Environnement** : VM, poste, serveur, LXC Proxmox ou hôte Docker (Linux ou Windows)
- **OS / Version** : Debian 12/13, Ubuntu 24.04/26.04, Rocky Linux 9, Alpine Linux, Windows 10/11, Windows Server 2022/2025
- **Catégorie** : réseau / couche 1-2
- **Tags** : `reseau`, `diagnostic`, `multi-os`, `depannage`

---

## Problème précis à résoudre

Confirmer que l'interface est active et identifier le gestionnaire réseau qui la pilote.

## 1. Hors-Production (Lab / Test / POC)

1. Debian, Ubuntu, Rocky : afficher l'état du lien et des adresses :
   ```bash
   ip -br link
   ip -br address
   ```
   👉 Explication : `UP` indique un lien actif; `DOWN` indique un câble, un port switch ou une vNIC en défaut.

2. Identifier le gestionnaire actif :
   ```bash
   systemctl is-active NetworkManager systemd-networkd
   nmcli -f NAME,DEVICE,TYPE connection show --active
   networkctl list
   ```
   👉 Explication : un seul des deux gestionnaires est normalement actif; ne pas en activer un second avant d'avoir identifié le propriétaire.

3. Alpine Linux (y compris LXC Proxmox) :
   ```sh
   ip -br link
   ip -br addr
   ip route
   rc-status
   ```
   👉 Explication : dans un LXC, adresse, passerelle, bridge et VLAN sont souvent définis côté Proxmox.

4. Windows 10/11 et Server : lister les cartes :
   ```powershell
   Get-NetAdapter | Format-Table Name, Status, LinkSpeed, MacAddress
   Get-NetIPConfiguration
   ```
   👉 Explication : on contrôle que la bonne carte est `Up`.

5. Alternative GUI Windows : ouvrir `ncpa.cpl` (**Win + R > ncpa.cpl**) et vérifier que la carte est activée.
   👉 Explication : ne pas supprimer/recréer une carte virtuelle avant d'avoir noté ses paramètres.

## 2. Production — Contrôles

Comparer avec la configuration attendue (câble, port switch, VLAN, bridge) avant toute action.

## 3. Production — Sécurité

- Ne jamais vider les règles du pare-feu ni le désactiver pour « tester ».
- Tester uniquement une adresse et un port autorisés; aucun balayage de réseau.

## Validation et retour arrière

- **Validation** : L'interface est `UP`, porte l'adresse attendue et son gestionnaire est identifié.
- **Retour arrière** : Aucune modification n'est faite ici; en cas de changement ultérieur, restaurer le profil réseau d'origine depuis la console.

## Si le problème n'est pas résolu

- [Netplan — documentation](https://netplan.readthedocs.io/)
- [Microsoft — cmdlets NetTCPIP](https://learn.microsoft.com/en-us/powershell/module/nettcpip/)
- [Guide complet — 3. Étape 1 — Vérifier le lien et l'interface](/02-fiches-completes/transverses/multi-os/diagnostic/15-depannage-reseau-diagnostic-complet-multi-os#3-etape-1-verifier-le-lien-et-linterface)