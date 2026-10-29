# Déployer TrueNAS CORE 13.0 (FreeBSD)

- **OS / Version** : TrueNAS CORE, branche documentaire 13.0 (appliance FreeBSD); numéro de build exact à relever sur l'ISO téléchargé
- **Type de fiche** : Installation/Déploiement
- **Périmètre** : installation en VM de laboratoire, pool ZFS, partage SMB, snapshots, sauvegarde de la configuration
- **Catégorie** : stockage NAS / ZFS

## 1. Statut du produit et décision

Fiche simple : [décider du statut du produit](/01-fiches-simples/truenas/core-13-0/vie-du-systeme/fiches-par-theme/deploiement/fiche-simple-truenas-core-13-0-deploiement-statut-decision).

TrueNAS CORE est la variante FreeBSD; [TrueNAS SCALE 25.10](/02-fiches-completes/truenas/scale-25-10/installation-deploiement/60-deploiement-truenas-scale-25-10) est la variante Linux déjà documentée dans ce pack. La documentation CORE consultée le 29 octobre 2026 suit la branche 13.0. La page de téléchargement officielle TrueNAS vérifiée ce jour présente la « Community Edition » et ne met pas CORE en avant : **le build CORE 13.0 à jour, sa disponibilité en téléchargement et son statut de support doivent être confirmés par l'équipe avant tout usage de production.** Aucun numéro de version n'est donc figé ici. Pour un nouveau déploiement sans contrainte FreeBSD, préférer SCALE; réserver CORE à un parc existant, à une migration ou à un laboratoire.

## 2. Prérequis

Fiche simple : [vérifier les prérequis et l'ISO](/01-fiches-simples/truenas/core-13-0/vie-du-systeme/fiches-par-theme/deploiement/fiche-simple-truenas-core-13-0-deploiement-prerequis).

Selon la documentation matérielle CORE 13.0 : processeur x86-64 à deux cœurs, 8 Go de RAM, périphérique de démarrage SSD de 16 Go, au moins deux disques de données de taille identique pour un pool. Éviter SMR, clés USB comme disque de boot et pool sur un seul disque ou en stripe. En VM de test : 8 Go de RAM, un disque d'au moins 8 Go pour le système (20 Go recommandés pour l'ISO standard), au moins un disque de 4 Go pour les données, réseau en bridge, type d'OS FreeBSD 64 bits et démarrage BIOS sous VMware. Les disques doivent être présentés bruts à ZFS (pas de RAID matériel).

Télécharger l'ISO depuis la source officielle iXsystems et contrôler son empreinte avec les informations publiées au même endroit avant de l'attacher à la VM. Si aucune empreinte n'est publiée pour le fichier obtenu, arrêter et escalader.

## 3. Installer (laboratoire)

Fiche simple : [installer en laboratoire](/01-fiches-simples/truenas/core-13-0/vie-du-systeme/fiches-par-theme/deploiement/fiche-simple-truenas-core-13-0-deploiement-installer-laboratoire).

1. Créer la VM, attacher l'ISO, démarrer et choisir **Install/Upgrade**.
2. Sélectionner le disque de démarrage. **L'installateur efface le disque choisi** : vérifier le disque avant de confirmer.
3. Définir le mot de passe du compte `root` avec un secret long, conservé dans le gestionnaire de secrets.
4. Choisir le mode de démarrage adapté (BIOS en VMware d'après la documentation).
5. À la fin, arrêter la VM, retirer l'ISO, puis redémarrer. Le menu console affiche l'adresse IP de l'interface web.
6. Attribuer une adresse IP fixe depuis le menu console, puis se connecter à l'interface web en HTTPS depuis un poste d'administration. Ne pas exposer l'interface sur Internet.

## 4. Créer un pool et un partage SMB

Fiche simple : [créer un pool et un partage SMB](/01-fiches-simples/truenas/core-13-0/vie-du-systeme/fiches-par-theme/deploiement/fiche-simple-truenas-core-13-0-deploiement-pool-partage-smb).

1. **Storage > Pools > Add** : créer un pool avec redondance (miroir ou RAIDZ) selon le nombre de disques. La création **détruit le contenu des disques sélectionnés**; ne sélectionner que les disques prévus.
2. Créer un dataset par usage (ne pas partager la racine du pool).
3. **Accounts** : créer un utilisateur de service et un groupe; ne pas utiliser `root` pour les partages.
4. **Sharing > Windows Shares (SMB)** : ajouter le chemin du dataset, activer le service SMB, tester l'accès depuis un client de test. Les ACL et l'intégration Active Directory se traitent dans une procédure distincte.

## 5. Snapshots et sauvegarde de configuration

Fiche simple : [gérer snapshots et sauvegarde de configuration](/01-fiches-simples/truenas/core-13-0/vie-du-systeme/fiches-par-theme/deploiement/fiche-simple-truenas-core-13-0-deploiement-snapshots-config).

- **Storage > Snapshots > Add** : créer un snapshot du dataset de test, puis une **tâche de snapshot périodique** avec une rétention définie.
- Pour récupérer des données, utiliser **Clone to new dataset** puis partager le clone, comme le recommande la documentation. Le **rollback** d'un dataset est destructif pour les données postérieures au snapshot et peut faire échouer les tâches de réplication : à éviter en production.
- **System > General > Save Config** après chaque changement de configuration. L'option « Export Password Secret Seed » permet de restaurer sur un autre périphérique de démarrage mais produit un fichier à protéger comme un secret. Sauvegarder séparément les clés SSH (`/usr/local/etc/ssh/ssh_host_*` et `/root/.ssh`), car elles ne sont pas dans la base de configuration. Une copie automatique de la base est aussi écrite chaque jour à 03:45 dans le dataset système, mais elle disparaît avec le pool de boot si celui-ci est perdu. Copier le fichier hors de la machine.
- Les snapshots ne remplacent pas une sauvegarde hors machine : répliquer vers un autre système ou utiliser une des solutions de sauvegarde du pack.

## 6. Validation

Fiche simple : [valider le déploiement](/01-fiches-simples/truenas/core-13-0/vie-du-systeme/fiches-par-theme/deploiement/fiche-simple-truenas-core-13-0-deploiement-validation).

- L'interface web répond; l'état du pool est `ONLINE` dans **Storage > Pools** et `zpool status` (Shell) ne signale aucune erreur.
- Un client accède au partage SMB avec le compte de service et un utilisateur non autorisé est refusé.
- Un snapshot existe; un fichier supprimé dans le dataset de test est récupéré via un clone.
- Un fichier de configuration `.db` est téléchargé, stocké hors du NAS et son contenu n'est pas exposé.
- L'envoi d'alertes (e-mail) est configuré et testé.

## 7. Retour arrière

Fiche simple : [préparer le retour arrière](/01-fiches-simples/truenas/core-13-0/vie-du-systeme/fiches-par-theme/deploiement/fiche-simple-truenas-core-13-0-deploiement-retour-arriere).

Avant toute mise à jour ou changement : exporter la configuration et prendre un snapshot de la VM (laboratoire). Pour revenir à un état précédent de la configuration, utiliser **Upload Config**. **Reset Config** remet l'appareil aux paramètres d'usine et force un nouveau mot de passe : à utiliser seulement après export de la configuration. Si un pool est détruit ou des disques sont effacés, aucune procédure de retour n'existe en dehors d'une sauvegarde externe. La mise à jour majeure vers un autre produit (SCALE) n'est pas décrite ici : suivre la documentation officielle de migration et valider d'abord en laboratoire.

## Sources

- [TrueNAS — documentation CORE 13.0](https://www.truenas.com/docs/core/13.0/)
- [TrueNAS CORE 13.0 — guide matériel](https://www.truenas.com/docs/core/13.0/gettingstarted/corehardwareguide/)
- [TrueNAS CORE 13.0 — installation](https://www.truenas.com/docs/core/13.0/gettingstarted/install/)
- [TrueNAS CORE 13.0 — création de pool](https://www.truenas.com/docs/core/13.0/coretutorials/storage/pools/poolcreate/)
- [TrueNAS CORE 13.0 — partage SMB](https://www.truenas.com/docs/core/13.0/coretutorials/sharing/smb/smbshare/)
- [TrueNAS CORE 13.0 — snapshots](https://www.truenas.com/docs/core/13.0/coretutorials/storage/snapshots/)
- [TrueNAS CORE 13.0 — sauvegardes de configuration](https://www.truenas.com/docs/core/13.0/coretutorials/systemconfiguration/usingconfigurationbackups/)
- [TrueNAS — page de téléchargement officielle](https://www.truenas.com/download/)
- [TrueNAS — Software Status](https://www.truenas.com/docs/softwarestatus/)

Le statut de support et la version précise de CORE n'ont pas été confirmés; l'installation et la restauration n'ont pas été testées. Conserver les statuts **À revoir** et **À tester**.