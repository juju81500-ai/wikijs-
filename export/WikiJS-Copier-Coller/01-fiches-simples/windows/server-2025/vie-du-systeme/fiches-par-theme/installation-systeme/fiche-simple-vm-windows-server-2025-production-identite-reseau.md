# Fiche_Simple_-_VM_Windows_Server_2025_Production_Identite_Reseau.md

- **Environnement** : Serveur physique ou VM Windows Server 2025 administré par l'organisation
- **OS / Version** : Windows Server 2025 Standard ou Datacenter
- **Catégorie** : installation / déploiement

---

## Problème précis à résoudre

Nommer le serveur, fixer réseau, heure et contrôler l'état de base.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : **Gestionnaire de serveur > Serveur local** pour le nom, l'adresse IP, le DNS, le fuseau horaire; jonction au domaine uniquement si le rôle et la stratégie l'exigent.
   👉 Explication : on respecte la convention de nommage.

2. Contrôles de base en PowerShell :
   ```powershell
   Get-ComputerInfo | Select-Object WindowsProductName, WindowsVersion, OsBuildNumber
   Get-NetIPConfiguration
   Get-HotFix | Sort-Object InstalledOn -Descending | Select-Object -First 10
   Get-Service sshd -ErrorAction SilentlyContinue
   ```
   👉 Explication : version, adresse, correctifs récents et état d'OpenSSH Server.

3. Vérifier l'état et les règles de pare-feu d'OpenSSH Server, présent par défaut sur Server 2025.
   👉 Explication : ne pas l'exposer ni l'activer si le mode d'administration retenu ne l'utilise pas.

## 2. Production — Contrôles

Documenter nom, adresse IP/DNS, source de temps et zone horaire approuvées.

## 3. Production — Sécurité

- Éviter les comptes d'administration partagés.
- Ne pas exposer OpenSSH inutilement.

## Validation et retour arrière

- **Validation** : Identité, réseau, heure et correctifs conformes.
- **Retour arrière** : Revenir aux paramètres réseau précédents via la console de la VM.

## Si le problème n'est pas résolu

- [Microsoft Learn — Nouveautés de Windows Server 2025](https://learn.microsoft.com/en-us/windows-server/get-started/whats-new-windows-server-2025)
- [Microsoft Learn — Installation de Windows Server](https://learn.microsoft.com/en-us/windows-server/get-started/install-options-server)
- [Guide complet déploiement Windows Server 2025](/02-fiches-completes/windows/server-2025/installation-deploiement/30-deploiement-windows-server-2025-production#3-configurer-lidentite-et-le-reseau)