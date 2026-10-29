---
title: "Fiche Simple - VM Windows Server 2022 RDS Activer Bureau a Dist"
description: "Activer l'accès Bureau à distance sur un serveur pilote uniquement après approbation, conserver NLA et limiter les flux au réseau d'administration."
published: true
date: 2026-10-29T20:41:47Z
tags: ["windows-server-2022", "rds", "rdp", "nla", "powershell"]
editor: markdown
dateCreated: 2026-10-29T20:41:47Z
dateModified: 2026-10-29T20:41:47Z
---

# Fiche_Simple_-_VM_Windows_Server_2022_RDS_Activer_Bureau_a_Dist

- **Environnement** : VM ou serveur pilote Windows Server 2022 avec accès console
- **OS / Version** : Windows Server 2022 Desktop Experience
- **Catégorie** : Vie du logiciel / Activation RDP
- **Tags** : `windows-server-2022`, `rds`, `rdp`, `nla`, `powershell`

---

## Problème précis à résoudre

Activer l'accès Bureau à distance sur un serveur pilote uniquement après approbation, conserver NLA et limiter les flux au réseau d'administration.

## 1. Hors-Production (Lab / Test / POC)

1. Dans **Gestionnaire de serveur** > **Serveur local** > **Bureau à distance**, ouvrir **Propriétés système** > **Utilisation à distance**; sélectionner **Autoriser les connexions à distance** et conserver l'exigence NLA.
   👉 Explication : Active RDP sur le serveur pilote et impose l'authentification réseau avant l'ouverture de session.
2. Équivalent PowerShell, dans une console administrateur :
   ```powershell
   Set-ItemProperty -Path 'HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server' -Name fDenyTSConnections -Value 0
   Set-ItemProperty -Path 'HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp' -Name UserAuthentication -Value 1
   ```
   👉 Explication : Autorise les connexions et impose NLA. Utiliser uniquement sur le serveur approuvé et prévoir un accès console.
3. Dans `wf.msc` > **Règles de trafic entrant**, activer les règles Bureau à distance uniquement sur les profils Domain/Private requis; dans **Étendue**, limiter les adresses distantes au réseau d'administration de lab.
   👉 Explication : Le profil et le sous-réseau sont à remplacer par le périmètre réellement autorisé; ne pas autoriser le profil Public par défaut.
4. Depuis un poste pilote, lancer `mstsc`, saisir le nom DNS approuvé et tester un compte utilisateur autorisé.
   👉 Explication : Confirme le chemin client et l'authentification NLA; le simple test du port ne valide pas l'accès utilisateur.

## 2. Production — Contrôles

- Valider l'usage métier, les groupes autorisés, les règles réseau, le certificat et la stratégie de journalisation.
- Préférer un VPN ou RD Gateway approuvée; ne pas exposer TCP/UDP 3389 directement à Internet.
- Confirmer l'édition serveur et les exigences de licence RDS si des sessions multi-utilisateurs sont prévues.

## 3. Production — Sécurité

- Ne pas désactiver NLA pour contourner une erreur client sans analyse de risque.
- Limiter l'accès aux profils attendus et au réseau de gestion; éviter les règles étendues à tous les profils et toutes les adresses.
- Changer le port RDP n'est pas une mesure de sécurité suffisante et ne remplace ni VPN/RD Gateway ni filtrage réseau.

## Validation et retour arrière

- **Validation** : connexion pilote autorisée fonctionne, NLA est actif, accès hors périmètre est bloqué.
- **Retour arrière** : désactiver **Bureau à distance** dans **Gestionnaire de serveur** > **Serveur local**, ou exécuter `Set-ItemProperty -Path 'HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server' -Name fDenyTSConnections -Value 1`; désactiver ensuite les règles entrantes activées par ce changement.

## Si le problème n'est pas résolu

- [Microsoft Learn — Autoriser l'accès au Bureau à distance](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/remotepc/remote-desktop-allow-access)
- [Prérequis et limites RDS](/01-fiches-simples/windows/server-2022/vie-du-logiciel/remote-desktop-services/fiche-simple-windows-server-2022-rds-prerequis-limites)
- [Sécuriser les accès RDS](/01-fiches-simples/windows/server-2022/vie-du-logiciel/remote-desktop-services/fiche-simple-windows-server-2022-rds-securiser-acces)