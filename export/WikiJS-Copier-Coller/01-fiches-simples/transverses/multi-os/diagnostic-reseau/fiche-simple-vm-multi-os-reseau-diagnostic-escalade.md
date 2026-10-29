# Fiche_Simple_-_VM_Multi-OS_Reseau_Diagnostic_Escalade.md

- **Environnement** : VM, poste, serveur, LXC Proxmox ou hôte Docker (Linux ou Windows)
- **OS / Version** : Debian 12/13, Ubuntu 24.04/26.04, Rocky Linux 9, Alpine Linux, Windows 10/11, Windows Server 2022/2025
- **Catégorie** : réseau / escalade

---

## Problème précis à résoudre

Rassembler les informations utiles pour transmettre l'incident.

## 1. Hors-Production (Lab / Test / POC)

1. Collecter les identifiants de la machine (Linux) :
   ```bash
   hostnamectl
   ip -br address
   ip route
   ```
   👉 Explication : OS, interface, adresse et passerelle sont les premières informations demandées.

2. Collecter les mêmes informations sous Windows :
   ```powershell
   Get-ComputerInfo -Property CsName, OsName, OsVersion
   Get-NetIPConfiguration
   ```
   👉 Explication : nom, version d'OS et configuration IP.

3. Noter destination, port, heure du test et message d'erreur exact.
   👉 Explication : le support peut ainsi reproduire le test.

4. Joindre résultats des commandes, changements récents, tests depuis un poste fonctionnel, règles modifiées et retour arrière utilisé.
   👉 Explication : évite les allers-retours inutiles.

## 2. Production — Contrôles

Masquer mots de passe, jetons et adresses sensibles avant d'envoyer les sorties.

## 3. Production — Sécurité

- Ne jamais joindre de secret ni de capture réseau non filtrée au ticket.

## Validation et retour arrière

- **Validation** : Le ticket contient toutes les informations listées.
- **Retour arrière** : Rien à annuler; le dossier est en lecture seule.

## Si le problème n'est pas résolu

- [Netplan — documentation](https://netplan.readthedocs.io/)
- [Microsoft — cmdlets NetTCPIP](https://learn.microsoft.com/en-us/powershell/module/nettcpip/)
- [Guide complet — 11. Informations à transmettre pour escalade](/02-fiches-completes/transverses/multi-os/diagnostic/15-depannage-reseau-diagnostic-complet-multi-os#11-informations-a-transmettre-pour-escalade)