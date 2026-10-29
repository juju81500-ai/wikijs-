---
title: "Fiche Simple - Windows Server 2022 StarWind Virtual SAN Mettre A Jour Retour Arriere"
description: "Préparer une mise à jour StarWind contrôlée et un retour arrière vérifié."
published: true
date: 2026-10-29T20:47:51Z
tags: ["starwind", "virtual-san", "windows-server", "mise-a-jour", "retour-arriere"]
editor: markdown
dateCreated: 2026-10-29T20:47:51Z
dateModified: 2026-10-29T20:47:51Z
---

# Fiche_Simple_-_Windows_Server_2022_StarWind_Virtual_SAN_Mettre_A_Jour_Retour_Arriere

- **Environnement** : Windows Server 2022 avec StarWind Virtual SAN; fenêtre de maintenance approuvée
- **OS / Version** : Windows Server 2022; compatibilité StarWind à confirmer auprès de l’éditeur
- **Catégorie** : stockage SAN / maintenance
- **Tags** : `starwind`, `virtual-san`, `windows-server`, `mise-a-jour`, `retour-arriere`

---

## Problème précis à résoudre

Préparer une mise à jour StarWind contrôlée et un retour arrière vérifié.

## 1. Hors-Production (Lab / Test / POC)

1. Relever les versions de Windows, StarWind, hyperviseur, pilotes et firmware; vérifier la matrice et les notes de version officielles.
   👉 Explication : ne pas extrapoler une compatibilité d’une version ou topologie à une autre.
2. Sauvegarder les données avec l’outil des charges et exporter la configuration selon le guide éditeur exact de la version; tester une restauration.
   👉 Explication : une mise à jour ne constitue pas un plan de reprise.
3. Vérifier dans la documentation le type d’installation et l’ordre de mise à jour; obtenir le paquet depuis le portail officiel et contrôler son intégrité selon les instructions éditeur.
   👉 Explication : n’appliquer aucun ordre générique à un cluster actif.
4. Sur une VM de test, suivre l’assistant graphique officiel de la version puis vérifier l’état dans la console StarWind et **Server Manager > Tools > Services**.
   👉 Explication : PowerShell en lecture seule peut confirmer l’état des services avec `Get-Service -Name '*StarWind*'`; ne pas inventer de commande de mise à jour produit.
5. Tester accès des volumes, état des nœuds et une charge non critique; consigner résultat et version.
   👉 Explication : comparer avec l’état observé avant changement.

## 2. Production — Contrôles

- Ne procéder que si le support, l’ordre, la compatibilité et le retour sont confirmés pour la topologie.
- Suspendre l’intervention et contacter StarWind si un élément n’est pas décrit.

## 3. Production — Sécurité

- Utiliser uniquement des paquets officiels; limiter les droits et protéger les sauvegardes.
- Ne pas désactiver la validation de signature ni exposer l’administration.

## Validation et retour arrière

- **Validation** : version attendue, état sain, volumes accessibles et test applicatif concluant.
- **Retour arrière** : rétrograder uniquement si StarWind documente ce scénario précis; sinon restaurer selon le plan approuvé et contacter le support.

## Si le problème n'est pas résolu

- [StarWind — Virtual SAN](https://www.starwindsoftware.com/starwind-virtual-san)
- [StarWind — bibliothèque officielle de ressources](https://www.starwindsoftware.com/resource-library)
- [Fiche d’entrée du logiciel](/01-fiches-simples/logiciels/06-stockage-et-san-nas/fiche-logiciel-starwind-virtual-san)