# Fiche_Simple_-_VM_Multi-OS_Reseau_Diagnostic_Chemin_Destination.md

- **Environnement** : VM, poste, serveur, LXC Proxmox ou hôte Docker (Linux ou Windows)
- **OS / Version** : Debian 12/13, Ubuntu 24.04/26.04, Rocky Linux 9, Alpine Linux, Windows 10/11, Windows Server 2022/2025
- **Catégorie** : réseau / routage
- **Tags** : `reseau`, `diagnostic`, `multi-os`, `depannage`

---

## Problème précis à résoudre

Savoir par où passent les paquets vers la destination et où ils s'arrêtent.

## 1. Hors-Production (Lab / Test / POC)

1. Linux : comparer la route choisie avec l'interface attendue (remplacer `192.0.2.10` par la destination) :
   ```bash
   ip route get 192.0.2.10
   ```
   👉 Explication : montre l'interface et la passerelle réellement utilisées.

2. Linux : suivre le chemin :
   ```bash
   tracepath 192.0.2.10
   ```
   👉 Explication : affiche les sauts; un saut muet n'est pas forcément une panne car certains routeurs filtrent les sondes.

3. Windows :
   ```powershell
   tracert -d 192.0.2.10
   ```
   👉 Explication : même suivi de chemin sans résolution de noms.

4. Si la passerelle répond mais pas le réseau distant, demander au propriétaire du réseau de contrôler routage, ACL, VPN, VLAN et routes de retour.
   👉 Explication : la cause est au-delà de la machine locale.

## 2. Production — Contrôles

Tester seulement une destination autorisée; documenter le dernier saut atteint.

## 3. Production — Sécurité

- Ne jamais vider les règles du pare-feu ni le désactiver pour « tester ».
- Tester uniquement une adresse et un port autorisés; aucun balayage de réseau.

## Validation et retour arrière

- **Validation** : Le chemin attendu est confirmé ou le dernier saut atteint est noté pour l'escalade.
- **Retour arrière** : Aucune modification ici.

## Si le problème n'est pas résolu

- [Netplan — documentation](https://netplan.readthedocs.io/)
- [Microsoft — cmdlets NetTCPIP](https://learn.microsoft.com/en-us/powershell/module/nettcpip/)
- [Guide complet — 5. Étape 3 — Vérifier le chemin vers la destination](../../../../02-Fiches-Completes/Transverses/Multi-OS/Diagnostic/15_Depannage_Reseau_Diagnostic_Complet_Multi_OS.md#5-etape-3-verifier-le-chemin-vers-la-destination)
