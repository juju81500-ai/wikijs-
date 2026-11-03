---
title: "Leçon — DHCP : attribution d'adresses, baux, réservations, relais et pièges"
description: "À la fin de cette leçon, vous saurez :"
published: true
date: 2026-11-03T14:22:28Z
tags: ["transverse", "tout-en-un", "lecon", "reseaux", "dhcp", "dora", "bail", "relais", "diagnostic"]
editor: markdown
dateCreated: 2026-11-03T14:22:28Z
dateModified: 2026-11-03T14:22:28Z
---

# Leçon — DHCP : attribution d'adresses, baux, réservations, relais et pièges

- **Tags** : `transverse`, `tout-en-un`, `lecon`, `reseaux`, `dhcp`, `dora`, `bail`, `relais`, `diagnostic`
- **Niveau** : débutant à intermédiaire
- **Durée estimée** : 3 h (lecture 1 h 15, laboratoire 1 h, exercices et quiz 45 min)
- **Catégorie** : Tout-en-un / Réseaux et protocoles

---

## Objectifs pédagogiques

À la fin de cette leçon, vous saurez :

1. expliquer ce que distribue [[Glossary:DHCP]] (adresse, masque, passerelle, [[Glossary:DNS]], durée du bail) ;
2. décrire l'échange **DORA** (Discover, Offer, Request, Acknowledge) et ses ports [[Glossary:UDP]] 67 et 68 ;
3. calculer T1, T2 et l'expiration d'un bail, et choisir une durée adaptée ;
4. distinguer plage dynamique, réservation et adresse statique ;
5. expliquer le rôle d'un **relais DHCP** et du champ `giaddr` ;
6. reconnaître les pièges classiques : serveur pirate, plage épuisée, conflits, adresse 169.254.x.x, pare-feu ;
7. lire les informations de bail sous Linux et Windows, et conduire un laboratoire isolé.

## Prérequis et durée

- Connaître une adresse IPv4, un masque, une passerelle par défaut.
- Savoir utiliser un terminal Linux ou PowerShell.
- Pour le laboratoire : deux [[Glossary:VM]] jetables (un serveur, un client) reliées par un **réseau interne isolé**, sans autre serveur DHCP.
- Durée totale : environ 3 h.

Les adresses de l'exemple appartiennent aux blocs de documentation `192.0.2.0/24`, `198.51.100.0/24` et `203.0.113.0/24` ; les adresses MAC utilisent la plage de documentation `00:00:5e:00:53:xx`. Aucun secret ni donnée réelle.

## l'essentiel en bref

- DHCP donne automatiquement à un poste sa configuration réseau, **pour une durée limitée** (le bail).
- L'échange initial se fait en quatre messages : **D**iscover, **O**ffer, **R**equest, **A**cknowledge ; le client utilise l'UDP/68, le serveur l'UDP/67.
- À **50 % du bail (T1)** le client tente de renouveler auprès de son serveur ; à **87,5 % (T2)** il diffuse la demande ; à 100 % il perd l'adresse.
- Une **réservation** associe une adresse à un identifiant de client : l'adresse reste fixe tout en étant gérée centralement.
- Un **relais** transmet les diffusions d'un réseau vers un serveur situé ailleurs, en ajoutant l'adresse de son interface (`giaddr`).
- Pièges majeurs : deux serveurs concurrents, plage trop petite, UDP 67/68 filtrés, relais absent, adresse `169.254.x.x` sur le client.

---

## 1. Pourquoi DHCP

Configurer à la main l'adresse, le masque, la passerelle et les DNS de chaque poste est lent et source d'erreurs : doublons d'adresses, mauvaise passerelle, oubli du DNS. Le **DHCP** (Dynamic Host Configuration Protocol, RFC 2131 et 2132) automatise cela.

**Analogie** : l'accueil d'un hôtel. L'arrivant demande à voix haute une chambre ; la réception propose la 42 ; le client accepte ; la réception remet une carte valable pour la durée du séjour, avec le plan de l'hôtel (passerelle, DNS). Si le client prolonge avant la fin, la carte est renouvelée ; sinon la chambre retourne dans le stock.

Un serveur DHCP fournit, au minimum :

| Information | Option DHCP | Exemple |
|---|---|---|
| Adresse [[Glossary:IP]] | champ `yiaddr` | `192.0.2.100` |
| Masque | option 1 | `255.255.255.0` |
| Passerelle par défaut | option 3 | `192.0.2.1` |
| Serveurs DNS | option 6 | `192.0.2.53` |
| Domaine de recherche | option 15 | `example.test` |
| Durée du bail | option 51 | `7200` (secondes) |
| Serveurs de temps | option 42 | `192.0.2.123` |

## 2. L'échange DORA

Au démarrage, le client n'a **pas d'adresse** et ne connaît pas le serveur. Il doit donc parler en **diffusion** (broadcast) : source `0.0.0.0` port 68, destination `255.255.255.255` port 67.

![Diagramme de séquence DHCP : DISCOVER, OFFER, REQUEST, ACKNOWLEDGE entre un client et un serveur](images/dhcp-baux-et-relais-1.svg)

*Figure 1 — Les quatre messages de l'échange DHCP. Schéma de Gelmo96, licence CC BY-SA 4.0, étiquettes en anglais (« client » = client, « server » = serveur, « time » = temps, DISCOVER = découverte, OFFER = offre, REQUEST = demande, ACKNOWLEDGE = accusé de réception).*

1. **DISCOVER** (client → diffusion) : « Y a-t-il un serveur DHCP ? » Le message contient l'adresse MAC du client et, souvent, des options demandées (masque, passerelle, DNS).
2. **OFFER** (serveur → client) : « Je te propose `192.0.2.100` pour 2 heures, avec ces options. » Plusieurs serveurs peuvent répondre.
3. **REQUEST** (client → diffusion) : « J'accepte l'offre du serveur `192.0.2.1` pour `192.0.2.100`. » Il est diffusé pour que les **autres serveurs** sachent que leur offre est refusée ; l'option 54 (identifiant du serveur) désigne le serveur choisi.
4. **ACKNOWLEDGE** (serveur → client) : « Confirmé. » Le bail démarre. Le client vérifie en général par un test [[Glossary:ARP]] que l'adresse n'est pas déjà utilisée ; s'il détecte un conflit, il envoie **DECLINE** et recommence.

### 2.1 Les autres messages

| Message | Rôle |
|---|---|
| **NAK** | Le serveur refuse la demande (adresse inconnue, plage changée) : le client repart de DISCOVER. |
| **DECLINE** | Le client signale que l'adresse est déjà utilisée. |
| **RELEASE** | Le client rend son adresse (ex. `dhclient -r`, `ipconfig /release`). |
| **INFORM** | Le client, déjà configuré en statique, demande seulement des options (DNS, domaine). |

Le type de message est porté par l'option 53 ; on le lit dans une capture réseau.

### 2.2 Démarrage rapide : INIT-REBOOT

Un client qui redémarre envoie directement un **REQUEST** pour son ancienne adresse : ACK si le serveur est d'accord, sinon NAK et DORA complet.

### 2.3 Ports et diffusion

Le serveur écoute sur l'**UDP 67** ; le client utilise l'**UDP 68**. Un pare-feu qui bloque ces ports, ou un commutateur qui filtre la diffusion, empêche toute attribution.

## 3. Le bail et son cycle de vie

Une adresse DHCP est **prêtée**, jamais donnée. La durée du bail (option 51) détermine à quelle fréquence le client doit se manifester.

![Frise d'un bail de 8 heures : T1 à 4 h, T2 à 7 h, expiration à 8 h](images/dhcp-baux-et-relais-3.svg)

*Figure 2 — Un bail de 8 heures. T1 = 50 % (renouvellement en unicast), T2 = 87,5 % (renouvellement en diffusion), expiration à 100 %. Schéma original (CC0).*

- **T1 (50 %)** : le client envoie un REQUEST en **unicast** à son serveur d'origine. Un ACK relance le bail pour toute sa durée.
- **T2 (87,5 %)** : sans réponse, il diffuse la demande : n'importe quel serveur peut renouveler.
- **Expiration** : sans réponse, le client abandonne l'adresse et reprend un DISCOVER.

Ces valeurs par défaut peuvent être modifiées par les options 58 (T1) et 59 (T2).

### 3.1 Quelle durée choisir ?

| Contexte | Durée typique | Raison |
|---|---|---|
| Réseau d'entreprise stable (postes fixes) | 8 h à plusieurs jours | peu de rotation, peu de trafic de renouvellement |
| Wi-Fi invités, salles de formation | 30 min à 2 h | nombreux appareils de passage ; la plage doit se libérer vite |
| Laboratoire de test | 2 à 10 min | pour observer facilement renouvellement et expiration |

**Règle pratique** : un bail plus long que la présence habituelle d'un appareil, mais assez court pour libérer la plage. Une plage de 51 adresses avec des baux de 7 jours et une forte rotation d'appareils se remplit en quelques jours ; l'étendue épuisée est l'une des pannes les plus courantes.

## 4. Plages, exclusions et réservations

Un serveur DHCP gère une ou plusieurs **étendues** (scopes, ou pools). Pour `192.0.2.0/24`, une organisation découpe typiquement :

| Plage | Usage |
|---|---|
| `192.0.2.1` à `192.0.2.50` | équipements d'infrastructure en **statique** (routeur, serveurs, imprimantes) |
| `192.0.2.51` à `192.0.2.99` | **réservations** DHCP |
| `192.0.2.100` à `192.0.2.200` | plage **dynamique** |
| `192.0.2.201` à `192.0.2.254` | marge ou exclusions |

- **Exclusion** : adresses du pool que le serveur ne doit pas attribuer (parce qu'elles sont configurées en statique).
- **Réservation** : le serveur attribue **toujours la même adresse** à un client reconnu par son adresse MAC ou son identifiant de client. La machine reste en DHCP, mais son adresse est prévisible. C'est préférable à une configuration statique sur la machine, car le changement se fait au seul endroit central.
- **Statique** : adresse écrite sur la machine. Elle doit être **en dehors** de la plage dynamique, sinon le serveur risque de l'attribuer à un autre appareil (conflit).

Limite : un appareil qui **randomise sa MAC** (smartphones, Wi-Fi) apparaît comme un nouvel appareil, et la réservation par MAC ne s'applique plus.

## 5. Le relais DHCP

Les diffusions s'arrêtent aux frontières d'un réseau. Avec un serveur DHCP unique pour plusieurs sous-réseaux, un équipement du réseau du client doit **relayer** la requête : le routeur (ou le commutateur de niveau 3) joue le rôle d'**agent de relais** (relay agent).

![Un client d'un réseau 198.51.100.0/24 diffuse un DISCOVER ; le routeur relais 198.51.100.1 le transmet en unicast avec giaddr au serveur 192.0.2.67](images/dhcp-baux-et-relais-2.svg)

*Figure 3 — Le routeur relais transforme la diffusion en unicast et ajoute son adresse (`giaddr`) ; le serveur choisit la plage correspondante. Schéma original (CC0).*

1. Le client diffuse son DISCOVER sur son réseau `198.51.100.0/24`.
2. Le relais (interface `198.51.100.1`) reçoit la diffusion, la transforme en **unicast** vers `192.0.2.67`, et inscrit `giaddr = 198.51.100.1` (Gateway IP Address).
3. Le serveur lit `giaddr`, en déduit le sous-réseau du client, choisit une adresse dans l'étendue `198.51.100.0/24` et répond **au relais** ; celui-ci retransmet au client.
4. REQUEST et ACK suivent le même chemin.

Sans `giaddr`, le serveur ne peut pas savoir pour quel sous-réseau choisir une adresse. Il faut donc **une étendue par sous-réseau relayé**, dont l'adresse de passerelle correspond au `giaddr`.

**Où configurer le relais** : sur l'interface du routeur tournée vers les clients (« DHCP relay » ou « IP helper »), avec l'adresse du serveur comme cible. Sous Linux, `dhcrelay` remplit cette fonction.

## 6. Redondance

Un serveur unique est un point de défaillance. On peut **séparer la plage** entre deux serveurs (80/20 ou 50/50), ou utiliser un **basculement synchronisé** (failover natif de Windows Server, haute disponibilité de Kea) où les serveurs partagent l'état des baux. Dans tous les cas, **deux serveurs non coordonnés qui servent la même plage** créent des conflits d'adresses.

## 7. Lire un bail côté client

### Linux

```bash
ip -br addr
ip route
resolvectl status
```

👉 Explication : affiche en lecture seule les adresses des interfaces, la table de routage (la route par défaut vient de l'option 3) et les DNS reçus (option 6). Si `resolvectl` est absent, lire `/etc/resolv.conf`.

```bash
nmcli -f DHCP4 device show enp0s3
```

👉 Explication : avec NetworkManager, liste les options reçues du serveur (adresse, bail, routeur, DNS). Remplacez `enp0s3` par le nom de l'interface réelle (`ip -br link`).

### Windows

```powershell
ipconfig /all
Get-NetIPConfiguration
```

👉 Explication : `ipconfig /all` affiche « DHCP activé », le serveur DHCP, les dates d'obtention et d'expiration du bail. `Get-NetIPConfiguration` donne l'adresse, la passerelle et les DNS par interface. Lecture seule.

```powershell
Get-NetIPInterface | Select-Object InterfaceAlias, AddressFamily, Dhcp
```

👉 Explication : indique pour chaque interface si DHCP est activé (`Enabled`) ou non, ce qui distingue une adresse statique d'une adresse obtenue par bail.

## Mise en pratique guidée

**Cadre** : deux VM jetables sur un **réseau interne isolé** (réseau interne de VirtualBox, réseau hôte uniquement de VMware, réseau privé de libvirt) **dont le serveur DHCP intégré est désactivé**. Ne jamais lancer ce laboratoire sur un réseau partagé : un second serveur DHCP perturberait les autres machines. Prenez un instantané des deux VM.

- **VM « serveur »** : Debian ou Ubuntu, interface `enp0s8` sur le réseau interne.
- **VM « client »** : Debian ou Ubuntu, interface `enp0s8` sur le même réseau interne.

Adaptez le nom d'interface à votre environnement (`ip -br link`).

### Étape 1 — Adresse statique du serveur (VM serveur)

```bash
sudo ip addr add 192.0.2.1/24 dev enp0s8
sudo ip link set enp0s8 up
ip -br addr show enp0s8
```

👉 Explication : donne temporairement l'adresse `192.0.2.1/24` à l'interface du réseau interne (perdue au redémarrage) et l'active. La dernière commande vérifie le résultat.

### Étape 2 — Installer et configurer le serveur

```bash
sudo apt update && sudo apt install -y dnsmasq tcpdump
mkdir -p ~/lab-dhcp && cd ~/lab-dhcp
cat > lab-dhcp.conf <<'EOF'
port=0
interface=enp0s8
bind-interfaces
dhcp-range=192.0.2.100,192.0.2.150,255.255.255.0,5m
dhcp-option=option:router,192.0.2.1
dhcp-option=option:dns-server,192.0.2.53
dhcp-option=option:domain-search,example.test
dhcp-leasefile=/var/lib/misc/lab-dhcp.leases
log-dhcp
EOF
```

👉 Explication : installe `dnsmasq` et `tcpdump` dans la VM jetable, puis écrit une configuration qui désactive la partie DNS (`port=0`), ne sert que l'interface du laboratoire, attribue `192.0.2.100` à `192.0.2.150` avec un bail de **5 minutes** (pour observer facilement le renouvellement) et annonce passerelle, DNS et domaine.

### Étape 3 — Lancer le serveur

```bash
sudo dnsmasq --conf-file=lab-dhcp.conf --keep-in-foreground --log-facility=- --pid-file=
```

👉 Explication : démarre `dnsmasq` au premier plan et affiche chaque échange DHCP. Laissez ce terminal ouvert. Si le service système `dnsmasq` est actif, arrêtez-le d'abord avec `sudo systemctl stop dnsmasq` pour libérer le port 67 (dans la VM jetable uniquement).

### Étape 4 — Capturer l'échange (VM serveur, second terminal)

```bash
sudo tcpdump -ni enp0s8 -vv 'udp port 67 or udp port 68'
```

👉 Explication : écoute uniquement le trafic DHCP sur l'interface du laboratoire. Laissez la capture tourner pendant l'étape suivante. La lecture d'une capture est détaillée dans [la leçon sur les ports, les protocoles et les captures](/fr/00-cours-theoriques/tout-en-un/01-reseaux-et-protocoles/lecons/lecon-ports-protocoles-et-captures).

### Étape 5 — Obtenir un bail (VM client)

```bash
sudo apt update && sudo apt install -y isc-dhcp-client
sudo dhclient -v enp0s8
```

👉 Explication : installe un client DHCP en ligne de commande et lance une demande sur l'interface du laboratoire. L'option `-v` affiche les quatre messages DORA : `DHCPDISCOVER`, `DHCPOFFER`, `DHCPREQUEST`, `DHCPACK`, puis « bound to 192.0.2.1xx ». Si le client utilise déjà NetworkManager, utilisez plutôt `sudo nmcli device connect enp0s8`.

```bash
ip -br addr show enp0s8
ip route
cat /var/lib/dhcp/dhclient.leases
```

👉 Explication : vérifie l'adresse reçue (entre `.100` et `.150`), la route par défaut vers `192.0.2.1` et le détail du bail (options, dates de renouvellement et d'expiration). Dans la capture, repérez les quatre messages et le champ `Option 53`.

### Étape 6 — Observer le renouvellement

Attendez environ **2 min 30** (50 % d'un bail de 5 minutes) en surveillant le terminal de capture : vous devez voir un REQUEST **unicast** de `192.0.2.1xx` vers `192.0.2.1`, suivi d'un ACK. Si votre client ne renouvelle pas (client géré par un autre outil), relancez `dhclient -v` et observez la sortie.

### Étape 7 — Ajouter une réservation (VM serveur)

Arrêtez `dnsmasq` (`Ctrl+C`). Relevez l'adresse MAC du client avec `ip -br link show enp0s8` (VM client). Ajoutez, à la fin de `lab-dhcp.conf`, une ligne de la forme (adresse MAC fictive à remplacer par la vraie) :

```bash
echo 'dhcp-host=00:00:5e:00:53:01,192.0.2.60' >> lab-dhcp.conf
```

👉 Explication : associe l'adresse MAC indiquée à `192.0.2.60`, hors de la plage dynamique. Remplacez `00:00:5e:00:53:01` par l'adresse MAC réelle de la VM cliente, relevée à l'étape précédente. Relancez ensuite `dnsmasq` comme à l'étape 3.

Sur la VM client :

```bash
sudo dhclient -r enp0s8
sudo dhclient -v enp0s8
ip -br addr show enp0s8
```

👉 Explication : `-r` libère le bail (message RELEASE), puis une nouvelle demande doit recevoir `192.0.2.60`, adresse réservée.

### Étape 8 — Provoquer l'échec : sans serveur

Arrêtez `dnsmasq`, puis sur le client :

```bash
sudo dhclient -v enp0s8
```

👉 Explication : sans serveur, `dhclient` répète des DISCOVER (« No DHCPOFFERS received ») et finit par abandonner. Une machine Windows afficherait alors une adresse **169.254.x.x** (APIPA). Rétablissez ensuite le serveur.

### Étape 9 — Nettoyer

```bash
sudo dhclient -r enp0s8
cd ~ && rm -r ~/lab-dhcp
```

👉 Explication : libère le bail côté client puis supprime le dossier du laboratoire côté serveur. Restaurez les instantanés des deux VM pour retrouver l'état initial.

## Exercices

1. **Vocabulaire.** Associez : (a) message du client qui accepte une offre ; (b) message du serveur qui refuse ; (c) message du client qui rend son adresse ; (d) champ renseigné par le relais.
2. **Calcul.** Un bail dure 24 h. Donnez T1 et T2 en heures et minutes.
3. **Dimensionnement.** Une plage dynamique va de `192.0.2.100` à `192.0.2.200`. Combien d'adresses contient-elle ? Pour 120 appareils par jour (certains ne revenant jamais), quel risque et quelle contre-mesure ?
4. **Lecture de journal.** Le journal du serveur montre : `DHCPDISCOVER(enp0s8) 00:00:5e:00:53:07`, `DHCPOFFER(enp0s8) 192.0.2.103`, `DHCPREQUEST(enp0s8) 192.0.2.103`, `DHCPACK(enp0s8) 192.0.2.103`. Décrivez l'échange et dites si un relais est en jeu.
5. **Relais.** Le sous-réseau `203.0.113.0/24` est servi par le serveur `192.0.2.67` via le routeur `203.0.113.1`. Quelles sont les deux informations à configurer sur le routeur et la configuration à créer sur le serveur ?
6. **Réservation ou statique ?** Un serveur d'impression doit toujours avoir `192.0.2.55`. Comparez les deux approches et recommandez-en une.
7. **Diagnostic.** Un poste Windows affiche `169.254.37.12` au démarrage, alors que ses voisins reçoivent une adresse. Listez quatre causes possibles, en suivant le chemin du paquet.
8. **Sécurité.** Quelle protection du commutateur évite qu'un équipement non autorisé branché sur une prise distribue des adresses ?

## Corrigés des exercices

1. (a) REQUEST ; (b) NAK ; (c) RELEASE ; (d) `giaddr`.
2. T1 = 12 h 00 ; T2 = 21 h 00 (87,5 % de 24 h) ; expiration à 24 h.
3. De `.100` à `.200` : **101 adresses**. Si les appareils de passage ne reviennent pas et que le bail est long (plusieurs jours), la plage s'épuise. Contre-mesures : raccourcir le bail, agrandir la plage ou ajouter un sous-réseau, supprimer les appareils fantômes.
4. Échange DORA complet sur le même segment pour le client dont la MAC se termine par `:07`, qui reçoit `192.0.2.103`. Rien n'indique de relais ici (le journal d'un serveur avec relais mentionnerait l'adresse du relais, `via 198.51.100.1` par exemple).
5. Sur le routeur : interface côté clients `203.0.113.1` avec comme cible de relais `192.0.2.67`. Sur le serveur : une étendue `203.0.113.0/24` (plage, passerelle `203.0.113.1`, DNS) dont l'adresse de sous-réseau correspond au `giaddr`. Vérifier aussi que le routeur et le pare-feu laissent passer l'UDP 67 en unicast vers le serveur.
6. Réservation : l'adresse est gérée au serveur, la machine reste en DHCP et reçoit aussi DNS et passerelle automatiquement ; l'adresse est tout de même fixe. Statique : indépendant du serveur DHCP (utile pour les composants dont dépend DHCP lui-même) mais change à plusieurs endroits et peut provoquer des conflits. Recommandation : réservation, sauf pour les équipements dont dépend DHCP.
7. (a) Câble ou port inactif (couche 2) ; (b) le serveur DHCP est arrêté ou plage épuisée ; (c) pas de relais pour ce [[Glossary:VLAN]] ; (d) filtrage UDP 67/68 ou DHCP snooping qui bloque la réponse. Après un `ipconfig /renew`, un échec persistant relève du serveur, du relais ou du filtrage.
8. Le **DHCP snooping** : le commutateur n'accepte les réponses de serveur que depuis des ports « de confiance ».

## Quiz

**Q1. Quel est l'ordre normal d'un échange initial ?**
A) Offer, Discover, Request, Ack. B) Discover, Offer, Request, Acknowledge. C) Request, Offer, Discover, Ack. D) Discover, Request, Offer, Ack.
**Réponse : B.** Le client cherche, le serveur propose, le client accepte, le serveur confirme.

**Q2. Quels ports UDP DHCPv4 utilise-t-il ?**
A) 53 et 54. B) 67 (serveur) et 68 (client). C) 80 et 443. D) 123 et 161.
**Réponse : B.** Le serveur écoute sur 67 et le client utilise 68.

**Q3. Pourquoi le DISCOVER est-il diffusé ?**
A) Pour économiser la bande passante. B) Le client n'a pas d'adresse et ne connaît pas le serveur. C) Les serveurs DHCP n'acceptent que la diffusion. D) Par sécurité.
**Réponse : B.** Sans adresse ni serveur connu, la diffusion est le seul moyen de joindre un serveur.

**Q4. À quel moment le client tente-t-il un premier renouvellement par défaut ?**
A) À 12,5 %. B) À 50 % du bail. C) À 87,5 %. D) À 100 %.
**Réponse : B.** T1 = 50 % (unicast) ; T2 = 87,5 % (diffusion).

**Q5. Que fait un relais DHCP ?**
A) Il remplace le serveur DHCP. B) Il transmet les requêtes de diffusion vers un serveur d'un autre réseau en ajoutant `giaddr`. C) Il filtre les adresses MAC. D) Il attribue lui-même les adresses.
**Réponse : B.** Il convertit la diffusion en unicast et précise le sous-réseau du client.

**Q6. Une adresse en `169.254.x.x` sur un poste Windows signifie :**
A) Un bail DHCP valide. B) Aucun serveur DHCP n'a répondu (adresse APIPA). C) Une réservation. D) Une adresse publique.
**Réponse : B.** L'auto-adressage lien-local prend le relais quand le DHCP échoue.

**Q7. Quelle réservation DHCP identifie le plus souvent un client ?**
A) Son adresse MAC (ou identifiant client). B) Son nom d'utilisateur. C) Son système d'exploitation. D) Son adresse IP publique.
**Réponse : A.** Un appareil à MAC aléatoire peut faire échouer cette correspondance.

**Q8. Une adresse statique placée dans la plage dynamique provoque :**
A) Rien. B) Un risque de conflit : le serveur peut l'attribuer à un autre appareil. C) Un renouvellement plus rapide. D) Un changement de masque.
**Réponse : B.** Les adresses statiques doivent être hors plage ou exclues du pool.

**Q9. Quelle fonction du commutateur limite les serveurs DHCP pirates ?**
A) Spanning tree. B) DHCP snooping. C) Port mirroring. D) PoE.
**Réponse : B.** Il n'autorise les réponses DHCP que sur les ports de confiance.

**Q10. Pourquoi une plage de 51 adresses s'épuise-t-elle avec des baux de 7 jours et beaucoup d'appareils de passage ?**
A) Les adresses sont perdues définitivement. B) Un bail non rendu reste occupé jusqu'à son expiration. C) Le serveur manque de mémoire. D) Les baux ne sont pas renouvelables.
**Réponse : B.** Un appareil qui part sans RELEASE garde son bail occupé jusqu'au bout.

## Erreurs fréquentes et dépannage

| Symptôme | Cause probable | Vérification |
|---|---|---|
| Adresse `169.254.x.x` | Aucun DHCP joignable, relais absent, UDP 67/68 filtrés | Câble et VLAN ; capture `tcpdump -ni IF 'udp port 67 or udp port 68'` ; journal du serveur |
| Mauvaise passerelle ou mauvais DNS | Serveur pirate ou second serveur concurrent | `ipconfig /all` (champ « Serveur DHCP ») ; DHCP snooping |
| Plage épuisée | Baux longs, forte rotation | Statistiques de l'étendue ; raccourcir le bail ou agrandir |
| Conflits d'adresses | Statique dans la plage dynamique | Exclusions ; inventaire des adresses statiques |
| Réservation ignorée | MAC modifiée ou aléatoire, faute de frappe, identifiant de client différent | Comparer la MAC vue par le serveur et celle de la réservation |
| Un sous-réseau ne reçoit rien | Relais absent ou sans étendue correspondante au `giaddr` | Configuration de l'interface du routeur ; étendue sur le serveur |
| Clones de VM avec la même adresse | Identifiant de client dupliqué | Régénérer l'identifiant (machine-id, DUID) |
| Après changement de plage, clients en erreur | Anciens baux incompatibles (NAK) | Redémarrer le client ou libérer puis renouveler le bail |

**Méthode** : (1) vérifier la couche 2 (lien, VLAN) ; (2) capturer sur le client ou le serveur pour voir quels messages passent ; (3) lire le journal du serveur (étendues, plage libre) ; (4) si un relais est impliqué, contrôler `giaddr` et l'étendue ; (5) chercher un second serveur.

```powershell
ipconfig /renew
```

👉 Explication : demande un renouvellement du bail sous Windows. Cette commande modifie l'état réseau du poste : à utiliser sur un poste de test ou avec l'accord de l'exploitant. Son équivalent de lecture seule est `ipconfig /all`.

Remarque IPv6 : DHCPv6 (UDP 546 et 547) existe, à côté de l'auto-configuration SLAAC ; bail et relais restent proches.

## À retenir

- DHCP attribue un bail : adresse, masque, passerelle, DNS, durée.
- DORA : Discover (diffusion), Offer, Request, Acknowledge ; UDP 68 côté client, 67 côté serveur.
- T1 = 50 % (unicast au serveur), T2 = 87,5 % (diffusion), expiration à 100 %.
- Statique hors de la plage dynamique ; réservation pour les adresses fixes gérées centralement.
- Un relais convertit la diffusion en unicast et renseigne `giaddr` ; une étendue par sous-réseau relayé.
- Un seul serveur autorisé par plage ; DHCP snooping contre les serveurs pirates.
- `169.254.x.x` = échec DHCP côté client ; commencez par couche 2, puis capture.
- Laboratoire : toujours sur un réseau isolé, avec instantané.

## Pour aller plus loin

- RFC 2131 — Dynamic Host Configuration Protocol : https://www.rfc-editor.org/rfc/rfc2131
- RFC 2132 — DHCP Options and BOOTP Vendor Extensions : https://www.rfc-editor.org/rfc/rfc2132
- RFC 3046 — DHCP Relay Agent Information Option : https://www.rfc-editor.org/rfc/rfc3046
- RFC 8415 — DHCPv6 : https://www.rfc-editor.org/rfc/rfc8415
- RFC 5737 — adresses de documentation : https://www.rfc-editor.org/rfc/rfc5737
- Documentation de Kea (ISC) : https://kea.readthedocs.io/
- Serveur DHCP sous Windows Server (Microsoft Learn) : https://learn.microsoft.com/windows-server/networking/technologies/dhcp/dhcp-top
- Leçon associée : [Ports, protocoles courants et lecture d'une capture](/fr/00-cours-theoriques/tout-en-un/01-reseaux-et-protocoles/lecons/lecon-ports-protocoles-et-captures)

## Crédits des images

| Fichier | Source | Auteur | Licence | Modifications |
|---|---|---|---|---|
| `images/dhcp-baux-et-relais-1.svg` | https://commons.wikimedia.org/wiki/File:DHCP_session.svg | Gelmo96 (travail personnel) | CC BY-SA 4.0 : https://creativecommons.org/licenses/by-sa/4.0/ | Aucune (fichier renommé) ; l'image reste sous CC BY-SA 4.0 |
| `images/dhcp-baux-et-relais-2.svg` | Création originale du projet Pack Master | Projet Pack Master | Création originale du projet Pack Master, dédiée au domaine public (CC0) : https://creativecommons.org/publicdomain/zero/1.0/ | Sans objet |
| `images/dhcp-baux-et-relais-3.svg` | Création originale du projet Pack Master | Projet Pack Master | Création originale du projet Pack Master, dédiée au domaine public (CC0) : https://creativecommons.org/publicdomain/zero/1.0/ | Sans objet |

## Historique de vérification

| Date | OS/logiciel | Testeur | Verdict |
|---|---|---|---|
| 2026-11-01 | Linux (dnsmasq, dhclient, tcpdump), Windows (ipconfig, PowerShell) | Rédaction assistée (Copilot) | Non testé sur plateforme cible |

Précision : à la rédaction, aucune commande de cette leçon n'a été exécutée (`dnsmasq`, `dhclient` et `tcpdump` n'étaient pas installés sur le poste de rédaction, et le laboratoire DHCP exige un réseau isolé). Les extraits de journal sont des exemples typiques. La licence de l'image 1 a été relevée sur Wikimedia Commons le 2026-11-01.