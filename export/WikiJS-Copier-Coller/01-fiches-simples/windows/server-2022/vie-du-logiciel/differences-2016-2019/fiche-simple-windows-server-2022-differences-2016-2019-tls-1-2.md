# Fiche_Simple_-_Windows_Server_2022_Differences_2016_2019_TLS_1_2

- **Environnement** : Windows Server 2016 et 2019 (comparés à 2022), lab ou serveur de test
- **OS / Version** : Windows Server 2016 / 2019 (référence 2022)
- **Catégorie** : systèmes / différences de versions

---

## Problème précis à résoudre

Vérifier et imposer TLS 1.2 sur 2016 et 2019 (TLS 1.3 n'est pas pris en charge de la même façon que sur 2022).

## 1. Hors-Production (Lab / Test / POC)

1. Lire la configuration Schannel existante :
   ```powershell
   Get-ChildItem 'HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols' -ErrorAction SilentlyContinue
   ```
   👉 Explication : TLS 1.2 est pris en charge par 2016 et 2019 ; l'absence de clés signifie que les valeurs par défaut du système s'appliquent.
2. Désactiver TLS 1.0 côté serveur après test (exemple, sauvegarder le registre avant) :
   ```powershell
   reg export 'HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL' C:\Sauvegarde\schannel.reg
   New-Item 'HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.0\Server' -Force
   New-ItemProperty 'HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.0\Server' -Name Enabled -Value 0 -PropertyType DWord -Force
   ```
   👉 Explication : redémarrer ensuite ; vérifier que les applications .NET anciennes utilisent TLS 1.2 (la documentation Microsoft décrit les paramètres `SchUseStrongCrypto`).
3. Tester depuis un client la négociation TLS 1.2 du service visé (remplacer `HOTE_A_TESTER` par le nom du serveur) :
   ```powershell
   Test-NetConnection -ComputerName HOTE_A_TESTER -Port 443
   ```
   👉 Explication : ce test valide l'ouverture du port ; contrôler le protocole négocié avec un outil de scan TLS approuvé.

## 2. Production — Contrôles

- Tester sur un serveur pilote : certains clients anciens (Windows XP/2003, vieux Java) échouent sans TLS 1.0/1.1.

## 3. Production — Sécurité

- Appliquer les paramètres par GPO plutôt que par saisie manuelle ; ne pas inventer de listes de suites de chiffrement : suivre la documentation Microsoft.

## Validation et retour arrière

- **Validation** : services accessibles uniquement en TLS 1.2 et clients critiques fonctionnels. **Retour arrière** : importer `C:\Sauvegarde\schannel.reg` puis redémarrer.

## Si le problème n'est pas résolu

- [Fiche d'entrée Windows Server 2016 / 2019 / 2022](/01-fiches-simples/logiciels/05-systemes-annuaires-et-services/fiche-logiciel-windows-server-2016-2019-2022)
- [Microsoft Learn — Protocoles TLS/SSL dans Schannel](https://learn.microsoft.com/fr-fr/windows-server/security/tls/tls-ssl-schannel-ssp-overview)
- [Microsoft Learn — Gérer TLS](https://learn.microsoft.com/fr-fr/windows-server/security/tls/manage-tls)