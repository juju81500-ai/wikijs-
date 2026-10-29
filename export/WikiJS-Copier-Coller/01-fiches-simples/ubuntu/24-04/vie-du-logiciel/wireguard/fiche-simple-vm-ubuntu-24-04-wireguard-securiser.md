# Fiche_Simple_-_VM_Ubuntu_24.04_WireGuard_Securiser

- **Environnement** : VM Ubuntu 24.04 dédiée à un serveur WireGuard natif
- **OS / Version** : Ubuntu 24.04 LTS Noble; noyau avec module WireGuard et paquet wireguard, versions à vérifier
- **Catégorie** : WireGuard natif / sécuriser

---

## Problème précis à résoudre

Réduire l'exposition du serveur WireGuard.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir seulement le port UDP VPN (ufw) :
   ```bash
   sudo ufw allow from ADMIN_NETWORK to any port 22 proto tcp
   sudo ufw allow VPN_UDP_PORT/udp
   sudo ufw enable
   sudo ufw status verbose
   ```
   👉 Explication : ADMIN_NETWORK (CIDR d'administration) et VPN_UDP_PORT (port UDP du serveur) sont à remplacer; autoriser SSH avant d'activer ufw.

2. Activer le routage uniquement si le serveur doit joindre un réseau interne :
   ```bash
   echo 'net.ipv4.ip_forward=1' | sudo tee /etc/sysctl.d/99-wireguard.conf
   sudo sysctl --system
   ```
   👉 Explication : Ajouter ensuite des règles de pare-feu limitant les destinations autorisées; ne pas router sans plan approuvé.

3. Contrôler les droits :
   ```bash
   sudo ls -l /etc/wireguard
   ```
   👉 Explication : server.key et wg0.conf doivent être en 0600, propriétaire root.

## 2. Production — Contrôles

Restreindre SSH au réseau d'administration; prévoir la rotation des clés d'un pair compromis (retrait du bloc Peer puis rechargement).

## 3. Production — Sécurité

- Retirer tout pair perdu ou sorti immédiatement : c'est la seule révocation possible.

## Validation et retour arrière

- **Validation** : Seul le port UDP VPN est ouvert; droits conformes.
- **Retour arrière** : sudo ufw delete allow VPN_UDP_PORT/udp

## Si le problème n'est pas résolu

- [Étape suivante du guide](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/wireguard/fiche-simple-vm-ubuntu-24-04-wireguard-valider)
- [Fiche d'entrée du logiciel](/01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-wireguard)
- [WireGuard — installation officielle](https://www.wireguard.com/install/)
- [WireGuard — démarrage rapide](https://www.wireguard.com/quickstart/)