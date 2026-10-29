# Fiche_Simple_-_VM_Multi-OS_Reseau_Diagnostic_Adresse_Passerelle.md

- **Environnement** : VM, poste, serveur, LXC Proxmox ou hôte Docker (Linux ou Windows)
- **OS / Version** : Debian 12/13, Ubuntu 24.04/26.04, Rocky Linux 9, Alpine Linux, Windows 10/11, Windows Server 2022/2025
- **Catégorie** : réseau / couche 3
- **Tags** : `reseau`, `diagnostic`, `multi-os`, `depannage`

---

## Problème précis à résoudre

Contrôler l'adresse IP, le préfixe et la passerelle utilisés par la machine.

## 1. Hors-Production (Lab / Test / POC)

1. Linux : lire adresses, routes et route choisie vers la destination (remplacer `192.0.2.10` par l'IP à joindre) :
   ```bash
   ip -br address
   ip route
   ip route get 192.0.2.10
   ```
   👉 Explication : on vérifie que le préfixe est correct et que la route sélectionnée passe par l'interface attendue.

2. Windows : lire la configuration et la route par défaut :
   ```powershell
   Get-NetIPConfiguration
   Get-NetRoute -DestinationPrefix 0.0.0.0/0
   ```
   👉 Explication : on confirme la passerelle par défaut et l'absence de route inattendue.

3. Tester la passerelle (remplacer `192.0.2.1` par la vraie passerelle) :
   ```bash
   ping -c 3 192.0.2.1
   ```
   👉 Explication : un retour confirme la couche 2/3 locale; un échec seul ne prouve rien car ICMP peut être filtré.

4. Équivalent Windows :
   ```powershell
   Test-Connection 192.0.2.1 -Count 3
   ```
   👉 Explication : même test de la passerelle sous PowerShell.

## 2. Production — Contrôles

Vérifier l'absence de conflit IP et que l'adresse respecte le plan d'adressage; ne jamais utiliser `192.0.2.0/24` (documentation) en production.

## 3. Production — Sécurité

- Ne jamais vider les règles du pare-feu ni le désactiver pour « tester ».
- Tester uniquement une adresse et un port autorisés; aucun balayage de réseau.

## Validation et retour arrière

- **Validation** : Adresse, préfixe et passerelle correspondent au plan réseau.
- **Retour arrière** : Aucune modification ici; ne corriger qu'avec le gestionnaire réseau actif, profil sauvegardé au préalable.

## Si le problème n'est pas résolu

- [Netplan — documentation](https://netplan.readthedocs.io/)
- [Microsoft — cmdlets NetTCPIP](https://learn.microsoft.com/en-us/powershell/module/nettcpip/)
- [Guide complet — 4. Étape 2 — Vérifier adresse, masque et passerelle](../../../../02-Fiches-Completes/Transverses/Multi-OS/Diagnostic/15_Depannage_Reseau_Diagnostic_Complet_Multi_OS.md#4-etape-2-verifier-adresse-masque-et-passerelle)
