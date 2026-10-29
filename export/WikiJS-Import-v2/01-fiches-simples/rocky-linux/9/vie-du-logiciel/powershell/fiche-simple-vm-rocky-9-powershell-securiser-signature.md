---
title: "Fiche Simple - VM Rocky 9 PowerShell Securiser Signature"
description: "Durcir l'usage de PowerShell 7 sur Linux et traiter la signature de scripts selon ce qui s'applique."
published: true
date: 2026-10-29T20:59:00Z
tags: ["rocky9", "powershell", "pwsh", "scripting"]
editor: markdown
dateCreated: 2026-10-29T20:59:00Z
dateModified: 2026-10-29T20:59:00Z
---

# Fiche_Simple_-_VM_Rocky_9_PowerShell_Securiser_Signature

- **Environnement** : VM Rocky Linux 9 de laboratoire, accès sudo, dépôt Microsoft pour RHEL 9
- **OS / Version** : Rocky Linux 9
- **Catégorie** : shell / scripting
- **Tags** : `rocky9`, `powershell`, `pwsh`, `scripting`

---

## Problème précis à résoudre

Durcir l'usage de PowerShell 7 sur Linux et traiter la signature de scripts selon ce qui s'applique.

## 1. Hors-Production (Lab / Test / POC)

1. Constater que la stratégie d'exécution ne s'applique pas :
   ```bash
   pwsh -NoLogo -NoProfile -Command 'Get-ExecutionPolicy -List'
   ```
   👉 Explication : sous Linux et macOS la stratégie est `Unrestricted` et non modifiable : elle ne constitue pas un contrôle ici.

2. Contrôler l'intégrité d'un script distribué par empreinte (CHEMIN_SCRIPT et FICHIER_EMPREINTES sont à remplacer) :
   ```bash
   sha256sum CHEMIN_SCRIPT
   sha256sum -c FICHIER_EMPREINTES
   ```
   👉 Explication : la signature Authenticode (`Set-/Get-AuthenticodeSignature`) est propre à Windows ; sous Linux on s'appuie sur des empreintes, des signatures GPG ou des commits Git signés.

3. Exécuter en compte non privilégié et refuser l'élévation inutile :
   ```bash
   id -un
   pwsh -NoLogo -NoProfile -File CHEMIN_SCRIPT
   ```
   👉 Explication : `-NoProfile` évite le chargement d'un profil non maîtrisé ; ne pas lancer pwsh avec sudo par défaut.

4. Activer une trace des sessions si votre politique l'exige :
   ```bash
   pwsh -NoLogo -Command 'Start-Transcript -Path ~/pwsh-transcript.log'
   ```
   👉 Explication : `Start-Transcript` journalise une session ; protéger le fichier (droits 600) car il peut contenir des données sensibles. La journalisation système (syslog) est décrite dans `about_Logging_Non-Windows`.

5. Limiter les modules installables aux dépôts approuvés :
   👉 Explication : garder PSGallery non approuvé, préférer un dépôt interne et épingler les versions.

## 2. Production — Contrôles

Définir une politique de scripts : provenance, relecture, empreintes publiées avec les versions. Commandes établies d'après la documentation officielle et non testées dans ce pack : à valider en lab avant toute production.

## 3. Production — Sécurité

- Pas de mot de passe dans les scripts : utiliser `Read-Host -AsSecureString`, un coffre ou le module SecretManagement après validation.
- Droits 600 sur journaux et transcripts.
- Ne pas confondre `ExecutionPolicy` et une frontière de sécurité.

## Validation et retour arrière

- **Validation** : empreintes concordantes, exécution en compte non privilégié, transcript protégé.
- **Retour arrière** : supprimer le transcript et les profils ajoutés ; aucun changement système n'est requis.

## Si le problème n'est pas résolu

- [Microsoft Learn — stratégies d'exécution](https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_execution_policies)
- [Microsoft Learn — journalisation hors Windows](https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_logging_non-windows)
- [Fiche connexe — Prerequis Limites](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/powershell/fiche-simple-vm-rocky-9-powershell-prerequis-limites)