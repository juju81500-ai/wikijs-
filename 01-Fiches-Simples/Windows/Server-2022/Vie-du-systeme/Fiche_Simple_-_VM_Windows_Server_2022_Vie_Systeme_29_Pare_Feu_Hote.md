# Fiche_Simple_-_VM_Windows_Server_2022_Vie_Systeme_29_Pare_Feu_Hote

- **Environnement** : Serveur Windows Server 2022
- **OS / Version** : Windows Server 2022; étape 29 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windowsserver2022`, `vie-du-systeme`, `cycle-de-vie`, `etape-29`

---

## Problème précis à résoudre

Activer et configurer le Pare-feu Windows avec fonctions avancées de sécurité.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir **Pare-feu Windows Defender avec fonctions avancées de sécurité** (`wf.msc`) et contrôler les trois profils.
   ```powershell
   Get-NetFirewallProfile | Select-Object Name, Enabled, DefaultInboundAction, DefaultOutboundAction
   ```
   👉 Explication : les trois profils doivent être activés, entrant bloqué par défaut.

2. Activer les profils si nécessaire :
   ```powershell
   Set-NetFirewallProfile -Profile Domain,Private,Public -Enabled True -DefaultInboundAction Block
   ```
   👉 Explication : applique le pare-feu partout.

3. Ouvrir un flux précis depuis une source limitée (remplacer `PORT` et `IP_SOURCE`) :
   ```powershell
   New-NetFirewallRule -DisplayName 'Service APP' -Direction Inbound -Protocol TCP -LocalPort PORT -RemoteAddress IP_SOURCE -Action Allow
   ```
   👉 Explication : autorise uniquement la source nécessaire.

## 2. Production — Contrôles

Journaliser les paquets rejetés (`Set-NetFirewallProfile -LogBlocked True`) et gérer les règles par GPO.

## 3. Production — Sécurité

Ne jamais désactiver le pare-feu pour un test; créer une règle ciblée à la place.

## Validation et retour arrière

- **Validation** : `Get-NetFirewallProfile` montre `Enabled True` et seuls les flux attendus passent.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Windows Server 2022](./Sommaire_-_Vie_du_systeme_Windows_Server_2022.md)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows-server/)
