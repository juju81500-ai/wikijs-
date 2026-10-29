# Fiche_Simple_-_VM_ESXi_8_VMware_vSphere_DRS

- **Environnement** : vCenter Server Appliance 8.x et hôtes ESXi 8.x de laboratoire
- **OS / Version** : VMware vSphere 8.x
- **Catégorie** : virtualisation / vCenter
- **Tags** : `vmware-vsphere`, `vsphere8`, `vcenter`, `drs`, `cluster`, `equilibrage`

---

## Problème précis à résoudre

Activer DRS pour équilibrer la charge des VM entre les hôtes d'un cluster.

## 1. Hors-Production (Lab / Test / POC)

1. Dans vSphere Client : cluster > **Configurer > Services > vSphere DRS > Modifier**, activer DRS.
   👉 Explication : DRS nécessite vMotion fonctionnel entre les hôtes (voir la fiche vMotion_VMkernel).
2. Choisir le niveau d'automatisation (manuel, partiellement automatisé, entièrement automatisé) et le seuil de migration.
   👉 Explication : démarrer en manuel ou partiellement automatisé, puis passer en automatique après observation.
3. Équivalent PowerCLI :
   ```powershell
   Set-Cluster -Cluster 'CLUSTER_A_REMPLACER' -DrsEnabled:$true -DrsAutomationLevel PartiallyAutomated -Confirm:$false
   ```
   👉 Explication : `CLUSTER_A_REMPLACER` est le nom du cluster.
4. Contrôler les recommandations : onglet **Surveiller > vSphere DRS**.
   👉 Explication : appliquer les migrations validées.

## 2. Production — Contrôles

- Hôtes compatibles CPU (EVC si besoin), réseau vMotion dédié.

## 3. Production — Sécurité

- Droits restreints, règles d'affinité documentées.

## Validation et retour arrière

- **Validation** : recommandations visibles et migrations réussies. **Retour arrière** : DRS en mode manuel ou désactivé : `Set-Cluster -DrsEnabled:$false`.

## Si le problème n'est pas résolu

- [Fiche d'entrée VMware vSphere](../../../../Logiciels/03-Virtualisation-et-conteneurisation/Fiche_Logiciel_-_VMware-vSphere.md)
- [Fiche voisine — vMotion VMkernel](Fiche_Simple_-_VM_ESXi_8_VMware_vSphere_vMotion_VMkernel.md)
- [Broadcom PowerCLI — Set-Cluster](https://developer.broadcom.com/powercli/latest/vmware.vimautomation.core/commands/set-cluster)
- [Broadcom — Documentation vSphere 8](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0.html)
