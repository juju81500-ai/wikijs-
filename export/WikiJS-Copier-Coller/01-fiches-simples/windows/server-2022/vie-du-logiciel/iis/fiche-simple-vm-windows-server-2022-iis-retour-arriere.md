# Fiche_Simple_-_VM_Windows_Server_2022_IIS_Retour_Arriere.md

- **Environnement** : VM Windows Server 2022 pilote
- **OS / Version** : Windows Server 2022; rôle Web Server (IIS)
- **Catégorie** : serveur Web / IIS

---

## Problème précis à résoudre

Restaurer la configuration IIS après un changement raté.

## 1. Hors-Production (Lab / Test / POC)

1. Lister les sauvegardes disponibles :
   ```powershell
   & "$env:windir\System32\inetsrv\appcmd.exe" list backup
   ```
   👉 Explication : on identifie l'état à restaurer et on conserve d'abord la configuration actuelle.

2. La restauration remplace la configuration IIS active (`appcmd restore backup NOM_DE_LA_SAUVEGARDE`, nom réel à indiquer); pratiquer d'abord sur une VM isolée et suivre la procédure Microsoft.
   👉 Explication : c'est une action destructive pour la configuration courante.

3. Pour un changement applicatif, remettre la version de contenu précédente et confirmer ACL, bindings, certificat et état du pool.
   👉 Explication : la sauvegarde IIS ne couvre pas le contenu.

## 2. Production — Contrôles

Documenter l'état restauré.

## 3. Production — Sécurité

- Ne pas désinstaller le rôle pour résoudre un incident sans plan de dépendances.

## Validation et retour arrière

- **Validation** : Le site retrouve son comportement antérieur.
- **Retour arrière** : Cette étape est le retour arrière; conserver la configuration exportée avant restauration.

## Si le problème n'est pas résolu

- [Microsoft Learn — documentation IIS](https://learn.microsoft.com/en-us/iis/)
- [Microsoft Learn — AppCmd.exe](https://learn.microsoft.com/en-us/iis/get-started/getting-started-with-iis/getting-started-with-appcmdexe)
- [Guide complet installation IIS Windows Server 2022](/02-fiches-completes/windows/server-2022/installation-deploiement/122-installation-iis-windows-server-2022#6-retour-arriere)