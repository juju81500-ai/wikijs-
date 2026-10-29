# Connecter les collaborateurs pour le télétravail
## 📃 Introduction au VPN

Le **VPN** (_Virtual Private Network_) est une technologie permettant de créer une connexion **sécurisée** entre deux points sur un réseau public, le plus souvent **Internet**.

### Rôles principaux :

- Créer un **tunnel sécurisé** pour les données
- **Chiffrer** les communications
- **Authentifier** les utilisateurs

---

## 🔢 Utilité des VPN

- 🔒 **Sécurité** : Protège contre les interceptions et les attaques
- 📡 **Confidentialité** : Masque l'adresse IP et chiffre les données
- 🌐 **Accès à distance** : Permet le télétravail et l'accès aux ressources internes

---

## 🔄 Fonctionnement des VPN

### 1. Tunnelisation

- Création d'un **tunnel chiffré** entre client et serveur

### 2. Chiffrement

- Les données sont **chiffrées** avant envoi et **déchiffrées** à la réception

### 3. Authentification

- L'utilisateur doit **s'authentifier** pour accéder au VPN

---

## 🔄 Avantages des VPN

- 🔒 **Sécurité des données** (contre "man-in-the-middle")
- 📡 **Confidentialité en ligne**
- 🌐 **Accès aux ressources** internes de l'entreprise

---

## 🔢 Types de VPN

|Type|Description|
|---|---|
|VPN d'accès à distance|Pour les particuliers/employés à distance|
|VPN site-à-site|Pour connecter deux réseaux distants|

---

## 🔧 Protocoles et solutions VPN

### PPTP

- Facile à configurer mais **obsolète**

### L2TP/IPSec

- Sécurité renforcée, performances moyennes

### IKEv2/IPSec

- Rapide et résilient (adapté aux mobiles)

### SSTP

- Intégré à Windows, passe les pare-feux

### OpenVPN

- **Open source**, sécurité robuste, très flexible
- Intégration native dans **pfSense**

### WireGuard

- **Protocole moderne**, rapide et léger
- Intégration dans pfSense

---

## 🔧 Configuration OpenVPN sur pfSense

- OpenVPN préinstallé sur pfSense
- Utilisation du package `openvpn-client-export`
- Nécessite un **certificat de confiance** (CA existant ou création)
- Possibilité d'ajouter **authentification LDAP** (comptes AD)
- Assistant pour générer les fichiers de configuration clients

### Règles de pare-feu

- Ouverture automatique des règles nécessaires sur WAN et OpenVPN

### Coté client

- Installation du client OpenVPN + fichiers de configuration

---

## 🔧 Configuration WireGuard sur pfSense

- Protocole moderne **très performant**
- Configuration des **clés privées/publiques**
- Association des pairs (**Peers**)
- Création des règles de pare-feu adaptées

### Coté client Linux

- Clés privée/publique stockées dans `/etc/WireGuard/`
- Configuration via `wg0.conf`
- Service : `wg-quick@wg0`
- Interface virtuelle `wg0` avec l'adresse IP du tunnel

---

## ✅ À retenir pour les révisions

- Un **VPN d’accès à distance** permet aux employés de se connecter de manière sécurisée au réseau de l’entreprise
- Le **VPN** crée un **tunnel chiffré** → garantit **confidentialité**, **intégrité** et **authenticité** des échanges
- Protocoles recommandés pour le télétravail :
    - **OpenVPN** (robuste, flexible, open-source)
    - **WireGuard** (moderne, très performant)
- **pfSense** permet de déployer facilement un serveur OpenVPN ou WireGuard
- Pour OpenVPN :
    - Utilisation du package `openvpn-client-export` pour simplifier le déploiement sur les postes clients
    - Authentification possible via **LDAP / Active Directory**
- La configuration du VPN doit être accompagnée de :
    - **Règles firewall adaptées**
    - **Supervision** des connexions VPN
    - **Journalisation** des accès
- L’usage de **PPTP** est à proscrire (protocole obsolète et non sécurisé)

---

## 📌 Bonnes pratiques professionnelles

- **Privilégier OpenVPN ou WireGuard** pour les connexions modernes
- Utiliser **authentification forte** (certificats, LDAP, 2FA)
- Sécuriser les configurations (règles de pare-feu, journaux, segmentation)
- Documenter les paramètres de tunnel VPN
- Garder les logiciels et protocoles à jour (abandon de PPTP)

---

## ⚠️ Pièges à éviter

- Utiliser des protocoles obsolètes (**PPTP**) ou non chiffrés
- Mauvaise gestion des clés privées / certificats
- Configurer le VPN sans restriction d'accès aux réseaux internes
- Oublier de superviser les connexions VPN
- Laisser des ports inutilisés ouverts

---

## ✅ Commandes utiles (diagnostic VPN)

### OpenVPN (côté pfSense)

```bash
# Vérification des logs OpenVPN
cat /var/log/openvpn.log

# Vérification de l'état des connexions
pfctl -ss | grep openvpn
```

### WireGuard (côté client Linux)

```bash
# Vérifier l'état de WireGuard
sudo wg show

# Lister l'interface virtuelle
ip a show wg0
```