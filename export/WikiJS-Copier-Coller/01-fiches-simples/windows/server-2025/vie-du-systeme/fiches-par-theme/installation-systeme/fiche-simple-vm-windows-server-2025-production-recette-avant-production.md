# Fiche_Simple_-_VM_Windows_Server_2025_Production_Recette_Avant_Production.md

- **Environnement** : Serveur physique ou VM Windows Server 2025 administré par l'organisation
- **OS / Version** : Windows Server 2025 Standard ou Datacenter
- **Catégorie** : installation / déploiement

---

## Problème précis à résoudre

Valider le serveur avant sa mise en production.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier DNS, heure, connectivité depuis les réseaux autorisés, mises à jour, accès d'administration, supervision, sauvegarde/restauration et journaux.
   👉 Explication : on contrôle tous les points d'exploitation.

2. Contrôler les services et l'historique d'événements :
   ```powershell
   Get-Service | Where-Object Status -eq 'Stopped' | Select-Object -First 20 Name, DisplayName
   Get-WinEvent -FilterHashtable @{ LogName = 'System'; Level = 2; StartTime = (Get-Date).AddHours(-24) } -MaxEvents 20
   ```
   👉 Explication : aucune erreur inattendue ne doit subsister.

3. Tester un redémarrage planifié (**Démarrer > Alimentation > Redémarrer**) puis documenter version, édition, build, adresse, rôles, exceptions et propriétaire.
   👉 Explication : on prouve la reprise.

## 2. Production — Contrôles

Conserver la fiche de recette.

## 3. Production — Sécurité

- Ne pas mettre en production avec un écart non accepté.

## Validation et retour arrière

- **Validation** : Tous les points de recette sont validés.
- **Retour arrière** : Garder le serveur hors production jusqu'à correction.

## Si le problème n'est pas résolu

- [Microsoft Learn — Nouveautés de Windows Server 2025](https://learn.microsoft.com/en-us/windows-server/get-started/whats-new-windows-server-2025)
- [Microsoft Learn — Installation de Windows Server](https://learn.microsoft.com/en-us/windows-server/get-started/install-options-server)
- [Guide complet déploiement Windows Server 2025](/02-fiches-completes/windows/server-2025/installation-deploiement/30-deploiement-windows-server-2025-production#5-recette-avant-mise-en-production)