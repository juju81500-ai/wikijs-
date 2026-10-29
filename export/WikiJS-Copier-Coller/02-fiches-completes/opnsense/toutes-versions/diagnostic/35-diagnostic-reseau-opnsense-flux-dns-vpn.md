# Diagnostiquer un incident réseau sur OPNsense

- **Type de fiche** : Diagnostic
- **Environnement** : Appliance OPNsense seule ou paire CARP; accès à la console recommandé
- **OS / Version** : OPNsense Community ou Business Edition maintenue
- **Rôle** : Localiser une panne de flux sans désactiver les protections du pare-feu

## 1. Délimiter le symptôme

Fiche simple : [délimiter le symptôme](/01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/fiches-par-theme/diagnostic/fiche-simple-appliance-opnsense-diagnostic-reseau-delimiter-symptome).

Noter source, destination, protocole/port, horaire, interface et dernier changement. Déterminer si la panne concerne un seul client, VLAN, service, tunnel ou tout le site. En environnement CARP, identifier le nœud MASTER et le dernier basculement.

Ne pas désactiver le filtrage global, vider toutes les tables d'état ou redémarrer les services avant d'avoir capturé les indices : ces actions peuvent masquer la cause et couper les sessions.

## 2. Contrôler l'état de l'appliance

Fiche simple : [contrôler l'état de l'appliance](/01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/fiches-par-theme/diagnostic/fiche-simple-appliance-opnsense-diagnostic-reseau-etat-appliance).

Dans l'interface : vérifier **System > Firmware > Status**, l'état matériel, **Interfaces > Overview**, les passerelles, CARP et les journaux système/firewall autour de l'heure concernée. Un audit de santé peut aider à repérer des fichiers ou dépendances altérés.

Depuis **Interfaces > Diagnostics**, utiliser Ping, DNS Lookup, Port Probe, Trace Route et Packet Capture. Choisir la bonne interface et l'adresse source; le pare-feu peut avoir une route ou une politique différente du client.

## 3. Suivre le flux de bout en bout

Fiche simple : [suivre le flux de bout en bout](/01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/fiches-par-theme/diagnostic/fiche-simple-appliance-opnsense-diagnostic-reseau-flux-bout-en-bout).

1. Vérifier l'adresse, le masque, la passerelle, le DNS et le VLAN du client.
2. Vérifier l'arrivée du paquet sur l'interface attendue avec une capture filtrée par hôte/port.
3. Lire le journal firewall et confirmer la règle correspondante, l'ordre, l'interface et l'état associé.
4. Vérifier route, passerelle, NAT et résolution DNS; tester depuis l'interface OPNsense avec la source appropriée.
5. Vérifier le retour côté serveur et les règles du chemin retour.

Capturer uniquement les champs et la durée nécessaires; les fichiers pcap peuvent contenir des données sensibles et doivent être protégés puis supprimés selon la politique.

## 4. Cas particuliers

Fiche simple : [traiter les cas DNS, VPN, CARP et MTU](/01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/fiches-par-theme/diagnostic/fiche-simple-appliance-opnsense-diagnostic-reseau-cas-particuliers).

- **DNS** : comparer résolution depuis le client et depuis OPNsense; vérifier les règles DNS, redirecteurs, DNSSEC et le service choisi.
- **VPN** : vérifier négociation, phase/SA, routes et sélecteurs avant de recréer les tunnels.
- **CARP/pfsync** : contrôler l'état des VIP et le lien de synchronisation sur les deux nœuds; éviter deux maîtres actifs.
- **MTU** : tester des paquets avec DF et tailles progressives; ne pas réduire globalement le MTU sans isoler le segment concerné.

## 5. Corriger et valider

Fiche simple : [corriger et valider](/01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/fiches-par-theme/diagnostic/fiche-simple-appliance-opnsense-diagnostic-reseau-corriger-valider).

Appliquer une modification minimale et documentée (route, règle précise ou configuration DNS), sauvegarder la configuration avant changement et garder un accès console. Tester succès et refus attendus depuis des postes représentatifs et confirmer le retour des journaux à un niveau normal.

## Sources

- [OPNsense — Outils de diagnostic réseau](https://docs.opnsense.org/manual/diagnostics_interfaces.html)
- [OPNsense — Dépannage général](https://docs.opnsense.org/troubleshooting.html)
- [OPNsense — Journaux système](https://docs.opnsense.org/manual/logging_system.html)
- [OPNsense — Haute disponibilité CARP](https://docs.opnsense.org/manual/hacarp.html)