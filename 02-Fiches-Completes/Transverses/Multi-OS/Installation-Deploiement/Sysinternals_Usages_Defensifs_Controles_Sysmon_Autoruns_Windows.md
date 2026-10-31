# Sysinternals : usages défensifs contrôlés (Sysmon, Autoruns, Sigcheck) sur Windows

- **OS / Version** : Windows 10/11 et Windows Server en environnement géré (Sysmon : Windows uniquement)
- **Type de fiche** : Installation/Déploiement
- **Périmètre** : Usages qui modifient l'état du système : installation de Sysmon, durcissement et audit de persistance, exports pour investigation
- **Catégorie** : Supervision / détection
- **Tags** : `sysinternals`,`sysmon`,`autoruns`,`sigcheck`,`windows`,`blue-team`

## 1. Portée, hypothèses et licences

- Complète la fiche [Administration Microsoft Sysinternals Windows 11](../../../Windows/Client-11/Installation-Deploiement/123_Administration_Microsoft_Sysinternals_Windows_11.md), qui reste la référence du diagnostic sur poste. Ici : outils qui **installent un pilote/service** (Sysmon) ou **peuvent changer la configuration** (Autoruns).
- Usage strictement défensif. Toute action décrite ici s'exécute uniquement sur des systèmes que vous possédez ou pour lesquels vous disposez d'une autorisation écrite (périmètre, dates, contacts). Ne pas utiliser ces outils pour contourner des protections ni pour collecter des données de tiers.
- Les outils Sysinternals sont gratuits mais soumis au contrat de licence Microsoft Sysinternals Software License Terms ; l'acceptation s'exprime par `-accepteula` ou en interface. Vérifier les conditions pour un usage commercial/redistribution.
- Hypothèses : droits administrateur local, poste ou VM pilote validé, point de restauration/snapshot disponible, SIEM ou collecte d'événements défini.

## 2. Prérequis

- Téléchargement depuis le site officiel Microsoft Learn (Sysinternals Suite) ; contrôle de la signature Authenticode avant déploiement.
- Un dossier protégé en écriture (ex. `C:\Tools\Sysinternals`) réservé aux administrateurs.
- Une configuration Sysmon relue et versionnée (fichier XML). Ne pas appliquer une configuration publique sans la lire : elle peut générer un volume important ou exclure des événements utiles.
- Taille du journal `Microsoft-Windows-Sysmon/Operational` dimensionnée et destination de collecte validée.

## 3. Vérifier l'intégrité des binaires

```powershell
Get-AuthenticodeSignature C:\Tools\Sysinternals\sysmon64.exe | Format-List Status,SignerCertificate
.\sigcheck64.exe -accepteula -nobanner C:\Tools\Sysinternals\sysmon64.exe
```

Le statut doit être `Valid` avec Microsoft comme éditeur.

## 4. Installer Sysmon sur la machine pilote

1. Sauvegarder un point de restauration ou un snapshot de VM.
2. Installer avec la configuration relue :

```powershell
C:\Tools\Sysinternals\sysmon64.exe -accepteula -i C:\Tools\sysmon-config.xml
```

3. Vérifier le service et le pilote :

```powershell
Get-Service Sysmon64
Get-WinEvent -LogName "Microsoft-Windows-Sysmon/Operational" -MaxEvents 5
```

4. Pour modifier la configuration sans réinstaller : `sysmon64.exe -c C:\Tools\sysmon-config-v2.xml` ; afficher la configuration active avec `sysmon64.exe -c`.
5. Déploiement à l'échelle : par GPO, outil de gestion de configuration ou MDM, par vagues, après validation sur le pilote. Mettre à jour Sysmon explicitement (nouveau binaire) selon la procédure Microsoft.

## 5. Auditer la persistance avec Autoruns

- Interface graphique : ouvrir Autoruns en administrateur, activer « Verify Code Signatures » et « Hide Microsoft Entries » pour isoler les écarts.
- Export en ligne de commande pour comparaison avec une référence :

```powershell
.\autorunsc64.exe -accepteula -a * -c -h -s > autoruns_reference.csv
```

- Comparer l'export à la référence validée d'une image saine. Ne **pas** désactiver ou supprimer une entrée en production sans ticket : décocher une entrée dans Autoruns modifie le démarrage. Documenter l'état initial avant toute action.

## 6. Validation

- Le service Sysmon est `Running` et des événements ID 1 (création de processus) apparaissent après le lancement d'un programme de test inoffensif (`notepad.exe`).
- La configuration active correspond au fichier versionné (hash identique).
- La collecte centrale reçoit les événements ; le volume par poste reste dans l'enveloppe prévue.
- L'export Autoruns se compare à la référence, les écarts sont expliqués.
- Les performances du poste pilote ne sont pas dégradées de façon visible.

## 7. Retour arrière

```powershell
C:\Tools\Sysinternals\sysmon64.exe -u
```

Cette commande désinstalle Sysmon (service et pilote) ; ajouter l'option `force` seulement après lecture de l'aide (`sysmon64.exe -?`). Restaurer ensuite le snapshot si un comportement anormal subsiste, restaurer les entrées de démarrage modifiées avec Autoruns à partir de l'état documenté, et conserver les journaux d'audit. Ne pas supprimer manuellement le pilote ou les clés de registre.

## Sources officielles

- [Sysinternals — Microsoft Learn](https://learn.microsoft.com/sysinternals/)
- [Sysmon](https://learn.microsoft.com/sysinternals/downloads/sysmon)
- [Autoruns](https://learn.microsoft.com/sysinternals/downloads/autoruns)
- [Sigcheck](https://learn.microsoft.com/sysinternals/downloads/sigcheck)

Aucune installation de Sysmon n'a été exécutée pendant la rédaction ; vérifier les options avec l'aide de la version téléchargée.

## Historique

| Date | Version | Changement | Statut de test |
|---|---|---|---|
| 2026-10-31 | 1.0 | Création de la fiche à partir de la documentation éditeur | Non testé sur plateforme cible |
