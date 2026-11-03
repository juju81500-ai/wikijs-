---
title: "Leçon — Active Directory Domain Services : domaine, forêt, DNS, Kerberos et sites"
description: "À la fin de cette leçon, vous saurez :"
published: true
date: 2026-11-03T14:22:28Z
tags: ["transverse", "tout-en-un", "lecon", "identites", "active-directory", "kerberos", "dns", "windows-server"]
editor: markdown
dateCreated: 2026-11-03T14:22:28Z
dateModified: 2026-11-03T14:22:28Z
---

# Leçon — Active Directory Domain Services : domaine, forêt, DNS, Kerberos et sites

- **Tags** : `transverse`, `tout-en-un`, `lecon`, `identites`, `active-directory`, `kerberos`, `dns`, `windows-server`
- **Niveau** : Débutant à intermédiaire ([[Glossary:TSSR]] / administrateur systèmes)
- **Durée estimée** : 3 h 30 (lecture 1 h 15, laboratoire 1 h 30, exercices et quiz 45 min)

---

## Objectifs pédagogiques

À la fin de cette leçon, vous saurez :

1. expliquer ce qu'apporte Active Directory Domain Services ([[Glossary:AD]] DS) par rapport à des comptes locaux dispersés ;
2. distinguer **domaine**, **arbre**, **forêt**, **contrôleur de domaine** et **catalogue global** ;
3. décrire le rôle du **[[Glossary:DNS]]** et vérifier qu'un contrôleur est annoncé aux clients ;
4. raconter un échange **Kerberos**, puis dire quand **[[Glossary:NTLM]]** prend le relais ;
5. lire un [[Glossary:DN]] [[Glossary:LDAP]] et comprendre le **schéma** ;
6. concevoir des **[[Glossary:OU]]** raisonnables et modéliser des **sites** ;
7. monter un laboratoire jetable et lancer des diagnostics en lecture seule.

## Prérequis et durée

- Notions de réseau [[Glossary:IP]], de DNS et de ports [[Glossary:TCP]]/UDP ; usage de PowerShell.
- Pour le laboratoire : un hyperviseur, une [[Glossary:VM]] Windows Server et une VM cliente Windows sur un réseau **isolé**, en versions d'évaluation officielles, détruisibles.
- Durée : environ 3 h 30 (lecture 1 h 15, laboratoire 1 h 30, exercices et quiz 45 min).

Les adresses appartiennent aux plages de documentation (192.0.2.0/24, 198.51.100.0/24), le domaine est `example.test`, et aucun mot de passe n'apparaît : les secrets sont saisis de façon interactive.

## L'essentiel en bref

- AD DS = **annuaire** d'objets + **authentification** (Kerberos, NTLM) + **administration** ([[Glossary:GPO]], étudiées dans une autre leçon).
- **Domaine** = frontière de réplication et d'administration ; **forêt** = frontière de sécurité, schéma unique.
- Un **contrôleur de domaine** ([[Glossary:DC]]) héberge la base `NTDS.dit` ; les DC se répliquent entre eux, sauf quelques rôles uniques ([[Glossary:FSMO]]).
- **Sans DNS correct, AD ne fonctionne pas** : les clients trouvent les DC par des enregistrements SRV.
- **Kerberos** repose sur des tickets et une heure cohérente (5 minutes de tolérance) ; **NTLM** est un secours plus ancien.
- Les **OU** servent à déléguer et à appliquer des GPO ; les **sites** décrivent la topologie réseau.

---

## 1. Pourquoi un annuaire ? L'analogie de la mairie

Imaginez une entreprise de 60 personnes avec 60 PC. Sans annuaire, chaque PC garde sa propre liste de comptes : quand Alice change de mot de passe, il faut le changer partout ; quand Bruno quitte l'entreprise, il faut penser à le supprimer sur chaque machine. C'est comme si chaque service possédait son propre registre papier de personnel.

Un annuaire centralise cette liste, comme **le registre d'état civil d'une mairie** : une seule source de vérité. AD DS remplit trois fonctions : **annuaire** (qui existe ?), **authentification** (cette personne est-elle bien celle qu'elle prétend ?) et **administration** (quelles règles s'appliquent à elle et à sa machine ?).

Le protocole d'accès à l'annuaire est **LDAP** (Lightweight Directory Access Protocol, RFC 4511). L'authentification s'appuie sur **Kerberos version 5** (RFC 4120) et, à défaut, sur **NTLM**. Le tout repose sur le **DNS** pour la localisation des services.

## 2. Domaine, arbre, forêt : emboîter les frontières

![Schéma montrant une forêt contenant deux domaines distincts, chacun représenté par un triangle parent avec deux triangles enfants](images/active-directory-ds-1.png)

*Une forêt (cadre orange) regroupant deux arbres de domaines indépendants. Les triangles symbolisent des domaines selon la notation habituelle d'AD. Les noms de domaine affichés sur l'image d'origine (acme.com.tw, contoso.com.tw) sont des exemples du schéma original ; dans la leçon, nous utilisons example.test.*

### 2.1 Le domaine

Le **domaine** est l'unité de base : objets partageant la même base, la même politique de mots de passe par défaut et le même espace de noms DNS (`example.test`). C'est la limite de **réplication**. Analogie : une **commune**, avec ses habitants et ses règles locales.

### 2.2 L'arbre

Un **arbre** est une suite de domaines qui partagent un espace de noms DNS contigu : `example.test` (racine), `paris.example.test`, `lyon.example.test`. Entre un parent et ses enfants existent des **approbations transitives bidirectionnelles** créées automatiquement.

![Un domaine racine au sommet relié à trois domaines enfants nommés sales, engineering et admin](images/active-directory-ds-2.png)

*Un arbre de domaines : un domaine racine et trois sous-domaines qui prolongent son nom DNS. Même remarque sur les noms d'exemple de l'image d'origine.*

### 2.3 La forêt

Une **forêt** regroupe un ou plusieurs arbres qui partagent :

- le **schéma** (la définition des types d'objets et de leurs attributs) ;
- la **partition de configuration** (topologie, sites, services) ;
- le **catalogue global** (index partiel de tous les objets de la forêt).

La forêt est la **véritable frontière de sécurité** : un administrateur d'un domaine enfant peut, dans certaines conditions, compromettre le reste de la forêt. Si deux structures ne se font pas confiance, on crée deux forêts distinctes et, au besoin, une approbation de forêt.

Règle pratique pour un petit établissement : **une forêt, un domaine**.

## 3. Les contrôleurs de domaine

Un **contrôleur de domaine** est un serveur Windows sur lequel le rôle AD DS est installé et promu. Il héberge :

- la base d'annuaire `NTDS.dit` (dossier `C:\Windows\NTDS` par défaut) ;
- le dossier partagé **[[Glossary:SYSVOL]]** (scripts et GPO, réplication par DFSR) ;
- les services Kerberos (KDC), LDAP, DNS (souvent), le service d'horloge Windows (W32Time).

### 3.1 Réplication multi-maître

Toute modification faite sur un DC est répliquée vers les autres : tous les DC acceptent les écritures. En cas de conflit sur un même attribut, la dernière écriture gagne.

### 3.2 Les rôles FSMO

Quelques opérations sont confiées à un seul DC à la fois (**FSMO**) :

| Rôle | Portée | Rôle en une phrase |
| --- | --- | --- |
| Maître de schéma | Forêt | Autorise les modifications du schéma |
| Maître de nommage de domaine | Forêt | Ajoute ou retire des domaines de la forêt |
| Émulateur PDC | Domaine | Référence de l'heure, verrouillages, changements de mot de passe urgents |
| Maître RID | Domaine | Distribue des plages d'identifiants relatifs (RID) pour créer des [[Glossary:SID]] |
| Maître d'infrastructure | Domaine | Maintient les références inter-domaines |

Dans un petit domaine, tous ces rôles résident souvent sur le premier DC.

### 3.3 Catalogue global (GC)

Un **catalogue global** détient, en plus de sa partition de domaine, une copie **partielle en lecture seule** des objets de tous les domaines de la forêt (ports 3268/3269). Il sert à l'ouverture de session et aux recherches dans toute la forêt. En production, prévoyez **au moins deux DC** : un seul est une panne annoncée.

## 4. Le DNS, colonne vertébrale d'AD

C'est la règle numéro un des dépannages AD : **« c'est toujours le DNS »**. Voici pourquoi.

Un client ne connaît pas l'adresse des DC. Il interroge le DNS pour trouver des **enregistrements SRV**, qui indiquent « tel service est offert par tel serveur, tel port ». Les enregistrements sont créés automatiquement par le service **Netlogon** de chaque DC dans la zone `_msdcs`, par exemple :

- `_ldap._tcp.dc._msdcs.example.test` : les DC du domaine, pour LDAP ;
- `_kerberos._tcp.dc._msdcs.example.test` : les serveurs Kerberos ;
- `_ldap._tcp.<NomDuSite>._sites.dc._msdcs.example.test` : les DC d'un site donné.

Analogie : le DNS est l'**annuaire téléphonique du bâtiment** ; les enregistrements SRV sont les lignes « standard — poste 8 » qui orientent les visiteurs vers le bon guichet.

### 4.1 Bonnes pratiques DNS

1. Les membres du domaine n'ont pour DNS que les **DC** : jamais de DNS public en secondaire, sous peine de ne plus retrouver les SRV.
2. Utilisez un nom que vous **maîtrisez** (`ad.example.com`), pas `.local` (réservé à mDNS). En laboratoire, `example.test` (réservé aux tests par la RFC 6761) convient.
3. Les zones AD-intégrées se répliquent avec l'annuaire.

### 4.2 Vérifier sans rien modifier

```powershell
Resolve-DnsName -Name _ldap._tcp.dc._msdcs.example.test -Type SRV -Server 192.0.2.10
```

👉 Explication : interroge le serveur DNS 192.0.2.10 pour lister les contrôleurs de domaine annoncés ; lecture seule. Chaque ligne donne le nom d'hôte, le port (389) et la priorité.

```bash
dig +short SRV _ldap._tcp.dc._msdcs.example.test @192.0.2.10
```

👉 Explication : même vérification depuis un poste Linux avec `dig` ; si la réponse est vide, le DNS que le client utilise ne connaît pas la zone du domaine.

## 5. Authentification : Kerberos, puis NTLM

### 5.1 L'analogie du parc d'attractions

À l'entrée, vous montrez votre pièce d'identité et recevez un **bracelet** valable la journée (le **TGT**). À chaque attraction, un guichet vous remet un **coupon** (le **ticket de service**, ST) en échange du bracelet. L'opérateur vérifie le coupon : il n'a jamais besoin de connaître votre mot de passe.

### 5.2 Les acteurs

Le **KDC** (Key Distribution Center) tourne sur chaque DC et comprend deux services logiques : l'**AS** (Authentication Service) et le **TGS** (Ticket-Granting Service). Le compte spécial `krbtgt` détient la clé secrète qui signe tous les TGT du domaine.

![Schéma du protocole Kerberos : client, serveur d'authentification, serveur d'octroi de tickets et serveur de service avec les messages A à H](images/active-directory-ds-3.svg)

*Échanges Kerberos : le client s'authentifie auprès de l'AS (messages A et B), reçoit un TGT, demande un ticket de service au TGS (messages C à F), puis présente ce ticket au serveur de service (messages E, G, H). Légende de l'image d'origine en anglais : « Client Authentication to the AS » = authentification du client auprès de l'AS ; « Client Service Authorization » = autorisation de service ; « Client Service Request » = requête de service ; « Ticket granting ticket » = TGT.*

### 5.3 Les trois temps, en français

1. **AS-REQ / AS-REP** : le client envoie son identité et une preuve chiffrée avec une clé dérivée de son mot de passe (pré-authentification). Le KDC répond avec un **TGT** et une clé de session. Le client déchiffre la clé de session sans jamais transmettre son mot de passe.
2. **TGS-REQ / TGS-REP** : pour accéder au partage `\\SRV-FICHIERS\Compta`, le client présente son TGT et le **nom principal de service** (SPN, par exemple `cifs/SRV-FICHIERS.example.test`). Le KDC renvoie un **ticket de service** chiffré avec la clé du serveur cible.
3. **AP-REQ / AP-REP** : le client présente le ticket au serveur, qui le déchiffre avec sa propre clé. S'il y parvient, c'est que le KDC l'a émis. Le serveur n'a pas eu à contacter le KDC.

### 5.4 Points d'attention Kerberos

- **L'heure** : les tickets contiennent des horodatages. Au-delà de 5 minutes d'écart (valeur par défaut), l'authentification échoue. Dans un domaine, la hiérarchie W32Time synchronise les membres sur leur DC, et l'émulateur PDC de la racine de forêt est la référence.
- **Les noms** : Kerberos construit un SPN à partir d'un nom ; un accès par adresse IP (`\\192.0.2.20\Compta`) n'en permet pas.
- **Le compte `krbtgt`** signe tous les TGT ; son renouvellement est une opération d'exploitation avancée, à ne pas tenter sans procédure.

### 5.5 NTLM : le plan B

**NTLM** est un protocole défi-réponse plus ancien : le serveur envoie un défi aléatoire, le client le chiffre avec le condensat de son mot de passe, et le serveur fait vérifier la réponse par un DC. Il est utilisé quand Kerberos n'est pas possible : accès par adresse IP, serveur hors domaine, application ancienne, client qui ne trouve pas de DC.

Pourquoi limiter NTLM ? Il n'authentifie pas le serveur, il est plus exposé au rejeu et au craquage hors ligne. On **mesure** son usage avant de le restreindre.

### 5.6 Visualiser ses tickets

```powershell
klist
```

👉 Explication : affiche les tickets Kerberos de la session courante (TGT dans `krbtgt/EXAMPLE.TEST`, tickets de service `cifs/...`). Lecture seule.


## 6. Le schéma et les objets

### 6.1 Classes et attributs

Le **schéma** est le « plan de la base » : il liste les **classes** d'objets (`user`, `computer`, `group`, `organizationalUnit`…) et les **attributs** que ces classes peuvent porter (`sAMAccountName`, `mail`, `memberOf`…). Chaque attribut a une syntaxe (chaîne, entier, SID…) et peut être indexé ou répliqué dans le catalogue global.

Analogie : le schéma, c'est le **formulaire vierge** (les cases possibles) ; un objet, c'est le formulaire rempli.

Le schéma est **commun à la forêt** et on ne peut qu'y ajouter (ou désactiver) des éléments : toute extension se teste d'abord en laboratoire.

### 6.2 Identifier un objet

Un objet possède plusieurs identités :

| Identité | Exemple | Usage |
| --- | --- | --- |
| DN (Distinguished Name) | `CN=Alice Martin,OU=Utilisateurs,OU=Entreprise,DC=example,DC=test` | Chemin complet dans l'arbre ; change si l'objet est déplacé ou renommé |
| objectGUID / objectSid | GUID 128 bits ; `S-1-5-21-…-1105` | Identifiants immuables ; le SID sert dans les listes d'accès |
| sAMAccountName | `alice.martin` | Nom de connexion « ancien format » (`EXAMPLE\alice.martin`) |
| userPrincipalName (UPN) | `alice.martin@example.test` | Nom de connexion « moderne » |

Composants du DN : `DC` (domain component), `OU` (unité d'organisation), `CN` (nom commun).

### 6.3 Lire l'annuaire

```powershell
Get-ADDomain | Select-Object DNSRoot, NetBIOSName, DomainMode, PDCEmulator
```

👉 Explication : affiche les caractéristiques principales du domaine (nom DNS, nom NetBIOS, niveau fonctionnel, détenteur du rôle d'émulateur PDC) ; nécessite le module `ActiveDirectory`, lecture seule.


## 7. Unités d'organisation (OU) et conteneurs

Une **OU** est un conteneur d'objets que l'on peut **déléguer** et auquel on peut **lier des GPO**. Elle s'oppose aux conteneurs par défaut (`CN=Users`, `CN=Computers`) auxquels on ne peut pas lier de GPO.

Deux usages justifient une OU : **appliquer des GPO différentes** à des populations différentes, et **déléguer** l'administration d'un périmètre.

### 7.1 Une arborescence simple et durable

```text
example.test
└── OU=Entreprise
    ├── OU=Utilisateurs
    │   ├── OU=Comptabilite
    │   └── OU=Direction
    ├── OU=Postes
    │   ├── OU=Fixes
    │   └── OU=Portables
    ├── OU=Serveurs
    ├── OU=Groupes
    └── OU=Comptes-de-service
```

Conseils : séparer **utilisateurs** et **ordinateurs** ; choisir des critères **stables** plutôt que l'organigramme ; limiter à 3 ou 4 niveaux ; protéger chaque OU contre la suppression accidentelle ; rediriger les nouveaux ordinateurs vers `OU=Postes` avec `redircmp`.


## 8. Les sites : décrire le réseau physique

Les **sites** ne sont pas des domaines : ils décrivent la **topologie du réseau**. Un site est un ensemble de sous-réseaux IP bien connectés (typiquement un bâtiment ou un campus).

![Schéma à deux colonnes : à gauche la hiérarchie logique forêt, domaine, OU ; à droite deux sites géographiques reliés par un lien de site et hébergeant trois contrôleurs de domaine](images/active-directory-ds-4.svg)

*Structure logique (forêt, domaine, OU) et structure physique (sites, sous-réseaux, contrôleurs, lien de site) : deux dimensions indépendantes. Création originale du projet Pack Master.*

### 8.1 À quoi servent les sites ?

- **Localisation des DC** : le client déduit son site de son adresse IP (sous-réseau déclaré) et s'adresse en priorité aux DC de son site, ce qui évite de traverser un lien lent.
- **Réplication** : entre sites, elle est **planifiée** et compressée (intervalle par défaut : 180 minutes) ; dans un site, elle est quasi immédiate.

### 8.2 Les objets de topologie

Un **site** regroupe des sous-réseaux et des DC ; un **sous-réseau** associe une plage IP à un site ; un **lien de site** relie des sites et porte un coût ; le **KCC** calcule automatiquement les connexions de réplication. Erreur classique : oublier de déclarer un sous-réseau, ce qui envoie parfois les clients vers un DC lointain.

### 8.3 Interroger les sites

```powershell
Get-ADReplicationSite -Filter * | Select-Object Name
Get-ADReplicationSubnet -Filter * | Select-Object Name, Site
```

👉 Explication : liste les sites et les sous-réseaux qui leur sont associés ; lecture seule.

```cmd
nltest /dsgetsite
```

👉 Explication : indique le site AD déduit pour la machine courante.

---

## Mise en pratique guidée

**Objectif** : monter un domaine `example.test` dans un laboratoire jetable, puis relever l'état du domaine avec des commandes de lecture.

**Matériel** : deux VM sur un réseau interne `192.0.2.0/24` — `SRV-DC01` (Windows Server, 192.0.2.10) et `PC-W11-01` (Windows, 192.0.2.50). Utilisez des images d'évaluation officielles. Faites un **instantané** avant chaque grande étape.

> Les commandes ci-dessous sont indiquées à titre pédagogique. Elles n'ont pas été exécutées pour rédiger cette leçon (voir l'historique de vérification). Ne les lancez **jamais** sur un serveur de production.

### Étape 1 — Nommer et adresser le futur DC

```powershell
Rename-Computer -NewName SRV-DC01 -Restart
```

👉 Explication : donne au serveur son nom définitif **avant** la promotion (le renommer après est possible mais déconseillé) ; redémarre la VM.

```powershell
New-NetIPAddress -InterfaceAlias "Ethernet" -IPAddress 192.0.2.10 -PrefixLength 24
Set-DnsClientServerAddress -InterfaceAlias "Ethernet" -ServerAddresses 127.0.0.1
```

👉 Explication : fixe une adresse IPv4 statique dans la plage de documentation et indique le DC lui-même comme DNS. Adaptez `Ethernet` au nom réel de l'interface (`Get-NetAdapter`).

### Étape 2 — Installer le rôle et promouvoir le DC

```powershell
Install-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools
```

👉 Explication : installe les binaires du rôle AD DS et les outils d'administration ; ne crée pas encore de domaine.

```powershell
Install-ADDSForest -DomainName "example.test" -DomainNetbiosName "EXAMPLE" -InstallDns -SafeModeAdministratorPassword (Read-Host -AsSecureString "Mot de passe DSRM")
```

👉 Explication : crée une nouvelle forêt et un premier domaine, installe le DNS et demande interactivement le mot de passe du mode de restauration des services d'annuaire ([[Glossary:DSRM]]). Le serveur redémarre à la fin. Choisissez un secret de laboratoire, jamais réutilisé ailleurs.

### Étape 3 — Vérifier l'état du DC (lecture seule)

```powershell
Get-ADForest | Select-Object Name, ForestMode, SchemaMaster, DomainNamingMaster, GlobalCatalogs
Get-ADDomain | Select-Object DNSRoot, PDCEmulator, RIDMaster, InfrastructureMaster
```

👉 Explication : affiche la forêt, les rôles FSMO et la liste des catalogues globaux. Dans ce laboratoire, tous les rôles doivent désigner `SRV-DC01.example.test`.

```powershell
dcdiag /test:dns /test:replications /v
```

👉 Explication : exécute les tests de diagnostic DNS et de réplication du contrôleur ; sortie très détaillée, lecture seule. Les tests échouent en cas d'erreur DNS, ce qui oriente vers la cause.

### Étape 4 — Créer une structure d'OU

```powershell
New-ADOrganizationalUnit -Name "Entreprise" -Path "DC=example,DC=test" -ProtectedFromAccidentalDeletion $true
foreach ($ou in "Utilisateurs","Postes","Serveurs","Groupes","Comptes-de-service") {
  New-ADOrganizationalUnit -Name $ou -Path "OU=Entreprise,DC=example,DC=test" -ProtectedFromAccidentalDeletion $true
}
```

👉 Explication : crée l'OU racine puis ses cinq sous-OU, toutes protégées contre la suppression accidentelle. Les commandes modifient l'annuaire du laboratoire ; ne les relancez pas sans vérifier : un nom en double produit une erreur sans conséquence.

### Étape 5 — Joindre le client et observer Kerberos

Sur `PC-W11-01`, réglez le DNS sur `192.0.2.10`, puis :

```powershell
Add-Computer -DomainName example.test -Credential EXAMPLE\Administrateur -Restart
```

👉 Explication : joint le poste au domaine après avoir demandé le mot de passe de l'administrateur du laboratoire, puis redémarre.

Après une connexion avec un compte de domaine, exécutez `klist`, puis ouvrez `\\SRV-DC01\SYSVOL` et relancez `klist` : un ticket `cifs/SRV-DC01.example.test` doit apparaître. Avec `\\192.0.2.10\SYSVOL`, aucun nouveau ticket : NTLM a servi.

### Étape 6 — Nettoyer

Restaurez l'instantané ou supprimez les deux VM.

---

## Exercices

1. **(Vocabulaire)** Associez : domaine, forêt, OU, site, GC ↔ « frontière de sécurité », « conteneur délégable », « index partiel de toute la forêt », « sous-réseaux bien reliés », « frontière de réplication ».
2. **(Lecture de DN)** Dans `CN=Bruno Durand,OU=Comptabilite,OU=Utilisateurs,OU=Entreprise,DC=example,DC=test`, donnez le domaine DNS, l'OU directe et le nom commun.
3. **(DNS)** Écrivez les deux commandes (une Windows, une Linux) qui listent les DC annoncés pour `example.test` auprès du DNS `192.0.2.10`.
4. **(Kerberos)** Un utilisateur accède à `\\SRV-FICHIERS\Compta`, puis à `\\192.0.2.20\Compta`. Dans quel cas Kerberos est-il utilisé ? Justifiez.
5. **(Heure)** Une VM Windows jointe au domaine a une heure en retard de 12 minutes ; l'ouverture de session échoue avec une erreur d'authentification. Donnez deux contrôles et une action corrective raisonnable.
6. **(Conception)** Une PME de 80 postes, deux sites (Paris, Lyon), veut AD. Proposez : nombre de forêts/domaines, nombre minimal de DC, sites et sous-réseaux (utilisez 192.0.2.0/24 et 198.51.100.0/24), et une arborescence d'OU à 3 niveaux maximum.
7. **(Sites)** Les utilisateurs de Lyon sont lents à l'ouverture de session. Listez trois causes possibles liées à la topologie AD et la commande qui vérifie la première.
## Corrigés des exercices

1. Domaine = frontière de réplication ; forêt = frontière de sécurité ; OU = conteneur délégable ; site = sous-réseaux bien reliés ; GC = index partiel de toute la forêt.
2. Domaine : `example.test` ; OU directe : `Comptabilite` (puis `Utilisateurs` et `Entreprise` plus haut) ; nom commun : `Bruno Durand`.
3. Windows : `Resolve-DnsName -Name _ldap._tcp.dc._msdcs.example.test -Type SRV -Server 192.0.2.10`. Linux : `dig +short SRV _ldap._tcp.dc._msdcs.example.test @192.0.2.10`.
4. Kerberos est utilisé pour `\\SRV-FICHIERS\Compta`, car un nom permet de construire le SPN `cifs/SRV-FICHIERS`. L'accès par adresse IP ne permet pas de SPN : le système bascule sur NTLM (ou échoue si NTLM est bloqué).
5. Contrôles : `klist` (heures du TGT) et `w32tm /query /status` (source et décalage). Action : corriger la source de temps puis `w32tm /resync` ; vérifier que l'hyperviseur n'impose pas une synchronisation d'horloge contradictoire.
6. Une forêt, un domaine ; deux DC au moins (un par site) ; `Site-Paris` (192.0.2.0/24) et `Site-Lyon` (198.51.100.0/24) reliés par un lien de site ; OU : `Entreprise` → `Utilisateurs` / `Postes` / `Serveurs` / `Groupes` / `Comptes-de-service`.
7. Sous-réseau de Lyon non déclaré ou mal rattaché ; aucun DC joignable à Lyon ; DNS de Lyon pointant vers un DC parisien. Vérification : `nltest /dsgetsite` puis `nltest /dsgetdc:example.test`.

## Quiz

**Q1.** Quelle est la vraie frontière de sécurité dans AD ? A) Le domaine — B) La forêt — C) L'OU — D) Le site

**Q2.** Quel protocole interroge l'annuaire ? A) SMB — B) LDAP — C) [[Glossary:SNMP]] — D) [[Glossary:NTP]]

**Q3.** Un client ne trouve plus de DC. Cause la plus vraisemblable ? A) Fond d'écran — B) DNS client ne connaissant pas la zone du domaine — C) Impression bloquée — D) Navigateur obsolète

**Q4.** Que prouve le TGT ? A) Le mot de passe en clair — B) L'authentification initiale auprès du KDC — C) La liste des GPO — D) Le schéma

**Q5.** Écart d'horloge toléré par défaut par Kerberos ? A) 5 secondes — B) 5 minutes — C) 5 heures — D) 5 jours

**Q6.** Pourquoi un accès par adresse IP bascule-t-il vers NTLM ? A) L'IP est chiffrée — B) Il n'existe pas de SPN pour une IP — C) SMB ignore Kerberos — D) Le DNS est coupé

**Q7.** Rôles FSMO : A) Répartis sur tous les DC — B) Chacun tenu par un seul DC à la fois — C) Obsolètes — D) Réservés au GC

**Q8.** OU et `CN=Users` : A) Identiques — B) On lie des GPO à une OU, pas à `CN=Users` — C) Les OU stockent le DNS — D) Les conteneurs sont plus rapides

**Q9.** Rôle des sites AD ? A) Créer des domaines — B) Décrire la topologie pour localiser les DC et planifier la réplication — C) Gérer les licences — D) Limiter l'accès aux partages

**Q10.** Pourquoi deux DC en production ? A) Doubler le schéma — B) Éviter qu'une panne unique bloque les authentifications — C) Exigence de l'installeur — D) Avoir deux forêts

### Réponses justifiées

1. **B** — Les administrateurs d'un domaine peuvent affecter les autres domaines de la forêt ; seule la forêt isole réellement.
2. **B** — LDAP (389/636) est le protocole d'annuaire ; SMB sert aux fichiers, SNMP à la supervision, NTP à l'heure.
3. **B** — Les DC sont localisés par des enregistrements SRV du DNS ; un DNS qui ne connaît pas la zone n'en renvoie aucun.
4. **B** — Le TGT atteste l'authentification initiale et permet de demander des tickets de service sans renvoyer le mot de passe.
5. **B** — Tolérance par défaut de 5 minutes ; au-delà, les horodatages sont refusés.
6. **B** — Kerberos exige un SPN, lié à un nom ; une adresse IP n'en a pas.
7. **B** — Chaque rôle n'a qu'un titulaire, déplaçable par transfert.
8. **B** — Les conteneurs par défaut n'acceptent pas de lien de GPO.
9. **B** — Les sites guident la localisation et la réplication inter-sites, rien de plus.
10. **B** — La redondance supprime le point de défaillance unique.

## Erreurs fréquentes et dépannage

| Symptôme | Cause probable | Vérification (lecture seule) | Action |
| --- | --- | --- | --- |
| « Domaine introuvable » à la jonction | Le client n'utilise pas le DNS du DC | `Get-DnsClientServerAddress`, `Resolve-DnsName _ldap._tcp.dc._msdcs.example.test -Type SRV` | Pointer le DNS du client vers le DC |
| Kerberos échoue, NTLM passe | Écart d'heure, SPN absent ou dupliqué, accès par IP | `klist`, `w32tm /query /status`, `setspn -L SRV-FICHIERS` | Corriger l'heure, utiliser le [[Glossary:FQDN]], supprimer le doublon de SPN |
| Ouverture de session lente | Sous-réseau non déclaré, DC lointain | `nltest /dsgetsite`, `nltest /dsgetdc:example.test` | Déclarer le sous-réseau, ajouter un DC local |
| Réplication en erreur | DNS, pare-feu, heure, SYSVOL | `repadmin /replsummary`, `dcdiag /test:replications` | Traiter d'abord la cause réseau ou DNS |

Ordre de dépannage : **réseau → DNS → heure → ports → journaux d'événements**.

## À retenir

- AD DS = annuaire + authentification + administration centralisée.
- Domaine = réplication ; forêt = sécurité et schéma commun ; arbre = espace de noms contigu.
- Un DC héberge `NTDS.dit` et SYSVOL ; réplication multi-maître, cinq rôles FSMO à titulaire unique.
- Le DNS est indispensable : enregistrements SRV `_ldap._tcp.dc._msdcs.<domaine>`.
- Kerberos : TGT, ticket de service, SPN, heure cohérente (5 minutes). NTLM : secours à surveiller.
- Schéma : classes et attributs, extension irréversible ; objet identifié par DN, GUID, SID.
- OU : pour déléguer et appliquer des GPO, pas pour recopier un organigramme.
- Sites : sous-réseaux, liens, coûts ; localisation des DC et réplication.
- Deux DC en production ; un laboratoire se jette.

## Pour aller plus loin

- Microsoft Learn — Vue d'ensemble d'AD DS : <https://learn.microsoft.com/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview>
- Microsoft Learn — Conception de la topologie de sites : <https://learn.microsoft.com/windows-server/identity/ad-ds/plan/designing-the-site-topology>
- Microsoft Learn — Ports et pare-feu pour AD : <https://learn.microsoft.com/troubleshoot/windows-server/active-directory/config-firewall-for-ad-domains-and-trusts>
- Microsoft Learn — Vue d'ensemble de Kerberos : <https://learn.microsoft.com/windows-server/security/kerberos/kerberos-authentication-overview>
- RFC 4120 — Kerberos V5 : <https://www.rfc-editor.org/rfc/rfc4120>
- RFC 4511 — LDAP : <https://www.rfc-editor.org/rfc/rfc4511>
- RFC 2782 — Enregistrements DNS SRV : <https://www.rfc-editor.org/rfc/rfc2782>
- RFC 6761 — Noms de domaine spéciaux (`.test`) : <https://www.rfc-editor.org/rfc/rfc6761>

## Crédits des images

| Fichier | Source | Auteur | Licence | Modifications |
| --- | --- | --- | --- | --- |
| `images/active-directory-ds-1.png` | <https://commons.wikimedia.org/wiki/File:ActiveDirectory_Forest.png> | 小朱 (Wikimedia Commons) | Domaine public — <https://creativecommons.org/publicdomain/mark/1.0/> | Aucune (fichier renommé) |
| `images/active-directory-ds-2.png` | <https://commons.wikimedia.org/wiki/File:ActiveDirectory_DomainTree.png> | 小朱 (Wikimedia Commons) | Domaine public — <https://creativecommons.org/publicdomain/mark/1.0/> | Aucune (fichier renommé) |
| `images/active-directory-ds-3.svg` | <https://commons.wikimedia.org/wiki/File:Kerberos_protocol.svg> | Jeran Renz (<https://commons.wikimedia.org/wiki/User:Jeran_Renz>) | CC BY-SA 4.0 — <https://creativecommons.org/licenses/by-sa/4.0/> | Aucune (fichier renommé) ; légende française ajoutée dans le texte ; l'image reste sous CC BY-SA 4.0 |
| `images/active-directory-ds-4.svg` | Création originale du projet Pack Master | Projet Pack Master | Dédiée au domaine public (CC0) — <https://creativecommons.org/publicdomain/zero/1.0/> | Sans objet |

## Historique de vérification

| Date | OS/logiciel | Testeur | Verdict |
| --- | --- | --- | --- |
| 2026-11-01 | Windows Server (AD DS), client Windows, Linux (`dig`) | Rédaction assistée (Copilot) | Non testé sur plateforme cible |

Remarque : aucune commande n'a été exécutée sur Windows Server ; seuls les licences d'images ([[Glossary:API]] Wikimedia Commons) et la validité XML des SVG ont été contrôlées localement.