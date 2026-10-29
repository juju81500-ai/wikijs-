# Fiche_Simple_-_VM_Proxmox_pfSense_CE_Deploiement_Creer_VM_Pare_Feu.md

- **Environnement** : VM pfSense CE en laboratoire sur Proxmox VE, deux interfaces (WAN et LAN isolés)
- **OS / Version** : pfSense Community Edition 2.9.0 (VM x86-64 sur Proxmox VE)
- **Catégorie** : pare-feu et routage

---

## Problème précis à résoudre

Créer la VM pfSense avec les paramètres de laboratoire prévus.

## 1. Hors-Production (Lab / Test / POC)

1. Dans Proxmox : **Créer une VM**, lui donner un identifiant documenté et un nom clair, puis attacher l'ISO Netgate au lecteur optique.
   👉 Explication : l'ISO sert à démarrer l'installateur; garder la console Proxmox disponible.

2. Régler **Système** (BIOS/UEFI selon la recette Netgate retenue) et **Disque** : VirtIO Block d'au moins 16 Go.
   👉 Explication : ne pas changer de mode BIOS/UEFI après installation.

3. Régler **CPU** : 2 vCPU et **Mémoire** : 2 Go.
   👉 Explication : les minimums publiés (1 CPU, 1 Go, 8 Go) ne conviennent pas à tous les scénarios.

4. Ajouter deux cartes réseau **VirtIO** : la première sur `vmbr-pfsense-wan`, la seconde sur `vmbr-pfsense-lan`.
   👉 Explication : l'ordre définit `vtnet0` (WAN) et `vtnet1` (LAN).

5. En commande sur l'hôte Proxmox, contrôler la configuration (remplacer 9100 par l'identifiant réel de la VM) :
   ```bash
   sudo qm config 9100
   ```
   👉 Explication : affiche disque, cartes réseau et ISO; 9100 est un identifiant d'exemple.

6. Créer séparément une VM cliente de test sur `vmbr-pfsense-lan`.
   👉 Explication : elle servira à joindre le GUI; l'administration de l'hyperviseur reste hors de ce segment.

## 2. Production — Contrôles

Documenter identifiant, stockage, ponts et propriétaire de la VM; dimensionner selon le débit attendu (non couvert ici).

## 3. Production — Sécurité

- Garder l'accès d'administration de l'hyperviseur hors du LAN pfSense.

## Validation et retour arrière

- **Validation** : la VM existe avec deux cartes VirtIO sur les bons ponts et l'ISO attachée.
- **Retour arrière** : arrêter puis supprimer uniquement la VM de test créée (**Plus > Supprimer**), après vérification de son identifiant.

## Si le problème n'est pas résolu

- [Netgate — exigences matérielles](https://docs.netgate.com/pfsense/en/latest/hardware/minimum-requirements.html)
- [Netgate — pfSense CE 2.9.0](https://docs.netgate.com/pfsense/en/latest/releases/2-9-0.html)
- [Guide complet](/02-fiches-completes/pfsense/toutes-versions/installation-deploiement/70-deploiement-pfsense-ce-2-9-0-proxmox-lab#3-creer-la-vm-de-pare-feu)