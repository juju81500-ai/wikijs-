---
title: "Fiche Simple - Tout-en-un Diagnostic Connectivite"
description: "Isoler à quelle couche se situe un problème d'accès réseau, en commençant par des vérifications non destructives."
published: true
date: 2026-11-03T09:36:13Z
tags: ["transverse", "tout-en-un", "reseau", "connectivite", "diagnostic"]
editor: markdown
dateCreated: 2026-11-03T09:36:13Z
dateModified: 2026-11-03T09:36:13Z
---

# Fiche_Simple_-_Tout-en-un_Diagnostic_Connectivite

- **Environnement** : poste ou serveur Linux ou Windows
- **OS / Version** : multi-OS ; procédures de correction propres à chaque plateforme
- **Catégorie** : Tout-en-un / Réseaux et protocoles
- **Tags** : `transverse`, `tout-en-un`, `reseau`, `connectivite`, `diagnostic`

---

## Problème précis à résoudre

Isoler à quelle couche se situe un problème d'accès réseau, en commençant par des vérifications non destructives.

## 1. Hors-Production (Lab / Test / POC)

1. Relever l'adresse et les routes Linux :
   ```bash
   ip -br address
   ip route
   ```
   👉 Explication : vérifie que l'interface attendue est active et qu'une route existe ; ne modifie pas le réseau.

2. Relever l'adresse et la route Windows :
   ```powershell
   Get-NetIPConfiguration
   Get-NetRoute -AddressFamily IPv4 | Sort-Object RouteMetric
   ```
   👉 Explication : affiche les interfaces configurées et les routes IPv4, sans changement.

3. Tester la résolution puis un port TCP autorisé sous Linux (remplacer l'exemple par une cible du laboratoire) :
   ```bash
   HOTE=serveur-lab.example
   PORT=443
   getent hosts "$HOTE"
   timeout 5 bash -c ": >/dev/tcp/$HOTE/$PORT"
   ```
   👉 Explication : le premier contrôle la résolution ; le second teste l'ouverture TCP avec un délai court. Un échec ne prouve pas à lui seul une panne réseau.

4. Tester le port sous Windows (remplacer l'exemple par une cible du laboratoire) :
   ```powershell
   $Hote = 'serveur-lab.example'
   $Port = 443
   Test-NetConnection -ComputerName $Hote -Port $Port -InformationLevel Detailed
   ```
   👉 Explication : indique la résolution, l'adresse distante et l'état de la connexion TCP. Utiliser uniquement une cible autorisée.

5. Relever un chemin réseau si l'outil est installé et autorisé :
   ```bash
   tracepath HOTE
   ```
   👉 Explication : observe les sauts visibles ; certains routeurs filtrent ces sondes, ce qui ne signifie pas nécessairement une panne.

## 2. Production — Contrôles

Consigner l'heure, les adresses, le port cible et le segment réseau. Comparer avec un hôte fonctionnel du même VLAN et escalader au réseau avec les observations, sans envoyer de capture contenant des données client.

## 3. Production — Sécurité

Ne pas scanner une plage entière, tester des ports non autorisés ni désactiver le pare-feu pour diagnostiquer. Cette fiche limite les tests à une cible et un port approuvés.

## Validation et retour arrière

- **Validation** : l'état de l'interface, de la route, de la résolution et du port cible est consigné séparément.
- **Retour arrière** : aucune modification n'est effectuée. Tout changement doit suivre la fiche propre à l'OS, après snapshot et avec accès console.

## Si le problème n'est pas résolu

- [Fiches réseau Debian](../../../01-fiches-simples/debian/13/vie-du-systeme/fiches-par-theme/reseau)
- [Fiches réseau Rocky Linux](../../../01-fiches-simples/rocky-linux/9/vie-du-systeme/fiches-par-theme/reseau)
- [Fiches réseau Windows Server 2022](../../../01-fiches-simples/windows/server-2022/vie-du-systeme/fiches-par-theme/reseau)
- [Documentation Microsoft — Test-NetConnection](https://learn.microsoft.com/powershell/module/nettcpip/test-netconnection)