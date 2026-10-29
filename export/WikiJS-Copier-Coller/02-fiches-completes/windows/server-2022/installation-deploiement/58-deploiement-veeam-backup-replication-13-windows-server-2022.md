# Déployer Veeam Backup & Replication 13 sur Windows Server 2022

- **OS / Version** : Windows Server 2022; Veeam Backup & Replication 13.1.2.57
- **Type de fiche** : Installation/Déploiement
- **Périmètre** : serveur de sauvegarde autonome et protection initiale d'un hôte Hyper-V
- **Catégorie** : Sauvegarde VM / reprise après incident

## 1. Dimensionner l'infrastructure

Fiche simple : [dimensionner l'infrastructure](/01-fiches-simples/windows/server-2022/vie-du-logiciel/veeam/fiche-simple-vm-windows-server-2022-veeam-dimensionner-infrastructure).

Cette fiche cible un pilote; une installation Veeam autonome n'est pas une architecture HA/PRA complète. Calculer le débit à protéger, concurrence des jobs, taille du catalogue, fenêtre de sauvegarde, rétention, capacité de dépôt, réplication/copie hors site et bande passante de restauration.

Veeam 13.1.2.57 indique pour le serveur Windows un minimum de 8 cœurs et 16 Go de RAM, plus 500 Mo par job concurrent. Vérifier les exigences et la matrice de compatibilité courantes avant le choix final. Prévoir un serveur de sauvegarde distinct des hôtes protégés, un stockage à accès restreint et des comptes de service dédiés.

## 2. Installer le serveur de sauvegarde

Fiche simple : [installer le serveur de sauvegarde](/01-fiches-simples/windows/server-2022/vie-du-logiciel/veeam/fiche-simple-vm-windows-server-2022-veeam-installer-serveur-sauvegarde).

Sur Windows Server 2022 patché, télécharger le média Veeam 13 depuis le portail officiel, vérifier la signature/checksum publié et monter l'ISO. Lancer l'installateur, appliquer la licence autorisée et choisir l'installation du Backup Server. Vérifier les prérequis, le compte de service, le moteur PostgreSQL/SQL choisi, le dossier de configuration et les ports avec les équipes systèmes/réseau.

Ne pas exposer l'interface d'administration sur Internet. Limiter les comptes Administrateurs Veeam et les communications aux hôtes, proxies et dépôts requis par l'architecture.

## 3. Ajouter un dépôt de sauvegarde

Fiche simple : [ajouter un dépôt de sauvegarde](/01-fiches-simples/windows/server-2022/vie-du-logiciel/veeam/fiche-simple-vm-windows-server-2022-veeam-ajouter-depot-sauvegarde).

Ajouter un dépôt dédié qui ne partage pas un même chemin avec un dépôt Veeam imbriqué. Dimensionner capacité, IOPS, rétention, marge de croissance et espace temporaire de restauration.

Pour les données critiques, ajouter un dépôt Linux durci immuable ou un stockage objet avec verrouillage/rétention conforme. L'immuabilité doit être configurée selon la procédure Veeam et le stockage ciblé; elle ne remplace ni une copie hors site ni des identifiants séparés. Restreindre l'administration du dépôt et empêcher que le compte Veeam puisse facilement supprimer les copies protégées.

## 4. Créer le job Hyper-V pilote

Fiche simple : [créer le job Hyper-V pilote](/01-fiches-simples/windows/server-2022/vie-du-logiciel/veeam/fiche-simple-vm-windows-server-2022-veeam-creer-job-hyperv-pilote).

Dans la console ou l'interface Web Veeam, ajouter l'hôte/cluster Hyper-V autorisé, valider le compte de connexion et les composants déployés, puis créer un job de sauvegarde. Sélectionner une VM pilote non critique, dépôt dédié, calendrier, rétention et fenêtres sans chevauchement.

Activer le traitement cohérent avec les applications lorsqu'il est supporté et configuré; examiner les journaux VSS et credentials invités. Créer une copie de sauvegarde indépendante selon la stratégie 3-2-1-1-0 et une destination distincte du serveur principal.

## 5. Recette obligatoire

Fiche simple : [recette obligatoire](/01-fiches-simples/windows/server-2022/vie-du-logiciel/veeam/fiche-simple-vm-windows-server-2022-veeam-recette-obligatoire).

Lancer le job pilote, confirmer résultat, durée, taille, points de restauration, journal et alerte en cas d'échec. Réaliser une restauration de fichier et une restauration de VM en réseau isolé; vérifier OS, application, données, permissions et retour à l'état attendu avant de généraliser.

```powershell
Get-Service Veeam* | Select-Object Name, Status, StartType
```

Contrôler également les sessions et points de restauration dans la console Veeam; une tâche terminée avec succès n'est pas une preuve suffisante de récupérabilité.

## 6. Exploitation et reprise

Fiche simple : [exploitation et reprise](/01-fiches-simples/windows/server-2022/vie-du-logiciel/veeam/fiche-simple-vm-windows-server-2022-veeam-exploitation-reprise).

- Surveiller jobs, repositories, capacity, catalog, licences, certificats et alertes.
- Sauvegarder la configuration Veeam avec encryption key et conserver les secrets séparément.
- Tester régulièrement une restauration complète dans un réseau isolé et un scénario de perte du serveur Veeam.
- Mettre à niveau après validation de compatibilité, sauvegarde de configuration et test pilote.
- En incident ransomware, isoler les composants, préserver les journaux et restaurer depuis une copie immuable/hors ligne validée.

## Sources

- [Veeam 13 — Installer Backup & Replication sous Windows](https://helpcenter.veeam.com/docs/vbr/userguide/install_vbr.html)
- [Veeam 13 — Exigences du serveur de sauvegarde](https://helpcenter.veeam.com/docs/vbr/userguide/system_requirements_backup_server.html)
- [Veeam 13 — Repositories de sauvegarde](https://helpcenter.veeam.com/docs/vbr/userguide/backup_repository.html)
- [Veeam 13 — Dépôt durci](https://helpcenter.veeam.com/docs/vbr/userguide/hardened_repository.html)
- [Veeam 13 — Créer des jobs Hyper-V](https://helpcenter.veeam.com/docs/vbr/userguide/backup_job_hv.html)
- [Veeam 13 — Guide utilisateur](https://helpcenter.veeam.com/docs/vbr/userguide/)