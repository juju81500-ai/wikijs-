# Fiche_Simple_-_VM_Multi-OS_Reseau_Diagnostic_Securiser_Diagnostic.md

- **Environnement** : VM, poste, serveur, LXC Proxmox ou hôte Docker (Linux ou Windows)
- **OS / Version** : Debian 12/13, Ubuntu 24.04/26.04, Rocky Linux 9, Alpine Linux, Windows 10/11, Windows Server 2022/2025
- **Catégorie** : réseau / prérequis
- **Tags** : `reseau`, `diagnostic`, `multi-os`, `depannage`

---

## Problème précis à résoudre

Préparer un diagnostic réseau sans risquer de couper l'accès à la machine.

## 1. Hors-Production (Lab / Test / POC)

1. Noter l'heure, la machine, l'interface, le VLAN, la source, la destination et le port concernés dans le ticket.
   👉 Explication : ces éléments permettent de reproduire le test et de comparer avec une machine saine.

2. Relever la route et l'adresse sur la machine en panne puis sur une machine fonctionnelle du même segment :
   ```bash
   ip -br address
   ip route
   ```
   👉 Explication : toute différence entre les deux machines est un indice de cause.

3. Ouvrir une console d'hyperviseur, Proxmox ou hors bande avant toute modification distante.
   👉 Explication : si l'accès réseau est perdu, la console permet de revenir en arrière.

4. Lister les changements récents : IP, DHCP, DNS, pare-feu, switch, hyperviseur.
   👉 Explication : la panne suit souvent un changement récent.

5. Sous Windows, relever l'état des cartes :
   ```powershell
   Get-NetAdapter | Format-Table Name, Status, LinkSpeed
   ```
   👉 Explication : on voit rapidement une carte déconnectée ou désactivée.

## 2. Production — Contrôles

Garder une session de secours ouverte pendant tout changement réseau distant.

## 3. Production — Sécurité

- Ne jamais vider les règles du pare-feu ni le désactiver pour « tester ».
- Tester uniquement une adresse et un port autorisés; aucun balayage de réseau.

## Validation et retour arrière

- **Validation** : Une console de secours est ouverte et le relevé « avant » est conservé.
- **Retour arrière** : Aucun changement appliqué : rien à annuler.

## Si le problème n'est pas résolu

- [Netplan — documentation](https://netplan.readthedocs.io/)
- [Microsoft — cmdlets NetTCPIP](https://learn.microsoft.com/en-us/powershell/module/nettcpip/)
- [Guide complet — 2. Sécuriser le diagnostic](../../../../02-Fiches-Completes/Transverses/Multi-OS/Diagnostic/15_Depannage_Reseau_Diagnostic_Complet_Multi_OS.md#2-securiser-le-diagnostic)
