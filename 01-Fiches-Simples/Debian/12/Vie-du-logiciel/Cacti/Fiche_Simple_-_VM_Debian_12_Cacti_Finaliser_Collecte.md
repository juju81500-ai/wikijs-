# Fiche_Simple_-_VM_Debian_12_Cacti_Finaliser_Collecte.md

- **Environnement** : VM Debian 12 dédiée (Apache, PHP, MariaDB, poller local)
- **OS / Version** : Debian 12 Bookworm; Cacti 1.2.31
- **Catégorie** : supervision / mise en service
- **Tags** : `debian12`, `cacti`, `snmp`, `rrdtool`, `mariadb`

---

## Problème précis à résoudre

Terminer l'assistant web et configurer un poller sur un équipement pilote.

## 1. Hors-Production (Lab / Test / POC)

1. Redémarrer Apache après configuration :
   ```bash
   sudo systemctl restart apache2
   ```
   👉 Explication : prend en compte PHP et la configuration.

2. Ouvrir l'interface en HTTPS : **https://nom-du-serveur/cacti** (nom d'exemple à remplacer), terminer l'assistant et changer les valeurs initiales.
   👉 Explication : un seul compte administrateur, sans accès de démonstration.

3. Configurer le poller (cron ou service systemd recommandé par la release) sous un compte dédié.
   👉 Explication : la collecte tourne sans utiliser un compte privilégié.

4. **Console > Create > New Device** : ajouter un équipement pilote autorisé en SNMPv3 authPriv lecture seule.
   👉 Explication : on valide la collecte sur un seul équipement avant d'étendre.

## 2. Production — Contrôles

Limiter UDP/161 aux sources nécessaires; attacher uniquement les templates utiles.

## 3. Production — Sécurité

- Interface uniquement en HTTPS.
- Aucun compte ou accès de démonstration conservé.

## Validation et retour arrière

- **Validation** : Le poller s'exécute et des graphes apparaissent pour l'équipement pilote.
- **Retour arrière** : Supprimer l'équipement pilote depuis **Console > Management > Devices**.

## Si le problème n'est pas résolu

- [Cacti — documentation officielle](https://docs.cacti.net/)
- [Cacti — installation Ubuntu/Debian](https://docs.cacti.net/Installing-Under-Ubuntu-Debian.md)
- [Guide complet — 5. Finaliser l'interface et la collecte](../../../../../02-Fiches-Completes/Debian/12/Installation-Deploiement/51_Deploiement_Cacti_1.2.31_Debian_12.md#5-finaliser-linterface-et-la-collecte)
