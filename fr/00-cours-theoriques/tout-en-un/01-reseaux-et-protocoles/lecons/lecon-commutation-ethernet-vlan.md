---
title: "Leçon — Commutation Ethernet, adresses MAC, VLAN, trunk 802.1Q et STP"
description: "À l'issue de cette leçon, vous saurez :"
published: true
date: 2026-11-03T09:36:13Z
tags: ["transverse", "tout-en-un", "lecon", "reseaux", "ethernet", "mac", "vlan", "802-1q", "stp", "commutateur"]
editor: markdown
dateCreated: 2026-11-03T09:36:13Z
dateModified: 2026-11-03T09:36:13Z
---

# Leçon — Commutation Ethernet, adresses MAC, VLAN, trunk 802.1Q et STP

- **Tags** : `transverse`, `tout-en-un`, `lecon`, `reseaux`, `ethernet`, `mac`, `vlan`, `802.1q`, `stp`, `commutateur`
- **Niveau** : débutant à intermédiaire (couche 2 du modèle OSI)
- **Durée estimée** : 3 h 30 (1 h 30 de cours, 1 h 30 de laboratoire, 30 min d'exercices et de quiz)

> Cette leçon est un texte original du pack. Les adresses IP utilisées sont des adresses de documentation (RFC 5737) et les adresses MAC appartiennent à la plage de documentation de la RFC 7042. Tout ce qui modifie une configuration est présenté comme un exemple de laboratoire : ne jamais l'appliquer sur un réseau de production sans validation préalable, fenêtre de maintenance et plan de retour arrière.

## Objectifs pédagogiques

À l'issue de cette leçon, vous saurez :

- expliquer le rôle d'un commutateur Ethernet et le distinguer d'un concentrateur ;
- décrire une adresse MAC (unicast, multicast, diffusion) ;
- dérouler l'apprentissage, l'inondation et le filtrage d'une trame ;
- définir un VLAN, distinguer port d'accès et trunk, lire une étiquette 802.1Q et comprendre le VLAN natif ;
- décrire le principe de STP (pont racine, ports racine, désigné, bloqué) ;
- reproduire un mini-réseau VLAN + trunk dans un laboratoire Linux jetable et lire les commandes équivalentes d'un équipement de type Cisco IOS.

## Prérequis et durée

- Notions d'adresse IP et de sous-réseau ; la commutation travaille en **couche 2** (liaison de données), le routage en couche 3.
- Savoir utiliser un terminal Linux.
- Laboratoire : une VM Linux jetable (`iproute2`, `tcpdump`) où l'on peut exécuter des commandes d'administration **sans risque pour autre chose**.
- Durée : environ 3 h 30.

## L'essentiel en bref

- Un **commutateur** apprend « quelle adresse MAC est sur quel port » et n'envoie chaque trame que vers le bon port.
- Une **adresse MAC** (48 bits) n'a de sens que sur le réseau local.
- Diffusion ou destination inconnue : **inondation** sur tous les autres ports du VLAN.
- Un **VLAN** est un domaine de diffusion logique, en pratique un sous-réseau IP.
- Un **trunk 802.1Q** transporte plusieurs VLAN grâce à une étiquette de 4 octets (VID de 1 à 4094).
- **STP** bloque logiquement les liens redondants pour éviter les boucles.

## 1. Le commutateur Ethernet : de quoi parle-t-on ?

### 1.1 Une analogie

Un concentrateur (hub) crie chaque message dans un couloir : tout le monde l'entend. Un commutateur (switch) est un standardiste qui connaît le bureau de chacun et ne transmet le message qu'à la bonne porte, plusieurs conversations pouvant avoir lieu en même temps.

### 1.2 Concentrateur, pont, commutateur

| Équipement | Comportement | Domaine de collision | Domaine de diffusion |
|---|---|---|---|
| Concentrateur (hub) | répète tout sur tous les ports | un seul pour tous les ports | un seul |
| Pont / commutateur (switch) | envoie vers le seul port concerné quand il connaît la destination | un par port | un seul (sans VLAN) |
| Routeur | transmet entre réseaux IP distincts | un par interface | un par interface |

Deux notions à bien séparer :

- le **domaine de collision** est l'ensemble des équipements qui risquent d'émettre en même temps sur le même support. Avec des liens commutés en mode full duplex, il n'y a pratiquement plus de collisions ;
- le **domaine de diffusion** est l'ensemble des équipements qui reçoivent une trame de diffusion émise par l'un d'eux. Un commutateur ne le réduit pas par défaut ; c'est précisément le rôle des VLAN et des routeurs.

![Photographie de modules de commutation Ethernet à 48 ports RJ45 vus de face, empilés dans un châssis](images/commutation-ethernet-vlan-5.jpg)

*Des rangées de ports RJ45 d'un commutateur modulaire : chaque port est une « porte » vers une machine, et c'est sur cette porte que le commutateur apprend les adresses MAC. Photographie de Ben Franske, licence CC BY-SA 4.0 (voir les crédits en fin de leçon).*

Le commutateur ne lit que l'en-tête Ethernet (MAC destination, MAC source, éventuelle étiquette de VLAN), jamais l'adresse IP ni le port TCP : c'est ce qui le rend rapide et simple.

## 2. Les adresses MAC

### 2.1 Structure

Une adresse MAC compte 48 bits, notés en 6 octets hexadécimaux : `00:00:5e:00:53:01`. Les trois premiers octets forment l'**OUI** (Organizationally Unique Identifier), attribué par l'IEEE à un fabricant ; les trois derniers sont choisis par le fabricant pour numéroter la carte. Dans la leçon, nous utilisons la plage `00:00:5e:00:53:xx`, réservée à la documentation par la RFC 7042, pour ne jamais confondre un exemple avec une vraie machine.

Dans le premier octet, le bit I/G (poids faible) vaut 0 pour une adresse individuelle et 1 pour une adresse de groupe (multicast, diffusion) ; le bit suivant, U/L, vaut 1 pour une adresse administrée localement (machines virtuelles, conteneurs). Exemple : `02:00:00:00:00:01` (`02` = `0000 0010`) est locale et individuelle.

### 2.2 Les trois types de destination

- **Unicast** : une seule destination.
- **Diffusion** : `ff:ff:ff:ff:ff:ff`, tout le domaine de diffusion (par exemple une requête ARP).
- **Multicast** : un groupe (`01:00:5e:…` en IPv4, `33:33:…` en IPv6).

### 2.3 Voir ses adresses MAC (lecture seule)

Sur Linux :

```bash
ip -br link show
```

👉 Explication : affiche en une ligne par interface le nom, l'état (UP/DOWN) et l'adresse MAC. La commande ne modifie rien.

### 2.4 MAC et IP

L'expéditeur découvre la MAC d'une machine du même réseau avec **ARP** (IPv4) et la garde en cache ; la MAC n'est valable que sur le dernier tronçon et est réécrite à chaque saut de routeur.

```bash
ip neighbour show
```

👉 Explication : affiche le cache des voisins (IP, interface, MAC, état), en lecture seule.

## 3. Comment un commutateur décide : apprendre, inonder, filtrer

Le commutateur maintient une **table d'adresses MAC** (aussi appelée table CAM ou table de transfert, *forwarding table*). Elle associe une adresse MAC à un port (et à un VLAN). Cette table n'est pas configurée à la main : elle se construit toute seule.

![Schéma d'un commutateur à quatre ports reliant les postes A, B, C et D, avec sa table MAC et la règle de décision](images/commutation-ethernet-vlan-1.svg)

*Un commutateur à quatre ports : la table MAC se remplit au fur et à mesure que les postes émettent. Création originale du projet Pack Master, dédiée au domaine public (CC0).*

### 3.1 La logique de décision

Pour chaque trame reçue : (1) **apprendre** la MAC source sur le port d'arrivée ; (2) chercher la destination ; (3) **transférer** vers le seul port concerné si elle est connue ; (4) **filtrer** (ignorer) si elle est sur le port d'arrivée ; (5) **inonder** les autres ports du VLAN si elle est inconnue ou de diffusion.

### 3.2 Exemple pas à pas

Table vide ; A, B, C, D sont sur les ports 1 à 4.

1. A diffuse une requête ARP pour joindre C. Le commutateur apprend « A = port 1 » et inonde les ports 2, 3 et 4 ; B et D l'ignorent.
2. C répond en unicast à A. Le commutateur apprend « C = port 3 » ; A est connue : la réponse part sur le port 1 seulement.
3. Les trames suivantes de A vers C ne vont que sur le port 3 : B et D ne voient plus rien passer.

### 3.3 Vieillissement et tempêtes

Une entrée non rafraîchie disparaît après un délai (souvent 300 s). En cas de boucle, une trame de diffusion tourne indéfiniment (**tempête de diffusion**) : les trames Ethernet n'ont pas de TTL, d'où STP (section 6).

Table MAC d'un pont Linux (après le laboratoire, lecture seule) :

```bash
bridge fdb show br br-lab
```

👉 Explication : montre les adresses MAC apprises par `br-lab` et leur port ; `permanent` désigne les entrées propres aux interfaces.

## 4. Les VLAN : plusieurs réseaux sur un seul commutateur

### 4.1 Le problème

Sans VLAN, tous les ports d'un commutateur sont dans le même domaine de diffusion. Le **VLAN** (IEEE 802.1Q) découpe logiquement un commutateur en plusieurs « commutateurs virtuels » étanches. Analogie : un immeuble dont chaque étage est fermé par un badge ; on ne passe d'un étage à l'autre que par la réception (le routeur).

### 4.2 Bénéfices

Isolation des diffusions, meilleures performances, organisation par fonction plutôt que par emplacement, et réduction de la surface d'attaque (à condition de filtrer ensuite entre VLAN).

### 4.3 Règles d'or

- Un VLAN correspond, en général, à **un sous-réseau IP** : VLAN 10 ↔ `192.0.2.0/24`, VLAN 20 ↔ `198.51.100.0/24`.
- Deux machines de VLAN différents ne peuvent communiquer qu'à travers un équipement de **couche 3** (routeur ou commutateur de niveau 3), qui devient la passerelle de chaque VLAN.
- Les numéros valides vont de 1 à 4094 (le 0 et le 4095 sont réservés). Le VLAN 1 est celui par défaut sur de nombreux équipements : on évite de l'utiliser pour du trafic utile.
- Entre VLAN, il faut un routeur « sur un bâton » (un trunk, une sous-interface par VLAN) ou un commutateur de niveau 3 : voir la [leçon sur le routage](/fr/00-cours-theoriques/tout-en-un/01-reseaux-et-protocoles/lecons/lecon-routage-ip).
- Un **VLAN n'est pas un mécanisme de chiffrement**.

### 4.4 Ports d'accès

Un **port d'accès** (*access port*) appartient à un seul VLAN. La trame arrive et repart **sans étiquette** ; le poste ignore tout des VLAN. C'est la configuration normale pour un ordinateur, une imprimante ou un serveur. Le commutateur ajoute lui-même l'appartenance au VLAN en interne.

## 5. Le trunk 802.1Q : transporter plusieurs VLAN sur un seul lien

### 5.1 Pourquoi un trunk ?

Quand deux commutateurs portent les mêmes VLAN, il faudrait un câble par VLAN. Le **trunk** est un lien unique qui transporte plusieurs VLAN en **étiquetant** chaque trame de son numéro de VLAN ; il sert aussi vers un routeur ou un hyperviseur.

![Deux commutateurs SW1 et SW2 reliés par un trunk 802.1Q portant les VLAN 10 et 20, avec quatre postes](images/commutation-ethernet-vlan-3.svg)

*Deux commutateurs, deux VLAN, un seul lien trunk. PC1 et PC3 (VLAN 10) se joignent à travers le trunk, mais ne voient pas PC2 et PC4 (VLAN 20). Création originale du projet Pack Master, dédiée au domaine public (CC0).*

### 5.2 L'étiquette 802.1Q

L'étiquette, insérée entre l'adresse MAC source et l'EtherType, ajoute 4 octets : **TPID** (16 bits, `0x8100`, « une étiquette suit »), **PCP** (3 bits, priorité 0 à 7), **DEI** (1 bit, trame abandonnable en cas de congestion) et **VID** (12 bits, numéro de VLAN).

![Structure d'une trame Ethernet II avec l'étiquette 802.1Q détaillée : TPID, PCP, DEI et VID](images/commutation-ethernet-vlan-2.svg)

*La trame Ethernet avec étiquette 802.1Q : les 4 octets ajoutés portent le numéro de VLAN. Création originale du projet Pack Master, dédiée au domaine public (CC0).*

La trame étiquetée fait 4 octets de plus (1522 au lieu de 1518) ; le MTU reste de 1500 octets.

### 5.3 Le VLAN natif

Sur un trunk, le VLAN **natif** circule **sans étiquette**, pour la compatibilité avec des équipements qui ignorent 802.1Q. Les deux extrémités doivent s'accorder sur lui, sinon des trames arrivent dans le mauvais VLAN. En lab, on utilise un VLAN natif dédié et inutilisé (par exemple 999) plutôt que le VLAN 1.

### 5.4 Limiter les VLAN autorisés

Par défaut, un trunk transporte tous les VLAN : on le restreint à la liste nécessaire (`10,20`).

### 5.5 Exemple de configuration (équipement de type Cisco IOS, laboratoire uniquement)

Exemple pour un commutateur d'enseignement ou un simulateur. Les noms d'interface et certaines commandes (`switchport trunk encapsulation dot1q` n'existe pas sur tous les modèles) varient : consultez la documentation de votre équipement et ne l'appliquez jamais en production sans validation.

```text
Switch> enable
Switch# configure terminal
Switch(config)# vlan 10
Switch(config-vlan)# name COMPTA
Switch(config-vlan)# vlan 20
Switch(config-vlan)# name INVITES
Switch(config-vlan)# exit
Switch(config)# interface range GigabitEthernet0/1 - 2
Switch(config-if-range)# switchport mode access
Switch(config-if-range)# switchport access vlan 10
Switch(config-if-range)# exit
Switch(config)# interface GigabitEthernet0/24
Switch(config-if)# switchport mode trunk
Switch(config-if)# switchport trunk native vlan 999
Switch(config-if)# switchport trunk allowed vlan 10,20
Switch(config-if)# end
```

👉 Explication : crée les VLAN 10 et 20 avec un nom, place les ports 1 et 2 en accès dans le VLAN 10, puis transforme le port 24 en trunk limité aux VLAN 10 et 20 avec le VLAN natif 999. Ces commandes modifient la configuration d'exécution : seulement pour un lab ou après validation écrite en production.

Pour vérifier (lecture seule) :

```text
Switch# show vlan brief
Switch# show interfaces trunk
Switch# show mac address-table
```

👉 Explication : affiche respectivement les VLAN et leurs ports d'accès, l'état des trunks (VLAN autorisés, VLAN natif) et la table MAC. Ce sont des commandes de consultation.

## 6. STP : éviter les boucles de commutation

### 6.1 Le problème

On relie souvent les commutateurs en triangle ou en maille pour la résilience. Mais une trame de diffusion n'a pas de durée de vie : elle tourne dans la boucle, se multiplie et sature le réseau. Le **Spanning Tree Protocol** (IEEE 802.1D) construit un **arbre sans boucle** à partir d'un graphe avec boucles.

### 6.2 Le principe en quatre étapes

![Trois commutateurs en triangle : SW1 est le pont racine, un port entre SW2 et SW3 est bloqué](images/commutation-ethernet-vlan-4.svg)

*STP transforme un triangle de liens en arbre : un des trois liens reste en réserve, port bloqué. Création originale du projet Pack Master, dédiée au domaine public (CC0).*

1. **Élection du pont racine** : chaque commutateur annonce son identifiant (priorité, 32768 par défaut + adresse MAC) ; le plus petit gagne. On baisse volontairement la priorité d'un commutateur central.
2. **Port racine** de chaque commutateur non racine : celui qui offre le chemin au coût le plus faible vers la racine (le coût décroît avec la vitesse).
3. **Port désigné** sur chaque segment : celui qui a le meilleur chemin vers la racine.
4. **Blocage** des ports restants : ils ne transmettent aucune donnée mais écoutent les **BPDU** (messages STP, toutes les 2 s) pour prendre le relais.

### 6.3 STP, RSTP et variantes

Le STP classique (802.1D) converge en 30 à 50 s ; le **RSTP** (802.1w) en quelques secondes et est le choix usuel ; **MSTP** (802.1s) regroupe des VLAN en instances ; PVST+ / Rapid-PVST+ sont des variantes constructeur par VLAN.

### 6.4 Protéger les ports d'accès

**PortFast** met un port de bordure immédiatement en transmission ; **BPDU Guard** le désactive si un BPDU arrive (un autre commutateur a été branché).

Exemple de laboratoire de type Cisco IOS :

```text
Switch(config)# spanning-tree mode rapid-pvst
Switch(config)# spanning-tree vlan 10,20 priority 4096
Switch(config)# interface GigabitEthernet0/1
Switch(config-if)# spanning-tree portfast
Switch(config-if)# spanning-tree bpduguard enable
Switch(config-if)# end
```

👉 Explication : active Rapid-PVST, fait du commutateur le pont racine préféré (priorité 4096) pour les VLAN 10 et 20, puis protège un port d'accès. À faire seulement en laboratoire : un changement de racine en production peut provoquer une réélection et une coupure brève.

Pour vérifier :

```text
Switch# show spanning-tree vlan 10
```

👉 Explication : affiche le pont racine, le rôle (racine, désigné, alternatif) et l'état de chaque port pour le VLAN 10, sans rien modifier.

## Mise en pratique guidée

Objectif : reproduire, dans une **VM Linux jetable**, un commutateur à trois ports d'accès (deux en VLAN 10, un en VLAN 20) et un port trunk, avec des espaces de noms réseau (*network namespaces*) jouant les postes. Tout reste dans la machine.

> **Avertissement** : ces commandes créent et suppriment des interfaces virtuelles, avec des droits d'administration. À exécuter uniquement dans la VM de laboratoire, jamais sur un poste ou un serveur utile. Le nettoyage est fourni à l'étape 6.

### Étape 1 — Créer le commutateur virtuel

```bash
sudo ip link add br-lab type bridge vlan_filtering 1
sudo ip link set br-lab up
```

👉 Explication : crée le pont `br-lab` avec le filtrage VLAN actif (il se comporte alors comme un commutateur 802.1Q), puis l'active.

### Étape 2 — Créer trois postes et les brancher

```bash
for i in 1 2 3; do
  sudo ip netns add ns$i
  sudo ip link add sw-p$i type veth peer name eth0 netns ns$i
  sudo ip link set sw-p$i master br-lab up
  sudo ip -n ns$i link set lo up
  sudo ip -n ns$i link set eth0 up
  sudo ip -n ns$i addr add 192.0.2.1$i/24 dev eth0
done
```

👉 Explication : pour chaque poste (`ns1` à `ns3`), crée un espace de noms, un câble virtuel (`sw-pX` côté pont, `eth0` côté poste) et l'adresse `192.0.2.11` à `192.0.2.13`. Les trois postes sont dans le même sous-réseau : ce seront les VLAN, pas l'adressage, qui les sépareront.

### Étape 3 — Affecter les VLAN aux ports d'accès

```bash
for p in sw-p1 sw-p2; do
  sudo bridge vlan del dev $p vid 1
  sudo bridge vlan add dev $p vid 10 pvid untagged
done
sudo bridge vlan del dev sw-p3 vid 1
sudo bridge vlan add dev sw-p3 vid 20 pvid untagged
```

👉 Explication : retire le VLAN 1 par défaut, place `sw-p1` et `sw-p2` en VLAN 10 et `sw-p3` en VLAN 20. `pvid untagged` signifie « entrée sans étiquette = ce VLAN, sortie sans étiquette » : c'est un port d'accès.

### Étape 4 — Tester l'isolation et observer

```bash
sudo ip netns exec ns1 ping -c 2 192.0.2.12
sudo ip netns exec ns1 ping -c 2 -W 1 192.0.2.13
bridge vlan show
bridge fdb show br br-lab | grep -v permanent
```

👉 Explication : le premier ping (même VLAN) doit réussir ; le second (VLAN 20, même sous-réseau) doit échouer car l'ARP ne traverse pas les VLAN. Les deux dernières commandes, en lecture seule, affichent les VLAN par port et les adresses MAC apprises. Ces commandes n'ont pas été exécutées par l'auteur : en cas d'écart, voir le dépannage.

### Étape 5 — Ajouter un port trunk

```bash
sudo ip netns add ns4
sudo ip link add sw-p4 type veth peer name eth0 netns ns4
sudo ip link set sw-p4 master br-lab up
sudo ip -n ns4 link set lo up
sudo ip -n ns4 link set eth0 up
sudo bridge vlan del dev sw-p4 vid 1
sudo bridge vlan add dev sw-p4 vid 10
sudo bridge vlan add dev sw-p4 vid 20
sudo ip -n ns4 link add link eth0 name eth0.10 type vlan id 10
sudo ip -n ns4 addr add 192.0.2.14/24 dev eth0.10
sudo ip -n ns4 link set eth0.10 up
```

👉 Explication : `ns4` joue un serveur relié par trunk. Le port `sw-p4` accepte les VLAN 10 et 20 **étiquetés** (pas de `pvid untagged`) et la sous-interface `eth0.10` émet des trames étiquetées VLAN 10.

```bash
sudo tcpdump -e -nn -c 4 -i sw-p4 icmp or arp
sudo ip netns exec ns4 ping -c 2 192.0.2.11
```

👉 Explication : lancez d'abord `tcpdump` dans un second terminal, puis le ping. L'option `-e` affiche l'en-tête de liaison : vous devez lire `vlan 10` sur le lien trunk, alors que `ns1` (accès) répond sans étiquette. La capture demande des droits d'administration : à limiter à la VM.

### Étape 6 — Nettoyage

```bash
for i in 1 2 3 4; do sudo ip netns del ns$i; done
sudo ip link del br-lab
ip -br link show | grep -E 'sw-p|br-lab' || echo "nettoyage terminé"
```

👉 Explication : supprime les espaces de noms (et donc leurs câbles virtuels) et le pont, puis vérifie qu'il ne reste aucune interface du laboratoire. Un simulateur de réseau permet de refaire le même exercice avec la syntaxe de la section 5.5.

## Exercices

1. **(Facile)** Une adresse MAC commence par l'octet `ff`. De quel type de destination s'agit-il ? Et pour `01:00:5e:00:00:fb` ?
2. **(Facile)** Un commutateur reçoit sur le port 2 une trame de source `…:53:02` vers `…:53:09`, adresse jamais vue. Que fait-il, étape par étape ?
3. **(Facile)** Distinguez domaine de collision et domaine de diffusion.
4. **(Moyen)** Vous avez les VLAN 10 (`192.0.2.0/24`) et 20 (`198.51.100.0/24`). Un poste du VLAN 10 doit joindre un poste du VLAN 20. De quoi avez-vous besoin et quelle sera la passerelle du poste du VLAN 10 ?
5. **(Moyen)** Décodez une étiquette 802.1Q dont les 16 bits de contrôle valent `0xA064` (PCP, DEI, VID). Donnez la priorité et le numéro de VLAN.
6. **(Moyen)** Un trunk est configuré avec le VLAN natif 1 d'un côté et 999 de l'autre. Décrivez le symptôme et la correction.
7. **(Difficile)** Trois commutateurs SW1 (priorité 32768, MAC `…:00:01`), SW2 (32768, `…:00:02`) et SW3 (4096, `…:00:03`) sont reliés en triangle par des liens de même vitesse. Quel est le pont racine ? Quel lien est bloqué, et sur quel critère de départage ?
## Corrigés des exercices

1. `ff:ff:ff:ff:ff:ff` (six octets) : diffusion. `01:00:5e:00:00:fb` : multicast IPv4 (bit I/G à 1, préfixe `01:00:5e`).
2. Il apprend `…:53:02` sur le port 2, ne trouve pas `…:53:09`, puis inonde la trame sur tous les ports du VLAN sauf le port 2 ; il apprendra le port de `…:53:09` quand cette machine répondra.
3. Collision : équipements qui émettent sur le même support, réduit à un lien par le full duplex. Diffusion : équipements qui reçoivent la même trame de diffusion, réduit par VLAN et routeurs, pas par un commutateur simple.
4. Un équipement de couche 3 avec une interface par VLAN ; la passerelle du VLAN 10 est son adresse dans ce VLAN, par exemple `192.0.2.1`.
5. `0xA064` = `1010 0000 0110 0100` : PCP `101` = 5, DEI 0, VID `0x064` = 100. Priorité 5, VLAN 100.
6. Des trames non étiquetées atterrissent dans le mauvais VLAN, avec des avertissements de discordance de VLAN natif. Corriger en alignant le VLAN natif des deux côtés, après validation.
7. SW3 (priorité 4096) est la racine ; ses deux liens sont actifs. Entre SW1 et SW2, à coût égal, le meilleur identifiant de pont (SW1, MAC plus basse) rend son port désigné ; le port de SW2 vers SW1 est bloqué.
## Quiz

**Q1.** Quelle information un commutateur utilise-t-il pour choisir le port de sortie ?
A. l'adresse IP de destination — B. l'adresse MAC de destination — C. le port TCP — D. le nom d'hôte

**Q2.** Une trame d'adresse de destination inconnue arrive. Le commutateur…
A. l'abandonne — B. l'envoie au routeur — C. l'inonde sur tous les autres ports du VLAN — D. renvoie une erreur ICMP

**Q3.** Quel équipement réduit le domaine de diffusion ?
A. un concentrateur — B. un câble croisé — C. un VLAN avec un routeur entre les VLAN — D. un répéteur

**Q4.** Combien de bits compte le champ VID d'une étiquette 802.1Q ?
A. 3 — B. 8 — C. 12 — D. 16

**Q5.** Quelle est la valeur du TPID d'une trame 802.1Q ?
A. 0x0800 — B. 0x8100 — C. 0x86DD — D. 0x0806

**Q6.** Sur un port d'accès, les trames envoyées au poste sont…
A. étiquetées avec le VLAN — B. non étiquetées — C. chiffrées — D. étiquetées avec le VLAN natif

**Q7.** Le VLAN natif d'un trunk est…
A. transporté sans étiquette — B. toujours le VLAN 100 — C. interdit — D. réservé au management uniquement

**Q8.** Qui devient pont racine dans STP ?
A. le commutateur le plus rapide — B. le commutateur ayant le plus petit identifiant de pont — C. le plus récent — D. celui qui a le plus de ports

**Q9.** À quoi sert BPDU Guard ?
A. chiffrer les BPDU — B. désactiver le port s'il reçoit un BPDU alors qu'il est censé être en bordure — C. augmenter le coût du chemin — D. créer un trunk

**Q10.** Pour que deux VLAN communiquent, il faut…
A. un câble croisé — B. un équipement de couche 3 qui route entre eux — C. le même adressage MAC — D. désactiver STP

### Réponses du quiz

1. **B** — couche 2 : MAC de destination. 2. **C** — inconnue = inondation. 3. **C** — les VLAN séparent les diffusions, le routeur les relie. 4. **C** — 12 bits (1 à 4094). 5. **B** — `0x8100` ; `0x0800` IPv4, `0x86DD` IPv6, `0x0806` ARP. 6. **B** — le commutateur retire l'étiquette. 7. **A** — non étiqueté, identique aux deux bouts. 8. **B** — plus petit identifiant de pont. 9. **B** — port de bordure désactivé si un BPDU arrive. 10. **B** — seul un équipement de couche 3 relie deux réseaux.

## Erreurs fréquentes et dépannage

| Symptôme | Cause probable | Vérification (lecture seule) | Correction prudente |
|---|---|---|---|
| Deux postes du même sous-réseau ne se voient pas | ports dans des VLAN différents | `show vlan brief` / `bridge vlan show` | aligner les VLAN après validation |
| Un VLAN ne passe pas entre deux commutateurs | VLAN non autorisé sur le trunk ou non créé sur l'autre commutateur | `show interfaces trunk` | ajouter le VLAN à la liste autorisée et le créer |
| Trunk muet ou alertes de VLAN natif | un côté en accès, l'autre en trunk, ou VLAN natif différent | `show interfaces trunk` | rendre les deux extrémités cohérentes |

Autres cas : un réseau très lent aux voyants affolés évoque une boucle (vérifier `show spanning-tree`, débrancher le lien fautif) ; un port `err-disabled` vient souvent de BPDU Guard (traiter la cause avant de le réactiver).

Méthode : partir de la couche 1 (câble, voyant), vérifier la couche 2 (VLAN du port, état du trunk, table MAC, STP), puis seulement la couche 3 (adresse, passerelle). Noter chaque changement et préparer le retour arrière avant toute modification.

## À retenir

- Le commutateur **apprend** (MAC source), **transfère** (MAC destination connue) ou **inonde** (inconnue, diffusion).
- Une adresse MAC compte 48 bits ; les bits I/G et U/L du premier octet indiquent groupe/individuelle et locale/universelle.
- Un **VLAN** = un domaine de diffusion = en général un sous-réseau ; sans couche 3, pas de communication entre VLAN.
- **Accès** : un VLAN, sans étiquette. **Trunk** : plusieurs VLAN étiquetés (802.1Q, 4 octets, VID sur 12 bits), VLAN natif non étiqueté et identique des deux côtés.
- **STP/RSTP** : pont racine (plus petit identifiant), ports racine, désignés, bloqués ; PortFast et BPDU Guard sur les ports d'accès.
- Les exemples Cisco IOS sont des exemples de lab : valider toute modification avant la production.

## Pour aller plus loin

- IEEE 802.1Q (VLAN et ponts) et IEEE 802.1D (ponts MAC, STP/RSTP) : <https://standards.ieee.org/> (normes d'accès payant ou par programme ; consulter le résumé officiel).
- RFC 7042 — adresses MAC de documentation et identifiants IANA : <https://www.rfc-editor.org/rfc/rfc7042>
- RFC 826 — ARP : <https://www.rfc-editor.org/rfc/rfc826>
- RFC 5737 — blocs d'adresses IPv4 de documentation : <https://www.rfc-editor.org/rfc/rfc5737>
- Documentation du noyau Linux sur le pont (bridge) et `iproute2` : <https://www.kernel.org/doc/html/latest/networking/bridge.html>
- Page de manuel `bridge(8)` : <https://man7.org/linux/man-pages/man8/bridge.8.html>

## Crédits des images

| Fichier | Source | Auteur | Licence | Modifications |
|---|---|---|---|---|
| `images/commutation-ethernet-vlan-1.svg` | Création originale du projet Pack Master | Pack Master | CC0 — dédiée au domaine public (<https://creativecommons.org/publicdomain/zero/1.0/>) | — |
| `images/commutation-ethernet-vlan-2.svg` | Création originale du projet Pack Master | Pack Master | CC0 (<https://creativecommons.org/publicdomain/zero/1.0/>) | — |
| `images/commutation-ethernet-vlan-3.svg` | Création originale du projet Pack Master | Pack Master | CC0 (<https://creativecommons.org/publicdomain/zero/1.0/>) | — |
| `images/commutation-ethernet-vlan-4.svg` | Création originale du projet Pack Master | Pack Master | CC0 (<https://creativecommons.org/publicdomain/zero/1.0/>) | — |
| `images/commutation-ethernet-vlan-5.jpg` | <https://commons.wikimedia.org/wiki/File:RJ45_Switch_Ports.jpg> | Ben Franske | CC BY-SA 4.0 (<https://creativecommons.org/licenses/by-sa/4.0/>) | redimensionnée par Wikimedia Commons (miniature de 960 px de large, sans autre retouche) ; reste sous CC BY-SA 4.0 |

## Historique de vérification

| Date | OS/logiciel | Testeur | Verdict |
|---|---|---|---|
| 2026-11-01 | Linux (`iproute2`, `tcpdump`), équipement de type Cisco IOS | Rédaction assistée (Copilot) | Non testé sur plateforme cible |

Précision : lors de la rédaction, seules des requêtes de lecture vers l'API publique de Wikimedia Commons ont été exécutées, afin de vérifier la licence et de télécharger l'image 5. Les commandes du laboratoire et les exemples Cisco IOS n'ont **pas** été exécutés.