# Fiche simple — Debian 13 : installer et contrôler Kea DHCPv4

- **OS / Version** : VM Debian 13 Trixie
- **Catégorie** : Services réseau / DHCPv4

## Objectif

Installer Kea DHCPv4 pour un VLAN autorisé, vérifier la configuration et effectuer un test client sans perturber un réseau partagé.

## 1. Préparer le réseau

Avant installation, noter l'interface, l'IP statique du serveur, le préfixe, la passerelle, les DNS et le pool approuvé. Vérifier qu'aucun autre serveur DHCP n'est actif sur le VLAN. Utiliser un VLAN de lab isolé pour le premier essai.

```bash
ip -br address
ip route
```
   👉 Explication : relève interface, IP statique et routes du serveur.

Les adresses de documentation `192.0.2.0/24` ne sont pas un plan d'adressage à reprendre.

## 2. Installer le paquet stable

Ajouter le dépôt ISC Cloudsmith **stable** conformément à l'instruction officielle pour Debian 13, puis installer les composants nécessaires :

```bash
apt-cache policy isc-kea-dhcp4
sudo apt update
sudo apt install isc-kea-dhcp4
```
   👉 Explication : vérifie la version proposée par le dépôt, puis installe Kea DHCPv4.

Sur Debian, l'unité systemd à utiliser est `isc-kea-dhcp4-server.service`.

## 3. Vérifier la configuration et l'unité

Après avoir modifié `/etc/kea/kea-dhcp4.conf` avec les valeurs validées, vérifier la syntaxe avant de démarrer ou recharger :

```bash
sudo kea-dhcp4 -t /etc/kea/kea-dhcp4.conf
sudo systemctl enable --now isc-kea-dhcp4-server.service
sudo systemctl --no-pager status isc-kea-dhcp4-server.service
sudo journalctl -u isc-kea-dhcp4-server.service -n 40 --no-pager
```
   👉 Explication : teste la syntaxe de la configuration, démarre le service et lit son état et ses journaux.

Pour configuration avec base de données ou hooks, le contrôle approfondi `sudo kea-dhcp4 -T /etc/kea/kea-dhcp4.conf` vérifie aussi ces dépendances.

## 4. Faire un essai client contrôlé

Tester depuis une VM cliente située sur le VLAN isolé. Vérifier qu'elle reçoit une adresse dans le pool approuvé et les bonnes options routeur, DNS et domaine. Ne jamais lancer un client DHCP de test sur un LAN partagé.

DHCPv4 utilise UDP 67/68. Restreindre les chemins et relais au périmètre prévu; les sockets bruts utilisés pour les clients directement connectés peuvent contourner certains filtres locaux.

## Retour arrière

Avant modification, sauvegarder le fichier de configuration et le fichier de baux. En cas d'échec, restaurer la configuration précédente, exécuter `kea-dhcp4 -t`, puis redémarrer le service. Ne pas supprimer les baux actifs pour corriger une erreur.

## Source

- [ISC Kea — Installation](https://kea.readthedocs.io/en/latest/arm/install.html)
- Guide complet : `02-Fiches-Completes/Debian-13/Installation-Deploiement/64_Deploiement_Kea_DHCPv4_Debian_13.md`