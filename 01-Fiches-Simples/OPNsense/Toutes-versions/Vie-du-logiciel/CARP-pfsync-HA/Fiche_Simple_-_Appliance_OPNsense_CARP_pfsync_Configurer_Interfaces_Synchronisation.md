# Fiche_Simple_-_Appliance_OPNsense_CARP_pfsync_Configurer_Interfaces_Synchronisation.md

- **Environnement** : Deux appliances OPNsense en haute disponibilité (CARP et pfsync)
- **OS / Version** : OPNsense (toutes versions compatibles entre les deux nœuds)
- **Catégorie** : pare-feu / haute disponibilité
- **Tags** : `opnsense`, `carp`, `pfsync`, `ha`, `firewall`

---

## Problème précis à résoudre

Configurer interfaces, pfsync et synchronisation de configuration sur les deux nœuds.

## 1. Hors-Production (Lab / Test / POC)

1. Configurer IP fixes et rôles d'interface sur les deux équipements : **Interfaces > [nom de l'interface]**.
   👉 Explication : les adresses doivent correspondre au plan.

2. Sur le nœud principal : **System > High Availability > Settings**, activer **Synchronize states** (pfsync) et choisir l'interface privée dédiée, avec l'adresse du pair.
   👉 Explication : ne jamais utiliser le WAN ou le réseau public pour pfsync.

3. Activer la synchronisation de configuration : renseigner l'adresse de l'interface dédiée du secondaire et le compte de synchronisation, puis sélectionner uniquement les composants à synchroniser.
   👉 Explication : limite la synchronisation au nécessaire.

4. Créer un compte de synchronisation dédié : **System > Access > Users**, protégé par un secret fort.
   👉 Explication : ne pas réutiliser un compte administrateur personnel.

5. Autoriser pfsync entre les deux nœuds dans **Firewall > Rules** de l'interface dédiée (protocole pfsync, sources limitées aux pairs).
   👉 Explication : sans cette règle l'état ne se synchronise pas.

## 2. Production — Contrôles

Consigner les composants synchronisés et le compte utilisé; tester la synchronisation avant de créer les VIP.

## 3. Production — Sécurité

- Limiter la règle pfsync aux deux pairs sur l'interface dédiée.
- Secret du compte de synchronisation hors documentation.

## Validation et retour arrière

- **Validation** : les états et la configuration se synchronisent du principal vers le secondaire.
- **Retour arrière** : désactiver la synchronisation dans **High Availability > Settings** et restaurer la configuration sauvegardée.

## Si le problème n'est pas résolu

- [OPNsense — haute disponibilité](https://docs.opnsense.org/manual/hacarp.html)
- [OPNsense — haute disponibilité](https://docs.opnsense.org/manual/hacarp.html)
- [Guide complet](../../../../../02-Fiches-Completes/OPNsense/Toutes-versions/Autres/10_Pare_Feu_Appliance_OPNsense_CARP_pfSync_HA.md#2-configurer-les-interfaces-et-la-synchronisation)
