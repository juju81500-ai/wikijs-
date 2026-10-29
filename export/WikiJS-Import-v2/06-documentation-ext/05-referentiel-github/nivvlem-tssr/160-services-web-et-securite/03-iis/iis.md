---
title: "Installation, configuration et utilisation de IIS (Internet Information Services)"
description: "- Système : Windows Server 2019 (ou 2022)"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# Installation, configuration et utilisation de IIS (Internet Information Services)
## 🧱 Prérequis et environnement

- Système : Windows Server 2019 (ou 2022)
- Rôle IIS installé via le Gestionnaire de serveur
- Interface Web : **IIS Manager**

---

## 🛠️ Installation du rôle IIS

### Ouvrir le Gestionnaire de serveur

- Cliquer sur **Gérer > Ajouter des rôles et fonctionnalités**
- Sélectionner **Installation basée sur un rôle ou une fonctionnalité**

### Choisir les options suivantes

- Rôle : **Serveur Web (IIS)**
- Ajouter les **fonctionnalités** recommandées (gestion web, compatibilité avec les versions précédentes, compression, etc.)

### Finaliser l’installation

- Redémarrer si nécessaire
- Vérifier l’accès : `http://localhost` depuis le serveur

---

## 🌐 Gestion de sites dans IIS

### Répertoire racine par défaut

- `C:\inetpub\wwwroot`
- Page d’accueil accessible via navigateur

### Création d’un nouveau site

- Ouvrir **IIS Manager**
- Clic droit sur **Sites > Ajouter un site Web**
- Nom du site : `SiteTestIIS`
- Répertoire physique : créer un dossier ex. `C:\inetpub\SiteTestIIS`
- Port : 81 (si 80 déjà utilisé)
- IP : laisser par défaut ou attribuer une IP spécifique
- Lancer le site : navigateur `http://localhost:81`

---

## 📄 Gérer le contenu du site

- Ajouter un fichier `index.html` dans le dossier `C:\inetpub\SiteTestIIS`
- Autoriser l’affichage de fichiers par défaut (si besoin)

---

## 🧩 Fonctions supplémentaires d’IIS

### Répertoires virtuels

- Utilisés pour **mapper un dossier externe** à une URL
- Dans IIS : clic droit sur site > **Ajouter un répertoire virtuel**

### Journaux (Logs)

- Par défaut dans `C:\inetpub\logs\LogFiles`
- Format configurable (W3C, binaire, etc.)
- Rotation quotidienne possible

### Compression

- Active la **compression statique et dynamique** pour les contenus web
- Gain de bande passante

---

## 🔒 Activation de HTTPS

### Générer un certificat autosigné

- IIS Manager > serveur racine > **Certificats de serveur**
- Créer un certificat autosigné : nom = `IIS-SSL-Test`

### Attribuer le certificat au site

- Clic droit sur le site > **Modifier les liaisons** > Ajouter liaison HTTPS
- Port : 443, Certificat : sélectionner `IIS-SSL-Test`

### Tester l’accès sécurisé

- Navigateur : `https://localhost`
- Avertissement attendu : certificat non reconnu, mais connexion chiffrée

---

## ✅ À retenir pour les révisions

- IIS est une **alternative Windows à Apache** pour l’hébergement web
- L’interface IIS Manager permet de **créer, démarrer, configurer** des sites web
- HTTPS nécessite un **certificat**, même autosigné
- Les fonctionnalités comme les **répertoires virtuels, les logs et la compression** sont configurables finement

---

## 📌 Bonnes pratiques professionnelles

- Toujours définir des ports clairs pour chaque site (si multi-sites)
- Utiliser **des noms explicites** pour les sites, dossiers, certificats
- Mettre les sites dans des répertoires **hors `wwwroot`** pour plus de lisibilité
- Activer **les journaux** pour tout site en production
- Sécuriser les communications par **certificat Let’s Encrypt** ou ADCS en interne
- Restreindre les IP ou plages d’adresses si besoin via **liens IP et restrictions IIS**