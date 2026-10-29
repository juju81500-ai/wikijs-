---
title: "Fiche Simple - VM Windows 11 Securite Activer BitLocker TPM"
description: "Activer le chiffrement BitLocker du volume système Windows 11, vérifier l'état du TPM et sauvegarder la clé de récupération dans un emplacement distinct et contrôlé."
published: true
date: 2026-10-29T20:22:42Z
tags: ["[windows-11]", "[bitlocker]", "[tpm]", "[chiffrement]", "[recovery-key]", "[hardening]"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# 📄 Fiche_Simple_-_VM_Windows_11_Securite_Activer_BitLocker_TPM.md

- **Environnement** : VM ou poste client Windows
- **OS / Version** : Windows 11 Pro, Enterprise ou Education
- **Catégorie** : Sécurité / Chiffrement
- **Tags** : `[windows-11]`, `[bitlocker]`, `[tpm]`, `[chiffrement]`, `[recovery-key]`, `[hardening]`

## 🎯 Problème précis à résoudre
Activer le chiffrement BitLocker du volume système Windows 11, vérifier l'état du TPM et sauvegarder la clé de récupération dans un emplacement distinct et contrôlé.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Vérifier l'édition Windows, le TPM et l'état actuel du volume :
   ```powershell
   Get-Tpm
   Get-BitLockerVolume -MountPoint C:
   ```
2. Dans **Panneau de configuration > Système et sécurité > Chiffrement de lecteur BitLocker**, sélectionner **Activer BitLocker** pour le lecteur système.
3. Suivre l'assistant, sauvegarder la clé de récupération hors du poste, choisir le chiffrement puis redémarrer si demandé.
   👉 *Explication : BitLocker avec gestion complète est disponible sur les éditions Pro/Enterprise/Education; l'option « Chiffrement de l'appareil » sur d'autres éditions varie selon le matériel et la gestion.*

## ⚡ 2. Production — Façon Simplifiée
1. Vérifier les stratégies de chiffrement de l'organisation et l'escrow de clé de récupération (AD DS, Entra ID ou coffre approuvé) avant le démarrage.
2. Activer BitLocker avec l'assistant GUI et vérifier que la clé a été sauvegardée et que le chiffrement a commencé :
   ```powershell
   Get-BitLockerVolume -MountPoint C: | Select-Object MountPoint, VolumeStatus, ProtectionStatus, EncryptionPercentage
   ```
3. Laisser le poste alimenté jusqu'à la fin du chiffrement et vérifier de nouveau son état.

## 🔒 3. Production — Façon Sécurisée
1. Ne jamais laisser la seule clé de récupération sur le volume chiffré ou dans un fichier non protégé sur le même poste.
2. Ne pas modifier le TPM, Secure Boot ou les paramètres de démarrage avant d'avoir confirmé l'accès à la clé de récupération.
3. Sur un parc géré, appliquer les stratégies centralisées de l'organisation plutôt que de choisir localement une méthode de récupération concurrente.

## ✅ Validation et retour arrière
- Confirmer `ProtectionStatus`, l'état du chiffrement et la présence de la clé dans le dépôt de récupération approuvé.
- Ne pas redémarrer en pensant que l'activation est terminée si le chiffrement est encore en cours.
- La désactivation du chiffrement peut prendre du temps; la réaliser uniquement selon la politique de l'organisation et surveiller l'état avec `Get-BitLockerVolume`.