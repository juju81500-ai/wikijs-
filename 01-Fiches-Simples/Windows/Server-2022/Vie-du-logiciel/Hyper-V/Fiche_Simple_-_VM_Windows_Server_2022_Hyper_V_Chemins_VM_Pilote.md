# Fiche_Simple_-_VM_Windows_Server_2022_Hyper_V_Chemins_VM_Pilote.md

- **Environnement** : Hôte Hyper-V autonome Windows Server 2022 (hors cluster)
- **OS / Version** : Windows Server 2022 Standard ou Datacenter
- **Catégorie** : virtualisation / VM
- **Tags** : `hyper-v`, `windows-server-2022`, `virtualisation`, `vm`, `powershell`

---

## Problème précis à résoudre

Fixer les chemins par défaut et créer une VM pilote unique.

## 1. Hors-Production (Lab / Test / POC)

1. Définir les chemins par défaut sur des volumes dédiés et sauvegardés (chemins d'exemple à remplacer) :
   ```powershell
   Set-VMHost -VirtualMachinePath 'D:\Hyper-V\VM' -VirtualHardDiskPath 'D:\Hyper-V\VHDX'
   ```
   👉 Explication : les configurations et disques sont stockés hors du volume système.

2. Créer la VM pilote (noms, tailles et commutateur d'exemple à remplacer) :
   ```powershell
   New-VM -Name 'VM-PILOTE' -Generation 2 -MemoryStartupBytes 4GB -NewVHDPath 'D:\Hyper-V\VHDX\VM-PILOTE.vhdx' -NewVHDSizeBytes 60GB -SwitchName 'vSwitch-Lab'
   Set-VMProcessor -VMName 'VM-PILOTE' -Count 2
   ```
   👉 Explication : (dérivé) VM génération 2 avec ressources documentées et switch approuvé.

3. GUI équivalente : **Hyper-V Manager > Action > New > Virtual Machine**.
   👉 Explication : même création par l'assistant.

4. Attacher une image OS vérifiée et ne pas utiliser les checkpoints comme sauvegarde.
   👉 Explication : les checkpoints ne protègent pas contre la perte de l'hôte.

## 2. Production — Contrôles

Activer Secure Boot si l'OS invité le supporte.

## 3. Production — Sécurité

- Une seule VM pilote, ressources documentées.

## Validation et retour arrière

- **Validation** : `Get-VM` affiche la VM pilote.
- **Retour arrière** : Supprimer la VM de test depuis Hyper-V Manager ou avec `Remove-VM`, après arrêt.

## Si le problème n'est pas résolu

- [Microsoft — installer Hyper-V](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/get-started/install-hyper-v)
- [Microsoft — créer un commutateur virtuel](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/get-started/create-a-virtual-switch-for-hyper-v-virtual-machines)
- [Guide complet — 4. Définir les chemins et créer une VM pilote](../../../../../02-Fiches-Completes/Windows/Server-2022/Installation-Deploiement/55_Deploiement_Hyper_V_Windows_Server_2022.md#4-definir-les-chemins-et-creer-une-vm-pilote)
