---
title: "Fiche Simple - VM Windows Server 2022 Journaux WEF"
description: "Centraliser les journaux d'événements de plusieurs serveurs Windows sur un collecteur unique grâce à Windows Event Forwarding (WEF), afin de disposer d'une vue unifiée des connexions et des erreurs système."
published: true
date: 2026-10-29T20:22:42Z
tags: ["[windows-server-2022]", "[wef]", "[wecutil]", "[event-forwarding]", "[winrm]", "[powershell]"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# 📄 Fiche_Simple_-_VM_Windows_Server_2022_Journaux_WEF

- **Environnement** : VM (Windows Server 2022, serveur collecteur WEF) / Serveurs et postes sources
- **OS / Version** : Windows Server 2022 - Famille Windows Server
- **Catégorie** : Système & Services / Journaux et supervision
- **Tags** : `[windows-server-2022]`, `[wef]`, `[wecutil]`, `[event-forwarding]`, `[winrm]`, `[powershell]`

## 🎯 Problème précis à résoudre
Centraliser les journaux d'événements de plusieurs serveurs Windows sur un collecteur unique grâce à Windows Event Forwarding (WEF), afin de disposer d'une vue unifiée des connexions et des erreurs système.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Sur le serveur collecteur, activer le service de collecte et WinRM :
   ```powershell
   wecutil qc /q
   ```
   👉 Explication : Démarre le service Windows Event Collector et configure WinRM en mode silencieux (`/q`).
2. Sur chaque serveur source, autoriser WinRM à recevoir les abonnements :
   ```powershell
   winrm quickconfig -q
   ```
   👉 Explication : Ouvre l'écoute WinRM nécessaire à la communication entre la source et le collecteur.
3. Lister les abonnements existants et vérifier le journal de réception :
   ```powershell
   wecutil es
   wevtutil gl ForwardedEvents
   ```
   👉 Explication : Liste les abonnements présents et affiche la configuration du journal ForwardedEvents. Créer l'abonnement dans l'Observateur d'événements (Abonnements > Créer un abonnement) avec le type « Initié par la source » pour ce lab.

---

## ⚡ 2. Production — Façon Simplifiée
1. Indiquer aux sources l'adresse du collecteur par stratégie de registre (à déployer par GPO en production) :
   ```powershell
   $key = "HKLM:\SOFTWARE\Policies\Microsoft\Windows\EventLog\EventForwarding\SubscriptionManager"
   New-Item -Path $key -Force | Out-Null
   Set-ItemProperty -Path $key -Name "1" -Value "Server=http://<nom_collecteur>.<nom_domaine>:5985/wsman/SubscriptionManager/WEC,Refresh=60" -Type String
   ```
   👉 Explication : Correspond à la stratégie « Configurer la cible de transfert ». Refresh=60 demande aux sources de consulter leur abonnement toutes les 60 secondes.
2. Contrôler l'état d'exécution de l'abonnement sur le collecteur :
   ```powershell
   wecutil gs "<nom_abonnement>"
   wecutil gr "<nom_abonnement>"
   ```
   👉 Explication : `gs` affiche la définition de l'abonnement et `gr` son état d'exécution, avec la liste des sources connectées.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Interdire le trafic WinRM non chiffré sur le collecteur :
   ```powershell
   Set-Item -Path WSMan:\localhost\Service\AllowUnencrypted -Value $false
   Get-Item -Path WSMan:\localhost\Service\AllowUnencrypted
   ```
   👉 Explication : Force le chiffrement des échanges WinRM. Le trafic entre sources et collecteur reste ainsi protégé sur le réseau.
2. Dimensionner le journal ForwardedEvents pour éviter la perte d'événements :
   ```powershell
   wevtutil sl ForwardedEvents /ms:1073741824
   ```
   👉 Explication : Fixe la taille maximale à 1 Go. Au-delà, les anciens événements sont écrasés : l'archivage vers un SIEM doit être prévu.
3. Relire les événements reçus avec leur machine d'origine :
   ```powershell
   Get-WinEvent -LogName ForwardedEvents -MaxEvents 20 | Select-Object TimeCreated, MachineName, Id, Message
   ```
   👉 Explication : Vérifie que les événements arrivent bien et que chaque source est identifiée. Une source absente doit être contrôlée (pare-feu, GPO, service Wecsvc).