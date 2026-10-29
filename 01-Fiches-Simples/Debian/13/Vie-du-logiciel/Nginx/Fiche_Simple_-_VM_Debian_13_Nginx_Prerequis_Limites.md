# Fiche_Simple_-_VM_Debian_13_Nginx_Prerequis_Limites

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; Nginx des dépôts Debian
- **Catégorie** : serveur Web / Nginx / Prérequis et limites
- **Tags** : `debian13`, `nginx`, `prerequis`

---

## Problème précis à résoudre

Vérifier que la VM peut accueillir Nginx seul (serveur Web statique ou reverse proxy) et connaître les limites du périmètre avant de l'installer.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler l'OS, la résolution DNS et l'espace disque :
   ```bash
   cat /etc/os-release | grep -E '^(PRETTY_NAME|VERSION_ID)='
   hostname -f
   df -h /var /etc
   ```
   👉 Explication : confirmer Debian 13, un nom d'hôte cohérent et de la place pour `/var/log/nginx` et `/var/www`.

2. Vérifier qu'aucun service n'occupe déjà les ports 80 et 443 :
   ```bash
   sudo ss -tlnp | grep -E ':(80|443)\b' || echo 'ports 80/443 libres'
   ```
   👉 Explication : un Apache ou un autre proxy installé par défaut doit être arrêté ou déplacé avant Nginx.

3. Noter les limites du périmètre :
   👉 Explication : cette série couvre Nginx du dépôt Debian (version 1.26 attendue, à vérifier avec `apt-cache policy nginx`), sans PHP-FPM (voir la fiche LEMP), sans module commercial Nginx Plus et sans haute disponibilité (voir Keepalived-HAProxy).

## 2. Production — Contrôles

Consigner le nom DNS, l'adresse IP, le rôle (statique, reverse proxy), le responsable, la fenêtre de maintenance et la politique de sauvegarde avant toute installation.

## 3. Production — Sécurité

- Ne pas exposer la VM sur Internet avant la fin de la fiche Sécuriser.
- Prévoir un compte d'administration nominatif avec `sudo`, jamais de connexion `root` distante.
- Ne pas mélanger Nginx et Apache sur les mêmes ports sans plan explicite.

## Validation et retour arrière

- **Validation** : OS confirmé, ports 80/443 libres, périmètre et responsable consignés.
- **Retour arrière** : aucune modification n'est faite par cette étape ; rien à annuler.

## Si le problème n'est pas résolu

- [Nginx — Installer](Fiche_Simple_-_VM_Debian_13_Nginx_Installer.md)
- [Nginx — Configurer un site](Fiche_Simple_-_VM_Debian_13_Nginx_Configurer.md)
- [Nginx — Sécuriser (TLS, en-têtes, pare-feu)](Fiche_Simple_-_VM_Debian_13_Nginx_Securiser.md)
- [Nginx — Valider (recette)](Fiche_Simple_-_VM_Debian_13_Nginx_Valider.md)
- [Nginx — Sauvegarder et restaurer](Fiche_Simple_-_VM_Debian_13_Nginx_Sauvegarder_Restaurer.md)
- [Nginx — Mise à jour et retour arrière](Fiche_Simple_-_VM_Debian_13_Nginx_Mettre_A_Jour.md)
- [Guide complet LEMP Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/02_Pile_LEMP_Debian_13_Nginx_PHP_MariaDB.md)
- [Nginx — documentation officielle](https://nginx.org/en/docs/)
