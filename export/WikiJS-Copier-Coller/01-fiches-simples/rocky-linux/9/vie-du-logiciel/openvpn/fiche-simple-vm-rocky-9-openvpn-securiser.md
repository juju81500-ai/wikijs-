# Fiche_Simple_-_VM_Rocky_9_OpenVPN_Securiser

- **Environnement** : VM Rocky Linux 9 dédiée à OpenVPN Community Edition (serveur)
- **OS / Version** : Rocky Linux 9; paquets openvpn et easy-rsa issus d'EPEL, version à vérifier
- **Catégorie** : OpenVPN Community Edition / sécuriser

---

## Problème précis à résoudre

Réduire l'exposition du serveur : pare-feu, droits, révocation et journalisation.

## 1. Hors-Production (Lab / Test / POC)

1. Configurer le pare-feu (firewalld) :
   ```bash
   sudo firewall-cmd --permanent --add-port=VPN_UDP_PORT/udp
   sudo firewall-cmd --permanent --add-masquerade
   sudo firewall-cmd --reload
   sudo firewall-cmd --list-all
   ```
   👉 Explication : VPN_UDP_PORT (1194 par défaut) est à remplacer par le port UDP retenu. Le masquerade n'est à ajouter que si le plan réseau impose du NAT; sinon omettre la ligne --add-masquerade et utiliser des routes.

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
- **Retour arrière** : Retirer la règle ajoutée (firewall-cmd --permanent --remove-port=VPN_UDP_PORT/udp puis --reload).

## Si le problème n'est pas résolu

- [Étape suivante du guide](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/openvpn/fiche-simple-vm-rocky-9-openvpn-valider)
- [Fiche d'entrée du logiciel](/01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-openvpn)
- [OpenVPN Community — documentation officielle](https://openvpn.net/community-resources/)
- [OpenVPN — manuel de référence 2.6](https://openvpn.net/community-resources/reference-manual-for-openvpn-2-6/)