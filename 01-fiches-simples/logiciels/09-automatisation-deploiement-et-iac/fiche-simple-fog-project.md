# 📄 FOG Project

- **Environnement** : VM (Debian 12), disque dédié pour les images
- **OS / Version** : Debian 12 (bookworm)
- **Version** : FOG Project, branche `master` du dépôt officiel (version exacte à vérifier sur la version déployée)
- **Catégorie** : Automatisation, déploiement et IaC
- **Tags** : `[debian-12]`, `[fog]`, `[pxe]`, `[imagerie]`, `[deploiement]`, `[hardening]`

## 🎯 Problème précis à résoudre
Installer le serveur FOG Project sur Debian 12 avec son script officiel, vérifier les services d'imagerie (web, TFTP, NFS, base), préparer le démarrage PXE des postes, puis durcir l'accès à l'interface d'administration et sauvegarder la base et les images.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation des prérequis et récupération du dépôt :
```bash
sudo apt update
sudo apt install -y git
sudo git clone --depth 1 -b master https://github.com/FOGProject/fogproject.git /opt/fogproject
```
👉 Explication : Installe Git et copie le dépôt officiel FOG dans `/opt/fogproject`. `--depth 1` limite le téléchargement au dernier état de la branche.

2. Lancement de l'installeur officiel :
```bash
cd /opt/fogproject/bin
sudo ./installfog.sh
```
👉 Explication : L'installeur est interactif. Il demande le type d'installation (normale ou développement, choisir normale), l'adresse IP du serveur (adresse fixe obligatoire), le nom DNS et la création de la base. Il installe Apache, MariaDB, TFTP et NFS. L'opération dure plusieurs minutes. Les options exactes proposées dépendent de la version, à vérifier pendant l'installation.

3. Contrôle des services :
```bash
systemctl status apache2 mariadb --no-pager
systemctl status tftpd-hpa nfs-kernel-server --no-pager
```
👉 Explication : Les quatre services doivent afficher `Active: active (running)`. Les noms `tftpd-hpa` et `nfs-kernel-server` sont ceux du paquet Debian, à vérifier sur la version déployée.

4. Test de l'interface web :
```bash
curl -I http://<adresse_serveur_fog>/fog/management/
```
👉 Explication : Une réponse `HTTP/1.1 200 OK` ou une redirection vers la page de connexion est attendue. Dans un navigateur, `http://<adresse_serveur_fog>/fog/management/` ouvre la console. Identifiant et mot de passe par défaut à remplacer dès la première connexion.

5. Configuration DHCP du lab pour le démarrage PXE :
```
option 66 (serveur TFTP) = <adresse_serveur_fog>
option 67 (fichier de démarrage) = undionly.kpxe
```
👉 Explication : Ces options sont à configurer sur le serveur DHCP du lab (pas sur FOG). Elles indiquent aux postes où charger le démarrage réseau. Le nom du fichier (`undionly.kpxe` ou `ipxe.efi` pour UEFI) est à vérifier selon le matériel.

---

## ⚡ 2. Production — Façon Simplifiée
1. Ouverture du pare-feu pour les services FOG :
```bash
sudo apt install -y ufw
sudo ufw allow from <adresse_ip_admin> to any port 22 proto tcp
sudo ufw allow from <plage_reseau_postes> to any port 80 proto tcp
sudo ufw allow from <plage_reseau_postes> to any port 69 proto udp
sudo ufw allow from <plage_reseau_postes> to any port 2049 proto tcp
sudo ufw enable
sudo ufw status verbose
```
👉 Explication : Limite l'accès au réseau des postes (`<plage_reseau_postes>`) pour le web, TFTP (UDP 69) et NFS (TCP 2049). La liste exacte des ports nécessaires dépend de la version : à vérifier avant mise en service. SSH reste limité à `<adresse_ip_admin>`.

2. Changement du mot de passe du compte d'administration FOG dans l'interface web, section `Utilisateurs`, avant toute mise en service.
👉 Explication : Le mot de passe par défaut de FOG est connu publiquement. La méthode en ligne de commande pour le modifier dépend de la version déployée : à vérifier avant utilisation, la console web reste la méthode de référence.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Restriction de l'accès web à l'administration :
```bash
sudo nano /etc/apache2/conf-available/fog-admin.conf
sudo a2enconf fog-admin
sudo systemctl reload apache2
```
Contenu, à adapter :
```
<Location "/fog/management">
    Require ip <plage_reseau_admin>
</Location>
```
👉 Explication : Limite la console `/fog/management` au réseau d'administration seulement. Le nom du fichier de configuration est un choix de cette fiche, à vérifier : le chemin `/fog/management` doit correspondre à celui de la version déployée.

2. Sauvegarde de la base de données FOG :
```bash
sudo mysqldump fog > /root/fog-db-$(date +%F).sql
sudo chmod 600 /root/fog-db-*.sql
sudo ls -l /root/fog-db-*.sql
```
👉 Explication : Exporte la base `fog` (nom par défaut, à vérifier). Le fichier contient les comptes et les hôtes : le copier hors du serveur et le protéger.

3. Sauvegarde des images système :
```bash
sudo rsync -a --info=progress2 /images/ /srv/sauvegarde-fog/images/
```
👉 Explication : Copie le dossier `/images` où FOG stocke les images capturées. Le dossier de destination `/srv/sauvegarde-fog` est un exemple, à remplacer par un espace de sauvegarde distinct du serveur. Les images peuvent être volumineuses.

4. Contrôle des journaux d'accès à l'interface :
```bash
sudo tail -n 50 /var/log/apache2/access.log
```
👉 Explication : Affiche les dernières requêtes. Les accès depuis des adresses inconnues, ou des échecs répétés sur `/fog/management`, sont à remonter au responsable sécurité.

---
