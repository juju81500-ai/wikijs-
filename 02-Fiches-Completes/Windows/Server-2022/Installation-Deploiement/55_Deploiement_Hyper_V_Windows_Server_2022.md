# Déployer Hyper-V sur Windows Server 2022

- **OS / Version** : Windows Server 2022 Datacenter ou Standard selon les droits de virtualisation
- **Type de fiche** : Installation/Déploiement
- **Périmètre** : Hôte Hyper-V autonome et VM pilote; hors cluster
- **Catégorie** : Virtualisation / infrastructure
- **Tags** : `hyper-v`, `windows-server-2022`, `virtualisation`, `vm`, `powershell`

## 1. Préparer l'hôte

Fiche simple : [préparer l'hôte](../../../../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/Hyper-V/Fiche_Simple_-_VM_Windows_Server_2022_Hyper_V_Preparer_Hote.md).

Vérifier le matériel, BIOS/UEFI, extensions de virtualisation, SLAT, mémoire, compatibilité des NIC/HBA, stockage et licence Windows Server. Planifier l'accès console hors bande, les VLANs, les adresses de gestion, l'espace pour les VM et la protection des sauvegardes. Une VM n'est pas une sauvegarde de son hôte.

Installer les correctifs et pilotes certifiés. Décider si l'hôte sera Server Core ou Desktop Experience et documenter les accès Hyper-V Administrators. Éviter les applications tierces qui dépendent du même hyperviseur matériel.

## 2. Installer le rôle Hyper-V

Fiche simple : [installer le rôle Hyper-V](../../../../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/Hyper-V/Fiche_Simple_-_VM_Windows_Server_2022_Hyper_V_Installer_Role.md).

Depuis une session PowerShell élevée :

```powershell
Install-WindowsFeature -Name Hyper-V -IncludeManagementTools -Restart
```

Après redémarrage, confirmer l'installation :

```powershell
Get-WindowsFeature Hyper-V
Get-VMHost
```

Ne pas configurer le rôle de manière distante avant d'avoir validé les privilèges, WinRM et le chemin de gestion.

## 3. Créer le réseau virtuel

Fiche simple : [créer le réseau virtuel](../../../../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/Hyper-V/Fiche_Simple_-_VM_Windows_Server_2022_Hyper_V_Reseau_Virtuel.md).

Lister les interfaces et convenir du NIC physique avec le réseau :

```powershell
Get-NetAdapter
Get-VMSwitch
```

Créer le commutateur virtuel en fonction du besoin validé : `External` pour raccorder des VM au réseau physique, `Internal` pour hôte/VM, ou `Private` pour échanges entre VM seulement. La création ou modification d'un commutateur External peut interrompre le réseau de l'hôte; intervenir avec accès console et fenêtre approuvée.

N'attribuer des VLANs qu'après confirmation du port physique et des VLAN autorisés. Séparer gestion, stockage, migration et réseaux invités selon le design; éviter de partager le NIC de gestion si le design ne le prévoit pas.

## 4. Définir les chemins et créer une VM pilote

Fiche simple : [définir les chemins et créer une VM pilote](../../../../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/Hyper-V/Fiche_Simple_-_VM_Windows_Server_2022_Hyper_V_Chemins_VM_Pilote.md).

Définir des volumes dédiés et sauvegardés pour les configurations et VHDX, puis configurer les chemins par défaut avec `Set-VMHost`. Pour une VM moderne, préférer génération 2, Secure Boot si compatible, démarrage contrôlé, ressources réalistes et VHDX dynamique/fixe selon les exigences d'IO et de capacité.

Créer une seule VM pilote dans Hyper-V Manager ou avec les cmdlets `New-VM`, `Set-VMProcessor` et `Set-VMMemory`. Attacher le switch explicitement approuvé, une image OS vérifiée et des ressources documentées. Ne pas activer les checkpoints comme mécanisme de sauvegarde.

## 5. Recette et exploitation

Fiche simple : [recetter et exploiter](../../../../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/Hyper-V/Fiche_Simple_-_VM_Windows_Server_2022_Hyper_V_Recette_Exploitation.md).

```powershell
Get-VM
Get-VMSwitch
Get-VMNetworkAdapter -VMName <VM-PILOTE>
Get-VMHardDiskDrive -VMName <VM-PILOTE>
```

Vérifier démarrage invité, réseau, stockage, intégration et journaux Hyper-V. Tester un arrêt contrôlé et confirmer que la VM redémarre automatiquement uniquement si la politique le demande. Configurer Windows Admin Center/Hyper-V Manager avec accès restreints, alertes de capacité et sauvegarde compatible application des VM.

## 6. Durcissement et retour arrière

Fiche simple : [durcir et prévoir le retour arrière](../../../../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/Hyper-V/Fiche_Simple_-_VM_Windows_Server_2022_Hyper_V_Durcissement_Retour.md).

- Utiliser des comptes nominatifs et un groupe restreint Hyper-V Administrators; auditer les accès.
- Restreindre WinRM, RDP et ports de migration aux réseaux de gestion.
- Maintenir Defender, pare-feu, Secure Boot et correctifs; n'activer que les services nécessaires.
- Tester sauvegarde et restauration de VM en réseau isolé; documenter propriétaire, RPO/RTO et dépendances.
- Si l'installation du rôle échoue, vérifier prérequis, build et firmware. Avant retrait du rôle, arrêter/migrer les VM, sauvegarder et suivre la procédure Microsoft.

## Sources

- [Microsoft — Installer Hyper-V sur Windows Server](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/get-started/install-hyper-v)
- [Microsoft — Créer une VM Hyper-V](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/get-started/create-a-virtual-machine-in-hyper-v)
- [Microsoft — Créer un commutateur virtuel Hyper-V](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/get-started/create-a-virtual-switch-for-hyper-v-virtual-machines)
- [Microsoft — Planifier le réseau Hyper-V](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/plan/plan-hyper-v-networking-in-windows-server)