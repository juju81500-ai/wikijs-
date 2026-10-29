# Fiche_Simple_-_VM_Debian_12_Bacula_Examiner_Ressources_Stockage.md

- **Environnement** : VM Debian 12 dédiée à Bacula (Director, Storage Daemon, File Daemon, catalogue PostgreSQL)
- **OS / Version** : Debian 12 Bookworm; Bacula Community 15.0.3 (backports)
- **Catégorie** : sauvegarde / configuration
- **Tags** : `debian12`, `bacula`, `backports`, `postgresql`, `storage`, `director`

---

## Problème précis à résoudre

Identifier les noms exacts de ressources Bacula et vérifier le répertoire de stockage.

## 1. Hors-Production (Lab / Test / POC)

1. Lister les fichiers inclus dans le Director :
   ```bash
   grep -n '^[[:space:]]*@' /etc/bacula/bacula-dir.conf
   ```
   👉 Explication : repère les fragments de configuration déjà chargés.

2. Lister les ressources définies :
   ```bash
   grep -nE '^[[:space:]]*(Name|Address|Device|Archive Device|Pool|FileSet|Storage)[[:space:]]*=' /etc/bacula/bacula-dir.conf /etc/bacula/bacula-sd.conf /etc/bacula/bacula-fd.conf
   ```
   👉 Explication : relève les noms du Director, client, Storage, Device, Pool et FileSet; ils doivent correspondre entre fichiers.

3. Vérifier le `Archive Device` relevé (chemin d'exemple à remplacer par la valeur trouvée) :
   ```bash
   ls -ld /var/lib/bacula/storage
   df -h /var/lib/bacula
   ```
   👉 Explication : le répertoire doit exister, être accessible en écriture au compte du service et disposer de place.

## 2. Production — Contrôles

Utiliser un volume séparé, surveillé et protégé contre l'accès depuis les clients.

## 3. Production — Sécurité

- Ne pas copier les mots de passe de configuration dans un ticket, un dépôt Git ou un wiki.
- Le stockage fourni par le paquet convient aux essais seulement.

## Validation et retour arrière

- **Validation** : les noms de ressources sont relevés et le répertoire de stockage est inscriptible et suffisant.
- **Retour arrière** : lecture seule: aucun retour arrière nécessaire.

## Si le problème n'est pas résolu

- [Bacula — manuels 15.0.x](https://www.bacula.org/15.0.x-manuals/en/main/)
- [Guide complet Bacula Debian 12](../../../../../02-Fiches-Completes/Debian/12/Installation-Deploiement/68_Deploiement_Bacula_15_Debian_12_Backports.md#3-examiner-les-ressources-et-le-stockage)
