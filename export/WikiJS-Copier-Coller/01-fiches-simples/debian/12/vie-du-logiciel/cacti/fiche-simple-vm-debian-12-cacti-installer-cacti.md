# Fiche_Simple_-_VM_Debian_12_Cacti_Installer_Cacti.md

- **Environnement** : VM Debian 12 dédiée (Apache, PHP, MariaDB, poller local)
- **OS / Version** : Debian 12 Bookworm; Cacti 1.2.31
- **Catégorie** : supervision / installation

---

## Problème précis à résoudre

Déployer les fichiers Cacti 1.2.31 de façon vérifiée.

## 1. Hors-Production (Lab / Test / POC)

1. Télécharger la release 1.2.31 depuis le projet officiel (https://www.cacti.net/) ou cloner explicitement le tag correspondant.
   👉 Explication : on utilise une version figée et connue.

2. Contrôler le checksum ou la signature publiés par le projet avant déploiement.
   👉 Explication : garantit que l'archive n'a pas été altérée.

3. Placer les fichiers dans un chemin dédié, par exemple `/var/www/html/cacti`, avec le propriétaire web attendu :
   ```bash
   sudo chown -R www-data:www-data /var/www/html/cacti
   ```
   👉 Explication : www-data est l'utilisateur d'Apache sous Debian.

4. Lancer Composer selon le guide officiel Cacti (https://docs.cacti.net/Installing-Under-Ubuntu-Debian.md).
   👉 Explication : installe les dépendances PHP de la release.

## 2. Production — Contrôles

Conserver le confinement de Debian et les profils du serveur web.

## 3. Production — Sécurité

- Ne pas désactiver AppArmor ni SELinux; en cas de refus, diagnostiquer l'événement et créer une règle minimale.
- Ne pas utiliser d'anciennes commandes d'exemple qui déplacent arbitrairement des répertoires.

## Validation et retour arrière

- **Validation** : Les fichiers sont en place et appartiennent à l'utilisateur web.
- **Retour arrière** : Supprimer le répertoire de test créé; la base n'est pas encore touchée.

## Si le problème n'est pas résolu

- [Cacti — documentation officielle](https://docs.cacti.net/)
- [Cacti — installation Ubuntu/Debian](https://docs.cacti.net/Installing-Under-Ubuntu-Debian.md)
- [Guide complet — 3. Installer Cacti](/02-fiches-completes/debian/12/installation-deploiement/51-deploiement-cacti-1-2-31-debian-12#3-installer-cacti)