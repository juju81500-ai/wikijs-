---
title: "Leçon — Déploiement et inventaire des postes : images, MDT/WDS/Autopilot/Intune, automatisation et cycle de vie"
description: "À l'issue de cette leçon, vous saurez :"
published: true
date: 2026-11-03T09:36:13Z
tags: ["transverse", "tout-en-un", "lecon", "support", "deploiement", "inventaire", "autopilot", "intune", "cycle-de-vie"]
editor: markdown
dateCreated: 2026-11-03T09:36:13Z
dateModified: 2026-11-03T09:36:13Z
---

# Leçon — Déploiement et inventaire des postes : images, MDT/WDS/Autopilot/Intune, automatisation et cycle de vie

- **Tags** : `transverse`, `tout-en-un`, `lecon`, `support`, `deploiement`, `inventaire`, `autopilot`, `intune`, `cycle-de-vie`
- **Niveau** : intermédiaire (technicien support N2, TSSR, administrateur junior)
- **Durée estimée** : 4 h (lecture 1 h 30, laboratoire 1 h 15, exercices et quiz 1 h 15)

---

## Objectifs pédagogiques

À l'issue de cette leçon, vous saurez :

1. Expliquer ce qu'est une **image de référence** et choisir entre image « épaisse », « mince » et approche hybride.
2. Situer **WDS, MDT, Configuration Manager, Autopilot et Intune** les uns par rapport aux autres (concepts et limites).
3. Décrire une **installation automatisée** : fichier de réponses, séquence de tâches, scripts de premier démarrage, gestionnaire de paquets.
4. Définir un **inventaire** utile : champs, sources, rapprochement, qualité des données.
5. Décrire le **cycle de vie du matériel**, de la commande au recyclage, avec l'effacement sécurisé des données.
6. Construire un **plan de déploiement** prudent : pilote, retour arrière, documentation.

## Prérequis et durée

- Notions de Windows (compte, domaine, disque), de réseau (DHCP, DNS) et de PowerShell de base ; la leçon [Le poste Windows client](/fr/00-cours-theoriques/tout-en-un/08-support-et-gestion-de-service/lecons/lecon-poste-windows-client) est un complément utile.
- Une **VM Windows jetable** pour la pratique (snapshot et console hyperviseur disponibles). Les outils serveur (WDS, Intune) sont étudiés **en concepts** : aucun n'est requis.
- Durée totale : environ 4 h.

## L'essentiel en bref

- Déployer, c'est rendre **reproductible** la mise à disposition d'un poste : même point de départ, mêmes réglages, moins d'erreurs, installation plus rapide.
- Deux grandes familles : l'**image** (on copie un système préparé) et l'**approvisionnement** (le poste reçoit sa configuration depuis un service à la première connexion).
- L'**automatisation** repose sur des scripts versionnés, idempotents, journalisés, **sans secret en clair**.
- L'**inventaire** n'a de valeur que s'il est **à jour** : plusieurs sources rapprochées, un identifiant stable (numéro de série).
- Le **cycle de vie** ne s'arrête pas à l'installation : affectation, exploitation, retrait et **effacement sécurisé** font partie du service.

---

## 1. Pourquoi standardiser le déploiement ?

Avec une **recette** et un **moule**, on produit en série et on repère les écarts. Pour les postes : **rapidité**, **cohérence** (dépannage plus simple), **traçabilité** et **sécurité** (correctifs intégrés dès le départ).

Prix à payer : maintenir et tester la recette.

## 2. L'image de référence

### 2.1 Définitions

Une **image** est une copie d'un système préparé, au format **WIM** (fichier d'image Windows, qui peut contenir plusieurs images et est manipulé avec DISM). On la prépare dans une machine de référence (de préférence une VM), puis on la **généralise** (outil Sysprep) pour retirer les éléments propres à la machine (identifiant de sécurité, nom), avant de la capturer.

Trois philosophies :

| Approche | Contenu de l'image | Avantages | Inconvénients |
|---|---|---|---|
| **Épaisse** | Système + pilotes + applications + réglages | Déploiement rapide, hors-ligne | Image lourde, à refaire à chaque changement d'application |
| **Mince** | Système à jour, quasi nu | Image stable, peu à maintenir | Installation d'applications au déploiement, plus longue |
| **Hybride** | Système + base commune ; applications et réglages ensuite | Bon équilibre | Demande une chaîne d'automatisation solide |

La tendance actuelle favorise l'image **mince ou hybride** : on évite de refabriquer l'image à chaque nouvelle version d'une application.

### 2.2 Bonnes pratiques

Construisez l'image dans une **VM propre** à partir d'un média officiel, à jour ; **versionnez** (`W11-2026-11`, journal des changements) ; gérez les **pilotes par modèle** ; ne laissez **aucun secret** ni donnée personnelle ; **testez** sur chaque modèle du parc avant diffusion.

### 2.3 Inspecter une image (lecture seule)

```powershell
Get-WindowsImage -ImagePath "D:\sources\install.wim"
```

👉 Explication : liste les images contenues dans un fichier WIM (index, nom, taille) ; le chemin est un exemple de média monté dans la VM de laboratoire, la lecture n'altère pas le fichier.

```powershell
dism /Get-WimInfo /WimFile:D:\sources\install.wim /Index:1
```

👉 Explication : affiche le détail d'une image (édition, version, architecture) ; vérifie qu'on déploie bien la version attendue.

> **Sysprep (⚠️)** : la généralisation est une opération **sans retour** sur la machine de référence. Prenez un **snapshot avant**, travaillez sur une VM jetable, et conservez la VM « avant Sysprep » pour la prochaine mise à jour de l'image.

## 3. Outils de déploiement : concepts

### 3.1 La chaîne classique par image

![Deux approches de déploiement : image classique avec serveur de déploiement, et approvisionnement cloud Autopilot et Intune](images/deploiement-inventaire-2.svg)

*Figure 1 — À gauche, le déploiement par image ; à droite, l'approvisionnement moderne depuis le service.*

Chaîne par image :

1. Le poste démarre par le **réseau (PXE)** ou depuis une clé USB.
2. **WDS** (Windows Deployment Services, rôle Windows Server) répond au démarrage réseau et fournit une image de démarrage (WinPE).
3. **MDT** (Microsoft Deployment Toolkit) ajoute une **séquence de tâches** : partitionnement, application de l'image, injection de pilotes, installation d'applications, jonction au domaine, paramétrage.
4. Le poste redémarre sur le système fraîchement installé.

**Configuration Manager** (anciennement SCCM) propose le même principe à grande échelle, avec distribution de logiciels, correctifs et rapports.

> **À connaître** : MDT n'est plus développé (Microsoft a annoncé la fin de sa maintenance) et WDS fait l'objet de restrictions et d'annonces de retrait. Consultez la documentation officielle pour l'état actuel avant de construire une nouvelle chaîne sur ces briques. Les concepts (démarrage réseau, séquence de tâches, pilotes par modèle) restent valables et se retrouvent dans les solutions successeurs.

### 3.2 L'approvisionnement moderne : Autopilot et Intune

- **Microsoft Intune** est un service de **gestion des appareils** : politiques de sécurité, applications, conformité, effacement à distance.
- **Windows Autopilot** prépare l'appareil au **premier démarrage** : enregistré (empreinte matérielle, souvent fournie par le revendeur) et associé à un **profil**, il se rattache dès la première connexion Internet à l'organisation (**Microsoft Entra ID**), s'inscrit à Intune et reçoit politiques et applications ; la **page d'état d'inscription** montre la progression.

Scénario : un poste est livré chez l'agent, qui l'allume, se connecte au Wi-Fi et s'identifie ; le poste se configure seul, sans image à maintenir.

### 3.3 Autopilot ou image : comment choisir ?

| Critère | Image (WDS/MDT) | Autopilot/Intune |
|---|---|---|
| Réseau nécessaire | Réseau local, serveur de déploiement | Connexion Internet vers le service |
| Poste pré-existant | Réinstallation complète | Nouvel appareil ou réinitialisation |
| Maintenance | Images, pilotes, séquences à entretenir | Profils et applications à maintenir dans le service |
| Applications lourdes ou hors-ligne | Bien adapté | Peut être long selon la bande passante |
| Appareils hors domaine, télétravail | Peu adapté | Bien adapté |
| Dépendances | Infrastructure sur site | Licences, abonnement au service |

Les deux approches **coexistent** souvent.

### 3.4 Pièges de l'approvisionnement

Définir qui peut enregistrer et inscrire des appareils ; prévoir l'accès réseau du poste au service (pare-feu, proxy) ; décider du statut d'administrateur local ; prévoir un repli si l'inscription échoue ; traiter à part les appareils partagés ou kiosques.

## 4. Automatiser l'installation

### 4.1 Les briques

- **Fichier de réponses** (`unattend.xml`) : dit à l'installation de Windows comment se configurer sans question (langue, partitions, nom, compte d'administration temporaire).
- **Séquence de tâches** (MDT, Configuration Manager) : enchaîne les étapes avec conditions (modèle, site, rôle).
- **Scripts de premier démarrage** : PowerShell exécuté une fois à la première session.
- **Gestionnaire de paquets** : **winget**, ou solution d'entreprise, pour installer et mettre à jour des applications de façon déclarative.
- **Gestion de configuration** : stratégies de groupe ou politiques MDM pour maintenir l'état dans le temps.

### 4.2 Principes d'un bon script de déploiement

1. **Idempotent** : l'exécuter deux fois donne le même résultat sans erreur.
2. **Journalisé** : chaque étape écrit dans un journal consultable en cas d'échec.
3. **Paramétrable** : les valeurs (nom du site, modèle) viennent de paramètres, pas du code.
4. **Sans secret en clair** : pas de mot de passe dans un script ni dans l'image ; recourir à un coffre, à une identité du poste, à des comptes à privilèges minimaux.
5. **Testé** sur VM, versionné, relu avant diffusion.

Squelette PowerShell de premier démarrage :

```powershell
$dir = "$env:ProgramData\Deploiement"
New-Item -ItemType Directory -Path $dir -Force | Out-Null
Start-Transcript -Path "$dir\premier-demarrage.log" -Append
try {
    if (-not (Test-Path "$dir\ok.flag")) { New-Item -ItemType File -Path "$dir\ok.flag" | Out-Null }
} finally {
    Stop-Transcript
}
```

👉 Explication : crée le dossier au besoin, ouvre un journal, ne crée le marqueur que s'il n'existe pas (idempotence) et clôt le journal quoi qu'il arrive ; les vraies étapes se placent dans le bloc `try`.

### 4.3 Fichier de réponses minimal

```xml
<?xml version="1.0" encoding="utf-8"?>
<unattend xmlns="urn:schemas-microsoft-com:unattend">
  <settings pass="specialize">
    <component name="Microsoft-Windows-Shell-Setup" processorArchitecture="amd64"
               publicKeyToken="31bf3856ad364e35" language="neutral" versionScope="nonSxS">
      <ComputerName>PC-LAB-001</ComputerName>
    </component>
  </settings>
</unattend>
```

👉 Explication : squelette qui ne fixe que le nom de l'ordinateur ; ni mot de passe ni clé de produit n'y figurent. Un vrai fichier se construit avec l'outil de création de fichiers de réponses Windows (Windows System Image Manager) pour respecter le schéma de la version de Windows.

Validez au minimum que le fichier est de l'XML bien formé :

```powershell
[xml](Get-Content .\unattend.xml -Raw) | Out-Null; "XML bien formé"
```

👉 Explication : tente de lire le fichier comme XML ; en cas d'erreur de syntaxe, PowerShell affiche l'erreur et le message final n'apparaît pas. Cela ne valide pas le schéma Windows.

### 4.4 winget : installer et inventorier des applications

```powershell
winget --version
```

👉 Explication : vérifie la présence du gestionnaire de paquets sur le poste (installé avec les versions récentes de Windows).

```powershell
winget search "7-zip" --source winget
```

👉 Explication : recherche une application dans le catalogue public et affiche son identifiant ; lecture seule.

```powershell
winget list
```

👉 Explication : liste les applications installées et leurs versions ; sert d'inventaire logiciel partiel et de point de comparaison entre postes.

Pour installer, on cible l'identifiant exact et on évite les installations interactives (⚠️ modification, à tester sur une VM de laboratoire) :

```powershell
winget install --id 7zip.7zip -e --silent --accept-package-agreements --accept-source-agreements
```

👉 Explication : installe 7-Zip de façon silencieuse en acceptant les accords du catalogue ; retour arrière : `winget uninstall --id 7zip.7zip -e`.

### 4.5 Et côté Linux ?

Mêmes idées : **kickstart**, **preseed** ou **autoinstall** pour l'installation, **cloud-init** pour le premier démarrage, Ansible pour maintenir l'état ; mêmes principes (idempotence, journaux, aucun secret en clair).

## 5. L'inventaire des postes

### 5.1 À quoi sert-il ?

Un inventaire répond à : *qu'avons-nous, où, à qui, dans quel état, avec quelles versions ?* Il sert la **gestion des licences**, les **correctifs de sécurité** (quels postes sont vulnérables ?), le **renouvellement** (quels postes ont plus de quatre ans ?), le **support** (modèle, historique) et l'**audit**.

### 5.2 Les champs utiles

- **Identité** : numéro de série (identifiant stable), nom d'hôte, modèle, constructeur, étiquette d'inventaire.
- **Technique** : système et version, processeur, mémoire, disque, version du BIOS/UEFI, chiffrement du disque, état de conformité.
- **Administratif** : date d'achat, fin de garantie, fournisseur, coût, centre de coûts.
- **Affectation** : utilisateur ou service, site, état (stock, en service, en réparation, retiré).
- **Logiciels** : applications et versions, licences associées.

### 5.3 Les sources et leur rapprochement

![Sources d'inventaire (agent, annuaire, réseau, achats) alimentant un inventaire central utilisé pour les licences, la sécurité, le renouvellement et le support](images/deploiement-inventaire-3.svg)

*Figure 2 — Plusieurs sources, une référence : on rapproche et on signale les écarts.*

| Source | Ce qu'elle apporte | Limite |
|---|---|---|
| Agent sur le poste | Matériel et logiciels détaillés | Absent des postes éteints ou hors réseau |
| Annuaire (comptes machine) | Liste des machines jointes et dernière connexion | Comptes obsolètes si le nettoyage n'est pas fait |
| Gestion des appareils (MDM) | Conformité, propriétaire, version | Seulement les appareils inscrits |
| Découverte réseau | Équipements inconnus | Informations limitées |
| Achats et factures | Date, prix, garantie | Pas d'état réel |

**Règle de rapprochement** : une machine connue d'une seule source est suspecte (poste fantôme, machine non gérée, compte obsolète). On pose une clé d'appariement (numéro de série) et on traite les écarts de façon régulière.

### 5.4 Collecter l'information (lecture seule)

```powershell
Get-CimInstance Win32_BIOS | Select-Object SerialNumber, SMBIOSBIOSVersion
```

👉 Explication : lit le numéro de série et la version du BIOS, clé d'appariement entre les sources.

```powershell
Get-CimInstance Win32_ComputerSystem | Select-Object Name, Manufacturer, Model, TotalPhysicalMemory
```

👉 Explication : nom, constructeur, modèle et mémoire de la machine.

```powershell
Get-CimInstance Win32_OperatingSystem | Select-Object Caption, Version, InstallDate, LastBootUpTime
```

👉 Explication : système, version, date d'installation et dernier démarrage ; une date de démarrage très ancienne trahit un poste jamais redémarré (correctifs en attente).

```powershell
Get-ItemProperty "HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\*" | Where-Object DisplayName | Select-Object DisplayName, DisplayVersion, Publisher
```

👉 Explication : énumère les applications installées à partir du registre ; on évite `Win32_Product`, dont l'interrogation peut déclencher des vérifications d'installation.

Un enregistrement par poste, exporté pour rapprochement :

```powershell
[pscustomobject]@{
  Serie  = (Get-CimInstance Win32_BIOS).SerialNumber
  Nom    = $env:COMPUTERNAME
  Modele = (Get-CimInstance Win32_ComputerSystem).Model
  OS     = (Get-CimInstance Win32_OperatingSystem).Caption
  Date   = (Get-Date -Format "yyyy-MM-dd")
} | Export-Csv -Path "$env:USERPROFILE\inventaire-poste.csv" -NoTypeInformation -Encoding UTF8
```

👉 Explication : construit un objet avec les champs clés et l'écrit au format CSV ; c'est la brique de base d'un inventaire scripté (à adapter ; en production, l'agent ou l'outil dédié fait ce travail).

Côté annuaire, repérer les comptes machine inactifs (module RSAT Active Directory requis, lecture seule) :

```powershell
Get-ADComputer -Filter * -Properties OperatingSystem, LastLogonDate | Where-Object { $_.LastLogonDate -lt (Get-Date).AddDays(-90) } | Select-Object Name, OperatingSystem, LastLogonDate
```

👉 Explication : liste les ordinateurs sans connexion depuis 90 jours ; ce sont des candidats à vérifier (retirés, éteints, perdus) avant tout nettoyage, jamais à supprimer d'office.

Sous Linux, un relevé minimal :

```bash
hostnamectl && lscpu | head -n 12 && lsblk -d -o NAME,SIZE,TYPE,MODEL
```

👉 Explication : affiche nom, système et architecture, processeur, puis disques physiques ; lecture seule et sans droits élevés.

### 5.5 Qualité de l'inventaire

Désignez un **propriétaire** des données, privilégiez la mise à jour **automatique** (agent) à la saisie manuelle, rapprochez les sources chaque mois et n'enregistrez que l'utile : l'affectation à une personne est une donnée personnelle à conserver pour une durée définie.

## 6. Cycle de vie du matériel

![Cycle de vie d'un poste en six phases : acquisition, préparation, affectation, exploitation, retrait, fin de vie, avec boucle de réaffectation](images/deploiement-inventaire-1.svg)

*Figure 3 — Du bon de commande au recyclage : chaque transition met à jour l'inventaire.*

1. **Acquisition** : commande selon un catalogue standard, réception, vérification du matériel et du numéro de série, enregistrement en inventaire (état « en stock »). Si Autopilot est utilisé, enregistrement de l'appareil.
2. **Préparation** : installation (image ou approvisionnement), pilotes, chiffrement du disque, étiquetage, tests de recette.
3. **Affectation** : remise à l'utilisateur, signature d'une fiche de remise (responsabilité, charte), état « en service », mise à jour de l'inventaire.
4. **Exploitation** : correctifs, support, réparations sous garantie, suivi de l'état (batterie, disque), changements de configuration documentés.
5. **Retrait** : restitution (départ de l'agent, remplacement), vérification de l'état, récupération des données à conserver, retrait des comptes et des inscriptions (annuaire, gestion des appareils, licences).
6. **Fin de vie** : si le poste est réutilisable, **réaffectation** après **réinitialisation** ; sinon **effacement sécurisé** puis recyclage ou don par une filière agréée.

### 6.1 Effacer les données avant de sortir un poste

- Disque **chiffré** : la destruction de la clé de chiffrement (effacement cryptographique) est une méthode reconnue, à condition que le chiffrement ait été actif depuis le début.
- Sinon : **effacement** avec un outil adapté au type de support (SSD, disque magnétique), selon les recommandations de la norme **NIST SP 800-88** ; **destruction physique** si le support est défaillant ou si les données sont très sensibles.
- **Trace** : certificat d'effacement ou de destruction, date, numéro de série, opérateur.
- **Filière DEEE** : les équipements électroniques en fin de vie se confient à un organisme agréé.

### 6.2 Durée de vie

Un poste bureautique se renouvelle souvent après **trois à cinq ans** ; l'inventaire permet de planifier par vagues et d'anticiper les fins de support de l'éditeur.

## 7. Conduire un déploiement sans risque

1. Définir le périmètre (qui, combien, quelle fenêtre) ; 2. tester sur VM puis sur un **groupe pilote** représentatif ; 3. déployer **par vagues** en mesurant les incidents ; 4. prévoir le **retour arrière** (image précédente conservée, critère de déclenchement) ; 5. communiquer (date, durée, contacts) ; 6. documenter version, résultats et anomalies.

Pour toute modification sensible (changement d'image, de politique, de séquence), appliquez les garde-fous du pack : snapshot ou sauvegarde préalable, accès console de secours, test, retour arrière.

---

## Mise en pratique guidée

**Cadre** : VM Windows jetable avec **snapshot** préalable et **console hyperviseur** accessible. Aucune donnée réelle, aucun serveur de production.

### Atelier 1 — Fiche d'inventaire d'un poste

Exécutez les commandes de la section 5.4 pour construire `inventaire-poste.csv`, puis affichez le résultat :

```powershell
Import-Csv "$env:USERPROFILE\inventaire-poste.csv" | Format-List
```

👉 Explication : relit le fichier exporté pour contrôler les champs ; si un champ est vide, comprenez pourquoi (matériel virtuel, valeur absente).

### Atelier 2 — Rapprochement de deux sources

Créez deux petits CSV factices (`agent.csv` et `achats.csv`) avec les colonnes `Serie,Nom`, contenant trois à cinq lignes avec **au moins un écart** ; puis comparez :

```powershell
Compare-Object (Import-Csv .\agent.csv) (Import-Csv .\achats.csv) -Property Serie -PassThru | Select-Object Serie, Nom, SideIndicator
```

👉 Explication : affiche les numéros de série présents dans une seule source (`<=` agent seul, `=>` achats seul) ; ce sont les écarts à investiguer.

### Atelier 3 — Fichier de réponses validé

Enregistrez le XML de la section 4.3 dans `unattend.xml` et contrôlez-le avec la commande de la même section. Provoquez ensuite une erreur (supprimez une balise fermante) et constatez le message. **Retour arrière** : restaurez la balise.

### Atelier 4 — Application et retour arrière

⚠️ Installez 7-Zip avec `winget install` (section 4.4), vérifiez avec `winget list`, puis désinstallez avec la commande de retour arrière. Notez la durée et la sortie.

### Atelier 5 — Plan de déploiement sur papier

Pour une société fictive de 120 postes à renouveler, rédigez un plan d'une page : approche choisie (image ou approvisionnement) et justification, pilote, vagues, retour arrière, communication, traitement des anciens postes (effacement, recyclage).

**Retour arrière général** : restaurez le snapshot de la VM et supprimez les fichiers CSV et XML créés.

---

## Exercices

1. **Vocabulaire.** Définissez en une phrase : WIM, Sysprep, séquence de tâches, empreinte matérielle, effacement cryptographique.
2. **Choix d'image.** Une organisation met à jour ses applications métier chaque mois. Image épaisse ou mince ? Justifiez.
3. **Autopilot ou image.** Choisissez et justifiez pour : (a) 30 postes neufs livrés chez des télétravailleurs ; (b) 200 postes d'une salle de formation à réinstaller chaque trimestre, sur réseau local rapide.
4. **Script.** Qu'est-ce qui rend un script de déploiement « idempotent » ? Donnez un exemple qui ne l'est pas.
5. **Secrets.** Un collègue propose d'écrire le mot de passe d'un compte de service dans le script de premier démarrage « pour aller vite ». Quelle réponse et quelles alternatives ?
6. **Inventaire.** Un inventaire comporte 480 postes, l'annuaire 520 comptes machine, l'outil de gestion 455 appareils. Quelles conclusions provisoires et quelles actions ?
7. **Retrait.** Rédigez la liste de contrôle de retrait d'un poste restitué par un agent qui quitte l'entreprise.
8. **Plan.** Décrivez un déploiement par vagues pour un nouveau modèle de poste : critères de passage d'une vague à l'autre et déclencheurs de retour arrière.

## Corrigés des exercices

1. **WIM** : fichier d'image système, pouvant contenir plusieurs images. **Sysprep** : outil qui généralise un système avant capture. **Séquence de tâches** : suite ordonnée et conditionnelle d'étapes de déploiement. **Empreinte matérielle** : identifiant d'un appareil utilisé pour l'enregistrer dans Autopilot. **Effacement cryptographique** : rendre les données illisibles en détruisant la clé de chiffrement.
2. Image **mince ou hybride** : refaire une image épaisse chaque mois est lourd ; les applications se déploient séparément, par le gestionnaire de paquets ou l'outil de gestion.
3. (a) Autopilot/Intune : appareils neufs, utilisateurs distants, pas de réseau interne. (b) Image ou réinitialisation par séquence de tâches : même configuration répétée, réseau local rapide, contrôle total du contenu.
4. Idempotent : le résultat reste identique si on rejoue le script (il vérifie l'état avant d'agir). Contre-exemple : un script qui ajoute à chaque exécution la même ligne à un fichier ou crée un compte sans tester s'il existe.
5. Refuser : un secret en clair se copie, se retrouve dans l'image, dans les journaux et dans les sauvegardes. Alternatives : coffre de secrets, identité gérée du poste ou jeton à durée limitée, compte à privilèges minimaux, injection au déploiement par l'outil de gestion.
6. Écarts : 40 comptes machine sans poste inventorié (comptes obsolètes ou postes non gérés), 25 postes inventoriés absents de la gestion des appareils (non inscrits, hors parc ?). Actions : rapprocher par numéro de série, vérifier les inactifs depuis 90 jours avant nettoyage, inscrire ou documenter les exceptions.
7. Récupérer le poste et les accessoires ; vérifier l'état ; sauvegarder les données à conserver avec l'accord du responsable ; retirer les comptes et inscriptions ; récupérer ou réattribuer les licences ; réinitialiser ou effacer ; mettre à jour l'inventaire (état, date) ; tracer l'effacement.
8. Pilote de 5 à 10 % représentatif, mesure des incidents, passage à la vague suivante si le taux d'incidents reste sous un seuil défini et si les retours sont bons. Retour arrière déclenché par un taux d'échec dépassant le seuil, un incident de sécurité ou un défaut bloquant ; image précédente conservée.

## Quiz

**Q1. Que contient une image « mince » ?**
A. Système + toutes les applications. B. Système à jour, quasi nu, avec applications ajoutées ensuite. C. Uniquement les pilotes. D. Les données utilisateur.
**Réponse : B.** L'image mince reste stable et se complète au déploiement.

**Q2. À quoi sert Sysprep ?**
A. À sauvegarder les données. B. À généraliser un système avant capture. C. À installer des pilotes. D. À joindre le domaine.
**Réponse : B.** Il retire les éléments propres à la machine avant la capture de l'image.

**Q3. Que fait WDS dans la chaîne classique ?**
A. Il inventorie les logiciels. B. Il répond au démarrage réseau (PXE) et fournit une image de démarrage. C. Il gère les licences. D. Il efface les disques.
**Réponse : B.** MDT ajoute ensuite la séquence de tâches.

**Q4. Autopilot est surtout adapté :**
A. Aux serveurs. B. Aux appareils neufs ou réinitialisés qui se configurent au premier démarrage depuis le service. C. Aux imprimantes. D. Aux sauvegardes.
**Réponse : B.** L'appareil enregistré se rattache à l'organisation à la première connexion.

**Q5. Qu'est-ce qu'un script idempotent ?**
A. Un script très rapide. B. Un script dont les exécutions répétées donnent le même résultat. C. Un script sans journal. D. Un script chiffré.
**Réponse : B.** Il vérifie l'état avant d'agir.

**Q6. Quel est le meilleur identifiant stable d'un poste pour rapprocher des sources ?**
A. Le nom d'hôte. B. Le numéro de série. C. L'adresse IP. D. Le nom de l'utilisateur.
**Réponse : B.** Le nom, l'IP et l'utilisateur changent ; le numéro de série reste.

**Q7. Pourquoi éviter `Win32_Product` pour l'inventaire logiciel ?**
A. Il n'existe pas. B. Son interrogation peut déclencher des vérifications d'installation et est lente. C. Il efface les logiciels. D. Il exige Internet.
**Réponse : B.** On préfère les clés de registre de désinstallation ou un agent dédié.

**Q8. Un poste connu de l'annuaire mais d'aucune autre source est :**
A. Normal. B. Suspect : compte obsolète ou machine non gérée à vérifier. C. À supprimer immédiatement. D. Un serveur.
**Réponse : B.** On vérifie d'abord ; on ne supprime pas d'office.

**Q9. Quelle est une méthode d'effacement reconnue pour un disque chiffré dès l'origine ?**
A. Supprimer les fichiers. B. Détruire la clé de chiffrement (effacement cryptographique). C. Formater rapidement. D. Renommer le volume.
**Réponse : B.** Les données deviennent illisibles ; les autres méthodes laissent des données récupérables.

**Q10. Quelle précaution avant de modifier une image de déploiement en production ?**
A. Aucune. B. Tests sur VM puis pilote, snapshot ou sauvegarde, accès de secours, retour arrière. C. Diffusion générale immédiate. D. Suppression de l'ancienne image.
**Réponse : B.** On conserve l'image précédente et on déploie progressivement.

## Erreurs fréquentes et dépannage

| Erreur | Conséquence | Remède |
|---|---|---|
| Secret dans un script | Fuite de mot de passe | Coffre, identité du poste, privilèges minimaux |
| Pas de retour arrière | Parc bloqué après une mauvaise diffusion | Image précédente conservée, pilote, vagues |
| Inventaire tenu à la main | Données fausses | Agent et rapprochement automatique |
| Suppression d'office des comptes inactifs | Perte de postes éteints mais légitimes | Vérification d'abord, mise en quarantaine, puis nettoyage |
| Poste sorti sans effacement | Fuite de données | Effacement tracé, filière agréée |

**Si le déploiement échoue** : lire le journal de la séquence ou du script, rejouer sur une VM, comparer avec un poste réussi, et ne corriger qu'une chose à la fois (voir la leçon [Méthode de dépannage structurée](/fr/00-cours-theoriques/tout-en-un/08-support-et-gestion-de-service/lecons/lecon-methode-depannage)).

## À retenir

- Standardiser, c'est produire des postes **reproductibles, traçables et sûrs**.
- Image **mince ou hybride** plutôt qu'épaisse ; pilotes par modèle ; image versionnée.
- Image classique (WDS/MDT) et approvisionnement moderne (Autopilot/Intune) répondent à des contextes différents ; vérifiez l'état officiel des outils.
- Scripts **idempotents, journalisés, sans secret**, testés en VM.
- Inventaire : **numéro de série**, plusieurs sources rapprochées, propriétaire des données.
- Cycle de vie : acquisition, préparation, affectation, exploitation, retrait, fin de vie avec **effacement tracé**.

## Pour aller plus loin

- Documentation Microsoft sur Windows Autopilot : <https://learn.microsoft.com/autopilot/>
- Documentation Microsoft Intune : <https://learn.microsoft.com/intune/>
- Référence DISM : <https://learn.microsoft.com/windows-hardware/manufacture/desktop/what-is-dism>
- NIST SP 800-88 (assainissement des supports) : <https://csrc.nist.gov/pubs/sp/800/88/r1/final>
- RFC 5737 (adresses de documentation) : <https://www.rfc-editor.org/rfc/rfc5737>

## Crédits des images

| Fichier | Source (URL Commons) | Auteur | Licence (nom + URL) | Modifications |
|---|---|---|---|---|
| `images/deploiement-inventaire-1.svg` | Création originale (aucune source externe) | Projet Pack Master | CC0 1.0 — <https://creativecommons.org/publicdomain/zero/1.0/> | Sans objet |
| `images/deploiement-inventaire-2.svg` | Création originale (aucune source externe) | Projet Pack Master | CC0 1.0 — <https://creativecommons.org/publicdomain/zero/1.0/> | Sans objet |
| `images/deploiement-inventaire-3.svg` | Création originale (aucune source externe) | Projet Pack Master | CC0 1.0 — <https://creativecommons.org/publicdomain/zero/1.0/> | Sans objet |

Création originale du projet Pack Master, dédiée au domaine public (CC0). Aucune image Commons retenue : l'API de Commons renvoyait HTTP 429 lors de la recherche.

## Historique de vérification

| Date | OS/logiciel | Testeur | Verdict |
|---|---|---|---|
| 2026-11-01 | Windows 10/11, PowerShell 5.1/7, winget | Rédaction assistée (Copilot) | Non testé sur plateforme cible |