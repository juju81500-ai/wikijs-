# 📄 Fiche_Simple_-_VM_Windows_Server_2022_Installation_OS_Premier_Demarrage.md

- **Environnement** : VM sur Proxmox VE, Hyper-V, KVM ou VMware
- **OS / Version** : Windows Server 2022 Standard ou Datacenter
- **Catégorie** : Installation / Système
- **Tags** : `[windows-server-2022]`, `[installation]`, `[vm]`, `[uefi]`, `[premier-demarrage]`, `[powershell]`

## 🎯 Problème précis à résoudre
Installer Windows Server 2022 sur une nouvelle VM, sélectionner Server Core ou Desktop Experience selon le rôle et préparer l'administration avant l'installation des rôles.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Obtenir l'ISO depuis une source autorisée et vérifier son édition et son intégrité selon la procédure de l'organisation.
2. Créer une VM avec firmware UEFI, disque, CPU, mémoire et carte réseau adaptés au lab; monter l'ISO.
3. Dans l'installateur, sélectionner l'édition et l'expérience (Server Core ou Desktop Experience), puis installer sur le disque validé.
4. Définir un mot de passe Administrateur local unique via l'installation; se connecter par console et vérifier :
   ```powershell
   Get-ComputerInfo | Select-Object WindowsProductName, WindowsVersion, OsBuildNumber
   Get-Disk | Select-Object Number, FriendlyName, OperationalStatus, Size
   Get-NetIPConfiguration
   ```
   👉 *Explication : Server Core n'a pas d'interface graphique complète; choisir selon les compétences d'exploitation et les exigences du rôle.*

**Équivalent interface graphique :**

- **Gestionnaire de serveur > Serveur local** (nom, build, réseau), **Gestion des disques** (`diskmgmt.msc`) pour les disques.
  👉 Explication : équivalent graphique des commandes de contrôle après installation.

## ⚡ 2. Production — Façon Simplifiée
1. Confirmer l'édition/licence, le rôle prévu, le nom de serveur, le plan IP/DNS, les disques et le support de sauvegarde.
2. Appliquer les mises à jour et les outils invités; configurer hostname, IP, DNS, heure et accès d'administration via les fiches dédiées.
3. Ne promouvoir le serveur en contrôleur de domaine et n'installer les rôles qu'après validation du premier démarrage et de la sauvegarde initiale.
4. Garder la console hyperviseur et un compte d'administration de secours documenté.

## 🔒 3. Production — Façon Sécurisée
1. Utiliser une image vérifiée et une licence conforme; ne pas réutiliser un mot de passe d'installation.
2. Installer uniquement l'expérience et les composants nécessaires; appliquer la baseline de sécurité de l'organisation.
3. Ne pas exposer RDP à Internet; restreindre le pare-feu et l'administration aux réseaux approuvés.

## ✅ Validation et retour arrière
- Confirmer édition, build, nom, stockage, adresse, DNS, heure, correctifs et état des services système.
- Prendre une sauvegarde initiale et vérifier sa présence avant l'installation des rôles critiques.
- En cas d'installation incorrecte, conserver les journaux puis reconstruire la VM depuis le média validé.