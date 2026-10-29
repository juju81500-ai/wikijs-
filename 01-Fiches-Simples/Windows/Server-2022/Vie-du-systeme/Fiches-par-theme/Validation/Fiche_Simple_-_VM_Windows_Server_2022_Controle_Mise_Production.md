# 📄 Fiche_Simple_-_VM_Windows_Server_2022_Controle_Mise_Production.md

- **Environnement** : Serveur Windows Server membre, autonome ou contrôleur de domaine
- **OS / Version** : Windows Server 2022
- **Catégorie** : Production / Validation / Exploitation
- **Tags** : `[windows-server-2022]`, `[production]`, `[validation]`, `[sauvegarde]`, `[roles]`, `[securite]`

## 🎯 Problème précis à résoudre
Effectuer la recette d'un serveur Windows Server 2022 avant mise en production : rôle, réseau, accès, pare-feu, journaux, supervision, sauvegarde et reprise.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Relever édition/build et rôles : GUI **Gestionnaire de serveur > Tableau de bord**, ou :
   ```powershell
   Get-ComputerInfo | Select-Object WindowsProductName, WindowsVersion, OsBuildNumber
   Get-WindowsFeature | Where-Object Installed
   Get-Service | Where-Object Status -eq 'Stopped'
   ```
   👉 Explication : seuls les rôles requis sont installés; vérifier les services arrêtés qui devraient tourner.

2. Pare-feu et journaux : GUI **Pare-feu Windows Defender avec fonctions avancées** et **Observateur d'événements**, ou :
   ```powershell
   Get-NetFirewallProfile | Select-Object Name, Enabled, DefaultInboundAction
   Get-WinEvent -LogName System -MaxEvents 20
   ```
   👉 Explication : profils actifs, entrée bloquée par défaut; relever les erreurs récentes.

3. Tester le service depuis un client autorisé et restaurer une sauvegarde dans une VM isolée :
   ```powershell
   Test-NetConnection IP_SERVEUR -Port PORT
   wbadmin get versions
   ```
   👉 Explication : remplacer IP et port; `wbadmin get versions` liste les sauvegardes Windows Server Backup disponibles.


## ⚡ 2. Production — Façon Simplifiée
1. **Système et réseau :** hostname/IP/DNS/heure validés, correctifs appliqués, redémarrage effectué et compte d'administration contrôlé.
2. **Rôle :** seuls les rôles et fonctionnalités requis sont installés; services, ports, dépendances et tests fonctionnels correspondent au dossier d'exploitation.
3. **Sécurité :** GPO/baseline appliquée, pare-feu actif, RDP limité aux réseaux d'administration, journaux collectés et secrets protégés.
4. **Continuité :** Windows Server Backup ou solution agréée configurée sur une cible distincte; version récente vérifiée et exercice de restauration réalisé.
5. **Si contrôleur de domaine :** vérifier santé et réplication AD DS/DNS; exécuter les contrôles d'annuaire prévus et suivre le runbook de restauration forêt.
6. **Bascule :** responsable, fenêtre, dépendances, critères d'acceptation et retour arrière consignés.
   👉 *Explication : une sauvegarde réussie n'est pas une preuve de reprise; réaliser l'exercice sur une VM isolée sans réintroduire le serveur restauré sur le réseau de production.*

## 🔒 3. Production — Façon Sécurisée
- Refuser l'ouverture si un rôle requis est en échec, si la sauvegarde est stockée uniquement sur le serveur ou si son accès n'est pas contrôlé.
- Pour AD DS, ne jamais improviser une restauration autoritaire; distinguer restauration non autoritaire, autoritaire et récupération de forêt.
- Vérifier les comptes, délégations, règles entrantes, certificats et chemins de journalisation spécifiques aux rôles installés.

## ✅ Validation et retour arrière
- Tester chaque fonction métier depuis une machine cliente et confirmer journaux, supervision et sauvegarde.
- Vérifier la restauration d'un échantillon ou d'une VM complète selon le rôle avant la bascule.
- En cas d'échec, arrêter la bascule, conserver les preuves et restaurer l'ancien serveur ou la sauvegarde selon le runbook validé.