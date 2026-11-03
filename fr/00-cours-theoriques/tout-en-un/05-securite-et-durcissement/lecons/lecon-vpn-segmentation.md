---
title: "Leçon — VPN et segmentation réseau : tunnels, zones, bastion et reverse proxy"
description: "À la fin de cette leçon, vous serez capable de :"
published: true
date: 2026-11-03T14:22:28Z
tags: ["transverse", "tout-en-un", "lecon", "securite", "durcissement", "vpn", "wireguard", "ipsec", "openvpn", "segmentation", "dmz", "bastion", "reverse-proxy"]
editor: markdown
dateCreated: 2026-11-03T14:22:28Z
dateModified: 2026-11-03T14:22:28Z
---

# Leçon — VPN et segmentation réseau : tunnels, zones, bastion et reverse proxy

- **Tags** : `transverse`, `tout-en-un`, `lecon`, `securite`, `durcissement`, `vpn`, `wireguard`, `ipsec`, `openvpn`, `segmentation`, `dmz`, `bastion`, `reverse-proxy`
- **Niveau** : Intermédiaire (administrateur systèmes et réseaux)
- **Durée estimée** : 3 h 30 (cours 1 h 30, laboratoire 1 h 15, exercices et quiz 45 min)

---

## Objectifs pédagogiques

À la fin de cette leçon, vous serez capable de :

1. **expliquer** ce qu'apporte un [[Glossary:VPN]] (confidentialité, intégrité, authentification des extrémités) et ce qu'il n'apporte pas ;
2. **comparer** WireGuard, IPsec/IKEv2 et OpenVPN : principes, ports, identités, cas d'usage ;
3. **distinguer** VPN site à site et accès distant, tunnel complet et tunnel partiel ;
4. **concevoir** des zones (Internet, [[Glossary:DMZ]], interne, administration) et une **matrice de flux** en « tout refuser sauf » ;
5. **décrire** le rôle d'un bastion et configurer un saut [[Glossary:SSH]] propre ;
6. **analyser**, côté sécurité, ce qu'apporte et ce que risque un reverse proxy ;
7. **mener** un laboratoire sur deux [[Glossary:VM]] jetables (WireGuard, nftables, saut SSH) avec snapshot, console de secours, test et retour arrière.

## Prérequis et durée

- Bases [[Glossary:TCP]]/IP (adresses, routage, [[Glossary:NAT]], ports) et pratique d'un shell Linux (`ip`, `ss`).
- Notions de clés et de certificats : voir [Cryptographie appliquée](/fr/00-cours-theoriques/tout-en-un/05-securite-et-durcissement/lecons/lecon-cryptographie-appliquee). Suite logique : [Menaces et défense](/fr/00-cours-theoriques/tout-en-un/05-securite-et-durcissement/lecons/lecon-menaces-defense).
- Matériel : un hyperviseur et deux VM Linux jetables sur un réseau de laboratoire isolé, avec snapshots.
- Durée : environ 3 h 30. Adresses de documentation (`192.0.2.0/24`, `198.51.100.0/24`, `203.0.113.0/24`, `2001:db8::/32`), domaines `example.com` et `example.test`. Les clés sont des étiquettes `<CLE_PRIVEE_...>` : générez les vôtres.

## L'essentiel en bref

- Un **VPN** crée un tunnel chiffré et authentifié à travers un réseau non fiable ; il protège le **transport**, pas ce qu'il y a au bout.
- **WireGuard** : minimaliste, clés publiques et adresses autorisées par pair. **IPsec/IKEv2** : standard interopérable. **OpenVPN** : basé sur [[Glossary:TLS]], passe bien les pare-feu.
- **Segmenter**, c'est découper en zones de confiance et n'autoriser que les flux nécessaires, en commençant par **tout refuser**.
- La **DMZ** héberge ce qui est exposé : un serveur compromis ne doit pas rebondir librement vers l'interne.
- Le **bastion** est l'unique porte d'administration, avec authentification forte et journalisation.
- Le **reverse proxy** centralise TLS et filtrage, mais est une cible à durcir.
- Toute modification : **snapshot, console de secours, test, retour arrière**.

![Schéma montrant un site siège et un site agence reliés par un tunnel chiffré à travers Internet, ainsi qu'un poste nomade qui se connecte à la passerelle VPN](images/vpn-segmentation-1.svg)

*Figure 1 — VPN site à site et accès distant. Schéma original, domaine public (CC0).*

---

## 1. Le problème : un périmètre qui n'existe plus

Le modèle du château fort (tout ce qui est dedans est de confiance) a cédé : utilisateurs et applications sont partout, et un poste compromis permet de se **déplacer latéralement** dans un réseau plat. Deux principes guident cette leçon : la **défense en profondeur** (plusieurs couches indépendantes) et le **moindre privilège**.

## 2. Ce que fait (et ne fait pas) un VPN

Un VPN **encapsule** les paquets dans d'autres paquets, les **chiffre** et les **authentifie**. Analogie : un convoi blindé dans une ville : on voit le camion, pas son contenu.

**Il garantit** la confidentialité et l'intégrité du trafic entre les extrémités, et leur authentification.

**Il ne garantit pas** que le poste distant soit sain (un poste infecté apporte son malware), que l'utilisateur n'accède qu'à ce qui le concerne (sans filtrage derrière le tunnel, « VPN connecté » donne souvent « accès à tout »), ni l'anonymat.

| Usage | Qui se connecte | Exemple |
|---|---|---|
| **Site à site** | Deux passerelles | Siège `192.0.2.0/24` ↔ agence `198.51.100.0/24`, tunnel permanent |
| **Accès distant** | Un utilisateur avec client VPN | Télétravailleur depuis `203.0.113.50` |

Côté client : **tunnel complet** (tout le trafic passe par l'entreprise : visibilité, mais bande passante et latence) ou **tunnel partiel** (seuls les réseaux d'entreprise : économe, mais le poste est à la fois sur Internet et dans le réseau interne).

## 3. IPsec / IKEv2 : le standard interopérable

IPsec est une **famille** de protocoles normalisés :

- **IKEv2** (RFC 7296) négocie : authentification des pairs (certificats, clé pré-partagée, EAP) et établissement des clés, en **[[Glossary:UDP]] 500**, ou **UDP 4500** avec traversée de NAT ;
- **ESP** (RFC 4303) transporte et chiffre les paquets ;
- la **SA** est le « contrat » unidirectionnel (algorithmes, clés, durée) ;
- le **mode tunnel** encapsule le paquet entier (réseau à réseau), le **mode transport** protège seulement le contenu (hôte à hôte) ;
- les **sélecteurs de trafic** définissent quels réseaux passent dans le tunnel.

**Forces** : présent partout, interopérable, intégré aux [[Glossary:PKI]]. **Attention** : nombreux paramètres à faire **correspondre exactement** des deux côtés (propositions, sélecteurs, durées), clés pré-partagées faibles, [[Glossary:MTU]].

Extrait strongSwan (`swanctl.conf`), à lire et à adapter :

```bash
connections {
  siege-agence {
    version = 2
    local_addrs  = 203.0.113.1
    remote_addrs = 203.0.113.2
    proposals    = aes256gcm16-prfsha384-x25519
    local  { auth = pubkey ; certs = siege.pem }
    remote { auth = pubkey ; id = agence.example.com }
    children {
      reseaux {
        local_ts  = 192.0.2.0/24
        remote_ts = 198.51.100.0/24
        esp_proposals = aes256gcm16-x25519
        start_action  = trap
      }
    }
  }
}
```

👉 Explication : exemple de tunnel IKEv2 entre deux passerelles de documentation, avec suites AEAD et échange éphémère, authentification par certificats et trafic limité aux deux sous-réseaux. Non testé : adaptez-le à votre version de strongSwan et validez-le en laboratoire.

Contrôles usuels : `sudo swanctl --list-sas` et `ip xfrm state` ; pas de SA après un test de trafic : chercher un désaccord de propositions ou de sélecteurs.

## 4. OpenVPN : un VPN construit sur TLS

OpenVPN s'appuie sur **TLS** pour l'authentification et l'échange de clés, puis chiffre les données (AES-GCM ou ChaCha20-Poly1305), en **UDP** (1194, recommandé) ou en **TCP** (souvent 443, pour traverser des pare-feu restrictifs).

**Forces** : très configurable, certificats, identifiants et second facteur, routes et [[Glossary:DNS]] poussés aux clients. **Attention** : une **PKI** à gérer (émission, expiration, révocation par [[Glossary:CRL]]) ; le **TCP dans TCP** dégrade les performances en cas de perte, à réserver aux contournements ; évitez les réglages historiques (CBC, compression) ; activez `tls-crypt` pour authentifier et masquer la négociation TLS.

```bash
port 1194
proto udp
dev tun
server 198.51.100.0 255.255.255.0
tls-version-min 1.2
data-ciphers AES-256-GCM:CHACHA20-POLY1305
tls-crypt tls-crypt.key
remote-cert-tls client
crl-verify crl.pem
```

👉 Explication : directives de sécurité d'un serveur OpenVPN d'exemple : TLS 1.2 minimum, chiffrements AEAD, clé `tls-crypt`, vérification du type de certificat client, liste de révocation, abandon des privilèges. Les fichiers cités viennent de **votre** PKI de laboratoire.

## 5. WireGuard : minimaliste et net

WireGuard a très peu de code, un seul jeu d'algorithmes (Curve25519, ChaCha20-Poly1305, BLAKE2s, cadre Noise) et aucune négociation : pas de « mauvaise suite » possible. Il est intégré au noyau Linux et existe sur Windows, macOS, Android, iOS.

### 5.1 Le modèle : clé publique et adresses autorisées

Pour chaque pair, on déclare **sa clé publique** et ses **adresses autorisées** (`AllowedIPs`), qui jouent deux rôles : **routage sortant** (vers ces adresses, on utilise le tunnel de ce pair) et **filtrage entrant** (un paquet déchiffré n'est accepté que si sa source est dans la liste de ce pair). Analogie : chaque correspondant n'a le droit d'écrire qu'avec **son** adresse d'expéditeur.

![Deux pairs WireGuard, chacun avec sa clé publique et la liste des adresses autorisées de l'autre pair, échangeant des paquets UDP chiffrés](images/vpn-segmentation-4.svg)

*Figure 2 — Principe de WireGuard : chaque clé publique est liée à des adresses autorisées. Schéma original, domaine public (CC0).*

### 5.2 Particularités

- Transport **UDP** (51820 par convention) ; **silencieux** : sans paquet authentifié, le port ne répond pas aux sondes.
- Pas de gestion native d'utilisateurs ni d'adresses dynamiques : **un pair = une clé = une section**. Révoquer, c'est retirer le pair.
- Peu de journaux : supervisez avec `wg show`. `PersistentKeepalive` maintient la traversée d'un NAT.

### 5.3 Configuration (étiquettes à remplacer)

```bash
[Interface]
Address = 198.51.100.1/24
ListenPort = 51820
PrivateKey = <CLE_PRIVEE_SERVEUR>

[Peer]
PublicKey = <CLE_PUBLIQUE_CLIENT>
AllowedIPs = 198.51.100.2/32
```

👉 Explication : `/etc/wireguard/wg0.conf` du serveur de laboratoire : adresse du tunnel, écoute UDP 51820, et seul `198.51.100.2` accepté depuis le pair client. Remplacez l'étiquette par une clé générée localement et gardez le fichier en droits `600`.

```bash
[Interface]
Address = 198.51.100.2/24
PrivateKey = <CLE_PRIVEE_CLIENT>

[Peer]
PublicKey = <CLE_PUBLIQUE_SERVEUR>
Endpoint = 192.0.2.10:51820
AllowedIPs = 198.51.100.1/32
PersistentKeepalive = 25
```

👉 Explication : fichier du client ; `Endpoint` désigne le serveur dans le réseau de laboratoire et `AllowedIPs` limite le tunnel au serveur (tunnel partiel). `0.0.0.0/0` ferait passer tout le trafic par le tunnel.

## 6. Comparatif

| Critère | WireGuard | IPsec / IKEv2 | OpenVPN |
|---|---|---|---|
| Transport | UDP | UDP 500/4500 + ESP | UDP 1194 ou TCP 443 |
| Authentification | Clés publiques | Certificats, PSK, EAP | Certificats, identifiants, [[Glossary:MFA]] |
| Complexité | Faible | Élevée | Moyenne |
| Interopérabilité | WireGuard seulement | Excellente | Clients OpenVPN |
| Cas typique | Petits réseaux, nomades, labo | Site à site multi-constructeurs | Accès distant avec identités |

Pas de gagnant universel : le choix dépend de l'**existant**, des identités à gérer et des compétences de l'équipe.

## 7. Accès distant : bonnes pratiques

1. **Authentification forte** : certificat ou clé plus second facteur.
2. **Moindre privilège** : le VPN place l'utilisateur dans une **zone dédiée** filtrée, jamais directement dans le [[Glossary:LAN]].
3. **Postes de confiance** (disque chiffré, correctifs) et **DNS maîtrisé**.
4. **Journalisation** des connexions et origines inhabituelles, **suppression des accès** au départ.

## 8. Segmentation : zones, flux et DMZ

### 8.1 L'idée

Un réseau « plat » est un immeuble sans portes intérieures. La **segmentation** découpe en **zones de confiance** reliées par un point de filtrage (pare-feu à états, routeur filtrant).

| Zone | Contenu | Confiance |
|---|---|---|
| Internet | Visiteurs, attaquants | Nulle |
| **DMZ** | Reverse proxy, relais de messagerie | Faible (exposée) |
| Interne | Applications, bases de données | Élevée |
| Administration | Bastion, supervision, sauvegarde | Très élevée |

### 8.2 La DMZ

La DMZ est un **sas** pour ce qui est joignable depuis Internet. Internet → DMZ : seulement les ports publiés. DMZ → interne : **le strict minimum** (un hôte, un port), journalisé ; idéalement l'interne initie les connexions vers la DMZ. L'objectif : un serveur compromis en DMZ ne sert pas de tête de pont.

### 8.3 La matrice de flux

Politique par défaut « **tout refuser** », puis des flux justifiés :

| Source → Destination | Protocole / port | Statut |
|---|---|---|
| Internet → reverse proxy (DMZ) | TCP 443 | Autorisé |
| Reverse proxy → application | TCP 8080 vers `192.0.2.20` seul | Autorisé, journalisé |
| Application → base de données | TCP 5432 vers `192.0.2.30` | Autorisé |
| Bastion → serveurs | TCP 22 | Autorisé |
| Tout le reste | Tous | **Refusé et journalisé** |

La matrice sert de cahier des charges et d'outil de revue (« pourquoi ce flux existe-t-il encore ? »).

![Zones Internet, DMZ, réseau interne et administration séparées par un pare-feu, avec les flux autorisés représentés par des flèches](images/vpn-segmentation-2.svg)

*Figure 3 — Zones et flux autorisés (exemple). Schéma original, domaine public (CC0).*

### 8.4 Mettre en œuvre

Moyens : **[[Glossary:VLAN]]** routés **via le pare-feu**, pare-feu **à états**, filtrage sur l'hôte pour le trafic *est-ouest*, groupes de sécurité en cloud. Exemple nftables pour une passerelle de laboratoire :

```bash
table inet filtre {
  chain input {
    type filter hook input priority 0; policy drop;
    ct state established,related accept
    iif lo accept
    meta l4proto { icmp, ipv6-icmp } accept
    udp dport 51820 accept
    tcp dport 22 ip saddr 192.0.2.20 accept
  }
  chain forward {
    type filter hook forward priority 0; policy drop;
    ct state established,related accept
    iifname "wg0" ip daddr 192.0.2.20 tcp dport 443 accept
    limit rate 5/minute log prefix "forward-refuse: "
  }
}
```

👉 Explication : politique `drop` par défaut en entrée et en transfert ; acceptés : flux établis, boucle locale, [[Glossary:ICMP]], port WireGuard, SSH depuis le seul bastion `192.0.2.20` et, depuis `wg0`, HTTPS vers un serveur précis ; le reste est journalisé avec limitation de débit. **Danger** : une règle `drop` mal posée coupe votre propre session SSH, d'où la procédure de la section 11.

## 9. Le bastion d'administration

Si chaque serveur expose SSH ou [[Glossary:RDP]] à plusieurs réseaux, la surface d'attaque est énorme et personne ne sait qui s'est connecté. Un **bastion** concentre l'administration en **un point** durci : seul hôte autorisé par le pare-feu à ouvrir des sessions d'administration, **authentification forte** et **comptes nominatifs** (pas de compte partagé), **journalisation** voire enregistrement des sessions, système minimal et à jour, accès lui-même précédé d'un VPN d'administration.

![Deux chaînes de contrôle : l'administrateur se connecte au bastion qui journalise puis atteint les serveurs ; le visiteur web arrive sur le reverse proxy en DMZ qui relaie vers l'application interne](images/vpn-segmentation-3.svg)

*Figure 4 — Bastion pour l'administration et reverse proxy pour la publication web. Schéma original, domaine public (CC0).*

OpenSSH traverse le bastion **sans y déposer la clé privée** :

```bash
Host bastion
    HostName bastion.example.com
    User prenom.nom
    IdentityFile ~/.ssh/id_ed25519

Host srv-*.example.test
    User prenom.nom
    ProxyJump bastion
    IdentityFile ~/.ssh/id_ed25519
```

👉 Explication : extrait de `~/.ssh/config` du poste administrateur ; tout hôte `srv-*` est atteint via `ProxyJump`. Évitez `ForwardAgent yes` : un administrateur du bastion pourrait réutiliser votre agent. La session reste chiffrée de bout en bout : le bastion ne fait que relayer.

```bash
sudo sshd -t
sudo sshd -T | grep -Ei 'permitrootlogin|passwordauthentication|allowusers|allowgroups'
```

👉 Explication : `sshd -t` valide la syntaxe sans rien modifier ; `sshd -T` affiche les paramètres réellement appliqués. Attendus : `permitrootlogin no`, `passwordauthentication no`, une liste d'utilisateurs ou groupes autorisés. Le filtrage « SSH seulement depuis le bastion » se pose au pare-feu.

## 10. Le reverse proxy, vu côté sécurité

Un reverse proxy se place **devant** les applications : les clients lui parlent, il relaie ensuite. 

**Apports** : **terminaison TLS** centralisée ; **masquage** de l'architecture ; **filtrage** (taille de requête, débit par client, méthodes autorisées, éventuellement [[Glossary:WAF]]) ; **en-têtes de sécurité** uniformes ; **journalisation** centralisée utile à la corrélation ; répartition de charge.

**Risques** : il **ne corrige pas** une application vulnérable ; il est lui-même **exposé** (mise à jour, durcissement) ; l'application ne doit faire confiance à `X-Forwarded-For` que s'il vient **du proxy**, sinon un client peut usurper une adresse ; un proxy mal configuré peut devenir un **relais ouvert** vers l'interne (définissez précisément les *upstreams*) ; après terminaison TLS, le tronçon interne est **en clair** s'il n'est ni chiffré ni isolé.

```bash
server {
    listen 443 ssl;
    server_name www.example.com;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_certificate     /etc/nginx/tls/www.example.com.crt;
    ssl_certificate_key /etc/nginx/tls/www.example.com.key;

    add_header Strict-Transport-Security "max-age=31536000" always;
    add_header X-Content-Type-Options "nosniff" always;
    client_max_body_size 5m;

    location / {
        proxy_pass http://192.0.2.20:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $remote_addr;
    }
}
```

👉 Explication : exemple nginx : HTTPS avec TLS 1.2 et 1.3 seulement, deux en-têtes de sécurité, taille de requête limitée, relais vers un serveur interne précis ; `X-Forwarded-For` est **écrasé** par l'adresse réellement vue, ce qui empêche l'usurpation par le client. Clé privée en droits `600`, jamais dans un dépôt.

```bash
sudo nginx -t
```

👉 Explication : teste la syntaxe de la configuration sans recharger le service ; à exécuter avant tout `systemctl reload nginx`.

## 11. Mise en pratique guidée

> **Cadre.** Deux VM Linux jetables sur un réseau de laboratoire isolé : **VM-A** « serveur » (`192.0.2.10`) et **VM-B** « client et bastion » (`192.0.2.20`). Les `sudo` ne s'exécutent que dans ces VM.
>
> **Avant chaque modification :** **1.** **snapshot** des deux VM et copie de `/etc` (`sudo cp -a /etc /root/etc-avant-lab`) ; **2.** **console de secours** de l'hyperviseur ouverte sur chaque VM (elle survit à une coupure réseau) ; **3.** **test** de configuration (`nft -c`, `sshd -t`, `nginx -t`) puis vérification depuis un **second terminal** ; **4.** **retour arrière** prévu : snapshot, fichiers sauvegardés ou minuterie automatique ci-dessous.

### Étape 1 — Installer WireGuard et générer des clés jetables

Sur chaque VM :

```bash
sudo apt update && sudo apt install -y wireguard wireguard-tools
umask 077
wg genkey | tee ~/wg-privee.key | wg pubkey > ~/wg-publique.key
cat ~/wg-publique.key
```

👉 Explication : installe les outils, génère une paire de clés (droits restreints par `umask 077`) et n'affiche que la **clé publique**, à recopier dans la configuration de l'autre VM. Ne copiez ni n'affichez jamais la clé privée.

### Étape 2 — Créer et activer le tunnel

Écrivez `/etc/wireguard/wg0.conf` sur chaque VM d'après la section 5.3, puis :

```bash
sudo chmod 600 /etc/wireguard/wg0.conf
sudo wg-quick up wg0
sudo wg show
```

👉 Explication : restreint les droits du fichier (il contient la clé privée), active `wg0` et affiche l'état ; avant le premier échange, aucune poignée de main n'apparaît.

### Étape 3 — Tester et observer

Sur VM-B :

```bash
ping -c 3 198.51.100.1
sudo wg show
```

👉 Explication : le `ping` vers l'adresse du tunnel doit répondre ; `wg show` montre alors `latest handshake` et des compteurs `transfer` non nuls. Facultatif : `sudo tcpdump -ni any udp port 51820 -c 5` pendant un `ping` ne montre que des paquets UDP au contenu chiffré.

### Étape 4 — Prouver le filtrage par `AllowedIPs`

Sur VM-A, remplacez temporairement `AllowedIPs = 198.51.100.2/32` par `198.51.100.99/32` dans le fichier, puis :

```bash
sudo wg syncconf wg0 <(sudo wg-quick strip wg0)
ping -c 2 198.51.100.2
```

👉 Explication : VM-A ne peut plus joindre `198.51.100.2` par ce pair (et refuserait ses paquets) : `AllowedIPs` sert bien de routage et de filtre. Retour arrière : remettre la valeur d'origine et relancer la même commande `syncconf`.

### Étape 5 — Politique « tout refuser » sans se couper

Enregistrez les règles de la section 8.4 dans `~/filtre.nft` sur VM-A, puis :

```bash
sudo nft -c -f ~/filtre.nft
sudo nft list ruleset > ~/regles-avant.nft
sudo systemd-run --on-active=300 --unit=retour-pare-feu nft flush ruleset
sudo nft -f ~/filtre.nft
```

👉 Explication : vérifie la syntaxe sans l'appliquer, sauvegarde les règles actuelles, **programme un retour automatique** dans 5 minutes (qui vide les règles) puis applique le nouveau jeu. Testez depuis un second terminal (tunnel, SSH depuis le bastion).

```bash
sudo systemctl stop retour-pare-feu.timer
sudo nft list ruleset
```

👉 Explication : annule le retour automatique une fois le test validé, puis affiche les règles actives. Retour arrière manuel : `sudo nft flush ruleset` puis `sudo nft -f ~/regles-avant.nft`, ou restauration du snapshot.

### Étape 6 — Saut SSH via le bastion

```bash
ssh -J utilisateur@192.0.2.20 utilisateur@192.0.2.10 hostname
```

👉 Explication : exécute `hostname` sur VM-A en passant par VM-B. La règle SSH de l'étape 5 n'accepte que le bastion `192.0.2.20` : une connexion directe depuis un autre hôte est refusée, seule la route avec saut fonctionne. Validez `sshd -t` avant tout rechargement SSH et gardez la console ouverte.

### Étape 7 — Nettoyage

```bash
sudo wg-quick down wg0
shred -u ~/wg-privee.key 2>/dev/null; rm -f ~/wg-publique.key ~/filtre.nft
```

👉 Explication : ferme le tunnel et supprime clés et règles de laboratoire ; restaurez ensuite le snapshot initial des deux VM.

## Exercices

1. **(Vocabulaire)** Définissez en une phrase : tunnel, SA, `AllowedIPs`, DMZ, bastion, reverse proxy.
2. **(Choix de VPN)** Un siège et une agence ont des pare-feu de marques différentes ; 8 télétravailleurs doivent aussi se connecter avec double authentification. Quelle(s) technologie(s) ?
3. **(Tunnel complet ou partiel)** Tout accès web des nomades doit traverser le proxy de filtrage de l'entreprise. Quel mode ? Deux inconvénients, une précaution.
4. **(Matrice de flux)** Dressez la matrice (6 lignes maximum) : navigateur → reverse proxy → application → base PostgreSQL, plus la supervision.
5. **(Reverse proxy)** L'application voit tous les clients arriver de l'adresse du proxy. Pourquoi, et comment corriger sans permettre l'usurpation de `X-Forwarded-For` ?
6. **(Laboratoire)** Réalisez les étapes 1 à 5, ajoutez une règle n'autorisant que `192.0.2.20` en TCP 443 depuis `wg0`, prouvez par un test que les autres destinations sont refusées et documentez le retour arrière.

## Corrigés des exercices

1. **Tunnel** : liaison logique où des paquets sont encapsulés (et chiffrés) dans d'autres paquets. **SA** : accord unidirectionnel IPsec (algorithmes, clés, durée). **`AllowedIPs`** : adresses associées à un pair WireGuard, pour le routage sortant et le filtrage entrant. **DMZ** : zone intermédiaire des services exposés. **Bastion** : hôte durci, unique point d'entrée de l'administration. **Reverse proxy** : frontal qui reçoit les requêtes et les relaie vers l'interne.
2. **IPsec/IKEv2** pour le site à site (interopérable entre constructeurs) ; **OpenVPN** ou **WireGuard** avec une couche d'identité pour les télétravailleurs, avec second facteur. OpenVPN est le plus naturel pour un MFA intégré.
3. **Tunnel complet**. Inconvénients : bande passante et latence côté siège ; trafic personnel qui passe aussi par l'entreprise. Précaution : dimensionner la passerelle et informer par une charte.
4. Navigateur → proxy TCP 443 (autorisé) ; proxy → application TCP 8080 vers l'hôte précis (autorisé) ; application → PostgreSQL TCP 5432 (autorisé) ; supervision → serveurs via agent ou SNMPv3 restreint (autorisé) ; navigateur → application directe (refusé) ; Internet → base de données (refusé).
5. Le proxy ouvre la connexion : l'application voit son adresse. Le proxy transmet l'adresse réelle (`X-Forwarded-For` ou protocole PROXY) en **écrasant** l'en-tête reçu de l'extérieur, et l'application ne l'accepte **que si la connexion vient d'un proxy de confiance** listé explicitement.
6. Règle : `iifname "wg0" ip daddr 192.0.2.20 tcp dport 443 accept`. Test : un `curl --max-time 5` vers un autre hôte ou port depuis `wg0` échoue et apparaît dans le journal (`forward-refuse`). Retour arrière : minuterie `systemd-run`, puis `nft -f ~/regles-avant.nft` ou snapshot.

## Quiz

**Q1.** Un VPN garantit en priorité :
- A. Que le poste distant est sain — B. La confidentialité et l'intégrité du trafic entre ses extrémités — C. L'anonymat total — D. La disponibilité de l'application

**Q2.** Rôle de `AllowedIPs` dans WireGuard :
- A. Seulement le DNS — B. Routage sortant et filtrage entrant par pair — C. Choisir le chiffrement — D. Définir le port

**Q3.** Ports d'IPsec/IKEv2 avec traversée de NAT :
- A. TCP 80 — B. UDP 500 et 4500 — C. TCP 3389 — D. UDP 53

**Q4.** Pourquoi éviter OpenVPN en TCP quand l'UDP est possible ?
- A. TCP est interdit — B. Le TCP dans TCP dégrade les performances en cas de pertes — C. UDP est chiffré, pas TCP — D. TCP n'accepte pas TLS

**Q5.** Politique de base d'un pare-feu de segmentation :
- A. Tout autoriser sauf exceptions — B. Tout refuser sauf flux explicitement autorisés — C. Autoriser l'entrant et le sortant — D. Désactiver la journalisation

**Q6.** Un serveur de la DMZ est compromis : quelle règle limite les dégâts ?
- A. DMZ → interne : tout autorisé — B. DMZ → interne limité à un hôte et un port, journalisé — C. Interne → Internet interdit — D. Désactiver le pare-feu

**Q7.** Rôle principal d'un bastion :
- A. Héberger les sites web — B. Concentrer et tracer l'administration derrière une authentification forte — C. Accélérer le réseau — D. Remplacer le VPN

**Q8.** Pourquoi éviter `ForwardAgent yes` sur un bastion ?
- A. Ralentit SSH — B. Un administrateur du bastion peut réutiliser l'agent de l'utilisateur — C. Désactive MFA — D. SSH l'interdit

**Q9.** Un reverse proxy corrige-t-il une vulnérabilité applicative ?
- A. Toujours — B. Non : il réduit l'exposition et filtre, sans remplacer le correctif — C. Oui, s'il est en TLS — D. Seulement avec WireGuard

**Q10.** Avant de changer des règles de pare-feu sur un serveur distant :
- A. Rien de particulier — B. Snapshot, console de secours, test de configuration et retour arrière — C. Un second pare-feu identique — D. Une autorisation orale

**Réponses justifiées.** **Q1 — B** : le VPN protège le canal, pas l'état du poste. **Q2 — B** : les adresses guident l'envoi et valident la source. **Q3 — B** : IKE sur UDP 500 ; avec NAT, ESP encapsulé en UDP 4500. **Q4 — B** : deux retransmissions empilées se perturbent. **Q5 — B** : « tout refuser sauf » rend chaque flux justifié. **Q6 — B** : un flux minimal empêche le déplacement latéral. **Q7 — B** : point de contrôle et de traçabilité. **Q8 — B** : le socket de l'agent est accessible aux administrateurs du bastion ; préférez `ProxyJump`. **Q9 — B** : une requête légitime en apparence exploite toujours la faille. **Q10 — B** : sans cette procédure, une règle erronée peut couper l'accès sans issue.

## Erreurs fréquentes et dépannage

| Symptôme | Cause probable | Vérification / solution |
|---|---|---|
| Pas de `latest handshake` | Clés croisées erronées, UDP bloqué, `Endpoint` faux | Revérifier les clés, `ss -lun`, pare-feu, adresse du pair |
| Tunnel IPsec « up » sans trafic | Sélecteurs incohérents, MTU, filtrage | `swanctl --list-sas`, `ping -M do -s 1400`, pare-feu |
| SSH coupé après des règles `drop` | Règle `established` ou port 22 oublié | Console de secours, minuterie de retour, `nft flush ruleset` |
| L'application voit l'[[Glossary:IP]] du proxy | En-têtes de transmission non utilisés | Configurer `X-Forwarded-For` et les proxys de confiance |

Règle : **changer une seule chose à la fois**, consigner l'heure, savoir revenir en arrière.

## À retenir

- Le VPN protège le transport ; il faut **en plus** filtrer, authentifier et journaliser derrière le tunnel.
- **WireGuard** : simple, rapide, clés publiques et `AllowedIPs`. **IPsec/IKEv2** : interopérable, plus de réglages. **OpenVPN** : TLS, identités, traversée de pare-feu.
- **Segmenter** : zones de confiance, « tout refuser », matrice de flux justifiée et revue.
- **DMZ** : héberger l'exposé, limiter au minimum les flux vers l'interne.
- **Bastion** : point d'entrée unique, comptes nominatifs, journaux ; `ProxyJump` plutôt que `ForwardAgent`.
- **Reverse proxy** : TLS, filtrage, journaux ; le durcir et gérer `X-Forwarded-For`.
- Toute modification : **snapshot, console de secours, test, retour arrière** (minuterie de retour pour un pare-feu distant).

## Pour aller plus loin

- WireGuard — documentation : <https://www.wireguard.com/> et démarrage rapide : <https://www.wireguard.com/quickstart/>
- RFC 7296 (IKEv2) : <https://www.rfc-editor.org/rfc/rfc7296> ; RFC 4303 (ESP) : <https://www.rfc-editor.org/rfc/rfc4303> ; RFC 3948 (NAT-T) : <https://www.rfc-editor.org/rfc/rfc3948>
- strongSwan : <https://docs.strongswan.org/>
- OpenVPN — manuel de référence : <https://openvpn.net/community-resources/reference-manual-for-openvpn-2-6/>
- nftables — wiki : <https://wiki.nftables.org/>
- OpenSSH : <https://man.openbsd.org/ssh_config> et <https://man.openbsd.org/sshd_config>
- nginx — module proxy : <https://nginx.org/en/docs/http/ngx_http_proxy_module.html>
- [[Glossary:NIST]] SP 800-77 Rev. 1 (IPsec) : <https://csrc.nist.gov/pubs/sp/800/77/r1/final> ; SP 800-207 (Zero Trust) : <https://csrc.nist.gov/pubs/sp/800/207/final>
- [[Glossary:ANSSI]] : <https://cyber.gouv.fr/>

## Crédits des images

| Fichier | Source (URL de la page Commons) | Auteur | Licence | Modifications |
|---|---|---|---|---|
| `images/vpn-segmentation-1.svg` | Création originale (pas de page Commons) | Projet Pack Master | CC0 1.0 : <https://creativecommons.org/publicdomain/zero/1.0/deed.fr> | Aucune |
| `images/vpn-segmentation-2.svg` | Création originale | Projet Pack Master | CC0 1.0 : <https://creativecommons.org/publicdomain/zero/1.0/deed.fr> | Aucune |
| `images/vpn-segmentation-3.svg` | Création originale | Projet Pack Master | CC0 1.0 : <https://creativecommons.org/publicdomain/zero/1.0/deed.fr> | Aucune |
| `images/vpn-segmentation-4.svg` | Création originale | Projet Pack Master | CC0 1.0 : <https://creativecommons.org/publicdomain/zero/1.0/deed.fr> | Aucune |

Création originale du projet Pack Master, dédiée au domaine public (CC0).

## Historique de vérification

| Date | OS/logiciel | Testeur | Verdict |
|---|---|---|---|
| 2026-11-01 | VM Linux de laboratoire (Debian/Ubuntu) : WireGuard, nftables, OpenSSH, nginx, strongSwan, OpenVPN | — | Non testé sur plateforme cible |
| 2026-11-01 | Poste de rédaction : validation XML des schémas SVG et contrôle des liens ; aucune commande réseau ni pare-feu exécutée | Agent de rédaction du pack | Contrôles de format uniquement |