# Déployer Bareos 25 sur Debian 13

- **OS / Version** : Debian 13 Trixie x86-64; Bareos 25 community, dépôt validé
- **Type de fiche** : Installation/Déploiement
- **Périmètre** : Director, Storage Daemon, File Daemon et catalogue PostgreSQL dans un lab
- **Catégorie** : Sauvegarde réseau et restauration granulaire

## 1. Concevoir l'architecture

Fiche simple : [cadrer l'architecture Bareos](/01-fiches-simples/debian/13/vie-du-logiciel/bareos/fiche-simple-vm-debian-13-bareos-cadrer-architecture).

Bareos repose sur un Director, un ou plusieurs Storage Daemons, un File Daemon par client et un catalogue PostgreSQL. Pour la production, séparer les rôles selon débit et criticité; isoler le stockage, protéger catalogue et configurations, et prévoir une copie hors site. La communauté recommande de tester les restaurations avant d'activer des données réelles.

Définir clients, FileSets, schedules, pools/volumes, rétention catalogue et RPO/RTO. Restreindre les ports Bareos (Director/Storage/File Daemon) aux composants concernés; chiffrer les communications avec TLS et garder les secrets de ressources hors documentation.

## 2. Installer les paquets Debian 13

Fiche simple : [installer les paquets Bareos](/01-fiches-simples/debian/13/vie-du-logiciel/bareos/fiche-simple-vm-debian-13-bareos-installer-paquets).

Choisir Bareos 25 et le dépôt communautaire stable/current compatible avec Trixie. Télécharger le script de dépôt officiel dans un fichier, vérifier l'origine et lire les modifications avant exécution; ne pas lancer un script réseau non inspecté en root.

```bash
sudo apt update
sudo apt install -y ca-certificates curl gnupg
```

Après configuration du dépôt et de sa clé selon la documentation, installer PostgreSQL puis les paquets Bareos métas `bareos` (serveur complet) et les composants requis. Vérifier le choix du catalogue PostgreSQL lors de l'installation et les versions candidates avant l'acceptation.

## 3. Préparer le catalogue et les secrets

Fiche simple : [configurer catalogue et secrets](/01-fiches-simples/debian/13/vie-du-logiciel/bareos/fiche-simple-vm-debian-13-bareos-catalogue-secrets).

Le Director requiert un catalogue PostgreSQL. Confirmer que le service PostgreSQL est actif et que le schéma Bareos a été initialisé. Les fichiers de configuration se trouvent généralement sous `/etc/bareos/`, en ressources séparées dans `bareos-dir.d`, `bareos-sd.d` et `bareos-fd.d`.

Remplacer les secrets par défaut par des valeurs fortes et uniques entre Director, Storage et File Daemons. Protéger les permissions des fichiers, activer TLS mutuel comme prévu par la documentation et conserver une copie chiffrée des configurations/certificats hors du serveur.

## 4. Démarrer les services et vérifier la syntaxe

Fiche simple : [démarrer un job pilote](/01-fiches-simples/debian/13/vie-du-logiciel/bareos/fiche-simple-vm-debian-13-bareos-demarrer-job-pilote).

```bash
sudo systemctl enable --now bareos-director.service bareos-storage.service bareos-filedaemon.service
sudo systemctl --no-pager status bareos-director.service bareos-storage.service bareos-filedaemon.service
sudo -u bareos /usr/sbin/bareos-dir -t
sudo -u bareos /usr/sbin/bareos-sd -t
sudo /usr/sbin/bareos-fd -t
```

Configurer un FileSet pilote, un client, un job planifié et un pool de volumes disque dédié. Lancer d'abord un job manuel dans la console `bconsole`; vérifier le JobId, le catalogue, le Volume et les journaux du Director/Storage/File Daemon.

## 5. Prouver la restauration

Fiche simple : [valider une restauration pilote](/01-fiches-simples/debian/13/vie-du-logiciel/bareos/fiche-simple-vm-debian-13-bareos-valider-restauration).

Exécuter `restore` depuis `bconsole`, sélectionner le client, le jeu de fichiers et le point de restauration; vérifier attentivement le client cible et le champ **Where** avant de démarrer. Pour le premier test, restaurer vers un répertoire temporaire non utilisé, comparer contenu, permissions et propriétaire, puis nettoyer les données d'essai.

Prévoir jobs de sauvegarde du catalogue et bootstrap, copie hors site des médias et configuration, rétention distincte pour fichiers/jobs/volumes, et exercices périodiques de restauration. Bareos seul n'est pas un PRA complet.

## 6. Exploitation et durcissement

Fiche simple : [exploiter et durcir Bareos](/01-fiches-simples/debian/13/vie-du-logiciel/bareos/fiche-simple-vm-debian-13-bareos-exploiter-durcir).

- Restreindre l'accès à `bconsole`, aux ressources de configuration et à PostgreSQL.
- Sauvegarder le catalogue, les fichiers de configuration et bootstrap sur une cible indépendante.
- Surveiller jobs échoués, capacité des volumes, prune/catalogue, dérive d'horloge, certificats et composants clients.
- Tester les upgrades du Director, Storage et File Daemons en staging et respecter la compatibilité des versions.
- Documenter une procédure de restauration de serveur bare metal séparée d'une restauration de fichiers.

## Sources

- [Bareos 25 — Installer le serveur](https://docs.bareos.org/IntroductionAndTutorial/InstallingBareos.html)
- [Bareos — Installer un client](https://docs.bareos.org/IntroductionAndTutorial/InstallingBareosClient.html)
- [Bareos — Démarrage et validation des configurations](https://docs.bareos.org/IntroductionAndTutorial/GettingStartedWithBareos.html)
- [Bareos — Commande de restauration](https://docs.bareos.org/TasksAndConcepts/TheRestoreCommand.html)
- [Bareos — Éléments critiques avant production](https://docs.bareos.org/IntroductionAndTutorial/CriticalItemsToImplementBeforeProduction.html)