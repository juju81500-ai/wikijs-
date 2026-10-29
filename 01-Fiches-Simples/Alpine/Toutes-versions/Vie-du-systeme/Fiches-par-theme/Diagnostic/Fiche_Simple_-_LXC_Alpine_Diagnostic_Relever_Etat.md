# Fiche_Simple_-_LXC_Alpine_Diagnostic_Relever_Etat.md

- **Environnement** : nœud Proxmox VE et console du CT Alpine
- **OS / Version** : branche Alpine maintenue
- **Catégorie** : diagnostic / relevé d'état
- **Tags** : `alpine`, `proxmox`, `lxc`, `pct`, `ip`, `openrc`

---

## Problème précis à résoudre

Comparer la configuration déclarée par Proxmox avec l'état observé dans le conteneur avant d'isoler une panne.

## 1. Hors-Production (Lab / Test / POC)

1. Sur l'hôte Proxmox :
   ```bash
   pct config CTID
   pct status CTID
   ```
   👉 Explication : relever bridge, VLAN tag, IP, passerelle, DNS et état du CT.

2. Dans le conteneur Alpine :
   ```sh
   cat /etc/alpine-release
   ip -br link
   ip -br addr
   ip route
   cat /etc/resolv.conf
   rc-status
   ```
   👉 Explication : comparer avec le plan réseau et une machine fonctionnelle du même segment.

## 2. Production — Contrôles

Confirmer CTID, nœud, heure, segment et sources des informations; masquer les informations sensibles avant partage.

## 3. Production — Sécurité

- Ne pas publier des sorties complètes contenant adresses ou détails de topologie hors des canaux autorisés.
- Ne pas confondre état de l'hôte avec état du CT.
- Ne pas lancer de commande modificatrice durant le relevé initial.
- Ne pas utiliser un CTID avant de confirmer l'hôte et le conteneur ciblés.

## Validation et retour arrière

- **Validation** : les valeurs Proxmox et Alpine sont rapprochées du plan réseau avec les écarts identifiés.
- **Arrêt** : ne pas corriger avant d'avoir confirmé quel composant possède la configuration divergente.

## Si le problème n'est pas résolu

- [Proxmox VE — documentation](https://pve.proxmox.com/pve-docs/)
- [Alpine Linux — documentation](https://docs.alpinelinux.org/)
- [Guide complet de diagnostic LXC Alpine](../../../../../../02-Fiches-Completes/Alpine/Toutes-versions/Diagnostic/17_Diagnostic_LXC_Alpine_Reseau_Services.md#2-relever-letat-proxmox-et-alpine)
