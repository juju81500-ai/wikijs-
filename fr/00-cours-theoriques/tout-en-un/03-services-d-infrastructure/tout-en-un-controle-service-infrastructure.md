---
title: "Fiche Simple - Tout-en-un Controle Service Infrastructure"
description: "Établir si un service d'infrastructure est disponible, à l'écoute sur le port attendu et fonctionnel sans redémarrage ni modification de configuration."
published: true
date: 2026-11-03T09:36:13Z
tags: ["transverse", "tout-en-un", "service", "infrastructure", "diagnostic"]
editor: markdown
dateCreated: 2026-11-03T09:36:13Z
dateModified: 2026-11-03T09:36:13Z
---

# Fiche_Simple_-_Tout-en-un_Controle_Service_Infrastructure

- **Environnement** : serveur d'infrastructure Linux ou Windows
- **OS / Version** : multi-OS ; les commandes ci-dessous sont à valider sur la version cible
- **Catégorie** : Tout-en-un / Services d'infrastructure
- **Tags** : `transverse`, `tout-en-un`, `service`, `infrastructure`, `diagnostic`

---

## Problème précis à résoudre

Établir si un service d'infrastructure est disponible, à l'écoute sur le port attendu et fonctionnel sans redémarrage ni modification de configuration.

## 1. Hors-Production (Lab / Test / POC)

1. Relever le service et son état sous Linux (remplacer le nom par un service autorisé) :
   ```bash
   SERVICE=ssh
   systemctl is-active "$SERVICE"
   systemctl is-enabled "$SERVICE"
   systemctl status "$SERVICE" --no-pager
   ```
   👉 Explication : distingue l'état courant de l'activation au démarrage ; `status` peut exposer des chemins ou noms internes, à ne pas publier sans revue.

2. Consulter les journaux récents :
   ```bash
   journalctl -u "$SERVICE" --since "-30 min" --no-pager
   ```
   👉 Explication : limite la collecte à une fenêtre courte et au service concerné ; protéger les journaux qui contiennent des données personnelles ou des secrets.

3. Vérifier l'écoute d'un port Linux connu :
   ```bash
   PORT=22
   ss -lntup "( sport = :$PORT )"
   ```
   👉 Explication : affiche les sockets correspondants localement ; l'écoute seule ne prouve pas l'accessibilité depuis un autre segment.

4. Contrôler sous Windows sans arrêter le service :
   ```powershell
   $Service = 'Dnscache'
   Get-Service -Name $Service | Format-List Name, Status, StartType
   Get-WinEvent -FilterHashtable @{ LogName = 'System'; StartTime = (Get-Date).AddMinutes(-30) } -MaxEvents 30 |
     Where-Object ProviderName -match 'Service Control Manager'
   ```
   👉 Explication : consulte l'état et un échantillon récent des événements de gestion des services ; les droits et journaux disponibles varient selon le rôle.

5. Tester uniquement une cible et un port approuvés :
   ```powershell
   Test-NetConnection -ComputerName 'serveur-lab.example' -Port 443
   ```
   👉 Explication : contrôle une connexion [[Glossary:TCP]] précise ; n'effectue ni balayage ni changement de pare-feu.

## 2. Production — Contrôles

Consigner l'heure, le service, la version, l'hôte, le port attendu, le résultat applicatif et les journaux pertinents. Comparer à un hôte sain et à la supervision avant d'envisager un redémarrage.

## 3. Production — Sécurité

Ne pas publier de journaux bruts, de noms de clients, de jetons ni de paramètres internes. Ne pas redémarrer un service critique sur la base de son seul état `inactive` : vérifier les dépendances, le cluster et la fenêtre de changement.

## Validation et retour arrière

- **Validation** : service actif ou état attendu documenté, port et contrôle applicatif conformes.
- **Retour arrière** : aucune modification n'a été effectuée. Tout redémarrage ou changement de configuration suit la procédure propre au produit avec accès de secours.

## Si le problème n'est pas résolu

- Consulter la fiche de diagnostic propre au service et à sa version.
- [Documentation systemd — systemctl](https://www.freedesktop.org/software/systemd/man/latest/systemctl.html)
- [Documentation Microsoft — Get-Service](https://learn.microsoft.com/powershell/module/microsoft.powershell.management/get-service)

## Historique de vérification

| Vérifié le | OS / version | Logiciel / version | Testeur | Verdict | Sources |
|---|---|---|---|---|---|
| 2026-10-31 | Multi-OS | — | — | Non testé sur plateforme cible | Liens éditeurs ci-dessus |