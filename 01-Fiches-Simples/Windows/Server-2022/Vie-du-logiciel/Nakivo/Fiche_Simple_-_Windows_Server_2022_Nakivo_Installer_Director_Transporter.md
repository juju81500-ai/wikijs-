# Fiche_Simple_-_Windows_Server_2022_Nakivo_Installer_Director_Transporter

- **Environnement** : `Serveur Windows Server 2022 (VM ou physique), compte administrateur local ou de domaine nominatif`
- **OS / Version** : `Windows Server 2022 (Desktop Experience ou Core selon support de la version); vérifier la compatibilité et la version courante du produit auprès de l'éditeur`
- **Catégorie** : `sauvegarde / restauration / NAKIVO`
- **Tags** : `nakivo`, `director`, `transporter`, `windows-server`, `installation`

---

## Problème précis à résoudre

Installer NAKIVO Backup & Replication (Director et Transporter) sur Windows Server 2022 et ouvrir l'interface web.

## 1. Hors-Production (Lab / Test / POC)

1. Télécharger le programme d'installation Windows depuis le site officiel NAKIVO et vérifier son empreinte : 
```powershell
Get-FileHash -Algorithm SHA256 -Path CHEMIN_INSTALLEUR
```
   👉 Explication : CHEMIN_INSTALLEUR est à remplacer par le fichier téléchargé.

2. Lancer l'installeur en administrateur et choisir l'installation complète (Director et Transporter) ou le seul Transporter selon le rôle de la machine ; les écrans exacts dépendent de la version.
   👉 Explication : le Director gère les jobs ; le Transporter exécute les transferts de données.

3. Contrôler les services. PowerShell :
```powershell
Get-Service -DisplayName '*NAKIVO*' | Format-Table Name,DisplayName,Status
```
   👉 Explication : le nom exact des services est à confirmer sur votre version.

4. Ouvrir l'interface web au format `https://ADRESSE_DIRECTOR:PORT_WEB` (PORT_WEB à lire dans la documentation de la version) et créer le compte administrateur initial si l'assistant le demande.
   👉 Explication : ADRESSE_DIRECTOR et PORT_WEB sont à remplacer ; le certificat auto-signé initial est normal avant la sécurisation.

5. Ajouter le dépôt : **Settings > Repositories** (libellé à vérifier) et choisir le dossier local dédié.
   👉 Explication : c'est là que seront stockées les sauvegardes.

6. Si un Transporter distant est utilisé, l'enregistrer dans l'interface : **Settings > Transporters** (libellé à vérifier).
   👉 Explication : le Director pilote ainsi plusieurs Transporters.

## 2. Production — Contrôles

- Noter la version installée.
- Tester d'abord en lab.

## 3. Production — Sécurité

- Compte administrateur nominatif et mot de passe fort hors fiche.
- Interface web non exposée sur Internet.

## Validation et retour arrière

- **Validation** : Services actifs, interface web accessible, dépôt visible dans l'interface.
- **Retour arrière** : Désinstaller NAKIVO dans `appwiz.cpl`; conserver ou supprimer le dépôt selon la politique de rétention.

## Si le problème n'est pas résolu

- [NAKIVO — Help Center officiel](https://helpcenter.nakivo.com/)
- [NAKIVO — System Requirements](https://helpcenter.nakivo.com/display/NH/System+Requirements)
- [Fiche d'entrée du logiciel](../../../../Logiciels/07-Sauvegarde-restauration-et-PRA-PCA/Fiche_Logiciel_-_Nakivo-Altaro.md)
