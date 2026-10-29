# Fiche_Simple_-_VM_Windows_Server_2022_Hyper_V_Reseau_Virtuel.md

- **Environnement** : Hôte Hyper-V autonome Windows Server 2022 (hors cluster)
- **OS / Version** : Windows Server 2022 Standard ou Datacenter
- **Catégorie** : virtualisation / réseau
- **Tags** : `hyper-v`, `windows-server-2022`, `virtualisation`, `vm`, `powershell`

---

## Problème précis à résoudre

Créer le commutateur virtuel adapté au besoin.

## 1. Hors-Production (Lab / Test / POC)

1. Lister cartes et commutateurs :
   ```powershell
   Get-NetAdapter
   Get-VMSwitch
   ```
   👉 Explication : choisir le NIC physique avec l'équipe réseau.

2. GUI : **Hyper-V Manager > Virtual Switch Manager > New virtual network switch** (External, Internal ou Private).
   👉 Explication : External = réseau physique; Internal = hôte et VM; Private = VM seulement.

3. Ligne de commande pour un commutateur interne d'exemple (nom à remplacer) :
   ```powershell
   New-VMSwitch -Name 'vSwitch-Lab' -SwitchType Internal
   ```
   👉 Explication : (dérivé de la documentation Microsoft) crée un commutateur sans toucher au réseau physique.

4. Attribuer des VLANs seulement après confirmation du port physique et des VLAN autorisés.
   👉 Explication : évite les coupures.

## 2. Production — Contrôles

Séparer gestion, stockage, migration et réseaux invités selon le design.

## 3. Production — Sécurité

- Créer un commutateur External peut interrompre le réseau de l'hôte : accès console et fenêtre approuvée.

## Validation et retour arrière

- **Validation** : `Get-VMSwitch` affiche le commutateur attendu.
- **Retour arrière** : Supprimer le commutateur de test : `Remove-VMSwitch -Name 'vSwitch-Lab'`.

## Si le problème n'est pas résolu

- [Microsoft — installer Hyper-V](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/get-started/install-hyper-v)
- [Microsoft — créer un commutateur virtuel](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/get-started/create-a-virtual-switch-for-hyper-v-virtual-machines)
- [Guide complet — 3. Créer le réseau virtuel](../../../../../02-Fiches-Completes/Windows/Server-2022/Installation-Deploiement/55_Deploiement_Hyper_V_Windows_Server_2022.md#3-creer-le-reseau-virtuel)
