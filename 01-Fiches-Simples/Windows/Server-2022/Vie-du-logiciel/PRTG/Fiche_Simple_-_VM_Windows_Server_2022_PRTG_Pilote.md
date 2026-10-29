# Fiche_Simple_-_VM_Windows_Server_2022_PRTG_Pilote.md

- **Environnement** : Serveur Windows dédié ou VM, accès d'administration restreint
- **OS / Version** : Windows Server 2022 ou 2025 en Desktop Experience; PRTG Network Monitor maintenu
- **Catégorie** : supervision / SNMP / WMI
- **Tags** : `prtg`, `windows-server`, `supervision`, `pilote`, `capteurs`

---

## Problème précis à résoudre

Superviser un petit périmètre autorisé avant d'élargir.

## 1. Hors-Production (Lab / Test / POC)

1. Ajouter un équipement autorisé : **Devices > Add Device**, puis ajouter d'abord les capteurs Ping et HTTP.
   👉 Explication : on commence par des capteurs simples.

2. Ajouter ensuite SNMP ou WMI selon les permissions approuvées.
   👉 Explication : le protocole dépend de l'équipement et des droits.

3. Régler intervalle, seuils et notifications avant d'augmenter la couverture.
   👉 Explication : on évite les alertes parasites.

4. Vérifier que le pare-feu Windows du serveur n'ouvre que les flux requis :
   ```powershell
   Get-NetFirewallRule -Enabled True -Direction Inbound | Select-Object -First 20 DisplayName
   ```
   👉 Explication : on contrôle les règles entrantes; confronter avec la matrice de ports officielle.

5. Mesurer la charge avant d'ajouter des capteurs WMI, flow ou sniffer.
   👉 Explication : ces capteurs coûtent plus cher en ressources.

## 2. Production — Contrôles

Ne superviser que des actifs appartenant à l'organisation et explicitement autorisés.

## 3. Production — Sécurité

- Ouvrir uniquement les flux requis entre Core/Probe et les appareils sélectionnés.

## Validation et retour arrière

- **Validation** : L'appareil pilote et ses capteurs sont `Up`.
- **Retour arrière** : Supprimer le périphérique pilote dans l'interface Web.

## Si le problème n'est pas résolu

- [Paessler — Exigences système PRTG](https://www.paessler.com/manuals/prtg/system_requirements)
- [Paessler — Installer le Core Server](https://www.paessler.com/manuals/prtg/install_a_prtg_core_server)
- [Guide complet — ajouter un périmètre pilote](../../../../../02-Fiches-Completes/Windows/Server-2022/Installation-Deploiement/47_Deploiement_PRTG_Network_Monitor_Windows_Server.md#4-ajouter-un-perimetre-pilote)
