# Fiche_Simple_-_VM_Windows_Server_2022_PRTG_Recette.md

- **Environnement** : Serveur Windows dédié ou VM, accès d'administration restreint
- **OS / Version** : Windows Server 2022 ou 2025 en Desktop Experience; PRTG Network Monitor maintenu
- **Catégorie** : supervision / SNMP / WMI
- **Tags** : `prtg`, `windows-server`, `supervision`, `recette`

---

## Problème précis à résoudre

Valider le service, l'alerte et les permissions.

## 1. Hors-Production (Lab / Test / POC)

1. Confirmer l'état du service Core :
   ```powershell
   Get-Service -Name 'PRTG*'
   ```
   👉 Explication : les services PRTG doivent être `Running`.

2. Vérifier accès Web et certificat dans le navigateur.
   👉 Explication : aucun avertissement de certificat ne doit rester.

3. Tester une alerte de seuil sur un capteur de test, son destinataire et sa résolution.
   👉 Explication : on prouve la chaîne de notification.

4. Examiner CPU/RAM/disque, durée des scans et journaux système : **Setup > System Administration > System Status** ou **Logs**.
   👉 Explication : on détecte une surcharge.

5. Valider les permissions avec un compte opérateur non administrateur.
   👉 Explication : il ne doit pas pouvoir modifier la configuration.

## 2. Production — Contrôles

Archiver le résultat de la recette.

## 3. Production — Sécurité

- Vérifier qu'un compte opérateur n'a pas de droits d'administration.

## Validation et retour arrière

- **Validation** : Service actif, capteurs pilotes `Up`, alerte reçue.
- **Retour arrière** : Reprendre l'étape fautive; si besoin, retirer l'appareil pilote.

## Si le problème n'est pas résolu

- [Paessler — Exigences système PRTG](https://www.paessler.com/manuals/prtg/system_requirements)
- [Paessler — Installer le Core Server](https://www.paessler.com/manuals/prtg/install_a_prtg_core_server)
- [Guide complet — recette](../../../../../02-Fiches-Completes/Windows/Server-2022/Installation-Deploiement/47_Deploiement_PRTG_Network_Monitor_Windows_Server.md#5-recette)
