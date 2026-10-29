# Déployer Windows Server 2025 en production

- **Type de fiche** : Installation / Déploiement
- **Environnement** : Serveur physique ou VM administré par l'organisation
- **OS / Version** : Windows Server 2025 Standard ou Datacenter
- **Rôle** : Installer, préparer, mettre à jour et réceptionner un serveur avant configuration de rôle

## 1. Préparer l'installation

Fiche simple : [préparer l'installation](/01-fiches-simples/windows/server-2025/vie-du-systeme/fiches-par-theme/installation-systeme/fiche-simple-vm-windows-server-2025-production-preparer-installation).

Définir le rôle, l'édition/licence, le modèle de support, le réseau d'administration, les sauvegardes et le propriétaire du service. Vérifier la compatibilité des applications et pilotes avec Server 2025 avant migration ou installation d'un rôle.

Pour une VM, valider le modèle CPU exposé : Server 2025 requiert notamment SSE4.2 et POPCNT. Utiliser une VM génération 2/UEFI lorsque la plateforme le permet, et prévoir les ressources selon la charge plutôt que le minimum d'installation.

## 2. Installer le système

Fiche simple : [installer le système](/01-fiches-simples/windows/server-2025/vie-du-systeme/fiches-par-theme/installation-systeme/fiche-simple-vm-windows-server-2025-production-installer-systeme).

1. Utiliser un média Microsoft ou un média d'entreprise dont l'origine et l'intégrité sont vérifiées.
2. Démarrer en UEFI, sélectionner Standard/Datacenter et Server Core/Desktop Experience selon le rôle et la politique d'exploitation.
3. Vérifier le disque cible avant partitionnement, définir le mot de passe administrateur de secours selon le coffre prévu et retirer les médias d'installation.
4. Installer les pilotes approuvés et les mises à jour cumulatives, puis redémarrer si requis.

## 3. Configurer l'identité et le réseau

Fiche simple : [configurer identité et réseau](/01-fiches-simples/windows/server-2025/vie-du-systeme/fiches-par-theme/installation-systeme/fiche-simple-vm-windows-server-2025-production-identite-reseau).

Attribuer un nom conforme à la convention, une adresse IP/DNS documentée, une source de temps et une zone horaire approuvées. Joindre le serveur au domaine uniquement lorsque le rôle et la stratégie l'exigent; éviter les comptes d'administration partagés.

Contrôles de base en PowerShell :

```powershell
Get-ComputerInfo | Select-Object WindowsProductName, WindowsVersion, OsBuildNumber
Get-NetIPConfiguration
Get-HotFix | Sort-Object InstalledOn -Descending | Select-Object -First 10
Get-Service sshd -ErrorAction SilentlyContinue
```

OpenSSH Server est présent par défaut sur Server 2025; vérifier son état et ses règles de pare-feu. Ne pas l'exposer ni l'activer par défaut si le mode d'administration retenu ne l'utilise pas.

## 4. Appliquer la gestion et le socle de sécurité

Fiche simple : [appliquer gestion et socle de sécurité](/01-fiches-simples/windows/server-2025/vie-du-systeme/fiches-par-theme/installation-systeme/fiche-simple-vm-windows-server-2025-production-gestion-socle-securite).

- Inscrire le serveur dans l'outil de gestion prévu (GPO, Windows Admin Center, MECM, Azure Arc ou autre).
- Appliquer la baseline et les stratégies approuvées pour le rôle.
- Vérifier Microsoft Defender, pare-feu, journalisation, sauvegarde et comptes privilégiés.
- Examiner Credential Guard, Secure Boot et VBS selon la compatibilité matérielle et applicative.
- Installer uniquement les rôles/features nécessaires après vérification des prérequis officiels.

## 5. Recette avant mise en production

Fiche simple : [réaliser la recette avant production](/01-fiches-simples/windows/server-2025/vie-du-systeme/fiches-par-theme/installation-systeme/fiche-simple-vm-windows-server-2025-production-recette-avant-production).

Vérifier DNS, heure, connectivité depuis les réseaux autorisés, mises à jour, accès d'administration, supervision, sauvegarde/restauration et journaux. Tester le redémarrage planifié et documenter version, édition, build, adresse, rôles, exceptions et propriétaire.

## 6. Retour arrière

Fiche simple : [préparer le retour arrière](/01-fiches-simples/windows/server-2025/vie-du-systeme/fiches-par-theme/installation-systeme/fiche-simple-vm-windows-server-2025-production-retour-arriere).

Avant toute migration ou ajout de rôle, confirmer une sauvegarde restaurable et un accès console. En cas d'échec, isoler le serveur, préserver journaux et état, puis appliquer le plan de restauration ou de réinstallation; ne pas désinstaller un rôle de production sans évaluer ses dépendances.

## Sources

- [Microsoft Learn — Nouveautés de Windows Server 2025](https://learn.microsoft.com/en-us/windows-server/get-started/whats-new-windows-server-2025)
- [Microsoft Learn — Installation de Windows Server](https://learn.microsoft.com/en-us/windows-server/get-started/install-options-server)
- [Microsoft Learn — Planifier et déployer Windows Server](https://learn.microsoft.com/en-us/windows-server/get-started/)