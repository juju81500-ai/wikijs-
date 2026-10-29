# Fiche_Simple_-_VM_Debian_13_OCS_Inventory_DNS_TLS.md

- **Environnement** : VM Debian 13 dédiée, OCS Inventory 3.0 (Nginx, uWSGI, PostgreSQL local)
- **OS / Version** : Debian 13 Trixie; OCS Inventory 3.0; PostgreSQL 17
- **Catégorie** : inventaire de parc / ITSM

---

## Problème précis à résoudre

Fixer les noms de serveur Nginx pour la console et l'API, puis activer TLS.

## 1. Hors-Production (Lab / Test / POC)

1. Éditer les deux vhosts Nginx fournis par le paquet : remplacer `server_name _;` par `ocs-api.example.net` et `ocs.example.net` (noms d'exemple à remplacer), et vérifier qu'aucun autre vhost catch-all ne crée de conflit.
   👉 Explication : chaque vhost doit répondre à son propre nom.

2. Dans la configuration de la console, régler `BACKEND_API_ROUTE` sur `https://ocs-api.example.net/`.
   👉 Explication : la console doit joindre l'API par son nom TLS.

3. Configurer TLS sur les deux vhosts selon la fiche officielle, puis tester et recharger Nginx :
   ```bash
   sudo nginx -t
   sudo systemctl reload nginx
   ```
   👉 Explication : `nginx -t` valide la syntaxe avant tout rechargement.

4. Rediriger HTTP vers HTTPS une fois les certificats validés.
   👉 Explication : évite l'accès en clair après vérification.

## 2. Production — Contrôles

Certificats émis par l'autorité approuvée, renouvellement planifié, clés privées en lecture restreinte.

## 3. Production — Sécurité

- Ne pas considérer le port API 8081 comme protégé tant que le vhost et le certificat effectifs ne sont pas validés.
- Protéger les clés privées (propriétaire root, mode 0600).

## Validation et retour arrière

- **Validation** : `sudo nginx -t` OK et accès HTTPS à la console sans alerte de certificat.
- **Retour arrière** : Restaurer les vhosts sauvegardés, puis `sudo nginx -t && sudo systemctl reload nginx`.

## Si le problème n'est pas résolu

- [OCS Inventory — TLS](https://documentation.ocsinventory-ng.org/administrator-docs/server-setup/security/securing-ocs-with-ssl.md)
- [OCS Inventory — Sécuriser le serveur](https://documentation.ocsinventory-ng.org/administrator-docs/server-setup/security.md)
- [Guide complet OCS Inventory 3 Debian 13](/02-fiches-completes/debian/13/installation-deploiement/41-deploiement-ocs-inventory-3-debian-13#5-configurer-noms-dns-et-tls)