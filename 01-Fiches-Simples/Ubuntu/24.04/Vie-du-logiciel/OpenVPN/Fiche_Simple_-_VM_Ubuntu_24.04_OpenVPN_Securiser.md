# Fiche_Simple_-_VM_Ubuntu_24.04_OpenVPN_Securiser

- **Environnement** : VM Ubuntu 24.04 dédiée à OpenVPN Community Edition (serveur)
- **OS / Version** : Ubuntu 24.04 LTS Noble; version des dépôts à vérifier sur l'hôte
- **Catégorie** : OpenVPN Community Edition / sécuriser
- **Tags** : `openvpn`, `ubuntu24-04`, `vie-du-logiciel`, `securiser`

---

## Problème précis à résoudre

Réduire l'exposition du serveur : pare-feu, droits, révocation et journalisation.

## 1. Hors-Production (Lab / Test / POC)

1. Configurer le pare-feu (ufw) :
   ```bash
   sudo ufw allow from ADMIN_NETWORK to any port 22 proto tcp
   sudo ufw allow VPN_UDP_PORT/udp
   sudo ufw enable
   sudo ufw status verbose
   ```
   👉 Explication : Autoriser SSH depuis le réseau d'administration (ADMIN_NETWORK, à remplacer par le CIDR approuvé) AVANT d'activer ufw pour ne pas perdre l'accès; VPN_UDP_PORT (1194 par défaut) est le port UDP du serveur.

2. Vérifier les droits des secrets :
   ```bash
   sudo ls -l /etc/openvpn/server
   sudo find /etc/openvpn/server -name '*.key' ! -perm 600
   ```
   👉 Explication : Aucune clé ne doit sortir de la commande find (toutes en 0600).

3. Activer la révocation : installer la CRL générée par la PKI hors ligne puis la déclarer dans server.conf :
   ```bash
   sudo install -o root -g root -m 0644 CRL_FICHIER /etc/openvpn/server/crl.pem
   sudoedit /etc/openvpn/server/server.conf   # ajouter : crl-verify /etc/openvpn/server/crl.pem
   ```
   👉 Explication : CRL_FICHIER est la CRL émise par la CA (à remplacer). Prévoir un renouvellement avant son expiration.

## 2. Production — Contrôles

Restreindre l'accès SSH au réseau d'administration; centraliser les journaux (journalctl -u openvpn-server@server).

## 3. Production — Sécurité

- Exposer uniquement le port UDP VPN; révoquer immédiatement tout certificat perdu ou lié à un départ.

## Validation et retour arrière

- **Validation** : Seul le port VPN est ouvert depuis l'extérieur et la CRL est chargée.
- **Retour arrière** : Retirer la règle ajoutée (sudo ufw delete allow VPN_UDP_PORT/udp).

## Si le problème n'est pas résolu

- [Étape suivante du guide](./Fiche_Simple_-_VM_Ubuntu_24.04_OpenVPN_Valider.md)
- [Fiche d'entrée du logiciel](../../../../Logiciels/04-Reseau-et-cybersecurite/Fiche_Logiciel_-_OpenVPN.md)
- [OpenVPN Community — documentation officielle](https://openvpn.net/community-resources/)
- [OpenVPN — manuel de référence 2.6](https://openvpn.net/community-resources/reference-manual-for-openvpn-2-6/)
