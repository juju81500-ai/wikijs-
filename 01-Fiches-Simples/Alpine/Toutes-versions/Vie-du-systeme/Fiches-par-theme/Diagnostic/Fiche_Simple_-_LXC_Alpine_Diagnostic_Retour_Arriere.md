# Fiche_Simple_-_LXC_Alpine_Diagnostic_Retour_Arriere.md

- **Environnement** : CT Alpine sur Proxmox VE; accès console de l'hôte conservé
- **OS / Version** : branche Alpine maintenue
- **Catégorie** : diagnostic / retour arrière
- **Tags** : `alpine`, `proxmox`, `lxc`, `rollback`, `backup`

---

## Problème précis à résoudre

Récupérer l'accès au CT ou au service après une correction réseau infructueuse en préservant configuration, données et journaux.

## 1. Hors-Production (Lab / Test / POC)

1. Restaurer la configuration du CT sauvegardée avant l'intervention :
   ```bash
   cat /root/ct-CTID-avant.conf
   pct set CTID -net0 name=eth0,bridge=vmbr0,ip=IP/PREFIXE,gw=PASSERELLE
   pct reboot CTID
   ```
   👉 Explication : reprendre exactement les valeurs du fichier sauvegardé; ou restaurer le fichier Alpine modifié depuis la console.

2. Si l'accès reste perdu : arrêter les écritures et conserver le CT :
   ```bash
   pct stop CTID
   ```
   👉 Explication : ne pas supprimer le CT ni ses journaux.

3. Restaurer une sauvegarde dans un ID et un réseau isolés : **Stockage PBS > Content > Restore** avec un ID temporaire.
   👉 Explication : voir la fiche de restauration isolée.

## 2. Production — Contrôles

Déclencher la procédure d'incident, prévenir le propriétaire et préserver les éléments nécessaires à l'analyse avant toute suppression.

## 3. Production — Sécurité

- Ne pas supprimer le CT ni son stockage pour résoudre une panne réseau.
- Ne pas restaurer une sauvegarde directement sur le réseau actif sans vérifier l'IP.
- Ne pas détruire les journaux, snapshots ou sauvegardes pendant l'investigation.
- Limiter l'accès à la copie restaurée et aux données récupérées.

## Validation et retour arrière

- **Validation** : service restauré ou CT isolé fonctionnel, données conservées et accès réseau maîtrisé.
- **Retour arrière** : revenir à la configuration précédente ou à l'instance antérieure; documenter la cause et le résultat.

## Si le problème n'est pas résolu

- [Proxmox VE — documentation](https://pve.proxmox.com/pve-docs/)
- [Alpine Linux — documentation](https://docs.alpinelinux.org/)
- [Guide complet de diagnostic LXC Alpine](../../../../../../02-Fiches-Completes/Alpine/Toutes-versions/Diagnostic/17_Diagnostic_LXC_Alpine_Reseau_Services.md#6-retour-arriere)
