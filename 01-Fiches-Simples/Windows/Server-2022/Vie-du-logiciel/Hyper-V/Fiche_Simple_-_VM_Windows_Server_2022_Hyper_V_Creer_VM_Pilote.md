# 📄 Fiche_Simple_-_VM_Windows_Server_2022_Hyper_V_Creer_VM_Pilote.md

- **Environnement** : Hôte Hyper-V Windows Server 2022
- **OS / Version** : Windows Server 2022 Standard/Datacenter, Hyper-V installé
- **Catégorie** : Virtualisation / création de VM
- **Tags** : `windows-server-2022`, `hyper-v`, `vm`, `powershell`, `reseau`

---

## 🎯 Problème précis à résoudre

Créer une VM pilote connectée uniquement au switch et au datastore approuvés.

## 🧪 1. Hors-Production (Lab / Test / POC)

1. Contrôler hôte, switch et espace :
   ```powershell
   Get-VMHost
   Get-VMSwitch
   Get-Volume
   Get-FileHash D:\ISO\windows.iso -Algorithm SHA256
   ```
   👉 Explication : espace, mémoire et génération invitée; comparer le hash de l'ISO à celui publié.

2. Créer la VM génération 2 : GUI **Gestionnaire Hyper-V > Action > Nouveau > Ordinateur virtuel** (génération 2, mémoire, réseau = switch de lab, disque virtuel, ISO), ou :
   ```powershell
   New-VM -Name "VM-PILOTE" -Generation 2 -MemoryStartupBytes 4GB -NewVHDPath "D:\VM\VM-PILOTE.vhdx" -NewVHDSizeBytes 60GB -SwitchName "LAB-ISOLE"
   Set-VMProcessor VM-PILOTE -Count 2
   Add-VMDvdDrive -VMName VM-PILOTE -Path D:\ISO\windows.iso
   ```
   👉 Explication : remplacer chemins et ressources approuvées; pour Windows, ajuster `Set-VMFirmware` pour démarrer sur le DVD.

3. Démarrer l'installation et vérifier :
   ```powershell
   Start-VM VM-PILOTE
   Get-VM VM-PILOTE | Select-Object State, Uptime
   Get-VMNetworkAdapter VM-PILOTE
   ```
   👉 Explication : GUI **Connecter...** pour la console; contrôler réseau, stockage et journaux (**Observateur d'événements > Hyper-V-VMMS**).


## ⚡ 2. Production — Façon Simplifiée

1. Renseigner propriétaire, criticité, vCPU/RAM, emplacement VHDX, réseau/VLAN, démarrage et sauvegarde :
   ```powershell
   Set-VM VM-PILOTE -Notes "Propriétaire: EQUIPE; Criticité: MOYENNE" -AutomaticStartAction StartIfRunning
   Set-VMNetworkAdapterVlan -VMName VM-PILOTE -Access -VlanId 20
   ```
   👉 Explication : remplacer les valeurs; tester migration ou restauration seulement selon le design de l'hôte.


## 🔒 3. Production — Façon Sécurisée

- N'utiliser que l'ISO et les réseaux autorisés; limiter Hyper-V Administrators.
- Valider en fenêtre contrôlée toute modification d'un switch External susceptible de couper l'hôte.
- Ne pas considérer les checkpoints comme sauvegarde et ne pas supprimer un VHDX sans validation de son propriétaire.

## ✅ Validation et retour arrière

- **Validation** : VM `Running`, switch et VHDX attendus, ressources conformes, accès invité conforme.
- **Retour arrière** : arrêter la VM et retirer uniquement les ressources créées pour ce pilote après vérification du nom, chemin et propriétaire.

## 🔗 Si le problème n'est pas résolu

- [Microsoft — Créer une VM Hyper-V](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/get-started/create-a-virtual-machine-in-hyper-v)
- [Microsoft — Commutateur virtuel Hyper-V](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/get-started/create-a-virtual-switch-for-hyper-v-virtual-machines)