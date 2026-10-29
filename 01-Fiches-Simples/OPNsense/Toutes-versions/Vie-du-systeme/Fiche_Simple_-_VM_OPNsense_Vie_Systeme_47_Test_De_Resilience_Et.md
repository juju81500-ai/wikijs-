# Fiche_Simple_-_VM_OPNsense_Vie_Systeme_47_Test_De_Resilience_Et

- **Environnement** : Pare-feu OPNsense (VM ou matériel)
- **OS / Version** : OPNsense; étape 47 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `opnsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-47`

---

## Problème précis à résoudre

Vérifier le comportement lors d'une panne et les alertes.

## 1. Hors-Production (Lab / Test / POC)

1. Simuler la perte du WAN (débrancher ou désactiver l'interface virtuelle) et observer Système > Passerelles > Groupes / État.
   👉 Explication : la bascule ou l'alerte doit se produire.

2. Avec CARP (si HA) : Interfaces > Diagnostics > CARP, passer en maintenance, vérifier le basculement. En shell :
   ```sh
   sysctl net.inet.carp.demotion
   ifconfig vtnet0 | grep carp
   ```
   👉 Explication : montre la rétrogradation et l'état MASTER/BACKUP des VIP.

3. Confirmer que la supervision a émis l'alerte attendue.
   👉 Explication : valide la chaîne d'alerte de bout en bout.

## 2. Production — Contrôles

Documenter le temps de bascule mesuré.

## 3. Production — Sécurité

Réaliser le test hors des heures de production.

## Validation et retour arrière

- **Validation** : Alerte reçue et service rétabli dans le délai prévu.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Fiche détaillée : Appliance OPNsense CARP pfsync Tester Basculement](<../Vie-du-logiciel/CARP-pfsync-HA/Fiche_Simple_-_Appliance_OPNsense_CARP_pfsync_Tester_Basculement.md>)
- [Fiche détaillée : Appliance OPNsense CARP pfsync Preparer Basculement](<../Vie-du-logiciel/CARP-pfsync-HA/Fiche_Simple_-_Appliance_OPNsense_CARP_pfsync_Preparer_Basculement.md>)
- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire OPNsense](./Sommaire_-_Vie_du_systeme_OPNsense.md)
- [Documentation officielle](https://docs.opnsense.org/)
