# 📄 ISC DHCP Server

- **Environnement** : VM (Debian 12)
- **OS / Version** : Debian 12 (bookworm)
- **Version** : ISC DHCP 4.4.3 (paquet des dépôts Debian 12, à vérifier sur la version déployée)
- **Catégorie** : Systèmes, annuaires et services

## 🎯 Problème précis à résoudre
Installer un serveur DHCP ISC (`dhcpd`) sur Debian 12 pour distribuer des baux sur un sous-réseau de test, vérifier qu'un client obtient bien une adresse, puis le durcir (réservations fixes, pare-feu restreint). ISC DHCP est en fin de vie : pour un nouveau déploiement, privilégier Kea (voir la fiche Kea du pack). Cette fiche sert à maintenir ou évaluer un existant.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation du serveur DHCP ISC :
```bash
sudo apt update
sudo apt install -y isc-dhcp-server
dpkg -s isc-dhcp-server | grep -E '^(Version|Status)'
```
👉 Explication : Installe le paquet `isc-dhcp-server` depuis les dépôts Debian 12. La seconde commande affiche la version et l'état d'installation.

2. Choix de l'interface d'écoute (exemple : `ens19`, interface du réseau de test) :
```bash
ip -br addr
sudo nano /etc/default/isc-dhcp-server
```
Dans le fichier, régler la ligne suivante :
```
INTERFACESv4="ens19"
```
👉 Explication : `ip -br addr` liste les interfaces. `INTERFACESv4` indique à `dhcpd` sur quelle interface répondre aux demandes IPv4. Sans cette ligne, le service ne démarre pas correctement.

3. Déclaration du sous-réseau et de la plage d'adresses :
```bash
sudo nano /etc/dhcp/dhcpd.conf
```
Contenu minimal :
```
authoritative;
default-lease-time 3600;
max-lease-time 7200;
subnet 192.168.10.0 netmask 255.255.255.0 {
    range 192.168.10.100 192.168.10.199;
    option routers 192.168.10.1;
    option domain-name-servers 192.168.10.10;
    option domain-name "lab.local";
}
```
👉 Explication : `authoritative` indique que ce serveur fait autorité sur le sous-réseau. La plage `192.168.10.100` à `192.168.10.199` est distribuée aux clients. `routers` donne la passerelle, `domain-name-servers` le serveur DNS. Adapter ces valeurs au réseau de test.

4. Vérification de la syntaxe puis démarrage :
```bash
sudo dhcpd -t -cf /etc/dhcp/dhcpd.conf
sudo systemctl restart isc-dhcp-server
systemctl status isc-dhcp-server --no-pager
```
👉 Explication : `dhcpd -t` contrôle la configuration sans démarrer le service. La ligne `Active: active (running)` est attendue dans la sortie de `status`.

5. Contrôle des baux accordés depuis un client de test :
```bash
sudo cat /var/lib/dhcp/dhcpd.leases
sudo journalctl -u isc-dhcp-server -n 50 --no-pager
```
Sur un client Debian de test, renouveler le bail :
```bash
sudo dhclient -r ens19
sudo dhclient -v ens19
ip -4 addr show ens19
```
👉 Explication : Le fichier `dhcpd.leases` liste les baux (adresse, adresse MAC, date d'expiration). `journalctl` affiche les messages `DHCPDISCOVER`, `DHCPOFFER`, `DHCPACK`. Côté client, `dhclient` libère puis redemande une adresse, et `ip` confirme l'adresse obtenue dans la plage.

---

## ⚡ 2. Production — Façon Simplifiée
1. Réservation d'une adresse fixe pour un poste identifié par son adresse MAC :
```bash
sudo nano /etc/dhcp/dhcpd.conf
```
Ajouter ce bloc dans le fichier, en remplaçant la MAC par celle du poste :
```
host poste-compta01 {
    hardware ethernet 00:50:56:aa:bb:cc;
    fixed-address 192.168.10.50;
}
```
👉 Explication : Le nom `poste-compta01` est un libellé libre. L'adresse MAC se relève sur le poste (`ip link` ou l'étiquette de la carte). `fixed-address` est une adresse hors plage distribuée dynamiquement.

2. Contrôle et redémarrage :
```bash
sudo dhcpd -t -cf /etc/dhcp/dhcpd.conf
sudo systemctl restart isc-dhcp-server
systemctl status isc-dhcp-server --no-pager
```
👉 Explication : Vérifie la syntaxe avant de relancer le service. Une erreur de syntaxe bloque le redémarrage, il faut la corriger avant de continuer.

3. Ouverture du pare-feu : DHCP est écouté sur le port UDP 67 et le client émet depuis `0.0.0.0`, donc la règle filtre sur l'interface et le port, pas sur une adresse source :
```bash
sudo apt install -y ufw
sudo ufw allow from 192.168.10.0/24 to any port 22 proto tcp
sudo ufw allow in on ens19 to any port 67 proto udp
sudo ufw enable
sudo ufw status verbose
```
👉 Explication : SSH est autorisé depuis le sous-réseau d'administration avant l'activation, pour éviter de se couper l'accès. La règle DHCP n'accepte que l'interface `ens19`. Vérifier que le sous-réseau `192.168.10.0/24` correspond bien à l'administration réelle.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Désactivation des mises à jour DNS dynamiques si elles ne sont pas utilisées :
```bash
sudo nano /etc/dhcp/dhcpd.conf
sudo dhcpd -t -cf /etc/dhcp/dhcpd.conf
```
Ajouter en tête de fichier :
```
ddns-update-style none;
```
👉 Explication : Empêche le serveur de modifier une zone DNS à la place des clients. À n'activer qu'en connaissance de cause si une intégration DDNS existe.

2. Droits sur les fichiers de configuration et de baux :
```bash
sudo chown root:root /etc/dhcp/dhcpd.conf
sudo chmod 644 /etc/dhcp/dhcpd.conf
ls -l /etc/dhcp/dhcpd.conf /var/lib/dhcp/dhcpd.leases
```
👉 Explication : Seul `root` modifie la configuration. Le fichier de baux est géré par le service : ne pas le modifier à la main pendant que le service tourne.

3. Journalisation vers le suivi central et contrôle régulier :
```bash
sudo journalctl -u isc-dhcp-server --since "1 hour ago" --no-pager
```
👉 Explication : Permet de repérer des demandes anormales (épuisement de la plage, clients inconnus). Une plage saturée doit être signalée à l'administrateur réseau.

4. Sauvegarde de la configuration et des baux :
```bash
sudo tar czf /root/dhcp-backup-$(date +%F).tgz /etc/dhcp /var/lib/dhcp
sudo ls -l /root/dhcp-backup-*.tgz
```
👉 Explication : Archive datée de la configuration et de la base des baux. La stocker hors du serveur.

5. Point à vérifier : la fin de vie d'ISC DHCP est annoncée par l'éditeur ISC. Avant toute extension de ce service, confirmer le statut de maintenance du paquet Debian 12 et évaluer une migration vers Kea (fiche `Fiche_Simple_-_Kea-DHCPv4.md`).

---