# Fiche_Simple_-_VM_Windows_Server_2022_Veeam_Installer_Serveur_Sauvegarde.md

- **Environnement** : Serveur Windows Server 2022 dédié au serveur de sauvegarde Veeam (pilote autonome) et hôte Hyper-V autorisé
- **OS / Version** : Windows Server 2022; Veeam Backup & Replication 13.1.2.57
- **Catégorie** : sauvegarde VM / installation
- **Tags** : `windows-server-2022`, `veeam`, `backup-replication`, `hyper-v`, `iso`, `backup-server`

---

## Problème précis à résoudre

Installer le Backup Server à partir du média officiel vérifié.

## 1. Hors-Production (Lab / Test / POC)

1. Télécharger le média Veeam 13 depuis le portail officiel et vérifier la signature ou le checksum publié :
   ```powershell
   Get-FileHash -Algorithm SHA256 C:\Installateurs\VeeamBackup.iso
   ```
   👉 Explication : un média altéré ne doit pas être installé.

2. Monter l'ISO : **Explorateur de fichiers > clic droit sur l'ISO > Monter**
   👉 Explication : donne accès à l'installateur.

3. GUI équivalent en commande :
   ```powershell
   Mount-DiskImage -ImagePath C:\Installateurs\VeeamBackup.iso | Get-Volume
   ```
   👉 Explication : monte l'ISO et affiche la lettre de lecteur.

4. Lancer l'installateur : **Setup > Veeam Backup & Replication > Install**, appliquer la licence autorisée et choisir le Backup Server.
   👉 Explication : vérifier prérequis, compte de service, moteur de base, dossier de configuration et ports.

## 2. Production — Contrôles

Valider comptes et ports avec les équipes systèmes et réseau.

## 3. Production — Sécurité

- Ne pas exposer l'interface d'administration sur Internet.
- Limiter les comptes Administrateurs Veeam et les flux aux hôtes, proxies et dépôts requis.

## Validation et retour arrière

- **Validation** : console Veeam accessible en local.
- **Retour arrière** : **Paramètres > Applications > Veeam Backup & Replication > Désinstaller** (la configuration doit avoir été sauvegardée).

## Si le problème n'est pas résolu

- [Veeam 13 — guide utilisateur](https://helpcenter.veeam.com/docs/vbr/userguide/)
- [Veeam 13 — installer Backup & Replication](https://helpcenter.veeam.com/docs/vbr/userguide/install_vbr.html)
- [Guide complet Veeam Windows Server 2022](../../../../../02-Fiches-Completes/Windows/Server-2022/Installation-Deploiement/58_Deploiement_Veeam_Backup_Replication_13_Windows_Server_2022.md#2-installer-le-serveur-de-sauvegarde)
