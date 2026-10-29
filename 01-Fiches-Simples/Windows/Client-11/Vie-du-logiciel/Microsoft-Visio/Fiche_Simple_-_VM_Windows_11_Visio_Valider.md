# Fiche_Simple_-_VM_Windows_11_Visio_Valider

- **Environnement** : Poste Windows 11 x64 d'un utilisateur ou administrateur (VM de test puis poste pilote)
- **OS / Version** : Windows 11 x64; version Visio à vérifier auprès de l'éditeur
- **Catégorie** : outil de diagrammes / poste de travail
- **Tags** : `visio`, `windows11`, `microsoft-365`, `validation`

---

## Problème précis à résoudre

Recetter Visio : démarrage, licence, création et enregistrement d'un diagramme.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler la version installée. PowerShell :
```powershell
(Get-Item 'C:\Program Files\Microsoft Office\root\Office16\VISIO.EXE').VersionInfo.ProductVersion
```
   👉 Explication : retourne la version de Visio.

2. Ouvrir Visio, créer un diagramme réseau, l'enregistrer en .vsdx dans DOSSIER_TEST (à remplacer).
   👉 Explication : valide la licence et l'écriture.

3. Réouvrir le fichier et l'exporter en PDF : GUI **Fichier > Exporter > Créer un document PDF/XPS**.
   👉 Explication : valide la lecture et l'export.

4. Vérifier **Fichier > Compte** : produit activé.
   👉 Explication : confirme l'activation.

## 2. Production — Contrôles

- Consigner le résultat.
- Tester sur un second poste.

## 3. Production — Sécurité

- Supprimer les fichiers de test.

## Validation et retour arrière

- **Validation** : Création, enregistrement, ouverture et export OK.
- **Retour arrière** : Réparer Office via **Paramètres > Applications > Microsoft 365 > Modifier > Réparation en ligne**.

## Si le problème n'est pas résolu

- [Microsoft — Office Deployment Tool](https://learn.microsoft.com/fr-fr/deployoffice/overview-office-deployment-tool)
- [Microsoft — Visio, plans et tarifs](https://www.microsoft.com/fr-fr/microsoft-365/visio/compare-visio-options)
- [Fiche d'entrée du logiciel](../../../../Logiciels/15-Topologie-IPAM-et-outils-metiers/Fiche_Logiciel_-_Microsoft-Visio.md)
- [Alternative draw.io : fiche d'entrée](../../../../Logiciels/15-Topologie-IPAM-et-outils-metiers/Fiche_Logiciel_-_draw-io-Desktop.md)
- [Alternative draw.io : installation (Debian 13)](../../../../Debian/13/Vie-du-logiciel/draw.io/Fiche_Simple_-_VM_Debian_13_draw_io_Installer.md)
