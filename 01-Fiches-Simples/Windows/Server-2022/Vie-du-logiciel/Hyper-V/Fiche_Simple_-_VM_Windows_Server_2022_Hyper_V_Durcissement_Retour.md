# Fiche_Simple_-_VM_Windows_Server_2022_Hyper_V_Durcissement_Retour.md

- **Environnement** : Hôte Hyper-V autonome Windows Server 2022 (hors cluster)
- **OS / Version** : Windows Server 2022 Standard ou Datacenter
- **Catégorie** : virtualisation / sécurité
- **Tags** : `hyper-v`, `windows-server-2022`, `virtualisation`, `vm`, `powershell`

---

## Problème précis à résoudre

Durcir l'hôte et maîtriser le retour arrière.

## 1. Hors-Production (Lab / Test / POC)

1. Lister les membres du groupe :
   ```powershell
   Get-LocalGroupMember -Group 'Hyper-V Administrators'
   ```
   👉 Explication : doit contenir seulement des comptes nominatifs.

2. Restreindre WinRM, RDP et ports de migration aux réseaux de gestion (pare-feu Windows).
   👉 Explication : réduit l'exposition.

3. Contrôler Defender et le pare-feu :
   ```powershell
   Get-MpComputerStatus | Select-Object AMServiceEnabled, RealTimeProtectionEnabled
   Get-NetFirewallProfile | Select-Object Name, Enabled
   ```
   👉 Explication : confirme que les protections sont actives.

4. Tester sauvegarde et restauration de VM en réseau isolé; documenter propriétaire, RPO/RTO et dépendances.
   👉 Explication : preuve de reprise.

5. Si l'installation du rôle échoue, vérifier prérequis, build et firmware.
   👉 Explication : causes les plus fréquentes.

## 2. Production — Contrôles

Auditer régulièrement les accès.

## 3. Production — Sécurité

- Comptes nominatifs, groupe Hyper-V Administrators restreint.
- N'activer que les services nécessaires.

## Validation et retour arrière

- **Validation** : Protections actives et restauration testée.
- **Retour arrière** : Avant retrait du rôle : arrêter ou migrer les VM, sauvegarder.

## Si le problème n'est pas résolu

- [Microsoft — installer Hyper-V](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/get-started/install-hyper-v)
- [Microsoft — créer un commutateur virtuel](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/get-started/create-a-virtual-switch-for-hyper-v-virtual-machines)
- [Guide complet — 6. Durcissement et retour arrière](../../../../../02-Fiches-Completes/Windows/Server-2022/Installation-Deploiement/55_Deploiement_Hyper_V_Windows_Server_2022.md#6-durcissement-et-retour-arriere)
