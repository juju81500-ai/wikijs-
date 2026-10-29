---
title: "Fiche Simple - Windows Server 2022 StarWind Virtual SAN Sauvegarder Restaurer"
description: "Tester la récupération sans confondre réplication/disponibilité StarWind et sauvegarde indépendante des données."
published: true
date: 2026-10-29T20:49:36Z
tags: ["starwind", "virtual-san", "windows-server", "sauvegarde", "restauration"]
editor: markdown
dateCreated: 2026-10-29T20:49:36Z
dateModified: 2026-10-29T20:49:36Z
---

# Fiche_Simple_-_Windows_Server_2022_StarWind_Virtual_SAN_Sauvegarder_Restaurer

- **Environnement** : Windows Server 2022 avec StarWind Virtual SAN; laboratoire isolé
- **OS / Version** : Windows Server 2022; version StarWind à confirmer dans la documentation éditeur
- **Catégorie** : stockage SAN / sauvegarde et restauration
- **Tags** : `starwind`, `virtual-san`, `windows-server`, `sauvegarde`, `restauration`

---

## Problème précis à résoudre

Tester la récupération sans confondre réplication/disponibilité StarWind et sauvegarde indépendante des données.

## 1. Hors-Production (Lab / Test / POC)

1. Dans la console StarWind, relever version, topologie, nœuds, disques et dépendances; suivre la procédure d’export de configuration du guide officiel correspondant à cette version.
   👉 Explication : les libellés et mécanismes d’export dépendent du produit installé; ne pas supposer qu’un menu identique existe partout.
2. Si la fonctionnalité est absente, l’ajouter dans **Server Manager > Add Roles and Features > Features > Windows Server Backup**. Équivalent PowerShell administrateur :
   ```powershell
   Install-WindowsFeature Windows-Server-Backup
   ```
   👉 Explication : installe l’outil facultatif Windows Server Backup; vérifier la réussite avant de poursuivre.
3. Ouvrir **Server Manager > Tools > Windows Server Backup > Backup Once** et choisir un emplacement de destination distinct.
   👉 Explication : ceci protège les éléments locaux sélectionnés, mais ne garantit pas la cohérence applicative des données présentées par StarWind.
4. Configurer une sauvegarde applicative des charges hébergées, avec l’outil prévu pour ces charges et un dépôt séparé; réaliser un petit test.
   👉 Explication : les données de VM et applications doivent être sauvegardées au niveau approprié; un miroir ou une réplication ne remplace pas une copie indépendante.
5. Dans un environnement isolé, restaurer d’abord la configuration selon le guide StarWind de la version, puis restaurer une charge depuis son outil de sauvegarde.
   👉 Explication : ne pas écraser un volume ni réimporter un ancien état sur les nœuds actifs.
6. Vérifier depuis un client de test que les volumes et données attendus sont accessibles.
   👉 Explication : la restauration réelle est la preuve que la sauvegarde est exploitable.

## 2. Production — Contrôles

- Documenter RPO/RTO, cohérence, rétention, séparation du dépôt et procédure de restauration par charge.
- Traiter miroir/réplication comme disponibilité, jamais comme sauvegarde autonome.

## 3. Production — Sécurité

- Protéger les exports et copies par chiffrement et contrôle d’accès approuvés.
- Tester la restauration sur une cible isolée; ne pas écraser la source.

## Validation et retour arrière

- **Validation** : export de configuration conservé hors hôte et restauration d’une charge de test vérifiée.
- **Retour arrière** : conserver l’original intact; retirer les seules ressources de test après approbation.

## Si le problème n'est pas résolu

- [StarWind — Virtual SAN](https://www.starwindsoftware.com/starwind-virtual-san)
- [StarWind — bibliothèque officielle de ressources](https://www.starwindsoftware.com/resource-library)
- [Fiche d’entrée du logiciel](/01-fiches-simples/logiciels/06-stockage-et-san-nas/fiche-logiciel-starwind-virtual-san)