# Déployer OCS Inventory 3.0 sur Debian 13

- **OS / Version** : Debian 13 Trixie; OCS Inventory 3.0; PostgreSQL 17
- **Type de fiche** : Installation/Déploiement
- **Environnement** : VM Linux dédiée, Nginx, backend API et console Web
- **Machine ciblée** : Serveur inventaire
- **Catégorie** : Inventaire de parc / ITSM

## 1. Architecture et prérequis

Fiche simple : [cadrer l'architecture OCS](/01-fiches-simples/debian/13/vie-du-logiciel/ocs-inventory/fiche-simple-vm-debian-13-ocs-inventory-cadrer).

OCS 3 sépare le backend API (Django/uWSGI) de la console Web (Vue.js). Ce guide suit les paquets officiels Debian et utilise PostgreSQL local. Le dépôt officiel prend en charge `trixie`; ne pas mélanger les paquets serveur OCS 2.x avec l'architecture OCS 3.

Prévoir DNS et certificat TLS pour `ocs.example.net` (console) et `ocs-api.example.net` (API), 4 Go RAM minimum (8 Go recommandés), stockage adapté aux inventaires, SMTP et sauvegarde hors hôte. Restreindre l'administration et l'API aux réseaux autorisés selon les besoins du parc.

## 2. Installer PostgreSQL et créer la base

Fiche simple : [installer PostgreSQL et créer la base](/01-fiches-simples/debian/13/vie-du-logiciel/ocs-inventory/fiche-simple-vm-debian-13-ocs-inventory-postgresql).

Sur Debian 13, vérifier la version disponible puis installer PostgreSQL 17 et les extensions nécessaires :

```bash
sudo apt update
apt-cache policy postgresql
sudo apt install postgresql postgresql-contrib
sudo systemctl enable --now postgresql
psql --version
```

Créer un compte et une base réservés à OCS. Saisir le mot de passe à l'invite `\password`; ne pas l'inscrire dans le script ou l'historique :

```bash
sudo -u postgres psql
```

Dans `psql` :

```sql
CREATE ROLE ocsuser LOGIN;
\password ocsuser
CREATE DATABASE ocsdb OWNER ocsuser ENCODING 'UTF8';
\q
```

Garder PostgreSQL lié à loopback pour cette architecture monohôte. Ne pas ouvrir 5432 au réseau si le backend et la base sont sur la même VM.

## 3. Ajouter le dépôt officiel et installer OCS

Fiche simple : [ajouter le dépôt et installer OCS](/01-fiches-simples/debian/13/vie-du-logiciel/ocs-inventory/fiche-simple-vm-debian-13-ocs-inventory-installer-paquets).

```bash
curl -fsSL https://deb-v3.ocsinventory-ng.org/repo-signing-key.gpg \
  | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/ocs-archive-keyring.gpg
echo "deb https://deb-v3.ocsinventory-ng.org/ trixie main" \
  | sudo tee /etc/apt/sources.list.d/ocsinventory.list
sudo apt update
apt-cache policy ocsinventory-server
sudo apt install ocsinventory-server
```

Confirmer l'origine du paquet affichée par `apt-cache policy` avant installation. Le paquet installe le backend, la console et les services Nginx/uWSGI correspondants.

## 4. Configurer le backend

Fiche simple : [configurer le backend](/01-fiches-simples/debian/13/vie-du-logiciel/ocs-inventory/fiche-simple-vm-debian-13-ocs-inventory-backend).

Lancer le script officiel de configuration :

```bash
sudo /usr/share/ocsinventory-backend/tools/configure-ocsinventory-backend.sh
```

Choisir PostgreSQL et saisir `127.0.0.1`, le port 5432, la base `ocsdb`, le rôle `ocsuser`, son secret et l'URL de console `https://ocs.example.net/`. Le script applique les migrations et journalise leur résultat.

## 5. Configurer noms DNS et TLS

Fiche simple : [configurer DNS et TLS](/01-fiches-simples/debian/13/vie-du-logiciel/ocs-inventory/fiche-simple-vm-debian-13-ocs-inventory-dns-tls).

Les paquets fournissent deux blocs Nginx distincts. Remplacer les noms génériques `server_name _;` par `ocs-api.example.net` et `ocs.example.net`; vérifier qu'aucun autre vhost catch-all ne crée de conflit. Dans la configuration de la console, régler `BACKEND_API_ROUTE` vers `https://ocs-api.example.net/`.

Configurer TLS pour les deux vhosts selon la fiche officielle OCS, en protégeant les clés privées et en redirigeant HTTP vers HTTPS après validation :

```bash
sudo nginx -t
sudo systemctl reload nginx
```

Ne pas considérer le port API 8081 comme protégé par TLS avant d'avoir validé le vhost et le certificat effectifs.

## 6. Créer les comptes et les permissions

Fiche simple : [créer comptes et permissions](/01-fiches-simples/debian/13/vie-du-logiciel/ocs-inventory/fiche-simple-vm-debian-13-ocs-inventory-comptes).

Créer des comptes nominatif(s) dans la console et un compte agent de service distinct. Appliquer uniquement les permissions nécessaires pour consulter les inventaires et déposer les remontées. Réserver les droits d'administration et de déploiement à des opérateurs habilités; ce guide n'active pas le déploiement distant de paquets.

## 7. Recette

Fiche simple : [recetter l'installation OCS](/01-fiches-simples/debian/13/vie-du-logiciel/ocs-inventory/fiche-simple-vm-debian-13-ocs-inventory-recette).

```bash
sudo systemctl --no-pager status nginx ocsinventory-backend-uwsgi
sudo journalctl -u ocsinventory-backend-uwsgi -n 50 --no-pager
sudo tail -n 50 /var/log/ocsinventory-backend/ocsinventory-backend.log
```

Vérifier l'accès TLS à la console, puis tester l'API avec un compte habilité. Une réponse `401 Unauthorized` à la racine de l'API peut être attendue et confirme sa disponibilité. Installer un agent de test depuis la fiche simple correspondante et vérifier qu'un inventaire apparaît.

## 8. Sauvegarde et exploitation

Fiche simple : [sauvegarder et exploiter OCS](/01-fiches-simples/debian/13/vie-du-logiciel/ocs-inventory/fiche-simple-vm-debian-13-ocs-inventory-sauvegarde).

- Sauvegarder la base PostgreSQL, la configuration, les clés OCS, les vhosts et les fichiers de personnalisation; chiffrer et copier les archives hors VM.
- Sauvegarder particulièrement la clé d'encryption OCS, qui protège les valeurs sensibles stockées en base.
- Tester la restauration dans un environnement isolé, sans reconnecter les agents de production.
- Mettre à jour depuis les dépôts officiels après sauvegarde, consulter les notes de version et tester un agent pilote.

## Sources

- [OCS Inventory — Installation essentielle](https://documentation.ocsinventory-ng.org/quickstart-guides/for-administrators/installation-essentials.md)
- [OCS Inventory — Dépôts officiels](https://documentation.ocsinventory-ng.org/administrator-docs/server-setup/installation-methods/using-official-repositories.md)
- [OCS Inventory — Prérequis](https://documentation.ocsinventory-ng.org/administrator-docs/system-requirements.md)
- [OCS Inventory — Sécuriser le serveur](https://documentation.ocsinventory-ng.org/administrator-docs/server-setup/security.md)
- [OCS Inventory — TLS](https://documentation.ocsinventory-ng.org/administrator-docs/server-setup/security/securing-ocs-with-ssl.md)
- [OCS Inventory — Différences v2/v3](https://documentation.ocsinventory-ng.org/project-overview/v2-vs-v3-whats-changed.md)