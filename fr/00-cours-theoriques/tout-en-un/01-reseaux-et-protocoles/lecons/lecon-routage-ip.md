---
title: "Leçon — Routage IP : passerelle, table de routage, routes statiques et routage dynamique"
description: "À l'issue de cette leçon, vous saurez :"
published: true
date: 2026-11-03T09:36:13Z
tags: ["transverse", "tout-en-un", "lecon", "reseaux", "routage", "passerelle", "table-de-routage", "rip", "ospf", "bgp"]
editor: markdown
dateCreated: 2026-11-03T09:36:13Z
dateModified: 2026-11-03T09:36:13Z
---

# Leçon — Routage IP : passerelle, table de routage, routes statiques et routage dynamique

- **Tags** : `transverse`, `tout-en-un`, `lecon`, `reseaux`, `routage`, `passerelle`, `table-de-routage`, `rip`, `ospf`, `bgp`
- **Niveau** : débutant à intermédiaire (couche 3 du modèle OSI)
- **Durée estimée** : 3 h 30 (1 h 15 de cours, 1 h 30 de laboratoire, 45 min d'exercices et de quiz)

> Texte original du pack. Les adresses utilisées sont des adresses de documentation (RFC 5737 : `192.0.2.0/24`, `198.51.100.0/24`, `203.0.113.0/24`). Les commandes qui modifient une configuration sont des exemples de laboratoire : ne jamais les appliquer en production sans validation, fenêtre de maintenance et retour arrière.

## Objectifs pédagogiques

À l'issue de cette leçon, vous saurez :

- expliquer comment un hôte décide d'envoyer un paquet directement ou à sa passerelle ;
- lire une table de routage ligne par ligne (préfixe, saut suivant, interface, métrique) ;
- appliquer la règle du préfixe le plus long et expliquer la route par défaut ;
- créer des routes statiques (Linux, exemple de type Cisco IOS) et penser à la route retour ;
- décrire le principe de RIP, OSPF et BGP et choisir une famille de protocole selon le contexte ;
- diagnostiquer une panne de routage avec `ip route get`, `ping` et `traceroute`.

## Prérequis et durée

- Adressage IPv4, masque et notation CIDR ; notion de commutateur et de VLAN ([leçon sur la commutation](/fr/00-cours-theoriques/tout-en-un/01-reseaux-et-protocoles/lecons/lecon-commutation-ethernet-vlan)).
- Terminal Linux ; pour le laboratoire, une VM Linux jetable avec `iproute2` (`traceroute` optionnel).
- Durée : environ 3 h 30.

## L'essentiel en bref

- Un **routeur** relie des réseaux IP différents et transmet les paquets d'un réseau à l'autre.
- La **passerelle par défaut** est le routeur local vers lequel un hôte envoie tout ce qui n'est pas dans son propre sous-réseau.
- La **table de routage** associe un préfixe de destination à un saut suivant et/ou une interface ; le **préfixe le plus long** gagne ; `0.0.0.0/0` est la route par défaut.
- Une **route statique** est écrite à la main ; elle est simple, prévisible, mais ne s'adapte pas aux pannes.
- Un **protocole de routage dynamique** apprend et met à jour les routes automatiquement : RIP (distance), OSPF (état de liens), BGP (entre organisations).
- Il faut toujours une **route aller et une route retour** : sans elle, le ping part mais la réponse ne revient jamais.

## 1. Le routeur et la passerelle

### 1.1 Analogie

Un routeur est un carrefour avec des panneaux : il ne connaît pas toute la route, seulement la bonne direction suivante pour chaque destination. Le courrier postal fonctionne ainsi : le bureau local ne sait pas porter la lettre jusqu'à la porte, il l'envoie au centre de tri suivant, qui fait de même. Chaque saut ne choisit que le **prochain** maillon.

### 1.2 La décision de l'hôte

Avant d'émettre, un hôte compare l'adresse de destination à **son propre sous-réseau** (adresse et masque). Si la destination est dans le même sous-réseau, il demande l'adresse MAC par ARP et envoie directement. Sinon, il envoie la trame à sa **passerelle par défaut** : l'adresse IP de destination reste celle du serveur lointain, mais l'adresse MAC de destination devient celle de la passerelle.

![Organigramme de la décision d'envoi d'un paquet : sous-réseau local, passerelle, recherche dans la table, route par défaut ou abandon](images/routage-ip-2.svg)

*Trois questions successives : le sous-réseau local ? la table du routeur ? la route par défaut ? Création originale du projet Pack Master, dédiée au domaine public (CC0).*

### 1.3 Ce qui change à chaque saut

À chaque routeur traversé : l'adresse IP source et destination **ne changent pas** (hors NAT, traité dans la [leçon NAT, ACL et CLI](/fr/00-cours-theoriques/tout-en-un/01-reseaux-et-protocoles/lecons/lecon-nat-acl-cisco-ios)) ; les adresses MAC sont **réécrites** ; le champ TTL (durée de vie) est décrémenté de 1 ; la somme de contrôle d'en-tête est recalculée. Si le TTL tombe à 0, le routeur abandonne le paquet et renvoie un message ICMP « Time Exceeded » : c'est ce que `traceroute` exploite.

Pour voir la configuration d'un hôte Linux (lecture seule) :

```bash
ip -br addr show
ip route show
```

👉 Explication : la première commande liste les interfaces et leurs adresses ; la seconde affiche la table de routage du noyau. Aucune modification.

Sur Windows :

```powershell
Get-NetIPConfiguration
Get-NetRoute -AddressFamily IPv4 | Sort-Object DestinationPrefix
```

👉 Explication : affiche adresses, passerelles et DNS, puis les routes IPv4 triées par préfixe. Lecture seule.

## 2. La table de routage

### 2.1 Ce que contient une ligne

Chaque entrée contient au minimum :

| Champ | Rôle |
|---|---|
| Préfixe de destination | réseau visé, en notation CIDR (`203.0.113.0/24`) |
| Saut suivant (*next hop*) | adresse du prochain routeur (absent pour un réseau directement connecté) |
| Interface de sortie | port par lequel émettre |
| Métrique | « coût » servant à départager plusieurs routes vers un même préfixe d'un même protocole |
| Origine | connectée, statique ou protocole dynamique ; sur les équipements de type Cisco, une **distance administrative** classe les origines (connectée 0, statique 1, eBGP 20, OSPF 110, RIP 120) |

![Topologie de laboratoire : PC1 dans 192.0.2.0/24, deux routeurs R1 et R2 reliés par 198.51.100.0/30, serveur dans 203.0.113.0/24](images/routage-ip-1.svg)

*Le réseau de référence de la leçon : deux routeurs, trois réseaux. Création originale du projet Pack Master, dédiée au domaine public (CC0).*

### 2.2 Lecture pas à pas d'un exemple

Voici la table du routeur R1 du schéma, sur un équipement de type Cisco IOS (sortie illustrative, non capturée, abrégée) :

```text
R1# show ip route
Gateway of last resort is not set

      192.0.2.0/24 is variably subnetted, 2 subnets, 2 masks
C        192.0.2.0/24 is directly connected, GigabitEthernet0/0
L        192.0.2.1/32 is directly connected, GigabitEthernet0/0
      198.51.100.0/24 is variably subnetted, 2 subnets, 2 masks
C        198.51.100.0/30 is directly connected, GigabitEthernet0/1
L        198.51.100.1/32 is directly connected, GigabitEthernet0/1
S     203.0.113.0/24 [1/0] via 198.51.100.2
```

👉 Explication : `show ip route` est une commande de consultation. Lecture ligne par ligne : `C` = réseau directement connecté (R1 a une interface dedans) ; `L` = adresse locale du routeur lui-même (`/32`) ; `S` = route statique. Dans `[1/0]`, 1 est la distance administrative d'une route statique et 0 la métrique. `via 198.51.100.2` est le saut suivant : R1 enverra à R2 tout paquet pour `203.0.113.0/24`. « Gateway of last resort is not set » indique qu'il n'y a pas de route par défaut : une destination inconnue sera abandonnée.

L'équivalent Linux sur un routeur ou un hôte :

```bash
ip route show
```

👉 Explication : la sortie ressemble à `192.0.2.0/24 dev eth0 proto kernel scope link src 192.0.2.1` (réseau connecté, créé automatiquement par le noyau) et `203.0.113.0/24 via 198.51.100.2 dev eth1` (route statique). `default via 192.0.2.254 dev eth0` serait la route par défaut.

### 2.3 Le préfixe le plus long

Quand plusieurs routes couvrent la destination, le routeur retient la plus **spécifique**, c'est-à-dire celle dont le masque est le plus long. Exemple de table :

| Préfixe | Saut suivant |
|---|---|
| `0.0.0.0/0` | A |
| `203.0.113.0/24` | B |
| `203.0.113.128/25` | C |

- Destination `203.0.113.200` : trois routes la couvrent ; `/25` est la plus longue → saut suivant **C**.
- Destination `203.0.113.50` : `/25` ne couvre que `.128` à `.255` ; `/24` gagne → **B**.
- Destination `198.51.100.7` : seule la route par défaut s'applique → **A**.

La route par défaut `0.0.0.0/0` est le « préfixe de dernier recours » : sa longueur est 0, donc elle ne gagne que si rien de plus précis n'existe.

### 2.4 Demander au noyau quelle route il choisit

```bash
ip route get 203.0.113.10
```

👉 Explication : affiche la route réellement retenue pour cette destination (interface, adresse source, saut suivant). C'est le meilleur outil de lecture : il applique le préfixe le plus long à votre place, sans rien modifier.

## 3. Les routes statiques

### 3.1 Principe

Une route statique est une ligne que l'administrateur écrit lui-même : « pour atteindre `203.0.113.0/24`, passer par `198.51.100.2` ». Avantages : simple, sans trafic de contrôle, prévisible, idéale pour un réseau d'extrémité (un site qui n'a qu'une sortie). Limites : aucune adaptation aux pannes ; plus il y a de réseaux, plus la maintenance et le risque d'oubli augmentent.

### 3.2 Exemples de commandes

Sous Linux (lab ; effet immédiat mais non persistant au redémarrage) :

```bash
sudo ip route add 203.0.113.0/24 via 198.51.100.2
sudo ip route add default via 192.0.2.254
```

👉 Explication : ajoute une route vers le réseau `203.0.113.0/24` par le routeur `198.51.100.2`, puis une route par défaut. Le saut suivant doit être **atteignable directement** (dans un réseau connecté). La persistance dépend du gestionnaire réseau de la distribution (non traité ici).

Sur un équipement de type Cisco IOS (lab) :

```text
R1# configure terminal
R1(config)# ip route 203.0.113.0 255.255.255.0 198.51.100.2
R1(config)# ip route 0.0.0.0 0.0.0.0 198.51.100.2
R1(config)# end
R1# show ip route static
```

👉 Explication : les deux premières lignes créent une route statique et une route par défaut ; la dernière affiche les routes statiques. Seulement en laboratoire : une route par défaut erronée peut couper l'administration d'un équipement réel.

### 3.3 Aller et retour

Pour qu'une conversation fonctionne, **chaque saut doit connaître le chemin du retour**. Si R2 ne sait pas joindre `192.0.2.0/24`, le serveur reçoit la requête mais sa réponse s'arrête en route : l'expéditeur voit un simple délai d'attente. C'est l'erreur la plus fréquente avec les routes statiques.

### 3.4 Variantes utiles

- **Route flottante** : une route statique de secours avec une distance administrative plus élevée (par exemple 200) : elle n'entre dans la table que si la route principale disparaît.
- **Route vers un trou noir** (`blackhole` / `Null0`) : jette volontairement le trafic vers un préfixe ; utile pour empêcher des fuites.
- **Agrégation** : une seule route `192.0.2.0/24` plutôt que 256 routes `/32`.

## 4. Le routage dynamique

### 4.1 Pourquoi automatiser

Avec dix routeurs et vingt réseaux, maintenir des routes statiques devient fragile : un lien tombe, il faut modifier dix tables à la main. Un **protocole de routage dynamique** fait échanger aux routeurs la liste des réseaux qu'ils connaissent, calcule les meilleurs chemins et les corrige tout seul en cas de panne. Le temps nécessaire pour que tous les routeurs soient d'accord s'appelle la **convergence**.

### 4.2 Deux grandes catégories

- **IGP** (*Interior Gateway Protocol*) : à l'intérieur d'une même organisation (un **système autonome**, AS) : RIP, OSPF, EIGRP (protocole propre à un constructeur), IS-IS.
- **EGP** (*Exterior Gateway Protocol*) : entre organisations : aujourd'hui, **BGP**.

![Comparaison de RIP, OSPF et BGP : famille, métrique, usage](images/routage-ip-3.svg)

*Trois familles de protocoles de routage. Création originale du projet Pack Master, dédiée au domaine public (CC0).*

### 4.3 RIP : le plus simple

RIP (RIPv2, RFC 2453) est un protocole à **vecteur de distance** : chaque routeur annonce périodiquement (toutes les 30 secondes, en multicast `224.0.0.9`) sa table à ses voisins. La métrique est le **nombre de sauts** ; 16 signifie « inaccessible », donc le réseau est limité à 15 sauts. Analogie : le bouche-à-oreille — « je connais une route à 2 sauts, mon voisin à 3 », sans vision d'ensemble. Il est lent à converger et ne tient pas compte de la vitesse des liens ; on le rencontre surtout en enseignement ou sur de très petits réseaux.

### 4.4 OSPF : la carte partagée

OSPF (RFC 2328 pour OSPFv2 en IPv4) est un protocole à **état de liens**. Chaque routeur décrit ses liens dans des annonces (LSA), qui sont diffusées dans la **zone** ; tous les routeurs d'une zone obtiennent la même carte (base d'états de liens) et calculent eux-mêmes les plus courts chemins avec l'algorithme de **Dijkstra**. La métrique est un **coût** dépendant de la bande passante (coût = bande passante de référence / bande passante du lien). Analogie : chacun possède la même carte routière et calcule son itinéraire.

Points clés :

- les voisins se découvrent par des messages « Hello » (multicast `224.0.0.5`) et doivent s'accorder sur certains paramètres (zone, temporisateurs, authentification éventuelle) ;
- une **zone 0** (*backbone*) relie les autres zones : cela limite la taille de la base à recalculer ;
- sur un segment partagé, un **routeur désigné** (DR) est élu pour réduire les échanges ;
- la convergence est rapide (secondes) : OSPF est un standard des réseaux d'entreprise.

Exemple de laboratoire de type Cisco IOS (minimal) :

```text
R1(config)# router ospf 1
R1(config-router)# router-id 1.1.1.1
R1(config-router)# network 192.0.2.0 0.0.0.255 area 0
R1(config-router)# network 198.51.100.0 0.0.0.3 area 0
R1(config-router)# end
R1# show ip ospf neighbor
R1# show ip route ospf
```

👉 Explication : active OSPF (processus local numéroté 1), fixe l'identifiant du routeur et annonce deux réseaux dans la zone 0 (le masque inversé `0.0.0.255` correspond à `/24`) ; les deux `show` consultent les voisins et les routes apprises (codées `O`). Lab uniquement : un mauvais `network` peut annoncer, ou masquer, des réseaux réels.

### 4.5 BGP : le routage d'Internet

BGP (version 4, RFC 4271) relie les **systèmes autonomes**, identifiés par un numéro d'AS. Il fonctionne sur TCP (port 179) entre voisins configurés explicitement. Au lieu d'optimiser un coût, il choisit selon des **attributs** et des **politiques** (chemin d'AS le plus court, préférence locale, filtres commerciaux) : « je choisis ce chemin parce que mon contrat avec tel opérateur le prévoit », pas seulement parce qu'il est court. On distingue **eBGP** (entre AS différents) et **iBGP** (à l'intérieur d'un AS). Il converge prudemment et passe à l'échelle de centaines de milliers de préfixes ; une erreur de configuration chez un opérateur peut affecter beaucoup de monde, d'où l'usage strict des filtres. Une PME ne le rencontre généralement que si elle possède ses propres blocs d'adresses et plusieurs opérateurs.

### 4.6 Choisir

| Contexte | Choix usuel |
|---|---|
| un site, une sortie | route par défaut statique |
| quelques routeurs, peu de changements | routes statiques ou OSPF |
| réseau d'entreprise multi-sites | OSPF (ou protocole constructeur) |
| connexion à plusieurs opérateurs, adresses propres | BGP |

Quand plusieurs protocoles connaissent le même préfixe, c'est la **distance administrative** (ou priorité) qui tranche ; la métrique ne compare que des routes issues du **même** protocole.

## Mise en pratique guidée

Objectif : construire, dans une **VM Linux jetable**, la topologie du schéma avec des espaces de noms réseau (`pc1`, `r1`, `r2`, `srv`), observer l'échec, puis ajouter les routes. Tout reste dans la machine.

> **Avertissement** : ces commandes créent/suppriment des objets réseau avec des droits d'administration : à exécuter uniquement dans la VM de laboratoire. Elles n'ont pas été exécutées par l'auteur de ce texte. Le nettoyage est à l'étape 6.

### Étape 1 — Créer les quatre machines et les trois liens

```bash
for n in pc1 r1 r2 srv; do sudo ip netns add $n; sudo ip -n $n link set lo up; done
sudo ip link add eth0 netns pc1 type veth peer name eth0 netns r1
sudo ip link add eth1 netns r1 type veth peer name eth0 netns r2
sudo ip link add eth1 netns r2 type veth peer name eth0 netns srv
```

👉 Explication : crée quatre espaces de noms et trois câbles virtuels : `pc1`–`r1`, `r1`–`r2` et `r2`–`srv`. Chaque extrémité est directement placée dans son espace de noms.

### Étape 2 — Adresser les interfaces

```bash
sudo ip -n pc1 addr add 192.0.2.10/24 dev eth0
sudo ip -n r1  addr add 192.0.2.1/24 dev eth0
sudo ip -n r1  addr add 198.51.100.1/30 dev eth1
sudo ip -n r2  addr add 198.51.100.2/30 dev eth0
sudo ip -n r2  addr add 203.0.113.1/24 dev eth1
sudo ip -n srv addr add 203.0.113.10/24 dev eth0
for p in "pc1 eth0" "r1 eth0" "r1 eth1" "r2 eth0" "r2 eth1" "srv eth0"; do set -- $p; sudo ip -n $1 link set $2 up; done
```

👉 Explication : attribue les adresses du schéma (le lien routeur-routeur est un `/30`, qui n'offre que deux adresses utilisables) puis active chaque interface.

### Étape 3 — Activer le transfert sur les routeurs

```bash
sudo ip netns exec r1 sysctl -w net.ipv4.ip_forward=1
sudo ip netns exec r2 sysctl -w net.ipv4.ip_forward=1
```

👉 Explication : autorise `r1` et `r2` à retransmettre des paquets d'une interface à l'autre. Le réglage est propre à chaque espace de noms et ne touche pas le système hôte.

### Étape 4 — Constater l'échec, puis ajouter les routes pas à pas

```bash
sudo ip netns exec pc1 ping -c 1 -W 1 203.0.113.10
sudo ip -n pc1 route add default via 192.0.2.1
sudo ip -n srv route add default via 203.0.113.1
sudo ip netns exec pc1 ping -c 1 -W 1 203.0.113.10
```

👉 Explication : le premier ping échoue (« Network is unreachable » : `pc1` n'a pas de passerelle). Après les routes par défaut de `pc1` et de `srv`, le deuxième ping échoue encore : `r1` ne connaît pas `203.0.113.0/24` et renvoie une erreur ICMP « destination unreachable » ou le paquet est perdu. Chaque échec indique quelle pièce manque.

```bash
sudo ip -n r1 route add 203.0.113.0/24 via 198.51.100.2
sudo ip netns exec pc1 ping -c 1 -W 1 203.0.113.10
sudo ip -n r2 route add 192.0.2.0/24 via 198.51.100.1
sudo ip netns exec pc1 ping -c 2 203.0.113.10
```

👉 Explication : après la route aller sur `r1`, le ping échoue encore (le paquet arrive à `srv` mais `r2` ne sait pas renvoyer vers `192.0.2.0/24`). Après la route retour sur `r2`, le ping réussit. C'est la démonstration de la règle « aller **et** retour ».

### Étape 5 — Observer

```bash
sudo ip -n r1 route show
sudo ip -n pc1 route get 203.0.113.10
sudo ip netns exec pc1 traceroute -n 203.0.113.10
```

👉 Explication : affiche la table de `r1` (routes connectées + route statique), la route retenue par `pc1` (via `192.0.2.1`) et le chemin hop par hop : vous devez voir `192.0.2.1`, `198.51.100.2` puis `203.0.113.10`. Si `traceroute` n'est pas installé, `tracepath` en est une alternative. Lecture seule hormis l'émission des sondes dans la VM.

### Étape 6 — Nettoyage

```bash
for n in pc1 r1 r2 srv; do sudo ip netns del $n; done
ip netns list
```

👉 Explication : supprime les quatre espaces de noms (et leurs câbles virtuels) puis vérifie qu'il n'en reste aucun du laboratoire.

## Exercices

1. **(Facile)** Un hôte a l'adresse `192.0.2.10/24` et la passerelle `192.0.2.1`. Doit-il passer par la passerelle pour joindre `192.0.2.77` ? Et `198.51.100.5` ?
2. **(Facile)** Quelle est la fonction de la route `0.0.0.0/0` ?
3. **(Moyen)** Avec la table du 2.3 (`0.0.0.0/0` → A, `203.0.113.0/24` → B, `203.0.113.128/25` → C), donnez le saut suivant pour `203.0.113.127`, `203.0.113.128` et `192.0.2.9`.
4. **(Moyen)** `ping` vers un serveur distant reste sans réponse. `traceroute` s'arrête au routeur R2 et rien ne s'affiche après. Donnez deux hypothèses et l'outil qui départage.
5. **(Moyen)** Écrivez les commandes Linux de lab pour que R2 joigne le réseau `192.0.2.0/24` via R1, puis expliquez pourquoi le saut suivant doit être dans un réseau connecté.
6. **(Difficile)** Deux routes existent pour `203.0.113.0/24` : une statique (distance 1) et une OSPF (distance 110, coût 20). Laquelle est installée ? Comment prévoir un secours automatique ?
7. **(Difficile)** Un site a deux liaisons (principale et secours) vers le siège. Proposez une conception avec routes statiques, puis avec un protocole dynamique, et comparez.

## Corrigés des exercices

1. `192.0.2.77` est dans `192.0.2.0/24` : envoi direct (ARP). `198.51.100.5` n'y est pas : passage par la passerelle `192.0.2.1`.
2. C'est la route par défaut : elle s'applique à toute destination qui ne correspond à aucun préfixe plus précis, typiquement la sortie vers Internet.
3. `203.0.113.127` n'est pas dans `/25` (`.128` à `.255`) mais dans `/24` : **B**. `203.0.113.128` est dans `/25` : **C**. `192.0.2.9` : seule la route par défaut : **A**.
4. Hypothèses : R2 ne connaît pas la route vers le serveur (ou n'a pas de route par défaut) ; ou le trafic arrive mais la route retour manque ; ou un filtre (pare-feu, liste de contrôle d'accès) bloque. On départage avec `show ip route` / `ip route get` sur R2, un `traceroute` depuis l'autre côté, et la consultation des compteurs ou règles de filtrage.
5. `sudo ip route add 192.0.2.0/24 via 198.51.100.1` (sur R2). Le noyau doit pouvoir résoudre le saut suivant par ARP, donc l'adresse doit appartenir à un réseau directement connecté sur une interface ; sinon la route est refusée (« Nexthop has invalid gateway »).
6. La route **statique** (distance 1 < 110). Pour un secours, rendre la statique flottante (distance supérieure à 110, par exemple 200) : OSPF sert alors de principal et la statique ne s'installe que si OSPF disparaît.
7. Statique : une route principale (distance 1) et une route flottante via le lien de secours (distance 200), mais la bascule dépend de la disparition de la route (surveillance du lien, parfois insuffisante) ; simple, mais risque de panne silencieuse. Dynamique : OSPF détecte la panne et recalcule, avec un coût plus élevé sur le lien de secours ; plus de configuration et de supervision, mais plus robuste.

## Quiz

**Q1.** Que contient la passerelle par défaut d'un hôte ?
A. l'adresse IP du routeur local — B. l'adresse MAC du serveur DNS — C. le nom de domaine — D. le masque de sous-réseau

**Q2.** Quel élément reste inchangé de bout en bout (hors NAT) ?
A. l'adresse MAC de destination — B. l'adresse IP de destination — C. le TTL — D. la somme de contrôle de l'en-tête

**Q3.** Plusieurs routes couvrent une destination. Laquelle est choisie ?
A. la plus ancienne — B. celle au préfixe le plus long — C. celle au préfixe le plus court — D. la dernière ajoutée

**Q4.** `0.0.0.0/0` désigne…
A. le réseau local — B. la route par défaut — C. une adresse de diffusion — D. une erreur

**Q5.** Quelle est la métrique de RIP ?
A. la bande passante — B. le délai — C. le nombre de sauts — D. le coût administratif

**Q6.** OSPF est…
A. un EGP à vecteur de chemins — B. un IGP à état de liens — C. un IGP à vecteur de distance — D. un protocole de couche 2

**Q7.** BGP est principalement utilisé…
A. dans un LAN — B. entre systèmes autonomes — C. entre un poste et son DNS — D. pour attribuer des adresses

**Q8.** `ping` part mais aucune réponse ne revient, alors que la route aller est correcte. Hypothèse la plus probable ?
A. la route retour manque — B. le TTL est trop grand — C. le masque est en `/24` — D. ICMP n'existe pas

**Q9.** Une route flottante est…
A. une route sans interface — B. une route statique de secours à distance administrative plus élevée — C. une route apprise par BGP — D. une route multicast

**Q10.** Quelle commande Linux indique la route réellement utilisée pour une destination ?
A. `ip route get 203.0.113.10` — B. `ip addr show` — C. `hostname` — D. `arp -d`

### Réponses du quiz

1. **A** — la passerelle est l'adresse IP du routeur du sous-réseau. 2. **B** — l'IP de destination ne change pas ; les MAC sont réécrites, le TTL décrémenté, la somme de contrôle recalculée. 3. **B** — règle du préfixe le plus long. 4. **B** — préfixe de longueur 0, dernier recours. 5. **C** — nombre de sauts (15 max). 6. **B** — état de liens et Dijkstra. 7. **B** — AS différents. 8. **A** — l'asymétrie « aller sans retour » est l'erreur classique. 9. **B** — elle ne s'installe que si la route principale disparaît. 10. **A** — `ip route get` applique la sélection de route à votre place.

## Erreurs fréquentes et dépannage

| Symptôme | Cause probable | Vérification (lecture seule) |
|---|---|---|
| « Network is unreachable » | pas de route (ni par défaut) sur l'émetteur | `ip route show` / `Get-NetRoute` |
| Délai d'attente, `traceroute` muet après un saut | route retour absente ou filtre | `ip route get` sur chaque saut, règles de filtrage |
| Routage qui boucle (TTL expiré) | deux routeurs se renvoient le trafic (routes contradictoires) | `traceroute` : mêmes sauts alternés |
| Route absente après redémarrage | route ajoutée à chaud, non persistante | fichier de configuration réseau de la distribution |
| Voisin OSPF qui ne monte pas | zone, masque ou temporisateurs différents, filtrage multicast | `show ip ospf neighbor`, journaux |
| Accès perdu après un changement | route par défaut ou masque erroné sur l'interface de gestion | préparer un retour arrière et un accès console avant de modifier |

Méthode : décrire le chemin sur papier, vérifier à chaque saut la route aller **et** retour, tester du plus proche au plus lointain (passerelle, routeur suivant, destination), changer **une seule chose à la fois** et noter le résultat.

## À retenir

- L'hôte envoie en direct dans son sous-réseau, sinon à sa **passerelle** ; le routeur lit sa **table** et applique le **préfixe le plus long**.
- À chaque saut : MAC réécrites, TTL − 1, IP inchangées.
- **Route par défaut** `0.0.0.0/0` = dernier recours ; sans elle, destination inconnue = paquet abandonné.
- **Statique** : simple, prévisible, pas d'adaptation ; penser à la route **retour** et au secours (route flottante).
- **RIP** (sauts, 15 max), **OSPF** (état de liens, coût, zones), **BGP** (entre AS, politiques) ; la distance administrative départage les protocoles.
- Outils : `ip route`, `ip route get`, `ping`, `traceroute`. Les exemples de type Cisco IOS sont des exemples de lab, à valider avant toute production.

## Pour aller plus loin

- RFC 1812 — exigences pour les routeurs IPv4 : <https://www.rfc-editor.org/rfc/rfc1812>
- RFC 2453 — RIP version 2 : <https://www.rfc-editor.org/rfc/rfc2453>
- RFC 2328 — OSPF version 2 : <https://www.rfc-editor.org/rfc/rfc2328>
- RFC 4271 — BGP-4 : <https://www.rfc-editor.org/rfc/rfc4271>
- RFC 5737 — adresses IPv4 de documentation : <https://www.rfc-editor.org/rfc/rfc5737>
- Page de manuel `ip-route(8)` : <https://man7.org/linux/man-pages/man8/ip-route.8.html>
- Page de manuel `ip-netns(8)` : <https://man7.org/linux/man-pages/man8/ip-netns.8.html>

## Crédits des images

| Fichier | Source | Auteur | Licence | Modifications |
|---|---|---|---|---|
| `images/routage-ip-1.svg` | Création originale du projet Pack Master | Pack Master | CC0 — dédiée au domaine public (<https://creativecommons.org/publicdomain/zero/1.0/>) | — |
| `images/routage-ip-2.svg` | Création originale du projet Pack Master | Pack Master | CC0 (<https://creativecommons.org/publicdomain/zero/1.0/>) | — |
| `images/routage-ip-3.svg` | Création originale du projet Pack Master | Pack Master | CC0 (<https://creativecommons.org/publicdomain/zero/1.0/>) | — |

## Historique de vérification

| Date | OS/logiciel | Testeur | Verdict |
|---|---|---|---|
| 2026-11-01 | Linux (`iproute2`, `traceroute`), équipement de type Cisco IOS | Rédaction assistée (Copilot) | Non testé sur plateforme cible |

Précision : aucune commande de la leçon n'a été exécutée lors de la rédaction ; les sorties de `show ip route` sont illustratives.