---
title: "Déployer Kea DHCPv4 sur Debian 13"
description: "Fiche simple : [cadrer le périmètre Kea](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/DHCP/FicheSimple-VMDebian13KeaCadrer.md)."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "kea", "dhcpv4", "isc", "networking", "lab"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Déployer Kea DHCPv4 sur Debian 13

- **OS / Version** : Debian 13 Trixie x86-64; canal stable ISC choisi et figé pour le service
- **Type de fiche** : Installation/Déploiement
- **Rôle** : Serveur DHCPv4 pour un VLAN autorisé
- **Tags** : `debian13`, `kea`, `dhcpv4`, `isc`, `networking`, `lab`

## 1. Périmètre et prérequis

Fiche simple : [cadrer le périmètre Kea](/01-fiches-simples/debian/13/vie-du-logiciel/dhcp/fiche-simple-vm-debian-13-kea-cadrer).

Cette fiche installe Kea DHCPv4 avec le backend de baux `memfile`. Elle ne configure pas DHCPv6, haute disponibilité, base SQL ou DNS dynamique. Le serveur doit disposer d'une adresse statique, d'une interface dédiée au VLAN servi ou d'un relais DHCP déclaré, d'une plage IP approuvée et d'un accès console.

**Ne pas démarrer Kea sur un réseau de production sans autorisation et fenêtre de changement.** Un serveur DHCP non prévu peut distribuer de mauvais paramètres aux clients. Dans un lab, isoler le VLAN virtuel et vérifier qu'aucun autre serveur DHCP ne répond.

Les adresses `192.0.2.0/24` ci-dessous sont réservées à la documentation. Remplacer toutes les adresses et `ens18` par les valeurs validées du réseau réel. Ne pas chevaucher les adresses statiques, réservations et pools.

## 2. Installer le paquet ISC stable

Fiche simple : [installer le paquet ISC Kea](/01-fiches-simples/debian/13/vie-du-logiciel/dhcp/fiche-simple-vm-debian-13-kea-installer).

ISC recommande ses paquets Cloudsmith et le méta-paquet `isc-kea`. Choisir le dépôt **stable** correspondant à la version retenue, suivre son instruction Debian/13 « Set Me Up », puis vérifier l'origine et la version avant installation :

```bash
apt-cache policy isc-kea isc-kea-dhcp4
sudo apt update
sudo apt install isc-kea-dhcp4 isc-kea-admin
```

Installer aussi `isc-kea-dhcp-ddns` uniquement si les mises à jour DNS sont prévues et configurées. Éviter le dépôt de développement et ne pas changer de série majeure sans plan de mise à jour.

Sur Debian, l'unité systemd réelle est `isc-kea-dhcp4-server.service` :

```bash
systemctl cat isc-kea-dhcp4-server.service
sudo systemctl status isc-kea-dhcp4-server.service --no-pager
```

## 3. Définir une configuration minimale

Fiche simple : [écrire la configuration minimale Kea](/01-fiches-simples/debian/13/vie-du-logiciel/dhcp/fiche-simple-vm-debian-13-kea-configurer).

Sauvegarder `/etc/kea/kea-dhcp4.conf`, puis configurer le serveur dans ce fichier. Exemple de configuration DHCPv4 autonome :

```json
{
  "Dhcp4": {
    "interfaces-config": {
      "interfaces": [ "ens18" ]
    },
    "lease-database": {
      "type": "memfile",
      "persist": true,
      "name": "kea-leases4.csv"
    },
    "valid-lifetime": 3600,
    "renew-timer": 900,
    "rebind-timer": 1800,
    "authoritative": true,
    "subnet4": [
      {
        "id": 1,
        "subnet": "192.0.2.0/24",
        "pools": [
          { "pool": "192.0.2.100 - 192.0.2.199" }
        ],
        "option-data": [
          { "name": "routers", "data": "192.0.2.1" },
          { "name": "domain-name-servers", "data": "192.0.2.53" },
          { "name": "domain-name", "data": "lab.example.test" }
        ]
      }
    ]
  }
}
```

La configuration suppose que `ens18` a une adresse fixe dans le sous-réseau et que `192.0.2.1` et `192.0.2.53` sont des routeur et DNS réels du lab. Si les requêtes arrivent par relais, configurer `relay.ip-addresses` avec l'adresse du relais et revoir l'interface d'écoute selon la topologie. Ne pas configurer un pool sur une interface qui ne dessert pas ce réseau.

Le backend `memfile` conserve les baux dans le répertoire de données Kea du paquet. Le nom sans chemin utilise le répertoire de données prévu par l'installation. Garder `persist: true`; une perte de persistance peut conduire à réattribuer des adresses encore utilisées.

## 4. Valider la configuration puis démarrer

Fiche simple : [valider puis démarrer Kea](/01-fiches-simples/debian/13/vie-du-logiciel/dhcp/fiche-simple-vm-debian-13-kea-valider-demarrer).

Vérifier l'interface, le routage, la syntaxe JSON et la configuration Kea avant d'activer le service :

```bash
ip -br address show dev ens18
ip route
sudo kea-dhcp4 -t /etc/kea/kea-dhcp4.conf
```

Le mode approfondi `-T` vérifie également des dépendances comme les connexions de bases de données et les bibliothèques hook :

```bash
sudo kea-dhcp4 -T /etc/kea/kea-dhcp4.conf
```

N'exécuter `-T` qu'avec les dépendances effectivement déclarées. Une réussite ne teste pas l'échange de paquets sur le VLAN.

Après validation, activer le service :

```bash
sudo systemctl enable --now isc-kea-dhcp4-server.service
sudo systemctl --no-pager status isc-kea-dhcp4-server.service
sudo journalctl -u isc-kea-dhcp4-server.service -n 50 --no-pager
```

## 5. Contrôler le service sans perturber le LAN

Fiche simple : [contrôler le service sans perturber le LAN](/01-fiches-simples/debian/13/vie-du-logiciel/dhcp/fiche-simple-vm-debian-13-kea-controler-service).

Confirmer que le daemon a ouvert les sockets attendues et ne signale pas d'erreur d'interface :

```bash
sudo ss -lunp '( sport = :67 )'
sudo journalctl -u isc-kea-dhcp4-server.service -b --no-pager
```

Tester l'attribution seulement depuis une VM cliente attachée au VLAN isolé, en confirmant l'adresse, la passerelle, les DNS, le nom de domaine et le renouvellement du bail. Contrôler le bail côté serveur dans le fichier persistant Kea et la connectivité vers les services annoncés. Ne pas lancer un client DHCP de test sur un LAN partagé.

Pour une infrastructure réelle, autoriser le trafic DHCP selon les règles réseau et relais validés. DHCPv4 utilise UDP/67 côté serveur et UDP/68 côté client. Kea peut employer des sockets bruts pour les clients directement connectés; ceux-ci peuvent contourner le filtrage local classique. Lire les journaux et tester depuis le réseau client réel avant de déclarer le service disponible.

## 6. Changer une plage ou revenir en arrière

Fiche simple : [changer une plage ou revenir en arrière](/01-fiches-simples/debian/13/vie-du-logiciel/dhcp/fiche-simple-vm-debian-13-kea-modifier-plage).

Avant toute modification, sauvegarder le fichier de configuration et l'état des baux; documenter les valeurs actuelles du VLAN. Éditer une copie de travail, vérifier les pools, les options et l'absence de chevauchement, puis exécuter `kea-dhcp4 -t`.

Un redémarrage contrôlé applique le fichier du paquet :

```bash
sudo systemctl restart isc-kea-dhcp4-server.service
sudo systemctl --no-pager status isc-kea-dhcp4-server.service
sudo journalctl -u isc-kea-dhcp4-server.service -n 50 --no-pager
```

En cas d'erreur, restaurer le fichier précédent, revalider avec `kea-dhcp4 -t`, puis redémarrer. Ne pas supprimer le fichier des baux pour « réparer » une panne. Toute restauration de baux doit être testée hors production et éviter une divergence avec des baux encore actifs.

## 7. Durcissement et exploitation

Fiche simple : [durcir et exploiter Kea](/01-fiches-simples/debian/13/vie-du-logiciel/dhcp/fiche-simple-vm-debian-13-kea-durcir).

- Limiter les interfaces d'écoute et les réseaux autorisés au strict besoin.
- Ne pas exposer l'API de contrôle HTTP à un réseau non maîtrisé. Si elle est activée, utiliser HTTPS, authentification appropriée et filtrage réseau; le socket de contrôle UNIX est désactivé par défaut.
- Restreindre les droits des fichiers de configuration et sauvegardes. Les secrets SQL sont généralement stockés en clair dans la configuration; protéger les fichiers et préférer un backend adapté seulement après étude.
- N'activer ni hook ni composant inutile. Utiliser une base SQL et la haute disponibilité uniquement avec leurs procédures ISC propres, schémas validés et tests de bascule.
- Maintenir le système et le canal stable Kea à jour, et tester toute mise à niveau sur un serveur pilote.

## 8. Limites de validation

Fiche simple : [connaître les limites de validation](/01-fiches-simples/debian/13/vie-du-logiciel/dhcp/fiche-simple-vm-debian-13-kea-limites).

Les noms de paquets, unités systemd et options proviennent du manuel Kea courant. La procédure n'a pas été exécutée sur Debian 13 dans ce workspace; l'installation Cloudsmith, l'attribution DHCP et la restauration des baux restent à éprouver dans le VLAN de test cible.

## Sources

- [ISC Kea Administrator Reference Manual — Installation](https://kea.readthedocs.io/en/latest/arm/install.html)
- [ISC Kea Administrator Reference Manual — DHCPv4 Server](https://kea.readthedocs.io/en/latest/arm/dhcp4-srv.html)
- [ISC Kea Administrator Reference Manual — Security](https://kea.readthedocs.io/en/latest/arm/security.html)
- [ISC — Dépôts officiels Kea Cloudsmith](https://cloudsmith.io/~isc/repos)