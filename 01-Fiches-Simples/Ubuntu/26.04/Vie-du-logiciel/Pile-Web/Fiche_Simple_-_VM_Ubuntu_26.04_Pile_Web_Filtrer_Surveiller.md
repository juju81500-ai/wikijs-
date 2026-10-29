# Fiche_Simple_-_VM_Ubuntu_26.04_Pile_Web_Filtrer_Surveiller.md

- **Environnement** : VM ou serveur dédié Ubuntu Server hébergeant une application PHP avec PostgreSQL local et TLS
- **OS / Version** : Ubuntu Server 26.04 LTS (Resolute); Nginx, PHP 8.5, PostgreSQL 18
- **Catégorie** : services web / pare-feu
- **Tags** : `ubuntu2604`, `nginx`, `php8.5`, `postgresql18`, `tls`

---

## Problème précis à résoudre

Limiter les flux entrants et surveiller le serveur.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler le pare-feu :
   ```bash
   sudo ufw status verbose
   ```
   👉 Explication : Affiche le pare-feu UFW s'il est actif; vérifier le pare-feu réellement utilisé.

2. Autoriser les flux requis :
   ```bash
   sudo ufw allow 443/tcp
   sudo ufw allow from 192.0.2.0/24 to any port 22 proto tcp
   ```
   👉 Explication : Autorise HTTPS et SSH depuis le seul réseau d'administration (`192.0.2.0/24` est un exemple à remplacer). À jouer seulement si UFW est le pare-feu retenu et après avoir prévu l'accès SSH.

3. Surveiller :
   ```bash
   df -h
   systemctl --failed
   sudo journalctl -u nginx --no-pager -n 30
   ```
   👉 Explication : Contrôle espace disque, services et journaux.

## 2. Production — Contrôles

Contrôler logs, espace disque et mises à jour.

## 3. Production — Sécurité

- Autoriser uniquement HTTPS et SSH depuis l'administration.
- Ne pas activer UFW sans règle SSH.

## Validation et retour arrière

- **Validation** : seuls les flux requis sont ouverts.
- **Retour arrière** : `sudo ufw delete allow 443/tcp` (ou la règle ajoutée).

## Si le problème n'est pas résolu

- [Nginx — documentation](https://nginx.org/en/docs/)
- [PostgreSQL 18 — documentation](https://www.postgresql.org/docs/18/)
- [Guide complet — étape 6](../../../../../02-Fiches-Completes/Ubuntu/26.04/Installation-Deploiement/21_Pile_Web_Ubuntu_Server_26.04_Nginx_PHP85_PostgreSQL18.md#6-filtrer-et-surveiller)
