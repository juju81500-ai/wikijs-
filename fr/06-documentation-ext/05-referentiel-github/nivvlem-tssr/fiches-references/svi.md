---
title: "SVI (Serveur Vocal Interactif)"
description: "Un Serveur Vocal Interactif (SVI, ou IVR en anglais) est un système téléphonique automatisé qui interagit avec l’appelant via des messages vocaux et une navigation par choix (DTMF). Il permet de diriger les appels entrants vers les bons interlocuteurs ou services (ex : “Tapez 1 pour le support”)."
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# SVI (Serveur Vocal Interactif)

## 📌 Présentation

Un Serveur Vocal Interactif (SVI, ou IVR en anglais) est un **système téléphonique automatisé** qui interagit avec l’appelant via des messages vocaux et une navigation par choix (DTMF). Il permet de **diriger les appels entrants** vers les bons interlocuteurs ou services (ex : “Tapez 1 pour le support”).

Dans un système comme **XiVO**, le SVI se configure via l’interface web ou via des fichiers de configuration Asterisk (`extensions.conf`).

---

## 🧱 Éléments clés d’un SVI
| Élément | Rôle |
|--------|------|
| **Message d’accueil** | Introduction et instructions |
| **Choix DTMF** | Chiffres que l’appelant peut taper (0 à 9, *) |
| **Actions associées** | Redirection, file d’attente, messagerie, autre SVI… |
| **Timeout / Default** | Que faire en cas de non-réponse ou touche invalide |

## 🎛️ Exemple de scénario SVI simple (XiVO / Asterisk)

```asterisk
exten => s,1,Answer()
 same => n,Background(svi/accueil)
 same => n,WaitExten(10)

exten => 1,1,Goto(service-technique,s,1)
exten => 2,1,Goto(service-commercial,s,1)
exten => i,1,Playback(invalid)
 same => n,Goto(s,1)
exten => t,1,Playback(vm-goodbye)
 same => n,Hangup()
```
- `s` : contexte principal
- `1`, `2` : choix de l’utilisateur
- `i` : touche invalide
- `t` : temps écoulé sans réponse

---

## 🧰 Configuration dans XiVO

Dans l’interface web :
1. Aller dans **Services → Répondeurs**
2. Créer un **nouveau SVI** (nom + message audio)
3. Ajouter des **étapes** : choix 1 → groupe technique, choix 2 → groupe commercial…
4. Associer le SVI à un numéro d’appel entrant (dans les règles de routage)

---

## 🔎 Cas d’usage courant

- Filtrage des appels (support, RH, comptabilité…)
- Automatisation des horaires (ex : message différent le week-end)
- Pré-décroché vocal avant mise en attente
- Navigation vers des boîtes vocales ou groupes d'appels

---

## ⚠️ Erreurs fréquentes

- Oublier de gérer les cas `i` (touche invalide) ou `t` (timeout)
- Fichiers audio absents ou mal nommés → blocage à l’accueil
- Mauvaise association entre choix DTMF et actions
- Messages trop longs ou confus → mauvaise UX utilisateur

---

## ✅ Bonnes pratiques

- Utiliser des **messages clairs et courts** (“Tapez 1 pour le support…”) 
- Tester tous les scénarios : réponse correcte, rien tapé, mauvaise touche
- Organiser les SVIs en cascade si besoin, mais éviter trop de niveaux
- Prévoir un chemin vers un interlocuteur humain en cas de doute

---

## 📚 Ressources complémentaires

- `man asterisk`, fichiers audio dans `/usr/share/asterisk/sounds/