# Fiche_Simple_-_VM_Rocky_9_WireGuard_Prerequis_Limites

- **Environnement** : VM Rocky Linux 9 dédiée à un serveur WireGuard natif
- **OS / Version** : Rocky Linux 9; wireguard-tools issu d'EPEL, module noyau à vérifier sur l'hôte
- **Catégorie** : WireGuard natif / prérequis et limites

---

## Problème précis à résoudre

Valider le cadre avant d'installer un serveur WireGuard : OS, réseau, adressage, pairs.

## 1. Hors-Production (Lab / Test / POC)

1. Relever l'OS, le noyau et le réseau :
   ```bash
   cat /etc/os-release
   uname -r
   ip -br address
   ip route
   ```
   👉 Explication : Noter l'IP ou le FQDN joignable par les clients.

2. Vérifier que le noyau sait charger WireGuard :
   ```bash
   sudo modprobe wireguard && lsmod | grep wireguard
   ```
   👉 Explication : La commande ne doit pas retourner d'erreur; sinon s'arrêter et revoir le noyau/les dépôts avant de continuer.

3. Consigner les valeurs à décider :
   👉 Explication : VPN_SERVER_CIDR (adresse du serveur dans le tunnel, ex. réseau dédié), VPN_UDP_PORT (port UDP), CLIENT_VPN_ADDRESS (adresse /32 par pair), SERVER_ENDPOINT (IP ou FQDN public). Valeurs en majuscules à remplacer par le plan validé.

## 2. Production — Contrôles

Valider avec le propriétaire : pairs, routes, journalisation et accès de secours. Limites : WireGuard n'a pas de gestion d'utilisateurs ni de révocation centralisée (un pair = une clé publique); pas de HA native.

## 3. Production — Sécurité

- Une paire de clés par pair; les clés privées ne quittent jamais leur machine.

## Validation et retour arrière

- **Validation** : Plan d'adressage et liste de pairs approuvés; le module se charge.
- **Retour arrière** : Aucun changement : rien à restaurer.

## Si le problème n'est pas résolu

- [Étape suivante du guide](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/wireguard/fiche-simple-vm-rocky-9-wireguard-installer)
- [Fiche d'entrée du logiciel](/01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-wireguard)
- [WireGuard — installation officielle](https://www.wireguard.com/install/)
- [WireGuard — démarrage rapide](https://www.wireguard.com/quickstart/)