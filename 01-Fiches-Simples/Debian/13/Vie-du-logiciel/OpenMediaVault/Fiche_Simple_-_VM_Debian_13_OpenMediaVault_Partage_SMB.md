# Fiche_Simple_-_VM_Debian_13_OpenMediaVault_Partage_SMB.md

- **Environnement** : OpenMediaVault 8 sur Debian 13 minimal
- **OS / Version** : Debian 13; OpenMediaVault 8.0 Synchrony
- **Catégorie** : stockage / SMB
- **Tags** : `debian13`, `openmediavault`, `smb`, `samba`, `permissions`

---

## Problème précis à résoudre

Publier un dossier SMB réservé à un groupe, sans accès invité.

## 1. Hors-Production (Lab / Test / POC)

1. Créer le dossier partagé (exemple `Equipe`) : **Storage > Shared Folders > Add**, permissions initiales restrictives.
   👉 Explication : Dossier sur le système de fichiers de données monté.

2. Créer comptes nominatifs et groupe dédié : **Users > Users** et **Users > Groups**.
   👉 Explication : Ne pas partager le compte root.

3. Donner l'accès au seul groupe prévu dans les permissions du dossier partagé.
   👉 Explication : Permissions OMV et POSIX/ACL sont deux couches; les deux doivent autoriser.

4. Activer SMB : **Services > SMB/CIFS > Settings**, puis créer le partage dans **Services > SMB/CIFS > Shares** sans accès public ni invité; appliquer dans la bannière de configuration.
   👉 Explication : Lecture/écriture pour les comptes nécessaires uniquement.

5. Tester depuis un client autorisé (remplacer `192.0.2.10`, `Equipe` et `alice` par vos valeurs; le mot de passe est demandé interactivement) :
   ```bash
   smbclient -L //192.0.2.10 -U alice
   smbclient //192.0.2.10/Equipe -U alice -c 'ls'
   ```
   👉 Explication : Liste les partages puis le contenu; vérifier aussi qu'un compte non autorisé est refusé.

## 2. Production — Contrôles

Autoriser TCP 445 uniquement depuis les clients prévus; désactiver anciens protocoles et invité.

## 3. Production — Sécurité

- Ne jamais utiliser guest ni permissions 777 pour résoudre un problème d'accès.
- N'exposer aucun service NAS sur Internet; VPN approuvé pour l'accès distant.

## Validation et retour arrière

- **Validation** : un compte autorisé lit/écrit/supprime un fichier test, un compte non autorisé est refusé.
- **Retour arrière** : supprimer le partage dans **Services > SMB/CIFS > Shares** puis appliquer; les données restent sur le dossier.

## Si le problème n'est pas résolu

- [OpenMediaVault — installation sur Debian](https://docs.openmediavault.org/en/latest/installation/on_debian.html)
- [OpenMediaVault — prérequis](https://docs.openmediavault.org/en/latest/prerequisites.html)
- [Guide complet OpenMediaVault Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/66_Deploiement_OpenMediaVault_8_Debian_13.md#6-creer-un-partage-smb-prive)
