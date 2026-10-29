# Fiche_Simple_-_VM_Rocky_9_OpenVPN_Configurer

- **Environnement** : VM Rocky Linux 9 dédiée à OpenVPN Community Edition (serveur)
- **OS / Version** : Rocky Linux 9; paquets openvpn et easy-rsa issus d'EPEL, version à vérifier
- **Catégorie** : OpenVPN Community Edition / configurer

---

## Problème précis à résoudre

Configurer le serveur OpenVPN UDP avec certificats, sans publier de routes non approuvées.

## 1. Hors-Production (Lab / Test / POC)

1. Installer les certificats émis par la PKI approuvée :
   ```bash
   sudo install -d -o root -g root -m 0750 /etc/openvpn/server
   sudo install -o root -g root -m 0644 CA_CERTIFICATE /etc/openvpn/server/ca.crt
   sudo install -o root -g root -m 0644 SERVER_CERTIFICATE /etc/openvpn/server/server.crt
   sudo install -o root -g root -m 0600 SERVER_PRIVATE_KEY /etc/openvpn/server/server.key
   sudo sh -c "umask 077; openvpn --genkey tls-crypt /etc/openvpn/server/tls-crypt.key"
   ```
   👉 Explication : CA_CERTIFICATE, SERVER_CERTIFICATE et SERVER_PRIVATE_KEY sont les chemins des fichiers approuvés (à remplacer); ne jamais copier la clé privée de la CA. La clé tls-crypt est générée localement et remise aux clients par un canal protégé.

2. Créer /etc/openvpn/server/server.conf avec le même contenu que la fiche Debian (le fichier est identique sur toutes les distributions) :
   ```bash
   sudoedit /etc/openvpn/server/server.conf
   ```
   👉 Explication : Reprendre le bloc de [la fiche Debian 13 OpenVPN Configurer](/01-fiches-simples/debian/13/vie-du-logiciel/openvpn/fiche-simple-vm-debian-13-openvpn-configurer) et remplacer VPN_NETWORK, VPN_NETMASK et le port par le plan validé; vérifier les directives dans le manuel de la version installée.

3. Appliquer les contextes SELinux sur les fichiers :
   ```bash
   sudo restorecon -Rv /etc/openvpn/server
   ls -Z /etc/openvpn/server
   ```
   👉 Explication : SELinux reste en mode Enforcing; si l'étiquetage est incorrect, restorecon le corrige. Ne pas passer SELinux en permissive pour contourner un refus.

4. Si le serveur doit router vers un réseau interne, activer le routage IPv4 de façon persistante :
   ```bash
   echo 'net.ipv4.ip_forward=1' | sudo tee /etc/sysctl.d/99-openvpn.conf
   sudo sysctl --system
   ```
   👉 Explication : À faire uniquement si le plan réseau prévoit le routage; ajouter ensuite dans server.conf la directive push "route RESEAU_INTERNE MASQUE_INTERNE" (valeurs à remplacer par le réseau approuvé).

## 2. Production — Contrôles

Faire relire routes, réseau du tunnel, algorithmes et unité; confirmer chaque directive avec le manuel de la version installée.

## 3. Production — Sécurité

- Exiger des certificats clients nominatifs; aucun secret dans les commandes, tickets ou captures.

## Validation et retour arrière

- **Validation** : Les fichiers sont en place avec les bons droits (clé en 0600) et le service n'est pas encore exposé.
- **Retour arrière** : Supprimer /etc/openvpn/server/server.conf et les clés copiées, ou restaurer la sauvegarde antérieure.

## Si le problème n'est pas résolu

- [Étape suivante du guide](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/openvpn/fiche-simple-vm-rocky-9-openvpn-securiser)
- [Fiche d'entrée du logiciel](/01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-openvpn)
- [OpenVPN Community — documentation officielle](https://openvpn.net/community-resources/)
- [OpenVPN — manuel de référence 2.6](https://openvpn.net/community-resources/reference-manual-for-openvpn-2-6/)