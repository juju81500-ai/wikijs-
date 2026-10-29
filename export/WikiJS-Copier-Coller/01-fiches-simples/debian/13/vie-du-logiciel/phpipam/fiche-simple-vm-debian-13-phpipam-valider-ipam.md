# Fiche_Simple_-_VM_Debian_13_phpIPAM_Valider_IPAM.md

- **Environnement** : phpIPAM 1.8.3 sur Debian 13, MariaDB locale et HTTPS
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : IPAM

---

## Problème précis à résoudre

Vérifier qu'un pilote d'adressage est cohérent, que les rôles sont limités et que la base peut être restaurée sans découvrir ni sonder le réseau.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier les services et l'accès HTTPS :
   ```bash
   systemctl --no-pager status nginx php8.4-fpm mariadb
   curl -fsSI https://ipam.example.net/
   ```
   👉 Explication : remplacer le nom; accès depuis le réseau d'administration uniquement.

2. Confirmer que l'assistant d'installation est désactivé :
   ```bash
   curl -s -o /dev/null -w '%{http_code}\n' https://ipam.example.net/app/install/
   ```
   👉 Explication : un code `403` ou `404` est attendu; remplacer aussi le compte `Admin` initial : **Administration > Users > Admin > Edit**.

3. Créer les objets de test : **Administration > Sections > Add section**, **Subnets > Add subnet** (préfixe de documentation, ex. `192.0.2.0/24`), puis ajouter quelques adresses.
   👉 Explication : vérifier hiérarchie et statut.

4. Créer un compte opérateur limité : **Administration > Users > Add user** (rôle Utilisateur normal, droits par section **Read/Write** sur le seul périmètre).
   👉 Explication : se connecter avec ce compte et confirmer qu'il ne modifie que son périmètre.

5. Sauvegarder base et configuration, puis restaurer sur une instance isolée :
   ```bash
   sudo mariadb-dump --single-transaction phpipam | gzip > /root/phpipam-$(date +%F).sql.gz
   sudo cp -a /var/www/phpipam/config.php /root/phpipam-config.$(date +%F).php
   gunzip -c /root/phpipam-AAAA-MM-JJ.sql.gz | sudo mariadb phpipam_test
   ```
   👉 Explication : remplacer la date; `config.php` contient des secrets; vérifier accès et objets sur l'instance isolée.

## 2. Production — Contrôles

Documenter propriétaires, sources d'autorité, processus de modification, sections, VLAN, conventions de préfixes et fréquence de rapprochement avant d'importer des données réelles.

## 3. Production — Sécurité

- HTTPS et accès réseau réservés aux administrateurs et utilisateurs approuvés.
- Compte MariaDB applicatif limité à la base `phpipam`; secret protégé dans `config.php`.
- Assistant d'installation désactivé après initialisation; compte initial changé; comptes nominatifs et API à privilèges minimaux.
- Ne pas activer ping/discovery ni suppression automatique dans le cadre de ce contrôle.
- Sauvegardes chiffrées hors hôte et restauration périodiquement testée.

## Validation et retour arrière

- **Validation** : préfixes cohérents, autorisations vérifiées, assistant désactivé, dump restaurable en environnement isolé.
- **Retour arrière** : conserver code, `config.php` et dump précédents; interrompre l'import si le périmètre ou la propriété des plages est incertain.

## Si le problème n'est pas résolu

- [phpIPAM — documentation d'installation](https://phpipam.net/documents/installation/)
- [phpIPAM — site de documentation](https://phpipam.net/documents/)
- [Guide complet phpIPAM 1.8.3 Debian 13](/02-fiches-completes/debian/13/installation-deploiement/74-deploiement-phpipam-1-8-3-debian-13)