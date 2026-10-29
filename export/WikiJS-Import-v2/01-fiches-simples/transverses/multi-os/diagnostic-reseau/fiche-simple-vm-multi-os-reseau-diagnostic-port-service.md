---
title: "Fiche Simple - VM Multi-OS Reseau Diagnostic Port Service"
description: "Confirmer qu'un port précis répond et que le service écoute."
published: true
date: 2026-10-29T19:39:36Z
tags: ["reseau", "diagnostic", "multi-os", "depannage"]
editor: markdown
dateCreated: 2026-10-29T19:39:36Z
dateModified: 2026-10-29T19:39:36Z
---

# Fiche_Simple_-_VM_Multi-OS_Reseau_Diagnostic_Port_Service.md

- **Environnement** : VM, poste, serveur, LXC Proxmox ou hôte Docker (Linux ou Windows)
- **OS / Version** : Debian 12/13, Ubuntu 24.04/26.04, Rocky Linux 9, Alpine Linux, Windows 10/11, Windows Server 2022/2025
- **Catégorie** : réseau / couche application
- **Tags** : `reseau`, `diagnostic`, `multi-os`, `depannage`

---

## Problème précis à résoudre

Confirmer qu'un port précis répond et que le service écoute.

## 1. Hors-Production (Lab / Test / POC)

1. Linux client : tester le port (remplacer `192.0.2.10` et `443` par la cible et le port autorisés) :
   ```bash
   nc -vz -w 3 192.0.2.10 443
   ```
   👉 Explication : `succeeded` confirme que le TCP est ouvert; l'application n'est pas encore validée.

2. Côté serveur Linux : vérifier l'écoute et les services en échec :
   ```bash
   sudo ss -lntup
   systemctl --failed
   ```
   👉 Explication : on voit quel processus écoute sur quel port et quels services sont tombés.

3. Windows client :
   ```powershell
   Test-NetConnection 192.0.2.10 -Port 443
   Get-NetFirewallProfile | Select-Object Name, Enabled, DefaultInboundAction
   ```
   👉 Explication : teste le port et affiche la politique du pare-feu local.

4. Lire ensuite les journaux du service concerné.
   👉 Explication : une connexion TCP réussie ne valide ni l'application ni l'authentification.

## 2. Production — Contrôles

Limiter les tests aux flux autorisés.

## 3. Production — Sécurité

- Ne jamais vider les règles du pare-feu ni le désactiver pour « tester ».
- Tester uniquement une adresse et un port autorisés; aucun balayage de réseau.

## Validation et retour arrière

- **Validation** : Le port répond et le service écoute sur l'interface attendue.
- **Retour arrière** : Aucune modification ici.

## Si le problème n'est pas résolu

- [Netplan — documentation](https://netplan.readthedocs.io/)
- [Microsoft — cmdlets NetTCPIP](https://learn.microsoft.com/en-us/powershell/module/nettcpip/)
- [Guide complet — 7. Étape 5 — Vérifier le port et le service](/02-fiches-completes/transverses/multi-os/diagnostic/15-depannage-reseau-diagnostic-complet-multi-os#7-etape-5-verifier-le-port-et-le-service)