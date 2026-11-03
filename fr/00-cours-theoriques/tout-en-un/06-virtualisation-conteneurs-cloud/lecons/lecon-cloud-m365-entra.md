---
title: "Leçon — Cloud : IaaS, PaaS, SaaS, responsabilité partagée, coûts, sécurité d'accès, Microsoft 365 et Microsoft Entra ID"
description: "À l'issue de cette leçon, vous saurez :"
published: true
date: 2026-11-03T14:22:28Z
tags: ["transverse", "tout-en-un", "lecon", "cloud", "iaas", "paas", "saas", "microsoft-365", "entra-id", "identite"]
editor: markdown
dateCreated: 2026-11-03T14:22:28Z
dateModified: 2026-11-03T14:22:28Z
---

# Leçon — Cloud : IaaS, PaaS, SaaS, responsabilité partagée, coûts, sécurité d'accès, Microsoft 365 et Microsoft Entra ID

- **Tags** : `transverse`, `tout-en-un`, `lecon`, `cloud`, `iaas`, `paas`, `saas`, `microsoft-365`, `entra-id`, `identite`
- **Niveau** : débutant à intermédiaire (technicien [[Glossary:TSSR]], administrateur junior)
- **Durée estimée** : 4 h (cours 1 h 45, labo guidé 1 h 30, exercices et quiz 45 min)

> **Avertissement de test** : aucun tenant Microsoft, abonnement cloud ni module PowerShell n'a été utilisé pour rédiger cette leçon. **Toutes les commandes et manipulations d'interface sont non testées sur la plateforme cible.** Travaillez uniquement dans un tenant de test ou de démonstration, jamais en premier sur un tenant de production.

---

## Objectifs pédagogiques

À l'issue de cette leçon, vous saurez :

1. Définir le cloud et distinguer **IaaS, PaaS et SaaS**, ainsi que cloud public, privé et hybride.
2. Appliquer le modèle de **responsabilité partagée** pour dire qui doit sécuriser quoi.
3. Expliquer **régions** et **zones de disponibilité** et choisir une région selon latence, conformité et coût.
4. Comprendre les mécanismes de **facturation** et mettre en place des garde-fous de coûts.
5. Appliquer les principes de **sécurité d'accès** : moindre privilège, [[Glossary:MFA]], comptes d'administration séparés, comptes de secours.
6. Décrire un **tenant Microsoft 365** et son lien avec **Microsoft Entra ID** (ex-Azure [[Glossary:AD]]).
7. Réaliser côté administrateur les opérations de base : utilisateurs, groupes, licences, rôles, MFA, accès conditionnel en mode rapport.

## Prérequis et durée

- Notions de réseau ([[Glossary:DNS]], HTTPS) et d'annuaire (compte, groupe).
- Un **tenant de test** Microsoft 365 (programme développeur, essai ou démonstration) et un compte administrateur de ce tenant ; un abonnement cloud de test est optionnel.
- PowerShell 7 pour la partie Microsoft Graph. Durée : 4 h.

## L'essentiel en bref

- Le **cloud** fournit des ressources informatiques à la demande, via le réseau, facturées à l'usage.
- **IaaS** : on loue de l'infrastructure ([[Glossary:VM]], réseau, disques). **PaaS** : on déploie son code sur une plateforme gérée. **SaaS** : on utilise un logiciel prêt à l'emploi.
- **Responsabilité partagée** : le fournisseur sécurise le cloud (datacentres, matériel, hyperviseur) ; le client sécurise **ce qu'il met dans** le cloud (données, identités, configuration). Les données et les accès sont **toujours** à la charge du client.
- Le coût est **variable** : sans suivi, il dérive. Budgets, alertes, étiquettes et arrêt des ressources inutiles sont indispensables.
- L'identité est le **nouveau périmètre** : la majorité des compromissions cloud passent par un compte volé. MFA et moindre privilège sont prioritaires.
- **Microsoft 365** (messagerie, fichiers, Teams…) s'appuie sur **Microsoft Entra ID**, l'annuaire cloud qui authentifie et autorise.

---

## 1. Le cloud, en clair

Le **cloud computing** consiste à consommer des ressources informatiques (calcul, stockage, réseau, logiciels) fournies par un prestataire, à la demande et via Internet. La définition de référence du [[Glossary:NIST]] retient cinq caractéristiques : **libre-service** à la demande, **accès large par le réseau**, **mutualisation** des ressources, **élasticité rapide** et **service mesuré** (on paie ce qu'on consomme).

Analogie : l'électricité. Autrefois, chaque usine produisait la sienne (salle serveur). Aujourd'hui on se branche sur un réseau, on consomme, on paie au compteur. Il reste à bien câbler chez soi : le fournisseur garantit le courant, pas que votre installation est sûre.

**Modèles de déploiement** : cloud **public** (infrastructure du fournisseur, partagée), **privé** (dédié à une organisation) et **hybride** (les deux reliés, courant quand un annuaire ou des applications historiques restent sur site). Pour l'administrateur : on passe d'investissements à des **dépenses d'exploitation**, la capacité s'ajuste en minutes, mais on dépend de la disponibilité du fournisseur et de la connexion Internet.

## 2. IaaS, PaaS, SaaS : qui gère quoi ?

![Tableau montrant, pour sur site, IaaS, PaaS et SaaS, les six couches de la pile informatique et qui les gère entre client et fournisseur](images/cloud-m365-entra-1.svg)
*Figure 1 — Plus on monte de IaaS vers SaaS, plus le fournisseur gère de couches ; les données et les accès restent chez le client.*

- **IaaS** (*Infrastructure as a Service*) : vous louez des machines virtuelles, des réseaux virtuels et des disques. Vous gérez le système d'exploitation, les mises à jour, le pare-feu applicatif, les sauvegardes. *Exemple : une VM Linux hébergée chez un fournisseur.* Souplesse maximale, travail d'exploitation maximal.
- **PaaS** (*Platform as a Service*) : le fournisseur gère le système et l'exécution ; vous déployez votre code ou vos données. *Exemples : base de données managée, hébergement d'applications web, Kubernetes managé.* Moins d'administration, moins de contrôle fin.
- **SaaS** (*Software as a Service*) : l'application est fournie complète, via un navigateur. *Exemples : messagerie et bureautique en ligne, outil de ticketing.* Vous configurez les comptes, les droits et les paramètres de sécurité.

Choisir : **contrôle** d'un système ancien → IaaS ; **rapidité** sur du code ou des données → PaaS ; **besoin standard** (mail, visioconférence) → SaaS. Les cas réels mélangent les trois : sachez toujours où s'arrête la responsabilité du fournisseur.

## 3. La responsabilité partagée

C'est la notion la plus testée et la plus mal comprise. Règle simple : **le fournisseur sécurise l'infrastructure du cloud ; vous sécurisez ce que vous y mettez et la façon dont vous y accédez.**

| Élément | IaaS | PaaS | SaaS |
|---|---|---|---|
| Datacentre, matériel, réseau physique | Fournisseur | Fournisseur | Fournisseur |
| Hyperviseur | Fournisseur | Fournisseur | Fournisseur |
| Système d'exploitation et correctifs | **Client** | Fournisseur | Fournisseur |
| Configuration réseau et pare-feu | **Client** | Partagé | Fournisseur |
| Application et son code | **Client** | **Client** | Fournisseur |
| **Identités et droits d'accès** | **Client** | **Client** | **Client** |
| **Données** (classification, partage, sauvegarde) | **Client** | **Client** | **Client** |

Conséquences : un **stockage public par erreur** est une faute du client ; en SaaS, un administrateur sans MFA ou un partage trop large relèvent de **vous** ; la **sauvegarde** reste à votre charge (la redondance du fournisseur ne protège ni de votre suppression, ni d'un rançongiciel) ; la **conformité** ([[Glossary:RGPD]]) engage le client.

## 4. Régions, zones et disponibilité

![Deux régions, chacune avec trois zones de disponibilité hébergeant des instances web et des réplicas de base de données, reliées par une réplication entre régions](images/cloud-m365-entra-2.svg)
*Figure 2 — Répartir sur plusieurs zones protège d'une panne de datacentre ; répliquer vers une autre région protège d'un sinistre régional.*

Une **région** est une zone géographique contenant plusieurs datacentres. Une **zone de disponibilité** est un datacentre (ou groupe) physiquement distinct à l'intérieur d'une région, relié aux autres par un réseau rapide. Le choix d'une région pèse sur :

- la **latence** : plus proche des utilisateurs, plus rapide ;
- la **conformité** : certaines données doivent rester dans un pays ou l'Union européenne ;
- le **coût** : les prix varient selon les régions ;
- les **services disponibles** : toutes les fonctions ne sont pas déployées partout.

Pour la disponibilité : une application répartie sur **trois zones** survit à la perte d'une zone ; une copie dans une **seconde région** couvre un sinistre régional, avec un surcoût et une complexité de bascule. Définissez deux objectifs chiffrés : le **[[Glossary:RTO]]** (durée maximale d'interruption acceptable) et le **[[Glossary:RPO]]** (perte de données maximale acceptable). Le **[[Glossary:SLA]]** du fournisseur (par exemple 99,9 % de disponibilité) donne des crédits en cas de manquement, pas une garantie de service sans panne.

En SaaS comme Microsoft 365, la région de résidence des données se choisit surtout à la création du tenant ; consultez les engagements de résidence du service.

Avec un abonnement de test et l'interface Azure [[Glossary:CLI]], cette commande en lecture seule vérifie le contexte actif :

```bash
az account show --query "{abonnement:name, tenant:tenantId}" -o table
```

👉 Explication : affiche l'abonnement et le tenant de la session (à contrôler avant toute action pour ne pas viser le mauvais contexte) ; `az account list-locations -o table` liste les régions. Lecture seule, non testée ici.

## 5. Les coûts : comprendre et maîtriser

Le cloud rend la facture **variable** : sans surveillance, elle explose. Postes principaux : **calcul** (à l'heure ou à la seconde), **stockage** (niveaux chaud, froid, archive), **réseau** (le trafic sortant, *egress*, est facturé et surprend souvent), **licences SaaS** (par utilisateur ; les licences de comptes inutilisés sont un gaspillage courant). Modes d'achat : *à la demande* (flexible, plus cher), *réservation* sur un à trois ans (remise pour charge stable), *capacité excédentaire* (bon marché mais interruptible).

Garde-fous de base : **budgets et alertes** à 50, 80 et 100 % ; **étiquettes** (`projet`, `responsable`, `environnement`) ; **revue mensuelle** des ressources orphelines et du dimensionnement ; **arrêt automatique** des environnements de test hors heures ; limitation des droits de création de ressources coûteuses. L'ensemble s'appelle **FinOps**. Un minage de cryptomonnaie lancé après la fuite d'une clé d'accès est un classique : coût et sécurité sont liés.

## 6. Sécurité d'accès : l'identité d'abord

Dans le cloud, il n'y a plus de pare-feu d'entreprise protégeant un réseau interne : toute ressource est joignable via Internet par quiconque s'authentifie. **L'identité devient le périmètre.** Les principes à appliquer partout :

- **MFA** (authentification multifacteur) pour tous les comptes, **obligatoire** pour les administrateurs. Privilégiez les méthodes résistantes à l'hameçonnage (clé de sécurité [[Glossary:FIDO2]], passkeys, application d'authentification avec confirmation numérique) plutôt que le SMS.
- **Moindre privilège** : attribuez le rôle le plus restreint qui permet la tâche, sur le périmètre le plus étroit possible, et pour la durée nécessaire.
- **Comptes d'administration séparés** : un compte nominatif pour la bureautique, un autre pour l'administration, jamais utilisé pour lire le courrier ni naviguer.
- **Pas de partage de comptes**, ni de mots de passe ou clés d'accès longue durée en clair dans du code ou Git.
- **Comptes de secours** (*break-glass*) : deux comptes cloud dédiés, mot de passe très long en coffre, exclus des politiques qui pourraient vous enfermer dehors, avec alerte à chaque connexion ; réservés aux pannes d'authentification.
- **Journaux et alertes** : conservez les journaux de connexion et d'audit, surveillez connexions inhabituelles et changements de rôles.
- **Exposition minimale** : stockage, bases et consoles non publics par défaut.
- **Cycle de vie** : arrivées, mutations, départs ; un compte d'ancien employé non désactivé est une porte ouverte.

---

## 7. Microsoft 365 : le tenant et ses services

**Microsoft 365** est un ensemble de services SaaS (messagerie, fichiers, collaboration, bureautique) proposé par abonnement. Votre organisation y est représentée par un **tenant** (« locataire ») : un espace isolé qui contient vos utilisateurs, vos données et vos paramètres, identifié par un nom initial du type `<nom>.onmicrosoft.com` (dans cette leçon on utilise le domaine fictif `example.test`) et un identifiant unique (GUID).

![Tenant example.test : identités et contrôle d'accès de Microsoft Entra ID au-dessus des services Microsoft 365](images/cloud-m365-entra-3.svg)
*Figure 3 — Entra ID authentifie et autorise ; les services Microsoft 365 consomment cette identité.*

Services principaux et leur rôle :

| Service | Fonction | À connaître côté administrateur |
|---|---|---|
| **Exchange Online** | messagerie et agendas | boîtes aux lettres, enregistrements DNS (MX, [[Glossary:SPF]], [[Glossary:DKIM]], [[Glossary:DMARC]]), règles de transport |
| **SharePoint Online / OneDrive** | sites d'équipe, stockage de fichiers | partage externe, quotas, rétention |
| **Teams** | discussions, réunions, équipes | création d'équipes, invités, stratégies |
| **Centre d'administration Microsoft 365** | gestion des utilisateurs, licences, domaines, santé du service | point d'entrée de l'administrateur |
| **Microsoft Entra ID** | annuaire, authentification, accès | utilisateurs, groupes, rôles, MFA, accès conditionnel |

**Domaines** : le tenant porte d'abord un domaine `.onmicrosoft.com`. Pour utiliser `example.test`, on l'ajoute dans le centre d'administration et on **prouve sa propriété** par un enregistrement DNS TXT, puis on ajuste MX, SPF, DKIM et DMARC. Toute modification DNS est sensible : notez les valeurs existantes, utilisez un [[Glossary:TTL]] court et conservez l'ancienne configuration pour revenir en arrière.

**Licences** : chaque utilisateur reçoit un plan qui active des services. L'affectation **par groupe** automatise le cycle de vie : on ajoute la personne au groupe, elle reçoit sa licence ; on la retire, la licence est libérée. Surveillez aussi l'état de santé des services, le centre de messages et les rapports d'utilisation.

## 8. Microsoft Entra ID : l'annuaire cloud

**Microsoft Entra ID** (anciennement Azure Active Directory) est le service d'identité de Microsoft. Il gère les **utilisateurs**, **groupes**, **appareils** et **applications**, authentifie les connexions et applique les règles d'accès. Il ne faut pas le confondre avec Active Directory Domain Services sur site : protocoles et modèles diffèrent (ici OAuth 2.0, OpenID Connect, [[Glossary:SAML]] ; là Kerberos et [[Glossary:LDAP]]). Dans les environnements **hybrides**, un outil de synchronisation (Microsoft Entra Connect ou Cloud Sync) copie les comptes de l'annuaire sur site vers le cloud.

**Objets** : *utilisateurs* (membres, invités B2B), *identités applicatives*, *groupes* de sécurité ou Microsoft 365 (à appartenance fixe ou **dynamique**), *appareils* enregistrés ou joints pour évaluer leur conformité.

**Rôles d'administration** : Entra ID fournit des rôles intégrés pour déléguer sans tout donner. Quelques exemples (liste non exhaustive) :

| Rôle | Pouvoirs principaux |
|---|---|
| Administrateur général | tout, dans le tenant ; **2 à 4 personnes**, jamais pour les tâches courantes |
| Administrateur d'utilisateurs | gérer les comptes non privilégiés (support de niveau 2) |
| Administrateur du support technique | réinitialiser les mots de passe de comptes non privilégiés (niveau 1) |
| Lecteur général | lecture seule sur la configuration (audit, diagnostic) |

Un rôle peut être **actif en permanence** ou, avec Entra ID P2 (Privileged Identity Management), **éligible** : activé temporairement, avec justification et approbation. C'est la meilleure application du moindre privilège.

**Éditions** : gratuite (incluse avec Microsoft 365), P1 (accès conditionnel, groupes dynamiques), P2 (protection des identités, PIM) ; vérifiez votre licence avant de concevoir une politique.

**Accès conditionnel** : règles « si… alors… » évaluées à chaque connexion. Exemples : *si rôle d'administration, exiger la MFA* ; *si authentification héritée, bloquer* ; *si appareil non conforme, refuser la messagerie*. Chaque politique définit utilisateurs (cibles, exclusions), applications, conditions et contrôle. Testez toujours en **mode rapport seul** et **excluez les comptes de secours**. Sans P1, les **valeurs par défaut de sécurité** activent un socle (MFA des administrateurs, blocage de l'authentification héritée) ; ne les combinez pas avec des politiques personnalisées.

**Journaux** : les journaux de connexion (qui, d'où, résultat) et d'audit (qui a modifié quoi) sont la première source en incident ; leur durée de conservation dépend de la licence, exportez-les si besoin.

## 9. Opérations d'administration de base

Deux voies : les **portails** (centre d'administration Microsoft 365, centre d'administration Microsoft Entra) pour l'ordinaire, et **Microsoft Graph PowerShell** pour automatiser et auditer. Connectez-vous toujours avec un compte d'administration **dédié**, avec les permissions minimales demandées explicitement.

Installer le module et se connecter en lecture seule :

```powershell
Install-Module Microsoft.Graph -Scope CurrentUser
Connect-MgGraph -Scopes "User.Read.All","Directory.Read.All"
Get-MgContext | Select-Object Account, TenantId, Scopes
```

👉 Explication : installe le SDK pour l'utilisateur courant, ouvre une connexion interactive avec seulement des permissions de lecture (un consentement peut être demandé), puis affiche le compte, le tenant et les permissions effectivement accordées ; vérifiez le tenant avant de continuer.

Lister quelques utilisateurs et l'état de leur compte :

```powershell
Get-MgUser -Top 10 -Property DisplayName,UserPrincipalName,AccountEnabled |
  Select-Object DisplayName, UserPrincipalName, AccountEnabled
```

👉 Explication : affiche dix comptes avec leur nom, leur identifiant de connexion et si le compte est activé ; lecture seule.

Contrôler les licences disponibles et consommées :

```powershell
Get-MgSubscribedSku | Select-Object SkuPartNumber, ConsumedUnits, @{n='Total';e={$_.PrepaidUnits.Enabled}}
```

👉 Explication : compare, pour chaque plan, les licences utilisées aux licences achetées, ce qui permet de repérer manque ou gaspillage.

Auditer les rôles privilégiés :

```powershell
Get-MgDirectoryRole | ForEach-Object {
  $role = $_
  Get-MgDirectoryRoleMember -DirectoryRoleId $role.Id |
    ForEach-Object { [pscustomobject]@{ Role = $role.DisplayName; Membre = $_.AdditionalProperties.userPrincipalName } }
} | Sort-Object Role, Membre
```

👉 Explication : énumère les rôles activés dans le tenant et leurs membres ; à utiliser pour vérifier qu'il y a très peu d'administrateurs généraux et que chacun est nominatif.

Créer un utilisateur de test (modification, **tenant de test uniquement**) :

```powershell
Connect-MgGraph -Scopes "User.ReadWrite.All"
$mdp = [guid]::NewGuid().ToString("N") + "aZ!"
New-MgUser -DisplayName "Alice Exemple" -UserPrincipalName "alice@example.test" -MailNickname "alice" `
  -AccountEnabled -PasswordProfile @{ Password = $mdp; ForceChangePasswordNextSignIn = $true }
```

👉 Explication : crée un compte avec un mot de passe temporaire aléatoire qui devra être changé à la première connexion ; remplacez `example.test` par un domaine vérifié de votre tenant de test. Transmettez le mot de passe par un canal sûr, ne l'écrivez pas dans un ticket. Retour arrière : supprimer le compte avec `Remove-MgUser -UserId alice@example.test` (il reste récupérable un temps dans la corbeille Entra).

Terminez toujours par `Disconnect-MgGraph` (ferme la session et libère le jeton d'accès).

**Processus d'arrivée, de mutation, de départ** : à l'arrivée, créer le compte (ou le laisser synchroniser), l'ajouter aux groupes (qui attribuent licences et accès), imposer l'enregistrement MFA ; à la mutation, retirer les anciens groupes ; au départ, **désactiver** le compte, révoquer les sessions, convertir ou transférer la boîte aux lettres selon la politique, puis supprimer après la durée de rétention prévue.

---

## Mise en pratique guidée

**Cadre** : tenant Microsoft 365 **de test**, sans donnée réelle, avec un compte administrateur de ce tenant ; commandes **non testées sur la plateforme cible**. 

**Sécurité de la manipulation** : avant toute modification de politique d'accès, **exportez la configuration actuelle** (captures d'écran ou export [[Glossary:JSON]] des politiques), vérifiez que **deux comptes de secours** existent et sont exclus des politiques, et gardez une session administrateur ouverte dans une fenêtre de navigation privée distincte pour pouvoir annuler une erreur. Pas de snapshot possible ici : le retour arrière consiste à désactiver la politique et à restaurer l'état exporté.

1. **Cartographier le tenant.** Dans le centre d'administration Microsoft Entra, notez le nom du tenant, son identifiant, les domaines vérifiés et l'édition de licence. Dans le centre d'administration Microsoft 365, notez les plans de licence et le nombre d'unités libres.
2. **Lister les administrateurs** avec le script d'audit de la section 9 : 2 à 4 administrateurs généraux nominatifs sont attendus.
3. **Créer deux groupes de sécurité** `GRP-Compta` et `GRP-Support` dans le centre d'administration Entra, puis un utilisateur de test comme à la section 9, et l'ajouter à `GRP-Compta`.
4. **Affecter une licence par groupe.** Dans les propriétés du groupe, section Licences, assignez un plan disponible ; contrôlez que l'utilisateur de test reçoit la licence (le traitement peut prendre quelques minutes).
5. **Activer la MFA.** Selon l'édition, activez les valeurs par défaut de sécurité, ou créez une politique d'accès conditionnel « Exiger la MFA pour les rôles d'administration » : utilisateurs cibles = rôles d'administration ; exclusions = comptes de secours ; accès = exiger l'authentification multifacteur ; état = **rapport seul**.
6. **Observer** les journaux de connexion et l'onglet « Rapport seul » : la politique indique ce qu'elle aurait fait.
7. **Basculer en activé** après vérification, puis tester une connexion administrateur en session privée : la MFA doit être demandée.
8. **Retour arrière du labo.** Désactivez la politique, supprimez l'utilisateur et les groupes de test :

```powershell
Connect-MgGraph -Scopes "User.ReadWrite.All","Group.ReadWrite.All"
Remove-MgUser -UserId "alice@example.test"
Get-MgGroup -Filter "displayName eq 'GRP-Compta'" | ForEach-Object { Remove-MgGroup -GroupId $_.Id }
Get-MgGroup -Filter "displayName eq 'GRP-Support'" | ForEach-Object { Remove-MgGroup -GroupId $_.Id }
Disconnect-MgGraph
```

👉 Explication : supprime nominativement le compte et les deux groupes créés pour le labo (aucun filtre large) puis ferme la session ; vérifiez le résultat dans le portail, la corbeille Entra conservant un temps les éléments supprimés.

---

## Exercices

1. **(Facile)** Classez en IaaS, PaaS ou SaaS : une VM Linux louée ; une base de données managée ; une messagerie en ligne.
2. **(Facile)** Citez trois éléments que le client doit toujours sécuriser, quel que soit le modèle.
3. **(Moyen)** Une société veut héberger ses données en Europe, avec une application accessible malgré la panne d'un datacentre. Quelle architecture de régions et de zones proposez-vous ?
4. **(Moyen)** La facture mensuelle double. Listez cinq vérifications rapides.
5. **(Moyen)** Expliquez la différence entre Microsoft 365 et Microsoft Entra ID, en une phrase chacun.
6. **(Avancé)** Vous devez imposer la MFA à tout le monde sans risquer de vous enfermer. Décrivez la démarche en six étapes.

## Corrigés des exercices

1. VM louée : **IaaS** ; base de données managée : **PaaS** ; messagerie en ligne : **SaaS**.
2. Les **données**, les **identités et droits d'accès**, et la **configuration** de ce qu'il déploie (par exemple l'exposition publique). Aussi : sauvegardes et conformité.
3. Une région en Europe choisie pour la conformité ; l'application répartie sur **au moins deux ou trois zones** avec un équilibreur ; base répliquée entre zones ; éventuellement seconde région européenne pour le sinistre régional. Définir RTO/RPO et tester la bascule.
4. Ressources oubliées (VM, disques orphelins) ; trafic sortant inhabituel ; changement de niveau de service ; clé fuitée avec minage ; licences inutilisées. Outils : analyse des coûts par étiquette, journal d'activité, alertes de budget.
5. **Microsoft 365** : ensemble de services SaaS (messagerie, fichiers, collaboration) ; **Entra ID** : service d'identité qui authentifie et autorise l'accès à ces services et à d'autres applications.
6. (1) Créer deux comptes de secours cloud avec mot de passe long en coffre ; (2) les exclure de la politique ; (3) créer la politique « exiger la MFA » en **rapport seul** ; (4) communiquer et faire enregistrer les méthodes MFA aux utilisateurs ; (5) analyser le rapport et traiter les cas bloquants (comptes de service, applications héritées) ; (6) activer par vagues, d'abord administrateurs puis un groupe pilote, avec point de retour (désactivation de la politique).

## Quiz

**Q1. Dans quel modèle gère-t-on le système d'exploitation ?** A) SaaS B) PaaS C) IaaS D) Aucun
**Réponse : C.** En IaaS, le fournisseur livre la VM ; système et correctifs sont au client.

**Q2. Qui est responsable des données stockées dans un service SaaS ?** A) Le fournisseur seul B) Le client C) L'hébergeur D) Personne
**Réponse : B.** Données, identités et droits d'accès restent toujours côté client.

**Q3. Une zone de disponibilité est…** A) Un pays B) Un datacentre physiquement distinct dans une région C) Un compte D) Une licence
**Réponse : B.** Répartir sur plusieurs zones protège d'une panne de datacentre.

**Q4. Quel poste de facturation surprend souvent ?** A) Le trafic entrant B) Le trafic sortant (*egress*) C) Le nom du tenant D) Le fuseau horaire
**Réponse : B.** La sortie de données hors du cloud ou entre régions est généralement facturée.

**Q5. Que signifie RTO ?** A) Durée maximale d'interruption acceptable B) Perte de données maximale C) Remise sur engagement D) Région de tenant
**Réponse : A.** Le RPO mesure la perte de données acceptable.

**Q6. Bonne pratique pour les administrateurs ?** A) Un seul compte pour tout B) Un compte d'administration séparé du compte quotidien C) Compte partagé D) Pas de MFA
**Réponse : B.** On limite l'exposition du compte privilégié à l'hameçonnage.

**Q7. Pourquoi des comptes de secours (*break-glass*) ?** A) Pour la messagerie B) Retrouver un accès si l'authentification ou une politique est défaillante C) Économiser des licences D) Pour les invités
**Réponse : B.** Exclus des politiques, protégés et supervisés, ils servent en dernier recours.

**Q8. Comment tester une politique d'accès conditionnel sans risque ?** A) L'activer pour tous B) Mode rapport seul C) La supprimer D) Désactiver les journaux
**Réponse : B.** Il évalue l'effet sans l'appliquer.

**Q9. Combien d'administrateurs généraux environ ?** A) Tous B) 2 à 4 nominatifs C) Un partagé D) Cent
**Réponse : B.** Assez pour la continuité, peu pour limiter le risque.

**Q10. Quelle commande lit les licences consommées ?** A) `Get-MgSubscribedSku` B) `Remove-MgUser` C) `Disconnect-MgGraph` D) `New-MgUser`
**Réponse : A.** Elle affiche plans, unités consommées et achetées (lecture seule).

## Erreurs fréquentes et dépannage

| Symptôme | Cause probable | Piste de résolution |
|---|---|---|
| Facture inattendue | ressources oubliées, sortie de données, clé fuitée | analyse des coûts par étiquette, journal d'activité, budgets et alertes |
| Stockage exposé publiquement | configuration par défaut modifiée | revue des accès publics, politiques de blocage, journalisation |
| Administrateur verrouillé après une politique | comptes de secours non exclus, politique activée sans rapport | utiliser un compte de secours, désactiver la politique, retester en rapport seul |
| `Insufficient privileges` dans Graph | permission ou consentement manquant | relancer `Connect-MgGraph` avec la portée adaptée, consentement administrateur |
| Licence non attribuée au nouvel utilisateur | pays d'usage non renseigné, licences épuisées, traitement du groupe en cours | renseigner le pays, vérifier `Get-MgSubscribedSku`, patienter ou re-traiter |
| Domaine non vérifié | enregistrement TXT absent ou non propagé | vérifier avec `nslookup -type=TXT example.test`, attendre le TTL |
| Mauvais tenant modifié | session connectée à un autre tenant | `Get-MgContext` avant toute action, profils de navigateur distincts |

Méthode : vérifier d'abord **le contexte** (tenant, abonnement, compte), puis l'état (portail), les **journaux** de connexion et d'audit, et seulement ensuite modifier. Toute modification sensible : export de l'état, test en mode rapport, point de retour documenté.

## À retenir

- Le cloud est un service mesuré, à la demande, via le réseau ; IaaS, PaaS, SaaS déterminent ce que vous administrez.
- **Responsabilité partagée** : le fournisseur protège le cloud ; vous protégez vos données, identités et configurations.
- Une région se choisit selon latence, conformité, coût et services ; plusieurs zones assurent la disponibilité, une seconde région le sinistre.
- La facture est variable : budgets, alertes, étiquettes et revues régulières sont obligatoires.
- L'identité est le périmètre : MFA, moindre privilège, comptes d'administration séparés, comptes de secours, journaux.
- Microsoft 365 = services ; Entra ID = identité ; l'accès conditionnel se teste en rapport seul.
- Tenant de test d'abord, export de l'état avant changement, retour arrière prévu.

## Pour aller plus loin

- Définition du cloud (NIST SP 800-145) : <https://csrc.nist.gov/pubs/sp/800/145/final>
- Responsabilité partagée dans Azure : <https://learn.microsoft.com/azure/security/fundamentals/shared-responsibility>
- Microsoft Entra ID : <https://learn.microsoft.com/entra/identity/>
- Accès conditionnel : <https://learn.microsoft.com/entra/identity/conditional-access/overview>
- Comptes d'accès d'urgence : <https://learn.microsoft.com/entra/identity/role-based-access-control/security-emergency-access>
- Centre d'administration Microsoft 365 : <https://learn.microsoft.com/microsoft-365/admin/>
- Microsoft Graph PowerShell : <https://learn.microsoft.com/powershell/microsoftgraph/>
- Principes FinOps : <https://www.finops.org/introduction/what-is-finops/>
- Autres leçons de la série : [Docker : fondamentaux](/fr/00-cours-theoriques/tout-en-un/06-virtualisation-conteneurs-cloud/lecons/lecon-docker-fondamentaux) ; [Compose, sécurité et Kubernetes](/fr/00-cours-theoriques/tout-en-un/06-virtualisation-conteneurs-cloud/lecons/lecon-compose-securite-kubernetes)

## Crédits des images

| Fichier | Source (URL Commons) | Auteur | Licence (nom + URL) | Modifications |
|---|---|---|---|---|
| `images/cloud-m365-entra-1.svg` à `-3.svg` | Création originale, aucune source externe | Projet Pack Master | CC0 1.0 — <https://creativecommons.org/publicdomain/zero/1.0/> | Sans objet |

Mention : « Création originale du projet Pack Master, dédiée au domaine public (CC0) ». Aucune image libre n'a pu être vérifiée sur Wikimedia Commons ([[Glossary:API]] indisponible, limitation de débit) ; des schémas originaux ont donc été créés.

## Historique de vérification

| Date | OS/logiciel | Testeur | Verdict |
|---|---|---|---|
| 2026-11-01 | Microsoft 365, Microsoft Entra ID, Microsoft Graph PowerShell, Azure CLI (aucun tenant ni commande exécutés) | Rédaction assistée par IA, relecture humaine à faire | Non testé sur plateforme cible |