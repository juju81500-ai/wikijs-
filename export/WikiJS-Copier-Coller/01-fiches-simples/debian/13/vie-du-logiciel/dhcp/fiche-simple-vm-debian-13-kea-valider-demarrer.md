# Fiche_Simple_-_VM_Debian_13_Kea_Valider_Demarrer.md

- **Environnement** : VM Debian 13 serveur DHCPv4 sur un VLAN de test isolé
- **OS / Version** : Debian 13 Trixie x86-64; ISC Kea (canal stable)
- **Catégorie** : réseau / DHCP

---

## Problème précis à résoudre

Valider la syntaxe et la configuration avant d'activer le service.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier l'interface et le routage :
   ```bash
   ip -br address show dev ens18
   ip route
   ```
   👉 Explication : `ens18` est un exemple : utiliser l'interface réelle du VLAN.

2. Tester la configuration :
   ```bash
   sudo kea-dhcp4 -t /etc/kea/kea-dhcp4.conf
   ```
   👉 Explication : `-t` vérifie la syntaxe et la cohérence sans démarrer le service.

3. Mode approfondi, seulement si des dépendances (base SQL, hooks) sont déclarées :
   ```bash
   sudo kea-dhcp4 -T /etc/kea/kea-dhcp4.conf
   ```
   👉 Explication : `-T` teste aussi les connexions et bibliothèques; il ne teste pas l'échange de paquets sur le VLAN.

4. Activer et démarrer le service puis lire l'état et les journaux :
   ```bash
   sudo systemctl enable --now isc-kea-dhcp4-server.service
   sudo systemctl --no-pager status isc-kea-dhcp4-server.service
   sudo journalctl -u isc-kea-dhcp4-server.service -n 50 --no-pager
   ```
   👉 Explication : confirme que le service tourne sans erreur d'interface.

## 2. Production — Contrôles

Fenêtre de changement validée avant le démarrage; accès console disponible.

## 3. Production — Sécurité

- Ne démarrer le service que sur le VLAN autorisé.
- Vérifier qu'aucun autre serveur DHCP n'est actif.

## Validation et retour arrière

- **Validation** : `-t` réussit, service `active (running)` et journaux sans erreur.
- **Retour arrière** : `sudo systemctl disable --now isc-kea-dhcp4-server.service` puis restaurer la configuration `.orig`.

## Si le problème n'est pas résolu

- [ISC Kea — Serveur DHCPv4](https://kea.readthedocs.io/en/latest/arm/dhcp4-srv.html)
- [Guide complet Kea DHCPv4 Debian 13](/02-fiches-completes/debian/13/installation-deploiement/64-deploiement-kea-dhcpv4-debian-13#4-valider-la-configuration-puis-demarrer)