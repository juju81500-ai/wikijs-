---
title: "Fiche Simple - Windows Server 2022 Nakivo Restaurer Interface"
description: "Restaurer des données ou une machine depuis un point de sauvegarde NAKIVO via la GUI, en test."
published: true
date: 2026-10-29T20:36:08Z
tags: ["nakivo", "restauration", "interface-web", "windows-server"]
editor: markdown
dateCreated: 2026-10-29T20:36:08Z
dateModified: 2026-10-29T20:36:08Z
---

# Fiche_Simple_-_Windows_Server_2022_Nakivo_Restaurer_Interface

- **Environnement** : `Serveur Windows Server 2022 (VM ou physique), compte administrateur local ou de domaine nominatif`
- **OS / Version** : `Windows Server 2022 (Desktop Experience ou Core selon support de la version); vérifier la compatibilité et la version courante du produit auprès de l'éditeur`
- **Catégorie** : `sauvegarde / restauration / NAKIVO`
- **Tags** : `nakivo`, `restauration`, `interface-web`, `windows-server`

---

## Problème précis à résoudre

Restaurer des données ou une machine depuis un point de sauvegarde NAKIVO via la GUI, en test.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir l'interface web et accéder à la restauration : menu **Recovery** ou équivalent selon la version.
   👉 Explication : c'est le point d'entrée des restaurations.

2. Choisir le type de restauration adapté (machine complète, fichiers ou objets applicatifs selon la licence et la source) et le point de restauration.
   👉 Explication : le type dépend de ce qui a été sauvegardé.

3. Choisir une destination de test isolée : nouveau nom, réseau isolé, ou dossier de test.
   👉 Explication : on évite d'écraser la production.

4. Lancer la restauration et suivre dans **Activities**.
   👉 Explication : la fin du job confirme le transfert.

5. Contrôler le résultat : démarrage de la machine de test ou ouverture des fichiers. PowerShell pour les fichiers restaurés :
```powershell
Get-ChildItem -Path CHEMIN_RESTAURE -Recurse | Measure-Object
```
   👉 Explication : CHEMIN_RESTAURE est à remplacer ; le nombre de fichiers est comparé à la source.

## 2. Production — Contrôles

- Planifier un test de restauration périodique.
- Consigner le temps de restauration.

## 3. Production — Sécurité

- Restaurer en environnement isolé d'abord.
- Ne pas exposer les données restaurées.

## Validation et retour arrière

- **Validation** : Les données ou la machine restaurée sont complètes et fonctionnelles.
- **Retour arrière** : Supprimer la machine ou les fichiers de test restaurés.

## Si le problème n'est pas résolu

- [NAKIVO — Help Center officiel](https://helpcenter.nakivo.com/)
- [NAKIVO — System Requirements](https://helpcenter.nakivo.com/display/NH/System+Requirements)
- [Fiche d'entrée du logiciel](/01-fiches-simples/logiciels/07-sauvegarde-restauration-et-pra-pca/fiche-logiciel-nakivo-altaro)