# Fiche_Simple_-_VM_Debian_13_Redis_Valider

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; Redis des dépôts Debian
- **Catégorie** : base clé-valeur / Redis / Valider (recette)

---

## Problème précis à résoudre

Prouver que Redis est opérationnel, authentifié et chiffré.

## 1. Hors-Production (Lab / Test / POC)

1. État du service et écoute :
   ```bash
   systemctl is-active redis-server
   sudo ss -tlnp | grep redis
   ```
   👉 Explication : écoute sur les adresses prévues seulement.

2. Refus sans authentification :
   ```bash
   redis-cli --tls --cacert /chemin/CA.crt -h NOM_SERVEUR ping
   ```
   👉 Explication : doit répondre `NOAUTH` ou une erreur d'authentification (remplacer les valeurs, à remplacer).

3. Test authentifié :
   ```bash
   read -rsp 'Mot de passe : ' REDISCLI_AUTH; export REDISCLI_AUTH; echo
   redis-cli --tls --cacert /chemin/CA.crt -h NOM_SERVEUR --user APPUSER SET APP:recette 1
   redis-cli --tls --cacert /chemin/CA.crt -h NOM_SERVEUR --user APPUSER DEL APP:recette
   unset REDISCLI_AUTH
   ```
   👉 Explication : la variable d'environnement évite d'exposer le mot de passe dans `ps`.

4. Contrôler mémoire et persistance :
   ```bash
   redis-cli INFO memory | grep -E 'used_memory_human|maxmemory_human'
   redis-cli INFO persistence | grep -E 'aof_enabled|rdb_last_save_time'
   ```
   👉 Explication : cohérent avec la configuration.

## 2. Production — Contrôles

Consigner la recette ; superviser mémoire, connexions, évictions, latence.

## 3. Production — Sécurité

- Supprimer toutes les clés de test.
- Ne pas laisser de variable d'environnement contenant un secret.
- Surveiller les journaux.

## Validation et retour arrière

- **Validation** : tous les contrôles réussis.
- **Retour arrière** : revenir à la configuration précédente.

## Si le problème n'est pas résolu

- [Redis — Prérequis et limites](/01-fiches-simples/debian/13/vie-du-logiciel/redis/fiche-simple-vm-debian-13-redis-prerequis-limites)
- [Redis — Installer](/01-fiches-simples/debian/13/vie-du-logiciel/redis/fiche-simple-vm-debian-13-redis-installer)
- [Redis — Configurer](/01-fiches-simples/debian/13/vie-du-logiciel/redis/fiche-simple-vm-debian-13-redis-configurer)
- [Redis — Sécuriser (ACL, TLS, pare-feu)](/01-fiches-simples/debian/13/vie-du-logiciel/redis/fiche-simple-vm-debian-13-redis-securiser)
- [Redis — Sauvegarder et restaurer](/01-fiches-simples/debian/13/vie-du-logiciel/redis/fiche-simple-vm-debian-13-redis-sauvegarder-restaurer)
- [Redis — Mise à jour et retour arrière](/01-fiches-simples/debian/13/vie-du-logiciel/redis/fiche-simple-vm-debian-13-redis-mettre-a-jour)
- [Redis — documentation officielle](https://redis.io/docs/latest/)
- [Redis — sécurité](https://redis.io/docs/latest/operate/oss_and_stack/management/security/)
- [Installation Redis avec NetBox (fiche du pack)](/01-fiches-simples/debian/13/vie-du-logiciel/postgresql/fiche-simple-vm-debian-13-netbox-installer-postgresql-redis)