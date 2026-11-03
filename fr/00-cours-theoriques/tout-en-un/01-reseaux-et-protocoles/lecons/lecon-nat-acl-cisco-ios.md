---
title: "Leçon — NAT/PAT, listes de contrôle d'accès (ACL) et bases de la ligne de commande de type Cisco IOS"
description: "À l'issue de cette leçon, vous saurez :"
published: true
date: 2026-11-03T09:36:13Z
tags: ["transverse", "tout-en-un", "lecon", "reseaux", "nat", "pat", "acl", "cisco-ios", "cli", "pare-feu"]
editor: markdown
dateCreated: 2026-11-03T09:36:13Z
dateModified: 2026-11-03T09:36:13Z
---

# Leçon — NAT/PAT, listes de contrôle d'accès (ACL) et bases de la ligne de commande de type Cisco IOS

- **Tags** : `transverse`, `tout-en-un`, `lecon`, `reseaux`, `nat`, `pat`, `acl`, `cisco-ios`, `cli`, `pare-feu`
- **Niveau** : intermédiaire (couches 3 et 4)
- **Durée estimée** : 4 h (1 h 15 de cours, 2 h de laboratoire, 45 min d'exercices et de quiz)

> Texte original du pack. Les adresses sont des adresses de documentation (RFC 5737 : `192.0.2.0/24`, `198.51.100.0/24`, `203.0.113.0/24`) ; elles tiennent lieu d'adresses « privées » et « publiques » dans les schémas. Toutes les commandes de type Cisco IOS sont des **exemples de laboratoire** (simulateur ou matériel jetable) : ne jamais les appliquer en production sans validation, fenêtre de maintenance, accès de secours (console) et retour arrière. Aucun mot de passe réel ne figure ici : les valeurs `<A_DEFINIR>` sont des marqueurs.

## Objectifs pédagogiques

À l'issue de cette leçon, vous saurez :

- vous repérer dans les modes de la ligne de commande d'un équipement de type Cisco IOS et utiliser l'aide, les abréviations et les commandes `show` ;
- distinguer configuration d'exécution et configuration de démarrage ;
- expliquer le [[Glossary:NAT]] statique, dynamique et le PAT (surcharge), lire une table de traduction et citer les limites du NAT ;
- écrire et ordonner une [[Glossary:ACL]] standard ou étendue, utiliser les masques génériques (*wildcard*) et placer l'ACL au bon endroit ;
- raisonner sur l'ordre d'exécution NAT / ACL / routage ;
- reproduire NAT et filtrage dans un laboratoire Linux jetable.

## Prérequis et durée

- Adressage IPv4 et sous-réseaux ; routage de base ([leçon sur le routage](/fr/00-cours-theoriques/tout-en-un/01-reseaux-et-protocoles/lecons/lecon-routage-ip)) ; notions de [[Glossary:VLAN]] ([leçon sur la commutation](/fr/00-cours-theoriques/tout-en-un/01-reseaux-et-protocoles/lecons/lecon-commutation-ethernet-vlan)).
- Notions de ports [[Glossary:TCP]]/UDP (80, 443, 53, 23, 22).
- Laboratoire : une [[Glossary:VM]] Linux jetable avec `iproute2`, `nftables`, `tcpdump` (et `conntrack` en option) ; ou un simulateur de réseau gratuit pour les exemples Cisco IOS.
- Durée : environ 4 h.

## L'essentiel en bref

- La **[[Glossary:CLI]] Cisco IOS** est organisée en **modes** (`>` utilisateur, `#` privilégié, `(config)#` global, `(config-if)#` interface) ; `?` donne l'aide ; `show` consulte, rien n'est permanent tant qu'on n'a pas sauvegardé.
- Le **NAT** traduit des adresses ; le **PAT** (NAT « overload ») fait partager **une** adresse publique à de nombreux postes en distinguant les flux par le **port**.
- Une **ACL** est une liste de règles lues **de haut en bas** : la **première** qui correspond s'applique ; un **deny implicite** termine toute liste.
- Une ACL se **place** sur une interface avec un sens (`in` ou `out`) ; mal placée, elle coupe tout, y compris votre propre accès d'administration.
- Le NAT n'est **pas** un pare-feu : il masque les adresses, il ne décide pas de ce qui est autorisé.

## 1. Les bases de la ligne de commande de type Cisco IOS

### 1.1 Les modes

![Les quatre modes de la CLI de type Cisco IOS et les commandes pour passer de l'un à l'autre](images/nat-acl-cisco-ios-3.svg)

*Quatre niveaux emboîtés, reconnaissables à l'invite. Création originale du projet Pack Master, dédiée au domaine public (CC0).*

| Invite | Mode | Usage |
|---|---|---|
| `Router>` | utilisateur | consultation très limitée |
| `Router#` | privilégié | tous les `show`, sauvegardes, `reload` |
| `Router(config)#` | configuration globale | nom, routes, listes, NAT |
| `Router(config-if)#` | configuration d'interface | adresse, `ip nat inside`, `ip access-group` |

Analogie : un bâtiment à accès par badges — le hall (utilisateur), le bureau (privilégié), l'atelier de réglages (configuration), puis l'armoire d'une machine précise (interface). On ne règle une interface qu'une fois entré dans son armoire.

### 1.2 Premiers gestes (lab)

```text
Router> enable
Router# show version
Router# show ip interface brief
Router# show running-config
Router# configure terminal
Router(config)# hostname R1
R1(config)# interface GigabitEthernet0/0
R1(config-if)# description LAN-interne
R1(config-if)# ip address 192.0.2.1 255.255.255.0
R1(config-if)# no shutdown
R1(config-if)# end
R1# copy running-config startup-config
```

👉 Explication : `enable` passe en mode privilégié ; les trois `show` sont des consultations (version, état résumé des interfaces, configuration en cours). Ensuite on nomme l'équipement, on configure une interface (description, adresse, activation avec `no shutdown`) et `end` revient au mode privilégié. La dernière ligne **sauvegarde** : sans elle, le changement disparaît au redémarrage. En production, ne sauvegardez qu'après validation du changement.

### 1.3 Aide, abréviations et négation

- `?` seul affiche les commandes possibles ; `show ip ?` les suites possibles ; `sh ip int br` est l'abréviation de `show ip interface brief` ; la touche Tab complète.
- Le préfixe **`no`** annule une commande : `no shutdown` active l'interface, `no ip access-group LAN-OUT in` retire une ACL.
- `do show ...` exécute un `show` depuis un mode de configuration.
- Un message `% Invalid input detected` signale une erreur de syntaxe, avec un `^` sous l'endroit fautif.

### 1.4 Configuration d'exécution et de démarrage

La **running-config** (en mémoire vive) est celle qui s'applique tout de suite ; la **startup-config** (mémoire non volatile) est relue au démarrage. Toute commande de configuration modifie la première seulement. Cette séparation est un filet de sécurité de laboratoire : en cas d'erreur, un redémarrage (`reload`) rétablit la dernière configuration sauvegardée, au prix d'une coupure. Sur un équipement réel, `reload` et `erase` sont des opérations à fenêtre de maintenance.

### 1.5 Accès sécurisé (principe)

Préférer **[[Glossary:SSH]]** à Telnet (qui transmet tout en clair), utiliser un secret robuste stocké hors du dépôt (marqueur `<A_DEFINIR>`) et limiter les adresses autorisées à administrer l'équipement. Exemple de lab : `enable secret <A_DEFINIR>`, puis `crypto key generate rsa modulus 2048` (nom d'hôte et domaine requis) et, sur `line vty 0 4`, `transport input ssh` et `login local`.

👉 Explication : ces commandes protègent le mode privilégié et imposent SSH ; une erreur sur les lignes `vty` peut vous interdire l'accès distant, donc lab uniquement.

## 2. Le NAT : traduire les adresses

### 2.1 Pourquoi

Les réseaux locaux utilisent des adresses **privées** (RFC 1918 : `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`) qui ne sont pas routées sur Internet. Le **NAT** (*Network Address Translation*, RFC 3022) remplace, au passage du routeur, une adresse par une autre. Il a prolongé la vie d'IPv4 face à la pénurie d'adresses. *Dans les schémas, `192.0.2.0/24` joue le rôle du réseau privé et `203.0.113.1` celui de l'adresse publique, pour rester dans les plages de documentation.*

Analogie : une réception d'entreprise. Le standard (le routeur) affiche **un seul numéro** public ; il note qui, à l'intérieur, a appelé quelle ligne et rebranche la réponse au bon poste.

### 2.2 Vocabulaire des quatre adresses

**Inside local** : poste interne vu de l'intérieur (`192.0.2.10`) ; **inside global** : le même poste vu de l'extérieur (`203.0.113.1`) ; **outside global** : serveur distant réel (`198.51.100.80`) ; **outside local** : ce serveur vu de l'intérieur (en général identique).

### 2.3 Les trois formes

- **NAT statique** : une correspondance fixe un-pour-un (`192.0.2.20` ⇄ `203.0.113.20`). Pour publier un serveur interne ; on peut aussi n'associer qu'un port (*redirection de port*).
- **NAT dynamique** : les adresses internes sont traduites vers un **pool** d'adresses publiques, à la demande. Rarement utile : il faut autant d'adresses publiques que de postes simultanés.
- **PAT** (*Port Address Translation*, ou NAT « overload » / masquerade) : une seule adresse publique ; les flux sont distingués par le **port source**. C'est le NAT des box domestiques et de la plupart des entreprises.

![Schéma du PAT : deux postes internes partagent l'adresse externe 203.0.113.1 et la table de traduction associe les ports](images/nat-acl-cisco-ios-1.svg)

*Le PAT : le routeur réécrit l'adresse (et le port) source à la sortie et retrouve le poste d'origine au retour grâce à la table de traduction. Création originale du projet Pack Master, dédiée au domaine public (CC0).*

### 2.4 Déroulement d'une traduction PAT

1. PC1 (`192.0.2.10`, port source 51000) envoie une requête HTTPS vers `198.51.100.80:443`.
2. Le routeur choisit un port externe libre (par exemple 40001), crée l'entrée `192.0.2.10:51000 ⇄ 203.0.113.1:40001` et envoie `203.0.113.1:40001 → 198.51.100.80:443`.
3. Le serveur répond vers `203.0.113.1:40001`.
4. Le routeur consulte sa table, retrouve `192.0.2.10:51000` et réécrit l'adresse et le port de **destination** avant de transmettre.

Sans entrée dans la table, un paquet venu de l'extérieur n'a nulle part où aller : c'est la raison pour laquelle le PAT bloque, de fait, les connexions **entrantes** non sollicitées. C'est un effet de bord utile, **pas** une politique de sécurité. Les entrées expirent après inactivité.

### 2.5 Configuration de type Cisco IOS (lab)

```text
R1(config)# interface GigabitEthernet0/0
R1(config-if)# ip nat inside
R1(config-if)# interface GigabitEthernet0/1
R1(config-if)# ip nat outside
R1(config-if)# exit
R1(config)# access-list 1 permit 192.0.2.0 0.0.0.255
R1(config)# ip nat inside source list 1 interface GigabitEthernet0/1 overload
R1(config)# end
```

👉 Explication : marque l'interface interne (`inside`) et l'interface externe (`outside`), définit par une ACL standard les adresses autorisées à être traduites (`192.0.2.0/24`) et active le PAT : les adresses de l'ACL sont traduites vers l'adresse de l'interface externe (`overload`). L'ACL joue ici le rôle de **sélecteur** de trafic à traduire, non de filtre de sécurité.

NAT statique avec redirection de port (publier un serveur HTTPS interne, lab) :

```text
R1(config)# ip nat inside source static tcp 192.0.2.20 443 interface GigabitEthernet0/1 443
```

👉 Explication : tout trafic TCP arrivant sur le port 443 de l'adresse externe est redirigé vers `192.0.2.20:443`. Exposer un service interne est une décision de sécurité : à valider, à limiter par ACL et à journaliser.

Vérifier (lecture seule) :

```text
R1# show ip nat translations
R1# show ip nat statistics
```

👉 Explication : la première affiche la table (colonnes Inside global / Inside local / Outside local / Outside global), la seconde les compteurs (traductions actives, accès, échecs). La commande `clear ip nat translation *` supprime des entrées actives : à éviter en production en pleine activité.

### 2.6 Limites et pièges

- Le NAT **brise** la transparence de bout en bout : les protocoles qui transportent des adresses dans leurs données exigent un traitement spécial (ALG).
- Un port externe par flux : la table peut se saturer (environ 64 000 ports par adresse).
- La journalisation est plus difficile : le serveur voit l'adresse du routeur, pas celle du poste ; conserver les journaux de traduction si la traçabilité est requise.
- IPv6 se passe de NAT et le NAT n'y remplace **pas** un pare-feu ; les opérateurs utilisent parfois un NAT de grande échelle (CGNAT, `100.64.0.0/10`, RFC 6598).

## 3. Les ACL : filtrer le trafic

### 3.1 Principe

Une **liste de contrôle d'accès** (ACL) est une suite ordonnée de règles `permit` (autoriser) ou `deny` (refuser) examinées pour chaque paquet. Analogie : la liste d'un videur — on la lit du haut vers le bas, et dès qu'une ligne correspond on obéit, sans lire la suite. Si aucune ligne ne correspond, le videur refuse (**deny implicite**).

![Évaluation d'une ACL de haut en bas : première correspondance gagnante puis deny implicite](images/nat-acl-cisco-ios-2.svg)

*Première correspondance gagnante, deny implicite à la fin. Création originale du projet Pack Master, dédiée au domaine public (CC0).*

### 3.2 Types

- **Standard** (numéros 1 à 99 et 1300 à 1999) : ne regarde que l'adresse **source**.
- **Étendue** (100 à 199 et 2000 à 2699) : protocole, source, destination, ports.
- **Nommée** : standard ou étendue, avec un nom parlant (`LAN-OUT`) et la possibilité de remarques et de numéros de séquence. C'est la forme recommandée.

### 3.3 Le masque générique (wildcard)

Un masque générique est l'**inverse** d'un masque de sous-réseau : `0` = « ce bit doit correspondre », `1` = « bit ignoré ».

| Besoin | Syntaxe | Équivaut à |
|---|---|---|
| un seul hôte | `host 192.0.2.50` ou `192.0.2.50 0.0.0.0` | `192.0.2.50/32` |
| un réseau /24 | `192.0.2.0 0.0.0.255` | `192.0.2.0/24` |
| un /26 | `192.0.2.64 0.0.0.63` | `192.0.2.64/26` |
| tout | `any` | `0.0.0.0/0` |

### 3.4 Exemple d'ACL étendue nommée (lab)

```text
R1(config)# ip access-list extended LAN-OUT
R1(config-ext-nacl)# remark Pas de Telnet depuis ce poste
R1(config-ext-nacl)# deny tcp host 192.0.2.50 any eq 23
R1(config-ext-nacl)# permit tcp 192.0.2.0 0.0.0.255 any eq 443
R1(config-ext-nacl)# permit tcp 192.0.2.0 0.0.0.255 any eq 80
R1(config-ext-nacl)# permit udp 192.0.2.0 0.0.0.255 host 198.51.100.53 eq 53
R1(config-ext-nacl)# permit icmp 192.0.2.0 0.0.0.255 any
R1(config-ext-nacl)# exit
R1(config)# interface GigabitEthernet0/0
R1(config-if)# ip access-group LAN-OUT in
R1(config-if)# end
```

👉 Explication : la liste refuse Telnet venant d'un poste précis, autorise le Web, la résolution [[Glossary:DNS]] vers un serveur désigné et le ping depuis le réseau interne, puis applique la liste **en entrée** de l'interface interne. Tout ce qui n'est pas listé (SSH, [[Glossary:SMTP]]…) est refusé par le deny implicite. Lab uniquement : appliquée par erreur sur l'interface de gestion, elle coupe votre session.

Vérifier (lecture seule) :

```text
R1# show access-lists
R1# show ip interface GigabitEthernet0/0
```

👉 Explication : la première affiche les règles avec leurs compteurs de correspondances (`matches`), très utiles pour savoir quelle ligne agit ; la seconde indique la liste appliquée (`Inbound access list is LAN-OUT`).

### 3.5 Règles de conception

- **Ordre** : règles précises d'abord, générales ensuite ; un `permit ip any any` trop haut rend le reste inutile.
- **Placement** : ACL étendue près de la **source** du trafic à bloquer, ACL standard près de la **destination** (elle ne connaît que la source).
- **Sens** : `in` = avant le routage, `out` = après ; une ACL par interface, sens et protocole.
- **Documenter** : une ligne `remark` par règle importante, sauvegarde avant modification.
- **Accès de secours** : garder une session ouverte et un accès console, prévoir un retour arrière.
- **Administration** : une ACL standard sur les lignes `vty` (`access-class`) plutôt que sur les interfaces.

## 4. NAT, ACL et routage : l'ordre compte

Pour un paquet qui traverse le routeur de l'**intérieur vers l'extérieur** : ACL entrante de l'interface interne (adresses **avant** NAT) → routage → traduction NAT → ACL sortante de l'interface externe (adresses **après** NAT). Dans l'autre sens : ACL entrante de l'interface externe (adresse **publique**), NAT, routage, ACL sortante (adresse **privée**). Retenez : *l'ACL voit toujours l'adresse telle qu'elle existe à cet endroit du trajet*. Une ACL qui nomme une adresse interne sur l'interface externe en entrée ne correspondra donc jamais.

## Mise en pratique guidée

Objectif : reproduire dans une **VM Linux jetable** un PAT et un filtrage, avec `nftables` (le pendant libre du routeur de type Cisco IOS), puis refaire l'exercice avec la syntaxe IOS dans un simulateur de votre choix.

> **Avertissement** : ces commandes créent des espaces de noms et des règles de filtrage avec des droits d'administration, **uniquement dans les espaces de noms** du laboratoire. Elles n'ont pas été exécutées par l'auteur de ce texte. N'utilisez pas `nft flush ruleset` sur l'hôte lui-même.

### Étape 1 — Topologie : lan — gw — srv

```bash
for n in lan gw srv; do sudo ip netns add $n; sudo ip -n $n link set lo up; done
sudo ip link add eth0 netns lan type veth peer name eth0 netns gw
sudo ip link add eth1 netns gw type veth peer name eth0 netns srv
sudo ip -n lan addr add 192.0.2.10/24 dev eth0
sudo ip -n gw addr add 192.0.2.1/24 dev eth0
sudo ip -n gw addr add 203.0.113.1/24 dev eth1
sudo ip -n srv addr add 203.0.113.80/24 dev eth0
for p in "lan eth0" "gw eth0" "gw eth1" "srv eth0"; do set -- $p; sudo ip -n $1 link set $2 up; done
sudo ip -n lan route add default via 192.0.2.1
sudo ip netns exec gw sysctl -w net.ipv4.ip_forward=1
```

👉 Explication : `lan` (réseau interne), `gw` (le routeur NAT, interface interne `eth0` et externe `eth1`) et `srv` (un serveur « de l'extérieur » dans `203.0.113.0/24`). `srv` n'a aucune route vers `192.0.2.0/24`, comme un serveur Internet n'en a pas vers un réseau privé.

### Étape 2 — Constater l'échec sans NAT

```bash
sudo ip netns exec lan ping -c 2 -W 1 203.0.113.80
```

👉 Explication : le ping doit échouer (100 % de perte) : la requête arrive jusqu'à `srv`, mais celui-ci ne sait pas renvoyer sa réponse vers `192.0.2.10`.

### Étape 3 — Activer le PAT (masquerade)

```bash
sudo ip netns exec gw nft add table ip nat
sudo ip netns exec gw nft add chain ip nat postrouting '{ type nat hook postrouting priority 100 ; }'
sudo ip netns exec gw nft add rule ip nat postrouting oifname "eth1" masquerade
sudo ip netns exec lan ping -c 2 203.0.113.80
```

👉 Explication : crée une table et une chaîne `nat` accrochées à la sortie du routage, puis une règle qui remplace l'adresse source par celle de `eth1` pour tout paquet sortant par `eth1`. Le ping doit maintenant réussir. C'est l'équivalent de `ip nat inside source list 1 interface ... overload`.

### Étape 4 — Observer la traduction

```bash
sudo ip netns exec srv tcpdump -n -c 2 -i eth0 icmp
sudo ip netns exec gw conntrack -L
```

👉 Explication : lancez `tcpdump` dans un second terminal avant le ping : `srv` voit l'adresse source `203.0.113.1` (celle du routeur), jamais `192.0.2.10`. `conntrack -L` (si l'outil `conntrack` est installé) affiche la table de suivi de connexions, équivalent de `show ip nat translations` ; la consultation est en lecture seule.

### Étape 5 — Ajouter une règle de filtrage (ACL)

```bash
sudo ip netns exec gw nft add table ip filter
sudo ip netns exec gw nft add chain ip filter forward '{ type filter hook forward priority 0 ; policy accept ; }'
sudo ip netns exec gw nft add rule ip filter forward ip saddr 192.0.2.0/24 icmp type echo-request counter drop
sudo ip netns exec lan ping -c 2 -W 1 203.0.113.80
sudo ip netns exec gw nft -a list ruleset
```

👉 Explication : crée une chaîne de filtrage des paquets **transitant** par `gw` (politique par défaut : accepter) et une règle qui abandonne les requêtes ping venant du réseau interne, avec un compteur. Le ping échoue à nouveau ; `nft -a list ruleset` montre les règles, leur compteur (équivalent de `matches`) et un numéro de `handle`.

### Étape 6 — Retirer la règle puis nettoyer

```bash
sudo ip netns exec gw nft -a list chain ip filter forward
sudo ip netns exec gw nft delete rule ip filter forward handle <NUMERO>
for n in lan gw srv; do sudo ip netns del $n; done
ip netns list
```

👉 Explication : repérez le numéro (`handle`) de la règle dans la première commande, remplacez `<NUMERO>` par cette valeur pour la supprimer (le ping reviendrait), puis supprimez les espaces de noms : tout ce qui a été créé disparaît avec eux. La dernière commande vérifie qu'il n'en reste aucun du lab.

## Exercices

1. **(Facile)** Quelle invite correspond au mode de configuration d'interface ? Quelle commande permet de revenir directement au mode privilégié ?
2. **(Facile)** Donnez le masque générique d'un réseau `/24` et d'un hôte unique.
3. **(Moyen)** Décrivez ce que voit le serveur `198.51.100.80` quand `192.0.2.10:51000` le contacte à travers un PAT dont l'adresse externe est `203.0.113.1`. Quelle entrée la table contient-elle ?
4. **(Moyen)** Une ACL contient : `10 permit ip any any` puis `20 deny tcp any any eq 23`. Telnet est-il bloqué ? Corrigez.
5. **(Moyen)** Écrivez (en syntaxe IOS, pour un lab) une ACL standard nommée `ADMIN` autorisant uniquement `192.0.2.0/26` et son application sur les lignes `vty`. Quel risque devez-vous anticiper ?
6. **(Difficile)** Après avoir appliqué `ip access-group LAN-OUT out` sur l'interface **externe** avec une règle `permit tcp 192.0.2.0 0.0.0.255 any eq 443`, plus rien ne passe. Pourquoi ? Que faut-il écrire ?
7. **(Difficile)** Un serveur interne `192.0.2.20` doit être joignable en HTTPS depuis l'extérieur. Listez les éléments à prévoir (NAT, ACL, journalisation, test) et les risques.

## Corrigés des exercices

1. `Router(config-if)#`. `end` (ou Ctrl+Z) revient au mode privilégié ; `exit` ne remonte que d'un niveau.
2. `/24` : `0.0.0.255` ; hôte unique : `0.0.0.0` (ou le mot-clé `host`).
3. Il voit une connexion venant de `203.0.113.1`, port externe choisi par le routeur (par exemple 40001), jamais `192.0.2.10`. La table contient `192.0.2.10:51000` (inside local) ⇄ `203.0.113.1:40001` (inside global), vers `198.51.100.80:443`.
4. Non : la ligne 10 autorise tout et s'arrête là (première correspondance gagnante). Il faut placer le `deny tcp any any eq 23` **avant** le `permit ip any any` (en nommée, utiliser des numéros de séquence ou réécrire la liste).
5. `ip access-list standard ADMIN` / `permit 192.0.2.0 0.0.0.63` ; puis `line vty 0 4` / `access-class ADMIN in`. Risque : se couper l'accès si l'adresse de votre poste n'est pas dans `192.0.2.0/26`. Prévoir une session ouverte, un accès console et un retour arrière.
6. L'ACL sortante est évaluée **après** NAT : l'adresse source n'est plus `192.0.2.x` mais `203.0.113.1`, donc la règle ne correspond jamais et le deny implicite abandonne tout. Il faut autoriser l'adresse traduite (`permit tcp host 203.0.113.1 any eq 443`) ou filtrer plutôt en entrée de l'interface interne, avant NAT.
7. Un NAT statique (redirection du port 443 vers `192.0.2.20`), une ACL entrante externe limitant aux ports voulus (443) et, si possible, aux sources attendues, une journalisation, un test depuis l'extérieur et la surveillance des compteurs. Risques : exposition d'un service, vulnérabilités du serveur, rebond vers le réseau interne ; la bonne pratique est de placer le serveur dans une zone séparée ([[Glossary:DMZ]]).

## Quiz

**Q1.** Quelle invite indique le mode de configuration globale ?
A. `Router>` — B. `Router#` — C. `Router(config)#` — D. `Router(config-if)#`

**Q2.** Quelle commande sauvegarde la configuration d'exécution dans la configuration de démarrage ?
A. `copy running-config startup-config` — B. `show running-config` — C. `reload` — D. `erase startup-config`

**Q3.** Que fait le préfixe `no` ?
A. il affiche l'aide — B. il annule ou supprime une commande — C. il redémarre l'équipement — D. il passe en mode utilisateur

**Q4.** Quel NAT permet à de nombreux postes de partager une seule adresse publique ?
A. NAT statique — B. NAT dynamique avec pool — C. PAT (overload) — D. aucun

**Q5.** Comment le PAT distingue-t-il les flux ?
A. par l'adresse MAC — B. par le port source traduit — C. par le [[Glossary:TTL]] — D. par le VLAN

**Q6.** Le NAT est-il un pare-feu ?
A. oui, par défaut — B. non : il traduit, il ne décide pas de la politique d'autorisation — C. oui, uniquement en statique — D. seulement en IPv6

**Q7.** Une ACL ne contient aucune règle correspondant à un paquet. Que se passe-t-il ?
A. il est autorisé — B. il est refusé (deny implicite) — C. il est mis en file — D. la liste se supprime

**Q8.** Quel masque générique désigne `192.0.2.0/24` ?
A. `255.255.255.0` — B. `0.0.0.255` — C. `0.0.0.0` — D. `255.0.0.0`

**Q9.** Où place-t-on de préférence une ACL étendue ?
A. près de la destination — B. près de la source du trafic à bloquer — C. sur une interface de bouclage — D. nulle part

**Q10.** Pour un trafic sortant, que voit une ACL en sortie de l'interface externe ?
A. l'adresse interne avant NAT — B. l'adresse après NAT — C. aucune adresse — D. uniquement l'adresse MAC

### Réponses du quiz

1. **C** — `(config)#` = global ; `(config-if)#` = interface. 2. **A** — copie la configuration en cours vers la configuration de démarrage. 3. **B** — `no` inverse une commande. 4. **C** — le PAT partage une adresse grâce aux ports. 5. **B** — port source traduit, mémorisé dans la table. 6. **B** — le NAT masque, il n'autorise ni n'interdit : on ajoute des ACL ou un pare-feu. 7. **B** — deny implicite final. 8. **B** — l'inverse de `255.255.255.0`. 9. **B** — près de la source on économise de la bande passante, car l'ACL étendue sait filtrer sur la destination. 10. **B** — l'ACL sortante est évaluée après NAT.

## Erreurs fréquentes et dépannage

| Symptôme | Cause probable | Vérification (lecture seule) |
|---|---|---|
| Aucun accès extérieur après activation du NAT | interfaces `inside`/`outside` inversées ou oubliées | `show ip nat statistics`, `show running-config interface …` |
| Table de traduction vide | l'ACL de sélection ne correspond pas (masque générique faux) | `show access-lists` (compteurs), `show ip nat translations` |
| Seuls certains protocoles échouent | ACL trop restrictive (deny implicite) | `show access-lists`, compteurs `matches` |
| Une règle semble ignorée | une règle plus haute l'a masquée | ordre des lignes, numéros de séquence |
| Accès d'administration perdu après une ACL | ACL appliquée au mauvais endroit ou dans le mauvais sens | console, retour arrière préparé |
| Serveur interne inaccessible de l'extérieur | pas de NAT statique ou ACL entrante bloquante | `show ip nat translations`, `show access-lists` |
| Une configuration disparaît au redémarrage | oubli de `copy running-config startup-config` | comparer running et startup |

Méthode : écrire le trajet attendu (source, destination, ports, adresses avant et après NAT), vérifier les compteurs avant et après un test, modifier **une chose à la fois** et valider en lab avant toute production.

## À retenir

- CLI IOS : `>` → `#` → `(config)#` → `(config-if)#` ; `?`, Tab, `no`, `show` ; sauvegarder avec `copy running-config startup-config` seulement une fois le changement validé.
- NAT = traduction d'adresses ; PAT = une adresse partagée, flux distingués par le port ; vocabulaire inside local/global, outside local/global.
- Le NAT ne remplace pas un pare-feu ; il a des limites (transparence, journalisation, saturation des ports).
- ACL = règles ordonnées, première correspondance gagnante, **deny implicite**, masque générique inversé ; étendue près de la source, standard près de la destination.
- L'ACL voit les adresses telles qu'elles sont à l'endroit de son application (avant ou après NAT).
- Toute commande d'exemple est destinée à un lab : valider, préparer un accès de secours et un retour arrière avant la production.

## Pour aller plus loin

- RFC 3022 — NAT traditionnel : <https://www.rfc-editor.org/rfc/rfc3022>
- RFC 1918 — adresses privées : <https://www.rfc-editor.org/rfc/rfc1918>
- RFC 6598 — espace d'adresses partagées pour le NAT de grande échelle : <https://www.rfc-editor.org/rfc/rfc6598>
- RFC 5737 — adresses de documentation : <https://www.rfc-editor.org/rfc/rfc5737>
- Documentation officielle Cisco (centre d'assistance ; chercher les guides « NAT Configuration Guide » et « Access Control Lists » de la version utilisée ; le site peut refuser les accès automatisés) : <https://www.cisco.com/c/en/us/support/index.html>
- Wiki officiel de nftables : <https://wiki.nftables.org/>
- Page de manuel `nft(8)` : <https://www.netfilter.org/projects/nftables/manpage.html>

## Crédits des images

| Fichier | Source | Auteur | Licence | Modifications |
|---|---|---|---|---|
| `images/nat-acl-cisco-ios-1.svg` | Création originale du projet Pack Master | Pack Master | CC0 — dédiée au domaine public (<https://creativecommons.org/publicdomain/zero/1.0/>) | — |
| `images/nat-acl-cisco-ios-2.svg` | Création originale du projet Pack Master | Pack Master | CC0 (<https://creativecommons.org/publicdomain/zero/1.0/>) | — |
| `images/nat-acl-cisco-ios-3.svg` | Création originale du projet Pack Master | Pack Master | CC0 (<https://creativecommons.org/publicdomain/zero/1.0/>) | — |

## Historique de vérification

| Date | OS/logiciel | Testeur | Verdict |
|---|---|---|---|
| 2026-11-01 | Linux (`iproute2`, `nftables`, `conntrack`), équipement de type Cisco IOS | Rédaction assistée (Copilot) | Non testé sur plateforme cible |

Précision : aucune commande de la leçon n'a été exécutée lors de la rédaction ; la syntaxe IOS et nftables est donnée à titre d'exemple de laboratoire et doit être vérifiée sur la version utilisée.