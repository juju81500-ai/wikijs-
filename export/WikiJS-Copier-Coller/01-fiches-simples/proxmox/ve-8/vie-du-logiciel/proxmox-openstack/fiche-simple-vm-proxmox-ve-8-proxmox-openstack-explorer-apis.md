# Fiche_Simple_-_VM_Proxmox_VE_8_Proxmox_OpenStack_Explorer_APIs

- **Environnement** : Proxmox VE 8.x et DevStack dans VM de lab isolée
- **OS / Version** : Proxmox VE 8.x; Ubuntu 24.04 LTS / OpenStack DevStack
- **Catégorie** : cloud privé / API

---

## Problème précis à résoudre

Observer les deux interfaces de gestion et évaluer une interaction API sans supposer un connecteur natif supporté.

## 1. Hors-Production (Lab / Test / POC)

1. Dans Proxmox, consulter **Datacenter > Permissions > API Tokens**; ne créer un jeton que pour un test précis et un compte restreint.
   👉 Explication : jetons Proxmox/OpenStack sont distincts et non interchangeables.
2. Depuis le client OpenStack du lab, charger le `openrc` local et interroger le catalogue :
   ```bash
   source openrc
   openstack catalog list
   ```
   👉 Explication : vérifie seulement l’API OpenStack visée; ne pas publier les secrets.
3. Pour une intégration personnalisée, spécifier système appelant, endpoint, droits minimum, gestion d’erreur, débit et support éditeur; commencer par lecture autorisée en lab.
   👉 Explication : appels API ne signifient ni synchronisation VM, stockage partagé ni intégration officiellement supportée. Pas d’automatisation d’écriture avant revue.
4. Comparer les contrats d’API officiels de chaque produit.
   👉 Explication : références séparées ne certifient pas un pont entre plateformes.

## 2. Production — Contrôles

- Toute intégration personnalisée en production requiert revue architecture, validation éditeurs, essais et contrat de support.

## 3. Production — Sécurité

- Identités non privilégiées, jetons limités, TLS, coffre-fort et journaux protégés; jamais token, `openrc` ou Authorization en clair dans commande/dépôt.

## Validation et retour arrière

- **Validation** : lecture réussie dans chaque API indépendamment; pas de modification d’état. **Retour arrière** : révoquer jeton de lab et désactiver le client personnalisé.

## Si le problème n'est pas résolu

- [Proxmox VE — API Viewer](https://pve.proxmox.com/pve-docs/api-viewer/index.html)
- [OpenStack — API Reference](https://docs.openstack.org/api-ref/)
- [Proxmox VE — Guide](https://pve.proxmox.com/pve-docs/)