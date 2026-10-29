# Fiche_Simple_-_VM_ESXi_8_VMware_vSphere_HA

- **Environnement** : vCenter Server Appliance 8.x et hôtes ESXi 8.x de laboratoire
- **OS / Version** : VMware vSphere 8.x
- **Catégorie** : virtualisation / vCenter

---

## Problème précis à résoudre

Activer vSphere HA pour redémarrer automatiquement les VM d'un hôte défaillant.

## 1. Hors-Production (Lab / Test / POC)

1. Dans vSphere Client : sélectionner le cluster > **Configurer > Services > Disponibilité vSphere > Modifier**, activer **Surveillance de l'hôte**.
   👉 Explication : HA nécessite au moins deux hôtes et un stockage partagé.
2. Régler **Contrôle d'admission** : nombre d'hôtes tolérés ou capacité réservée ; régler la réponse à l'isolement de l'hôte.
   👉 Explication : le contrôle d'admission garantit la capacité de redémarrage.
3. Équivalent PowerCLI :
   ```powershell
   Set-Cluster -Cluster 'CLUSTER_A_REMPLACER' -HAEnabled:$true -Confirm:$false
   ```
   👉 Explication : `CLUSTER_A_REMPLACER` est le nom du cluster.
4. Tester en lab en simulant la panne d'un hôte.
   👉 Explication : vérifier le redémarrage des VM dans l'ordre voulu.

## 2. Production — Contrôles

- Réseau de gestion redondant, datastores de heartbeat, capacité suffisante.

## 3. Production — Sécurité

- Limiter le droit de modifier le cluster ; journaliser les modifications.

## Validation et retour arrière

- **Validation** : l'état HA du cluster est configuré et le test de panne redémarre les VM. **Retour arrière** : désactiver HA : `Set-Cluster -HAEnabled:$false`.

## Si le problème n'est pas résolu

- [Fiche d'entrée VMware vSphere](/01-fiches-simples/logiciels/03-virtualisation-et-conteneurisation/fiche-logiciel-vmware-vsphere)
- [Broadcom PowerCLI — Set-Cluster](https://developer.broadcom.com/powercli/latest/vmware.vimautomation.core/commands/set-cluster)
- [Broadcom — Documentation vSphere 8](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0.html)