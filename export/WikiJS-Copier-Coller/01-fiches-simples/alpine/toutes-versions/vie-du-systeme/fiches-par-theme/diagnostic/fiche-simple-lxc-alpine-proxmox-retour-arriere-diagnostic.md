# Fiche_Simple_-_LXC_Alpine_Proxmox_Retour_Arriere_Diagnostic.md

- **Environnement** : CT Alpine sur Proxmox VE avec accès à la console de l'hôte
- **OS / Version** : branche Alpine maintenue retenue pour le CT
- **Catégorie** : virtualisation / dépannage et reprise

---

## Problème précis à résoudre

Rétablir l'accès ou le service après un problème réseau ou applicatif sans supprimer de CT, volume ou sauvegarde par erreur.

## 1. Hors-Production (Lab / Test / POC)

1. En cas de perte réseau, corriger bridge/VLAN/IP depuis la console Proxmox :
   ```bash
   pct config CTID
   pct set CTID -net0 name=eth0,bridge=vmbr0,ip=IP/PREFIXE,gw=PASSERELLE,tag=VLAN
   ```
   👉 Explication : remplacer les valeurs; ne pas se fier à l'accès réseau du CT lui-même.

2. Si le service ne démarre pas, dans le CT :
   ```sh
   rc-status
   rc-service SERVICE status
   tail -50 /var/log/messages
   ```
   👉 Explication : consulter l'état OpenRC et les journaux.

3. Pour annuler le déploiement, arrêter le CT sans le supprimer :
   ```bash
   pct stop CTID
   ```
   👉 Explication : ne supprimer le CT qu'après validation de la sauvegarde et de l'acceptation.

## 2. Production — Contrôles

Appliquer la procédure d'incident, conserver les journaux utiles, identifier le propriétaire des données et obtenir l'approbation avant toute suppression.

## 3. Production — Sécurité

- Ne pas supprimer un CT ou son stockage par simple réflexe de dépannage.
- Ne pas réutiliser une adresse pendant qu'une ancienne instance peut être active.
- Ne pas contourner les règles de filtrage du nœud pour rétablir rapidement un service.
- Préserver une sauvegarde indépendante avant toute opération irréversible.

## Validation et retour arrière

- **Validation** : cause identifiée, service accessible depuis le réseau attendu, données conservées et accès non autorisés refusés.
- **Retour arrière** : redémarrer l'ancien CT ou restaurer une sauvegarde vers une cible isolée puis basculer après recette.

## Si le problème n'est pas résolu

- [Proxmox VE — documentation](https://pve.proxmox.com/pve-docs/)
- [Alpine Linux — documentation](https://docs.alpinelinux.org/)
- [Guide complet LXC Alpine sur Proxmox](/02-fiches-completes/alpine/toutes-versions/installation-deploiement/16-installation-lxc-alpine-proxmox#7-retour-arriere-et-depannage)