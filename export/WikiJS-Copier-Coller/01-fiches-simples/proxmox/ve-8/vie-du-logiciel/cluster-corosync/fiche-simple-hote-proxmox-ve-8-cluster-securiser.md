# Fiche_Simple_-_Hote_Proxmox_VE_8_Cluster_Securiser.md

- **Environnement** : Nœuds physiques dédiés, réseau Corosync faible latence
- **OS / Version** : Proxmox VE 8.x
- **Catégorie** : virtualisation / cluster

---

## Problème précis à résoudre

Restreindre et durcir l'accès à l'interface Web, à l'API et à SSH.

## 1. Hors-Production (Lab / Test / POC)

1. Restreindre l'interface Web/API et SSH au réseau d'administration (pare-feu : **Datacenter > Firewall**).
   👉 Explication : on réduit la surface d'attaque.

2. Créer des comptes nominatifs : **Datacenter > Permissions > Users**, puis activer le MFA : **Datacenter > Permissions > Two Factor**.
   👉 Explication : fini les comptes partagés; le second facteur protège les accès.

3. Gérer les certificats : **Node > System > Certificates**.
   👉 Explication : on remplace le certificat auto-signé par un certificat approuvé.

4. Limiter les privilèges via des rôles : **Datacenter > Permissions**.
   👉 Explication : chacun n'a que les droits nécessaires.

5. Centraliser les sauvegardes hors cluster.
   👉 Explication : un incident cluster ne doit pas détruire les sauvegardes.

## 2. Production — Contrôles

Garder un accès console avant toute règle de pare-feu.

## 3. Production — Sécurité

- Ne pas appliquer de règles de pare-feu sans accès console de secours.
- Ne pas utiliser le compte root pour l'usage courant.

## Validation et retour arrière

- **Validation** : Accès limité au réseau d'administration, comptes nominatifs avec MFA.
- **Retour arrière** : Désactiver la règle de pare-feu fautive depuis la console.

## Si le problème n'est pas résolu

- [Proxmox VE — Cluster Manager](https://pve.proxmox.com/wiki/Cluster_Manager)
- [Proxmox VE — Guide d'administration](https://pve.proxmox.com/pve-docs/)
- [Guide complet — sécuriser l'administration](/02-fiches-completes/proxmox/ve-8/installation-deploiement/09-hyperviseur-proxmox-ve-8x-cluster-corosync#4-securiser-ladministration)