# Fiche_Simple_-_VM_Ubuntu_24.04_PowerShell_Prerequis_Limites

- **Environnement** : VM Ubuntu 24.04 LTS de laboratoire, accès sudo, dépôt Microsoft officiel
- **OS / Version** : Ubuntu 24.04 LTS
- **Catégorie** : shell / scripting

---

## Problème précis à résoudre

Cadrer le périmètre PowerShell 7 sur Ubuntu 24.04 LTS avant installation : support, différences avec Windows PowerShell 5.1 et limites.

## 1. Hors-Production (Lab / Test / POC)

1. Relever l'OS et l'architecture :
   ```bash
   cat /etc/os-release
   uname -m
   ```
   👉 Explication : PowerShell 7 est publié par Microsoft pour des architectures précises (x64, Arm64) ; comparer avec la page officielle d'installation.

2. Consulter la matrice de support de la version visée.
   👉 Explication : Microsoft documente les distributions supportées par version de PowerShell ; Ubuntu 24.04 LTS figure dans la documentation d'installation (vérifier la version publiée).

3. Noter les différences PowerShell 7 / Windows PowerShell 5.1 :
   👉 Explication : PowerShell 7 (`pwsh`, édition Core) est multiplateforme et s'installe côte à côte ; Windows PowerShell 5.1 (`powershell.exe`, édition Desktop) n'existe que sous Windows. Ici seul PowerShell 7 est disponible : pas de modules dépendant de .NET Framework, WMI/CIM Windows, ni de remoting WinRM natif.

4. Décider du mode de remoting visé :
   👉 Explication : sous Linux, le remoting PowerShell passe par SSH (sous-système `powershell` de sshd) ; WinRM/WSMan n'est pas utilisé pour s'y connecter.

5. Noter que la stratégie d'exécution et les signatures Authenticode ne s'appliquent pas :
   👉 Explication : `Set-ExecutionPolicy` n'a pas d'effet sous Linux ; l'intégrité des scripts se contrôle autrement (empreinte, signature GPG/Git) — voir la fiche Securiser.

## 2. Production — Contrôles

Valider avec l'équipe sécurité l'usage d'un dépôt tiers (Microsoft) et la version cible. Prévoir un miroir interne si l'accès Internet est filtré. Commandes établies d'après la documentation officielle et non testées dans ce pack : à valider en lab avant toute production.

## 3. Production — Sécurité

- Ne pas exécuter pwsh en root par défaut.
- Ne pas stocker d'identifiants dans l'historique ou le profil.

## Validation et retour arrière

- **Validation** : OS, architecture et support documentés par écrit.
- **Retour arrière** : aucune modification n'est faite par cette fiche.

## Si le problème n'est pas résolu

- [Microsoft Learn — installer PowerShell sur Linux](https://learn.microsoft.com/powershell/scripting/install/installing-powershell-on-linux)
- [Microsoft Learn — remoting PowerShell via SSH](https://learn.microsoft.com/powershell/scripting/security/remoting/ssh-remoting-in-powershell)
- [Guide complet Windows 11 (référence PowerShell 7)](/02-fiches-completes/windows/client-11/installation-deploiement/85-administration-powershell-7-6-9-windows-11)