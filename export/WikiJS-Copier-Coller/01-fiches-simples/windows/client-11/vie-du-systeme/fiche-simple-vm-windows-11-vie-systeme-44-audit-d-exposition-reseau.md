# Fiche_Simple_-_VM_Windows_11_Vie_Systeme_44_Audit_D_Exposition_Reseau

- **Environnement** : PC Windows 11 (poste de travail)
- **OS / Version** : Windows 11; étape 44 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Vérifier de l'extérieur ce que le poste expose.

## 1. Hors-Production (Lab / Test / POC)

1. Depuis un autre poste du réseau d'administration, tester les ports courants (`ADRESSE_POSTE` est l'IP du poste contrôlé).
   ```powershell
   135,139,445,3389,5985,22 | ForEach-Object { Test-NetConnection ADRESSE_POSTE -Port $_ -WarningAction SilentlyContinue | Select-Object ComputerName,RemotePort,TcpTestSucceeded }
   ```
   👉 Explication : indique pour chaque port s'il répond.

2. Analyse complète autorisée avec Nmap, uniquement sur un périmètre approuvé par écrit.
   ```powershell
   nmap -sV -p- ADRESSE_POSTE
   ```
   👉 Explication : inventorie les ports et services exposés; dans le cadre d'un audit validé uniquement.

3. Comparer avec les règles du pare-feu locales.
   ```powershell
   Get-NetFirewallRule -Direction Inbound -Enabled True -Action Allow | Get-NetFirewallPortFilter | Select-Object Protocol,LocalPort
   ```
   👉 Explication : liste les ports autorisés en entrée.

4. Consigner les écarts et corriger (fermer le port ou ajuster le pare-feu).
   👉 Explication : le résultat doit rester identique au besoin documenté.

## 2. Production — Contrôles

Audit planifié, avec accord du responsable sécurité et horodatage dans le dossier.

## 3. Production — Sécurité

Ne jamais scanner un réseau ou un poste sans autorisation écrite.

## Validation et retour arrière

- **Validation** : Aucun port non prévu n'est atteignable.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Windows 11](/01-fiches-simples/windows/client-11/vie-du-systeme/sommaire-vie-du-systeme-windows-11)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows/)