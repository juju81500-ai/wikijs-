# 📄 Fiche_Simple_-_VM_Ubuntu_24.04_Securite_Diagnostic_AppArmor.md

- **Environnement** : VM Ubuntu Server
- **OS / Version** : Ubuntu Server 24.04 LTS
- **Catégorie** : Sécurité / Contrôle d'accès
- **Tags** : `[ubuntu24.04]`, `[ubuntu]`, `[apparmor]`, `[securite]`, `[audit]`, `[hardening]`

## 🎯 Problème précis à résoudre
Identifier un refus AppArmor affectant une application Ubuntu et corriger le profil de façon ciblée sans désactiver le contrôle.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Relever l'état d'AppArmor et les profils chargés :
   ```bash
   sudo aa-status
   ```
2. Filtrer les refus noyau récents :
   ```bash
   sudo journalctl -k --since today --no-pager | grep -i 'apparmor.*denied'
   ```
   👉 *Explication : rapprocher chaque refus du nom du profil, du chemin visé et de l'action demandée par l'application.*

## ⚡ 2. Production — Façon Simplifiée
1. Sauvegarder le profil identifié sous `/etc/apparmor.d/` et vérifier que le refus est reproductible.
2. Lancer l'outil d'aide à la mise à jour et examiner chaque règle proposée :
   ```bash
   sudo aa-logprof
   ```
3. Recharger le profil modifié et vérifier qu'il reste en mode enforce :
   ```bash
   sudo apparmor_parser -r /etc/apparmor.d/<profil-identifie>
   sudo aa-status
   ```
   👉 *Explication : adapter le chemin au profil concerné; `aa-logprof` peut élargir les accès et exige une revue humaine.*

## 🔒 3. Production — Façon Sécurisée
1. Ne pas désactiver AppArmor, ni laisser durablement un profil en mode complain.
2. Autoriser seulement les chemins et opérations nécessaires; éviter les accès globaux ou récursifs inutiles.
3. Tester la mise à jour sur un système de préproduction avant de la déployer à plusieurs serveurs.

## ✅ Validation et retour arrière
- Reproduire l'action qui échouait, vérifier les journaux noyau et confirmer le mode `enforce` avec `aa-status`.
- Si l'application est dégradée, restaurer le profil sauvegardé, recharger le profil puis vérifier le service.
- Examiner de nouveau les refus AppArmor après la correction.