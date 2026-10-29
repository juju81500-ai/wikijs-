# Fiche_Simple_-_LXC_Alpine_Diagnostic_Preparer_Intervention.md

- **Environnement** : LXC Alpine sur Proxmox VE; console d'administration accessible
- **OS / Version** : branche Alpine maintenue; noter la version réelle avant intervention
- **Catégorie** : diagnostic / préparation

---

## Problème précis à résoudre

Préparer un diagnostic réseau/service en préservant l'accès console et en évitant les actions globales risquées.

## 1. Hors-Production (Lab / Test / POC)

1. Noter l'état de départ :
   ```sh
   date; ip -br addr; ip route
   ```
   👉 Explication : relever heure, IP, interface, bridge/VLAN, destination et port concernés.

2. Garder la console Proxmox ouverte : **CT > Console** (ou `pct enter CTID` depuis le nœud).
   👉 Explication : l'accès doit survivre à une perte réseau.

3. Sauvegarder la configuration du CT :
   ```bash
   pct config CTID > /root/ct-CTID-avant.conf
   ```
   👉 Explication : remplacer `CTID`; ne pas vider les règles du firewall ni redémarrer le nœud.

4. Suivre la chaîne : hôte/bridge → interface → IP → passerelle → route → DNS → port → service.
   👉 Explication : on ne corrige qu'une couche à la fois.

## 2. Production — Contrôles

Consigner symptômes, périmètre, changement récent, propriétaire réseau et personne autorisée à effectuer la correction.

## 3. Production — Sécurité

- Ne pas vider les règles de pare-feu ni redémarrer tout le nœud Proxmox.
- Ne pas supposer qu'un LXC se configure comme une VM.
- Ne pas modifier des fichiers générés automatiquement par Proxmox.
- Ne pas réaliser de test vers une destination ou un port hors périmètre.

## Validation et retour arrière

- **Validation** : console de secours et état initial documentés avant toute action.
- **Arrêt** : ne pas appliquer de correction si le propriétaire de la configuration n'est pas identifié.

## Si le problème n'est pas résolu

- [Proxmox VE — documentation](https://pve.proxmox.com/pve-docs/)
- [Alpine Linux — documentation](https://docs.alpinelinux.org/)
- [Guide complet de diagnostic LXC Alpine](/02-fiches-completes/alpine/toutes-versions/diagnostic/17-diagnostic-lxc-alpine-reseau-services#1-objectif-et-precautions)