# Fiche_Simple_-_VM_Windows_11_Visio_Installer

- **Environnement** : Poste Windows 11 x64 d'un utilisateur ou administrateur (VM de test puis poste pilote)
- **OS / Version** : Windows 11 x64; version Visio à vérifier auprès de l'éditeur
- **Catégorie** : outil de diagrammes / poste de travail
- **Tags** : `visio`, `windows11`, `microsoft-365`, `installation`

---

## Problème précis à résoudre

Installer Visio sur Windows 11 avec l'ODT ou Intune.

## 1. Hors-Production (Lab / Test / POC)

1. Télécharger l'Office Deployment Tool depuis le Centre de téléchargement Microsoft et extraire setup.exe dans C:\ODT.
   👉 Explication : l'outil est officiel et gratuit.

2. Créer C:\ODT\configuration.xml (Visio seul, abonnement) :
```xml
<Configuration>
  <Add OfficeClientEdition="64" Channel="CANAL">
    <Product ID="VisioProRetail">
      <Language ID="fr-fr" />
    </Product>
  </Add>
  <Display Level="Full" AcceptEULA="TRUE" />
</Configuration>
```
   👉 Explication : CANAL est à remplacer (par ex. Current ou MonthlyEnterprise, à vérifier) ; pour un perpétuel en volume, l'identifiant de produit diffère (vérifier la liste officielle des Product ID).

3. Installer. PowerShell administrateur :
```powershell
cd C:\ODT
.\setup.exe /configure .\configuration.xml
```
   👉 Explication : l'installation télécharge depuis le CDN ou depuis SOURCE_ODT si SourcePath est ajouté.

4. Variante Intune : GUI **Centre d'administration Intune > Applications > Windows > Ajouter > Microsoft 365 Apps** ; dans les paramètres, activer l'application Visio (libellé à vérifier), assigner le groupe GROUPE_VISIO.
   👉 Explication : GROUPE_VISIO est un groupe Entra ID à remplacer.

5. Contrôler l'installation :
```powershell
Test-Path 'C:\Program Files\Microsoft Office\root\Office16\VISIO.EXE'
```
   👉 Explication : True indique que Visio est présent.

## 2. Production — Contrôles

- Noter la version installée.
- Poste pilote d'abord.

## 3. Production — Sécurité

- Installer depuis les sources Microsoft uniquement.

## Validation et retour arrière

- **Validation** : VISIO.EXE présent, démarrage OK.
- **Retour arrière** : Désinstaller via **Paramètres > Applications > Visio** ou avec ODT et RemoveProduct si nécessaire.

## Si le problème n'est pas résolu

- [Microsoft — Office Deployment Tool](https://learn.microsoft.com/fr-fr/deployoffice/overview-office-deployment-tool)
- [Microsoft — Visio, plans et tarifs](https://www.microsoft.com/fr-fr/microsoft-365/visio/compare-visio-options)
- [Fiche d'entrée du logiciel](../../../../Logiciels/15-Topologie-IPAM-et-outils-metiers/Fiche_Logiciel_-_Microsoft-Visio.md)
- [Alternative draw.io : fiche d'entrée](../../../../Logiciels/15-Topologie-IPAM-et-outils-metiers/Fiche_Logiciel_-_draw-io-Desktop.md)
- [Alternative draw.io : installation (Debian 13)](../../../../Debian/13/Vie-du-logiciel/draw.io/Fiche_Simple_-_VM_Debian_13_draw_io_Installer.md)
