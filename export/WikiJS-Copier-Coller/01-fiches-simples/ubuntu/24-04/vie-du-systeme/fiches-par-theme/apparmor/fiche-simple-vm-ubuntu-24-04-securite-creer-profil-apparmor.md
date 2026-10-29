# 📄 Fiche_Simple_-_VM_Ubuntu_24.04_Securite_Creer_Profil_AppArmor.md

- **Environnement** : VM Ubuntu Server exécutant une application personnalisée
- **OS / Version** : Ubuntu Server 24.04 LTS avec AppArmor
- **Catégorie** : Sécurité / Contrôle d'accès

## 🎯 Problème précis à résoudre
Générer puis resserrer un profil AppArmor pour une application locale afin de limiter ses accès aux seuls fichiers et opérations nécessaires.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Vérifier l'état d'AppArmor et que l'exécutable existe :
   ```bash
   sudo aa-status
   test -x /usr/local/bin/monapp
   ```
2. Démarrer l'assistant de profilage en laboratoire :
   ```bash
   sudo aa-genprof /usr/local/bin/monapp
   ```
   Pendant l'analyse, exécuter les parcours applicatifs représentatifs dans un jeu de données de test et examiner chaque accès proposé.
3. Examiner puis charger le profil généré :
   ```bash
   sudo aa-status
   sudo apparmor_parser -r /etc/apparmor.d/usr.local.bin.monapp
   ```
   👉 *Explication : le chemin et le nom du profil dépendent de l'exécutable; confirmer le fichier effectivement créé avant de le charger.*

## ⚡ 2. Production — Façon Simplifiée
1. Copier le profil généré dans une revue de changement; supprimer les accès aux chemins et opérations non justifiés.
2. Tester le profil en préproduction avec les tâches nominales, démarrage, rotation de journaux et mises à jour de l'application.
3. Passer le profil en mode enforce et confirmer qu'il est chargé :
   ```bash
   sudo aa-enforce /etc/apparmor.d/usr.local.bin.monapp
   sudo aa-status
   sudo journalctl -k --since today --no-pager | grep -i 'apparmor.*denied'
   ```
   👉 *Explication : compléter le test fonctionnel après passage en enforce; les parcours non testés peuvent révéler de nouveaux refus.*

## 🔒 3. Production — Façon Sécurisée
1. Ne pas accepter les règles proposées automatiquement sans examen; les accès larges peuvent neutraliser l'intérêt du profil.
2. Ne pas laisser l'application en mode complain ou désactiver AppArmor pour contourner un refus.
3. Garder une copie de la version précédente et déployer progressivement avant une généralisation.

## ✅ Validation et retour arrière
- Vérifier `aa-status`, le fonctionnement métier et l'absence de refus inattendus après un cycle complet d'utilisation.
- Pour revenir en arrière, restaurer le profil validé précédemment, le recharger avec `apparmor_parser -r`, puis contrôler le statut.
- Documenter les chemins et opérations explicitement autorisés.