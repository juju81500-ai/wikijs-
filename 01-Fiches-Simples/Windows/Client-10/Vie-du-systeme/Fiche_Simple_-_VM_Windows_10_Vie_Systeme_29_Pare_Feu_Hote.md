# Fiche_Simple_-_VM_Windows_10_Vie_Systeme_29_Pare_Feu_Hote

- **Environnement** : PC Windows 10 (poste de travail)
- **OS / Version** : Windows 10; étape 29 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windows10`, `vie-du-systeme`, `cycle-de-vie`, `etape-29`

---

## Problème précis à résoudre

Activer le Pare-feu Windows Defender avec une politique restrictive.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler et activer sur les trois profils : **Panneau de configuration > Pare-feu Windows Defender > Activer ou désactiver**, ou **Sécurité Windows > Pare-feu et protection réseau**.
   ```powershell
   Get-NetFirewallProfile | Select-Object Name,Enabled,DefaultInboundAction,DefaultOutboundAction
   Set-NetFirewallProfile -Profile Domain,Private,Public -Enabled True -DefaultInboundAction Block
   ```
   👉 Explication : active le pare-feu et bloque tout entrant non autorisé.

2. Autoriser le strict nécessaire, par exemple SSH depuis le réseau d'administration (`RESEAU_ADMIN`, au format CIDR).
   ```powershell
   New-NetFirewallRule -DisplayName 'SSH admin' -Direction Inbound -Protocol TCP -LocalPort 22 -RemoteAddress RESEAU_ADMIN -Action Allow
   ```
   👉 Explication : ouvre le port 22 uniquement depuis le réseau d'administration.

3. Activer la journalisation des paquets refusés : **wf.msc > Propriétés > Journalisation**.
   ```powershell
   Set-NetFirewallProfile -Profile Domain,Private,Public -LogBlocked True -LogFileName '%SystemRoot%\System32\LogFiles\Firewall\pfirewall.log'
   ```
   👉 Explication : trace les connexions bloquées.

4. Lister les règles actives entrantes.
   ```powershell
   Get-NetFirewallRule -Direction Inbound -Enabled True -Action Allow | Select-Object DisplayName,Profile | Sort-Object DisplayName
   ```
   👉 Explication : audit des règles ouvertes.

## 2. Production — Contrôles

Règles gérées par GPO ou Intune (Sécurité des points de terminaison > Pare-feu).

## 3. Production — Sécurité

Refus par défaut en entrée; pas de désactivation du pare-feu pour « tester ».

## Validation et retour arrière

- **Validation** : Les trois profils sont `Enabled : True` et seules les règles prévues existent.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Windows 10](./Sommaire_-_Vie_du_systeme_Windows_10.md)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows/)
