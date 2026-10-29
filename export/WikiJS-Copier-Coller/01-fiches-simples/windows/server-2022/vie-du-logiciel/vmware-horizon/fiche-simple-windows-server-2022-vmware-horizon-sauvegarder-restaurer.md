# Fiche_Simple_-_Windows_Server_2022_VMware_Horizon_Sauvegarder_Restaurer

- **Environnement** : Serveurs Windows Server 2022 (Connection Server), vCenter, UAG, compte administrateur nominatif
- **OS / Version** : Windows Server 2022; version Horizon à vérifier auprès de l'éditeur
- **Catégorie** : VDI / Horizon

---

## Problème précis à résoudre

Sauvegarder et restaurer la configuration Horizon (LDAP du Connection Server, base d'événements, UAG).

## 1. Hors-Production (Lab / Test / POC)

1. GUI **Settings > Servers > Connection Servers > Backup** : vérifier la planification et la rétention de la sauvegarde automatique de la base de configuration.
   👉 Explication : par défaut une sauvegarde automatique existe ; confirmer la fréquence sur votre version.

2. Exporter manuellement la configuration avec l'outil officiel vdmexport (chemin d'installation à vérifier) :
```powershell
cd 'C:\Program Files\VMware\VMware View\Server\tools\bin'
.\vdmexport.exe -f CHEMIN_SAUVEGARDE\horizon-config.ldf
```
   👉 Explication : CHEMIN_SAUVEGARDE est à remplacer ; le fichier exporté est sensible.

3. Sauvegarder la base d'événements SQL (si utilisée) :
```powershell
Backup-SqlDatabase -ServerInstance 'SQL_HORIZON' -Database 'EVENT_DB' -BackupFile 'CHEMIN_SAUVEGARDE\EVENT_DB.bak'
```
   👉 Explication : SQL_HORIZON et EVENT_DB sont à remplacer.

4. Exporter la configuration UAG depuis GUI **Admin UI > Support Settings > Export Settings** et conserver le fichier chiffré.
   👉 Explication : permet de redéployer un UAG identique.

5. Restaurer en lab : arrêter le service Connection Server puis importer avec vdmimport :
```powershell
vdmimport.exe -f CHEMIN_SAUVEGARDE\horizon-config.ldf
```
   👉 Explication : vérifier les options dans la documentation de la version avant exécution.

## 2. Production — Contrôles

- Copie hors site chiffrée.
- Test de restauration périodique.

## 3. Production — Sécurité

- Mot de passe de récupération stocké en coffre.
- Accès restreint aux fichiers.

## Validation et retour arrière

- **Validation** : Fichiers de sauvegarde présents et restauration testée en lab.
- **Retour arrière** : Restaurer l'export LDAP et les snapshots, puis redémarrer les services.

## Si le problème n'est pas résolu

- [Documentation Horizon (Omnissa/VMware)](https://docs.omnissa.com/)
- [Broadcom TechDocs — Horizon](https://techdocs.broadcom.com/)
- [Fiche d'entrée du logiciel](/01-fiches-simples/logiciels/13-poste-de-travail-et-vdi/fiche-logiciel-vmware-horizon)