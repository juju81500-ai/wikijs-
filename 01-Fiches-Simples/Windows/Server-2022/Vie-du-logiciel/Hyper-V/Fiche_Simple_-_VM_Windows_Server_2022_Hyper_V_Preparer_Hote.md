# Fiche_Simple_-_VM_Windows_Server_2022_Hyper_V_Preparer_Hote.md

- **Environnement** : Hôte Hyper-V autonome Windows Server 2022 (hors cluster)
- **OS / Version** : Windows Server 2022 Standard ou Datacenter
- **Catégorie** : virtualisation / prérequis
- **Tags** : `hyper-v`, `windows-server-2022`, `virtualisation`, `vm`, `powershell`

---

## Problème précis à résoudre

Vérifier matériel, licence et correctifs avant d'installer Hyper-V.

## 1. Hors-Production (Lab / Test / POC)

1. Lire les capacités de virtualisation de l'hôte :
   ```powershell
   systeminfo | Select-String 'Hyper-V','Virtualization'
   ```
   👉 Explication : affiche si les extensions de virtualisation et SLAT sont disponibles.

2. Relever la mémoire, les disques et les cartes réseau :
   ```powershell
   Get-ComputerInfo -Property CsTotalPhysicalMemory
   Get-PhysicalDisk | Format-Table FriendlyName, Size, HealthStatus
   Get-NetAdapter
   ```
   👉 Explication : confirme capacité, santé du stockage et NIC disponibles.

3. **Paramètres > Windows Update** (ou WSUS) : installer les correctifs et pilotes certifiés.
   👉 Explication : hôte à jour avant le rôle.

4. Décider Server Core ou Desktop Experience, planifier console hors bande, VLANs, adresses de gestion, espace VM et protection des sauvegardes.
   👉 Explication : ces choix sont documentés avant l'installation.

## 2. Production — Contrôles

Documenter le groupe Hyper-V Administrators; une VM n'est pas une sauvegarde de son hôte.

## 3. Production — Sécurité

- Éviter les applications tierces dépendant du même hyperviseur matériel.

## Validation et retour arrière

- **Validation** : Matériel, licence et correctifs validés.
- **Retour arrière** : Aucune modification ici.

## Si le problème n'est pas résolu

- [Microsoft — installer Hyper-V](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/get-started/install-hyper-v)
- [Microsoft — créer un commutateur virtuel](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/get-started/create-a-virtual-switch-for-hyper-v-virtual-machines)
- [Guide complet — 1. Préparer l'hôte](../../../../../02-Fiches-Completes/Windows/Server-2022/Installation-Deploiement/55_Deploiement_Hyper_V_Windows_Server_2022.md#1-preparer-lhote)
