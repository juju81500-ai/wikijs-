---
title: "TP – XiVO, ToIP, Analyse SIP, Circuit d’appel & IVR"
description: "Réaliser une mise en œuvre complète d’un système de téléphonie sur IP (ToIP) avec XiVO :"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# TP – XiVO, ToIP, Analyse SIP, Circuit d’appel & IVR

## 🧠 Objectif

Réaliser une mise en œuvre complète d’un système de téléphonie sur IP (ToIP) avec **XiVO** :

- Installation et configuration serveur
- Création des utilisateurs et lignes
- Tests softphones
- Analyse des trames SIP/RTP avec Wireshark
- Création de groupes, conférence, filtrage secrétaire
- Configuration de l’IVR avec synthèse vocale

---

## 🧾 Prérequis et installation XiVO

### 1. Préparation de la VM

- Processeur : **1 vCPU minimum**, idéalement 2 vCPU
- RAM : **2 Go** (minimum requis)
- Disque dur : **20 Go**
- Accès Internet obligatoire pour télécharger les paquets nécessaires
- Réseau : interface VoIP configurée sur un réseau `/24`, exemple : `192.168.0.0/24`

### 2. Téléchargement et installation

- Récupérer l’ISO officielle
- Démarrer la VM avec l’ISO
- Suivre l’assistant d’installation Debian
- Une fois installé, mettre à jour le système :

```bash
apt update && apt dist-upgrade -y
```

### 3. Configuration réseau

- Modifier l’interface réseau dans `/etc/network/interfaces` :

```bash
iface eth0 inet static
 address 192.168.0.1/30
 gateway 192.168.0.2
```

- Relancer le service réseau :

```bash
systemctl restart networking
```

- S’assurer que l’interface est UP :

```bash
ip addr show eth0
```

### 4. Accès Web et configuration initiale

- Depuis un navigateur : `http://192.168.0.1`
- Choisir la langue
- Saisir les paramètres :
    - Nom du serveur : XiVO
    - Domaine fictif : xivo.local
    - Adresse IP du serveur + passerelle : 192.168.0.1 / 192.168.0.2
    - Serveur DNS : celui de la box ou Google (8.8.8.8)
    - Mot de passe admin Web
    - Entité : Badlands, plage 100–200

---

## 👥 Création des utilisateurs et lignes

### 5. Ajouter des utilisateurs

- Aller dans **Utilisateurs > Ajouter**
- Créer 3 utilisateurs :
    - `Geralt Deriv` (101)
    - `Yennefer Vengerberg` (102)
    - `Triss Merigold` (103)
- Renseigner prénom, nom, langue, fuseau horaire
- Associer une ligne dans l’onglet _Ligne SIP_

### 6. Paramétrer les softphones

- Ouvrir Zoiper / Linphone / Jitsi
- Paramètres SIP :
    - Identifiant : `login SIP XiVO`
    - Mot de passe : récupéré dans l’onglet Ligne
    - Serveur : `192.168.0.1`

### 7. Tester les appels

- 101 appelle 102 → Décroché et conversation
- 102 appelle 103 → Vérification de la connexion bidirectionnelle
- Vérifier les logs sur le XiVO Client ou interface web

---

## 🧪 Analyse des trames SIP/RTP avec Wireshark

### 8. Lancer Wireshark sur l’hôte

- Filtres utiles : `sip`, `rtp`, `udp.port==5060`

### 9. Passer un appel et capturer :

- Séquence SIP : `INVITE → TRYING → RINGING → OK → ACK → BYE`
- Flux RTP : 2 canaux (un par direction)
- Vérifier latence, jitter, codec utilisé

---

## 🧾 Configuration avancée XiVO

### 10. Import CSV d’utilisateurs

- Export existants en CSV → modifier le fichier
- Supprimer les champs inutiles (provisioning, codes internes)
- Réimport depuis l’interface web

### 11. Création de groupes

- Groupes : _accueil (201)_, _support (202)_, _communication (203)_
- Ajouter utilisateurs aux groupes
- Affecter musiques d’attente, règles horaires

### 12. Chambre de conférence

- Aller dans **Services > Conférences**
- Créer _Afterlife_, poste 301, accès libre

### 13. Filtrage secrétaire

- Hanako Arasaka = directrice, Evelyn Parker = secrétaire
- Accès aux appels : via préfixe + association dans _Filtres_
- Activation via code : `*372`

---

## ☎️ Configuration d’un circuit d’appel (extensions.conf)

### 14. Accéder au fichier Asterisk

```bash
vim /etc/asterisk/extensions.conf
```

### 15. Configuration

```asterisk
[default]
exten => 100,1,Ringing()
exten => 100,2,Wait(4)
exten => 100,3,Goto(accueil,s,1)

[accueil]
exten => s,1,SetGlobalVar(sounds_path=/var/asterisk/sounds/)
exten => s,2,Background(${sounds_path}welcome)
exten => #,1,Goto(menu,s,1)
exten => i,1,Playback(${sounds_path}erreur-saisie)
exten => t,1,Goto(accueil,s,1)

[menu]
exten => s,1,Background(${sounds_path}menu)
exten => 1,1,Goto(appel,s,1)
exten => 2,1,Goto(message,s,1)
exten => 3,1,Goto(support,s,1)
```

---

## 🔊 IVR avec synthèse vocale GoogleTTS

### 16. Installer GoogleTTS

```bash
apt install perl libwww-perl sox mpg123
cd /usr/share/asterisk/agi-bin/
wget https://raw.github.com/zaf/asterisk-googletts/master/googletts.agi
chmod 755 googletts.agi
```

### 17. Fichier final [ivr]

```asterisk
[ivr]
exten => s,1,Answer()
exten => s,2,Set(TIMEOUT(response)=20)
exten => s,3,agi(googletts.agi,"Bonjour et bienvenue chez Arasaka I",fr,any)
exten => s,4,agi(googletts.agi,"Pour joindre l'accueil, tapez 1.",fr,any)
exten => s,5,agi(googletts.agi,"Pour joindre le service technique, tapez 2.",fr,any)
exten => s,6,agi(googletts.agi,"Pour joindre le service communication, tapez 3.",fr,any)
exten => s,7,agi(googletts.agi,"Pour joindre le service administratif, tapez 4.",fr,any)
exten => s,8,agi(googletts.agi,"Pour joindre madame Hanako Arasaka, tapez 5.",fr,any)
exten => s,9,WaitExten()

; ######## CHOIX 1 : Accueil ########
exten => 1,1,SayNumber(1)
exten => 1,2,Goto(default,201,1)

; ######## CHOIX 2 : Service Technique ########
exten => 2,1,SayNumber(2)
exten => 2,2,Goto(default,200,1)

; ######## CHOIX 3 : Service Communication ########
exten => 3,1,SayNumber(3)
exten => 3,2,Goto(default,202,1)

; ######## CHOIX 4 : Service Administratif ########
exten => 4,1,SayNumber(4)
exten => 4,2,Goto(default,203,1)

; ######## CHOIX 5 : Madame Hanako Arasaka ########
exten => 5,1,SayNumber(5)
exten => 5,2,Goto(default,105,1)

; ######## CHOIX INVALIDE ########
exten => _[06-9*#],1,NoOp(Caractère invalide pressé : ${EXTEN})
exten => _[06-9*#],2,GotoIf($["${EXTEN}"="*"]?say_star)
exten => _[06-9*#],3,GotoIf($["${EXTEN}"="#"]?say_hash)
exten => _[06-9*#],4,SayNumber(${EXTEN})
exten => _[06-9*#],5,Goto(ivr,say_invalid)

; Dire "étoile" pour *
exten => say_star,1,agi(googletts.agi,"étoile",fr,any)
exten => say_star,2,Goto(ivr,say_invalid)

; Dire "dièse" pour #
exten => say_hash,1,agi(googletts.agi,"dièse",fr,any)
exten => say_hash,2,Goto(ivr,say_invalid)

; Dire "Entrée invalide" et rediriger
exten => say_invalid,1,agi(googletts.agi,"Entrée invalide",fr,any)
exten => say_invalid,2,Goto(ivr,s,1)

; ######## TIMEOUT ########
exten => t,1,Goto(ivr,s,3)
```

> Tester en DTMF (RFC2833) depuis le softphone

---

## ✅ À retenir pour les révisions

- Un serveur XiVO permet une **téléphonie IP d’entreprise complète**
- Le **fichier extensions.conf** est au cœur de la logique d’appel
- L’analyse **SIP/RTP** permet de diagnostiquer la ToIP (Wireshark)
- **GoogleTTS** peut enrichir l’expérience utilisateur
- Les tests doivent valider tous les scénarios : appels directs, groupes, conférence, IVR

---

## 📌 Bonnes pratiques professionnelles

- Faire un **instantané de la VM** avant chaque manipulation majeure
- **Nommer clairement** les entités, contextes, utilisateurs, lignes
- Vérifier **l’enregistrement SIP** des softphones avant test
- Garder les configs **documentées** dans Git ou Notion
- Implémenter le **chiffrement TLS/SRTP** pour les flux SIP/RTP en production