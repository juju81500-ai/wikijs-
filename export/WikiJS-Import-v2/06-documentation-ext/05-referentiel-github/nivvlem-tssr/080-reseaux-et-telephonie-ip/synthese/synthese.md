---
title: "Synthèse – Réseaux et téléphonie IP (ToIP)"
description: "- Chaque couche ajoute/enlève des en-têtes (encapsulation)"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# Synthèse – Réseaux et téléphonie IP (ToIP)
## 🧱 Fondamentaux réseau

### Modèle OSI (7 couches)

- **Application → Physique**
- Chaque couche ajoute/enlève des en-têtes (encapsulation)

### Analyse des paquets

- Trame Ethernet : MAC source/dest, EtherType, CRC
- Paquet IP : IP source/dest, TTL, protocole
- Outils : **Wireshark** (filtres `ip`, `arp`, `tcp`, `sip`, `rtp`…)

### Routage

- Routage **statique** : `ip route 192.168.1.0 255.255.255.0 10.0.0.1`
- Routage **inter-VLAN** : Router-on-a-stick via `g0/0.x + encapsulation dot1Q`
- **Distance administrative** : plus c’est bas, plus la source est fiable
- **RIP v2** : protocole de routage dynamique simple

### VLAN & Trunk

- VLAN = segmentation logique : `vlan 10`, `switchport access vlan 10`
- Trunk : transport de plusieurs VLANs : `switchport mode trunk`

### SVI (interface VLAN)

- Permet l’accès IP au switch : `interface vlan 10 + ip address + no shutdown`

---

## 🔐 Sécurité des équipements

### Accès

- `enable secret`, `line vty`, `password`, `login`
- SSH : `transport input ssh`, `crypto key generate rsa`
- Bannière légale : `banner motd #...#`

### ACL (listes de contrôle d’accès)

- Standard : filtrage IP source uniquement
- Étendue : filtrage IP source/destination, protocole, port
- Syntaxe :

```shell
access-list 100 permit tcp 192.168.1.0 0.0.0.255 any eq 80
interface g0/0
 ip access-group 100 in
```

- Attention à l’**ordre** et au **deny implicite** final

### NAT

- Statique : `ip nat inside source static 192.168.0.10 209.1.1.10`
- PAT : `overload` → plusieurs clients sur une IP publique

---

## 📞 Téléphonie IP – ToIP

### Protocoles clés

|Protocole|Rôle|Port|
|---|---|---|
|**SIP**|Signalisation|5060/5061|
|**RTP**|Flux audio|Dynamique (UDP)|
|**RTCP**|Statistiques RTP|UDP 5005|

### Codecs audio

|Codec|Qualité (MOS)|Débit|
|---|---|---|
|G.711|4.1 (haute)|64 kbps|
|G.729|3.9 (bonne)|8 kbps|

### QoS (Qualité de service)

- Latence < 150 ms, Jitter < 30 ms, Perte < 1 %
- DSCP : `EF` (voix), `AFxx` (flux sensible), `CSx` (autres)

### Dimensionnement

- Bande passante : 100 Kbps/appel (G.711 + overhead)
- Isolation des flux : VLAN voix + VLAN data

---

## 🛠️ XiVO – Serveur IPBX open source

### Installation

- Debian + ISO XiVO
- Interface réseau statique, accès via WebUI : `http://192.168.0.1`
- Configuration initiale : entité, plages de numéros, DNS, domaine

### Gestion utilisateurs

- Ajout manuel ou via import CSV
- Affectation de lignes SIP, groupe, profil, musique d’attente

### Tests softphone

- Zoiper / Linphone / Jitsi
- SIP : identifiant, mot de passe, IP serveur
- Vérifier les appels, l’audio, les logs sur XiVO Client

### Trames SIP

- `INVITE`, `TRYING`, `RINGING`, `OK`, `ACK`, `BYE`
- Wireshark : filtres `sip`, `rtp`, `udp.port==5060`

---

## ☎️ Fonctions avancées ToIP

### Conférence et groupes

- Services > Conférence : créer salle, attribuer numéro
- Groupes d’appels : affectation utilisateurs + règles horaires

### Filtrage secrétaire

- Appels filtrés selon le poste, redirigés ou supervisés (code `*372`)

### Circuit d’appel – extensions.conf (Asterisk)

```asterisk
[default]
exten => 100,1,Ringing()
exten => 100,2,Wait(4)
exten => 100,3,Goto(menu,s,1)

[menu]
exten => s,1,Background(menu)
exten => 1,1,Goto(accueil,s,1)
exten => 2,1,Goto(support,s,1)
```

### IVR avec GoogleTTS

```bash
apt install perl libwww-perl sox mpg123
wget https://raw.github.com/zaf/asterisk-googletts/master/googletts.agi
```

```asterisk
exten => s,1,agi(googletts.agi,"Bienvenue chez Badlands !",fr,any)
exten => s,2,WaitExten()
```

---

## ✅ À retenir pour les révisions

- Le réseau doit être **segmenté, sécurisé et documenté**
- La **téléphonie IP nécessite une QoS stricte** pour être fiable
- XiVO est une **solution open source complète** pour la ToIP
- Le **fichier extensions.conf** structure toute la logique d’appel

---

## 📌 Bonnes pratiques professionnelles

- Documenter les VLANs, ACL, routes, lignes téléphoniques
- Cloisonner les flux VoIP du reste du trafic
- Appliquer des ACL d’accès à l’interface web d’administration
- Sécuriser les flux SIP avec TLS, les RTP avec SRTP
- Sauvegarder les configurations XiVO avant toute modification
- Analyser régulièrement le trafic SIP/RTP avec Wireshark
- Utiliser un dépôt Git ou Notion pour les scripts `extensions.conf`, configs d’appel, guides internes