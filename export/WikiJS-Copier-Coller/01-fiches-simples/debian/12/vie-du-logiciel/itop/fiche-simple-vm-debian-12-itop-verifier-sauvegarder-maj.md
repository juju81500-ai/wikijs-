# Fiche_Simple_-_VM_Debian_12_iTop_Verifier_Sauvegarder_MAJ.md

- **Environnement** : VM Linux dédiée avec Apache, PHP 8.2 ou 8.3 et MariaDB 10.11 (serveur ITSM/CMDB)
- **OS / Version** : Debian 12 Bookworm (ou Ubuntu Server 24.04 LTS); iTop Community 3.3.0
- **Catégorie** : ITSM / CMDB / helpdesk

---

## Problème précis à résoudre

Valider l'installation, sauvegarder et préparer les mises à jour.

## 1. Hors-Production (Lab / Test / POC)

1. Tester connexion, création d'un ticket, d'une CI et les autorisations avec un compte non administrateur.
   👉 Explication : valide l'usage réel.

2. Contrôler les journaux Apache/PHP :
   ```bash
   sudo tail -n 50 /var/log/apache2/error.log
   ```
   👉 Explication : repère les erreurs; vérifier aussi l'exécution des tâches planifiées.

3. Sauvegarder la base de façon cohérente (le mot de passe est demandé de manière interactive, jamais en argument) :
   ```bash
   sudo mysqldump --single-transaction -u itop -p itop > ~/itop-backup.sql
   ```
   👉 Explication : `--single-transaction` donne une sauvegarde cohérente.

4. Sauvegarder aussi `conf/production/config-itop.php`, les extensions et les fichiers de données.
   👉 Explication : permettent de reconstruire l'application; tester une restauration isolée.

5. Avant toute mise à jour, sauvegarder puis suivre le guide de migration de la version cible.
   👉 Explication : ne pas mélanger code nouveau et schéma ancien sans exécuter le setup de migration.

## 2. Production — Contrôles

Pour des volumes importants, utiliser une solution de sauvegarde éprouvée; vérifier la limite iTop pour les archives internes dépassant 68 Go.

## 3. Production — Sécurité

- Chiffrer et restreindre l'accès aux sauvegardes (elles contiennent des données de la CMDB).

## Validation et retour arrière

- **Validation** : une restauration isolée de la sauvegarde fonctionne.
- **Retour arrière** : restaurer la base et les fichiers de configuration sauvegardés avant la mise à jour.

## Si le problème n'est pas résolu

- [iTop — sauvegarde](https://www.itophub.io/wiki/page?id=latest:admin:backup)
- [iTop — installation et mise à niveau](https://www.itophub.io/wiki/page?id=latest:install:start)
- [Guide complet](/02-fiches-completes/transverses/multi-os/installation-deploiement/40-deploiement-itop-3-3-debian12-ubuntu2404#7-verifier-sauvegarder-et-mettre-a-jour)