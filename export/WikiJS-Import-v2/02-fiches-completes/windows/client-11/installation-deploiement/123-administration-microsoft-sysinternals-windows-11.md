---
title: "Utiliser Microsoft Sysinternals pour le diagnostic sur Windows 11"
description: "Fiche simple : [périmètre et précautions Sysinternals](../../../../01-Fiches-Simples/Windows/Client-11/Vie-du-logiciel/Sysinternals/FicheSimple-VMWindows11SysinternalsPerimetrePrecautions.md)."
published: true
date: 2026-10-29T20:14:10Z
tags: ["sysinternals", "windows11", "diagnostic", "process-explorer", "autoruns", "process-monitor", "defense"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Utiliser Microsoft Sysinternals pour le diagnostic sur Windows 11

- **OS / Version** : Windows 11; suite Sysinternals téléchargée depuis Microsoft Learn ou Microsoft Store
- **Type de fiche** : Installation/Déploiement
- **Périmètre** : acquisition vérifiée et usage local de Process Explorer, Autoruns et Process Monitor pour le diagnostic défensif
- **Catégorie** : administration / diagnostic Windows
- **Tags** : `sysinternals`, `windows11`, `diagnostic`, `process-explorer`, `autoruns`, `process-monitor`, `defense`

## 1. Périmètre et précautions

Fiche simple : [périmètre et précautions Sysinternals](/01-fiches-simples/windows/client-11/vie-du-logiciel/sysinternals/fiche-simple-vm-windows-11-sysinternals-perimetre-precautions).

Sysinternals est une collection d'outils d'administration et de diagnostic Windows. Cette fiche se limite à l'inventaire local, au diagnostic de processus et à l'examen des démarrages automatiques sur un poste administré. Elle ne décrit ni accès distant, ni modification de comptes, ni exécution de commandes sur des tiers.

Obtenir une autorisation avant d'examiner un poste d'un utilisateur ou de recueillir une trace. Les traces peuvent contenir noms d'utilisateurs, chemins, arguments de processus, données personnelles ou secrets; limiter la collecte et protéger les fichiers. Utiliser un compte standard et élever les droits uniquement si le diagnostic le requiert.

## 2. Télécharger et vérifier la suite

Fiche simple : [télécharger et vérifier la suite Sysinternals](/01-fiches-simples/windows/client-11/vie-du-logiciel/sysinternals/fiche-simple-vm-windows-11-sysinternals-telecharger-verifier).

Télécharger la suite depuis la page Microsoft Learn et l'extraire dans un répertoire contrôlé. Alternative : installer l'application officielle Microsoft Store. Ne pas utiliser de miroir non autorisé.

Vérifier la signature Authenticode des exécutables avant usage :

```powershell
Get-AuthenticodeSignature .\procexp64.exe | Format-List Status,StatusMessage,SignerCertificate
Get-AuthenticodeSignature .\autorunsc64.exe | Format-List Status,StatusMessage,SignerCertificate
```

Le statut doit être `Valid` et le signataire attendu. En cas de signature invalide, fichier altéré ou source incertaine, ne pas lancer l'outil; supprimer l'archive selon la politique de poste et signaler l'incident.

## 3. Diagnostic en lecture seule

Fiche simple : [diagnostic en lecture seule avec Sysinternals](/01-fiches-simples/windows/client-11/vie-du-logiciel/sysinternals/fiche-simple-vm-windows-11-sysinternals-diagnostic-lecture-seule).

### Process Explorer

Lancer `procexp64.exe` et examiner l'arborescence des processus, éditeur/signature, chemin d'image, parent, consommation de ressources et connexions associées lorsque disponibles. Comparer les résultats à l'inventaire logiciel et aux journaux de sécurité. Ne pas terminer un processus système sur la seule base d'un nom ou d'une alerte heuristique.

### Autoruns

Lancer Autoruns et consulter les emplacements de démarrage automatique. Activer la vérification des signatures et masquer les entrées Microsoft signées pour réduire le bruit, sans interpréter l'absence de signature comme preuve de malveillance. Enregistrer un export seulement si nécessaire et le stocker dans un emplacement protégé.

Ne pas décocher ni supprimer une entrée pendant l'inventaire initial. Pour une entrée inconnue, noter son chemin, éditeur, empreinte et contexte, puis suivre le processus d'analyse et de changement approuvé.

### Process Monitor

Process Monitor collecte de nombreux événements système. Définir d'abord des filtres ciblés, une durée courte et les catégories requises; éviter une collecte globale prolongée. Sauvegarder au format natif seulement si nécessaire, avec accès limité et durée de rétention définie.

## 4. Collecte et validation

Fiche simple : [collecte et validation Sysinternals](/01-fiches-simples/windows/client-11/vie-du-logiciel/sysinternals/fiche-simple-vm-windows-11-sysinternals-collecte-validation).

- Consigner le poste, utilisateur/consentement selon la politique, l'heure, la version de Sysinternals, le motif et les filtres choisis.
- Examiner les métadonnées et la signature avant d'interpréter le comportement.
- Corroborer avec Defender, journaux Windows, inventaire de gestion et données de supervision.
- Faire relire toute action corrective; conserver l'état initial et un plan de restauration.
- Supprimer les traces temporaires de manière approuvée après transfert vers le dépôt sécurisé.

## 5. Retour arrière et limites

Fiche simple : [retour arrière et limites de Sysinternals](/01-fiches-simples/windows/client-11/vie-du-logiciel/sysinternals/fiche-simple-vm-windows-11-sysinternals-retour-arriere-limites).

La simple exécution des outils ne modifie généralement pas la configuration; des exports, filtres persistants ou préférences utilisateur peuvent toutefois être écrits. Fermer les outils, supprimer les exports temporaires suivant la politique et restaurer les préférences sauvegardées si nécessaire.

Sysinternals est un outil d'observation, pas un verdict antivirus. Les signatures valides ne garantissent pas qu'un fichier soit sûr et les résultats doivent être corroborés. Les outils de la suite qui modifient comptes, processus, démarrage ou état système ne sont pas couverts par cette fiche.

## Sources

- [Microsoft Learn — Sysinternals Suite](https://learn.microsoft.com/en-us/sysinternals/downloads/sysinternals-suite)
- [Microsoft Learn — Process Explorer](https://learn.microsoft.com/en-us/sysinternals/downloads/process-explorer)
- [Microsoft Learn — Autoruns](https://learn.microsoft.com/en-us/sysinternals/downloads/autoruns)
- [Microsoft Learn — Process Monitor](https://learn.microsoft.com/en-us/sysinternals/downloads/procmon)
- [Microsoft Learn — Get-AuthenticodeSignature](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.security/get-authenticodesignature)

Aucune collecte n'a été réalisée sur un poste cible. Tout usage doit respecter l'autorisation, la minimisation des données et la politique de conservation de l'organisation.