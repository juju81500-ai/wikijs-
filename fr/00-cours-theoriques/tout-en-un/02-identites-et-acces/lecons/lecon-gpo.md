---
title: "Leçon — Stratégies de groupe (GPO) : ordre LSDOU, héritage, filtrage et dépannage"
description: "À la fin de cette leçon, vous saurez :"
published: true
date: 2026-11-03T09:36:13Z
tags: ["transverse", "tout-en-un", "lecon", "identites", "active-directory", "gpo", "strategies-de-groupe", "windows-server"]
editor: markdown
dateCreated: 2026-11-03T09:36:13Z
dateModified: 2026-11-03T09:36:13Z
---

# Leçon — Stratégies de groupe (GPO) : ordre LSDOU, héritage, filtrage et dépannage

- **Tags** : `transverse`, `tout-en-un`, `lecon`, `identites`, `active-directory`, `gpo`, `stratégies-de-groupe`, `windows-server`
- **Niveau** : Intermédiaire (TSSR / administrateur systèmes)
- **Durée estimée** : 3 h 30 (lecture 1 h 10, laboratoire 1 h 40, exercices et quiz 40 min)

---

## Objectifs pédagogiques

À la fin de cette leçon, vous saurez :

1. expliquer ce qu'est une GPO et où elle est stockée (conteneur AD et dossier SYSVOL) ;
2. prédire l'ordre de traitement **LSDOU** et le résultat d'un conflit ;
3. utiliser **l'héritage**, **Appliqué (Enforced)**, **Bloquer l'héritage** et le traitement par **boucle de rappel (loopback)** ;
4. cibler une GPO avec le **filtrage de sécurité** et un **filtre WMI** ;
5. diagnostiquer avec `gpupdate`, `gpresult` et les journaux ;
6. réaliser quatre cas pratiques dans un laboratoire jetable.

## Prérequis et durée

- Avoir suivi la leçon sur Active Directory Domain Services (domaine, OU, DNS, sites) ou en maîtriser les notions.
- Un laboratoire à deux VM sur un réseau isolé : `SRV-DC01` (192.0.2.10, contrôleur du domaine `example.test`) et `PC-W11-01` (192.0.2.50, poste joint au domaine), en versions d'évaluation officielles et détruisibles. Prenez un **instantané** avant de commencer.
- Les outils de gestion des stratégies de groupe (console GPMC et module PowerShell `GroupPolicy`) installés sur le DC.

Aucun mot de passe n'apparaît dans cette leçon. Les adresses sont des adresses de documentation.

## L'essentiel en bref

- Une **GPO** est un paquet de réglages appliqué automatiquement aux **ordinateurs** (configuration ordinateur) et aux **utilisateurs** (configuration utilisateur).
- Une GPO ne s'applique que si elle est **liée** à un site, au domaine ou à une OU **parente** de l'objet visé.
- Ordre d'application : **Local → Site → Domaine → OU** (du parent vers l'enfant) ; en cas de conflit, **le dernier appliqué gagne**.
- **Appliqué (Enforced)** impose un lien vers le bas ; **Bloquer l'héritage** coupe l'héritage venant du haut.
- Le ciblage fin se fait par **filtrage de sécurité** (Lecture + Appliquer) et par **filtre WMI**.
- Dépannage : `gpupdate /force`, `gpresult /r` ou `/h`, journal `Microsoft-Windows-GroupPolicy/Operational`.

---

## 1. Le principe : un règlement intérieur appliqué automatiquement

Analogie : un immeuble de bureaux possède un **règlement général** (celui du propriétaire), puis un règlement par **étage** (celui du syndic), puis des consignes spécifiques à chaque **bureau**. Le règlement le plus proche du bureau complète ou remplace les règles plus générales. Les GPO fonctionnent ainsi : on règle des centaines de postes en une seule modification, sans passer par chaque machine.

Une GPO contient des **paramètres** de deux familles :

| Famille | Exemples | Où se règle-t-elle ? |
| --- | --- | --- |
| **Stratégies** (administrative templates, paramètres de sécurité) | Verrouillage d'écran, panneau de configuration masqué | Application forcée : l'utilisateur ne peut pas la modifier |
| **Préférences** (GPP) | Lecteurs réseau, raccourcis, clés de registre | Réglages « par défaut » modifiables par l'utilisateur, avec ciblage au niveau de l'élément |

Chaque GPO a une **configuration ordinateur** (appliquée au démarrage de la machine, puis périodiquement) et une **configuration utilisateur** (appliquée à l'ouverture de session). On peut désactiver l'une des deux moitiés pour gagner en rapidité si elle est vide.

## 2. Anatomie d'une GPO

Une GPO est en réalité **deux objets** liés par un GUID :

- le **conteneur de stratégie de groupe (GPC)**, dans l'annuaire, sous `CN=Policies,CN=System,DC=example,DC=test` : il porte le nom, l'état, la version et les permissions ;
- le **modèle de stratégie de groupe (GPT)**, dans le dossier **SYSVOL** : `\\example.test\SYSVOL\example.test\Policies\{GUID}`. Il contient les fichiers de réglages (`Registry.pol`, scripts, modèles de sécurité).

Le GPC se réplique avec l'annuaire, le GPT avec le mécanisme de réplication de SYSVOL (DFSR). Quand les deux se désynchronisent (versions différentes), la GPO ne s'applique pas correctement : c'est une cause de panne classique (voir la section dépannage).

Deux GPO sont créées par défaut :

- **Default Domain Policy** : politique de mots de passe, de verrouillage de compte et de Kerberos du domaine (ces « stratégies de compte » ne sont efficaces qu'au niveau du domaine) ;
- **Default Domain Controllers Policy** : droits propres aux DC, liée à l'OU `Domain Controllers`.

Bonne pratique : créer des GPO dédiées et nommées selon leur fonction (`Postes-Verrouillage-Ecran`) plutôt que d'empiler des réglages dans ces deux GPO.

## 3. L'ordre de traitement : LSDOU

![Quatre blocs successifs Local, Site, Domaine, OU avec la mention que le dernier appliqué gagne et deux exceptions](images/gpo-1.svg)

*Ordre d'application des GPO (L, S, D, OU) et les deux exceptions Appliqué et Bloquer l'héritage. Création originale du projet Pack Master.*

L'ordre est :

1. **L**ocal : la stratégie locale de l'ordinateur (appliquée en premier, la plus faible) ;
2. **S**ite : GPO liées au site AD de la machine (rarement utilisé, utile pour des réglages réseau propres à un site) ;
3. **D**omaine : GPO liées à `example.test` ;
4. **OU** : GPO liées aux OU, de la plus haute (parent) à la plus profonde (enfant). La plus proche de l'objet est appliquée en dernier.

**Règle de conflit** : si deux GPO règlent le même paramètre, c'est celle appliquée en dernier qui l'emporte. Si elles règlent des paramètres différents, **les effets s'additionnent**.

Précisions importantes :

- Au **même niveau** (plusieurs GPO liées à une même OU), l'ordre dépend du **numéro d'ordre de liaison** : le lien numéro 1 est appliqué en dernier, donc prioritaire.
- L'état d'un paramètre compte : *Non configuré* n'écrase rien ; *Activé* et *Désactivé* écrasent.
- Les deux configurations s'enchaînent : **ordinateur d'abord** (au démarrage), **utilisateur ensuite** (à l'ouverture de session).
- Les objets sont traités selon **leur propre position** dans l'annuaire : un utilisateur suit la chaîne de **son** OU, un ordinateur celle de **la sienne**. Une GPO « utilisateur » liée à l'OU des postes ne s'applique donc pas… sauf avec la boucle de rappel (section 5).

### 3.1 Exemple chiffré

Domaine : GPO-D active le pare-feu et règle le verrouillage à 15 min. OU Postes : GPO-P règle le verrouillage à 10 min. OU Postes/Portables : GPO-L règle le verrouillage à 5 min. Un portable dans `Portables` obtient : pare-feu actif (seule GPO à le régler), verrouillage à **5 min** (dernière appliquée).

## 4. Héritage, Appliqué et Bloquer l'héritage

Par défaut, une OU **hérite** des GPO des niveaux supérieurs. Deux commutateurs modifient ce comportement :

- **Bloquer l'héritage** (sur une OU) : l'OU ignore les GPO venant du site, du domaine et des OU parentes. Efficace, mais brutal : l'OU perd aussi les réglages de sécurité d'entreprise.
- **Appliqué (Enforced)** (sur un **lien** de GPO) : le lien ne peut pas être écrasé par un niveau plus bas, et il **traverse** « Bloquer l'héritage ». Si plusieurs liens Appliqué se concurrencent, le plus **haut** dans la hiérarchie gagne.

Analogie : « Bloquer l'héritage » est une porte fermée à clé ; « Appliqué » est la clé du propriétaire qui ouvre toutes les portes.

Conseils d'architecture :

- Réservez *Appliqué* aux réglages de sécurité non négociables.
- Évitez *Bloquer l'héritage* : il rend la lecture des résultats difficile. Préférez le **filtrage** ou une structure d'OU adaptée.
- Documentez chaque exception dans la description de la GPO.

## 5. Boucle de rappel (loopback)

Cas typique : une salle de formation, un kiosque, un serveur Bureau à distance. On veut que **tous** les utilisateurs qui s'ouvrent une session sur ces machines reçoivent les mêmes réglages, quel que soit leur propre OU.

Le paramètre **Configurer le mode de traitement par boucle de rappel de la stratégie de groupe utilisateur** (Configuration ordinateur → Modèles d'administration → Système → Stratégie de groupe) a deux modes :

- **Fusionner (Merge)** : on applique d'abord les GPO de l'utilisateur, puis celles de l'ordinateur ; en cas de conflit, la configuration utilisateur **de l'ordinateur** gagne ;
- **Remplacer (Replace)** : on ignore les GPO utilisateur de son OU et on n'applique que la configuration utilisateur des GPO liées à l'ordinateur.

La GPO qui active le mode boucle de rappel est une GPO **liée à l'OU des ordinateurs concernés**. Dans le registre, la valeur est `HKLM\Software\Policies\Microsoft\Windows\System\UserPolicyMode` (1 = fusionner, 2 = remplacer).

## 6. Cibler finement : filtrage de sécurité et WMI

![Organigramme en cinq étapes : lien, activation, moitié configurée, filtrage de sécurité, filtre WMI](images/gpo-2.svg)

*Décision d'application d'une GPO. Création originale du projet Pack Master.*

### 6.1 Filtrage de sécurité

Une GPO possède une **liste de contrôle d'accès** comme un fichier. Pour qu'une GPO s'applique à un objet, celui-ci (ou un de ses groupes) doit avoir les deux droits **Lecture** et **Appliquer la stratégie de groupe**. Par défaut, le groupe *Utilisateurs authentifiés* (qui comprend aussi les ordinateurs) possède les deux : la GPO touche donc tout le monde.

Pour limiter une GPO à un groupe :

1. on **retire** *Appliquer la stratégie de groupe* à *Utilisateurs authentifiés* ;
2. on **ajoute** le groupe cible avec *Lecture* + *Appliquer la stratégie de groupe*.

**Piège (correctif de sécurité MS16-072, juin 2016)** : la partie utilisateur d'une GPO est lue avec le contexte de l'**ordinateur**. Si vous supprimez complètement *Utilisateurs authentifiés*, il faut que *Utilisateurs authentifiés* ou *Ordinateurs du domaine* garde au moins *Lecture* sur la GPO, sinon la GPO est ignorée sans message évident. La méthode sûre est donc : **laisser *Lecture* à Utilisateurs authentifiés et ne donner *Appliquer* qu'au groupe cible**.

Autre précision : un filtre par groupe n'agit qu'après ouverture d'une **nouvelle session** (jeton d'accès renouvelé) pour les utilisateurs et après un **redémarrage** pour les ordinateurs ajoutés à un groupe.

### 6.2 Filtre WMI

Un **filtre WMI** est une requête WQL évaluée sur la machine cible ; la GPO ne s'applique que si la requête renvoie au moins un résultat. Exemples :

- postes de travail uniquement (pas de serveurs) : `SELECT * FROM Win32_OperatingSystem WHERE ProductType = 1` (1 = poste, 2 = contrôleur de domaine, 3 = serveur) ;
- portables : `SELECT * FROM Win32_ComputerSystem WHERE PCSystemType = 2` (2 = mobile ; attention, la plupart des VM se déclarent « Desktop »).

Contraintes : une GPO ne peut avoir qu'**un seul** filtre WMI (un même filtre peut servir à plusieurs GPO), il est évalué à chaque traitement (coût d'exécution) et certains systèmes très anciens l'ignorent. Préférez, quand c'est possible, une OU dédiée ou un groupe : plus rapide et plus lisible.

Pour tester une requête sans rien modifier :

```powershell
Get-CimInstance -Query "SELECT * FROM Win32_OperatingSystem WHERE ProductType = 1" | Select-Object Caption, ProductType
```

👉 Explication : exécute localement la requête WQL du filtre ; si elle renvoie une ligne, la GPO s'appliquerait à cette machine. Lecture seule.

### 6.3 Ciblage au niveau de l'élément (préférences)

Les **préférences** disposent d'un ciblage par élément (groupe, OU, nom, plage IP…), qui évite de multiplier les GPO. N'y enregistrez **jamais** de mot de passe : le chiffrement historique est cassé et a été retiré (MS14-025).

## 7. Quand une GPO est-elle appliquée ? Le rafraîchissement

- **Au démarrage** de l'ordinateur (configuration ordinateur) et **à l'ouverture de session** (configuration utilisateur) ;
- **En arrière-plan**, toutes les **90 minutes** avec un décalage aléatoire de 0 à 30 minutes sur les postes et serveurs membres ; **toutes les 5 minutes** sur les contrôleurs de domaine ;
- **À la demande** avec `gpupdate`.

Certains réglages (installation de logiciels, redirection de dossiers) ne s'appliquent qu'au démarrage ou à l'ouverture de session : `gpupdate` peut alors demander un redémarrage ou une déconnexion. Les réglages de registre issus des stratégies sont en général pris en compte à chaud, mais l'application qui les lit peut avoir besoin d'être relancée.

## 8. Dépannage : méthode et outils

### 8.1 Méthode en cinq questions

1. **Le poste voit-il un DC ?** (DNS, heure, canal sécurisé)
2. **La GPO est-elle liée au bon endroit ?** (OU de l'objet et de ses parents)
3. **Le lien et la GPO sont-ils activés ?**
4. **Un filtre l'écarte-t-il ?** (sécurité, WMI)
5. **Un conflit ou une exception (Appliqué, Bloquer, ordre) la neutralise-t-il ?**

### 8.2 Les commandes à connaître

```powershell
gpupdate /force
```

👉 Explication : relance immédiatement l'évaluation de toutes les GPO (ordinateur et utilisateur), y compris celles inchangées ; peut inviter à redémarrer ou fermer la session.

```powershell
gpresult /r /scope computer
gpresult /r /scope user
```

👉 Explication : affiche le **résultat de stratégie** : GPO appliquées, GPO filtrées (avec la raison), site, dernière application. L'option `/scope computer` demande une invite élevée.

```powershell
gpresult /h "$env:USERPROFILE\Documents\gp-rapport.html" /f
```

👉 Explication : génère un rapport HTML détaillé (valeur finale de chaque paramètre et **GPO gagnante**) ; `/f` écrase un rapport existant du même nom.

```powershell
Get-WinEvent -LogName "Microsoft-Windows-GroupPolicy/Operational" -MaxEvents 30 | Select-Object TimeCreated, Id, Message
```

👉 Explication : lit les 30 derniers événements de traitement des GPO (début, fin, erreurs de lecture, durée) ; lecture seule.

```powershell
nltest /sc_verify:example.test
dcdiag /test:sysvolcheck /test:netlogons
```

👉 Explication : vérifie le canal sécurisé du poste avec le domaine, puis la santé de SYSVOL et du partage Netlogon sur un DC. Lecture seule.

### 8.3 Lire la sortie de `gpresult`

Dans `gpresult /r`, deux rubriques se complètent :

- **Objets de stratégie de groupe appliqués** : liste dans l'ordre d'application ;
- **Les objets de stratégie de groupe suivants n'ont pas été appliqués car ils ont été filtrés** : avec la raison, par exemple *Filtrage de sécurité refusé (Denied)*, *Filtrage WMI*, *Vide (pas de paramètre)*, *Désactivé*.

Cette seconde liste répond à la question « pourquoi ma GPO ne s'applique-t-elle pas ? » dans la grande majorité des cas.

### 8.4 Causes fréquentes

| Cause | Indice |
| --- | --- |
| DNS ou heure incorrects | `gpresult` ne retourne aucune GPO de domaine |
| GPC et GPT désynchronisés | Versions différentes ; erreurs SYSVOL dans le journal |
| Droit de lecture retiré | GPO « filtrée » sans raison évidente |
| Objet dans `CN=Computers` | Aucune GPO d'OU ne s'applique |
| GPO utilisateur liée à l'OU des ordinateurs | Aucun effet (sans boucle de rappel) |
| Réplication lente | GPO visible sur un DC, pas sur l'autre |

---

## Mise en pratique guidée

![Arborescence du laboratoire : domaine, OU Entreprise, OU Postes et Utilisateurs avec GPO liées](images/gpo-3.svg)

*Maquette du laboratoire : où chaque GPO est liée et comment elle est ciblée. Création originale du projet Pack Master.*

**Pré-requis du laboratoire** : l'arborescence `OU=Entreprise` avec `OU=Postes` et `OU=Utilisateurs` (voir la leçon Active Directory), le poste `PC-W11-01` placé dans `OU=Postes`, un utilisateur de test `alice.martin` dans `OU=Utilisateurs`, et un groupe global `GG_Standard` dont Alice est membre.

> Les commandes de cette section sont données à titre pédagogique, elles n'ont pas été exécutées pour rédiger la leçon. Utilisez uniquement un laboratoire jetable.

### Cas 1 — Verrouillage d'écran par inactivité (configuration ordinateur)

```powershell
New-GPO -Name "Lab-Verrouillage-Ecran" -Comment "Lab : inactivité 10 min"
Set-GPRegistryValue -Name "Lab-Verrouillage-Ecran" -Key "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" -ValueName "InactivityTimeoutSecs" -Type DWord -Value 600
New-GPLink -Name "Lab-Verrouillage-Ecran" -Target "OU=Postes,OU=Entreprise,DC=example,DC=test" -LinkEnabled Yes
```

👉 Explication : crée la GPO, y inscrit la valeur de registre qui verrouille la session après 600 secondes d'inactivité, puis la lie à l'OU des postes.

Sur `PC-W11-01` (invite élevée) :

```powershell
gpupdate /force
reg query "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v InactivityTimeoutSecs
gpresult /r /scope computer
```

👉 Explication : force l'application, vérifie la valeur de registre (attendu : `0x258`, soit 600) et contrôle que la GPO figure dans la liste des GPO appliquées.

### Cas 2 — Filtrage de sécurité (configuration utilisateur)

```powershell
New-GPO -Name "Lab-Restrictions-Utilisateur"
Set-GPRegistryValue -Name "Lab-Restrictions-Utilisateur" -Key "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" -ValueName "NoControlPanel" -Type DWord -Value 1
New-GPLink -Name "Lab-Restrictions-Utilisateur" -Target "OU=Utilisateurs,OU=Entreprise,DC=example,DC=test"
Set-GPPermission -Name "Lab-Restrictions-Utilisateur" -TargetName "Authenticated Users" -TargetType Group -PermissionLevel GpoRead
Set-GPPermission -Name "Lab-Restrictions-Utilisateur" -TargetName "GG_Standard" -TargetType Group -PermissionLevel GpoApply
```

👉 Explication : crée une GPO qui masque le Panneau de configuration, la lie à l'OU des utilisateurs, puis remplace le droit des Utilisateurs authentifiés par *Lecture seule* et donne *Appliquer* uniquement à `GG_Standard`. Sur un système localisé, le nom du groupe *Authenticated Users* peut s'afficher différemment ; vérifiez dans GPMC, onglet *Délégation*.

Testez : ouvrez une session `alice.martin` sur le poste ; `gpresult /r /scope user` doit lister la GPO. Retirez Alice de `GG_Standard`, ouvrez une **nouvelle** session : la GPO apparaît en *filtrée*.

### Cas 3 — Filtre WMI

Dans GPMC : **Filtres WMI** → *Nouveau* → nom `Postes-Uniquement`, requête `SELECT * FROM Win32_OperatingSystem WHERE ProductType = 1`. Puis, dans la GPO `Lab-Verrouillage-Ecran` → onglet *Étendue* → *Filtrage WMI* → sélectionner `Postes-Uniquement`. Si vous liez la GPO plus haut (par exemple au domaine), le DC (`ProductType = 2`) ne reçoit plus le verrouillage.

```powershell
gpresult /r /scope computer
```

👉 Explication : sur le DC, la GPO doit apparaître dans la liste des GPO **filtrées** avec la raison « Filtrage WMI ».

### Cas 4 — Appliqué, Bloquer l'héritage et ordre

```powershell
New-GPO -Name "Lab-Domaine-Securite"
Set-GPRegistryValue -Name "Lab-Domaine-Securite" -Key "HKLM\SOFTWARE\Policies\ExampleLab" -ValueName "NiveauSecurite" -Type DWord -Value 1
New-GPLink -Name "Lab-Domaine-Securite" -Target "DC=example,DC=test"
Set-GPInheritance -Target "OU=Postes,OU=Entreprise,DC=example,DC=test" -IsBlocked Yes
```

👉 Explication : crée une GPO marqueur liée au domaine (elle écrit une valeur de test inoffensive), puis bloque l'héritage sur `OU=Postes`. Après `gpupdate /force` sur le poste, `reg query "HKLM\SOFTWARE\Policies\ExampleLab"` ne doit plus trouver la valeur.

```powershell
Set-GPLink -Name "Lab-Domaine-Securite" -Target "DC=example,DC=test" -Enforced Yes
Get-GPInheritance -Target "OU=Postes,OU=Entreprise,DC=example,DC=test"
```

👉 Explication : force le lien au niveau du domaine, puis affiche l'état d'héritage et la liste des liens vus par l'OU. Après un nouveau `gpupdate /force`, la valeur réapparaît : *Appliqué* traverse *Bloquer l'héritage*.

Retour à l'état initial :

```powershell
Set-GPInheritance -Target "OU=Postes,OU=Entreprise,DC=example,DC=test" -IsBlocked No
Remove-GPLink -Name "Lab-Domaine-Securite" -Target "DC=example,DC=test"
```

👉 Explication : annule le blocage et supprime le lien de test (la GPO elle-même reste, vous pouvez la supprimer par `Remove-GPO`).

### Cas 5 — Sauvegarde et nettoyage

```powershell
Backup-GPO -All -Path "C:\GPO-Sauvegardes"
```

👉 Explication : exporte toutes les GPO dans un dossier (créez-le au préalable). Avant toute modification d'une GPO de production, une sauvegarde permet de revenir en arrière avec `Restore-GPO`.

Détruisez ensuite les VM ou restaurez l'instantané.

---

## Exercices

1. **(Ordre)** Un utilisateur est dans `OU=Comptabilite` sous `OU=Utilisateurs`. Une GPO est liée au domaine, une à `Utilisateurs`, une à `Comptabilite`. Classez-les par ordre d'application.
2. **(Conflit)** GPO-D (domaine) règle le verrouillage à 15 min, GPO-O (OU) à 5 min, aucun lien n'est *Appliqué*. Quelle valeur s'applique ? Et si le lien de GPO-D est *Appliqué* ?
3. **(Ordre de liaison)** Deux GPO A (ordre 1) et B (ordre 2) sont liées à la même OU et règlent le même paramètre différemment. Laquelle gagne ?
4. **(Filtrage)** Écrivez, en PowerShell, les commandes pour que la GPO `Lab-Poste` ne s'applique qu'aux ordinateurs du groupe `GG_Postes_Pilote`.
5. **(Panne)** Une GPO utilisateur est liée à `OU=Postes`. Elle ne s'applique pas aux utilisateurs. Pourquoi, et comment corriger ?
6. **(Lecture de sortie)** `gpresult` indique « Filtré : Refus (sécurité) ». Donnez deux causes possibles et une vérification pour chacune.
7. **(Scénario)** Vous devez désactiver le stockage USB uniquement sur les postes de la salle 12 (`OU=Salle12`), sans toucher aux autres. Proposez la solution (GPO, lien, héritage) et le test de validation.

## Corrigés des exercices

1. Local → domaine → `Utilisateurs` → `Comptabilite` ; la GPO de `Comptabilite` est appliquée en dernier.
2. 5 min (l'OU gagne, étant appliquée après). Avec GPO-D en *Appliqué* : 15 min, car un lien Appliqué ne peut pas être écrasé par un niveau inférieur.
3. A (ordre 1) : le lien numéro 1 est appliqué en dernier, donc prioritaire.
4. `Set-GPPermission -Name "Lab-Poste" -TargetName "Authenticated Users" -TargetType Group -PermissionLevel GpoRead` puis `Set-GPPermission -Name "Lab-Poste" -TargetName "GG_Postes_Pilote" -TargetType Group -PermissionLevel GpoApply`. Les ordinateurs doivent être membres du groupe, avec un redémarrage pour mettre à jour leur jeton.
5. Un utilisateur est traité selon sa propre OU, pas celle de son poste. Correction : lier la GPO à l'OU des utilisateurs, ou activer la boucle de rappel (Fusionner ou Remplacer) dans une GPO liée à `OU=Postes`.
6. (a) Le groupe de l'objet n'a pas *Appliquer la stratégie de groupe* : vérifier l'onglet *Délégation* ; (b) l'utilisateur n'a pas ouvert de nouvelle session après son ajout au groupe : vérifier `whoami /groups` avant et après reconnexion.
7. Créer `GPO-Salle12-USB` avec le paramètre de restriction des périphériques de stockage amovibles (configuration ordinateur), la lier à `OU=Salle12` seulement ; vérifier avec `gpresult /r /scope computer` sur un poste de la salle et sur un poste d'une autre OU (il ne doit pas figurer dans la liste), puis tester l'insertion d'une clé USB de test.

## Quiz

**Q1.** Ordre de traitement ? A) OU, domaine, site, local — B) Local, site, domaine, OU — C) Domaine, local, OU, site — D) Site, local, OU, domaine

**Q2.** Deux GPO règlent le même paramètre, sans Appliqué. Laquelle gagne ? A) La première — B) La dernière appliquée — C) La plus ancienne — D) Au hasard

**Q3.** Que fait *Appliqué (Enforced)* ? A) Il désactive la GPO — B) Il empêche un niveau plus bas d'écraser le lien et traverse Bloquer l'héritage — C) Il supprime SYSVOL — D) Il force un redémarrage

**Q4.** Pour qu'une GPO s'applique à un objet par filtrage de sécurité, il faut : A) Contrôle total — B) Lecture et Appliquer la stratégie de groupe — C) Écriture — D) Aucun droit

**Q5.** Une GPO utilisateur liée à l'OU des ordinateurs : A) S'applique toujours — B) Ne s'applique pas sans boucle de rappel — C) S'applique aux administrateurs seulement — D) Bloque l'ordinateur

**Q6.** Rafraîchissement par défaut d'un poste membre ? A) 5 min — B) 90 min + décalage aléatoire jusqu'à 30 min — C) 24 h — D) Jamais

**Q7.** Commande pour afficher les GPO appliquées et filtrées ? A) `gpupdate /r` — B) `gpresult /r` — C) `nltest /gpo` — D) `ipconfig /gpo`

**Q8.** Un filtre WMI s'applique si : A) La requête renvoie au moins un résultat — B) Elle renvoie 0 — C) Le poste est un DC — D) La GPO est Appliquée

**Q9.** Où est stocké le modèle (fichiers) d'une GPO ? A) Dans le registre du client — B) Dans SYSVOL — C) Dans le DNS — D) Dans le profil utilisateur

**Q10.** Pourquoi éviter de modifier la Default Domain Policy à tout propos ? A) Elle est en lecture seule — B) Pour garder des réglages isolés, nommés et faciles à annuler — C) Elle ne s'applique qu'aux serveurs — D) Elle est ignorée

### Réponses justifiées

1. **B** — LSDOU : local, site, domaine, OU (parent puis enfant).
2. **B** — Le dernier appliqué l'emporte en cas de conflit.
3. **B** — Appliqué verrouille le lien vers le bas ; il traverse aussi Bloquer l'héritage.
4. **B** — Il faut à la fois Lecture et Appliquer la stratégie de groupe.
5. **B** — Un utilisateur suit la chaîne d'OU de son propre compte ; seule la boucle de rappel change cela.
6. **B** — 90 minutes avec décalage aléatoire de 0 à 30 minutes (5 minutes sur les DC).
7. **B** — `gpresult /r` liste les GPO appliquées et celles qui ont été filtrées.
8. **A** — La requête WQL doit retourner au moins une instance.
9. **B** — Le GPT est dans `SYSVOL\<domaine>\Policies\{GUID}` ; le GPC est dans l'annuaire.
10. **B** — Des GPO dédiées facilitent le test, l'audit et le retour arrière ; les stratégies de compte, elles, restent dans la Default Domain Policy.

## Erreurs fréquentes et dépannage

| Symptôme | Cause probable | Vérification (lecture seule) | Action |
| --- | --- | --- | --- |
| La GPO n'apparaît nulle part dans `gpresult` | Lien sur la mauvaise OU, objet dans `CN=Computers` | `Get-ADComputer PC-W11-01 \| Select DistinguishedName` | Déplacer l'objet ou ajouter le lien |
| « Filtrée : Refus (sécurité) » | Droit *Appliquer* absent ou ajout de groupe sans reconnexion | Onglet *Délégation*, `whoami /groups` | Corriger la délégation, rouvrir la session |
| GPO d'utilisateur ignorée après durcissement des permissions | *Lecture* retirée à Utilisateurs authentifiés (MS16-072) | `Get-GPPermission -Name X -All` | Redonner *Lecture* |
| Réglage inversé le lendemain | Une GPO d'un niveau inférieur l'écrase | `gpresult /h` (colonne « GPO gagnante ») | Ajuster l'ordre ou supprimer le doublon |
| Effets différents selon le DC | Réplication SYSVOL ou AD en retard | `dcdiag /test:sysvolcheck`, `repadmin /replsummary` | Attendre ou traiter la réplication |
| Retard important à l'ouverture de session | Trop de GPO, filtres WMI lents, liens WAN | Journal GroupPolicy (durées) | Simplifier, regrouper, désactiver les moitiés vides |

Règle d'or : **tester d'abord sur une OU pilote** ; sauvegarder (`Backup-GPO`) avant de changer.

## À retenir

- Une GPO = GPC (annuaire) + GPT (SYSVOL), liée à site, domaine ou OU.
- **LSDOU** : le dernier appliqué gagne ; au même niveau, ordre de liaison 1 = prioritaire.
- **Appliqué** > **Bloquer l'héritage** ; réservez Appliqué à ce qui est non négociable.
- Un objet suit **sa propre** chaîne d'OU ; la **boucle de rappel** change cela pour la partie utilisateur.
- Filtrage de sécurité : *Lecture* à tous, *Appliquer* au groupe cible ; WMI en dernier recours.
- Dépannage : `gpupdate /force`, `gpresult /r` (surtout la liste des GPO filtrées), `/h` pour le détail, journal GroupPolicy.
- Toujours sauvegarder, nommer par fonction, tester sur une OU pilote.

## Pour aller plus loin

- Microsoft Learn — Traitement des stratégies de groupe : <https://learn.microsoft.com/windows-server/identity/ad-ds/manage/group-policy/group-policy-processing>
- Microsoft Learn — Guide de dépannage de l'application des GPO : <https://learn.microsoft.com/troubleshoot/windows-server/group-policy/applying-group-policy-troubleshooting-guidance>
- Microsoft Learn — `gpresult` : <https://learn.microsoft.com/windows-server/administration/windows-commands/gpresult>
- Microsoft Learn — `gpupdate` : <https://learn.microsoft.com/windows-server/administration/windows-commands/gpupdate>
- Microsoft Learn — Module PowerShell GroupPolicy : <https://learn.microsoft.com/powershell/module/grouppolicy/>

## Crédits des images

| Fichier | Source | Auteur | Licence | Modifications |
| --- | --- | --- | --- | --- |
| `images/gpo-1.svg` | Création originale du projet Pack Master | Projet Pack Master | Dédiée au domaine public (CC0) — <https://creativecommons.org/publicdomain/zero/1.0/> | Sans objet |
| `images/gpo-2.svg` | Création originale du projet Pack Master | Projet Pack Master | Dédiée au domaine public (CC0) — <https://creativecommons.org/publicdomain/zero/1.0/> | Sans objet |
| `images/gpo-3.svg` | Création originale du projet Pack Master | Projet Pack Master | Dédiée au domaine public (CC0) — <https://creativecommons.org/publicdomain/zero/1.0/> | Sans objet |

Aucune image tierce n'a été retenue : la recherche sur Wikimedia Commons n'a pas fourni de ressource libre adaptée (seule une icône de produit propriétaire est apparue, exclue par la charte). Les trois schémas sont donc des créations originales.

## Historique de vérification

| Date | OS/logiciel | Testeur | Verdict |
| --- | --- | --- | --- |
| 2026-11-01 | Windows Server (AD DS, GPMC), client Windows | Rédaction assistée (Copilot) | Non testé sur plateforme cible |

Remarque : aucune commande n'a été exécutée sur Windows. Seule la validité XML des schémas SVG a été contrôlée localement.