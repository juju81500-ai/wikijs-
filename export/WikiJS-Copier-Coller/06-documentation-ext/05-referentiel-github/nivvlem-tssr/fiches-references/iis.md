# IIS (Internet Information Services)

## 📌 Présentation

IIS est le serveur web développé par Microsoft, intégré à Windows Server. Il permet d’héberger des sites web, des applications ASP.NET, des API ou des services intranet, avec gestion fine des protocoles (HTTP, HTTPS, FTP, etc.). Il est administrable via l’interface graphique, PowerShell ou Web Platform Installer.

---

## 🧰 Commandes PowerShell utiles

| Cmdlet / Commande                   | Description                      | Exemple                                                                                                   |
| ----------------------------------- | -------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `Install-WindowsFeature Web-Server` | Installe IIS                     | `Install-WindowsFeature Web-Server`                                                                       |
| `Get-WindowsFeature`                | Liste les rôles installables     | `Get-WindowsFeature *web*`                                                                                |
| `iisreset`                          | Redémarre le service IIS         | `iisreset`                                                                                                |
| `Import-Module WebAdministration`   | Importe le module de gestion IIS | `Import-Module WebAdministration`                                                                         |
| `Get-Website`                       | Liste les sites                  | `Get-Website`                                                                                             |
| `New-Website`                       | Crée un site web                 | `New-Website -Name "Site1" -Port 80 -PhysicalPath 'C:\inetpub\site1' -ApplicationPool "DefaultAppPool"`   |
| `Remove-Website`                    | Supprime un site                 | `Remove-Website -Name "Site1"`                                                                            |
| `Set-ItemProperty`                  | Modifie une propriété IIS        | `Set-ItemProperty IIS:\Sites\Site1 -Name bindings -Value @{protocol='http';bindingInformation='*:8080:'}` |

---

## 📁 Répertoires et outils

- 📁 `C:\inetpub\wwwroot\` : racine web par défaut
- 🔧 `IIS Manager` : interface graphique (GUI) pour créer des sites, configurer SSL, gérer les pools d’application
- 🧱 Application Pools : permettent d’isoler les sites (mémoire/processus)
- 🔒 Gestion SSL : possible via l’onglet « Bindings » (HTTPS)

---

## 🔎 Cas d’usage courant

- Hébergement de sites intranet en entreprise
- Déploiement d’applications ASP.NET ou API REST
- Configuration de bindings HTTP/HTTPS spécifiques par IP ou nom de domaine
- Mise en place de redirections, authentification Windows, quotas FTP

---

## ⚠️ Erreurs fréquentes

- Oublier d’installer les rôles nécessaires : `Web-Mgmt-Tools`, `Web-Common-Http`, etc.
- Mauvais `binding` (port déjà utilisé ou nom DNS mal configuré)
- Site en arrêt sans cause apparente → vérifier les journaux ou l’état du pool d’application
- Permissions NTFS incorrectes sur le répertoire du site

---

## ✅ Bonnes pratiques

- Donner uniquement les droits nécessaires à `IIS_IUSRS` ou à un utilisateur applicatif dédié
- Créer un pool d’application par site critique pour isoler les pannes
- Toujours nommer clairement les sites et dossiers (`intranet`, `support`, etc.)
- Activer les logs IIS pour diagnostiquer les erreurs (ex : erreurs 500 ou 403)
- Sauvegarder les configurations via export (commande ou interface)

---

## 📚 Ressources complémentaires

- [Microsoft Learn – IIS](https://learn.microsoft.com/fr-fr/iis/)
- [Module PowerShell WebAdministration](https://learn.microsoft.com/en-us/powershell/module/webadministration/)
- `iisreset /?`, `Get-Help WebAdministration`