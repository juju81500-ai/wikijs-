# Fiche_Simple_-_VM_Debian_13_NetBox_Nginx_TLS.md

- **Environnement** : Debian 13; NetBox 4.7.4; certificat TLS provisionné par l'organisation
- **OS / Version** : Debian 13; Nginx et NetBox
- **Catégorie** : IPAM / DCIM / reverse proxy
- **Tags** : `debian13`, `netbox`, `nginx`, `tls`, `reverse-proxy`

---

## Problème précis à résoudre

Publier l'interface NetBox derrière Nginx en HTTPS sans exposer Gunicorn, PostgreSQL ou Redis.

## 1. Hors-Production (Lab / Test / POC)

1. Installer le certificat et sa clé (droits restreints) :
   ```bash
   sudo install -d -m 0755 /etc/ssl/netbox
   sudo install -m 0644 netbox.crt /etc/ssl/netbox/
   sudo install -m 0600 netbox.key /etc/ssl/netbox/
   ```
   👉 Explication : le certificat doit correspondre au FQDN de `ALLOWED_HOSTS`.

2. Copier la configuration fournie et l'adapter :
   ```bash
   sudo cp /opt/netbox/contrib/nginx.conf /etc/nginx/sites-available/netbox
   sudoedit /etc/nginx/sites-available/netbox
   ```
   👉 Explication : remplacer `server_name`, ajouter `listen 443 ssl`, `ssl_certificate` et `ssl_certificate_key` selon la politique locale.

3. Activer le site et tester :
   ```bash
   sudo ln -s /etc/nginx/sites-available/netbox /etc/nginx/sites-enabled/netbox
   sudo nginx -t
   sudo systemctl reload nginx
   ```
   👉 Explication : `nginx -t` doit réussir; ne supprimer le site par défaut qu'après validation, en gardant un accès de secours.

4. Contrôler l'accès :
   ```bash
   curl -kI https://FQDN/
   sudo ss -ltnp | grep -E ':(80|443|5432|6379|8001)\b'
   ```
   👉 Explication : remplacer `FQDN`; seuls 80/443 sont ouverts au réseau d'administration; 5432, 6379 et Gunicorn restent locaux.

## 2. Production — Contrôles

Faire approuver nom DNS, certificat, renouvellement, en-têtes proxy, politique d'accès, journaux et règles de pare-feu avec les propriétaires applicatif et réseau.

## 3. Production — Sécurité

- Ne pas supprimer le site Nginx par défaut avant validation et accès de secours.
- Ne jamais exposer TCP/5432, TCP/6379 ou le socket/port Gunicorn.
- Ne pas utiliser de certificat auto-signé ou expiré pour le service métier.
- Ne pas transmettre des en-têtes d'identité venant de clients non fiables.

## Validation et retour arrière

- **Validation** : HTTPS validé, nom et certificat conformes, accès limité au réseau autorisé, services internes non exposés.
- **Retour arrière** : restaurer l'ancien vhost Nginx, lancer `nginx -t` puis recharger.

## Si le problème n'est pas résolu

- [NetBox — serveur HTTP Nginx](https://netbox.readthedocs.io/en/stable/installation/5-http-server/)
- [Nginx — documentation](https://nginx.org/en/docs/)
- [Guide complet NetBox Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/73_Deploiement_NetBox_4.7.4_Debian_13.md#7-configurer-nginx-avec-tls)
