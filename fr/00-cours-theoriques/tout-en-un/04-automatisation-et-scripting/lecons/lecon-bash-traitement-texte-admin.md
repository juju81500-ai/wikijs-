---
title: "Leçon — Traitement de texte pour l'administrateur : grep, sed, awk, cut, sort, uniq, find et xargs sur journaux et inventaires"
description: "À la fin de cette leçon, vous serez capable de :"
published: true
date: 2026-11-03T09:36:13Z
tags: ["transverse", "tout-en-un", "lecon", "automatisation", "bash", "grep", "sed", "awk", "find", "xargs", "journaux", "inventaire"]
editor: markdown
dateCreated: 2026-11-03T09:36:13Z
dateModified: 2026-11-03T09:36:13Z
---

# Leçon — Traitement de texte pour l'administrateur : grep, sed, awk, cut, sort, uniq, find et xargs sur journaux et inventaires

- **Tags** : `transverse`, `tout-en-un`, `lecon`, `automatisation`, `bash`, `grep`, `sed`, `awk`, `find`, `xargs`, `journaux`, `inventaire`
- **Niveau** : Débutant à intermédiaire (bases de Bash : tubes et redirections)
- **Durée estimée** : 4 h (cours 1 h 45, laboratoire 1 h 15, exercices et quiz 1 h)

---

## Objectifs pédagogiques

À la fin de cette leçon, vous serez capable de :

1. composer des **tubes** d'outils simples pour répondre à une question sur un journal ou un inventaire ;
2. filtrer avec **`grep`** (motifs simples et étendus, comptage, inversion) ;
3. extraire et trier avec **`cut`**, **`sort`**, **`uniq`**, **`wc`**, **`head`**, **`tr`** ;
4. transformer avec **`sed`** (substitution, plage de lignes, modification en place **avec copie de sécurité**) ;
5. calculer avec **`awk`** (champs, conditions, compteurs, sommes, tableaux associatifs) ;
6. rechercher des fichiers avec **`find`** et agir dessus avec **`xargs`** ou `-exec`, y compris pour des noms contenant des espaces ;
7. choisir le bon outil selon la question posée.

## Prérequis et durée

- Leçon « Bash pour débuter » (tubes, redirections, quoting) : [lecon-bash-debutant.md](/fr/00-cours-theoriques/tout-en-un/04-automatisation-et-scripting/lecons/lecon-bash-debutant).
- Un **laboratoire jetable** : [[Glossary:VM]] Linux (Debian, Ubuntu ou Rocky Linux), compte non privilégié, **instantané préalable**. Toutes les commandes **lisent** des fichiers factices créés dans `~/labo-texte` ; les seules écritures sont dans ce dossier, et les suppressions sont **simulées** (`echo`).
- Aucune donnée réelle : adresses de documentation (192.0.2.0/24, 198.51.100.0/24, 203.0.113.0/24, 2001:db8::/32) et noms fictifs. Ne rejouez jamais ces essais sur des journaux de production sans copie préalable.
- Outils GNU : Debian, Ubuntu et Rocky Linux les fournissent ; sur [[Glossary:BSD]] ou macOS, certaines options diffèrent.

## L'essentiel en bref

- La philosophie Unix : **de petits outils, chacun excellent dans une tâche**, reliés par des **tubes**. Le texte est l'interface commune.
- `grep` **trouve** des lignes ; `cut` **découpe** des colonnes simples ; `sort` et `uniq -c` **classent et comptent** ; `sed` **transforme** ; `awk` **calcule** ; `find` **cherche des fichiers** ; `xargs` **applique** une commande à une liste.
- Le motif « top N » : `... | sort | uniq -c | sort -rn | head`.
- `uniq` ne supprime que les doublons **adjacents** : toujours trier avant.
- Fichiers à noms quelconques : `find ... -print0 | xargs -0`.
- Avant toute modification en masse : **lire d'abord, simuler ensuite (`echo`), modifier enfin**, avec une copie de secours (`sed -i.bak`).
- Fixez `LC_ALL=C` pour des tris prévisibles lors des tests.

---

## 1. De petits outils reliés par des tubes

Un journal web peut peser des gigaoctets : aucune lecture à l'œil n'est possible. L'administrateur pose une **question** (« Qui provoque des erreurs ? ») et assemble des outils qui y répondent.

**Analogie.** Une chaîne de tri postal : un poste écarte (`grep`), un autre découpe la zone de destination (`cut`), un autre classe (`sort`), un dernier compte par tas (`uniq -c`). Aucun poste n'est intelligent ; la chaîne, si.

![Schéma d'un pipeline POSIX : le clavier alimente le programme 1, dont la sortie standard alimente le programme 2 puis le programme 3, avec les flux d'erreur renvoyés à l'affichage](images/bash-texte-admin-1.svg)

*Figure 1 — Un pipeline d'outils : la sortie standard de chaque programme devient l'entrée du suivant. Schéma de TuukkaH, domaine public (Wikimedia Commons).*

## 2. Préparer les jeux de données factices

Créez le dossier de travail et trois fichiers : un journal web, un journal d'authentification [[Glossary:SSH]] et un inventaire CSV (séparateur point-virgule).

```bash
mkdir -p ~/labo-texte && cd ~/labo-texte
export LC_ALL=C

cat > access.log <<'EOF'
198.51.100.10 - - [01/Nov/2026:09:00:01 +0100] "GET /index.html HTTP/1.1" 200 5120
198.51.100.10 - - [01/Nov/2026:09:00:02 +0100] "GET /style.css HTTP/1.1" 200 1320
203.0.113.7 - - [01/Nov/2026:09:01:15 +0100] "GET /login HTTP/1.1" 200 2048
203.0.113.7 - - [01/Nov/2026:09:01:20 +0100] "POST /login HTTP/1.1" 401 512
203.0.113.7 - - [01/Nov/2026:09:01:23 +0100] "POST /login HTTP/1.1" 401 512
203.0.113.7 - - [01/Nov/2026:09:01:26 +0100] "POST /login HTTP/1.1" 401 512
192.0.2.44 - - [01/Nov/2026:09:02:00 +0100] "GET /api/inventaire HTTP/1.1" 200 15360
192.0.2.44 - - [01/Nov/2026:09:02:05 +0100] "GET /api/inventaire?site=lyon HTTP/1.1" 200 4096
198.51.100.23 - - [01/Nov/2026:09:03:10 +0100] "GET /admin HTTP/1.1" 403 256
198.51.100.23 - - [01/Nov/2026:09:03:12 +0100] "GET /admin/config HTTP/1.1" 403 256
198.51.100.10 - - [01/Nov/2026:09:04:00 +0100] "GET /missing.png HTTP/1.1" 404 128
192.0.2.44 - - [01/Nov/2026:09:05:30 +0100] "GET /api/inventaire HTTP/1.1" 500 64
203.0.113.7 - - [01/Nov/2026:09:06:00 +0100] "POST /login HTTP/1.1" 200 1024
198.51.100.10 - - [01/Nov/2026:09:07:11 +0100] "GET /index.html HTTP/1.1" 304 0
2001:db8::25 - - [01/Nov/2026:09:08:00 +0100] "GET /index.html HTTP/1.1" 200 5120
EOF

cat > auth.log <<'EOF'
Nov  1 08:55:01 srv-web01 sshd[1201]: Accepted publickey for admin from 192.0.2.44 port 51022 ssh2
Nov  1 08:57:13 srv-web01 sshd[1244]: Failed password for invalid user test from 203.0.113.7 port 40112 ssh2
Nov  1 08:57:16 srv-web01 sshd[1244]: Failed password for invalid user test from 203.0.113.7 port 40112 ssh2
Nov  1 08:57:20 srv-web01 sshd[1246]: Failed password for root from 203.0.113.7 port 40118 ssh2
Nov  1 08:58:02 srv-web01 sshd[1250]: Failed password for admin from 198.51.100.23 port 33210 ssh2
Nov  1 08:58:40 srv-web01 sshd[1252]: Accepted password for backup from 198.51.100.10 port 52044 ssh2
Nov  1 09:10:00 srv-web01 sudo:   admin : TTY=pts/0 ; PWD=/home/admin ; USER=root ; COMMAND=/usr/bin/systemctl restart nginx
Nov  1 09:12:31 srv-web01 sshd[1301]: Failed password for root from 203.0.113.7 port 40200 ssh2
Nov  1 09:15:09 srv-web01 sshd[1310]: Failed password for invalid user oracle from 198.51.100.23 port 33300 ssh2
EOF

cat > inventaire.csv <<'EOF'
hostname;ip;os;role;site;ram_go
srv-web01;192.0.2.11;debian12;web;lyon;8
srv-web02;192.0.2.12;debian12;web;lyon;8
srv-db01;192.0.2.21;debian12;base;paris;32
srv-db02;192.0.2.22;rocky9;base;paris;32
srv-app01;198.51.100.5;ubuntu2404;appli;paris;16
srv-app02;198.51.100.6;ubuntu2404;appli;lyon;16
srv-bkp01;198.51.100.50;debian12;sauvegarde;nantes;4
srv-mon01;203.0.113.9;rocky9;supervision;nantes;8
EOF

mkdir -p arbo/conf arbo/logs arbo/tmp
echo "port=8080" > arbo/conf/app.conf
echo "base=prod" > arbo/conf/db.conf
echo "ancien=oui" > "arbo/conf/vieux fichier.conf"
: > arbo/logs/app.log
seq 1 200 > arbo/logs/gros.log
echo x > arbo/tmp/x.tmp; echo y > arbo/tmp/y.tmp
touch -d '40 days ago' arbo/logs/app.log arbo/tmp/x.tmp
```

👉 Explication : chaque `cat > fichier <<'EOF'` écrit le texte qui suit (délimiteur entre apostrophes : aucun développement) ; `export LC_ALL=C` impose l'ordre de tri « octets » pour des résultats identiques partout ; la dernière partie crée une arborescence factice avec un nom contenant une **espace** (`vieux fichier.conf`), deux fichiers « vieux de 40 jours » (`touch -d`) et un fichier de 200 lignes.

Le journal web suit le schéma *adresse – – [date] "méthode chemin protocole" statut taille* ; l'inventaire a six colonnes. Gardez ces fichiers : ils servent à tout le reste.

## 3. `grep` : trouver les lignes qui comptent

`grep motif fichier` affiche les lignes qui contiennent le motif. Ses options les plus utiles :

| Option | Rôle |
|---|---|
| `-i` | ignore la casse |
| `-v` | **inverse** : lignes qui ne correspondent pas |
| `-c` | **compte** les lignes correspondantes |
| `-n` | affiche le numéro de ligne |
| `-E` | expressions régulières étendues (`\|`, `+`, `{n}`, `()`) |
| `-o` | n'affiche que la partie correspondante |
| `-w` | mot entier uniquement |
| `-r`, `-l` | récursif ; liste seulement les noms de fichiers |
| `-q` | silencieux : seul le code retour compte (idéal dans un `if`) |

```bash
grep -c ' 404 ' access.log
grep -cE '" [45][0-9]{2} ' access.log
grep -n 'POST' access.log | cut -c1-60
```

👉 Explication : la première commande compte les requêtes en erreur 404 (**1**) ; la deuxième compte tous les statuts 4xx et 5xx grâce à l'expression `[45][0-9]{2}` : un guillemet, un espace, un chiffre 4 ou 5 puis deux chiffres (**7**) ; la troisième numérote les requêtes POST (lignes 4, 5, 6 et 13) et `cut -c1-60` tronque l'affichage.

```bash
grep -v -E '" [23][0-9]{2} ' access.log | cut -d' ' -f1 | sort | uniq -c | sort -rn | head -n 2
```

👉 Explication : on écarte les réponses 2xx et 3xx (`-v`), on isole la première colonne (l'adresse), on trie, on compte les doublons, on classe par nombre décroissant et on garde les deux premières lignes. Résultat : `3 203.0.113.7` puis `2 198.51.100.23`.

Motifs : `.` = un caractère, `*` répète le précédent, `^` / `$` ancrent début / fin, `[abc]` = jeu de caractères. Mettez **toujours** le motif entre apostrophes pour que le shell n'y touche pas.

## 4. `cut`, `sort`, `uniq`, `wc`, `head`, `tr` : les petits outils

- **`cut -d';' -f1,5`** extrait des colonnes d'un fichier délimité (`-d` : séparateur, `-f` : numéros de champs) ; `cut -c1-60` extrait des positions de caractères. `cut` ne sait pas gérer « plusieurs espaces » comme un seul séparateur : pour cela, `awk`.
- **`sort`** trie ; `-n` numérique, `-r` inverse, `-u` supprime les doublons, `-t';'` choisit le séparateur, `-k5,5` trie sur la colonne 5 uniquement.
- **`uniq -c`** compte les lignes **consécutives** identiques : on le fait donc **toujours précéder de `sort`**.
- **`wc -l`** compte les lignes ; **`head -n 3`** / **`tail -n 3`** gardent les premières / dernières ; `tail -n +2` saute la première ligne (en-tête).
- **`tr`** remplace ou supprime des caractères (`tr -d '\r'` retire les fins de ligne Windows).

```bash
tail -n +2 inventaire.csv | sort -t';' -k5,5 -k1,1 | cut -d';' -f1,5
tail -n +2 inventaire.csv | sort -t';' -k6,6nr -k1,1 | head -n 3 | cut -d';' -f1,6
```

👉 Explication : la première commande retire l'en-tête, trie par site puis par nom de machine et n'affiche que ces deux colonnes (lyon : `srv-app02`, `srv-web01`, `srv-web02` ; puis nantes ; puis paris) ; la seconde classe par mémoire décroissante (`6,6nr`) et garde les trois plus gros serveurs : `srv-db01;32`, `srv-db02;32`, `srv-app01;16`.

![Pipeline top N : grep isole les lignes, cut extrait la colonne, sort rapproche, uniq -c compte, sort -rn classe, head garde le début](images/bash-texte-admin-2.svg)

*Figure 2 — Le motif « top N » : filtrer, extraire, trier, compter, reclasser, tronquer. Création originale du projet Pack Master (CC0).*

## 5. `sed` : transformer le flux

`sed` (*stream editor*) lit un flux ligne par ligne et applique des commandes. La plus célèbre est la **substitution** `s/motif/remplacement/`.

```bash
sed -n '2,4p' inventaire.csv
sed 's/debian12/debian13/' inventaire.csv | sed -n '2,3p'
sed -E 's/([0-9]+\.[0-9]+\.[0-9]+)\.[0-9]+/\1.x/' inventaire.csv | sed -n '2,3p'
```

👉 Explication : `-n '2,4p'` n'affiche (`p`) que les lignes 2 à 4 ; la deuxième commande remplace la **première** occurrence de `debian12` sur chaque ligne (ajoutez `g` en fin d'expression pour **toutes** les occurrences) ; la troisième utilise un groupe capturant `( )` rappelé par `\1` pour masquer le dernier octet d'une adresse (`192.0.2.11` devient `192.0.2.x`), pratique pour anonymiser avant de partager un extrait.

`sed` sert aussi à **extraire** :

```bash
grep 'Failed password' auth.log | sed -E 's/.* from ([^ ]+) port.*/\1/' | sort | uniq -c | sort -rn
```

👉 Explication : `.* from ([^ ]+) port.*` capture le mot situé entre `from` et `port` (l'adresse source) et le remplace pour toute la ligne ; la suite compte les échecs par adresse : `4 203.0.113.7` et `2 198.51.100.23`. Le séparateur `/` peut être remplacé (`s#/usr#/opt#`) quand le motif contient des barres.

**Modifier un fichier en place** est le geste le plus dangereux :

```bash
cp inventaire.csv inv-test.csv
sed -i.bak 's/rocky9/rocky10/' inv-test.csv
diff inv-test.csv.bak inv-test.csv
```

👉 Explication : `-i.bak` modifie le fichier **et conserve l'original** sous le nom `inv-test.csv.bak` ; `diff` montre exactement ce qui a changé (ici deux lignes). Habitude à prendre : travailler sur une **copie**, relire avec `diff`, et seulement ensuite appliquer sur le vrai fichier (après sauvegarde). Sans suffixe, `sed -i` ne laisse aucune trace.

## 6. `awk` : filtrer, compter, calculer

`awk` lit les lignes, les découpe en **champs** (`$1`, `$2`…, `$0` = toute la ligne, `NF` = nombre de champs, `NR` = numéro de ligne) et exécute des actions `condition { action }`. Le séparateur par défaut est « un ou plusieurs espaces » ; `-F';'` le change.

```bash
awk '$9 >= 500 {print $1, $7, $9}' access.log
awk -F';' 'NR > 1 && $6 >= 16 {print $1, $6}' inventaire.csv
```

👉 Explication : la première commande affiche adresse, chemin et statut des requêtes en statut 500 ou plus (`192.0.2.44 /api/inventaire 500`) ; la seconde, sur le CSV, ignore l'en-tête (`NR > 1`) et liste les machines d'au moins 16 Go : `srv-db01`, `srv-db02`, `srv-app01`, `srv-app02`.

La vraie force d'`awk` est le **tableau associatif** (indexé par du texte), qui remplace `sort | uniq -c` et sait aussi additionner :

```bash
awk '{n[$9]++} END {for (c in n) print c, n[c]}' access.log | sort
awk '{o[$1] += $10} END {for (i in o) printf "%-16s %6d\n", i, o[i]}' access.log | sort -k2 -rn
awk -F';' 'NR > 1 {n[$3]++; r[$3] += $6} END {for (o in n) print o, n[o], r[o]}' inventaire.csv | sort
```

👉 Explication : (1) compte les requêtes par statut (`200 7`, `304 1`, `401 3`, `403 2`, `404 1`, `500 1`) ; (2) additionne les octets transmis par adresse et les classe (`192.0.2.44` en tête avec 19 520 octets) ; `printf` aligne les colonnes ; (3) calcule, par système d'exploitation, le nombre de machines et la mémoire totale (`debian12 4 52`, `rocky9 2 40`, `ubuntu2404 2 32`). Le bloc `END` s'exécute **après** la dernière ligne ; l'ordre de parcours d'un `for (k in tableau)` n'étant pas garanti, on passe par `sort`.

Structure : `BEGIN { avant }`, `condition { pour chaque ligne }`, `END { après }`. Au-delà d'une dizaine de lignes, écrivez le programme `awk` dans un fichier.

## 7. `find` : chercher des fichiers

`find dossier critères actions` parcourt une arborescence. Les critères se combinent (« et » implicite) :

| Critère | Signification |
|---|---|
| `-type f` / `-type d` | fichiers / dossiers |
| `-name '*.conf'` | nom (motif entre apostrophes ; `-iname` ignore la casse) |
| `-mtime +30` | modifié il y a **plus** de 30 jours (`-30` : moins de 30 ; `-mmin` pour les minutes) |
| `-size +100c` | plus de 100 octets (`k`, `M`, `G` pour les unités plus grandes) |
| `-user`, `-perm` | propriétaire ; droits |
| `-maxdepth 1` | ne descend pas dans les sous-dossiers |

```bash
find arbo -type f -name '*.conf' | sort
find arbo -type f -mtime +30 | sort
find arbo -type f -size +100c
```

👉 Explication : liste les trois fichiers de configuration (dont celui à l'espace dans son nom) ; liste les fichiers modifiés il y a plus de 30 jours (`arbo/logs/app.log` et `arbo/tmp/x.tmp`) ; liste les fichiers de plus de 100 octets (`arbo/logs/gros.log`).

Côté **actions**, `-print` (par défaut) affiche, `-exec commande {} \;` lance la commande **une fois par fichier** et `-exec commande {} +` la lance **une fois pour un lot** de fichiers :

```bash
find arbo -type f -name '*.log' -exec wc -l {} +
```

👉 Explication : exécute `wc -l` sur tous les `.log` trouvés (`200` lignes pour `gros.log`, `0` pour `app.log`, puis le total ; l'ordre d'affichage dépend du système de fichiers). `{}` est remplacé par les noms trouvés, et `+` regroupe les fichiers pour limiter le nombre de processus.

Pour toute action destructrice (`-delete`, `rm`) : **d'abord** la même recherche avec `-print`, relecture, puis seulement l'action ; `-delete` se place en dernier.

## 8. `xargs` : transformer une liste en arguments

`xargs` lit des noms sur l'entrée standard et construit une ligne de commande avec. Il est précieux quand la commande finale n'accepte pas de tube. Le danger : par défaut, il **découpe sur les espaces**.

```bash
find arbo -type f -name '*.conf' | xargs ls -l
find arbo -type f -name '*.conf' -print0 | xargs -0 grep -l 'base'
```

👉 Explication : la première commande échoue partiellement : `vieux fichier.conf` est coupé en deux mots, et `ls` signale `arbo/conf/vieux` et `fichier.conf` introuvables ; la seconde utilise `-print0` (séparateur « octet nul ») avec `xargs -0`, qui gère n'importe quel nom ; elle affiche `arbo/conf/db.conf`, seul fichier contenant `base`. **Le couple `-print0 | xargs -0` est la forme sûre.**

Autres options : `-n 1` (un argument par appel), `-I{}` (placer l'argument où l'on veut), `-r` (ne rien lancer si l'entrée est vide) :

```bash
find arbo -type f -mtime +30 -print0 | xargs -0 -r echo rm --
printf 'a\nb\n' | xargs -I{} echo "traite {}"
```

👉 Explication : la première commande **simule** une suppression : `echo` affiche `rm -- arbo/logs/app.log arbo/tmp/x.tmp` sans rien supprimer ; vérifiée, on retirerait `echo`. La seconde affiche `traite a` puis `traite b`. Retenez la méthode : **`echo` d'abord, vraie commande ensuite**.

## 9. Assembler : trois recettes d'administrateur

![Aide au choix d'outil : trouver une ligne, extraire une colonne, transformer, calculer, chercher des fichiers](images/bash-texte-admin-3.svg)

*Figure 3 — Quel outil pour quelle question ? Création originale du projet Pack Master (CC0).*

**Recette 1 — Qui force la connexion SSH ?** Voir §5 : `203.0.113.7` totalise 4 échecs, candidate à un blocage par le pare-feu après validation.

**Recette 2 — Quelles adresses sont à la fois fautives côté web et côté SSH ?**

```bash
comm -12 <(cut -d' ' -f1 access.log | sort -u) \
         <(grep 'Failed password' auth.log | sed -E 's/.* from ([^ ]+) port.*/\1/' | sort -u)
```

👉 Explication : `comm -12` n'affiche que les lignes **communes** à deux listes triées ; `<( ... )` (substitution de processus) fournit chaque liste comme un fichier. Résultat : `198.51.100.23` et `203.0.113.7`.

**Recette 3 — Requêtes par minute.**

```bash
awk '{print substr($4, 14, 5)}' access.log | sort | uniq -c | head -n 3
```

👉 Explication : `substr($4, 14, 5)` extrait l'heure et la minute du champ date (`09:01`) ; on compte les requêtes par minute : `2 09:00`, `4 09:01`, `2 09:02`. Un pic soudain révèle un balayage ou une panne.

---

## Mise en pratique guidée

**Contexte.** VM jetable, instantané pris, tout dans `~/labo-texte` (fichiers du §2). Répondez **en une ligne de commande chacune**, puis comparez.

1. Combien de requêtes ont reçu une réponse 5xx ? *(1)*
2. Quelle est l'adresse qui a le plus d'échecs d'authentification (statut 401) sur le web ? *(203.0.113.7)*
3. Combien de machines de l'inventaire par site ? *(lyon 3, nantes 2, paris 3)*
4. Quelle est la mémoire totale de l'inventaire, en Go ? *(124)*
5. Quels fichiers `.conf` de `arbo` contiennent `prod` ? *(arbo/conf/db.conf)*

```bash
grep -c '" 5[0-9][0-9] ' access.log
awk '$9 == 401 {n[$1]++} END {for (i in n) print n[i], i}' access.log | sort -rn | head -n 1
awk -F';' 'NR > 1 {print $5}' inventaire.csv | sort | uniq -c
awk -F';' 'NR > 1 {t += $6} END {print t}' inventaire.csv
find arbo -type f -name '*.conf' -print0 | xargs -0 grep -l 'prod'
```

👉 Explication : une solution possible par question, dans l'ordre.

**Nettoyage et retour arrière.**

```bash
cd ~ && rm -r ~/labo-texte
```

👉 Explication : supprime uniquement le dossier de l'exercice (vérifiez le chemin) ; en cas de doute, restaurez l'instantané.

## Exercices

1. **grep.** Affichez les lignes de `auth.log` mentionnant `invalid user`, avec leur numéro de ligne, puis comptez-les.
2. **cut/sort/uniq.** Donnez la liste des rôles distincts de l'inventaire avec le nombre de machines de chacun.
3. **sed.** Produisez une version de `inventaire.csv` où le séparateur `;` devient `,`, sans modifier le fichier original.
4. **awk.** Affichez le nombre total d'octets transmis pour les seules requêtes `GET` de `access.log`.
5. **Top N.** Quels sont les deux utilisateurs visés par le plus d'échecs d'authentification dans `auth.log` ? *(piège : la formule « invalid user »)*
6. **find.** Listez les fichiers de `arbo` modifiés depuis moins de 30 jours.
7. **xargs.** Comptez les lignes de chaque fichier `.conf` de `arbo` en gérant l'espace du nom.

## Corrigés des exercices

**1.** `grep -n 'invalid user' auth.log` affiche les lignes 2, 3 et 9 ; `grep -c 'invalid user' auth.log` donne `3`.

**2.** `cut -d';' -f4 inventaire.csv | tail -n +2 | sort | uniq -c` : les rôles et leurs effectifs (appli 2, base 2, sauvegarde 1, supervision 1, web 2). On retire l'en-tête **avant** de trier.

**3.** `sed 's/;/,/g' inventaire.csv > inventaire-virgules.csv` (ou `tr ';' ',' < inventaire.csv`). Sans `g`, seule la première occurrence de chaque ligne serait remplacée ; la redirection protège l'original.

**4.** `awk '/GET/ {t += $10} END {print t}' access.log` : somme des tailles des lignes contenant `GET`, soit 33 768 octets.

**5.**

```bash
grep 'Failed password' auth.log | awk '{for (i = 1; i <= NF; i++) if ($i == "for") {u = $(i+1); if (u == "invalid") u = $(i+3); print u}}' | sort | uniq -c | sort -rn
```

👉 Explication : après le mot `for`, l'utilisateur est le champ suivant, sauf pour `invalid user NOM` où il se trouve trois champs plus loin ; le résultat est `2 test` et `2 root`, `1 oracle`, `1 admin` : les deux premiers sont à égalité, l'ordre des ex æquo n'étant pas garanti.

**6.** `find arbo -type f -mtime -30` : `-30` signifie « moins de 30 jours » (`app.log` et `x.tmp` en sont exclus).

**7.** `find arbo -type f -name '*.conf' -print0 | xargs -0 wc -l` (ou `-exec wc -l {} +`). Sans `-print0`/`-0`, le nom à espace serait coupé.

## Quiz

**1. Pourquoi faire précéder `uniq -c` de `sort` ?**
a) `uniq` ne rapproche que les lignes identiques consécutives b) `sort` accélère `uniq` c) `uniq` ne lit que des nombres
**Réponse : a.**

**2. Que fait `grep -v` ?**
a) affiche la version b) n'affiche que les lignes qui **ne** correspondent **pas** c) affiche le détail
**Réponse : b.**

**3. Quelle commande extrait la 5e colonne d'un CSV séparé par `;` ?**
a) `cut -d';' -f5` b) `cut -c5` c) `sort -k5`
**Réponse : a.** `-c` travaille sur des positions de caractères, `sort` ne fait que trier.

**4. Que remplace `sed 's/a/b/'` ?**
a) toutes les occurrences de `a` du fichier b) la première occurrence de `a` de chaque ligne c) rien sans `-i`
**Réponse : b.** Il faut `g` pour toutes les occurrences d'une ligne ; sans `-i`, le résultat est affiché, le fichier n'est pas modifié.

**5. Quelle option de `sed` conserve une copie de sécurité ?**
a) `-n` b) `-e` c) `-i.bak`
**Réponse : c.**

**6. Dans `awk`, que désigne `$NF` ?**
a) le dernier champ de la ligne b) le nombre de lignes c) la ligne entière
**Réponse : a.** `NF` est le nombre de champs, donc `$NF` le dernier ; `$0` est la ligne entière.

**7. Pourquoi `find ... -print0 | xargs -0` ?**
a) c'est plus rapide b) pour gérer les noms de fichiers contenant espaces ou retours à la ligne c) pour trier la sortie
**Réponse : b.**

**8. Que fait `find . -mtime +30` ?**
a) fichiers modifiés il y a moins de 30 jours b) fichiers de plus de 30 Mo c) fichiers modifiés il y a plus de 30 jours
**Réponse : c.**

**9. Quelle est la bonne méthode pour tester une suppression en masse ?**
a) la lancer sur un petit dossier puis sur le reste b) remplacer `rm` par `echo rm` et relire la liste c) ajouter `-f`
**Réponse : b.** La simulation n'a aucun effet de bord ; `-f` supprime encore plus agressivement.

**10. Quel outil choisir pour additionner une colonne de nombres ?**
a) `awk` b) `cut` c) `grep`
**Réponse : a.** `cut` découpe et `grep` filtre ; seul `awk` calcule.

## Erreurs fréquentes et dépannage

| Symptôme | Cause probable | Remède |
|---|---|---|
| Comptes absurdes avec `uniq -c` | entrée non triée | `sort \| uniq -c` |
| `grep` ne trouve pas `a\|b` | expression étendue non activée | `grep -E 'a\|b'` |
| Le shell « mange » le motif | motif non protégé | apostrophes autour du motif |
| `sed -i` a détruit un fichier | pas de copie, mauvais motif | `-i.bak`, essai sur copie, `diff` |
| Colonnes décalées dans `awk` | séparateur par défaut sur un CSV | `-F';'` |
| Tri « bizarre » (10 avant 2) | tri alphabétique | `sort -n`, `-k6,6n` |
| `xargs` coupe les noms avec espaces | séparation par défaut | `-print0 \| xargs -0` |
| `find` sans résultat | motif non protégé (`*.conf` développé par le shell) | `-name '*.conf'` |

## À retenir

- Un petit outil par tâche, reliés par des tubes ; le texte est l'interface.
- `grep` filtre, `cut` découpe, `sort | uniq -c | sort -rn` classe et compte, `sed` transforme, `awk` calcule, `find` cherche, `xargs` applique.
- `sort` avant `uniq` ; protégez les motifs par des apostrophes.
- `sed -i.bak` et `diff` : jamais de modification en place sans filet.
- `-print0 | xargs -0` pour tous les noms de fichiers ; simulez avec `echo` avant d'agir.

## Pour aller plus loin

- Manuel de GNU grep : <https://www.gnu.org/software/grep/manual/grep.html>
- Manuel de GNU sed : <https://www.gnu.org/software/sed/manual/sed.html>
- Manuel de GNU awk (gawk) : <https://www.gnu.org/software/gawk/manual/gawk.html>
- GNU findutils (`find`, `xargs`) : <https://www.gnu.org/software/findutils/manual/html_mono/find.html>
- GNU coreutils (`cut`, `sort`, `uniq`, `wc`, `tr`) : <https://www.gnu.org/software/coreutils/manual/coreutils.html>
- Adresses réservées à la documentation (RFC 5737) : <https://www.rfc-editor.org/rfc/rfc5737>

## Crédits des images

| Fichier | Source (URL Commons) | Auteur | Licence (nom + URL) | Modifications |
|---|---|---|---|---|
| `images/bash-texte-admin-1.svg` | <https://commons.wikimedia.org/wiki/File:Pipeline-notitle.svg> | TuukkaH | Domaine public (Public domain, selon la fiche Commons) — <https://commons.wikimedia.org/wiki/File:Pipeline-notitle.svg> | Aucune (fichier tel que téléchargé) |
| `images/bash-texte-admin-2.svg` | Création originale du projet Pack Master | Projet Pack Master | CC0 1.0 — <https://creativecommons.org/publicdomain/zero/1.0/deed.fr> | Aucune |
| `images/bash-texte-admin-3.svg` | Création originale du projet Pack Master | Projet Pack Master | CC0 1.0 — <https://creativecommons.org/publicdomain/zero/1.0/deed.fr> | Aucune |

Création originale du projet Pack Master, dédiée au domaine public (CC0). Licence de `bash-texte-admin-1.svg` vérifiée par l'[[Glossary:API]] de Wikimedia Commons le 2026-11-01 (« Public domain », attribution non requise mais indiquée).

## Historique de vérification

| Date | OS/logiciel | Testeur | Verdict |
|---|---|---|---|
| 2026-11-01 | GNU Bash 5.3, GNU grep/sed/gawk/findutils/coreutils (Linux, poste de rédaction) | Rédaction assistée (agent Copilot) : jeu de données et commandes des §3 à §9 exécutés dans un dossier jetable, lecture seule hors dossier de test, sans privilège ; sorties annoncées relevées à l'exécution | Non testé sur plateforme cible (commandes exécutées avec succès en local uniquement) |
| 2026-11-01 | Debian 12 / Ubuntu 24-04 / Rocky Linux 9 (VM de laboratoire) | Rédaction assistée (agent Copilot) | Non testé sur plateforme cible |