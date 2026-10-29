# Fiche_Simple_-_Windows_Server_2022_WDS_MDT_Maintenance_Retour_arriere

- **Environnement** : Windows Server 2022, WDS + MDT en service
- **OS / Version** : Windows Server 2022; WDS, MDT, ADK : vérifier la version publiée
- **Catégorie** : Automatisation, déploiement et IaC

---

## Problème précis à résoudre

Maintenir le service (images de démarrage, ADK, partage) et revenir en arrière si une modification échoue. L'installation initiale est dans la [procédure historique WDS + MDT](/01-fiches-simples/logiciels/09-automatisation-deploiement-et-iac/fiche-simple-wds-mdt).

## 1. Hors-Production (Lab / Test / POC)

1. Avant toute modification, sauvegarder (fiche Sauvegarde/Restauration) et conserver l'image de démarrage actuelle :
   ```powershell
   $Share = "D:\DeploymentShare$"
   Copy-Item "$Share\Boot\LiteTouchPE_x64.wim" "$Share\Boot\LiteTouchPE_x64.wim.AVANT" -Force
   ```
   👉 Explication : `$Share` est à remplacer. La copie `.AVANT` permet le retour arrière rapide.

2. Régénérer l'image de démarrage (après mise à jour de l'ADK ou de MDT) :
   ```powershell
   Import-Module "C:\Program Files\Microsoft Deployment Toolkit\bin\MicrosoftDeploymentToolkit.psd1"
   New-PSDrive -Name DS001 -PSProvider MDTProvider -Root $Share
   Update-MDTDeploymentShare -Path "DS001:" -Force
   ```
   👉 Explication : `-Force` régénère les images complètement. Les versions ADK/WinPE compatibles avec MDT sont à vérifier.

3. Remplacer l'image publiée dans WDS. GUI : `Services de déploiement Windows > Images de démarrage > clic droit > Remplacer l'image`.
   ```powershell
   wdsutil /Replace-Image /Image:"NOM-IMAGE-DEMARRAGE" /ImageType:Boot /Architecture:x64 /ReplacementImage /ImageFile:"$Share\Boot\LiteTouchPE_x64.wim"
   ```
   👉 Explication : `NOM-IMAGE-DEMARRAGE` à remplacer (visible avec `wdsutil /Get-AllImages /Show:Boot`). Syntaxe à vérifier avec `wdsutil /?`.

4. Tester avec une VM en PXE (fiche Recette).
   👉 Explication : ne généraliser qu'après un test réussi.

5. Retour arrière si l'image échoue :
   ```powershell
   Copy-Item "$Share\Boot\LiteTouchPE_x64.wim.AVANT" "$Share\Boot\LiteTouchPE_x64.wim" -Force
   wdsutil /Replace-Image /Image:"NOM-IMAGE-DEMARRAGE" /ImageType:Boot /Architecture:x64 /ReplacementImage /ImageFile:"$Share\Boot\LiteTouchPE_x64.wim"
   ```
   👉 Explication : on remet l'ancienne image dans le partage puis dans WDS. Si l'ADK a aussi été mis à jour et pose problème, le désinstaller via `Paramètres > Applications` et réinstaller la version précédente.

## 2. Production — Contrôles

Fenêtre de maintenance; poste pilote; surveiller les échecs PXE. Appliquer les mises à jour Windows Server (fiche Vie du système) hors période de déploiement.

## 3. Production — Sécurité

- Binaires ADK/MDT uniquement depuis les sites Microsoft officiels; contrôler la signature.
- Supprimer les images obsolètes et les copies `.AVANT` après la période de rétention.

## Validation et retour arrière

- **Validation** : image régénérée publiée, VM de test déployée avec succès.
- **Retour arrière** : étape 5 ci-dessus; en dernier recours, restauration complète depuis la fiche Sauvegarde/Restauration.

## Si le problème n'est pas résolu

- [Procédure historique WDS + MDT](/01-fiches-simples/logiciels/09-automatisation-deploiement-et-iac/fiche-simple-wds-mdt)
- [Fiche d'entrée WDS/MDT](/01-fiches-simples/logiciels/09-automatisation-deploiement-et-iac/fiche-logiciel-wds-mdt)
- [Microsoft Learn — wdsutil](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/wdsutil)
- [Microsoft Learn — Démarrer avec MDT](https://learn.microsoft.com/en-us/windows/deployment/deploy-windows-mdt/get-started-with-the-microsoft-deployment-toolkit)