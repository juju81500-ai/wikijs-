# Fiche_Simple_-_LXC_Alpine_Sauvegarde_Cadrer_Protection.md

- **Environnement** : Proxmox VE avec CT Alpine; PBS ou cible de sauvegarde dédiée
- **OS / Version** : branche Alpine maintenue choisie pour le service
- **Catégorie** : sauvegarde LXC / cadrage

---

## Problème précis à résoudre

Définir ce qui doit être protégé et comment restaurer un CT Alpine sans confondre sauvegarde du conteneur et sauvegarde cohérente de l'application.

## 1. Hors-Production (Lab / Test / POC)

1. Inventorier le CT :
   ```bash
   pct config CTID
   ```
   👉 Explication : relever ID, hostname, IP, bridge/VLAN, points de montage.

2. Lister données et tâches dans le CT :
   ```sh
   df -h
   cat /proc/mounts | grep -v 'proc\|sys'
   crontab -l; ls /etc/periodic
   rc-status
   ```
   👉 Explication : repérer données persistantes, secrets, montages et tâches planifiées.

3. Choisir une cible distincte du nœud, la rétention, le chiffrement et le responsable de la récupération.
   👉 Explication : un snapshot local ne remplace pas une copie indépendante; pour une base, ajouter une sauvegarde applicative cohérente.

## 2. Production — Contrôles

Faire approuver périmètre, cohérence applicative, fréquence, rétention, chiffrement, accès aux clés et modalités d'escalade.

## 3. Production — Sécurité

- Une snapshot locale ne remplace pas une copie indépendante.
- Ne pas stocker les seules clés de chiffrement ou identifiants PBS dans le CT sauvegardé.
- Protéger les secrets hors du conteneur dans le coffre approuvé.
- Ne pas considérer une sauvegarde CT comme cohérente pour une base active sans procédure applicative.

## Validation et retour arrière

- **Validation** : liste des données, dépendances, cible, RPO/RTO et restauration pilote sont documentés.
- **Arrêt** : ne pas activer la sauvegarde de production avant d'avoir défini la cohérence applicative et la cible indépendante.

## Si le problème n'est pas résolu

- [Proxmox VE — vzdump](https://pve.proxmox.com/pve-docs/vzdump.1.html)
- [Proxmox Backup Server — documentation](https://pbs.proxmox.com/docs/)
- [Guide complet sauvegarde/restauration LXC Alpine](/02-fiches-completes/alpine/toutes-versions/autres/18-alpine-lxc-sauvegarde-restauration-production#1-concevoir-la-protection)