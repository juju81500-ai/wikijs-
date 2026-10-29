# Fiche_Simple_-_Windows_Server_2022_Differences_2016_2019_Windows_Admin_Center

- **Environnement** : Windows Server 2016 et 2019 (comparés à 2022), lab ou serveur de test
- **OS / Version** : Windows Server 2016 / 2019 (référence 2022)
- **Catégorie** : systèmes / différences de versions

---

## Problème précis à résoudre

Administrer des serveurs 2016 et 2019 avec Windows Admin Center (WAC) depuis une passerelle.

## 1. Hors-Production (Lab / Test / POC)

1. Télécharger Windows Admin Center depuis la page officielle Microsoft et noter la version publiée.
   👉 Explication : la compatibilité des versions cibles (2016, 2019) est indiquée dans la documentation WAC ; vérifier la version publiée.
2. Installer la passerelle sur un serveur ou un poste d'administration (GUI : lancer le MSI, choisir le port HTTPS et un certificat de confiance). Équivalent en ligne de commande (remplacer `CHEMIN_MSI`) :
   ```powershell
   Start-Process msiexec.exe -ArgumentList '/i CHEMIN_MSI /qn /L*v C:\Sauvegarde\wac-install.log SME_PORT=443 SSL_CERTIFICATE_OPTION=generate' -Wait
   ```
   👉 Explication : `generate` crée un certificat auto-signé de test ; en production, utiliser un certificat d'une autorité interne.
3. Ajouter un serveur 2016/2019 : ouvrir l'URL de la passerelle, **Ajouter > Serveurs**, saisir le nom.
   👉 Explication : WAC s'appuie sur WinRM et PowerShell 5.1 des cibles ; activer WinRM si besoin : `Enable-PSRemoting -Force` sur la cible.

## 2. Production — Contrôles

- Limiter l'accès à la passerelle à un groupe d'administrateurs et aux postes d'administration.

## 3. Production — Sécurité

- Utiliser un certificat valide, HTTPS uniquement, et déléguer par groupes AD plutôt que par comptes locaux.

## Validation et retour arrière

- **Validation** : la console liste le serveur cible, ses rôles et ses compteurs. **Retour arrière** : désinstaller WAC via **Paramètres > Applications**; les serveurs cibles ne sont pas modifiés.

## Si le problème n'est pas résolu

- [Fiche d'entrée Windows Server 2016 / 2019 / 2022](/01-fiches-simples/logiciels/05-systemes-annuaires-et-services/fiche-logiciel-windows-server-2016-2019-2022)
- [Microsoft Learn — Windows Admin Center](https://learn.microsoft.com/fr-fr/windows-server/manage/windows-admin-center/overview)
- [Microsoft Learn — Installer Windows Admin Center](https://learn.microsoft.com/fr-fr/windows-server/manage/windows-admin-center/deploy/install)