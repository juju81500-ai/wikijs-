# Fiche_Simple_-_VM_Debian_12_Bacula_Valider_Config_Demarrer.md

- **Environnement** : VM Debian 12 dédiée à Bacula (Director, Storage Daemon, File Daemon, catalogue PostgreSQL)
- **OS / Version** : Debian 12 Bookworm; Bacula Community 15.0.3 (backports)
- **Catégorie** : sauvegarde / services
- **Tags** : `debian12`, `bacula`, `backports`, `postgresql`, `systemd`, `firewall`

---

## Problème précis à résoudre

Tester les configurations puis démarrer Director, Storage Daemon et File Daemon.

## 1. Hors-Production (Lab / Test / POC)

1. Tester chaque configuration :
   ```bash
   sudo bacula-dir -t
   sudo bacula-sd -t
   sudo bacula-fd -t
   ```
   👉 Explication : toute erreur de ressource, de secret ou de syntaxe doit être corrigée avant de continuer.

2. Lister les unités installées :
   ```bash
   systemctl list-unit-files 'bacula*'
   ```
   👉 Explication : confirme leurs noms réels (habituellement `bacula-director`, `bacula-sd`, `bacula-fd`).

3. Activer et démarrer les services :
   ```bash
   sudo systemctl enable --now bacula-director.service bacula-sd.service bacula-fd.service
   ```
   👉 Explication : démarre les trois composants et au boot.

4. Contrôler l'état :
   ```bash
   sudo systemctl --no-pager --full status bacula-director.service bacula-sd.service bacula-fd.service
   ```
   👉 Explication : les trois unités doivent être actives, sans erreur.

## 2. Production — Contrôles

Limiter le pare-feu aux flux 9101 (console vers Director), 9102 (Director vers File Daemon) et 9103 (Director/File Daemon vers Storage Daemon) entre composants.

## 3. Production — Sécurité

- Ne jamais exposer 9101-9103 à Internet.
- Ne pas redémarrer si un test `-t` échoue.

## Validation et retour arrière

- **Validation** : les trois tests `-t` sont silencieux et les trois unités sont actives.
- **Retour arrière** : `sudo systemctl disable --now bacula-director.service bacula-sd.service bacula-fd.service`, puis restaurer `/etc/bacula` sauvegardé.

## Si le problème n'est pas résolu

- [Bacula — manuels 15.0.x](https://www.bacula.org/15.0.x-manuals/en/main/)
- [Guide complet Bacula Debian 12](../../../../../02-Fiches-Completes/Debian/12/Installation-Deploiement/68_Deploiement_Bacula_15_Debian_12_Backports.md#5-valider-la-configuration-et-demarrer-les-services)
