# 📄 Fiche_Simple_-_VM_Windows_Server_Lansweeper_Scan_Pilote.md

- **Environnement** : Lansweeper Classic installé sur un serveur Windows
- **OS / Version** : Windows Server 2022 ou autre version explicitement prise en charge
- **Catégorie** : Inventaire / réseau

---

## 🎯 Problème précis à résoudre

Valider un scan pilote d'actifs appartenant à l'organisation avec une plage restreinte et des comptes de lecture seule.

## 🧪 1. Hors-Production (Lab / Test / POC)

1. Utiliser une plage isolée approuvée avec quelques postes de test :
   ```powershell
   Test-Connection 192.0.2.10 -Count 2
   ```
   👉 Explication : remplacer l'IP; plage de lab seulement.

2. Créer un identifiant de scan dédié, non administrateur de domaine, avec droits de lecture sur les seuls hôtes pilotes :
   ```powershell
   New-LocalUser -Name "svc-lansweeper" -NoPassword
   Add-LocalGroupMember -Group "Administrateurs" -Member "svc-lansweeper"
   ```
   👉 Explication : en lab, sur chaque hôte pilote; en domaine, utiliser un compte de service à droits délégués (GUI **Utilisateurs et ordinateurs Active Directory > Nouveau > Utilisateur**) et définir le mot de passe dans le coffre.

3. Créer la cible : Lansweeper **Scanning > Scanning Targets > Add new scanning target > IP Range**, plage du lab, puis **Scanning > Scanning Credentials > Add new credentials** (type Windows, mappé à la plage).
   👉 Explication : une seule plage de lab.

4. Lancer un scan pilote : **Scanning > Scanning Targets > Scan now**, puis consulter **Scanning > Scanning Status** et la page de chaque actif (erreurs de scan).
   👉 Explication : analyser les erreurs par actif avant de continuer.

## ⚡ 2. Production — Façon Simplifiée

1. Ajouter une plage de production à la fois, avec approbation du propriétaire réseau : **Scanning > Scanning Targets > Add new scanning target**, planification hors heures de pointe : **Scanning > Scanning Targets > Edit > Schedule**.
   👉 Explication : vérifier taux de succès, durée et volume réseau avant d'élargir.

## 🔒 3. Production — Façon Sécurisée

- N'utiliser que des réseaux que l'organisation possède ou est autorisée à inventorier.
- Pour WMI, ouvrir uniquement les flux et règles Windows requis entre le scanner et les cibles prévues; ne pas désactiver le pare-feu Windows.
- Préférer LsAgent lorsqu'il réduit l'exposition entrante ou lorsque les postes sont hors site.
- Employer des comptes de découverte en lecture seule et des credentials SNMPv3 read-only; ne jamais stocker de mot de passe dans une fiche ou un ticket.
- Désactiver/supprimer le compte ou la cible temporaire lorsque le pilote est terminé.

## ✅ Validation et retour arrière

- **Précontrôles** : propriétaire de plage, fenêtre approuvée, identifiants restreints, exclusions définies.
- **Validation** : un petit nombre d'actifs apparaît avec données cohérentes et sans erreur d'autorisation.
- **Retour arrière** : désactiver la cible de scan, retirer la règle firewall ciblée et révoquer les credentials temporaires.

## 🔗 Si le problème n'est pas résolu

- **Fiche de résolution complémentaire** : [[Windows_Lansweeper_Scan_WMI_Echec]]
- [Lansweeper Classic — Prérequis scan Windows domaine](https://docs.lansweeper.com/classic/docs/windows-domain-scanning-requirements.md)
- [Lansweeper Classic — Identifiants de scan](https://docs.lansweeper.com/classic/docs/create-and-map-scanning-credentials.md)