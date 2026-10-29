# Fiche_Simple_-_VM_Windows_11_Visio_Mise_A_Jour_Retour_Arriere

- **Environnement** : Poste Windows 11 x64 d'un utilisateur ou administrateur (VM de test puis poste pilote)
- **OS / Version** : Windows 11 x64; version Visio à vérifier auprès de l'éditeur
- **Catégorie** : outil de diagrammes / poste de travail

---

## Problème précis à résoudre

Mettre à jour Visio et revenir en arrière.

## 1. Hors-Production (Lab / Test / POC)

1. Lancer la mise à jour. PowerShell :
```powershell
& 'C:\Program Files\Common Files\Microsoft Shared\ClickToRun\OfficeC2RClient.exe' /update user
```
   👉 Explication : déclenche la mise à jour Click-to-Run ; GUI équivalent **Fichier > Compte > Options de mise à jour > Mettre à jour maintenant**.

2. Sur un parc : définir le canal par Intune ou GPO, et déployer en anneaux (pilote puis production).
   👉 Explication : limite l'impact d'une régression.

3. Retour arrière vers une version connue :
```powershell
& 'C:\Program Files\Common Files\Microsoft Shared\ClickToRun\OfficeC2RClient.exe' /update user updatetoversion=VERSION_CONNUE
```
   👉 Explication : VERSION_CONNUE est à remplacer par un numéro de build publié par Microsoft ; vérifier que la version cible est disponible sur le canal.

4. Désactiver temporairement les mises à jour automatiques pendant l'analyse de l'incident (GUI **Fichier > Compte > Options de mise à jour > Désactiver les mises à jour**).
   👉 Explication : à réactiver après résolution.

## 2. Production — Contrôles

- Noter la version avant/après.
- Anneau pilote d'abord.

## 3. Production — Sécurité

- Sources de mise à jour officielles uniquement.

## Validation et retour arrière

- **Validation** : Version attendue et démarrage correct.
- **Retour arrière** : Utiliser updatetoversion ou réinstaller via ODT avec la version précédente.

## Si le problème n'est pas résolu

- [Microsoft — Office Deployment Tool](https://learn.microsoft.com/fr-fr/deployoffice/overview-office-deployment-tool)
- [Microsoft — Visio, plans et tarifs](https://www.microsoft.com/fr-fr/microsoft-365/visio/compare-visio-options)
- [Fiche d'entrée du logiciel](/01-fiches-simples/logiciels/15-topologie-ipam-et-outils-metiers/fiche-logiciel-microsoft-visio)
- [Alternative draw.io : fiche d'entrée](/01-fiches-simples/logiciels/15-topologie-ipam-et-outils-metiers/fiche-logiciel-draw-io-desktop)
- [Alternative draw.io : installation (Debian 13)](/01-fiches-simples/debian/13/vie-du-logiciel/draw-io/fiche-simple-vm-debian-13-draw-io-installer)