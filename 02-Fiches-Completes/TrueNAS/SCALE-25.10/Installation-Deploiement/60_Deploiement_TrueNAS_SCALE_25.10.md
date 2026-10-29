# Déployer TrueNAS SCALE 25.10

- **OS / Version** : TrueNAS SCALE 25.10 Community Edition; matériel x86-64 compatible
- **Type de fiche** : Installation/Déploiement
- **Périmètre** : NAS autonome pilote, pool miroir, partage contrôlé et copie de sauvegarde
- **Catégorie** : Stockage réseau / NAS ZFS
- **Tags** : `truenas`, `scale2510`, `zfs`, `nas`, `smb`, `nfs`, `sauvegarde`

## 1. Dimensionner et préparer

Fiche simple : [dimensionner et préparer](../../../../01-Fiches-Simples/TrueNAS/SCALE-25.10/Vie-du-systeme/Fiches-par-theme/Deploiement/Fiche_Simple_-_TrueNAS_SCALE_25.10_Deploiement_Dimensionner_Preparer.md).

Confirmer matériel, contrôleur HBA, disques, réseau, capacité utile, croissance, tolérance aux pannes et clients SMB/NFS/iSCSI. La documentation TrueNAS donne 8 Go de RAM comme minimum de base et au moins deux disques de même capacité pour un pool miroir; augmenter les ressources selon nombre de disques, connexions, apps, VM et charge. Utiliser ECC lorsque le matériel le permet.

TrueNAS doit voir les disques de données directement. Éviter un contrôleur RAID matériel qui masque les disques et leurs informations SMART; utiliser HBA/JBOD compatible. TrueNAS virtualisé avec disques virtuels n'est pas recommandé pour héberger des données critiques en production.

Réserver un support de démarrage distinct (20 Go recommandé par l'installateur 25.10), un accès console/IPMI, une interface de gestion et un réseau de stockage approprié. Définir les VLANs, DNS, NTP, certificats TLS, administrateurs, partage prévu et stratégie de chiffrement des datasets.

## 2. Télécharger, vérifier et installer

Fiche simple : [télécharger, vérifier et installer](../../../../01-Fiches-Simples/TrueNAS/SCALE-25.10/Vie-du-systeme/Fiches-par-theme/Deploiement/Fiche_Simple_-_TrueNAS_SCALE_25.10_Deploiement_Telecharger_Installer.md).

Télécharger l'ISO TrueNAS SCALE 25.10 depuis la page officielle, puis vérifier SHA-256 ou signature PGP publiée avant de créer le média. Démarrer en UEFI selon le matériel et installer sur le périphérique de boot identifié; l'installateur efface le disque choisi.

Après redémarrage, utiliser l'adresse affichée dans le menu console pour ouvrir l'interface d'administration. Définir un compte admin dédié, un mot de passe unique, nom d'hôte, IP statique et DNS/NTP. Utiliser HTTPS avec un certificat approuvé et ne pas exposer l'interface à Internet.

## 3. Créer le pool et les datasets

Fiche simple : [créer le pool et les datasets](../../../../01-Fiches-Simples/TrueNAS/SCALE-25.10/Vie-du-systeme/Fiches-par-theme/Deploiement/Fiche_Simple_-_TrueNAS_SCALE_25.10_Deploiement_Pool_Datasets.md).

Planifier les vdevs en fonction de capacité, disponibilité, performances et extensions futures. Le choix de layout est difficile à modifier après création. Pour un pilote, sélectionner les disques attendus et un layout miroir simple; pour la production, faire valider le nombre de vdevs, la redondance, les spare et le plan de remplacement par le responsable stockage.

Créer des datasets enfants distincts par usage/équipe; ne jamais partager le dataset racine du pool. Examiner preset, sensibilité de casse, ACL et chiffrement avant sauvegarde des données. Créer un jeu de données et un partage SMB/NFS dédiés avec comptes nominatifs et permissions minimales.

## 4. Mettre en service le partage

Fiche simple : [mettre en service le partage](../../../../01-Fiches-Simples/TrueNAS/SCALE-25.10/Vie-du-systeme/Fiches-par-theme/Deploiement/Fiche_Simple_-_TrueNAS_SCALE_25.10_Deploiement_Partage.md).

Configurer l'interface et l'adresse de gestion; séparer réseau d'administration et flux SMB/NFS lorsque le design le prévoit. Créer le partage dans l'interface TrueNAS, vérifier l'ACL côté dataset, puis tester depuis un seul client pilote autorisé.

Valider lecture/écriture, héritage ACL, verrouillage, nommage et interruption/reprise. Surveiller pool, alertes SMART, scrubs, températures et espace; établir une fenêtre de maintenance avant extension ou remplacement des disques.

## 5. Sauvegarder et récupérer

Fiche simple : [sauvegarder et récupérer](../../../../01-Fiches-Simples/TrueNAS/SCALE-25.10/Vie-du-systeme/Fiches-par-theme/Deploiement/Fiche_Simple_-_TrueNAS_SCALE_25.10_Deploiement_Sauvegarder_Recuperer.md).

Exporter la configuration régulièrement avec **Export Password Secret Seed** lorsque nécessaire; protéger physiquement le fichier de configuration et les clés pour jeux de données chiffrés. Conserver un debug initial pour comparaison.

Les snapshots et réplications protègent contre certains scénarios mais ne remplacent pas une copie indépendante. Configurer réplication vers un autre TrueNAS ou une cible distante, ou Cloud Sync/TrueCloud conformément aux coûts et à la confidentialité. Tester un restore de fichier et une réimportation de configuration sur un appareil ou lab séparé.

## 6. Exploitation et retour arrière

Fiche simple : [exploiter et revenir en arrière](../../../../01-Fiches-Simples/TrueNAS/SCALE-25.10/Vie-du-systeme/Fiches-par-theme/Deploiement/Fiche_Simple_-_TrueNAS_SCALE_25.10_Deploiement_Exploitation_Retour.md).

- Vérifier l'état du pool et les alertes dans l'interface; ne pas lancer de scrub ou remplacement de disque sans suivre la procédure et identifier le slot/périphérique.
- Avant upgrade, vérifier les notes 25.10, sauvegarder configuration et données, puis tester l'accès aux partages.
- En cas de panne, isoler le NAS du réseau si nécessaire, ne jamais créer un nouveau pool sur les disques existants et contacter l'équipe stockage/support.
- Documenter topologie, layout, numéros de série, chiffrement, propriétaires de partages, RPO/RTO et résultats des restaurations.

## Sources

- [TrueNAS SCALE 25.10 — Installation](https://www.truenas.com/docs/scale/25.10/gettingstarted/install/installingscale/)
- [TrueNAS SCALE 25.10 — Guide matériel](https://www.truenas.com/docs/scale/25.10/gettingstarted/scalehardwareguide/)
- [TrueNAS SCALE 25.10 — Mise en place du stockage](https://www.truenas.com/docs/scale/25.10/gettingstarted/configure/setupstoragescale/)
- [TrueNAS SCALE 25.10 — Sauvegarde](https://www.truenas.com/docs/scale/25.10/gettingstarted/configure/setupbackupscale/)
- [TrueNAS — Téléchargements](https://www.truenas.com/download/)