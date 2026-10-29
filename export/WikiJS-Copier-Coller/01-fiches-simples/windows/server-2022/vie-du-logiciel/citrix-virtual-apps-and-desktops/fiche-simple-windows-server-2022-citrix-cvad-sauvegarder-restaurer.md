# Fiche_Simple_-_Windows_Server_2022_Citrix_CVAD_Sauvegarder_Restaurer

- **Environnement** : Serveurs Windows Server 2022 (Delivery Controller, StoreFront, licences, SQL) et VM VDA, compte administrateur nominatif
- **OS / Version** : Windows Server 2022; version CVAD à vérifier auprès de l'éditeur
- **Catégorie** : VDI / virtualisation d'applications / Citrix

---

## Problème précis à résoudre

Sauvegarder et restaurer les bases SQL du site, la configuration StoreFront et les licences CVAD.

## 1. Hors-Production (Lab / Test / POC)

1. Identifier les bases du site. PowerShell :
```powershell
Add-PSSnapin Citrix*
Get-BrokerDBConnection
Get-ConfigDBConnection
Get-MonitorDBConnection
```
   👉 Explication : retourne les chaînes de connexion des bases ; noter les noms réels.

2. Sauvegarder les bases côté SQL Server (module SqlServer requis) :
```powershell
Backup-SqlDatabase -ServerInstance 'SQL_CITRIX' -Database 'SITE_DB' -BackupFile 'CHEMIN_SAUVEGARDE\SITE_DB.bak' -CompressionOption On
```
   👉 Explication : SQL_CITRIX, SITE_DB et CHEMIN_SAUVEGARDE sont à remplacer ; répéter pour les bases de supervision et de journalisation ; privilégier un plan SQL Agent planifié.

3. Exporter la configuration StoreFront : GUI console StoreFront **Server Group > Export Configuration** (libellé à vérifier selon version), enregistrer le fichier ZIP hors du serveur.
   👉 Explication : ce fichier peut contenir des éléments sensibles ; le chiffrer et le stocker sécurisé.

4. Copier les fichiers de licence et noter les certificats (export avec clé privée protégé par mot de passe saisi, jamais écrit).
   👉 Explication : permet de reconstruire le serveur de licences.

5. Test de restauration en lab : restaurer SITE_DB sur une instance de test avec RESTORE DATABASE puis pointer un Controller vers elle.
   👉 Explication : une sauvegarde n'est valide que si une restauration a été testée.

## 2. Production — Contrôles

- Planifier les sauvegardes complètes et journaux selon le RPO.
- Copie hors site et test de restauration trimestriel.

## 3. Production — Sécurité

- Chiffrer les sauvegardes et limiter l'accès NTFS/SQL.
- Séparer le stockage des sauvegardes du serveur SQL.

## Validation et retour arrière

- **Validation** : Fichiers .bak présents et restauration testée.
- **Retour arrière** : Restaurer les bases dans l'ordre site puis supervision, puis relancer les services Citrix.

## Si le problème n'est pas résolu

- [Citrix — documentation produit CVAD](https://docs.citrix.com/en-us/citrix-virtual-apps-desktops)
- [Citrix — System requirements](https://docs.citrix.com/en-us/citrix-virtual-apps-desktops/system-requirements.html)
- [Fiche d'entrée du logiciel](/01-fiches-simples/logiciels/13-poste-de-travail-et-vdi/fiche-logiciel-citrix-virtual-apps-and-desktops)