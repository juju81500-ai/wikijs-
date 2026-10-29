# Fiche_Simple_-_Appliance_OPNsense_Diagnostic_Reseau_Flux_Bout_En_Bout.md

- **Environnement** : Appliance OPNsense seule ou paire CARP; accès console recommandé
- **OS / Version** : OPNsense Community ou Business Edition maintenue
- **Catégorie** : pare-feu / flux
- **Tags** : `opnsense`, `diagnostic`, `reseau`, `firewall`, `dns`, `vpn`

---

## Problème précis à résoudre

Suivre un paquet du client au serveur.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier adresse, masque, passerelle, DNS et VLAN du client.
   👉 Explication : premier point de panne.

2. **Interfaces > Diagnostics > Packet Capture** : filtrer par hôte et port pour confirmer l'arrivée du paquet. Équivalent shell (interface `igb0` et adresse d'exemple à remplacer) :
   ```sh
   tcpdump -ni igb0 host 192.0.2.10 and port 443
   ```
   👉 Explication : (dérivé) montre si le paquet arrive sur l'interface attendue; arrêter avec Ctrl+C.

3. **Firewall > Log Files > Live View** : confirmer la règle, l'ordre, l'interface et l'état.
   👉 Explication : identifie la règle qui laisse passer ou bloque.

4. Vérifier route, passerelle, NAT (**Firewall > NAT**) et DNS, depuis l'interface avec la bonne source.
   👉 Explication : écarte les erreurs de routage.

5. Contrôler le retour côté serveur et les règles du chemin retour.
   👉 Explication : un flux asymétrique est bloqué.

## 2. Production — Contrôles

Limiter durée et champs des captures; protéger puis supprimer les fichiers pcap selon la politique.

## 3. Production — Sécurité

- Un pcap peut contenir des données sensibles.

## Validation et retour arrière

- **Validation** : Le point de rupture du flux est identifié.
- **Retour arrière** : Aucune modification ici.

## Si le problème n'est pas résolu

- [OPNsense — outils de diagnostic](https://docs.opnsense.org/manual/diagnostics_interfaces.html)
- [OPNsense — dépannage](https://docs.opnsense.org/troubleshooting.html)
- [Guide complet — 3. Suivre le flux de bout en bout](../../../../../../02-Fiches-Completes/OPNsense/Toutes-versions/Diagnostic/35_Diagnostic_Reseau_OPNsense_Flux_DNS_VPN.md#3-suivre-le-flux-de-bout-en-bout)
