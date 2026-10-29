---
title: "Gestion des PKI (Public Key Infrastructure)"
description: "- Fichier contenant : clé publique, nom du sujet, période de validité, signature de l’AC"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# Gestion des PKI (Public Key Infrastructure)
## 🔐 Définitions fondamentales

### Certificat numérique

- Fichier contenant : clé publique, nom du sujet, période de validité, signature de l’AC
- But : authentifier l’émetteur, garantir l’intégrité, sécuriser les échanges

### AC (Autorité de Certification)

- Entité de confiance qui signe les certificats (ex : DigiCert, Let's Encrypt ou interne)
- Elle valide l’identité du demandeur avant émission

### Types d’autorités internes

|Type|Description|
|---|---|
|**Root CA**|Racine de confiance, souvent hors-ligne|
|**Subordinate CA**|Déléguée par la racine, délivre les certificats|

### Rôle de la PKI

- Fournir les services : **authentification**, **chiffrement**, **signature numérique**, **gestion du cycle de vie des certificats**

---

## 🔧 Installation d'une AC interne sous Windows Server

### Ajout du rôle ADCS

- Ouvrir **Gestionnaire de serveur > Ajouter des rôles**
- Sélectionner **Services de certificats Active Directory** (ADCS)
- Ajouter les fonctionnalités requises

### Sélection des services ADCS

- **Autorité de certification** (obligatoire)
- (Facultatif selon besoin) : Web Enrollment, Online Responder

### Configuration de l’AC

- Type : **Autorité d’entreprise** (intégrée à l’AD)
- Rôle : **Autorité de certification racine** (ou subordonnée si déjà une CA racine)
- Clé : RSA 2048+ bits, SHA256
- Nom commun : `SRV-CA.domaine.tld`

### Définition des paramètres

- Validité : 5 ans (ou plus selon politique interne)
- Emplacement base de données : laisser par défaut ou personnaliser

### Vérifications

- Console : **Certification Authority** → vérifier le service et les modèles de certificats disponibles

---

## 📥 Délivrance d’un certificat serveur Web (HTTPS)

### Depuis IIS (SRV-IIS)

- Ouvrir IIS Manager > **Certificats de serveur** > **Créer une demande de certificat**
- Remplir : nom commun, organisation, unité, ville, pays
- Générer un **fichier CSR** (`.req`)

### Sur l’AC (SRV-CA)

- Ouvrir la console d’AC → clic droit **Soumettre une nouvelle demande**
- Choisir le fichier CSR
- Une fois signé, exporter le **certificat émis**

### Retour sur IIS

- Importer le certificat signé (`.cer`) dans IIS
- Lier ce certificat au site HTTPS dans **liaisons > https**

---

## 📜 Gestion des modèles de certificats

- Console : **certsrv.msc > Modèles de certificats**
- Modifier ou dupliquer un modèle existant (ex : Web Server, User, Smartcard)
- Personnaliser : durée, types de clefs, habilitations, publication

---

## 🔁 Cycle de vie des certificats

### Étapes principales

1. Création d’une **clé privée/publique** par le demandeur
2. Création d’une **demande (CSR)**
3. Signature de la demande par l’AC (certificat émis)
4. Installation du certificat
5. Suivi et **renouvellement** ou **révocation** avant expiration

### Révocation

- Liste CRL (Certificate Revocation List) : publiée régulièrement
- OCSP (Online Certificate Status Protocol) : méthode dynamique de vérification

---

## 🔐 Accès client au portail Web (optionnel)

- Installation de **Web Enrollment** (ADCS Web)** : permet aux utilisateurs de demander ou récupérer des certificats via une interface web : `http://SRV-CA/certsrv`

---

## ✅ À retenir pour les révisions

- Une PKI est un **système de gestion de certificats** : émission, validation, révocation
- Une AC **signe des certificats** pour authentifier des serveurs, utilisateurs, services
- IIS peut générer une demande CSR, à signer via une AC
- Le cycle de vie doit être suivi pour éviter les **certificats expirés ou compromis**

---

## 📌 Bonnes pratiques professionnelles

- Toujours utiliser des **clés RSA ≥ 2048 bits** et SHA256 ou plus
- Protéger l’accès à la **CA racine** (hors ligne, sauvegardée)
- Documenter chaque certificat émis (nom, date, usage, durée, CA utilisée)
- Automatiser le **renouvellement** via scripts ou GPO
- Privilégier l’usage de **modèles de certificats** adaptés à chaque rôle
- Mettre en place un système de **supervision de l’expiration des certificats**