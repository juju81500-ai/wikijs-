# Fiche_Simple_-_VM_OPNsense_Vie_Systeme_17_Resolution_De_Noms_Client

- **Environnement** : Pare-feu OPNsense (VM ou matériel)
- **OS / Version** : OPNsense; étape 17 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `opnsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-17`

---

## Problème précis à résoudre

Configurer les serveurs DNS utilisés par le pare-feu et les clients.

## 1. Hors-Production (Lab / Test / POC)

1. Renseigner Système > Paramètres > Général > Serveurs DNS (ex. `IP_DNS1`, `IP_DNS2`) et décocher « Autoriser le remplacement par le DHCP du WAN » si les DNS sont imposés.
   👉 Explication : `IP_DNS1` et `IP_DNS2` sont les résolveurs internes ou publics choisis.

2. Activer le résolveur local dans Services > Unbound DNS > Général (Activer, interfaces LAN, DNSSEC).
   👉 Explication : les clients interrogent le pare-feu qui résout ou relaie.

3. Tester en shell :
   ```sh
   drill exemple.fr @127.0.0.1
   cat /etc/resolv.conf
   ```
   👉 Explication : prouve la résolution par Unbound et affiche les serveurs configurés.

## 2. Production — Contrôles

Avoir deux résolveurs et documenter leur propriétaire.

## 3. Production — Sécurité

Activer DNSSEC et ne pas autoriser les requêtes DNS depuis le WAN.

## Validation et retour arrière

- **Validation** : `drill` renvoie une réponse `NOERROR`.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire OPNsense](./Sommaire_-_Vie_du_systeme_OPNsense.md)
- [Documentation officielle](https://docs.opnsense.org/)
