# Fiche_Simple_-_VM_Windows_Server_2025_Production_Retour_Arriere.md

- **Environnement** : Serveur physique ou VM Windows Server 2025 administré par l'organisation
- **OS / Version** : Windows Server 2025 Standard ou Datacenter
- **Catégorie** : installation / déploiement
- **Tags** : `windows-server-2025`, `installation`, `production`, `uefi`, `openssh`

---

## Problème précis à résoudre

Prévoir et appliquer le retour arrière en cas d'échec.

## 1. Hors-Production (Lab / Test / POC)

1. Avant toute migration ou ajout de rôle, confirmer une sauvegarde restaurable et un accès console :
   ```powershell
   wbadmin get versions
   ```
   👉 Explication : liste les sauvegardes Windows Server Backup disponibles; tester aussi la console de l'hyperviseur.

2. En cas d'échec, isoler le serveur depuis la console et préserver les journaux :
   ```powershell
   Get-NetAdapter | Disable-NetAdapter -Confirm:$false
   wevtutil epl System C:\Preuves\System.evtx
   wevtutil epl Application C:\Preuves\Application.evtx
   ```
   👉 Explication : coupe le réseau et exporte les journaux. GUI : **Panneau de configuration > Centre Réseau et partage > Modifier les paramètres de la carte > Désactiver**, **Observateur d'événements > Enregistrer tous les événements sous...**.

3. Appliquer le plan de restauration ou de réinstallation validé.
   👉 Explication : seul un plan préalablement testé est fiable.

## 2. Production — Contrôles

Ne pas désinstaller un rôle de production sans évaluer ses dépendances.

## 3. Production — Sécurité

- Préserver les journaux avant toute action.

## Validation et retour arrière

- **Validation** : Le serveur est revenu à un état connu et fonctionnel.
- **Retour arrière** : Cette étape est le retour arrière : restaurer la sauvegarde ou réinstaller.

## Si le problème n'est pas résolu

- [Microsoft Learn — Nouveautés de Windows Server 2025](https://learn.microsoft.com/en-us/windows-server/get-started/whats-new-windows-server-2025)
- [Microsoft Learn — Installation de Windows Server](https://learn.microsoft.com/en-us/windows-server/get-started/install-options-server)
- [Guide complet déploiement Windows Server 2025](../../../../../../02-Fiches-Completes/Windows/Server-2025/Installation-Deploiement/30_Deploiement_Windows_Server_2025_Production.md#6-retour-arriere)
