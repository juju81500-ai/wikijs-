---
title: "Leçon — Méthode de dépannage structurée : questionner, reproduire, isoler, tester, documenter"
description: "À l'issue de cette leçon, vous saurez :"
published: true
date: 2026-11-03T14:22:28Z
tags: ["transverse", "tout-en-un", "lecon", "support", "depannage", "methode", "diagnostic"]
editor: markdown
dateCreated: 2026-11-03T14:22:28Z
dateModified: 2026-11-03T14:22:28Z
---

# Leçon — Méthode de dépannage structurée : questionner, reproduire, isoler, tester, documenter

- **Tags** : `transverse`, `tout-en-un`, `lecon`, `support`, `depannage`, `methode`, `diagnostic`
- **Niveau** : débutant à intermédiaire (technicien support N1/N2, étudiant [[Glossary:TSSR]])
- **Durée estimée** : 3 h 30 (lecture 1 h 30, laboratoire 1 h, exercices et quiz 1 h)

---

## Objectifs pédagogiques

À l'issue de cette leçon, vous saurez :

1. Recueillir un signalement exploitable en distinguant **faits observés** et **interprétations**.
2. **Reproduire** un défaut de façon fiable, ou expliquer pourquoi c'est impossible et comment contourner la difficulté.
3. **Isoler** la zone fautive par comparaison, par dichotomie et par raisonnement en couches.
4. Formuler, classer et **tester des hypothèses** en ne changeant qu'une chose à la fois, avec retour arrière.
5. Suivre un **arbre de décision** (réseau, lenteur, application qui ne démarre plus) et en construire un pour votre contexte.
6. **Documenter** l'intervention de manière à ce qu'un collègue puisse la rejouer sans vous.

## Prérequis et durée

- Notions sur un poste Windows ou Linux, l'adressage [[Glossary:IP]] et le [[Glossary:DNS]] ; savoir ouvrir un terminal.
- Une **machine virtuelle jetable** pour la mise en pratique (aucune machine de production).
- Durée totale : environ 3 h 30.

## L'essentiel en bref

- Dépanner, c'est **réduire l'incertitude** : questionner → reproduire → isoler → hypothèses → tester → documenter, avec retour aux hypothèses tant que la cause n'est pas confirmée.
- **Un seul changement à la fois**, réversible, noté.
- Commencer par le **probable, rapide et sans risque**.
- 
![Cycle de dépannage en six étapes : questionner, reproduire, isoler, hypothèses, tester, documenter, avec une boucle de retour vers les hypothèses](images/methode-depannage-1.svg)

*Figure 1 — Le cycle de dépannage : la flèche pointillée rappelle qu'une hypothèse infirmée n'est pas un échec, c'est une information.*

---

## 1. Pourquoi une méthode ? L'analogie du médecin

Un médecin qui reçoit un patient ne prescrit pas immédiatement une opération. Il **interroge** (« depuis quand ? à quel moment ? »), **observe**, **examine** (température, tension), pense à plusieurs causes possibles, demande un examen complémentaire, puis traite et **note** dans le dossier. Il évite aussi d'administrer trois traitements simultanés : il ne saurait pas lequel a fonctionné, ni lequel a provoqué un effet indésirable.

Le technicien de support tombe dans trois pièges : le **geste réflexe** (redémarrer, réinstaller : on ignore pourquoi cela marche), le **tâtonnement** (cinq réglages à la fois) et la **fixation** sur la première idée. > **Principe directeur** : un bon test est un test dont **chaque résultat possible** vous apprend quelque chose. Si, quel que soit le résultat, vous ne changerez pas votre plan, le test est inutile.

## 2. Questionner : transformer un signalement en faits

### 2.1 Le premier message est rarement exploitable

« Ça ne marche pas » mélange symptôme, cause supposée et émotion. Votre travail est de le convertir en une description que n'importe quel collègue comprendrait. Pour cela, la grille classique **QQOQCCP** (Qui, Quoi, Où, Quand, Comment, Combien, Pourquoi) est utile, à condition de la poser en langage naturel.

| Dimension | Question à poser | Exemple de réponse exploitable |
|---|---|---|
| Quoi | Que voyez-vous exactement à l'écran ? Pouvez-vous recopier le message ? | « Erreur : impossible de se connecter au serveur » |
| Qui | Combien de personnes sont touchées ? Y a-t-il un collègue à côté qui n'a pas le problème ? | « Moi seul dans le bureau » |
| Quand | Depuis quand ? Une heure précise ? Tout le temps ou par moments ? | « Depuis 9 h 10, de façon continue » |
| Comment | Que faisiez-vous juste avant ? Qu'est-ce qui a changé (mise à jour, déplacement, nouveau mot de passe) ? | « Redémarrage après mises à jour hier soir » |
| Contournement | Existe-t-il un moyen de continuer à travailler ? | « Oui, via le portail web » |

### 2.2 Faits et interprétations

Séparez systématiquement ce qui est **observé** de ce qui est **supposé**.

```text
Signalement brut     : "Le serveur est en panne, rien ne s'ouvre depuis ce matin."
Faits                : - Message "délai d'attente dépassé" sur le partage \\srv-fichiers.example.test
                       - Constaté à 09:10 par l'utilisateur, poste PC-042
                       - La messagerie fonctionne
Interprétation       : "Le serveur est en panne" (non vérifiée)
Première hypothèse   : problème de résolution de nom OU de joignabilité du serveur de fichiers
```

👉 Explication : ce gabarit force à isoler le symptôme exact (un partage précis, un message précis) avant d'évoquer la moindre cause. Ici, « rien ne s'ouvre » devient « un seul partage expire, la messagerie fonctionne ».

### 2.3 Bonnes pratiques d'entretien

- Posez des questions ouvertes d'abord, fermées ensuite, puis **reformulez** pour validation.
- Ne jugez pas : l'utilisateur ne mentionnera son changement que s'il se sent en confiance.
- Demandez une preuve (texte exact de l'erreur, heure, capture recadrée).
- Cherchez le **changement récent** : la majorité des pannes en suit un.

## 3. Reproduire : rendre le défaut observable

Un défaut que l'on peut déclencher à la demande est déjà à moitié résolu. Reproduire sert à trois choses : **confirmer** que le problème existe, **mesurer** (avant/après correction) et **tester** sans dépendre de l'humeur de l'utilisateur.

### 3.1 Niveaux de reproduction

Reproduisez avec l'utilisateur (à distance, avec son accord), puis seul sur son poste, puis sur un poste de référence ou une [[Glossary:VM]]. Pour un défaut **intermittent**, on capture (journaux, mesures régulières) jusqu'à obtenir une occurrence horodatée à corréler avec d'autres événements.

### 3.2 Pièges et minimum reproductible

- « Chez moi ça marche » n'accuse pas l'utilisateur : la différence entre les deux contextes *est* l'indice.
- Un défaut qui disparaît quand vous arrivez révèle un état transitoire (cache, verrou, session) : notez-le.
- Ne reproduisez pas en production avec des données réelles (courriel envoyé, commande validée).
- Réduisez la manipulation au minimum : « ouvrir le document X depuis le partage Y avec le compte Z » vaut mieux que « utiliser l'application une heure ».

## 4. Isoler : réduire le périmètre

Isoler consiste à **partitionner** l'ensemble des causes possibles en deux groupes et à déterminer lequel contient la panne, puis à recommencer. C'est la dichotomie appliquée à l'informatique.

### 4.1 Comparer : le bon contre le mauvais

La question la plus rentable : **qu'est-ce qui diffère entre ce qui fonctionne et ce qui ne fonctionne pas ?**

| Comparaison | Si le problème suit… | Alors la cause est plutôt… |
|---|---|---|
| Même compte, autre poste | le compte | profil, droits, configuration utilisateur |
| Autre compte, même poste | le poste | système, pilote, réseau local, logiciel |
| Même poste, autre réseau (câble ↔ Wi-Fi, [[Glossary:VPN]] ↔ site) | le réseau | segment, [[Glossary:VLAN]], filtrage, DNS |
| Même poste, autre application | l'application | version, configuration, dépendance |

### 4.2 Raisonner en couches

Les systèmes s'empilent (application, session, système, réseau, matériel) : une panne se situe dans une couche et se voit dans celles du dessus. On vérifie **du bas vers le haut** (« plus rien ne marche »), **du haut vers le bas** (un seul service touché) ou **au milieu** en testant une couche intermédiaire pour couper l'espace de recherche en deux.

![Modèle en couches : application, session, système, réseau, matériel, avec flèches remonter et descendre](images/methode-depannage-3.svg)

*Figure 2 — Isoler par couches : chaque test valide ou élimine une couche entière.*

### 4.3 Dichotomie

Avec 16 causes équiprobables, un test qui les sépare en 8 + 8 puis encore en deux : quatre tests suffisent. D'où la règle : tester d'abord du **large** (« le poste joint-il une IP externe ? »), ensuite du fin. Restez en **lecture seule** pendant l'isolement et comparez avec un poste de référence ou un profil de test plutôt que de modifier le poste de l'utilisateur.

## 5. Formuler des hypothèses

### 5.1 Une hypothèse est une phrase testable

Mal formulée : « C'est le réseau. » Bien formulée : « Le poste n'obtient plus d'adresse [[Glossary:DHCP]], donc il se retrouve en 169.254.x.x et ne joint aucun serveur. » La seconde indique **ce qu'on devrait observer** si elle est vraie, donc comment la tester.

### 5.2 Trois critères de tri

Testez d'abord ce qui cumule **forte probabilité** (un changement récent l'explique), **test rapide** (lire un journal : 1 min ; réinstaller : 1 h) et **risque faible** (redémarrer un service plutôt que supprimer un profil).

### 5.3 Deux principes opposés

**Rasoir d'Occam** : essayez d'abord l'explication la plus simple. **Principe de Hickam** : plusieurs pannes peuvent coexister ; si le correctif n'explique qu'une partie des symptômes, cherchez une seconde cause. Contre le biais de confirmation, écrivez *avant* le test ce qui infirmerait l'hypothèse (« si le ping de la passerelle réussit, l'hypothèse "pas de lien local" est fausse »).

## 6. Tester : un changement à la fois, réversible

### 6.1 Règles d'or et garde-fous

1. **Un seul changement par test**, sinon l'effet est inattribuable.
2. **Noter l'état initial** et prévoir le **retour arrière** avant d'agir.
3. **Mesurer** avec un critère de succès clair (« le partage s'ouvre en moins de 3 secondes ») et **informer** l'utilisateur.

Pour toute modification sensible (serveur, équipement réseau, poste critique) : **snapshot ou sauvegarde préalable**, **accès console de secours** (console hyperviseur, accès hors bande, autre administrateur joignable : ne modifiez jamais la configuration réseau d'une machine accessible uniquement par le réseau sans moyen de reprise), **test sur un périmètre restreint**, retour arrière vérifié et fenêtre de changement validée en production.

### 6.2 Commandes de diagnostic de base

Les commandes ci-dessous sont en **lecture seule** : elles observent sans modifier. Les adresses utilisées appartiennent aux plages de documentation (192.0.2.0/24, 198.51.100.0/24, 203.0.113.0/24).

**Windows (PowerShell)**

```powershell
Get-NetIPConfiguration
```

👉 Explication : affiche, pour chaque interface, l'adresse IP, la passerelle et les serveurs DNS. Une adresse en 169.254.x.x trahit l'absence de réponse DHCP.

```powershell
Test-NetConnection -ComputerName 192.0.2.1
```

👉 Explication : envoie un test [[Glossary:ICMP]] vers la passerelle supposée (adresse de documentation à remplacer en laboratoire) et indique si elle répond ; premier test de la couche réseau locale.

```powershell
Resolve-DnsName -Name www.example.com
```

👉 Explication : interroge le DNS configuré et affiche l'adresse obtenue ; sépare un problème de **nom** d'un problème de **joignabilité**.

```powershell
Test-NetConnection -ComputerName www.example.com -Port 443
```

👉 Explication : vérifie qu'un port [[Glossary:TCP]] précis (ici HTTPS) est joignable ; la ligne `TcpTestSucceeded` donne le verdict.

```powershell
Get-WinEvent -LogName System -MaxEvents 20
```

👉 Explication : liste les 20 derniers événements du journal Système, à corréler avec l'heure du début du problème.

**Linux (shell)**

```bash
ip -br address
```

👉 Explication : affiche en une ligne par interface l'état (UP/DOWN) et les adresses ; vérifie la couche lien et l'adressage.

```bash
ping -c 3 192.0.2.1
```

👉 Explication : envoie trois requêtes ICMP vers la passerelle présumée (adresse de documentation) ; la perte de paquets ou le délai indique si le lien local fonctionne.

```bash
dig +short www.example.com
```

👉 Explication : interroge le DNS et n'affiche que la réponse ; une sortie vide ou un délai d'attente oriente vers le DNS.

```bash
curl -sS -I --max-time 5 https://www.example.com/
```

👉 Explication : demande uniquement les en-têtes [[Glossary:HTTP]] avec un délai maximal de 5 secondes ; teste la chaîne complète (DNS, TCP, [[Glossary:TLS]], HTTP) et le message d'erreur distingue les cas.

```bash
journalctl -p warning --since "30 min ago" --no-pager | tail -n 30
```

👉 Explication : affiche les avertissements et erreurs des 30 dernières minutes (30 dernières lignes) pour les confronter à la panne.

### 6.3 Lire le résultat d'un test

Un test a trois issues : **confirme**, **infirme** ou **est non concluant** (résultat ambigu, test mal choisi). Ne forcez pas un résultat non concluant vers l'un des deux autres. Notez-le et choisissez un test plus discriminant.

| Observation avec `curl` | Signification probable |
|---|---|
| `Could not resolve host` | Échec de résolution DNS |
| `Connection refused` (réponse immédiate) | La machine répond mais **aucun service n'écoute** sur ce port |
| `Connection timed out` (attente) | Paquets perdus : pare-feu qui jette, route absente, machine éteinte |
| Code HTTP 5xx | Panne côté serveur/application |

## 7. Arbres de décision

Un arbre de décision capitalise l'expérience : une suite de **questions fermées**, chacune orientant vers une action ou une autre question. Il sert à former les nouveaux, à homogénéiser les pratiques et à ne rien oublier un jour de stress.

### 7.1 Arbre « service inaccessible depuis un poste »

![Arbre de décision en cinq questions : IP valide, passerelle joignable, DNS, port, compte ou serveur](images/methode-depannage-2.svg)

*Figure 3 — Arbre de décision pour un service inaccessible : on descend tant que la réponse est « oui », on s'arrête et on traite dès le premier « non ».*

Version textuelle à copier dans une procédure :

```text
1. IP valide ?          NON -> lien, DHCP, VLAN.            OUI -> 2
2. Passerelle répond ?  NON -> LAN local (câble, port).     OUI -> 3
3. Nom résolu ?         NON -> DNS (serveurs, cache).       OUI -> 4
4. Port joignable ?     NON -> pare-feu, service, route.    OUI -> 5
5. Autre compte/poste réussit ? OUI -> compte ou poste. NON -> serveur : escalader avec preuves.
```

👉 Explication : chaque étape élimine une couche ; on s'arrête au premier « non » et on traite avant de poursuivre.

### 7.2 Autres arbres

Sur le même modèle, écrivez un arbre « le poste est lent » (général ou ciblé ? ressource saturée ? lenteur récente ?) ou « l'application ne démarre plus » (message ? nouveau profil ? mise à jour récente ? journaux ?). La première question doit toujours être la plus discriminante : le périmètre.

### 7.3 Construire son propre arbre

1. Partez d'un **symptôme précis** (pas d'un domaine entier).
2. Listez les causes réelles rencontrées (tickets passés).
3. Ordonnez les questions de la plus **discriminante et rapide** à la plus fine.
4. Terminez chaque branche par une **action** ou une **escalade avec contenu attendu**.
5. **Testez l'arbre** sur trois anciens tickets, puis révisez-le après chaque cas qu'il ne résout pas.

## 8. Documenter : écrire pour le prochain technicien

### 8.1 Pourquoi et quand

On note **pendant** le dépannage (notes datées) : un collègue peut reprendre le ticket. À la clôture, on rédige la synthèse.

### 8.2 Modèle de note de ticket

```text
Symptôme (faits)       : ...
Début / périmètre      : ... (heure avec fuseau, nombre d'utilisateurs, site)
Hypothèses testées     : H1 ... -> infirmée (preuve) ; H2 ... -> confirmée (preuve)
Cause                  : ...
Action corrective      : ... (commande ou procédure exacte)
Retour arrière         : ...
Vérification           : critère de succès constaté, par qui, quand
Recommandation         : correctif durable, article de base de connaissances à créer
```

👉 Explication : conserver les hypothèses **infirmées** évite qu'un collègue refasse les mêmes tests, et sert de matière à la base de connaissances.

### 8.3 Ce qu'il ne faut pas écrire

Aucun secret (mot de passe, jeton, clé), aucune donnée personnelle inutile, des captures recadrées.

### 8.4 Escalade et savoir collectif

Après un incident, demandez-vous ce qui aurait permis de résoudre plus vite : la réponse nourrit la base de connaissances. En escaladant, joignez le dossier complet (faits, preuves, tests, modifications) et restez dans le cadre : droits d'accès, aucun contournement de sécurité, autorisation avant toute prise en main à distance.

---

## Mise en pratique guidée

**Cadre** : machine virtuelle Linux **jetable** (aucune machine de production), sans accès à des réseaux de laboratoire partagés. Avant de commencer, prenez un **snapshot** de la VM et vérifiez que vous disposez de la **console de l'hyperviseur** : elle vous permettra de reprendre la main si une manipulation réseau coupe l'accès distant. Les commandes ci-dessous n'effectuent que des lectures ou lancent un petit service local.

### Atelier 1 — Distinguer « service arrêté » et « paquets perdus »

1. Dans un premier terminal, démarrez un petit serveur web local :

```bash
python3 -m http.server 8080 --bind 127.0.0.1
```

👉 Explication : lance un serveur HTTP écoutant uniquement sur l'interface locale, port 8080 ; il simule le « service » à dépanner. Le terminal reste occupé.

2. Dans un second terminal, testez-le :

```bash
curl -sS -o /dev/null -w "%{http_code}\n" --max-time 5 http://127.0.0.1:8080/
```

👉 Explication : affiche uniquement le code HTTP (attendu : 200) ; c'est votre état « sain » de référence.

3. Arrêtez le serveur (Ctrl+C dans le premier terminal) et relancez la même commande `curl`.

```bash
curl -sS -o /dev/null -w "%{http_code}\n" --max-time 5 http://127.0.0.1:8080/
```

👉 Explication : vous obtenez « Connection refused » immédiatement : la machine répond, mais plus aucun service n'écoute. Notez le **délai** : quasi nul.

4. Interrogez une adresse de documentation qui ne répond pas :

```bash
curl -sS -o /dev/null --max-time 5 http://192.0.2.1:8080/
```

👉 Explication : l'adresse 192.0.2.1 n'est pas routée ; la commande attend 5 secondes puis signale un délai dépassé (ou « Network is unreachable » selon l'environnement). Comparez avec l'étape précédente : « refusé » ≠ « sans réponse ».

**Questions** : quelle couche suspecteriez-vous dans chaque cas ? (Réponse attendue : service arrêté ou mal lié pour le cas 3 ; routage, filtrage ou machine éteinte pour le cas 4.)

### Atelier 2 — Séparer le nom de la joignabilité

```bash
dig +time=2 +tries=1 @192.0.2.53 www.example.com
```

👉 Explication : interroge un serveur DNS fictif (adresse de documentation) avec un délai de 2 secondes et une seule tentative ; la sortie « no servers could be reached » illustre un DNS injoignable, distinct d'un nom inexistant (NXDOMAIN).

```bash
getent hosts localhost
```

👉 Explication : résout un nom via la configuration locale du système (fichier hosts) ; contrôle témoin pour confirmer que la résolution locale fonctionne indépendamment du DNS distant.

### Atelier 3 — Rédiger une note de clôture

Remplissez le modèle de la section 8.2 pour l'un des ateliers, puis relisez-le comme un collègue qui ne connaît pas l'atelier.

**Retour arrière** : aucune configuration n'a été modifiée ; fermez les terminaux et restaurez au besoin le snapshot initial.

---

## Exercices

1. **Faits ou interprétations ?** Classez ces phrases : (a) « Le serveur est tombé. » (b) « Le message affiché est : accès refusé. » (c) « Ça a dû être la mise à jour. » (d) « Depuis 8 h 45 mon collègue a le même message. »
2. **Questions de cadrage.** Un utilisateur écrit : « L'imprimante ne fonctionne pas. » Rédigez cinq questions, de la plus large à la plus précise, que vous poseriez.
3. **Comparaison.** Un utilisateur ne peut plus ouvrir son application métier. Le même compte fonctionne sur le poste d'un collègue, et le collègue réussit aussi sur le poste de l'utilisateur. Où est la cause probable ? Justifiez.
4. **Lire un test.** Trois commandes `curl` renvoient respectivement : « Could not resolve host », « Connection refused », « Operation timed out ». Associez chaque résultat à une famille de causes.
5. **Classer des hypothèses.** Pour « plus d'Internet sur un poste après une coupure de courant », proposez quatre hypothèses et classez-les selon probabilité, coût du test et risque.
6. **Changement unique.** On vous propose, pour un partage inaccessible, de « vider le cache DNS, redémarrer le poste, réinitialiser la pile réseau et changer le câble » en une seule intervention. Critiquez et proposez un ordre de test.
7. **Construire un arbre.** Écrivez un arbre de décision de six questions maximum pour « le Wi-Fi est connecté mais aucune page web ne s'ouvre ».
8. **Note de clôture.** Rédigez la note de l'atelier 1 avec le modèle de la section 8.2.

## Corrigés des exercices

1. (a) interprétation ; (b) fait ; (c) interprétation ; (d) fait (périmètre : au moins deux personnes, heure précise). Conséquence : le périmètre n'est pas limité à un seul poste.
2. Exemple : (1) « Que se passe-t-il exactement quand vous imprimez ? » ; (2) « Quel message voyez-vous ? » ; (3) « Une seule imprimante ou toutes ? » ; (4) « Cela fonctionnait-il avant, et qu'est-ce qui a changé ? » ; (5) « Un collègue imprime-t-il sur la même imprimante ? ».
3. Ni le compte seul ni le poste seul ne sont en cause (chacun fonctionne avec un autre partenaire) : le défaut n'apparaît que dans la **combinaison** compte + poste : profil utilisateur local, cache, droits, configuration propre à cette association. Piste : tester avec un nouveau profil sur le poste.
4. « Could not resolve host » : DNS (serveur injoignable, suffixe, nom erroné). « Connection refused » : la machine répond mais aucun service n'écoute sur ce port (service arrêté, mauvais port). « Operation timed out » : paquets perdus (pare-feu qui jette, route manquante, machine éteinte).
5. Exemple : H1 lien non rétabli (probable, test immédiat, risque nul) ; H2 pas de bail DHCP (probable, lire l'adresse) ; H3 commutateur ou DHCP encore hors service (moyenne, comparer avec un autre poste) ; H4 profil réseau corrompu (faible, long, risque modéré). Ordre : H1, H2, H3, H4.
6. Quatre changements simultanés empêchent d'attribuer l'effet et le redémarrage efface des preuves. Ordre : lire les faits (IP, passerelle, résolution), puis une seule action ciblée, mesurer, et seulement en cas d'échec passer à la suivante.
7. Exemple : IP valide ? → passerelle joignable ? → IP externe joignable ? → nom résolu ? → proxy configuré ? → portail d'authentification affiché en HTTP simple ?
8. Symptôme : « Connection refused » sur 127.0.0.1:8080 ; H1 service arrêté (confirmée) ; H2 filtrage (infirmée : refus immédiat) ; correctif : redémarrer le serveur ; retour arrière sans objet ; vérification : code 200.

## Quiz

**Q1. Quel est l'objectif principal de l'étape « questionner » ?**
A. Trouver un coupable. B. Transformer un signalement en faits exploitables. C. Rassurer l'utilisateur uniquement. D. Choisir le correctif.
**Réponse : B.** L'entretien sert à établir des faits (quoi, quand, où, qui, changement récent) ; chercher un coupable ou un correctif à ce stade est prématuré.

**Q2. Pourquoi reproduire le défaut ?**
A. Pour impressionner l'utilisateur. B. Pour confirmer, mesurer et tester le correctif. C. Pour éviter de documenter. D. Pour supprimer les journaux.
**Réponse : B.** Un défaut reproductible permet de comparer avant/après correction.

**Q3. Le même compte fonctionne sur un autre poste, mais un autre compte échoue sur le poste concerné. Que suggère cela ?**
A. Un problème de compte. B. Un problème de poste. C. Un problème applicatif côté serveur. D. Rien.
**Réponse : B.** Le problème suit le poste, non le compte : système, pilote, réseau local ou logiciel du poste.

**Q4. Quel est l'intérêt d'une dichotomie ?**
A. Tester toutes les causes une par une. B. Réduire rapidement le périmètre en séparant les causes en deux groupes. C. Éviter de noter les résultats. D. Remplacer l'arbre de décision.
**Réponse : B.** Chaque test large élimine environ la moitié des causes.

**Q5. « Connection refused » reçu immédiatement signifie le plus souvent que :**
A. Un pare-feu jette silencieusement les paquets. B. La machine répond mais aucun service n'écoute sur ce port. C. Le DNS est en panne. D. Le câble est débranché.
**Réponse : B.** Un refus immédiat provient de la machine cible ; une attente suivie d'un délai suggère plutôt des paquets perdus.

**Q6. Pourquoi ne faire qu'un changement à la fois ?**
A. Par habitude. B. Pour pouvoir attribuer l'effet observé à une cause et revenir en arrière. C. Parce que les outils l'imposent. D. Pour allonger l'intervention.
**Réponse : B.** Plusieurs changements simultanés brouillent la causalité et compliquent le retour arrière.

**Q7. Quelle hypothèse tester en premier ?**
A. La plus spectaculaire. B. La plus probable, rapide à tester et sans risque. C. La plus coûteuse. D. La dernière de la liste.
**Réponse : B.** On cumule probabilité, faible coût et faible risque.

**Q8. Le « principe de Hickam » invite à :**
A. Toujours choisir l'explication la plus simple. B. Envisager que plusieurs pannes coexistent. C. Ignorer les journaux. D. Réinstaller le système.
**Réponse : B.** Si un correctif n'explique qu'une partie des symptômes, il peut y avoir une seconde cause.

**Q9. Avant de modifier la configuration réseau d'un serveur à distance, que prévoir ?**
A. Rien. B. Snapshot, accès console de secours et retour arrière. C. Un redémarrage. D. Un mot de passe par courriel.
**Réponse : B.** Sans accès de secours, une erreur peut vous couper de la machine.

**Q10. Que doit contenir une note de clôture ?**
A. Les mots de passe. B. Symptôme, hypothèses, cause, correctif, retour arrière, vérification. C. Uniquement « résolu ». D. Tout l'écran de l'utilisateur.
**Réponse : B.** La note doit permettre de rejouer et de capitaliser ; elle ne contient ni secret ni donnée inutile.

## Erreurs fréquentes et dépannage

| Erreur | Conséquence | Remède |
|---|---|---|
| Redémarrer d'abord, par réflexe | Perte des preuves et du contexte | Relever d'abord l'état (adresse, journaux, processus), puis agir |
| Changer plusieurs paramètres à la fois | Cause inconnue, risque de récidive | Un changement par test, notés |
| Confondre « refusé » et « sans réponse » | Mauvaise couche suspectée | Lire le message et mesurer le délai |
| Ne pas noter les hypothèses infirmées | Tests refaits par le suivant | Les consigner avec la preuve |

**Si vous êtes bloqué** : revenez aux faits, cherchez le dernier changement, comparez avec un système sain et reprenez la dichotomie plus large.

## À retenir

- Questionner, reproduire, isoler, hypothèses, tester, documenter : réduire l'incertitude par étapes.
- Distinguez faits et interprétations ; le **changement récent** est le meilleur indice.
- Comparez le bon et le mauvais, raisonnez en couches, procédez par dichotomie.
- **Un changement à la fois**, avec snapshot, accès de secours et retour arrière.
- Un arbre de décision capitalise l'expérience ; une note de clôture la transmet.

## Pour aller plus loin

- `Test-NetConnection` : <https://learn.microsoft.com/powershell/module/nettcpip/test-netconnection>
- `Get-WinEvent` : <https://learn.microsoft.com/powershell/module/microsoft.powershell.diagnostics/get-winevent>
- `journalctl` : <https://www.freedesktop.org/software/systemd/man/latest/journalctl.html>
- RFC 5737 : <https://www.rfc-editor.org/rfc/rfc5737>

## Crédits des images

| Fichier | Source (URL Commons) | Auteur | Licence (nom + URL) | Modifications |
|---|---|---|---|---|
| `images/methode-depannage-1.svg` | Création originale (aucune source externe) | Projet Pack Master | CC0 1.0 — <https://creativecommons.org/publicdomain/zero/1.0/> | Sans objet |
| `images/methode-depannage-2.svg` | Création originale (aucune source externe) | Projet Pack Master | CC0 1.0 — <https://creativecommons.org/publicdomain/zero/1.0/> | Sans objet |
| `images/methode-depannage-3.svg` | Création originale (aucune source externe) | Projet Pack Master | CC0 1.0 — <https://creativecommons.org/publicdomain/zero/1.0/> | Sans objet |

Création originale du projet Pack Master, dédiée au domaine public (CC0). Aucune image Commons retenue : l'[[Glossary:API]] de Commons renvoyait HTTP 429 lors de la recherche.

## Historique de vérification

| Date | OS/logiciel | Testeur | Verdict |
|---|---|---|---|
| 2026-11-01 | Windows 10/11, Linux (commandes de diagnostic standard) | Rédaction assistée (Copilot) | Non testé sur plateforme cible |