# Fiche_Simple_-_VM_Multi-OS_Reseau_Diagnostic_Conteneurs.md

- **Environnement** : VM, poste, serveur, LXC Proxmox ou hôte Docker (Linux ou Windows)
- **OS / Version** : Debian 12/13, Ubuntu 24.04/26.04, Rocky Linux 9, Alpine Linux, Windows 10/11, Windows Server 2022/2025
- **Catégorie** : réseau / Docker et LXC

---

## Problème précis à résoudre

Diagnostiquer le réseau d'une pile Docker Compose ou d'un LXC Proxmox.

## 1. Hors-Production (Lab / Test / POC)

1. Docker Compose : lister services et réseaux :
   ```bash
   docker compose ps
   docker network ls
   ```
   👉 Explication : on voit l'état des services et les réseaux disponibles.

2. Inspecter le réseau et tester le nom d'un service (remplacer `reseau_app`, `client` et `cible` par vos noms) :
   ```bash
   docker network inspect reseau_app
   docker compose exec client getent hosts cible
   docker compose logs --tail 100 cible
   ```
   👉 Explication : les noms de service sont résolus dans le réseau Compose; un port interne n'est pas forcément publié sur l'hôte.

3. LXC Proxmox : ouvrir **CT > Network** (bridge, VLAN tag, IP, passerelle) et **CT > Firewall**.
   👉 Explication : la configuration réseau du conteneur vient de Proxmox; on la compare à l'intérieur du CT.

4. Dans le CT :
   ```sh
   ip -br addr
   ip route
   ```
   👉 Explication : doit correspondre à la configuration affichée dans Proxmox.

## 2. Production — Contrôles

Garder la console Proxmox ouverte pendant toute correction.

## 3. Production — Sécurité

- Ne jamais exécuter `iptables -F` ni `nft flush ruleset` pour dépanner Docker.

## Validation et retour arrière

- **Validation** : Le service cible est joignable par son nom et son port depuis le conteneur client.
- **Retour arrière** : Aucune modification ici.

## Si le problème n'est pas résolu

- [Netplan — documentation](https://netplan.readthedocs.io/)
- [Microsoft — cmdlets NetTCPIP](https://learn.microsoft.com/en-us/powershell/module/nettcpip/)
- [Guide complet — 8. Cas particuliers des conteneurs](/02-fiches-completes/transverses/multi-os/diagnostic/15-depannage-reseau-diagnostic-complet-multi-os#8-cas-particuliers-des-conteneurs)