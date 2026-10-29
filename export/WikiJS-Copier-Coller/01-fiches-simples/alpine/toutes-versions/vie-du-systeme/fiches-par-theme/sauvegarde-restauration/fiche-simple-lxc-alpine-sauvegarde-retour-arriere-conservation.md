# Fiche_Simple_-_LXC_Alpine_Sauvegarde_Retour_Arriere_Conservation.md

- **Environnement** : reprise LXC Alpine en période d'acceptation; CT source et restauration conservés
- **OS / Version** : Proxmox VE, PBS et branche Alpine maintenue
- **Catégorie** : sauvegarde LXC / retour arrière

---

## Problème précis à résoudre

Revenir à l'instance antérieure après un échec de restauration tout en évitant les doubles écritures et les suppressions prématurées.

## 1. Hors-Production (Lab / Test / POC)

1. Si le test échoue, garder le CT restauré isolé et vérifier l'ancien :
   ```bash
   pct status CTID
   pct status 9001
   ```
   👉 Explication : confirmer qu'il n'y a pas d'écritures concurrentes avant de relancer l'ancien service.

2. Remettre l'ancien service en marche :
   ```bash
   pct start CTID
   ```
   👉 Explication : ne jamais avoir deux CT avec la même IP ni exécutant les mêmes tâches.

3. Conserver ancienne instance et point de sauvegarde jusqu'à la fin de la période d'acceptation :
   ```bash
   pvesm list STOCKAGE_PBS --vmid CTID
   ```
   👉 Explication : consigner le RPO/RTO réellement mesuré.

## 2. Production — Contrôles

Faire valider période de conservation, propriétaire de données, critères de clôture, responsabilités, points de sauvegarde retenus et résultats de reprise.

## 3. Production — Sécurité

- Ne pas supprimer l'ancienne instance ni les sauvegardes avant approbation et fin de conservation.
- Ne pas exécuter des traitements métier en double pendant la bascule.
- Protéger les copies et journaux selon la classification des données.
- Garder la restauration isolée tant qu'elle n'est pas certifiée.

## Validation et retour arrière

- **Validation** : service stable durant la période définie, données cohérentes et retour arrière disponible.
- **Retour arrière** : arrêter et isoler la nouvelle instance, remettre l'ancienne en service après contrôle des écritures.

## Si le problème n'est pas résolu

- [Proxmox Backup Server — documentation](https://pbs.proxmox.com/docs/)
- [Proxmox Backup Server — vérification d'intégrité](https://pbs.proxmox.com/docs/maintenance.html)
- [Guide complet sauvegarde/restauration LXC Alpine](/02-fiches-completes/alpine/toutes-versions/autres/18-alpine-lxc-sauvegarde-restauration-production#6-retour-arriere-et-conservation)