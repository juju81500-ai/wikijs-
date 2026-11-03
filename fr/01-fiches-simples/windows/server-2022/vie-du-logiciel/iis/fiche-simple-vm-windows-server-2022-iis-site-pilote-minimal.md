---
title: "fiche-simple-vm-windows-server-2022-iis-site-pilote-minimal"
description: "Créer un site statique de test isolé."
published: true
date: 2026-11-03T14:22:28Z
tags: ["iis", "windows-server-2022", "web-server", "tls", "application-pool"]
editor: markdown
dateCreated: 2026-11-03T14:22:28Z
dateModified: 2026-11-03T14:22:28Z
---

# fiche-simple-vm-windows-server-2022-iis-site-pilote-minimal.md

- **Environnement** : [[Glossary:VM]] Windows Server 2022 pilote
- **OS / Version** : Windows Server 2022; rôle Web Server ([[Glossary:IIS]])
- **Catégorie** : serveur Web / IIS
- **Tags** : `iis`, `windows-server-2022`, `web-server`, `tls`, `application-pool`

---

## Problème précis à résoudre

Créer un site statique de test isolé.

## 1. Hors-Production (Lab / Test / POC)

1. Créer le répertoire et la page de test :
   ```powershell
   New-Item -ItemType Directory -Path 'C:\Sites\Pilote' -Force
   Set-Content -Path 'C:\Sites\Pilote\index.html' -Value '<!doctype html><title>IIS pilote</title><h1>IIS pilote</h1>' -Encoding UTF8
   ```
   👉 Explication : contenu sans donnée métier.

2. [[Glossary:GUI]] : **Gestionnaire des services Internet (IIS) > clic droit sur Sites > Ajouter un site Web**, nom `Pilote`, chemin `C:\Sites\Pilote`, avec un pool d'applications dédié.
   👉 Explication : le site utilise son propre pool.

3. Configurer un binding correspondant au nom [[Glossary:DNS]] et au certificat prévus; pour un pilote local, limiter le test à localhost ou au réseau d'administration.
   👉 Explication : on évite toute exposition prématurée.

## 2. Production — Contrôles

Pour une application réelle, choisir l'identité de pool dédiée avec les permissions [[Glossary:NTFS]] minimales.

## 3. Production — Sécurité

- Ne pas accorder `Everyone:FullControl` ni utiliser un compte Administrateur.
- Ne pas exposer à Internet avant bindings, [[Glossary:TLS]], journaux, mises à jour, authentification et règles réseau.

## Validation et retour arrière

- **Validation** : Le site `Pilote` répond en local.
- **Retour arrière** : Supprimer le site `Pilote` dans IIS Manager et le dossier `C:\Sites\Pilote`.

## Si le problème n'est pas résolu

- [Microsoft Learn — documentation IIS](https://learn.microsoft.com/en-us/iis/)
- [Microsoft Learn — AppCmd.exe](https://learn.microsoft.com/en-us/iis/get-started/getting-started-with-iis/getting-started-with-appcmdexe)
- [Microsoft Learn — Application pools](https://learn.microsoft.com/en-us/iis/configuration/system.applicationhost/applicationpools/)
- [Guide complet installation IIS Windows Server 2022](/fr/02-fiches-completes/windows/server-2022/installation-deploiement/122-installation-iis-windows-server-2022#3-preparer-un-site-pilote-minimal)