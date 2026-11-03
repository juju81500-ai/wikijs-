---
title: "Leçon — Durcissement de Windows"
description: "À la fin de cette leçon, vous saurez :"
published: true
date: 2026-11-03T14:22:28Z
tags: ["transverse", "tout-en-un", "lecon", "securite", "durcissement", "windows", "defender", "gpo", "bitlocker", "laps"]
editor: markdown
dateCreated: 2026-11-03T14:22:28Z
dateModified: 2026-11-03T14:22:28Z
---

# Leçon — Durcissement de Windows

- **Tags** : `transverse`, `tout-en-un`, `lecon`, `securite`, `durcissement`, `windows`, `defender`, `gpo`, `bitlocker`, `laps`
- **Niveau** : intermédiaire
- **Durée estimée** : 3 h 30 (lecture 1 h 15, laboratoire 1 h 45, exercices et quiz 30 min)

---

## Objectifs pédagogiques

À la fin de cette leçon, vous saurez :

1. contrôler l'état de **Microsoft Defender** et des **correctifs** avec PowerShell, en lecture seule ;
2. auditer les **comptes locaux** et expliquer le **principe de [[Glossary:LAPS]]** ;
3. décrire l'ordre d'application des **stratégies de groupe ([[Glossary:GPO]])** et vérifier le résultat ;
4. expliquer le **principe de BitLocker** et ses précautions de récupération ;
5. lire les **journaux de sécurité** et repérer les événements importants ;
6. détecter et encadrer l'exposition de **SMB** et **[[Glossary:RDP]]** ;
7. conduire chaque changement avec : **snapshot → console de secours → test → retour arrière**.

## Prérequis et durée

- Administration Windows de base : PowerShell, services, utilisateurs et groupes.
- Laboratoire : une **[[Glossary:VM]] jetable** Windows Server (évaluation) ou Windows 11, avec **snapshot** et **console de l'hyperviseur** ; idéalement un contrôleur de domaine de test `example.test` pour GPO et LAPS. Adresses de documentation : `192.0.2.0/24`, `198.51.100.0/24`.
- PowerShell **en administrateur** pour les contrôles des sections 7 à 10.
- Durée : environ 3 h 30.

> ⚠️ **Périmètre.** Ne durcissez que des machines dont vous êtes responsable. Une GPO mal pensée s'applique à des centaines de postes en quelques minutes : testez sur une [[Glossary:OU]] pilote.

## L'essentiel en bref

- Windows se durcit **en couches** : données, hôte, comptes, réseau, supervision. Aucune couche ne suffit seule.
- **Defender** et les **correctifs** sont la base ; on les **vérifie** (état, dates, exclusions), on ne présume pas.
- **LAPS** donne à chaque machine un mot de passe administrateur local **unique et renouvelé**.
- Les **GPO** appliquent la configuration à grande échelle, dans l'ordre **local → site → domaine → OU**.
- **BitLocker** protège les données au repos, à condition que la **clé de récupération** soit sauvegardée *avant* d'activer.
- **SMB (445)** et **RDP (3389)** ne sont jamais exposés directement à Internet.
- Tout changement : **snapshot, console de secours, test, retour arrière**.

---

## 1. La défense en couches

**Analogie.** Un château ne repose pas sur un seul mur : douves, muraille, gardes, coffre-fort, registre des visiteurs. Si une couche cède, la suivante limite les dégâts.

![Schéma original de la défense en couches Windows : BitLocker pour les données, Defender et correctifs pour l'hôte, LAPS pour les comptes, pare-feu pour le réseau, journaux de sécurité pour la supervision](images/durcissement-windows-1.svg)

*Figure 1 — Cinq couches complémentaires pour un poste ou un serveur Windows. Création originale Pack Master (CC0).*

| Couche | Risque traité | Outil |
|---|---|---|
| Données | vol du disque ou de la machine | BitLocker |
| Hôte | logiciel malveillant, faille connue | Defender, Windows Update |
| Comptes | rebond avec un mot de passe local identique | LAPS, moindre privilège |
| Réseau | accès distant non voulu | Pare-feu, limitation SMB/RDP |
| Supervision | attaque non détectée | journal Sécurité |

---

## 2. La règle d'or du changement

Sous Windows aussi, la faute classique est de **s'enfermer dehors** (règle de pare-feu, RDP désactivé, GPO trop stricte).

1. **Snapshot préalable** : point de contrôle de l'hyperviseur (ou sauvegarde, point de restauration, export de la GPO avec `Backup-GPO`).
2. **Accès console de secours** : console de l'hyperviseur, iLO/iDRAC, ou environnement de récupération Windows. Il doit marcher sans réseau.
3. **Changement** limité à un seul paramètre à la fois, sur une machine ou une OU pilote.
4. **Test** : ouvrir une seconde session (RDP ou console) avant de fermer la première ; contrôler le résultat (`gpresult`, journaux).
5. **Retour arrière** : restaurer le snapshot, désactiver ou délier la GPO, annuler la règle.

---

## 3. Microsoft Defender : vérifier que le gardien veille

Microsoft Defender Antivirus est intégré à Windows. Le durcir, c'est d'abord **vérifier qu'il est actif, à jour, non contourné**.

```powershell
Get-MpComputerStatus | Select-Object AMServiceEnabled, AntivirusEnabled, RealTimeProtectionEnabled, IsTamperProtected, AntivirusSignatureLastUpdated, AMProductVersion
```

👉 Explication : affiche l'état du moteur, de la protection en temps réel, de la protection contre la falsification et l'ancienneté des signatures ; lecture seule. Des signatures vieilles de plusieurs jours sont un signal d'alerte.

```powershell
Get-MpPreference | Select-Object DisableRealtimeMonitoring, PUAProtection, MAPSReporting, ExclusionPath, ExclusionExtension, ExclusionProcess
```

👉 Explication : montre les paramètres effectifs et surtout les **exclusions**, un classique de contournement : toute exclusion doit être justifiée par écrit. Si un autre antivirus est installé, Defender peut être en mode passif : ce n'est pas une anomalie en soi.

```powershell
Get-MpThreatDetection | Select-Object -First 5 InitialDetectionTime, ThreatID, Resources
```

👉 Explication : liste les dernières détections ; une liste vide est normale sur un laboratoire propre.

**Mesures complémentaires (principe).**

- **Protection contre la falsification** (*Tamper Protection*) : empêche un programme ou un administrateur compromis de couper Defender.
- **PUA** : bloque les applications potentiellement indésirables.
- **Règles de réduction de la surface d'attaque (ASR)** : bloquent des comportements typiques d'attaque (macros Office lançant des processus, scripts obfusqués…). **Démarrez en mode audit**, lisez les événements, puis passez en blocage. C'est le même principe que « tester avant d'appliquer ».
- Mise à jour manuelle des signatures : `Update-MpSignature` (sans risque, elle modifie seulement les définitions).

---

## 4. Correctifs : garder la longueur d'avance

```powershell
Get-ComputerInfo -Property WindowsProductName, WindowsVersion, OsBuildNumber
Get-HotFix | Sort-Object InstalledOn -Descending | Select-Object -First 10 HotFixID, Description, InstalledOn
Test-Path 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\Auto Update\RebootRequired'
Get-Service wuauserv, UsoSvc | Select-Object Name, Status, StartType
```

👉 Explication : (1) version et build du système, (2) dix derniers correctifs installés (la date de la dernière mise à jour est l'indicateur clé), (3) `True` si un redémarrage est en attente, (4) état des services de mise à jour. Tout est en lecture seule.

**Organisation pour un parc.** Distribuez par **anneaux** : test, pilote, production ([[Glossary:WSUS]], Windows Update for Business ou Intune). Les correctifs de sécurité mensuels sont prioritaires ; un serveur critique se met à jour en **fenêtre de maintenance**, snapshot avant, vérification après.

**Rappel.** Un redémarrage en attente laisse souvent le correctif **inactif** : un système « à jour » mais non redémarré reste vulnérable.

---

## 5. Comptes locaux et LAPS (principe)

### Auditer les comptes locaux

```powershell
Get-LocalUser | Select-Object Name, Enabled, LastLogon, PasswordLastSet, PasswordRequired
Get-LocalGroupMember -SID S-1-5-32-544
Get-LocalUser | Where-Object { $_.SID -like '*-500' } | Select-Object Name, Enabled
```

👉 Explication : liste les comptes locaux avec leur état et la date du dernier changement de mot de passe, puis les membres du groupe **Administrateurs** désigné par son [[Glossary:SID]] (le nom du groupe varie selon la langue : `Administrators`, `Administrateurs`), puis le compte administrateur intégré (RID 500). Lecture seule.

À rechercher : comptes actifs mais inutilisés, `PasswordRequired` à `False`, membres inconnus dans le groupe Administrateurs, compte *Invité* actif.

**Bonnes pratiques.** Comptes **nominatifs** ; administrateur intégré désactivé ou géré par LAPS ; compte d'élévation distinct de la session quotidienne ; mots de passe longs et verrouillage après échecs répétés.

### LAPS : le principe

**Analogie.** Imaginez que toutes les portes d'un immeuble s'ouvrent avec la même clé : si elle fuit, tout est compromis. LAPS (*Local Administrator Password Solution*) donne à chaque porte **sa propre clé**, changée régulièrement, rangée dans un coffre.

![Schéma original du principe de LAPS : le poste dépose un mot de passe administrateur local aléatoire dans l'annuaire avec une échéance ; un administrateur autorisé peut le consulter](images/durcissement-windows-3.svg)

*Figure 2 — LAPS : un mot de passe administrateur local différent par poste. Création originale Pack Master (CC0).*

Fonctionnement de **Windows LAPS** (intégré aux versions récentes de Windows et Windows Server après les mises à jour de sécurité d'avril 2023) :

1. Une GPO ou une politique Intune définit le **compte géré**, la **longueur**, la **complexité** et la **durée de vie** du mot de passe.
2. Le poste génère un mot de passe **aléatoire** et le sauvegarde dans **Active Directory** (ou Microsoft Entra ID).
3. À l'échéance, ou après utilisation, le mot de passe est **renouvelé**.
4. Seuls les groupes **explicitement délégués** peuvent lire le mot de passe ; la lecture est tracée.

Gain : le mot de passe volé sur `PC-01` est inutile sur `PC-02`, ce qui bloque le déplacement latéral par « même mot de passe partout ». Côté diagnostic en lecture seule, le module LAPS fournit par exemple `Get-LapsDiagnostics` sur le poste. **Lire** un mot de passe dans l'annuaire est un acte sensible : réservez-le à la maintenance et conservez la trace.

---

## 6. Stratégies de groupe (GPO) : configurer à grande échelle

**Analogie.** Une GPO est une **circulaire interne** : au lieu de régler chaque bureau, on publie une règle que tous les bureaux concernés appliquent.

![Schéma original de l'ordre d'application des GPO : stratégie locale, site, domaine, unité d'organisation ; le dernier appliqué l'emporte](images/durcissement-windows-2.svg)

*Figure 3 — Ordre LSDOU : le dernier niveau appliqué l'emporte en cas de conflit. Création originale Pack Master (CC0).*

**L'ordre LSDOU** : stratégie **L**ocale, **S**ite, **D**omaine, **O**U (les OU imbriquées s'appliquent de la plus haute à la plus basse). En cas de conflit, la **dernière appliquée gagne**, sauf si une GPO supérieure est **appliquée** (*Enforced*) ou si l'héritage est bloqué sur une OU.

**Réglages de sécurité typiques** : longueur minimale des mots de passe et verrouillage de compte, audit avancé (connexions, comptes, processus), droits d'ouverture de session par Bureau à distance, [[Glossary:NTLM]] restreint, signature SMB, [[Glossary:UAC]], profils du pare-feu, paramètres LAPS et BitLocker.

**Méthode sûre.**

1. Créez la GPO **non liée** et **sauvegardez-la** (`Backup-GPO`).
2. Liez-la à une **OU pilote** contenant quelques machines de test.
3. Contrôlez le résultat, puis étendez progressivement.
4. Retour arrière : **délier** la GPO ou désactiver son lien ; la valeur reprend son état d'origine (selon le type de paramètre, un redémarrage peut être requis).

```powershell
gpresult /r /scope computer
gpupdate /force
Get-GPOReport -Name "Durcissement-Postes" -ReportType Html -Path .\Durcissement-Postes.html
```

👉 Explication : (1) résume les GPO réellement appliquées à l'ordinateur, (2) force l'actualisation immédiate des stratégies (déclenche l'application, hors lecture seule stricte mais sans risque en lui-même), (3) génère un rapport HTML de la GPO nommée (module `GroupPolicy`, poste d'administration). Remplacez le nom par celui de votre GPO.

> 💡 Les **bases de référence de sécurité** publiées par Microsoft (*Security Baselines*, via le *Security Compliance Toolkit*) et les benchmarks du CIS constituent des points de départ éprouvés : importez-les en **audit** et comparez avant d'appliquer.

---

## 7. BitLocker (principe)

BitLocker **chiffre le volume** : un disque volé ou une machine perdue n'expose pas les données. C'est une protection **au repos**, pas contre un attaquant qui travaille sur la session ouverte.

- **[[Glossary:TPM]]** : puce qui contient la clé et vérifie l'intégrité du démarrage ; le déverrouillage est transparent.
- **Protecteurs** : TPM seul, TPM + code PIN, mot de passe, **clé de récupération** de 48 chiffres.
- **Clé de récupération** : **à sauvegarder avant d'activer** (dans Active Directory ou Entra ID, via une GPO). Sans elle, une panne de matériel ou un changement du démarrage peut rendre les données définitivement illisibles.
- **Suspension** : avant une mise à jour du micrologiciel ([[Glossary:BIOS]]/UEFI), suspendez temporairement la protection (`Suspend-BitLocker -MountPoint C: -RebootCount 1`), sinon la machine demande la clé de récupération.

```powershell
Get-BitLockerVolume | Select-Object MountPoint, VolumeStatus, ProtectionStatus, EncryptionMethod
manage-bde -status C:
Get-Tpm | Select-Object TpmPresent, TpmReady
```

👉 Explication : montre l'état de chiffrement et de protection des volumes, le détail du volume système et la présence d'un TPM prêt ; lecture seule (droits administrateur requis). Un statut `FullyEncrypted` avec protection `On` est l'état cible.

**Mise en œuvre (principe).** Prévoir la **sauvegarde des clés dans l'annuaire**, activer sur une machine pilote, vérifier la récupération avec la clé, puis généraliser. Retour arrière : le déchiffrement existe (`manage-bde -off`) mais prend du temps ; on le teste sur la VM, pas en production.

---

## 8. Journaux d'événements de sécurité

**Analogie.** Le journal Sécurité est le registre des entrées et sorties : il ne **bloque** rien, il permet de **comprendre** après coup, et de **détecter** pendant.

Le journal **Sécurité** (consultable avec l'observateur d'événements ou `Get-WinEvent`, droits administrateur) contient surtout ce que la **stratégie d'audit** a demandé d'enregistrer. Sans audit configuré, il reste pauvre.

| ID | Signification | Intérêt |
|---|---|---|
| 4624 | ouverture de session réussie | qui, d'où, type de connexion (3 réseau, 10 RDP) |
| 4625 | échec d'ouverture de session | force brute, mot de passe erroné |
| 4672 | privilèges spéciaux attribués | connexion d'un administrateur |
| 4688 | création d'un processus | traçage des commandes (si audit activé) |
| 4720 / 4726 | compte créé / supprimé | création de compte pirate |
| 4732 | membre ajouté à un groupe local | ajout aux Administrateurs |
| 4740 | compte verrouillé | attaque ou erreur d'utilisateur |
| 4719 | stratégie d'audit modifiée | tentative de masquer ses traces |
| 1102 | journal d'audit effacé | trace d'un effacement, à investiguer |

```powershell
auditpol /get /category:*
wevtutil gl Security
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4625; StartTime=(Get-Date).AddHours(-24)} -MaxEvents 20 | Select-Object TimeCreated, Id, Message
```

👉 Explication : (1) affiche la stratégie d'audit avancée effective ; (2) montre la configuration du journal (taille maximale, rétention) ; (3) cherche les 20 derniers échecs de connexion des 24 dernières heures. L'erreur « aucun événement correspondant » signifie simplement qu'il n'y en a pas. Tout est en lecture.

**Durcissement des journaux.** Augmentez la taille du journal Sécurité (la valeur par défaut sature vite), activez l'audit avancé par GPO, **centralisez** les événements (*Windows Event Forwarding* ou supervision) pour que l'effacement local ne détruise pas la preuve, et alertez sur 1102 et 4719.

---

## 9. SMB et RDP exposés : deux portes à ne jamais laisser ouvertes

**SMB** (partage de fichiers, [[Glossary:TCP]] 445) et **RDP** (Bureau à distance, TCP 3389) sont les deux services Windows les plus visés par les scanners et les rançongiciels. Règle absolue : **ne jamais les exposer directement à Internet**. En interne, on les **limite** par pare-feu aux seuls réseaux d'administration, et l'accès distant passe par un **[[Glossary:VPN]]**, un **bastion** ou une **passerelle RD Gateway** avec authentification forte.

![Schéma original de l'exposition de SMB et RDP : Internet est bloqué par le pare-feu, l'administrateur passe par un VPN ou un bastion et une règle limitée au réseau d'administration](images/durcissement-windows-4.svg)

*Figure 4 — Aucun accès direct depuis Internet ; accès d'administration encadré. Création originale Pack Master (CC0).*

### Contrôles SMB

```powershell
Get-SmbServerConfiguration | Select-Object EnableSMB1Protocol, EnableSMB2Protocol, RequireSecuritySignature, EncryptData
Get-SmbShare | Select-Object Name, Path, Description
Get-NetTCPConnection -State Listen -LocalPort 445,3389 -ErrorAction SilentlyContinue | Select-Object LocalAddress, LocalPort, OwningProcess
```

👉 Explication : (1) vérifie que **SMBv1** est désactivé (`EnableSMB1Protocol` à `False`) et si la signature est exigée, (2) liste les partages exposés (les partages administratifs `ADMIN$`, `C$` sont normaux), (3) montre si 445 ou 3389 sont en écoute. Lecture seule.

**Si SMBv1 est actif :** vérifiez d'abord qui l'utilise (`Set-SmbServerConfiguration -AuditSmb1Access $true` active un audit sans bloquer, puis consultez le journal *Microsoft-Windows-SMBServer/Audit*). Désactivez ensuite avec snapshot préalable : `Set-SmbServerConfiguration -EnableSMB1Protocol $false`. Retour arrière : `$true`.

### Contrôles RDP

```powershell
Get-ItemProperty 'HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server' -Name fDenyTSConnections
Get-ItemProperty 'HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp' -Name UserAuthentication
Get-NetFirewallRule -Name 'RemoteDesktop-UserMode-In-TCP' | Get-NetFirewallAddressFilter | Select-Object RemoteAddress
```

👉 Explication : (1) `fDenyTSConnections` à `0` signifie RDP **activé**, `1` désactivé ; (2) `UserAuthentication` à `1` signifie que l'authentification au niveau du réseau (**[[Glossary:NLA]]**) est exigée ; (3) affiche les adresses autorisées par la règle RDP entrante. `Any` signifie qu'il n'y a aucune limitation.

### Encadrer RDP

1. Gardez **NLA activé** et exigez des mots de passe longs ou une authentification forte.
2. **Limitez l'adresse source** de la règle : `Set-NetFirewallRule -Name 'RemoteDesktop-UserMode-In-TCP' -RemoteAddress 192.0.2.0/24`. **Attention au lockout** : si vous êtes connecté depuis une autre adresse, vous perdez votre propre accès. Gardez la **console** ouverte, testez une **seconde connexion** avant de fermer la première, et planifiez le retour arrière (`-RemoteAddress Any`).
3. Limitez les comptes autorisés (groupe *Utilisateurs du Bureau à distance*), activez le **verrouillage des comptes** après échecs, surveillez les événements **4625** et **4624 de type 10**.

---

## 10. Un script de contrôle en lecture seule

```powershell
# Collecte en lecture seule : aucune modification. À lancer en administrateur.
Get-Date -Format s
Get-ComputerInfo -Property WindowsProductName, OsBuildNumber
Get-MpComputerStatus | Select-Object RealTimeProtectionEnabled, AntivirusSignatureLastUpdated
Get-HotFix | Sort-Object InstalledOn -Descending | Select-Object -First 3
Get-LocalGroupMember -SID S-1-5-32-544 | Select-Object Name, ObjectClass
Get-SmbServerConfiguration | Select-Object EnableSMB1Protocol, RequireSecuritySignature
Get-NetTCPConnection -State Listen | Select-Object LocalAddress, LocalPort, OwningProcess | Sort-Object LocalPort
Get-BitLockerVolume | Select-Object MountPoint, ProtectionStatus
Get-NetFirewallProfile | Select-Object Name, Enabled, DefaultInboundAction
```

👉 Explication : rassemble les contrôles de la leçon (date, version, Defender, correctifs, administrateurs locaux, SMB, ports en écoute, BitLocker, profils du pare-feu) ; à rediriger vers un fichier horodaté avec `| Out-File`, puis à comparer avant et après chaque durcissement.

---

## Mise en pratique guidée

**Cadre.** VM `lab-win` Windows Server 2022 (évaluation) ou Windows 11, sans réseau externe, adresse `192.0.2.30`. **Avant de commencer** : point de contrôle `avant-durcissement`, console de l'hyperviseur testée. Durée : environ 1 h 45.

**Étape 1 — État initial.** Exécutez le script de la section 10 et enregistrez la sortie (`etat-initial.txt`). Notez : date de la dernière mise à jour, présence d'exclusions Defender, état de SMBv1, ports en écoute.

**Étape 2 — Defender et correctifs.** Lancez `Update-MpSignature`, relisez `Get-MpComputerStatus`, installez les mises à jour Windows Update, redémarrez si nécessaire, puis recontrôlez `Get-HotFix`.

**Étape 3 — Comptes.** Activez l'audit de la gestion des comptes (`auditpol /set /subcategory:"User Account Management" /success:enable /failure:enable`, nom localisé sur un système français), puis :

```powershell
New-LocalUser -Name 'test-lab' -NoPassword -Description 'Compte de test jetable'
Remove-LocalUser -Name 'test-lab'
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4720,4726} -MaxEvents 5 | Select-Object TimeCreated, Id
```

👉 Explication : crée puis supprime un compte local de test (VM jetable uniquement) et relit les événements de création et de suppression. Retour arrière : restaurer le point de contrôle.

**Étape 4 — Limiter RDP, en sécurité.** Avec la **console** ouverte et une session RDP déjà établie depuis `192.0.2.10`, limitez la règle RDP à `192.0.2.0/24` (section 9), testez une **seconde** connexion depuis cette adresse, vérifiez qu'une connexion depuis une autre adresse est refusée, puis revenez à `Any` pour terminer.

**Étape 5 — SMBv1.** Contrôlez `EnableSMB1Protocol` ; s'il est à `True`, activez l'audit, puis désactivez-le après vérification.

**Étape 6 — GPO (si un domaine de test existe).** Créez la GPO `Durcissement-Postes` (par exemple verrouillage de compte après 5 échecs), sauvegardez-la, liez-la à l'OU pilote, vérifiez avec `gpresult /r`, puis déliez-la pour revenir en arrière.

**Étape 7 — Comparer et revenir en arrière.** Relancez le script (`etat-final.txt`), comparez avec `Compare-Object (Get-Content etat-initial.txt) (Get-Content etat-final.txt)`, puis restaurez le point de contrôle.

---

## Exercices

1. **(Facile)** Citez trois contrôles de l'état de Microsoft Defender et ce que signifie une exclusion non justifiée.
2. **(Facile)** Pourquoi désigne-t-on le groupe Administrateurs par son SID dans un script destiné à un parc multilingue ?
3. **(Facile)** Quel est l'intérêt de LAPS, en une phrase ?
4. **(Intermédiaire)** Une GPO de domaine impose une valeur, une GPO d'OU en impose une autre : laquelle gagne, et à quelle exception près ?
5. **(Intermédiaire)** Vous devez activer BitLocker sur 50 postes. Listez les précautions et l'ordre des opérations.
6. **(Intermédiaire)** Quels événements du journal Sécurité regarder pour détecter une attaque par force brute sur RDP ?
7. **(Avancé)** `Get-SmbServerConfiguration` montre `EnableSMB1Protocol : True` sur un serveur de fichiers de production. Décrivez votre plan.
8. **(Avancé)** Vous voulez limiter RDP à `192.0.2.0/24` sur un serveur distant. Décrivez la procédure anti-lockout.

---

## Corrigés des exercices

1. `Get-MpComputerStatus` (temps réel, signatures, protection contre la falsification), `Get-MpPreference` (exclusions), `Get-MpThreatDetection`. Une exclusion soustrait un chemin à l'analyse : un malware placé là n'est pas vu ; on la justifie et on la revoit.
2. Les noms de groupes sont localisés, mais le SID `S-1-5-32-544` est identique partout.
3. Un mot de passe administrateur local unique et renouvelé par poste : le vol d'un mot de passe ne permet pas le rebond.
4. La GPO d'**OU** gagne (dernière appliquée), sauf si celle du domaine est **Enforced**.
5. Vérifier TPM et mode de démarrage ; configurer par GPO la **sauvegarde des clés** dans l'annuaire ; contrôler une clé sur un poste pilote ; tester la récupération ; déployer par vagues ; documenter la suspension avant mise à jour du micrologiciel.
6. 4625 (échecs), 4624 de type 10 (RDP réussi), 4740 (verrouillage) ; compter les échecs par adresse source sur une fenêtre de temps.
7. Inventorier les clients SMBv1 (`AuditSmb1Access`), les migrer ou les isoler, snapshot, désactiver en maintenance, surveiller, retour arrière (`$true`), puis retirer la fonctionnalité.
8. Console prête ; session RDP n°1 ouverte ; **tâche de retour arrière** qui remet `Any` après 10 minutes ; modification de la règle ; test d'une session n°2 depuis `192.0.2.0/24` ; succès : supprimer la tâche ; échec : elle rétablit l'accès, ou utiliser la console.

## Quiz

**Q1. Quel paramètre indique que SMBv1 est actif ?**
a) `EncryptData` b) `EnableSMB1Protocol` à `True` c) `RequireSecuritySignature` d) `AuditSmb1Access`
**Réponse : b.** C'est le drapeau d'activation de SMBv1, à désactiver sur les systèmes modernes.

**Q2. Dans l'ordre LSDOU, quelle stratégie est appliquée en dernier ?**
a) locale b) site c) domaine d) unité d'organisation
**Réponse : d.** L'OU est le niveau le plus proche de l'objet.

**Q3. Que protège BitLocker ?**
a) un administrateur malveillant b) le vol du disque ou de la machine c) les virus d) l'hameçonnage
**Réponse : b.** Il chiffre les données au repos.

**Q4. Pourquoi sauvegarder la clé de récupération BitLocker avant d'activer ?**
a) le chiffrement est plus rapide b) sans elle, une panne ou un changement de démarrage peut rendre les données illisibles c) c'est inutile avec un TPM d) pour désactiver Defender
**Réponse : b.** Un TPM ne dispense pas de la clé de récupération.

**Q5. L'événement 4625 correspond à…**
a) une session réussie b) un échec d'ouverture de session c) une création de compte d) un effacement du journal
**Réponse : b.** Une rafale de 4625 évoque une force brute.

**Q6. L'événement 1102 signale…**
a) un démarrage b) l'effacement du journal d'audit c) un verrouillage de compte d) une mise à jour
**Réponse : b.** Un attaquant efface souvent le journal pour masquer ses traces.

**Q7. Pourquoi ne jamais exposer RDP (3389) à Internet ?**
a) c'est lent b) il est massivement scanné et attaqué c) il ne chiffre rien d) il n'a pas de journal
**Réponse : b.** On le place derrière VPN, bastion ou passerelle avec authentification forte.

**Q8. Apport principal de LAPS ?**
a) chiffrer les disques b) un mot de passe administrateur local unique par machine, renouvelé c) filtrer le réseau d) mettre à jour Windows
**Réponse : b.** Il empêche le rebond par un mot de passe identique partout.

**Q9. Avant de généraliser une GPO de sécurité ?**
a) la lier à toute l'entreprise b) la sauvegarder et la tester sur une OU pilote c) la supprimer d) désactiver Defender
**Réponse : b.** Le retour arrière consiste à délier le lien.

**Q10. Pourquoi garder la console ouverte en limitant la règle RDP ?**
a) pour accélérer la règle b) pour corriger si l'on se coupe soi-même c) c'est obligatoire pour PowerShell d) pour désactiver NLA
**Réponse : b.** La console fonctionne sans réseau : c'est le filet contre le lockout.

## Erreurs fréquentes et dépannage

| Symptôme | Cause probable | Remède |
|---|---|---|
| `Get-MpComputerStatus` renvoie une erreur | Defender désinstallé ou autre antivirus principal, module indisponible | vérifier l'état dans Sécurité Windows et le service `WinDefend` |
| La GPO ne s'applique pas | lien absent, filtrage de sécurité, réplication, héritage bloqué | `gpresult /r`, `gpupdate /force`, vérifier l'OU de la machine |
| Perte d'accès RDP après règle de pare-feu | adresse source non autorisée | console ; `Set-NetFirewallRule ... -RemoteAddress Any`, puis corriger |
| BitLocker réclame la clé de récupération | changement de micrologiciel, de démarrage ou de TPM | saisir la clé ; à l'avenir `Suspend-BitLocker` avant la mise à jour |
| `Get-WinEvent` : « aucun événement » | audit non activé, ou filtre erroné | `auditpol /get /category:*`, élargir la période |
| Applications cassées après désactivation de SMBv1 | un équipement ancien utilise SMBv1 | audit préalable, migrer l'équipement, retour arrière `$true` |

---

## À retenir

- Le durcissement Windows est **stratifié** : données, hôte, comptes, réseau, supervision.
- **Defender** actif et à jour, **exclusions** justifiées ; **correctifs** par anneaux, **redémarrage** compris.
- **LAPS** : un mot de passe administrateur local unique par machine ; la lecture est un acte sensible.
- **GPO** : ordre LSDOU, **test sur OU pilote**, sauvegarde, retour arrière par déliaison.
- **BitLocker** : chiffrement au repos ; **clé de récupération sauvegardée d'abord**.
- **Journal Sécurité** : 4624, 4625, 4672, 4720, 4732, 4740, 4719, 1102 ; audit à activer, journaux à centraliser.
- **SMB et RDP** : jamais exposés à Internet ; limiter, NLA, VPN/bastion ; **anti-lockout** avec console.

---

## Pour aller plus loin

- Documentation de sécurité Windows (Microsoft Learn) : <https://learn.microsoft.com/fr-fr/windows/security/>
- Windows LAPS : <https://learn.microsoft.com/fr-fr/windows-server/identity/laps/laps-overview>
- BitLocker : <https://learn.microsoft.com/fr-fr/windows/security/operating-system-security/data-protection/bitlocker/>
- Pare-feu Windows : <https://learn.microsoft.com/fr-fr/windows/security/operating-system-security/network-security/windows-firewall/>
- Détecter, activer et désactiver SMB : <https://learn.microsoft.com/fr-fr/windows-server/storage/file-server/troubleshoot/detect-enable-and-disable-smbv1-v2-v3>
- Audit de sécurité : <https://learn.microsoft.com/fr-fr/windows/security/threat-protection/auditing/security-auditing-overview>
- Benchmarks CIS (site officiel) : <https://www.cisecurity.org/cis-benchmarks>
- [[Glossary:ANSSI]], publications et guides de sécurité : <https://cyber.gouv.fr/publications>

*Si une adresse Microsoft Learn a changé, cherchez le titre de la page sur le site officiel.*

---

## Crédits des images

Aucune image tierce n'est utilisée dans cette leçon : les quatre schémas sont des créations originales.

| Fichier | Source (URL de la page) | Auteur | Licence | Modifications |
|---|---|---|---|---|
| `images/durcissement-windows-1.svg` | Création originale du projet Pack Master | Projet Pack Master | CC0 / domaine public — <https://creativecommons.org/publicdomain/zero/1.0/deed.fr> | Sans objet (œuvre originale) |
| `images/durcissement-windows-2.svg` | Création originale du projet Pack Master | Projet Pack Master | CC0 / domaine public — <https://creativecommons.org/publicdomain/zero/1.0/deed.fr> | Sans objet |
| `images/durcissement-windows-3.svg` | Création originale du projet Pack Master | Projet Pack Master | CC0 / domaine public — <https://creativecommons.org/publicdomain/zero/1.0/deed.fr> | Sans objet |
| `images/durcissement-windows-4.svg` | Création originale du projet Pack Master | Projet Pack Master | CC0 / domaine public — <https://creativecommons.org/publicdomain/zero/1.0/deed.fr> | Sans objet |

*Création originale du projet Pack Master, dédiée au domaine public (CC0).*

---

## Historique de vérification

| Date | OS/logiciel | Testeur | Verdict |
|---|---|---|---|
| 2026-11-01 | Windows Server 2022 / Windows 11, PowerShell 5.1 et 7 (commandes de la leçon) | Rédaction assistée (Copilot) | Non testé sur plateforme cible |

*Les commandes ont été relues pour leur syntaxe et leur caractère lecture seule, mais aucune n'a été exécutée sur une machine Windows lors de la rédaction. Validez-les dans votre laboratoire avant tout usage.*