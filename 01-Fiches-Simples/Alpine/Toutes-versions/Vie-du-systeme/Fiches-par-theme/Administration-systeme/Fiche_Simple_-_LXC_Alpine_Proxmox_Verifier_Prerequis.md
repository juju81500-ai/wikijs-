# Fiche_Simple_-_LXC_Alpine_Proxmox_Verifier_Prerequis.md

- **Environnement** : nœud Proxmox VE et plan de création du CT validé
- **OS / Version** : Proxmox VE en version maintenue; template Alpine compatible
- **Catégorie** : virtualisation / prérequis LXC
- **Tags** : `alpine`, `proxmox`, `lxc`, `prerequis`, `reseau`

---

## Problème précis à résoudre

Vérifier que l'hôte, le template, le réseau, les ressources et les accès de secours sont prêts avant de créer le conteneur.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier le nœud, le stockage et l'ID libre :
   ```bash
   pveversion
   pvesm status
   pct status CTID 2>&1 | head -1
   ```
   👉 Explication : remplacer `CTID`; un « does not exist » signifie que l'ID est libre.

2. Vérifier les templates Alpine disponibles et maintenus :
   ```bash
   pveam update
   pveam available | grep -i alpine
   ```
   👉 Explication : ne pas choisir Alpine 3.19 pour un nouveau service de production.

3. Vérifier l'accès console de secours : dans l'interface Proxmox, ouvrir **Nœud > Shell**.
   👉 Explication : toujours garder un accès hors réseau du CT.

4. Consigner : hostname, plan IP/DNS, bridge/VLAN, quotas, sauvegarde.
   👉 Explication : éviter un CT privilégié; nesting, FUSE et montages seulement si justifiés.

## 2. Production — Contrôles

Valider le changement, l'ID libre, le réseau disponible, les quotas, le stockage, l'accès console, la branche Alpine et la restauration.

## 3. Production — Sécurité

- Ne pas sélectionner Alpine 3.19 pour un nouveau service de production.
- Ne pas choisir un template sans vérifier sa provenance et son état de maintenance.
- Ne pas se fier à un accès réseau unique; conserver un accès console Proxmox.
- Ne pas activer des options de conteneur privilégiées pour contourner un défaut de conception.

## Validation et retour arrière

- **Validation** : toutes les valeurs sont documentées et les ressources sont disponibles.
- **Arrêt** : reporter si template, réseau, stockage ou sauvegarde n'est pas validé.

## Si le problème n'est pas résolu

- [Proxmox VE — documentation](https://pve.proxmox.com/pve-docs/)
- [Alpine Linux — documentation](https://docs.alpinelinux.org/)
- [Guide complet LXC Alpine sur Proxmox](../../../../../../02-Fiches-Completes/Alpine/Toutes-versions/Installation-Deploiement/16_Installation_LXC_Alpine_Proxmox.md#2-prerequis)
