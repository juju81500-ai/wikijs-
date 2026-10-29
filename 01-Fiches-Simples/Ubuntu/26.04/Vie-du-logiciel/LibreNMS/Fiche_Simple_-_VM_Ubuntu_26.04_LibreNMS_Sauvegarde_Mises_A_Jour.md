# Fiche_Simple_-_VM_Ubuntu_26.04_LibreNMS_Sauvegarde_Mises_A_Jour.md

- **Environnement** : VM Ubuntu Server 26.04 dédiée à LibreNMS (Nginx, PHP-FPM, MariaDB, SNMP)
- **OS / Version** : Ubuntu Server 26.04 LTS; LibreNMS 26.10.2; PHP 8.5
- **Catégorie** : supervision / maintenance
- **Tags** : `ubuntu2604`, `librenms`, `snmpv3`, `nginx`, `mariadb`

---

## Problème précis à résoudre

Sauvegarder LibreNMS et le mettre à jour avec la procédure officielle.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder la base MariaDB, `/opt/librenms/.env` (contient `APP_KEY`), les configurations Nginx/PHP/SNMP et les chemins RRD/logs requis.
   👉 Explication : sans `.env` ni base, la restauration est impossible.

2. Exemple d'export de la base :
   ```bash
   sudo mariadb-dump --single-transaction librenms > librenms.sql
   ```
   👉 Explication : Exporte la base (authentification par socket root, aucun mot de passe en argument).

3. Chiffrer les sauvegardes et tester une restauration hors production.
   👉 Explication : une sauvegarde non testée n'est pas fiable.

4. Avant mise à jour : lire les notes de version, sauvegarder, puis suivre la procédure officielle; ensuite lancer `validate.php`.
   👉 Explication : contrôle poller, scheduler et collecte complète.

## 2. Production — Contrôles

Planifier les sauvegardes et conserver les notes de version consultées.

## 3. Production — Sécurité

- Le dump et `.env` contiennent des secrets : chiffrer et restreindre l'accès.

## Validation et retour arrière

- **Validation** : sauvegarde chiffrée existante, restauration testée, `validate.php` OK après mise à jour.
- **Retour arrière** : restaurer base et `.env` depuis la sauvegarde ou le snapshot de la VM.

## Si le problème n'est pas résolu

- [LibreNMS — Release 26.10.2](https://github.com/librenms/librenms/releases/tag/26.10.2)
- [LibreNMS — Installation](https://docs.librenms.org/Installation/Install-LibreNMS/)
- [Guide complet — étape 8](../../../../../02-Fiches-Completes/Ubuntu/26.04/Installation-Deploiement/46_Deploiement_LibreNMS_26.10.2_Ubuntu_26.04.md#8-sauvegarde-et-mises-a-jour)
