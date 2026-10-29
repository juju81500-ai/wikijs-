# Fiche_Simple_-_VM_Debian_13_Redis_Prerequis_Limites

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; Redis des dépôts Debian
- **Catégorie** : base clé-valeur / Redis / Prérequis et limites

---

## Problème précis à résoudre

Cadrer l'usage de Redis sur Debian 13 (cache, file, sessions) avant installation.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier l'OS, la version candidate et la mémoire :
   ```bash
   cat /etc/os-release | grep PRETTY_NAME
   apt-cache policy redis-server
   free -h
   ```
   👉 Explication : Redis stocke ses données en mémoire : dimensionner la RAM avec une marge pour la persistance (fork) ; vérifier la version publiée dans Debian.

2. Contrôler le port :
   ```bash
   sudo ss -tlnp | grep -E ':6379\b' || echo 'port 6379 libre'
   ```
   👉 Explication : aucun autre Redis ne doit écouter.

3. Qualifier l'usage :
   👉 Explication : cache pur (perte tolérée) ou données à conserver (persistance RDB/AOF) ; clients autorisés ; taille maximale.

## 2. Production — Contrôles

Consigner usage, volumétrie, politique d'éviction, persistance, responsable.

## 3. Production — Sécurité

- Ne jamais exposer Redis à Internet.
- Ne pas stocker de données sensibles non chiffrées sans nécessité.
- Limites : instance unique ; Sentinel et Cluster hors périmètre. La licence des versions récentes est à vérifier selon l'usage.

## Validation et retour arrière

- **Validation** : usage et dimensionnement validés.
- **Retour arrière** : aucune modification effectuée.

## Si le problème n'est pas résolu

- [Redis — Installer](/01-fiches-simples/debian/13/vie-du-logiciel/redis/fiche-simple-vm-debian-13-redis-installer)
- [Redis — Configurer](/01-fiches-simples/debian/13/vie-du-logiciel/redis/fiche-simple-vm-debian-13-redis-configurer)
- [Redis — Sécuriser (ACL, TLS, pare-feu)](/01-fiches-simples/debian/13/vie-du-logiciel/redis/fiche-simple-vm-debian-13-redis-securiser)
- [Redis — Valider (recette)](/01-fiches-simples/debian/13/vie-du-logiciel/redis/fiche-simple-vm-debian-13-redis-valider)
- [Redis — Sauvegarder et restaurer](/01-fiches-simples/debian/13/vie-du-logiciel/redis/fiche-simple-vm-debian-13-redis-sauvegarder-restaurer)
- [Redis — Mise à jour et retour arrière](/01-fiches-simples/debian/13/vie-du-logiciel/redis/fiche-simple-vm-debian-13-redis-mettre-a-jour)
- [Redis — documentation officielle](https://redis.io/docs/latest/)
- [Redis — sécurité](https://redis.io/docs/latest/operate/oss_and_stack/management/security/)
- [Installation Redis avec NetBox (fiche du pack)](/01-fiches-simples/debian/13/vie-du-logiciel/postgresql/fiche-simple-vm-debian-13-netbox-installer-postgresql-redis)