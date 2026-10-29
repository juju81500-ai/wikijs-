# Fiche_Simple_-_Windows_Server_2022_RDS_Sauvegarder_Restaurer

- **Environnement** : Déploiement RDS de test et dépôt de sauvegarde contrôlé
- **OS / Version** : Windows Server 2022
- **Catégorie** : Vie du logiciel / Continuité RDS
- **Tags** : `windows-server-2022`, `rds`, `sauvegarde`, `restauration`

---

## Problème précis à résoudre

Préserver la configuration RDS et les données de profils requises, puis préparer une restauration testée sans supposer qu'une copie de fichiers suffit pour restaurer une ferme.

## 1. Hors-Production (Lab / Test / POC)

1. Exporter le résultat des stratégies appliquées :
   ```powershell
   New-Item -ItemType Directory -Path 'C:\Admin\RDS-Export' -Force
   gpresult /h 'C:\Admin\RDS-Export\gpresult.html'
   ```
   👉 Explication : Crée un rapport de stratégie; le chemin est un emplacement de lab à remplacer si nécessaire.
2. Exporter l'inventaire des rôles et services :
   ```powershell
   Get-WindowsFeature RDS* | Export-Csv 'C:\Admin\RDS-Export
oles-rds.csv' -NoTypeInformation -Encoding UTF8
   Get-Service TermService | Select-Object Name, Status, StartType | Export-Csv 'C:\Admin\RDS-Export\service-rds.csv' -NoTypeInformation -Encoding UTF8
   ```
   👉 Explication : Archive un inventaire, pas les certificats privés, données de profils ou l'état complet du déploiement.
3. Dans **Gestionnaire de serveur** > **Services Bureau à distance** > **Vue d'ensemble** > **Tâches** > **Exporter la configuration de déploiement**, exporter si cette option est disponible pour la topologie.
   👉 Explication : Cet export est disponible pour certaines configurations et ne remplace pas la sauvegarde VM, les certificats avec clés privées ni les données utilisateur.
4. Sauvegarder les profils via la solution de profils approuvée, puis tester la restauration sur un hôte isolé.
   👉 Explication : Les procédures de profils itinérants/containers dépendent du produit; ne pas copier un profil actif sans consigne de l'éditeur.

## 2. Production — Contrôles

- Définir RPO/RTO, protection hors ligne/immutabilité, chiffrement et contrôle d'accès du dépôt.
- Inclure configuration, certificats et clés privées via coffre/PKI, serveurs de licences et données de profils selon leurs procédures.
- Documenter l'ordre de restauration des rôles Broker, Web Access, Gateway, Session Host et licences pour la topologie réelle.

## 3. Production — Sécurité

- Restreindre les exports contenant noms de serveurs, groupes, URL et informations d'architecture.
- Ne jamais exporter une clé privée vers un partage non protégé ni inscrire une phrase secrète dans le runbook.
- Tester dans un réseau isolé afin d'éviter les doublons d'identité ou l'exposition de sessions.

## Validation et retour arrière

- **Validation** : restaurer l'export et les données nécessaires dans un environnement isolé; vérifier la connexion pilote et les objectifs de reprise.
- **Retour arrière** : conserver les composants sources et sauvegardes immuables jusqu'à validation formelle du service restauré.

## Si le problème n'est pas résolu

- [Microsoft Learn — Exporter et importer un déploiement RDS](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds-export-import-deployment)
- [Microsoft Learn — Sauvegarde Windows Server](https://learn.microsoft.com/en-us/windows-server/administration/windows-server-backup/backup-restore)
- [Valider la recette RDS](./Fiche_Simple_-_Windows_Server_2022_RDS_Valider_Recette.md)
