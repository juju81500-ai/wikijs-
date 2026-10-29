# Fiche_Simple_-_VM_OPNsense_Config_Preparer.md

- **Environnement** : Appliance OPNsense physique ou virtuelle, seule ou en HA
- **OS / Version** : OPNsense Community ou Business Edition maintenue
- **Catégorie** : pare-feu / sauvegarde-restauration

---

## Problème précis à résoudre

Inventorier la configuration et garantir un accès console avant toute sauvegarde ou restauration.

## 1. Hors-Production (Lab / Test / POC)

1. Inventorier interfaces, VLAN, règles, NAT, certificats, VPN, comptes, plugins et rôle CARP : **Interfaces > Assignments**, **Firewall > Rules**, **VPN**.
   👉 Explication : on sait ce que la sauvegarde doit contenir.

2. Afficher la version installée : **Lobby > Dashboard**, ou en console :
   ```bash
   opnsense-version
   ```
   👉 Explication : la version source est nécessaire pour restaurer sur une release compatible.

3. Conserver un accès console et noter l'ordre des interfaces matérielles.
   👉 Explication : sur du nouveau matériel, les noms d'interface peuvent changer.

4. En HA, documenter l'état MASTER/BACKUP, les adresses propres et les VIP de chaque nœud.
   👉 Explication : la synchronisation ne remplace pas une copie indépendante.

## 2. Production — Contrôles

Prévoir un export par appliance, même en HA.

## 3. Production — Sécurité

- Traiter identifiants, clés privées, PSK et certificats de la configuration comme des secrets.

## Validation et retour arrière

- **Validation** : Inventaire à jour et accès console confirmé.
- **Retour arrière** : Aucune modification : rien à annuler.

## Si le problème n'est pas résolu

- [OPNsense — Sauvegardes de configuration](https://docs.opnsense.org/manual/backups.html)
- [OPNsense — Snapshots système](https://docs.opnsense.org/manual/snapshots.html)
- [Guide complet — préparer l'accès et le périmètre](/02-fiches-completes/opnsense/toutes-versions/autres/36-sauvegarde-restauration-configuration-opnsense#1-preparer-lacces-et-le-perimetre)