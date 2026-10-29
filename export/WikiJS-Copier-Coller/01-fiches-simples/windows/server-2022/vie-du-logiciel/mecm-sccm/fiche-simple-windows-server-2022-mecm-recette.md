# Fiche_Simple_-_Windows_Server_2022_MECM_Recette

- **Environnement** : Windows Server 2022, site MECM/SCCM configuré, un poste de test dans `COLLECTION-TEST`
- **OS / Version** : Windows Server 2022; Configuration Manager : vérifier la version publiée
- **Catégorie** : Automatisation, déploiement et IaC

---

## Problème précis à résoudre

Recetter un site MECM/SCCM : santé des composants, client fonctionnel, contenu distribué, déploiement de test réussi.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler l'état du site. GUI : `Surveillance > État du site` et `État des composants`.
   ```powershell
   Get-Service SMS_EXECUTIVE, SMS_SITE_COMPONENT_MANAGER, SMS_SITE_VSS_WRITER | Select-Object Name, Status
   ```
   👉 Explication : les services doivent être `Running`; aucun composant en état « Critique » dans la console.

2. Contrôler les appareils découverts et le client. GUI : `Biens et conformité > Appareils`.
   ```powershell
   Get-CMDevice -Name "POSTE-TEST" | Select-Object Name, ClientVersion, IsActive
   ```
   👉 Explication : remplacer `POSTE-TEST`; le client doit être installé et actif.

3. Sur le poste de test, contrôler le client :
   ```powershell
   Get-Service CcmExec
   Get-Content C:\Windows\CCM\Logs\ClientIDManagerStartup.log -Tail 20
   ```
   👉 Explication : `CcmExec` doit être `Running`; le journal montre l'enregistrement auprès du site.

4. Distribuer et déployer une application de test. GUI : `Biens et conformité > Collections d'appareils`, clic droit sur la collection, `Déployer`.
   👉 Explication : utiliser un paquet inoffensif; vérifier la distribution (`Surveillance > État de distribution du contenu`) puis l'état du déploiement.

5. Vérifier le résultat côté client :
   ```powershell
   Get-Content C:\Windows\CCM\Logs\AppEnforce.log -Tail 30
   ```
   👉 Explication : doit indiquer une installation réussie (code de sortie attendu).

## 2. Production — Contrôles

Rejouer le test sur une collection pilote réelle; enregistrer date, version du site et résultat.

## 3. Production — Sécurité

- Ne déployer en test que du contenu validé; pas d'exécution avec compte privilégié non nécessaire.
- Supprimer les déploiements de test à la fin de la recette.

## Validation et retour arrière

- **Validation** : état du site sain, client actif, contenu distribué, déploiement en « Réussi ».
- **Retour arrière** : supprimer le déploiement de test (console : clic droit > `Supprimer`) et désinstaller l'application de test du poste.

## Si le problème n'est pas résolu

- [Fiche d'entrée MECM/SCCM](/01-fiches-simples/logiciels/09-automatisation-deploiement-et-iac/fiche-logiciel-microsoft-mecm-sccm)
- [Microsoft Learn — Fichiers journaux](https://learn.microsoft.com/en-us/intune/configmgr/core/plan-design/hierarchy/log-files)