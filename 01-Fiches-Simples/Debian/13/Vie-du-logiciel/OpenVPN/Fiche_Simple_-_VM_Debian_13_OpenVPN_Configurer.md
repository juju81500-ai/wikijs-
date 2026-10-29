# Fiche_Simple_-_VM_Debian_13_OpenVPN_Configurer

- **Environnement** : VM Debian 13 dédiée à OpenVPN Community Edition
- **OS / Version** : Debian 13 Trixie; version des dépôts à vérifier sur l’hôte
- **Catégorie** : OpenVPN Community Edition / configurer
- **Tags** : `openvpn`, `debian13`, `vie-du-logiciel`, `configurer`

---

## Problème précis à résoudre

Configurer un serveur VPN UDP avec certificats, sans publier de routes non approuvées.

## 1. Hors-Production (Lab / Test / POC)

1. Installer les certificats préparés par la PKI approuvée :
   ```bash
   sudo install -d -o root -g root -m 0750 /etc/openvpn/server
   sudo install -o root -g root -m 0644 CA_CERTIFICATE /etc/openvpn/server/ca.crt
   sudo install -o root -g root -m 0644 SERVER_CERTIFICATE /etc/openvpn/server/server.crt
   sudo install -o root -g root -m 0600 SERVER_PRIVATE_KEY /etc/openvpn/server/server.key
   sudo sh -c "umask 077; openvpn --genkey tls-crypt /etc/openvpn/server/tls-crypt.key"
   ```
   👉 Explication : CA_CERTIFICATE, SERVER_CERTIFICATE et SERVER_PRIVATE_KEY sont des chemins à remplacer par les fichiers approuvés; ne jamais copier la clé privée de la CA.

2. Créer la configuration serveur :
   ```bash
   sudoedit /etc/openvpn/server/server.conf
   ```
   Configuration minimale à adapter :
   ```text
   port 1194
   proto udp
   dev tun
   topology subnet
   server VPN_NETWORK VPN_NETMASK
   ca /etc/openvpn/server/ca.crt
   cert /etc/openvpn/server/server.crt
   key /etc/openvpn/server/server.key
   tls-crypt /etc/openvpn/server/tls-crypt.key
   verify-client-cert require
   remote-cert-tls client
   data-ciphers AES-256-GCM:AES-128-GCM
   tls-version-min 1.2
   persist-key
   persist-tun
   verb 3
   ```
   👉 Explication : Remplacer VPN_NETWORK et VPN_NETMASK par le plan validé. La clé tls-crypt est générée sur l’hôte et doit être remise au client par un canal protégé; une CRL reste à ajouter si la procédure de révocation la prévoit.

3. Restreindre les droits :
   ```bash
   sudo chown root:root /etc/openvpn/server/server.conf /etc/openvpn/server/server.key
   sudo chmod 600 /etc/openvpn/server/server.conf /etc/openvpn/server/server.key /etc/openvpn/server/tls-crypt.key
   ```
   👉 Explication : La configuration et la clé serveur ne sont accessibles qu’à root.

## 2. Production — Contrôles

Faire relire routes, réseau VPN, certificat, algorithmes et unité systemd; confirmer les directives avec le manuel de la version installée.

## 3. Production — Sécurité

- Exiger des certificats clients vérifiés et nominatifs; ne pas inscrire de secrets dans les commandes ou tickets.

## Validation et retour arrière

- **Validation** : Configuration approuvée et fichiers protégés; le service n’est pas encore exposé.
- **Retour arrière** : restaurer la configuration antérieure vérifiée et arrêter le service ou la capture si la recette échoue; consigner le changement.

## Si le problème n’est pas résolu

- [OpenVPN Community Edition — documentation officielle](https://openvpn.net/community-resources/)
- [Étape suivante du guide](./Fiche_Simple_-_VM_Debian_13_OpenVPN_Securiser.md)
