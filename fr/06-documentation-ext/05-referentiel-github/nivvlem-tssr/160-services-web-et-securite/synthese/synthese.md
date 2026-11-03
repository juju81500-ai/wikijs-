---
title: "Synthèse – Services Web et Sécurité (Apache, IIS, PKI, VPN)"
description: "apt install apache2"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# Synthèse – Services Web et Sécurité (Apache, IIS, PKI, VPN)
## 🌐 Serveurs Web : Apache & IIS

### Apache (Linux)

#### Installation

```bash
apt install apache2
systemctl enable apache2 && systemctl start apache2
```

#### Arborescence importante

|Répertoire|Fonction|
|---|---|
|`/var/www/`|Racine des sites|
|`/etc/apache2/sites-available`|Config des vhosts|
|`/etc/apache2/mods-available`|Modules disponibles|
|`/etc/apache2/apache2.conf`|Fichier principal|

#### Gestion des sites (vhosts)

```bash
a2ensite monsite.conf && systemctl reload apache2
```

- Exemple de vhost :

```apache
<VirtualHost *:80>
  DocumentRoot /var/www/monsite
  ServerName monsite.local
</VirtualHost>
```

#### Certificats autosignés (OpenSSL)

```bash
openssl req -x509 -newkey rsa:4096 -nodes -keyout key.pem -out cert.pem -days 365
```

### IIS (Windows Server)

#### Installation

- Ajout du rôle **Serveur Web (IIS)** via le Gestionnaire de serveur
- Page par défaut : `C:\inetpub\wwwroot`

#### Création de sites

- Répertoires personnalisés sur `E:\sites_web`
- Liaison par hôte/IP/port via l’interface IIS Manager

#### Certificats SSL

- Génération d’un certificat autosigné via **Certificats de serveur**
- Liaison HTTPS dans **Modifier les liaisons** du site concerné

---

## 🔐 PKI – Infrastructure de certificats

### AC interne (Active Directory Certificate Services)

#### Installation

- Rôle **ADCS** + Web Enrollment (facultatif)
- AC racine ou subordonnée, entreprise

#### Création de modèles personnalisés

- Dupliquer `Web Server`
- Attribuer droits au poste concerné
- Publier le modèle via `certsrv.msc`

#### Demande et liaison

- Demande de certificat via `certlm.msc` (SRV-IIS)
- Liaison HTTPS dans IIS avec certificat signé → plus d’avertissement navigateur

---

## 🔐 OpenVPN – VPN nomade avec pfSense

### AC + Certificat serveur

- Création via Cert. Manager (pfSense)
- Export client via **openvpn-client-export**

### Intégration Active Directory

- Authentification LDAP (base DN, bind DN, tests)
- Permet l’usage des comptes AD pour l’accès VPN

### Assistant OpenVPN

- Tunnel : `10.0.8.0/24`
- Réseau local à exposer : `192.168.159.0/24`
- DNS : AD-DNS
- Interface WAN + redirection passerelle = tunnel par défaut

### Règles pare-feu

- WAN : autoriser port VPN (ex. 1194 UDP)
- OpenVPN : autoriser trafic vers LAN (ou affiner en prod)

---

## ✅ À retenir pour les révisions

- Apache & IIS : serveurs web configurables, compatibles SSL
- Les **vhosts** (Apache) ou **liaisons** (IIS) permettent l’hébergement multi-sites
- Une PKI permet de signer des certificats valides pour intranet ou public
- pfSense + OpenVPN + LDAP = VPN sécurisé avec intégration Active Directory
- Un certificat autosigné génère une alerte, un certificat signé valide est reconnu automatiquement

---

## 📌 Bonnes pratiques professionnelles

### Apache / IIS

- Ne jamais modifier directement les fichiers par défaut : préférer les duplications
- Isoler chaque site dans un vhost dédié
- Sécuriser les dossiers par `Require ip` ou ACL NTFS

### PKI

- Utiliser **SHA256+** et RSA ≥ 2048 bits
- Documenter chaque certificat émis (poste, durée, usage)
- Superviser les dates d’expiration et mettre en place des alertes

### OpenVPN

- Restreindre l’usage à un **groupe AD dédié**
- Séparer la configuration **client LAN / client nomade**
- Exporter les profils avec mot de passe fort et certificat

---

## 🛠️ Commandes utiles à mémoriser

### Apache

```bash
apache2ctl configtest     # vérifier la configuration
apache2ctl -S             # liste des vhosts
systemctl restart apache2
```

### OpenSSL

```bash
openssl x509 -in cert.crt -noout -text    # lecture d’un certificat
```

### pfSense

- `Diagnostics > Authentication` → test LDAP
- `Status > OpenVPN` → connexions actives