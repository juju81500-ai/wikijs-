# Fiche_Simple_-_VM_Debian_13_Kea_Cadrer.md

- **Environnement** : VM Debian 13 serveur DHCPv4 sur un VLAN de test isolé
- **OS / Version** : Debian 13 Trixie x86-64; ISC Kea (canal stable)
- **Catégorie** : réseau / DHCP
- **Tags** : `debian13`, `kea`, `dhcpv4`, `isc`, `reseau`

---

## Problème précis à résoudre

Définir le périmètre du serveur DHCPv4 et vérifier les prérequis avant toute installation, sans perturber un réseau réel.

## 1. Hors-Production (Lab / Test / POC)

1. Identifier l'interface du VLAN servi et son adresse (l'interface `ens18` est un exemple à remplacer) :
   ```bash
   ip -br address
   ip route
   ```
   👉 Explication : le serveur doit avoir une adresse statique dans le sous-réseau servi.

2. Noter la plage approuvée, la passerelle et le DNS. Les adresses `192.0.2.0/24` sont réservées à la documentation et sont à remplacer par les valeurs validées.
   👉 Explication : les pools ne doivent pas chevaucher les adresses statiques ni les réservations.

3. Confirmer dans le VLAN de test isolé qu'aucun autre serveur DHCP ne répond.
   👉 Explication : un second serveur DHCP distribuerait des paramètres contradictoires.

## 2. Production — Contrôles

Obtenir l'autorisation et la fenêtre de changement; prévoir un accès console, la topologie (relais éventuel) et le plan de retour.

## 3. Production — Sécurité

- Ne pas démarrer Kea sur un réseau de production sans autorisation.
- Ne pas lancer de test DHCP sur un LAN partagé.

## Validation et retour arrière

- **Validation** : Interface, adresse statique, plage et VLAN isolé identifiés et documentés.
- **Retour arrière** : Aucune modification n'est faite à cette étape.

## Si le problème n'est pas résolu

- [ISC Kea — Installation](https://kea.readthedocs.io/en/latest/arm/install.html)
- [ISC Kea — Serveur DHCPv4](https://kea.readthedocs.io/en/latest/arm/dhcp4-srv.html)
- [Guide complet Kea DHCPv4 Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/64_Deploiement_Kea_DHCPv4_Debian_13.md#1-perimetre-et-prerequis)
