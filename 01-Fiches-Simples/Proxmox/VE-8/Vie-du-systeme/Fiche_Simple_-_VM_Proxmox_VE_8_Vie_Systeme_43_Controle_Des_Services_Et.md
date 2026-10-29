# Fiche_Simple_-_VM_Proxmox_VE_8_Vie_Systeme_43_Controle_Des_Services_Et

- **Environnement** : Hôte Proxmox VE 8 (hyperviseur)
- **OS / Version** : Proxmox VE 8; étape 43 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `proxmoxve8`, `vie-du-systeme`, `cycle-de-vie`, `etape-43`

---

## Problème précis à résoudre

Vérifier que seuls les services attendus tournent.

## 1. Hors-Production (Lab / Test / POC)

1. Lister les services actifs et en échec :
   ```bash
   systemctl list-units --type=service --state=running
   systemctl --failed
   ```
   👉 Explication : comparer à la liste attendue (pve-cluster, pvedaemon, pveproxy, pvestatd, corosync si cluster).

2. Lister les ports en écoute :
   ```bash
   ss -tulpn
   ```
   👉 Explication : comparer à la liste autorisée.

3. Contrôler le pare-feu et l'état de santé :
   ```bash
   pve-firewall status
   pvecm status
   pveversion
   ```
   👉 Explication : vérifie les services Proxmox et le quorum.

## 2. Production — Contrôles

Comparer à la baseline de l'étape 25.

## 3. Production — Sécurité

Corriger tout écart avant production.

## Validation et retour arrière

- **Validation** : Aucun service en échec; ports conformes.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Proxmox VE 8](./Sommaire_-_Vie_du_systeme_Proxmox_VE_8.md)
- [Documentation officielle](https://pve.proxmox.com/pve-docs/)
