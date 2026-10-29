# Fiche_Simple_-_VM_Windows_Server_2022_IIS_Verifier_Service_Site.md

- **Environnement** : VM Windows Server 2022 pilote
- **OS / Version** : Windows Server 2022; rôle Web Server (IIS)
- **Catégorie** : serveur Web / IIS

---

## Problème précis à résoudre

Contrôler que le service, le site et le pool fonctionnent.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler service, site et pool, puis tester la page :
   ```powershell
   Get-Service W3SVC
   & "$env:windir\System32\inetsrv\appcmd.exe" list site
   & "$env:windir\System32\inetsrv\appcmd.exe" list apppool 'Pilote'
   Invoke-WebRequest -Uri 'http://localhost/' -UseBasicParsing
   ```
   👉 Explication : le service doit être `Running` et la requête renvoyer le code 200.

2. GUI : **IIS Manager > Sites** et **Pools d'applications** pour vérifier l'état démarré.
   👉 Explication : vue graphique équivalente.

3. Consulter les journaux IIS dans `%SystemDrive%\inetpub\logs\LogFiles`.
   👉 Explication : on confirme la requête de test; en environnement cible, tester le nom DNS et le certificat depuis un poste client approuvé.

## 2. Production — Contrôles

Contrôler identité et état du pool.

## 3. Production — Sécurité

- Protéger les journaux et fixer leur rétention.

## Validation et retour arrière

- **Validation** : Code 200, pool démarré, journaux alimentés.
- **Retour arrière** : Arrêter le site depuis IIS Manager si le comportement est anormal.

## Si le problème n'est pas résolu

- [Microsoft Learn — documentation IIS](https://learn.microsoft.com/en-us/iis/)
- [Microsoft Learn — AppCmd.exe](https://learn.microsoft.com/en-us/iis/get-started/getting-started-with-iis/getting-started-with-appcmdexe)
- [Guide complet installation IIS Windows Server 2022](/02-fiches-completes/windows/server-2022/installation-deploiement/122-installation-iis-windows-server-2022#4-verifier-le-service-et-le-site)