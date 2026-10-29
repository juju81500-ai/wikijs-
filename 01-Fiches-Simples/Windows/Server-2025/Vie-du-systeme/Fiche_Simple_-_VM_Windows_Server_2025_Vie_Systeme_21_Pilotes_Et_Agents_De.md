# Fiche_Simple_-_VM_Windows_Server_2025_Vie_Systeme_21_Pilotes_Et_Agents_De

- **Environnement** : Serveur Windows Server 2025
- **OS / Version** : Windows Server 2025; étape 21 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windowsserver2025`, `vie-du-systeme`, `cycle-de-vie`, `etape-21`

---

## Problème précis à résoudre

Installer les pilotes et services d'intégration.

## 1. Hors-Production (Lab / Test / POC)

1. Hyper-V : les services d'intégration passent par Windows Update. Vérifier-les dans **Gestionnaire Hyper-V > Paramètres de la VM > Services d'intégration**.
   ```powershell
   Get-VMIntegrationService -VMName NOM_VM
   ```
   👉 Explication : tous les services doivent être activés et `OK`.

2. Sur la VM, repérer les périphériques sans pilote (**Gestionnaire de périphériques**) :
   ```powershell
   Get-PnpDevice -Status Error,Unknown | Select-Object FriendlyName, Class, Status
   ```
   👉 Explication : une liste vide signifie que tous les pilotes sont chargés.

3. VMware ou Proxmox : monter l'ISO d'outils (VMware Tools ou VirtIO) et l'installer :
   ```powershell
   Get-Service | Where-Object Name -match 'VMTools|QEMU|vmicheartbeat' | Select-Object Name, Status
   ```
   👉 Explication : confirme que l'agent est démarré.

## 2. Production — Contrôles

Installer l'agent adapté à l'hyperviseur et le conserver à jour.

## 3. Production — Sécurité

Télécharger les pilotes uniquement depuis l'éditeur de l'hyperviseur ou du constructeur.

## Validation et retour arrière

- **Validation** : Aucun périphérique en erreur et agent actif.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Windows Server 2025](./Sommaire_-_Vie_du_systeme_Windows_Server_2025.md)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows-server/)
