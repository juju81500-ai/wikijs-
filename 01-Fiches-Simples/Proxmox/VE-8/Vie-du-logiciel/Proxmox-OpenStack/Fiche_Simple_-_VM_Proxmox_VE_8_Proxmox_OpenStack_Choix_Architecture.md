# Fiche_Simple_-_VM_Proxmox_VE_8_Proxmox_OpenStack_Choix_Architecture

- **Environnement** : Décision d’architecture pour lab autonome, sans interconnexion implicite
- **OS / Version** : Proxmox VE 8.x; OpenStack lab sur Ubuntu Server 24.04 LTS
- **Catégorie** : virtualisation / cloud privé / architecture
- **Tags** : `proxmox-ve`, `pve8`, `openstack`, `architecture`, `lab`

---

## Problème précis à résoudre

Définir une manière d’étudier Proxmox VE 8 et OpenStack sans prétendre qu’il existe une intégration native officiellement prise en charge.

## 1. Hors-Production (Lab / Test / POC)

1. Définir l’objectif : comparer deux plateformes autonomes, héberger une VM OpenStack sur Proxmox, ou évaluer un connecteur tiers avec sa propre matrice de support. Pour une première maquette, retenir deux environnements indépendants et une VM OpenStack jetable.
   👉 Explication : Proxmox VE est un hyperviseur avec API; OpenStack est une plateforme et API distinctes. Réseau commun ne signifie pas plan de contrôle commun.
2. Schématiser : Proxmox fournit la VM Ubuntu; DevStack y installe OpenStack mono-nœud de développement. Isoler réseaux de gestion et d’essai.
   👉 Explication : modèle imbriqué pour apprendre, pas pour héberger des charges réelles ou valider la HA.
3. Pour la production, choisir une méthode OpenStack dont les fournisseurs publient explicitement matrices OS/hyperviseur/stockage/réseau; faire confirmer tout connecteur tiers.
   👉 Explication : API accessible ne prouve ni certification ni support.

## 2. Production — Contrôles

- Documenter opérateur et support de chaque plateforme, versions, responsabilités et cycle de vie. DevStack n’est pas un déploiement de production.

## 3. Production — Sécurité

- Garder séparés plans de gestion et identités; ne pas partager de jetons d’administration.

## Validation et retour arrière

- **Validation** : schéma distingue hyperviseur, VM OpenStack, APIs, propriétaires et limites de support. **Retour arrière** : arrêter le POC; aucune modification de production requise.

## Si le problème n'est pas résolu

- [Proxmox VE — documentation officielle](https://pve.proxmox.com/pve-docs/)
- [Proxmox VE — API Viewer](https://pve.proxmox.com/pve-docs/api-viewer/index.html)
- [OpenStack — documentation officielle](https://docs.openstack.org/)
- [DevStack — Quick Start](https://docs.openstack.org/devstack/latest/)
