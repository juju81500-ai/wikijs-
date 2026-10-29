# Fiche_Simple_-_Windows_Server_2022_PowerShell_Installer

- **Environnement** : Windows Server 2022 de laboratoire (Desktop Experience ou Core), session administrateur
- **OS / Version** : Windows Server 2022
- **Catégorie** : shell / scripting
- **Tags** : `windows-server-2022`, `powershell`, `pwsh`, `scripting`, `remoting`

---

## Problème précis à résoudre

Installer PowerShell 7 sur Windows Server 2022 avec le paquet MSI officiel, sans toucher à Windows PowerShell 5.1.

## 1. Hors-Production (Lab / Test / POC)

1. Télécharger le MSI x64 depuis la page de versions officielle (https://github.com/PowerShell/PowerShell/releases ou lien de Microsoft Learn), puis le fichier d'empreintes publié avec la version. GUI : navigateur, page de la version stable approuvée, section Assets.
   👉 Explication : choisir explicitement la version approuvée (VERSION dans la suite, à remplacer) ; ne pas utiliser de miroir non autorisé. Le client `winget` n'est pas à supposer présent sur Windows Server 2022 : vérifier avant de s'en servir.

2. Contrôler l'empreinte et la signature du MSI (CHEMIN_MSI et EMPREINTE_PUBLIEE sont à remplacer) :
   ```powershell
   $msi = 'CHEMIN_MSI'
   (Get-FileHash -Algorithm SHA256 -Path $msi).Hash
   Get-AuthenticodeSignature -FilePath $msi | Select-Object Status,SignerCertificate
   ```
   👉 Explication : comparer le hash à `EMPREINTE_PUBLIEE` (valeur de la page officielle) ; la signature doit être valide et émise par Microsoft.

3. Installer. GUI : double-clic sur le MSI et assistant (cocher l'ajout au PATH et l'enregistrement du manifeste d'événements si souhaité). Ligne de commande silencieuse :
   ```powershell
   msiexec.exe /package "$msi" /quiet ADD_PATH=1 REGISTER_MANIFEST=1
   ```
   👉 Explication : les propriétés MSI (`ADD_PATH`, `REGISTER_MANIFEST`, `ENABLE_PSREMOTING`, `USE_MU`, `ENABLE_MU`…) sont décrites par Microsoft Learn ; vérifier leurs effets avant de les activer en production.

4. Ouvrir un nouveau terminal et contrôler :
   ```powershell
   & 'C:\Program Files\PowerShell\7\pwsh.exe' -NoProfile -Command '$PSVersionTable.PSVersion.ToString()'
   ```
   👉 Explication : chemin d'installation par défaut documenté pour le MSI ; comparer la version à celle approuvée.

## 2. Production — Contrôles

Déployer par outil de distribution (GPO, MECM ou script) avec le même MSI validé, après test sur un pilote. Commandes établies d'après la documentation officielle et non testées dans ce pack : à valider en lab avant toute production.

## 3. Production — Sécurité

- Contrôler hash et signature avant chaque installation.
- Ne pas activer `ENABLE_PSREMOTING` sans décision explicite : il ouvre un point d'accès distant.

## Validation et retour arrière

- **Validation** : `pwsh.exe` répond avec la version attendue et 5.1 reste disponible.
- **Retour arrière** : désinstaller le MSI (voir la fiche Mise_A_Jour_Retour_Arriere).

## Si le problème n'est pas résolu

- [Microsoft Learn — installer PowerShell sur Windows](https://learn.microsoft.com/powershell/scripting/install/installing-powershell-on-windows)
- [Microsoft Learn — différences 5.1 / 7](https://learn.microsoft.com/powershell/scripting/whats-new/differences-from-windows-powershell)
- [Fiche connexe — Prerequis Limites](Fiche_Simple_-_Windows_Server_2022_PowerShell_Prerequis_Limites.md)
