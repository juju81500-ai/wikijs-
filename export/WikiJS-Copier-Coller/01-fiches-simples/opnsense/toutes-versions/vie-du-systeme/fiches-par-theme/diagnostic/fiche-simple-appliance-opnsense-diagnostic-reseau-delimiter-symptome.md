# Fiche_Simple_-_Appliance_OPNsense_Diagnostic_Reseau_Delimiter_Symptome.md

- **Environnement** : Appliance OPNsense seule ou paire CARP; accès console recommandé
- **OS / Version** : OPNsense Community ou Business Edition maintenue
- **Catégorie** : pare-feu / diagnostic

---

## Problème précis à résoudre

Décrire précisément la panne avant d'agir.

## 1. Hors-Production (Lab / Test / POC)

1. Noter source, destination, protocole/port, horaire, interface et dernier changement dans le ticket.
   👉 Explication : permet de reproduire et de corréler avec les journaux.

2. Déterminer si la panne touche un client, un VLAN, un service, un tunnel ou tout le site.
   👉 Explication : cadre la zone à tester.

3. En CARP : **Interfaces > Virtual IPs > Status** pour identifier le nœud MASTER et le dernier basculement.
   👉 Explication : évite de diagnostiquer le mauvais nœud.

## 2. Production — Contrôles

Ne pas désactiver le filtrage global, vider les tables d'état ni redémarrer les services avant d'avoir capturé les indices.

## 3. Production — Sécurité

- Ces actions masquent la cause et coupent des sessions.

## Validation et retour arrière

- **Validation** : Symptôme décrit dans le ticket.
- **Retour arrière** : Aucune modification ici.

## Si le problème n'est pas résolu

- [OPNsense — outils de diagnostic](https://docs.opnsense.org/manual/diagnostics_interfaces.html)
- [OPNsense — dépannage](https://docs.opnsense.org/troubleshooting.html)
- [Guide complet — 1. Délimiter le symptôme](/02-fiches-completes/opnsense/toutes-versions/diagnostic/35-diagnostic-reseau-opnsense-flux-dns-vpn#1-delimiter-le-symptome)