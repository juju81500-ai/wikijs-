# 📄 VM_WinSrv_2022_GPO_Forcer-Et-Auditer-Mise-A-Jour-GPUpdate.md

- **Environnement** : VM / Poste de travail / Serveur Active Directory
- **OS / Version** : Windows Server 2022 / Windows 11 / Windows 10
- **Catégorie** : Active Directory / GPO

---

## 🎯 Problème précis à résoudre
Forcer l'application immédiate des stratégies de groupe Active Directory (GPO) sur une machine sans attendre le délai de rafraîchissement automatique (90 min), et générer un rapport d'audit d'application des GPO.

---

## 🖥️ Actualiser et auditer les GPO

### Actualiser localement (CMD)
1. Sur le poste cible, ouvrir **Terminal** ou **Invite de commandes**. Exécuter :
   ```cmd
   gpupdate /force
   ```
   👉 Explication : relance le traitement local des stratégies; accepter une fermeture de session ou un redémarrage uniquement si Windows le demande.
2. Attendre la fin de la commande et lire les messages de réussite/échec. Cette commande relance le traitement local des stratégies ; elle ne garantit pas que les paramètres attendus aient été appliqués.

### Déclencher une actualisation distante (GPMC)
1. Sur un poste d'administration avec GPMC/RSAT, ouvrir **Gestionnaire de stratégie de groupe** (`gpmc.msc`).
2. Sélectionner l'OU qui contient les ordinateurs de test, clic droit > **Mise à jour de stratégie de groupe...**, vérifier le nombre de machines ciblées et confirmer.
3. Utiliser cette action uniquement sur le périmètre prévu. Les postes doivent être joignables et les règles de pare-feu/planification distante nécessaires doivent être disponibles ; en cas d'échec, lancer `gpupdate /force` localement ou diagnostiquer la connectivité.

### Vérifier le résultat dans GPMC
1. Dans GPMC, clic droit sur **Résultats de stratégie de groupe** > **Assistant Résultats de stratégie de groupe**.
2. Choisir l'ordinateur et, si nécessaire, l'utilisateur ciblé ; terminer l'assistant et vérifier **GPO appliquées**, **GPO refusées** et les raisons de filtrage.
3. Pour conserver un rapport, utiliser **Enregistrer le rapport**. En alternative CMD, ```cmd
   gpresult /h C:\Rapport_GPO.html /f
   ```
   👉 Explication : produit un rapport local (`/f` écrase l'ancien) ; ouvrir le fichier avec un navigateur disposant des droits de lecture.

Le rafraîchissement forcé ne corrige ni un mauvais lien GPO, ni un filtre de sécurité, ni une erreur de réplication AD/SYSVOL. Diagnostiquer ces causes avant de répéter l'opération.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. **Actualisation des GPO à distance sur une machine cliente via PowerShell** :
   ```powershell
   Invoke-GPUpdate -Computer "PC-TSSR-01" -Force
   ```
   👉 *Explication : Tu déclenches la mise à jour des GPO à distance sur le poste client sans quitter ton serveur.*