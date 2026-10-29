# Fiche_Simple_-_Windows_Server_2025_RDS_Prerequis_Licences_CAL

- **Environnement** : VM ou serveur Windows dédié aux services Bureau à distance
- **OS / Version** : Windows Server 2025 Desktop Experience
- **Catégorie** : Vie du logiciel / Prérequis et licences RDS

---

## Problème précis à résoudre

Définir périmètre, rôles RDS et licences (Windows Server + RDS CAL) avant d'installer un hôte de session sous Windows Server 2025, sans ouvrir l'accès distant.

## 1. Hors-Production (Lab / Test / POC)

1. Relever l'édition, la version et le nom du serveur cible :
   ```powershell
   Get-ComputerInfo | Select-Object WindowsProductName, WindowsVersion, OsBuildNumber
   hostname
   ```
   👉 Explication : Confirme l'identité de la machine; vérifier la version publiée de Windows Server 2025 et ses prérequis officiels avant production.
2. Inventorier les rôles RDS déjà présents :
   ```powershell
   Get-WindowsFeature RDS-*
   ```
   👉 Explication : Liste les rôles RDS (hôte de session RDS-RD-Server, licences RDS-Licensing, Broker RDS-Connection-Broker, passerelle RDS-Gateway, accès Web RDS-Web-Access) installés ou non.
3. Dans **Gestionnaire de serveur** > **Gérer** > **Ajouter des rôles et fonctionnalités**, parcourir **Services Bureau à distance** sans valider l'installation.
   👉 Explication : L'assistant montre les services de rôle disponibles; choisir uniquement ceux requis par le scénario documenté.
4. Lister les CAL RDS à acquérir : type **Par utilisateur** ou **Par appareil**, version CAL **2025** (une CAL RDS doit être de version égale ou supérieure à celle de l'hôte de session) et quantité NB_CAL.
   👉 Explication : NB_CAL est à remplacer par le nombre d'utilisateurs ou d'appareils réels; les CAL RDS s'ajoutent à la licence Windows Server et ne sont pas incluses dans celle-ci. Vérifier les conditions auprès de Microsoft ou du revendeur.

## 2. Production — Contrôles

- Documenter sessions simultanées, capacité, DNS, certificats, dépendance Active Directory et réseau d'administration.
- Prévoir le serveur de licences RDS (rôle RDS-Licensing) sur un serveur membre du domaine, jamais par défaut sur un contrôleur de domaine.
- Sans serveur de licences ni CAL, un hôte de session n'accepte les connexions que pendant la période de grâce; ne pas s'en servir en production.

## 3. Production — Sécurité

- Ne pas publier TCP/UDP 3389 sur Internet; privilégier VPN ou RD Gateway approuvée.
- Prévoir un accès console hors bande et un point de restauration avant tout changement de rôle.
- Limiter l'accès aux groupes ayant un besoin métier documenté.

## Validation et retour arrière

- **Validation** : édition, rôles envisagés, type et nombre de CAL et flux réseau sont documentés et approuvés.
- **Retour arrière** : aucune modification appliquée; suspendre le déploiement si un prérequis ou une licence manque.

## Si le problème n'est pas résolu

- [Microsoft Learn — Vue d'ensemble RDS](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/overview)
- [Microsoft Learn — Licences RDS (CAL)](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds-client-access-license)
- [Installer et configurer RDS 2025](/01-fiches-simples/windows/server-2025/vie-du-logiciel/remote-desktop-services/fiche-simple-windows-server-2025-rds-installer-configurer)
- [Équivalent Windows Server 2022](/01-fiches-simples/windows/server-2022/vie-du-logiciel/remote-desktop-services/fiche-simple-windows-server-2022-rds-prerequis-limites)