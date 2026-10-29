# Fiche_Simple_-_VM_Multi-OS_Reseau_Diagnostic_Validation_Retour_Arriere.md

- **Environnement** : VM, poste, serveur, LXC Proxmox ou hôte Docker (Linux ou Windows)
- **OS / Version** : Debian 12/13, Ubuntu 24.04/26.04, Rocky Linux 9, Alpine Linux, Windows 10/11, Windows Server 2022/2025
- **Catégorie** : réseau / validation
- **Tags** : `reseau`, `diagnostic`, `multi-os`, `depannage`

---

## Problème précis à résoudre

Prouver que la panne est résolue et savoir revenir en arrière.

## 1. Hors-Production (Lab / Test / POC)

1. Refaire la chaîne **Lien → Adresse → Passerelle → Route → DNS → Port → Application** depuis le client touché.
   👉 Explication : on vérifie chaque couche dans l'ordre.

2. Exemple Linux de contrôle final (remplacer `192.0.2.10` et `srv1.example.test`) :
   ```bash
   ip -br address
   ip route get 192.0.2.10
   getent ahosts srv1.example.test
   nc -vz -w 3 192.0.2.10 443
   ```
   👉 Explication : regroupe adresse, route, DNS et port dans un seul contrôle.

3. Tester aussi depuis une machine qui ne doit pas être autorisée.
   👉 Explication : le refus attendu confirme que le filtrage est toujours actif.

4. Comparer avec le relevé « avant » et noter le changement dans le ticket.
   👉 Explication : garde une trace et facilite un éventuel retour arrière.

## 2. Production — Contrôles

Surveiller le service après correction.

## 3. Production — Sécurité

- Ne jamais vider les règles du pare-feu ni le désactiver pour « tester ».
- Tester uniquement une adresse et un port autorisés; aucun balayage de réseau.

## Validation et retour arrière

- **Validation** : La chaîne complète passe et le filtrage attendu est confirmé.
- **Retour arrière** : Si l'accès est perdu, restaurer le profil ou la configuration Proxmox précédente depuis la console, sans enchaîner d'autres changements.

## Si le problème n'est pas résolu

- [Netplan — documentation](https://netplan.readthedocs.io/)
- [Microsoft — cmdlets NetTCPIP](https://learn.microsoft.com/en-us/powershell/module/nettcpip/)
- [Guide complet — 10. Validation et retour arrière](../../../../02-Fiches-Completes/Transverses/Multi-OS/Diagnostic/15_Depannage_Reseau_Diagnostic_Complet_Multi_OS.md#10-validation-et-retour-arriere)
