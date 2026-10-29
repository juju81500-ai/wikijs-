# Fiche_Simple_-_VM_ESXi_8_VMware_vSphere_Maintenance_Hote

- **Environnement** : vCenter Server 8.x et hôte ESXi 8.x de laboratoire
- **OS / Version** : VMware vSphere 8.x
- **Catégorie** : virtualisation / maintenance

---

## Problème précis à résoudre

Passer un hôte ESXi de laboratoire en maintenance puis le réintégrer sans supposer que les VM ont été migrées ou arrêtées.

## 1. Hors-Production (Lab / Test / POC)

1. Dans vSphere Client : hôte > **Actions > Mode de maintenance > Passer en mode maintenance**. Confirmer seulement après arrêt/migration des VM jetables.
   👉 Explication : migration DRS/vMotion dépend des réglages; un hôte autonome ne garantit pas la disponibilité des VM.
2. Variante PowerCLI documentée sur l'hôte jetable après vérification de son nom :
   ```powershell
   $vmhost = Get-VMHost -Name 'ESXI_LAB_FQDN'
   Set-VMHost -VMHost $vmhost -State Maintenance
   ```
   👉 Explication : placeholder à remplacer; action modifiant l’état opérationnel, pas à appliquer en production avec cette fiche.
3. Contrôle en lecture seule : `esxcli system maintenanceMode get`.
   👉 Explication : affiche l'état courant sans le changer.
4. Après le test, hôte > **Actions > Mode de maintenance > Quitter le mode de maintenance**; attendre l'état connecté, vérifier alarmes et réseaux avant retour des VM.
   👉 Explication : ne pas réactiver les charges si stockage, réseau ou gestion ne sont pas sains.

## 2. Production — Contrôles

- Valider approbation, sauvegarde, capacité, cluster, compatibilité et plan de remise en service. Le mode maintenance ne réalise pas un patch/upgrade.

## 3. Production — Sécurité

- Préserver l’accès console hors bande; ne pas forcer l’arrêt des VM ni contourner les alarmes.

## Validation et retour arrière

- **Validation** : état maintenance conforme puis hôte connecté sans défaut non résolu; VM vérifiées. **Retour arrière** : ne pas réintroduire l’hôte ni relancer VM à l’aveugle; suivre plan et support.

## Si le problème n'est pas résolu

- [Broadcom PowerCLI — Set-VMHost](https://developer.broadcom.com/powercli/latest/vmware.vimautomation.core/commands/set-vmhost)
- [Broadcom — Maintenance ESXi avec ESXCLI](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere-sdks-tools/7-0/esxcli-concepts-and-examples-7-0/managing-hosts/enter-and-exit-maintenance-mode-with-esxcli.html)
- [Broadcom ESXCLI — référence actuelle](https://developer.broadcom.com/xapis/esxcli-command-reference/latest/)
- [Broadcom — Documentation vSphere 8](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0.html)