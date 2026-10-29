# Fiche_Simple_-_VM_Windows_10_Vie_Systeme_42_Journaux_Taille_Retention_Et

- **Environnement** : PC Windows 10 (poste de travail)
- **OS / Version** : Windows 10; étape 42 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windows10`, `vie-du-systeme`, `cycle-de-vie`, `etape-42`

---

## Problème précis à résoudre

Conserver et centraliser les journaux d'événements.

## 1. Hors-Production (Lab / Test / POC)

1. Régler la taille et la rétention : **Observateur d'événements > clic droit sur le journal > Propriétés**.
   ```powershell
   wevtutil gl Security
   wevtutil sl Security /ms:536870912
   Limit-EventLog -LogName Application -MaximumSize 100MB -OverflowAction OverwriteOlder
   ```
   👉 Explication : agrandit le journal Sécurité à 512 Mo (valeur en octets) et règle Application à 100 Mo.

2. Activer la transcription PowerShell et l'enregistrement des blocs de script : GPO **Composants Windows > Windows PowerShell**.
   ```powershell
   New-Item 'HKLM:\SOFTWARE\Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging' -Force | Out-Null
   Set-ItemProperty 'HKLM:\SOFTWARE\Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging' EnableScriptBlockLogging 1 -Type DWord
   ```
   👉 Explication : journalise les scripts exécutés (attention aux secrets saisis dans les commandes).

3. Centraliser avec le transfert d'événements Windows (WEF) vers un collecteur : GPO **Gestionnaire d'abonnements** ou agent SIEM.
   ```powershell
   winrm quickconfig -q
   wecutil qc /q
   ```
   👉 Explication : configure la collecte (`wecutil` côté collecteur, WinRM côté source).

4. Exporter un journal pour analyse.
   ```powershell
   wevtutil epl Security "$env:USERPROFILE\Security.evtx"
   ```
   👉 Explication : copie le journal Sécurité en fichier `.evtx`.

## 2. Production — Contrôles

Rétention conforme à la politique (par exemple 90 jours en ligne, un an archivé).

## 3. Production — Sécurité

Droits en lecture seule pour les analystes; journaux protégés contre l'effacement.

## Validation et retour arrière

- **Validation** : Les événements du poste apparaissent dans le collecteur.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Windows 10](./Sommaire_-_Vie_du_systeme_Windows_10.md)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows/)
