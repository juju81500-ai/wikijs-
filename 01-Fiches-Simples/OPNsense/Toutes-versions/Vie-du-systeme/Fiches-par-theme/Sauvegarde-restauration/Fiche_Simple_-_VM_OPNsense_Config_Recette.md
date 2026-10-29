# Fiche_Simple_-_VM_OPNsense_Config_Recette.md

- **Environnement** : Appliance OPNsense physique ou virtuelle, seule ou en HA
- **OS / Version** : OPNsense Community ou Business Edition maintenue
- **Catégorie** : pare-feu / sauvegarde-restauration
- **Tags** : `opnsense`, `sauvegarde`, `configuration`, `recette`, `ha`

---

## Problème précis à résoudre

Valider le fonctionnement et consigner l'opération.

## 1. Hors-Production (Lab / Test / POC)

1. Tester clients, routage, DHCP/DNS, NAT, VPN et règles de blocage/autorisation.
   👉 Explication : on valide le service rendu.

2. En HA, rétablir la synchronisation seulement après avoir confirmé les rôles et adresses propres des deux nœuds : **System > High Availability > Settings**.
   👉 Explication : une mauvaise synchro peut écraser une bonne configuration.

3. Consigner version, sauvegarde, résultat du test et prochaines échéances.
   👉 Explication : cette trace sert aux futurs incidents.

## 2. Production — Contrôles

Planifier la prochaine sauvegarde et le prochain test de restauration.

## 3. Production — Sécurité

- Ne pas réactiver la synchronisation HA sans avoir vérifié les rôles.

## Validation et retour arrière

- **Validation** : Tests réseau réussis et opération consignée.
- **Retour arrière** : Restaurer la configuration précédente via l'export ou le snapshot.

## Si le problème n'est pas résolu

- [OPNsense — Sauvegardes de configuration](https://docs.opnsense.org/manual/backups.html)
- [OPNsense — Snapshots système](https://docs.opnsense.org/manual/snapshots.html)
- [Guide complet — recette et clôture](../../../../../../02-Fiches-Completes/OPNsense/Toutes-versions/Autres/36_Sauvegarde_Restauration_Configuration_OPNsense.md#5-recette-et-cloture)
