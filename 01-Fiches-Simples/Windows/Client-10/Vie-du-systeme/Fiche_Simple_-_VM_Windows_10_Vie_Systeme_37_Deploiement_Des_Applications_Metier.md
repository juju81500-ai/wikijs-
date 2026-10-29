# Fiche_Simple_-_VM_Windows_10_Vie_Systeme_37_Deploiement_Des_Applications_Metier

- **Environnement** : PC Windows 10 (poste de travail)
- **OS / Version** : Windows 10; étape 37 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windows10`, `vie-du-systeme`, `cycle-de-vie`, `etape-37`

---

## Problème précis à résoudre

Installer les logiciels métier de manière standardisée.

## 1. Hors-Production (Lab / Test / POC)

1. Installer avec WinGet ou Intune (**Applications > Windows > Ajouter**) plutôt que manuellement.
   ```powershell
   winget install --id ID_APPLICATION -e --silent --accept-package-agreements
   ```
   👉 Explication : installe l'application identifiée par `ID_APPLICATION` (obtenu avec `winget search`) sans interaction.

2. Installer un paquet MSI interne en mode silencieux.
   ```powershell
   Start-Process msiexec.exe -ArgumentList '/i "\\SERVEUR\Logiciels\APPLICATION.msi" /qn /norestart /l*v C:\Windows\Temp\APPLICATION.log' -Wait -NoNewWindow
   ```
   👉 Explication : déploie en silence avec un journal d'installation.

3. Contrôler les applications installées : **Paramètres > Applications > Applications installées**.
   ```powershell
   Get-Package | Select-Object Name,Version,ProviderName | Sort-Object Name
   ```
   👉 Explication : liste les logiciels et leurs versions pour l'inventaire.

4. Appliquer les profils de l'utilisateur (imprimantes, lecteurs réseau) par GPO ou Intune.
   ```powershell
   Get-PrinterPort | Select-Object -First 5
   Get-SmbMapping
   ```
   👉 Explication : montre les imprimantes et partages mappés.

## 2. Production — Contrôles

Applications packagées, versionnées, installées depuis le catalogue de l'entreprise.

## 3. Production — Sécurité

Vérifier la signature numérique et l'empreinte du paquet avant diffusion.

## Validation et retour arrière

- **Validation** : L'application se lance et sa version est conforme au catalogue.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Windows 10](./Sommaire_-_Vie_du_systeme_Windows_10.md)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows/)
