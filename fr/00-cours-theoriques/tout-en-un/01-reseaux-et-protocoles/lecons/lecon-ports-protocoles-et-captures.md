---
title: "Leçon — Ports et protocoles courants, HTTP/HTTPS/TLS vus du réseau et lecture d'une capture"
description: "À la fin de cette leçon, vous saurez :"
published: true
date: 2026-11-03T14:22:28Z
tags: ["transverse", "tout-en-un", "lecon", "reseaux", "ports", "tcp", "http", "tls", "wireshark", "tcpdump", "capture"]
editor: markdown
dateCreated: 2026-11-03T14:22:28Z
dateModified: 2026-11-03T14:22:28Z
---

# Leçon — Ports et protocoles courants, HTTP/HTTPS/TLS vus du réseau et lecture d'une capture

- **Tags** : `transverse`, `tout-en-un`, `lecon`, `reseaux`, `ports`, `tcp`, `http`, `tls`, `wireshark`, `tcpdump`, `capture`
- **Niveau** : intermédiaire
- **Durée estimée** : 3 h 30 (lecture 1 h 30, laboratoire 1 h 15, exercices et quiz 45 min)
- **Catégorie** : Tout-en-un / Réseaux et protocoles

---

## Objectifs pédagogiques

À la fin de cette leçon, vous saurez :

1. expliquer le port et le quintuplet d'une connexion ;
2. citer les ports et protocoles courants et dire s'ils sont chiffrés ;
3. décrire la poignée de main [[Glossary:TCP]], la fermeture et les états vus avec `ss` ;
4. dire ce qui est lisible ou non en [[Glossary:HTTP]] et en HTTPS ;
5. situer la négociation [[Glossary:TLS]], le SNI et le certificat ;
6. lire une capture (poignée de main TCP, requête [[Glossary:DNS]], requête HTTP) avec `tcpdump` et Wireshark ;
7. reconnaître trois signatures de panne : SYN sans réponse, RST, retransmissions.

## Prérequis et durée

- Connaître le modèle en couches ([[Glossary:IP]], transport, application) et une adresse IPv4.
- Savoir ouvrir deux terminaux Linux ; connaître les bases de `curl`.
- Laboratoire : une [[Glossary:VM]] Linux jetable ; captures **uniquement sur l'interface locale `lo`**.
- Durée totale : environ 3 h 30.

Les adresses d'exemple appartiennent aux blocs de documentation (`192.0.2.0/24`, `198.51.100.0/24`, `203.0.113.0/24`, `2001:db8::/32`) et les noms à `example.com` ou `example.test`. Les extraits de capture sont **fictifs**.

## l'essentiel en bref

- Une connexion est identifiée par **cinq éléments** : protocole, IP source, port source, IP destination, port destination.
- Le **port** désigne le service sur une machine. Le serveur écoute sur un port connu (80, 443, 53…) ; le client prend un port **éphémère**.
- **TCP** est fiable et orienté connexion (SYN, SYN-ACK, ACK) ; **[[Glossary:UDP]]** envoie sans connexion (DNS, [[Glossary:DHCP]], [[Glossary:NTP]]).
- **HTTP** est lisible en clair ; **HTTPS** = HTTP dans **TLS** : seuls adresses, ports, volumes et (souvent) le nom du site restent visibles.
- Dans une capture, les **drapeaux** TCP racontent l'histoire : `[S]` ouverture, `[S.]` réponse, `[.]` accusé, `[P.]` données, `[F.]` fermeture, `[R]` rupture.
- Filtrer avant de lire : on ne lit jamais toute une capture, on isole une conversation.

---

## 1. Les ports : numéroter les services

Une adresse IP désigne une **machine**. Elle ne dit pas quel programme doit recevoir le paquet. Le **port** (16 bits, de 0 à 65535) désigne le programme.

**Analogie** : l'IP est l'adresse de l'immeuble, le port le numéro de l'appartement.

| Plage | Nom | Usage |
|---|---|---|
| 0 à 1023 | ports « bien connus » (system) | services standards : 22, 53, 80, 443… |
| 1024 à 49151 | ports enregistrés (user) | applications : 3306, 5432, 8080… |
| 49152 à 65535 | ports dynamiques ou **éphémères** | choisis par le client pour une connexion |

Linux utilise par défaut 32768–60999 comme plage éphémère.

### 1.1 Le quintuplet d'une connexion

Une connexion web est identifiée par :

```text
TCP  198.51.100.20:50422  →  203.0.113.10:443
```

Plusieurs connexions simultanées vers le même serveur utilisent des ports sources différents (50422, 50423…) : c'est ce quintuplet qui permet de répartir les paquets.

### 1.2 TCP et UDP

| | TCP | UDP |
|---|---|---|
| Connexion | oui (poignée de main) | non |
| Fiabilité | accusés de réception, retransmissions, ordre | aucune garantie |
| Exemples | HTTP, HTTPS, [[Glossary:SSH]], [[Glossary:SMTP]] | DNS (petites requêtes), DHCP, NTP, QUIC |

Le DNS illustre le choix : une question et une réponse tiennent chacune dans un datagramme UDP. Un même numéro de port existe séparément en TCP et en UDP.

## 2. Les ports et protocoles à connaître

| Port | Protocole | Transport | Rôle | Chiffré ? |
|---|---|---|---|---|
| 20/21 | [[Glossary:FTP]] | TCP | transfert de fichiers (21 commande, 20 données actives) | non |
| 22 | SSH | TCP | administration à distance, SFTP | oui |
| 23 | Telnet | TCP | terminal à distance (obsolète) | non |
| 25 | SMTP | TCP | transfert de courrier entre serveurs | optionnel ([[Glossary:STARTTLS]]) |
| 53 | DNS | UDP et TCP | résolution de noms | non (sauf DoT/DoH) |
| 67/68 | DHCP | UDP | attribution d'adresses (serveur/client) | non |
| 80 | HTTP | TCP | web en clair | non |
| 123 | NTP | UDP | synchronisation de l'heure | non |
| 143 / 993 | [[Glossary:IMAP]] / IMAPS | TCP | courrier consulté sur le serveur | non / oui |
| 443 | HTTPS | TCP (et UDP pour HTTP/3) | web chiffré | oui |
| 445 | SMB | TCP | partage de fichiers Windows | selon la configuration |
| 3389 | [[Glossary:RDP]] | TCP | bureau à distance Windows | oui |

Le registre officiel est tenu par l'IANA ; `/etc/services` (voir `getent services nom`) en donne une copie. Un numéro de port **n'est qu'une convention** : un service web peut écouter sur 8080, un SSH sur 2222.

**Réflexe de sécurité** : un protocole « en clair » (21, 23, 80, 143) expose identifiants et contenu à qui observe le réseau ; préférez sa variante chiffrée.

## 3. TCP vu du réseau

### 3.1 La poignée de main en trois temps

Avant d'échanger des données, un client TCP doit établir la connexion avec trois segments.

![Diagramme de séquence : le client envoie SYN, le serveur répond SYN-ACK, le client confirme ACK, puis une requête HTTP GET et la réponse, et enfin la fermeture FIN](images/ports-protocoles-captures-1.svg)

*Figure 1 — Poignée de main TCP, requête HTTP, réponse et fermeture, avec numéros de séquence relatifs. Schéma original (CC0).*

1. **SYN** : le client propose de se connecter et annonce son numéro de séquence initial.
2. **SYN-ACK** : le serveur accepte, annonce le sien et confirme celui du client.
3. **ACK** : le client confirme ; la connexion est **établie**.

Une connexion TCP coûte un **aller-retour** (RTT) avant la première donnée.

![Diagramme montrant un client et un serveur : demande de connexion à 0 ms, connexion confirmée à 34 ms, premières données de l'application à 68 ms](images/ports-protocoles-captures-4.svg)

*Figure 2 — Latence de la poignée de main : les données applicatives ne partent qu'après un aller-retour complet. Schéma de Fleshgrinder et du projet Tango Desktop, domaine public ; étiquettes en anglais (« Client » = client ; « Server » = serveur ; « Connection Request » = demande de connexion ; « Connection Acknowledged » = connexion confirmée ; « Application Data » = données applicatives ; « Time » = temps).*

### 3.2 Numéros de séquence et accusés

Chaque octet est numéroté. Un segment porte `seq` (premier octet transporté) et `ack` (prochain octet attendu). Wireshark et `tcpdump` affichent des numéros **relatifs**. Sans accusé, l'émetteur **retransmet**.

### 3.3 Fermeture et rupture

- **FIN** : fermeture ordonnée, sens par sens.
- **RST** : rupture brutale, par exemple quand personne n'écoute sur le port (« connexion refusée ») ou quand un pare-feu coupe la session.

### 3.4 Les états vus par `ss`

`LISTEN` : un service attend sur ce port. `ESTABLISHED` : connexion ouverte. `TIME-WAIT` : connexion fermée, quintuplet bloqué un moment. `SYN-SENT` : SYN envoyé, réponse attendue.

Des `SYN-SENT` qui s'éternisent indiquent un pare-feu qui **abandonne** (drop) ; un RST immédiat indique un port **fermé** ou un rejet explicite.

## 4. HTTP vu du réseau

HTTP est un protocole **texte** de type requête-réponse (RFC 9110 pour la sémantique). Sur le réseau, en clair, voici une requête et sa réponse :

```text
GET /index.html HTTP/1.1
Host: www.example.com
User-Agent: curl/8.5.0
Accept: */*

HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 1256
Server: exemple-serveur

<html>…
```

- La **ligne de requête** contient la méthode (GET, POST, PUT, DELETE, HEAD), le chemin et la version.
- L'en-tête **Host** permet d'héberger plusieurs sites derrière une même adresse IP.
- Le **code** de la réponse : 2xx succès, 3xx redirection (souvent HTTP vers HTTPS), 4xx erreur du client (403 interdit, 404 introuvable), 5xx erreur du serveur ou du proxy en amont (500, 502, 503).

**Versions.** HTTP/2 est **binaire** (plusieurs requêtes par connexion) et presque toujours sur TLS. HTTP/3 utilise **QUIC sur UDP/443** : du trafic UDP 443 est du web.

**Analogie** : HTTP en clair est une carte postale ; HTTPS est une lettre scellée : on voit l'adresse et le poids, pas le contenu.

## 5. HTTPS et TLS vus du réseau

**HTTPS**, c'est HTTP transporté à l'intérieur de **TLS** (Transport Layer Security, TLS 1.3 décrit par la RFC 8446). TLS apporte : **confidentialité** (chiffrement), **intégrité** (détection de modification) et **authentification du serveur** (certificat).

![Quatre étapes d'une visite HTTPS : DNS, TCP vers le port 443, négociation TLS, HTTP chiffré, avec ce qui est lisible ou opaque pour un observateur](images/ports-protocoles-captures-2.svg)

*Figure 3 — Ce que voit un observateur du réseau lors d'une visite en HTTPS. Schéma original (CC0).*

### 5.1 La négociation TLS (version simplifiée)

1. **ClientHello** (client → serveur) : versions et suites de chiffrement acceptées, une part de clé, le **SNI** (nom du site demandé) et les protocoles applicatifs proposés (ALPN : `h2`, `http/1.1`).
2. **ServerHello** + certificat + validation : le serveur choisit les paramètres et prouve son identité avec un **certificat**. En TLS 1.3, la suite de la négociation est déjà chiffrée.
3. **Finished** de part et d'autre : les clés sont confirmées.
4. **Application Data** : HTTP circule chiffré (enregistrements TLS opaques).

### 5.2 Ce qu'un observateur peut lire

| Élément | Visible en HTTPS ? |
|---|---|
| Adresses IP, ports, horaires, volumes | oui |
| Requête DNS (si DNS classique) | oui |
| Nom du site (SNI du ClientHello) | généralement oui (sauf ECH, extension encore peu déployée) |
| Certificat serveur | en TLS 1.2 oui ; en TLS 1.3 chiffré |
| URL complète, en-têtes, cookies, contenu | non |

### 5.3 Le certificat et la confiance

Le client vérifie que le certificat est signé par une autorité de confiance (**chaîne**), qu'il couvre le **nom demandé** (champ [[Glossary:SAN]]) et qu'il est **valide à la date du jour**. Causes d'échec : certificat expiré, nom inexact, chaîne incomplète, horloge fausse. Un site redirige souvent le port 80 vers 443 (`301`) : dans une capture, on voit un bref échange en clair, puis une connexion vers 443.

## 6. Les outils de capture

| Outil | Usage |
|---|---|
| `tcpdump` | capture en ligne de commande, légère, présente sur la plupart des serveurs |
| **Wireshark** | interface graphique d'analyse (dissecteurs de protocoles, « Suivre le flux ») |
| `tshark` | version en ligne de commande de Wireshark |

Capturer exige des **droits élevés**. Sur un réseau d'entreprise, **demandez l'autorisation** : une capture peut contenir des mots de passe et des données personnelles.

### 6.1 Filtre de capture et filtre d'affichage

- Le **filtre de capture** (syntaxe BPF, ex. `tcp port 8080`) décide de ce qui est enregistré : on le pose **avant**, pour limiter le volume.
- Le **filtre d'affichage** (syntaxe Wireshark, ex. `http` ou `tcp.port == 8080`) masque ce qu'on ne veut pas voir **après**. Ne mélangez pas les deux syntaxes.

Filtres d'affichage utiles dans Wireshark :

| Besoin | Filtre |
|---|---|
| Un port | `tcp.port == 443` |
| Premiers SYN d'une connexion | `tcp.flags.syn == 1 && tcp.flags.ack == 0` |
| DNS ou HTTP en clair | `dns`, `http` |
| ClientHello TLS | `tls.handshake.type == 1` |
| Retransmissions | `tcp.analysis.retransmission` |

Dans Wireshark, le menu contextuel **Suivre → Flux TCP** reconstitue la conversation complète.

## 7. Lire une capture

### 7.1 Anatomie d'une ligne `tcpdump`

![Une ligne de capture tcpdump décomposée : heure, protocole IP, source avec port éphémère, destination avec port 80, drapeaux TCP, numéros de séquence](images/ports-protocoles-captures-3.svg)

*Figure 4 — Lecture d'une ligne de `tcpdump` : heure, protocole, source, destination, drapeaux, séquence. Schéma original (CC0).*

### 7.2 Exemple fictif : poignée de main TCP puis requête HTTP

```text
10:42:07.118 IP 198.51.100.20.50422 > 203.0.113.10.80: Flags [S],  seq 1000, win 64240, length 0
10:42:07.131 IP 203.0.113.10.80 > 198.51.100.20.50422: Flags [S.], seq 2000, ack 1001, win 65160, length 0
10:42:07.131 IP 198.51.100.20.50422 > 203.0.113.10.80: Flags [.],  ack 1, win 502, length 0
10:42:07.132 IP 198.51.100.20.50422 > 203.0.113.10.80: Flags [P.], seq 1:79, ack 1, length 78: HTTP: GET / HTTP/1.1
10:42:07.150 IP 203.0.113.10.80 > 198.51.100.20.50422: Flags [P.], seq 1:512, ack 79, length 511: HTTP: HTTP/1.1 200 OK
```

Lecture ligne par ligne :

1. `[S]` : le client (port 50422) envoie un SYN vers le port 80.
2. `[S.]` : le serveur répond SYN-ACK (`.` signifie « avec ACK »), `ack 1001` confirme le seq 1000 reçu.
3. `[.]` : le client confirme ; le délai SYN → SYN-ACK (13 ms) donne le **temps aller-retour**.
4. `[P.]` : 78 octets de données poussés : la requête `GET / HTTP/1.1`.
5. `[P.]` : le serveur répond 511 octets, début `HTTP/1.1 200 OK`.

### 7.3 Exemple fictif : requête DNS

```text
10:43:02.004 IP 198.51.100.20.40312 > 192.0.2.53.53: 4211+ A? www.example.com. (33)
10:43:02.021 IP 192.0.2.53.53 > 198.51.100.20.40312: 4211 1/0/0 A 203.0.113.10 (49)
```

- UDP : pas de drapeaux ni de poignée de main, un paquet de question et un de réponse.
- `4211` : identifiant, identique dans la réponse. `+` : récursion demandée. `A?` : adresse IPv4 demandée. `1/0/0` : une réponse, aucun serveur d'autorité, aucun complément.
- 17 ms de délai : temps de résolution. Plusieurs secondes, ou une question répétée sans réponse, signalent un **résolveur lent ou injoignable** (voir [la leçon DNS](/fr/00-cours-theoriques/tout-en-un/01-reseaux-et-protocoles/lecons/lecon-dns-en-profondeur)).

### 7.4 Trois signatures de panne

| Ce qu'on voit | Interprétation |
|---|---|
| `[S]` répété (retransmissions à 1 s, 2 s, 4 s…) sans `[S.]` | paquets perdus ou filtrés : pare-feu qui abandonne, route cassée, serveur éteint |
| `[S]` suivi immédiatement de `[R.]` | le port est fermé (aucun service) ou rejeté explicitement |
| retransmissions de données | pertes sur le chemin, réseau saturé |
| requête DNS sans réponse | résolveur injoignable ou UDP/53 filtré |
| ClientHello suivi d'une alerte TLS | incompatibilité de version, certificat ou nom refusé |

## Mise en pratique guidée

**Cadre** : VM Linux jetable, avec `tcpdump`, `curl`, `openssl` et Python 3. Tout se passe sur l'interface locale `lo` : aucune machine distante n'est contactée. Les commandes `sudo` ne servent que pour la capture, dans la VM jetable.

### Étape 1 — Lire le registre des ports

```bash
getent services http https domain bootps
```

👉 Explication : interroge la base locale de services (`/etc/services`) et affiche les numéros officiels de ces quatre services. Lecture seule.

```bash
ss -tuln
```

👉 Explication : liste les ports **en écoute** (`-l`) en TCP (`-t`) et UDP (`-u`), sans résolution de noms (`-n`). C'est l'état `LISTEN` vu en section 3.4. Lecture seule.

### Étape 2 — Démarrer un petit serveur web local

```bash
mkdir -p ~/lab-ports && cd ~/lab-ports
echo '<h1>Labo ports</h1>' > index.html
python3 -m http.server 8080 --bind 127.0.0.1
```

👉 Explication : crée une page, puis lance le serveur HTTP intégré à Python sur le port 8080, **uniquement sur l'interface locale**. Laissez ce terminal ouvert (arrêt : `Ctrl+C`).

### Étape 3 — Capturer pendant une requête (deuxième et troisième terminaux)

Terminal 2 :

```bash
cd ~/lab-ports
sudo tcpdump -ni lo -w labo-http.pcap 'tcp port 8080'
```

👉 Explication : enregistre dans `labo-http.pcap` uniquement le trafic TCP du port 8080 sur l'interface locale (`-n` : pas de résolution de noms). Laissez tourner.

Terminal 3 :

```bash
curl -v http://127.0.0.1:8080/
```

👉 Explication : envoie une requête HTTP au serveur local ; `-v` affiche la requête (`> GET / HTTP/1.1`) et la réponse (`< HTTP/1.0 200 OK`, version employée par Python). Arrêtez ensuite la capture avec `Ctrl+C` dans le terminal 2.

### Étape 4 — Relire la capture

```bash
sudo tcpdump -nr labo-http.pcap
```

👉 Explication : relit le fichier enregistré (`-r`). Repérez, dans l'ordre : `[S]`, `[S.]`, `[.]`, puis `[P.]` avec la requête, `[P.]` avec la réponse, enfin les `[F.]`. Sur `lo`, les deux adresses sont `127.0.0.1`. Dans Wireshark : **Fichier → Ouvrir**, puis **Suivre → Flux TCP**.

```bash
sudo tcpdump -nr labo-http.pcap -A | head -n 40
```

👉 Explication : affiche le contenu en ASCII (`-A`) : `GET / HTTP/1.1` et `Host:` sont lisibles. Sans TLS, tout l'est.

### Étape 5 — Observer TLS avec un serveur de test local

```bash
openssl req -x509 -newkey rsa:2048 -nodes -keyout lab.key -out lab.crt -days 1 -subj "/CN=lab.example.test"
openssl s_server -accept 8443 -cert lab.crt -key lab.key -www
```

👉 Explication : la première commande génère une clé et un certificat **auto-signés** d'un jour, pour ce laboratoire seulement (à supprimer ensuite). La seconde lance un serveur TLS sur le port 8443. Laissez ce terminal ouvert.

Dans un autre terminal, lancez `sudo tcpdump -ni lo -A 'tcp port 8443'`, puis dans un troisième :

```bash
curl -vk --resolve lab.example.test:8443:127.0.0.1 https://lab.example.test:8443/
```

👉 Explication : `--resolve` associe le nom à `127.0.0.1` sans DNS ; `-k` accepte le certificat auto-signé (**test local uniquement** : en production, cette vérification ne se désactive jamais). Dans la capture `-A`, le nom `lab.example.test` apparaît dans le **ClientHello** (SNI), mais plus la requête HTTP ni la page.

### Étape 6 — Interroger un vrai certificat (lecture seule, accès Internet requis)

```bash
openssl s_client -connect example.com:443 -servername example.com </dev/null 2>/dev/null | openssl x509 -noout -subject -issuer -dates
```

👉 Explication : se connecte au domaine réservé `example.com` et n'affiche que le sujet, l'émetteur et les dates de validité du certificat. Lecture seule ; c'est le contrôle de base d'une expiration.

### Étape 7 — Nettoyer

```bash
cd ~ && rm -r ~/lab-ports
```

👉 Explication : arrête d'abord les trois serveurs et captures (`Ctrl+C`), puis supprime le dossier du laboratoire (page, captures, clé et certificat de test).

## Exercices

1. **Ports.** Associez chaque service à son port par défaut : SSH, HTTPS, DHCP (serveur), DNS, NTP, RDP.
2. **Quintuplet.** Un navigateur ouvre deux onglets vers `203.0.113.10:443` depuis `198.51.100.20`. Donnez deux quintuplets possibles et expliquez pourquoi le serveur peut les distinguer.
3. **Drapeaux.** Que signifient les drapeaux `[S]`, `[S.]`, `[.]`, `[P.]`, `[F.]`, `[R]` ?
4. **Ligne de capture.** Décodez : `10:50:11.402 IP 192.0.2.77.38844 > 198.51.100.5.22: Flags [S], seq 4100, win 64240, length 0`.
5. **Diagnostic.** Un client contacte `203.0.113.10:8443`. Cas A : la capture montre quatre `[S]` espacés de 1, 2 et 4 secondes. Cas B : un `[S]` puis un `[R.]` en quelques millisecondes. Interprétez chaque cas.
6. **DNS.** Dans l'échange `4211+ A? www.example.com.` puis `4211 1/0/0 A 203.0.113.10`, quelle information relie les deux paquets et quel transport est utilisé ?
7. **HTTPS.** Un collègue affirme : « avec HTTPS, personne sur le réseau ne sait quel site je visite ». Nuancez avec trois éléments visibles.
8. **Filtres.** Écrivez un filtre de capture BPF ne gardant que le DNS, et un filtre d'affichage Wireshark ne montrant que les premiers SYN vers le port 443.

## Corrigés des exercices

1. SSH 22 ; HTTPS 443 ; DHCP serveur 67 ; DNS 53 ; NTP 123 ; RDP 3389.
2. `TCP 198.51.100.20:50422 → 203.0.113.10:443` et `TCP 198.51.100.20:50423 → 203.0.113.10:443`. Seul le port source diffère, mais le quintuplet est unique : chaque paquet est associé à la bonne connexion.
3. `[S]` SYN (ouverture) ; `[S.]` SYN-ACK ; `[.]` ACK seul ; `[P.]` données poussées avec ACK ; `[F.]` FIN (fermeture) ; `[R]` RST (rupture).
4. À 10 h 50 min 11 s, `192.0.2.77` (port éphémère 38844) envoie un SYN (séquence 4100, fenêtre 64240, sans données) vers `198.51.100.5` port 22 (SSH).
5. Cas A : pas de réponse (pare-feu qui abandonne, route absente, machine éteinte), d'où les retransmissions à délais croissants. Cas B : refus immédiat ; le port 8443 est fermé ou rejeté explicitement.
6. L'**identifiant de requête 4211**, identique dans la question et la réponse. Transport : UDP (port 53), sans connexion.
7. Restent visibles : l'IP du serveur, les ports et volumes, la requête DNS en clair, le SNI du ClientHello (sauf ECH). Seuls l'URL, les en-têtes et le contenu sont protégés.
8. Capture : `port 53` (BPF) ; affichage : `tcp.flags.syn == 1 && tcp.flags.ack == 0 && tcp.dstport == 443`.

## Quiz

**Q1. Quel est le rôle d'un port ?**
A) Désigner la machine. B) Désigner le service sur la machine. C) Chiffrer. D) Attribuer une IP.
**Réponse : B.** L'IP vise la machine, le port le programme.

**Q2. Quel port par défaut pour HTTPS ?**
A) 80. B) 8080. C) 443. D) 22.
**Réponse : C.** 80 est HTTP, 22 est SSH.

**Q3. Quelle séquence correspond à l'établissement d'une connexion TCP ?**
A) ACK, SYN, SYN-ACK. B) SYN, SYN-ACK, ACK. C) SYN, ACK, FIN. D) SYN-ACK, SYN, ACK.
**Réponse : B.** SYN, SYN-ACK, puis ACK du client.

**Q4. Dans `tcpdump`, que signifie `Flags [S.]` ?**
A) Un SYN seul. B) Un SYN-ACK. C) Une fermeture. D) Des données.
**Réponse : B.** Le point signifie « avec ACK ».

**Q5. `[S]` suivi immédiatement de `[R.]` indique le plus souvent :**
A) Un serveur très lent. B) Un port fermé ou rejeté. C) Un certificat expiré. D) Une perte de paquets.
**Réponse : B.** Le RST immédiat signale qu'aucun service n'écoute.

**Q6. Dans une capture HTTPS, quel élément reste généralement lisible ?**
A) Le mot de passe. B) Le corps de la page. C) Le nom du site dans le ClientHello (SNI). D) Les cookies.
**Réponse : C.** Le SNI part avant le chiffrement (sauf ECH).

**Q7. Quel transport utilise HTTP/3 ?**
A) TCP/80. B) UDP/53. C) QUIC sur UDP/443. D) TCP/22.
**Réponse : C.** HTTP/3 repose sur QUIC.

**Q8. Quel filtre Wireshark isole les ClientHello TLS ?**
A) `tls.handshake.type == 1` B) `http.request` C) `dns.qry.type == 1` D) `tcp.port == 22`
**Réponse : A.** Le type 1 est le ClientHello.

**Q9. Quelle différence entre filtre de capture et filtre d'affichage ?**
A) Aucune. B) Le premier limite ce qui est enregistré (syntaxe BPF), le second ce qui est affiché (syntaxe Wireshark). C) Le premier ne fonctionne qu'en UDP. D) Le second chiffre la capture.
**Réponse : B.** Les syntaxes diffèrent.

**Q10. Pourquoi ne jamais utiliser `curl -k` en production ?**
A) Il ralentit la connexion. B) Il désactive la vérification du certificat et ouvre la voie à l'usurpation. C) Il force HTTP/1.0. D) Il supprime les cookies.
**Réponse : B.** Sans vérification, un faux serveur peut se faire passer pour le vrai.

## Erreurs fréquentes et dépannage

| Symptôme | Cause probable | Vérification |
|---|---|---|
| « Connection timed out » | paquet filtré ou abandonné, route absente | capture : SYN sans réponse ; `ss -tn state syn-sent` |
| « Connection refused » | aucun service sur ce port, ou rejet explicite | `ss -tuln` côté serveur ; capture : SYN puis RST |
| Erreur de certificat | expiré, nom absent du SAN, chaîne incomplète, horloge fausse | `openssl s_client -connect hôte:443 -servername hôte` |
| Capture vide | mauvaise interface, filtre trop strict, droits insuffisants | `tcpdump -D`, retirer le filtre, `sudo` |
| Mauvais site servi | en-tête `Host` ou SNI incorrect | `curl -v -H 'Host: …'` ; `--resolve` |

**Méthode** : (1) poser l'hypothèse (DNS, TCP, TLS, HTTP) ; (2) capturer avec un **filtre précis** ; (3) repérer le premier paquet manquant ou refusé ; (4) comparer avec le côté serveur.

```bash
sudo tcpdump -ni any -c 20 'host 192.0.2.10 and tcp port 443'
```

👉 Explication : capture 20 paquets au plus (`-c 20`) sur toutes les interfaces (`-i any`), restreints à une machine et au port 443. À réserver à un poste de test ou avec l'accord de l'exploitant : une capture peut révéler des données sensibles.

## À retenir

- IP désigne la machine, le port désigne le service ; le quintuplet identifie la connexion.
- Ports courants : 22 SSH, 53 DNS, 67/68 DHCP, 80 HTTP, 123 NTP, 443 HTTPS, 3389 RDP ; ce n'est qu'une convention.
- TCP : SYN, SYN-ACK, ACK, puis données, puis FIN ; RST = rupture ou port fermé.
- HTTP est lisible en clair ; HTTPS ne laisse voir que IP, ports, volumes, parfois DNS et SNI.
- TLS : ClientHello (avec SNI et ALPN), serveur et certificat, puis données chiffrées.
- tcpdump : filtre de capture BPF avant, filtre d'affichage Wireshark après.
- Trois signatures : SYN sans réponse (filtrage), SYN puis RST (port fermé), retransmissions (perte).

## Pour aller plus loin

- Registre IANA des noms de services et numéros de ports : https://www.iana.org/assignments/service-names-port-numbers/
- RFC 9293 — Transmission Control Protocol : https://www.rfc-editor.org/rfc/rfc9293
- RFC 768 — User Datagram Protocol : https://www.rfc-editor.org/rfc/rfc768
- RFC 9110 — HTTP Semantics : https://www.rfc-editor.org/rfc/rfc9110
- RFC 8446 — TLS 1.3 : https://www.rfc-editor.org/rfc/rfc8446
- RFC 9000 — QUIC : https://www.rfc-editor.org/rfc/rfc9000
- Documentation de Wireshark : https://www.wireshark.org/docs/
- Manuel de `tcpdump` : https://www.tcpdump.org/manpages/tcpdump.1.html
- Syntaxe des filtres de capture (pcap-filter) : https://www.tcpdump.org/manpages/pcap-filter.7.html
- Leçon associée : [DNS en profondeur](/fr/00-cours-theoriques/tout-en-un/01-reseaux-et-protocoles/lecons/lecon-dns-en-profondeur) ; [DHCP, baux et relais](/fr/00-cours-theoriques/tout-en-un/01-reseaux-et-protocoles/lecons/lecon-dhcp-baux-et-relais)

## Crédits des images

| Fichier | Source | Auteur | Licence | Modifications |
|---|---|---|---|---|
| `images/ports-protocoles-captures-1.svg` | Création originale du projet Pack Master | Projet Pack Master | Création originale du projet Pack Master, dédiée au domaine public (CC0) : https://creativecommons.org/publicdomain/zero/1.0/ | Sans objet |
| `images/ports-protocoles-captures-2.svg` | Création originale du projet Pack Master | Projet Pack Master | Création originale du projet Pack Master, dédiée au domaine public (CC0) : https://creativecommons.org/publicdomain/zero/1.0/ | Sans objet |
| `images/ports-protocoles-captures-3.svg` | Création originale du projet Pack Master | Projet Pack Master | Création originale du projet Pack Master, dédiée au domaine public (CC0) : https://creativecommons.org/publicdomain/zero/1.0/ | Sans objet |
| `images/ports-protocoles-captures-4.svg` | https://commons.wikimedia.org/wiki/File:TCP_Three-Way_Handshake.svg | Fleshgrinder et The People (projet Tango Desktop) | Domaine public (« Public domain » sur la page Commons) | Aucune (fichier renommé) |

## Historique de vérification

| Date | OS/logiciel | Testeur | Verdict |
|---|---|---|---|
| 2026-11-01 | Linux (tcpdump, curl, openssl, python3), Wireshark | Rédaction assistée (Copilot) | Non testé sur plateforme cible |

Précision : à la rédaction, seule une commande locale en lecture seule (`getent services`) a été exécutée ; `tcpdump`, `ss` et `tshark` n'étaient pas installés sur le poste de rédaction. Les extraits de capture sont fictifs ; les sorties sont des exemples typiques. La licence de l'image 4 a été relevée sur Wikimedia Commons le 2026-11-01.