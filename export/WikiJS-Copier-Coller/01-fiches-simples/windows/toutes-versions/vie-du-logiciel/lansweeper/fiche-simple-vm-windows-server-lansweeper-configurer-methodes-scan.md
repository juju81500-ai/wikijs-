# Fiche_Simple_-_VM_Windows_Server_Lansweeper_Configurer_Methodes_Scan.md

- **Environnement** : Serveur Windows x64 avec Lansweeper Classic (SQL LocalDB ou SQL Server selon l'échelle)
- **OS / Version** : Windows Server 2022 recommandé; Lansweeper Classic selon la matrice officielle
- **Catégorie** : inventaire de parc / découverte réseau

---

## Problème précis à résoudre

Choisir la méthode de scan adaptée à chaque type d'actif.

## 1. Hors-Production (Lab / Test / POC)

1. Postes Windows: choisir scan agentless WMI ou **LsAgent**.
   👉 Explication : l'agent réduit les ports entrants et convient aux appareils hors site.

2. Linux/macOS: privilégier les agents, ou SSH avec compte restreint.
   👉 Explication : limite les privilèges.

3. Équipements réseau et NAS: configurer SNMPv3 en lecture seule avec une liste de cibles définie.
   👉 Explication : évite une découverte trop large.

4. Espacer et limiter les scans; ne lancer aucune découverte large sans fenêtre approuvée.
   👉 Explication : limite l'impact réseau.

5. Vérifier le pare-feu selon les ports officiels du scénario choisi; sur le serveur de scan :
   ```powershell
   Get-NetFirewallRule -Enabled True -Direction Inbound | Select-Object -First 20 DisplayName
   ```
   👉 Explication : aperçu des règles entrantes actives; n'ouvrir aucune règle à tout le réseau en dépannage.

## 2. Production — Contrôles

Documenter les ports ouverts, leurs sources et leur justification.

## 3. Production — Sécurité

- Ne jamais ouvrir de règles à tout le réseau pour dépanner.

## Validation et retour arrière

- **Validation** : les méthodes de scan sont définies par type d'actif avec ports documentés.
- **Retour arrière** : désactiver la méthode de scan ou la règle de pare-feu ajoutée.

## Si le problème n'est pas résolu

- [Lansweeper — scan Windows](https://docs.lansweeper.com/classic/docs/windows-domain-scanning-requirements.md)
- [Lansweeper Classic — prérequis](https://docs.lansweeper.com/classic/docs/lansweeper-installation-requirements.md)
- [Guide complet](/02-fiches-completes/windows/server-2022/installation-deploiement/44-deploiement-lansweeper-classic-windows-server#4-configurer-les-methodes-de-scan)