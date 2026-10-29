# Fiche_Simple_-_VM_Windows_Server_2022_PRTG_Installer.md

- **Environnement** : Serveur Windows dédié ou VM, accès d'administration restreint
- **OS / Version** : Windows Server 2022 ou 2025 en Desktop Experience; PRTG Network Monitor maintenu
- **Catégorie** : supervision / SNMP / WMI
- **Tags** : `prtg`, `windows-server`, `supervision`, `installation`

---

## Problème précis à résoudre

Installer PRTG Core Server depuis l'installateur officiel.

## 1. Hors-Production (Lab / Test / POC)

1. Télécharger l'installateur depuis le site officiel Paessler et vérifier la signature (chemin d'exemple à remplacer) :
   ```powershell
   Get-AuthenticodeSignature 'C:\Installateurs\PRTG_Setup.exe'
   ```
   👉 Explication : le statut `Valid` et l'éditeur Paessler confirment l'origine.

2. Exécuter l'installateur avec un compte administrateur local dédié (clic droit > **Exécuter en tant qu'administrateur**).
   👉 Explication : l'assistant d'installation démarre.

3. Choisir le mode **Custom**, définir les répertoires programme et données, et ignorer l'auto-discovery initiale.
   👉 Explication : on évite tout scan global par défaut.

4. Terminer, configurer la licence/activation et ouvrir l'interface Web en HTTPS (ou le binding/TLS approuvé).
   👉 Explication : l'accès Web ne doit pas être en clair.

5. Définir un mot de passe administrateur robuste, les notifications système et le fuseau horaire.
   👉 Explication : ces réglages de base évitent des alertes décalées ou des accès faibles.

## 2. Production — Contrôles

Documenter licence, répertoires et compte d'installation.

## 3. Production — Sécurité

- Ne pas conserver le mot de passe administrateur par défaut.
- Toujours vérifier la signature de l'installateur.

## Validation et retour arrière

- **Validation** : L'interface Web répond en HTTPS et le service Core tourne.
- **Retour arrière** : Désinstaller PRTG via **Paramètres > Applications**; conserver la base si elle doit être réutilisée.

## Si le problème n'est pas résolu

- [Paessler — Exigences système PRTG](https://www.paessler.com/manuals/prtg/system_requirements)
- [Paessler — Installer le Core Server](https://www.paessler.com/manuals/prtg/install_a_prtg_core_server)
- [Guide complet — télécharger et installer](../../../../../02-Fiches-Completes/Windows/Server-2022/Installation-Deploiement/47_Deploiement_PRTG_Network_Monitor_Windows_Server.md#2-telecharger-et-installer)
