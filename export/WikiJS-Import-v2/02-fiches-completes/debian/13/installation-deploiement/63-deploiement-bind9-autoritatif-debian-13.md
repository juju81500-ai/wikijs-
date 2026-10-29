---
title: "Déployer BIND 9 comme serveur DNS autoritatif sur Debian 13"
description: "Fiche simple : [cadrer le périmètre autoritatif](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/BIND9/FicheSimple-VMDebian13BIND9AutoritatifCadrer.md)."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "bind9", "dns", "authoritative", "hardening", "lab"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Déployer BIND 9 comme serveur DNS autoritatif sur Debian 13

- **OS / Version** : Debian 13 Trixie, paquets de la distribution
- **Type de fiche** : Installation/Déploiement
- **Rôle** : DNS autoritatif primaire pour une zone privée de laboratoire
- **Tags** : `debian13`, `bind9`, `dns`, `authoritative`, `hardening`, `lab`

## 1. Périmètre et prérequis

Fiche simple : [cadrer le périmètre autoritatif](/01-fiches-simples/debian/13/vie-du-logiciel/bind9/fiche-simple-vm-debian-13-bind9-autoritatif-cadrer).

Cette procédure configure BIND comme serveur **autoritatif uniquement**. Elle ne configure ni résolveur récursif pour les postes ni mises à jour DNS dynamiques. Déployer un résolveur interne séparé si les clients doivent résoudre des noms Internet.

Les valeurs `lab.example.test`, `192.0.2.0/24` et `192.0.2.53` sont réservées aux exemples et ne doivent pas être reprises comme plan d'adressage réel. Remplacer les variables par une zone et une adresse statique maîtrisées. Vérifier également qu'aucun autre service n'écoute sur l'adresse prévue au port TCP/UDP 53.

Prévoir une console hors bande ou une session d'administration indépendante du DNS. Sauvegarder `/etc/bind` et les fichiers de zone avant toute modification.

## 2. Installer le paquet Debian

Fiche simple : [installer BIND 9](/01-fiches-simples/debian/13/vie-du-logiciel/bind9/fiche-simple-vm-debian-13-bind9-autoritatif-installer).

```bash
sudo apt update
sudo apt install bind9 bind9-utils dnsutils
sudo systemctl enable --now bind9
sudo systemctl --no-pager status bind9
```

Le paquet Debian fournit l'unité `bind9`, l'utilisateur de service dédié et les protections du paquet, dont AppArmor sur l'installation standard. Ne pas ajouter de chroot manuel ni modifier récursivement les propriétaires de `/etc/bind`.

Confirmer la version et l'adresse statique du serveur :

```bash
named -V
ip -br address
sudo ss -lntup '( sport = :53 )'
```

## 3. Définir une politique autoritative

Fiche simple : [définir la politique et les zones](/01-fiches-simples/debian/13/vie-du-logiciel/bind9/fiche-simple-vm-debian-13-bind9-autoritatif-politique-zones).

Ajouter la liste de clients autorisés en tête de `/etc/bind/named.conf.options`, puis ajuster le bloc `options` existant sans créer un second bloc concurrent :

```conf
acl clients_dns {
    127.0.0.1;
    192.0.2.0/24;
};

options {
    directory "/var/cache/bind";
    listen-on { 192.0.2.53; };
    listen-on-v6 { none; };
    recursion no;
    allow-query { clients_dns; };
    allow-query-cache { none; };
    allow-transfer { none; };
    version "non divulguée";
    dnssec-validation auto;
};
```

L'adresse d'écoute doit correspondre à une adresse locale statique. Si IPv6 est utilisé, remplacer `listen-on-v6 { none; };` par les adresses IPv6 voulues et inclure les préfixes autorisés dans l'ACL. Ne pas remplacer l'ACL par `any` sur un réseau privé.

Déclarer la zone dans `/etc/bind/named.conf.local` :

```conf
zone "lab.example.test" {
    type primary;
    file "/etc/bind/db.lab.example.test";
    allow-query { clients_dns; };
    allow-transfer { none; };
    notify no;
};

zone "2.0.192.in-addr.arpa" {
    type primary;
    file "/etc/bind/db.192.0.2";
    allow-query { clients_dns; };
    allow-transfer { none; };
    notify no;
};
```

Créer `/etc/bind/db.lab.example.test` :

```dns
$TTL 3600
@ IN SOA ns1.lab.example.test. hostmaster.lab.example.test. (
    2026102701 ; serial: incrémenter à chaque modification
    3600       ; refresh
    900        ; retry
    1209600    ; expire
    300        ; negative cache TTL
)
@    IN NS ns1.lab.example.test.
ns1  IN A  192.0.2.53
srv1 IN A  192.0.2.20
```

Créer `/etc/bind/db.192.0.2` :

```dns
$TTL 3600
@ IN SOA ns1.lab.example.test. hostmaster.lab.example.test. (
    2026102701
    3600
    900
    1209600
    300
)
@  IN NS  ns1.lab.example.test.
20 IN PTR srv1.lab.example.test.
53 IN PTR ns1.lab.example.test.
```

Vérifier que les fichiers restent lisibles par le service et que les chemins respectent le profil AppArmor du paquet. Ne pas rendre les fichiers de configuration inscriptibles par l'utilisateur `bind`.

## 4. Valider avant activation

Fiche simple : [valider avant activation](/01-fiches-simples/debian/13/vie-du-logiciel/bind9/fiche-simple-vm-debian-13-bind9-autoritatif-valider).

La validation doit réussir avant chaque rechargement :

```bash
sudo named-checkconf -z /etc/bind/named.conf
sudo named-checkzone lab.example.test /etc/bind/db.lab.example.test
sudo named-checkzone 2.0.192.in-addr.arpa /etc/bind/db.192.0.2
```

Si l'une de ces commandes retourne une erreur, corriger la configuration et ne pas recharger. Les deux fichiers de zone doivent utiliser un numéro SOA cohérent, et le numéro doit augmenter après toute modification.

Une fois les contrôles réussis :

```bash
sudo systemctl reload bind9
sudo rndc status
sudo journalctl -u bind9 -n 50 --no-pager
```

Le rechargement n'est pas une validation en soi. Vérifier les réponses avec `dig` depuis le serveur et depuis un client autorisé :

```bash
dig @192.0.2.53 lab.example.test SOA +norecurse
dig @192.0.2.53 srv1.lab.example.test A +norecurse
dig @192.0.2.53 -x 192.0.2.20 +norecurse
dig @192.0.2.53 debian.org A +recurse
```

Les trois premières réponses doivent être autoritatives (`aa`). La dernière ne doit pas fournir de résolution récursive. Tester aussi depuis une adresse non autorisée : la politique ACL doit empêcher l'accès voulu.

## 5. Pare-feu et exploitation

Fiche simple : [ouvrir le pare-feu et exploiter](/01-fiches-simples/debian/13/vie-du-logiciel/bind9/fiche-simple-vm-debian-13-bind9-autoritatif-pare-feu-exploitation).

Autoriser UDP **et** TCP 53 uniquement depuis les réseaux clients approuvés. TCP est requis notamment pour les réponses DNS volumineuses et les transferts de zone. Garder les transferts désactivés tant qu'aucun secondaire n'est configuré.

Pour ajouter un secondaire, utiliser une ACL limitée à son adresse, protéger les transferts et notifications par TSIG, et valider la configuration des deux côtés avant ouverture réseau. Ne pas utiliser une ACL basée uniquement sur une IP source pour autoriser des mises à jour dynamiques.

Surveiller `systemctl status bind9`, les journaux du service, les refus d'accès, l'espace disque et l'expiration des certificats si DNS-over-TLS est ajouté séparément. Documenter les changements de zone et incrémenter le numéro SOA.

## 6. Sauvegarde et retour arrière

Fiche simple : [sauvegarder et revenir en arrière](/01-fiches-simples/debian/13/vie-du-logiciel/bind9/fiche-simple-vm-debian-13-bind9-autoritatif-sauvegarde-retour).

Avant changement, archiver `/etc/bind` et conserver une copie des zones dans un dépôt de configuration protégé. En cas d'échec après modification, restaurer les fichiers précédents, exécuter de nouveau `named-checkconf -z` et `named-checkzone`, puis recharger le service. Ne pas réinstaller ou purger le paquet pour corriger une erreur de zone.

La sauvegarde n'est considérée vérifiée qu'après restauration dans un environnement isolé et comparaison des réponses DNS attendues.

## 7. Limites de validation

Fiche simple : [connaître les limites de validation](/01-fiches-simples/debian/13/vie-du-logiciel/bind9/fiche-simple-vm-debian-13-bind9-autoritatif-limites).

Les commandes de cette fiche proviennent des documentations BIND et Debian. Elles n'ont pas été exécutées sur un serveur Debian 13 dans ce workspace. La validation structurelle de la page ne prouve ni l'écoute réseau ni le fonctionnement des zones.

## Sources

- [ISC BIND 9 Administrator Reference Manual — Configurations and Zone Files](https://bind9.readthedocs.io/en/latest/chapter3.html)
- [ISC BIND 9 Administrator Reference Manual — Security Configurations](https://bind9.readthedocs.io/en/latest/chapter7.html)
- [ISC BIND 9 — Manpages](https://bind9.readthedocs.io/en/latest/manpages.html)
- [Debian — Paquet bind9 pour Trixie](https://packages.debian.org/trixie/bind9)