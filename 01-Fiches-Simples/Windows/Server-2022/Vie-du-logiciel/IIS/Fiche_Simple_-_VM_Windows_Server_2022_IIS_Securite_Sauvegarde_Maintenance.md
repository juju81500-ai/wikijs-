# Fiche_Simple_-_VM_Windows_Server_2022_IIS_Securite_Sauvegarde_Maintenance.md

- **Environnement** : VM Windows Server 2022 pilote
- **OS / Version** : Windows Server 2022; rôle Web Server (IIS)
- **Catégorie** : serveur Web / IIS
- **Tags** : `iis`, `windows-server-2022`, `web-server`, `tls`, `application-pool`

---

## Problème précis à résoudre

Appliquer les contrôles de sécurité et sauvegarder la configuration IIS.

## 1. Hors-Production (Lab / Test / POC)

1. Dans **Pare-feu Windows Defender avec fonctions avancées > Règles de trafic entrant**, n'autoriser que les ports et sources nécessaires, avec profil et périmètre explicites.
   👉 Explication : toute règle entrante doit être délimitée.

2. Utiliser HTTPS avec un certificat valide; ne désactiver le binding HTTP qu'après validation complète de HTTPS et des dépendances.
   👉 Explication : on évite de couper un accès encore utilisé.

3. Retirer les modules inutiles, limiter les méthodes HTTP et les permissions, désactiver l'indexation de répertoire et ne placer aucun secret dans le contenu Web.
   👉 Explication : on réduit la surface d'attaque.

4. Créer une sauvegarde IIS avant changement :
   ```powershell
   & "$env:windir\System32\inetsrv\appcmd.exe" add backup 'AvantChangement'
   ```
   👉 Explication : la sauvegarde couvre la configuration IIS, pas le contenu du site, les certificats privés ni les bases de données; les sauvegarder séparément.

## 2. Production — Contrôles

Surveiller erreurs, espace disque et état des pools.

## 3. Production — Sécurité

- Pare-feu restrictif, HTTPS, modules minimaux, aucun secret dans le contenu.

## Validation et retour arrière

- **Validation** : Sauvegarde `AvantChangement` présente (`appcmd list backup`).
- **Retour arrière** : Voir l'étape 6 pour restaurer.

## Si le problème n'est pas résolu

- [Microsoft Learn — documentation IIS](https://learn.microsoft.com/en-us/iis/)
- [Microsoft Learn — AppCmd.exe](https://learn.microsoft.com/en-us/iis/get-started/getting-started-with-iis/getting-started-with-appcmdexe)
- [Guide complet installation IIS Windows Server 2022](../../../../../02-Fiches-Completes/Windows/Server-2022/Installation-Deploiement/122_Installation_IIS_Windows_Server_2022.md#5-securite-sauvegarde-et-maintenance)
