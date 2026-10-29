---
title: "Sécuriser la navigation internet"
description: "Le proxy est un composant intermédiaire entre les clients internes et Internet."
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# Sécuriser la navigation internet
## 📃 Introduction : Le proxy

Le **proxy** est un composant intermédiaire entre les clients internes et Internet.

### Rôles principaux :

- **Filtrer l'accès** aux sites dangereux ou indésirables (blacklists)
- **Ajouter une couche de sécurité** contre les menaces externes et les usages malveillants en interne
- **Optimiser la bande passante** par la mise en cache
- **Enregistrer l'activité des utilisateurs** (logs)

### Obligations légales en France :

- Conservation des **logs d'accès pendant 1 an**
- Article **L34-1 du Code des postes et des communications électroniques**
- Article 9 de la **LCEN** (Loi pour la Confiance dans l'Économie Numérique) du 21 juin 2004

---

## 🔢 Fonctionnement du proxy

- **Mise en cache** des ressources demandées pour accélérer les accès futurs
- **Transparence** pour les utilisateurs
- Contrôle et journalisation par les administrateurs réseau

---

## 🛠️ Squid Proxy

**Squid** est un serveur **proxy** et **reverse proxy** open-source.

### Fonctionnalités :

- Gère les protocoles **FTP, HTTP, HTTPS, Gopher**
- Moteur performant en **I/O asynchrone**
- Mise en **cache des contenus web**
- Peut agir comme intermédiaire entre clients et serveurs internes
- Large communauté, configurations multiples (filtrage, authentification, etc.)

### Configuration typique sous pfSense :

- **Taille du cache disque** : ex. 1 Go (1024 Mo)
- **Interface écoutée** : LANCLIENT
- **Port par défaut** : 3128
- **Filtrage SSL/TLS** sur port 3129
- **Logging activé**

---

## 🔧 SquidGuard Proxy

**SquidGuard** est un module de **filtrage d'URL** pour Squid.

### Fonctionnalités :

- Utilisation de **blacklists** catégorisées (sites indésirables)
- Exemples : pornographie, jeux d'argent, réseaux sociaux
- Filtrage sur **adresses IP en URL**
- Activation de **SafeSearch** sur les moteurs de recherche
- Création de blacklists personnalisées
- Application de **règles par catégorie** (Allow / Deny)

### Blacklist recommandée :

- [https://dsi.ut-capitole.fr/blacklists/download/](https://dsi.ut-capitole.fr/blacklists/download/)

---

## 🛏️ Portail Captif

### Définition :

Un **portail captif** est une page d'authentification obligatoire avant d'accéder au réseau.

### Fonctionnement :

1. Connexion à un réseau Wi-Fi
2. Redirection vers la page du portail captif
3. Interaction utilisateur (acceptation, authentification)
4. Accès accordé au réseau

### Cas d'usage :

- **Hôtels**
- **Cafés**
- **Écoles / universités**
- **Entreprises** (pour les **invités**, le **proxy** reste préférable pour les employés)

### Remarque :

- Pas de démonstration dans le cours → à faire en **bonus**.

---

## ✅ À retenir pour les révisions

- Un **proxy** agit comme **intermédiaire** entre les clients et Internet
- Il permet de :
    - **Filtrer** l’accès aux sites web (via **blacklists**)
    - **Journaliser** les activités des utilisateurs
    - **Optimiser la bande passante** par la mise en cache
- En France, la **conservation des logs** d’accès Internet est **obligatoire pendant 1 an**
- **Squid** est un proxy open-source couramment utilisé, intégrable dans pfSense
- **SquidGuard** permet de **filtrer les URL** par catégories (pornographie, réseaux sociaux, etc.)
- Un **portail captif** permet de contrôler l’accès au réseau (souvent utilisé pour les visiteurs)
- Le filtrage HTTPS nécessite une **inspection SSL** correctement paramétrée pour éviter de casser les sites sécurisés
- La configuration des **logs**, des **blacklists** et des **droits d’accès** doit être soigneusement maintenue

---

## 📌 Bonnes pratiques professionnelles

- **Activer les logs** et respecter les obligations de conservation
- **Filtrer par catégorie** les accès web
- **Mettre à jour régulièrement** les blacklists
- **Limiter les risques SSL** avec l'inspection contrôlée
- Différencier les usages : proxy pour les employés, portail captif pour les visiteurs
- Bien configurer les **droits d'accès**

---

### ⚠️ Pièges à éviter

- Ne pas conserver les logs (risque juridique)
- Mal configurer le filtrage SSL (risque de casse HTTPS)
- Filtrage trop permissif (blacklists incomplètes)
- Exposer un portail captif sans authentification / supervision

---

### ✅ Commandes utiles (diagnostic proxy / filtrage)

#### Sur pfSense / Squid

```bash
# Vérification de l'état de Squid
ps aux | grep squid

# Vérification des logs Squid
cat /var/squid/logs/access.log

# Vérification des logs SquidGuard
cat /var/squidGuard/log/squidGuard.log

# Test de connexion via proxy
curl -x http://ip_proxy:3128 http://www.example.com
```

#### Depuis un poste client

```bash
# Test de navigation HTTP/HTTPS via proxy
curl -I http://site_test
curl -I https://site_test

# Analyse du filtrage
nmap -p 3128,3129 ip_proxy
```