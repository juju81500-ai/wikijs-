# Fiche_Simple_-_LXC_Alpine_Proxmox_Cadrer_Architecture.md

- **Environnement** : cluster ou nœud Proxmox VE hébergeant un service dans un LXC Alpine
- **OS / Version** : branche Alpine maintenue disponible dans Proxmox VE
- **Catégorie** : virtualisation / cadrage LXC

---

## Problème précis à résoudre

Définir l'isolation, le réseau et les ressources d'un conteneur Alpine en tenant compte du noyau partagé avec l'hôte Proxmox.

## 1. Hors-Production (Lab / Test / POC)

1. Relever sur le nœud Proxmox les ponts, VLAN et stockages disponibles :
   ```bash
   pvesm status
   ip -br link show type bridge
   pct list
   ```
   👉 Explication : choisir bridge/VLAN et stockage cohérents avec le rôle du CT; relever les ID déjà utilisés.

2. Consigner : ID CT, hostname, IP/DNS, VLAN, CPU/RAM/disque, politique de sauvegarde.
   👉 Explication : un LXC partage le noyau de l'hôte; créer un conteneur **non privilégié**, isolé sur le réseau prévu.

3. Vérifier la version du noyau hôte :
   ```bash
   uname -r
   pveversion
   ```
   👉 Explication : le noyau de l'hôte doit être maintenu; les fonctions noyau du CT en dépendent.

## 2. Production — Contrôles

Faire approuver architecture, capacité, réseau, stockage, sauvegarde, restauration, cycle de maintenance et responsables d'exploitation.

## 3. Production — Sécurité

- Ne pas utiliser un CT privilégié ou des montages hôte sensibles par défaut.
- Ne pas exposer de ports non nécessaires au rôle.
- Ne pas traiter l'isolation LXC comme une séparation de noyau complète.
- Ne pas déployer sur une branche Alpine en fin de maintenance.

## Validation et retour arrière

- **Validation** : choix techniques, risques de noyau partagé, accès de secours et restauration sont approuvés.
- **Arrêt** : ne pas créer le CT si l'ID, le réseau, le stockage ou les responsabilités ne sont pas définis.

## Si le problème n'est pas résolu

- [Proxmox VE — documentation](https://pve.proxmox.com/pve-docs/)
- [Alpine Linux — documentation](https://docs.alpinelinux.org/)
- [Guide complet LXC Alpine sur Proxmox](/02-fiches-completes/alpine/toutes-versions/installation-deploiement/16-installation-lxc-alpine-proxmox#1-objectif-et-architecture)