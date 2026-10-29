---
title: "Fiche Simple - VM Windows 10 Vie Systeme 11 Compte D Administration Delegue"
description: "Donner des droits d'administration limités et nominatifs au support, sans partager de compte."
published: true
date: 2026-10-29T20:22:10Z
tags: ["windows10", "vie-du-systeme", "cycle-de-vie", "etape-11"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Windows_10_Vie_Systeme_11_Compte_D_Administration_Delegue

- **Environnement** : PC Windows 10 (poste de travail)
- **OS / Version** : Windows 10; étape 11 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windows10`, `vie-du-systeme`, `cycle-de-vie`, `etape-11`

---

## Problème précis à résoudre

Donner des droits d'administration limités et nominatifs au support, sans partager de compte.

## 1. Hors-Production (Lab / Test / POC)

1. Créer un groupe local ou de domaine dédié au support : **Gestion de l'ordinateur > Utilisateurs et groupes locaux > Groupes > Nouveau groupe**.
   ```powershell
   New-LocalGroup -Name 'Support-Poste' -Description 'Support N2 du poste'
   ```
   👉 Explication : crée un groupe pour les techniciens autorisés.

2. Ajouter un compte nominatif (domaine) à ce groupe et au groupe Administrateurs seulement si nécessaire : **Paramètres > Comptes > Autres utilisateurs** pour un compte local.
   ```powershell
   Add-LocalGroupMember -Group 'Administrateurs' -Member 'DOMAINE\PRENOM.NOM'
   Get-LocalGroupMember -Group 'Administrateurs'
   ```
   👉 Explication : `DOMAINE\PRENOM.NOM` est le compte nominatif du technicien; le contrôle affiche les membres effectifs.

3. Préférer des groupes restreints par GPO : **Configuration ordinateur > Préférences > Paramètres du Panneau de configuration > Utilisateurs et groupes locaux**, ou Intune **Protection de compte > Groupes locaux**.
   ```powershell
   gpresult /r /scope computer
   ```
   👉 Explication : montre les GPO appliquées qui gèrent les groupes locaux.

4. Tester avec le compte délégué : ouvrir un terminal en administrateur (**clic droit sur Démarrer > Terminal (administrateur)**).
   ```powershell
   whoami /groups | Select-String 'Administrateurs|Support-Poste'
   ```
   👉 Explication : confirme les groupes du jeton de session.

## 2. Production — Contrôles

Un compte par technicien, rattaché à un groupe, avec rotation et revue trimestrielle des membres.

## 3. Production — Sécurité

Aucun compte partagé; l'utilisation de droits élevés est journalisée (événements 4672, 4732) et centralisée.

## Validation et retour arrière

- **Validation** : `Get-LocalGroupMember` ne contient que les comptes autorisés.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Windows 10](/01-fiches-simples/windows/client-10/vie-du-systeme/sommaire-vie-du-systeme-windows-10)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows/)