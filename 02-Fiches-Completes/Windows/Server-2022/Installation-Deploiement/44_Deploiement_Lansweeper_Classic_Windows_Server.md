# Déployer Lansweeper Classic sur Windows Server

- **OS / Version** : Windows Server 2022 recommandé; Lansweeper Classic maintenu selon la matrice officielle
- **Type de fiche** : Installation/Déploiement
- **Environnement** : Serveur Windows x64, SQL LocalDB ou SQL Server selon l'échelle
- **Machine ciblée** : Serveur d'inventaire Windows
- **Catégorie** : Inventaire de parc / découverte réseau
- **Tags** : `lansweeper`, `windows-server-2022`, `inventaire`, `wmi`, `snmp`, `sql-server`

## 1. Choisir la variante et préparer les droits

Fiche simple : [choisir la variante et préparer les droits](../../../../01-Fiches-Simples/Windows/Toutes-versions/Vie-du-logiciel/Lansweeper/Fiche_Simple_-_VM_Windows_Server_Lansweeper_Choisir_Variante_Droits.md).

Cette fiche porte sur **Lansweeper Classic on-premises**; le produit Lansweeper Platform est une offre distincte. Vérifier que la version Classic et la licence conviennent au besoin. L'édition Easy installe web, service de scan et SQL LocalDB sur une machine et convient aux petits environnements; SQL LocalDB est limité à 10 Go. Utiliser SQL Server et une architecture distribuée si le volume/scanning l'exige.

La machine d'installation doit être Windows 64 bits, non-Home/non-Core/non-Starter, avec .NET Framework 4.8 à jour. Windows Server est recommandé au-delà de 1 000 actifs. Prévoir sauvegarde, DNS, certificat HTTPS et un compte d'administration nominatif.

## 2. Installer le serveur

Fiche simple : [installer le serveur Lansweeper](../../../../01-Fiches-Simples/Windows/Toutes-versions/Vie-du-logiciel/Lansweeper/Fiche_Simple_-_VM_Windows_Server_Lansweeper_Installer_Serveur.md).

1. Télécharger l'installateur depuis le site officiel et vérifier l'origine du fichier.
2. Choisir Easy Install pour une petite installation ou Advanced Install pour séparer scanning service, SQL Server et web console.
3. Pour une installation répartie, installer la base d'abord, puis les services de scan et enfin la console; partager la clé `Encryption.txt` générée avec les autres serveurs de scan via le coffre et suivre le guide officiel.
4. Appliquer la licence ou lier l'installation à la plateforme selon le type de licence.
5. Configurer le compte de connexion à la console et activer uniquement les rôles nécessaires.

## 3. Définir un périmètre pilote

Fiche simple : [définir un périmètre pilote](../../../../01-Fiches-Simples/Windows/Toutes-versions/Vie-du-logiciel/Lansweeper/Fiche_Simple_-_VM_Windows_Server_Lansweeper_Definir_Perimetre_Pilote.md).

Dans le First Run Wizard, commencer par une petite plage IP explicitement autorisée, appartenant à l'organisation et validée par l'équipe réseau. Ne pas scanner des réseaux tiers ou non approuvés.

Créer des identifiants de découverte distincts et à privilèges minimaux. Pour Windows, préférer un compte de lecture/découverte dédié aux droits administrateur de domaine; l'accès WMI et la lecture AD doivent être limités aux systèmes concernés. Pour SNMP, utiliser SNMPv3 en lecture seule lorsque disponible. Garder les secrets dans le coffre du produit et limiter leur portée par domaine/plage.

## 4. Configurer les méthodes de scan

Fiche simple : [configurer les méthodes de scan](../../../../01-Fiches-Simples/Windows/Toutes-versions/Vie-du-logiciel/Lansweeper/Fiche_Simple_-_VM_Windows_Server_Lansweeper_Configurer_Methodes_Scan.md).

- Pour les postes Windows, choisir scan agentless WMI ou LsAgent. L'agent réduit les besoins d'ouverture de ports entrants et peut servir aux appareils hors site.
- Pour Linux/macOS, privilégier les agents ou SSH avec compte restreint.
- Pour les équipements réseau/NAS, configurer SNMPv3 lecture seule et une liste de cibles définie.
- Espacer et limiter le volume des scans; ne pas lancer de découverte large sans fenêtre approuvée.

Les communications doivent suivre les ports officiels correspondant au produit, à l'agent et au scénario sélectionnés. N'ouvrez pas les règles firewall à tout le réseau en dépannage.

## 5. Recette

Fiche simple : [recette Lansweeper](../../../../01-Fiches-Simples/Windows/Toutes-versions/Vie-du-logiciel/Lansweeper/Fiche_Simple_-_VM_Windows_Server_Lansweeper_Recette.md).

- Vérifier que le service Lansweeper démarre, que la console HTTPS est accessible et que la base sélectionnée est en ligne.
- Scanner un petit groupe d'actifs connus; comparer modèle, OS, numéro de série et utilisateur aux données sources.
- Lire les erreurs de scan et ajuster une seule permission ou règle à la fois.
- Vérifier séparation des rôles, accès aux rapports et journaux/audit trail.
- Valider l'impact réseau avant d'ajouter d'autres plages.

## 6. Sauvegarde et maintenance

Fiche simple : [sauvegarde et maintenance](../../../../01-Fiches-Simples/Windows/Toutes-versions/Vie-du-logiciel/Lansweeper/Fiche_Simple_-_VM_Windows_Server_Lansweeper_Sauvegarde_Maintenance.md).

Avant toute mise à jour, sauvegarder la base SQL, rapports, configuration, clé `Encryption.txt`, identité des serveurs de scan et certificat. Tester une restauration en lab. Mettre à jour chaque composant selon les instructions de la version et confirmer que la clé de chiffrement des identifiants reste cohérente.

## Sources

- [Lansweeper Classic — Prérequis d'installation](https://docs.lansweeper.com/classic/docs/lansweeper-installation-requirements.md)
- [Lansweeper Classic — Installer on-premises](https://docs.lansweeper.com/classic/docs/install-lansweeper-on-prem.md)
- [Lansweeper Classic — Identifiants de scan](https://docs.lansweeper.com/classic/docs/create-and-map-scanning-credentials.md)
- [Lansweeper Classic — Prérequis scan Windows domaine](https://docs.lansweeper.com/classic/docs/windows-domain-scanning-requirements.md)
- [Lansweeper — Plateforme et Classic](https://docs.lansweeper.com/classic/docs/comparing-lansweeper-platform-and-lansweeper-classic.md)