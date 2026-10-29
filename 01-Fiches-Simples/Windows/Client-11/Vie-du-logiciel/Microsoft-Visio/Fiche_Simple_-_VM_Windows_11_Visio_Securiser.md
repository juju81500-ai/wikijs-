# Fiche_Simple_-_VM_Windows_11_Visio_Securiser

- **Environnement** : Poste Windows 11 x64 d'un utilisateur ou administrateur (VM de test puis poste pilote)
- **OS / Version** : Windows 11 x64; version Visio à vérifier auprès de l'éditeur
- **Catégorie** : outil de diagrammes / poste de travail
- **Tags** : `visio`, `windows11`, `microsoft-365`, `securite`

---

## Problème précis à résoudre

Sécuriser Visio : macros, sources de données, compte et mises à jour.

## 1. Hors-Production (Lab / Test / POC)

1. GUI **Fichier > Options > Centre de gestion de la confidentialité > Paramètres du Centre > Paramètres des macros** : désactiver toutes les macros avec notification.
   👉 Explication : limite l'exécution de code.

2. GUI **Paramètres de l'affichage protégé** : activer pour les fichiers de provenance Internet.
   👉 Explication : évite l'ouverture active de fichiers douteux.

3. Restreindre les connexions de données externes : GUI **Centre de gestion > Contenu externe**.
   👉 Explication : évite les fuites vers des sources non voulues.

4. Contrôler le canal de mise à jour. PowerShell :
```powershell
Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Office\ClickToRun\Configuration' | Select-Object CDNBaseUrl,UpdateChannel,VersionToReport
```
   👉 Explication : permet de confirmer que le poste reçoit bien les correctifs.

## 2. Production — Contrôles

- Appliquer ces options par GPO ou Intune.
- Revue des licences trimestrielle.

## 3. Production — Sécurité

- Compte avec MFA.
- Pas de partage de licence.

## Validation et retour arrière

- **Validation** : Macros bloquées, affichage protégé actif.
- **Retour arrière** : Rétablir les options précédentes via la stratégie.

## Si le problème n'est pas résolu

- [Microsoft — Office Deployment Tool](https://learn.microsoft.com/fr-fr/deployoffice/overview-office-deployment-tool)
- [Microsoft — Visio, plans et tarifs](https://www.microsoft.com/fr-fr/microsoft-365/visio/compare-visio-options)
- [Fiche d'entrée du logiciel](../../../../Logiciels/15-Topologie-IPAM-et-outils-metiers/Fiche_Logiciel_-_Microsoft-Visio.md)
- [Alternative draw.io : fiche d'entrée](../../../../Logiciels/15-Topologie-IPAM-et-outils-metiers/Fiche_Logiciel_-_draw-io-Desktop.md)
- [Alternative draw.io : installation (Debian 13)](../../../../Debian/13/Vie-du-logiciel/draw.io/Fiche_Simple_-_VM_Debian_13_draw_io_Installer.md)
