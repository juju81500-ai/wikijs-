# 📄 FreeRADIUS

- **Environnement** : VM (Debian 13)
- **OS / Version** : Debian 13 (trixie)
- **Version** : FreeRADIUS 3.2.x (paquet des dépôts Debian, à vérifier sur la version déployée)
- **Catégorie** : Réseau et cybersécurité
- **Tags** : `[debian-13]`, `[freeradius]`, `[radius]`, `[aaa]`, `[hardening]`

## 🎯 Problème précis à résoudre
Installer un serveur RADIUS FreeRADIUS sur Debian 13, vérifier sur ce même serveur qu'il accepte une authentification de test, puis le durcir (secret partagé propre, équipements réseau autorisés, pare-feu restreint) avant de le raccorder à un équipement réseau de l'entreprise (commutateur, borne Wi-Fi, concentrateur VPN). Les tests ne se font que sur votre propre serveur.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation de FreeRADIUS et des outils de test :
```bash
sudo apt update
sudo apt install -y freeradius freeradius-utils
```
👉 Explication : Installe le serveur RADIUS et `radtest`, l'outil qui envoie une demande d'authentification de test. Les paquets proviennent des dépôts Debian 13.

2. Vérification de la version et de la syntaxe de la configuration :
```bash
freeradius -v
ls /etc/freeradius/
sudo freeradius -CX
```
👉 Explication : `freeradius -v` affiche la version installée. `ls /etc/freeradius/` indique le dossier de configuration présent : `<dossier_config>` désigne ce dossier (par exemple `3.0` ou `3.2`, à vérifier sur la version déployée) et sera utilisé dans toutes les étapes suivantes. `sudo freeradius -CX` relit toute la configuration sans démarrer le service et affiche les erreurs éventuelles.

3. Démarrage du service et contrôle de son état :
```bash
sudo systemctl enable freeradius
sudo systemctl start freeradius
systemctl status freeradius --no-pager
```
👉 Explication : Active le démarrage automatique au redémarrage, lance le service, puis affiche son état. La ligne `Active: active (running)` est attendue.

4. Création d'un utilisateur de test dans le fichier `authorize` du module `files` :
```bash
sudo nano /etc/freeradius/<dossier_config>/mods-config/files/authorize
```
Ajouter à la fin du fichier, en remplaçant les valeurs entre chevrons :
```
<utilisateur_test> Cleartext-Password := "<mot_de_passe_test>"
```
👉 Explication : `<utilisateur_test>` est le nom de compte de test, `<mot_de_passe_test>` un mot de passe de lab, jamais réutilisé ailleurs. Ce mot de passe en clair ne doit exister que dans un environnement de test.

5. Relance du service puis test d'authentification sur le serveur lui-même :
```bash
sudo systemctl restart freeradius
radtest <utilisateur_test> <mot_de_passe_test> 127.0.0.1 0 testing123
```
👉 Explication : `radtest` envoie une demande `Access-Request` au serveur local (`127.0.0.1`, port 1812 UDP, secret `testing123` du client `localhost` fourni par défaut). La réponse attendue est `Access-Accept`. Un `Access-Reject` signifie que le nom ou le mot de passe ne correspond pas à l'entrée du fichier `authorize`.

---

## ⚡ 2. Production — Façon Simplifiée
1. Déclaration de l'équipement réseau (NAS) avec un secret propre dans `clients.conf` :
```bash
sudo nano /etc/freeradius/<dossier_config>/clients.conf
```
Ajouter ce bloc, en remplaçant les valeurs entre chevrons :
```
client <nom_equipement> {
    ipaddr = <adresse_ip_equipement>
    secret = <secret_partage_fort>
}
```
👉 Explication : `<nom_equipement>` est un libellé libre, `<adresse_ip_equipement>` est l'adresse IP du commutateur, de la borne ou du concentrateur VPN qui interroge RADIUS. `<secret_partage_fort>` est un secret d'au moins 24 caractères aléatoires, saisi à l'identique sur l'équipement.

2. Contrôle de la syntaxe puis redémarrage :
```bash
sudo freeradius -CX
sudo systemctl restart freeradius
systemctl status freeradius --no-pager
```
👉 Explication : Vérifie la configuration avant de relancer le service, puis confirme que le service est actif.

3. Ouverture du pare-feu uniquement pour l'équipement déclaré et pour l'administration :
```bash
sudo apt install -y ufw
sudo ufw allow from <adresse_ip_admin> to any port 22 proto tcp
sudo ufw allow from <adresse_ip_equipement> to any port 1812 proto udp
sudo ufw allow from <adresse_ip_equipement> to any port 1813 proto udp
sudo ufw enable
sudo ufw status verbose
```
👉 Explication : Autorise SSH seulement depuis `<adresse_ip_admin>` avant d'activer le pare-feu, ce qui évite de se couper l'accès. Le port 1812 UDP sert à l'authentification, le port 1813 UDP à la comptabilité (à ouvrir seulement si l'équipement l'utilise). `ufw status verbose` liste les règles actives.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Suppression des secrets par défaut, connus publiquement (`testing123`) :
```bash
sudo grep -n "testing123" /etc/freeradius/<dossier_config>/clients.conf
sudo nano /etc/freeradius/<dossier_config>/clients.conf
```
👉 Explication : La première commande liste les blocs `client` qui utilisent encore le secret d'usine. Dans l'éditeur, supprimer ces blocs, notamment `client localhost` et les blocs de réseau privé. Aucun secret par défaut ne doit subsister en production.

2. Restriction des droits sur le fichier qui contient les secrets :
```bash
sudo chown root:freerad /etc/freeradius/<dossier_config>/clients.conf
sudo chmod 640 /etc/freeradius/<dossier_config>/clients.conf
ls -l /etc/freeradius/<dossier_config>/clients.conf
```
👉 Explication : Seul `root` peut modifier le fichier, et seul le groupe `freerad` peut le lire (le service tourne sous ce compte). Le groupe `freerad` est créé par le paquet, à vérifier sur la version déployée.

3. Restriction des interfaces d'écoute :
```bash
sudo nano /etc/freeradius/<dossier_config>/sites-enabled/default
sudo freeradius -CX
```
👉 Explication : Dans le bloc `listen` de type `auth` et `acct`, remplacer `ipaddr = *` par `ipaddr = <adresse_ip_serveur>` pour n'écouter que sur l'interface prévue. `<adresse_ip_serveur>` est l'adresse IP du serveur RADIUS. Le test `-CX` confirme que la syntaxe reste valide (la structure du fichier `default` peut varier selon la version, à vérifier sur la version déployée).

4. Contrôle des journaux d'authentification :
```bash
sudo tail -n 50 /var/log/freeradius/radius.log
```
👉 Explication : Affiche les 50 dernières lignes du journal. Les rejets (`Login incorrect`, `Reject`) et les demandes d'un client inconnu (`Ignoring request from unknown client`) doivent être surveillés. Un pic d'échecs peut indiquer une tentative de mot de passe deviné : à remonter au responsable sécurité.

5. Sauvegarde de la configuration avant toute évolution :
```bash
sudo tar czf /root/freeradius-conf-$(date +%F).tgz /etc/freeradius/<dossier_config>
sudo ls -l /root/freeradius-conf-*.tgz
```
👉 Explication : Crée une archive datée de toute la configuration FreeRADIUS. Le fichier contient les secrets partagés : le stocker hors du serveur, dans un coffre-fort (voir la fiche Passbolt ou Vaultwarden du pack), et le protéger en lecture.

---
