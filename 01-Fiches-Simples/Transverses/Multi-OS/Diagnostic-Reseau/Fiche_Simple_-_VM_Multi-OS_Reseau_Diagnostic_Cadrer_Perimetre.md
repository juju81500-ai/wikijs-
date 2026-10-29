# Fiche_Simple_-_VM_Multi-OS_Reseau_Diagnostic_Cadrer_Perimetre.md

- **Environnement** : VM, poste, serveur, LXC Proxmox ou hôte Docker (Linux ou Windows)
- **OS / Version** : Debian 12/13, Ubuntu 24.04/26.04, Rocky Linux 9, Alpine Linux, Windows 10/11, Windows Server 2022/2025
- **Catégorie** : réseau / cadrage
- **Tags** : `reseau`, `diagnostic`, `multi-os`, `depannage`

---

## Problème précis à résoudre

Poser le parcours de diagnostic (Lien → Adresse → Passerelle → Route → DNS → Port → Application) avant de toucher à la configuration.

## 1. Hors-Production (Lab / Test / POC)

1. Noter la machine concernée et l'état actuel (exemple Linux) :
   ```bash
   hostname
   date
   ip -br address
   ```
   👉 Explication : on fige le nom de la machine, l'heure et les adresses pour comparer avant/après.

2. Sous Windows, relever la même information :
   ```powershell
   hostname
   Get-Date
   Get-NetIPConfiguration
   ```
   👉 Explication : même relevé côté Windows : adresse, passerelle et DNS actuels.

3. Écrire dans le ticket l'ordre de test : **Lien → Adresse → Passerelle → Route → DNS → Port → Application**.
   👉 Explication : on teste du plus bas niveau au plus haut; on ne change rien tant que la couche inférieure n'est pas validée.

4. Identifier le gestionnaire réseau (Netplan, NetworkManager, systemd-networkd, OpenRC, Windows, Proxmox, Docker) avant toute modification persistante.
   👉 Explication : la configuration durable se fait uniquement avec l'outil propriétaire de l'interface.

## 2. Production — Contrôles

Définir qui peut intervenir sur le réseau, la fenêtre de maintenance et le canal d'escalade.

## 3. Production — Sécurité

- Ne jamais vider les règles du pare-feu ni le désactiver pour « tester ».
- Tester uniquement une adresse et un port autorisés; aucun balayage de réseau.

## Validation et retour arrière

- **Validation** : Le périmètre (machine, interface, destination, port) et l'ordre de test sont écrits dans le ticket.
- **Retour arrière** : Aucune modification n'est faite à ce stade; il n'y a rien à annuler.

## Si le problème n'est pas résolu

- [Netplan — documentation](https://netplan.readthedocs.io/)
- [Microsoft — cmdlets NetTCPIP](https://learn.microsoft.com/en-us/powershell/module/nettcpip/)
- [Guide complet — 1. Objectif et périmètre](../../../../02-Fiches-Completes/Transverses/Multi-OS/Diagnostic/15_Depannage_Reseau_Diagnostic_Complet_Multi_OS.md#1-objectif-et-perimetre)
