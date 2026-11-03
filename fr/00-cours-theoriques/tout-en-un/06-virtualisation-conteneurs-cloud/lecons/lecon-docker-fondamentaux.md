---
title: "Leçon — Docker : images, conteneurs, couches, volumes, réseaux, Dockerfile et registres"
description: "À l'issue de cette leçon, vous saurez :"
published: true
date: 2026-11-03T14:22:28Z
tags: ["transverse", "tout-en-un", "lecon", "virtualisation", "conteneurs", "docker", "dockerfile", "registre"]
editor: markdown
dateCreated: 2026-11-03T14:22:28Z
dateModified: 2026-11-03T14:22:28Z
---

# Leçon — Docker : images, conteneurs, couches, volumes, réseaux, Dockerfile et registres

- **Tags** : `transverse`, `tout-en-un`, `lecon`, `virtualisation`, `conteneurs`, `docker`, `dockerfile`, `registre`
- **Niveau** : débutant à intermédiaire (administrateur système ou technicien [[Glossary:TSSR]])
- **Durée estimée** : 3 h 30 (cours 1 h 30, labo guidé 1 h 30, exercices et quiz 30 min)

> **Avertissement de test** : au moment de la rédaction, Docker n'était pas installé sur la machine de rédaction et aucune installation n'a été tentée. **Toutes les commandes de cette leçon sont donc présentées comme non testées sur la plateforme cible.** Exécutez-les d'abord dans une [[Glossary:VM]] jetable, jamais en premier en production.

---

## Objectifs pédagogiques

À l'issue de cette leçon, vous saurez :

1. Distinguer machine virtuelle et conteneur, et dire ce que les conteneurs partagent.
2. Distinguer une **image** (modèle en lecture seule) d'un **conteneur** (instance).
3. Expliquer les **couches** et en déduire l'ordre optimal d'un Dockerfile.
4. Écrire, construire, étiqueter et lancer une image à partir d'un **Dockerfile**.
5. Rendre des données persistantes (**volume**, bind mount) et connecter des conteneurs par un **réseau**.
6. Utiliser un **registre** : connexion, étiquetage, envoi, récupération, épinglage par digest.
7. Diagnostiquer avec `logs`, `inspect`, `exec` et `ps`.

## Prérequis et durée

- Ligne de commande Linux (fichiers, droits, processus) et réseau de base ([[Glossary:IP]], port, [[Glossary:DNS]]).
- Une **VM Linux jetable** (Debian ou Ubuntu) avec accès console de secours, environ 2 Go libres.
- Durée : 3 h 30. Aucune connaissance préalable de Docker.

## L'essentiel en bref

- Un **conteneur** est un processus (ou un groupe de processus) isolé par le noyau Linux (espaces de noms, groupes de contrôle). Il **partage le noyau de l'hôte** ; il n'embarque pas de système d'exploitation complet.
- Une **image** est un empilement de couches en lecture seule, plus des métadonnées (commande de démarrage, port exposé…). Un conteneur est une image + une fine couche inscriptible.
- Tout ce qui est écrit dans un conteneur **disparaît avec lui** sauf s'il est placé dans un **volume**.
- Un **Dockerfile** est la recette de fabrication d'une image : chaque instruction crée une couche, et l'ordre influence le cache.
- Un **registre** stocke et distribue les images ; on y accède par un nom de la forme `hôte/dépôt:étiquette` ou `hôte/dépôt@sha256:…`.
- Publier un port (`-p`) expose un service à l'extérieur : c'est un choix de sécurité, pas un réflexe.

---

## 1. Pourquoi des conteneurs ? L'idée en une analogie

Imaginez un restaurant. Une **machine virtuelle**, c'est un restaurant complet loué à chaque client : cuisine, électricité, plomberie, personnel. C'est très isolé, mais cher et long à ouvrir. Un **conteneur**, c'est un *stand* dans une halle gourmande : chacun a son comptoir et ses ingrédients, mais tous partagent le bâtiment, l'électricité et l'eau (le **noyau**). On en ouvre dix en quelques secondes.

![Comparaison de deux piles : trois machines virtuelles avec chacune un système invité sur un hyperviseur, et trois conteneurs partageant le noyau de l'hôte via un moteur de conteneurs](images/docker-fondamentaux-1.svg)
*Figure 1 — Machines virtuelles et conteneurs : ce qui est dupliqué et ce qui est partagé.*

À retenir : légèreté (quelques dizaines de Mo contre plusieurs Go), démarrage en secondes, reproductibilité (l'application embarque ses bibliothèques), mais **isolation plus faible qu'une VM** : une faille du noyau touche tous les conteneurs de l'hôte. On ne lance pas non plus un conteneur Windows sur un noyau Linux.

Le moteur le plus répandu est **Docker Engine** (démon `dockerd`, client `docker`). D'autres outils comprennent les mêmes images, car elles suivent la spécification **OCI** (Open Container Initiative) : Podman, containerd, CRI-O.

## 2. Images et conteneurs : le moule et le gâteau

Une **image** est un moule : immuable, partageable, versionnée. Un **conteneur** est le gâteau sorti du moule : on peut en faire dix à partir du même moule, chacun évolue indépendamment.

Vérifier la présence du client et du moteur :

```bash
docker version
```

👉 Explication : affiche la version du client et du serveur (démon) ; si la partie « Server » est absente ou en erreur, le démon n'est pas démarré ou votre utilisateur n'a pas le droit d'y accéder. Commande non testée ici.

Lancer un premier conteneur jetable :

```bash
docker run --rm hello-world
```

👉 Explication : télécharge si besoin l'image `hello-world`, démarre un conteneur qui affiche un message puis s'arrête ; `--rm` supprime le conteneur à la fin pour ne pas laisser de déchet. Nécessite un accès au registre public.

Lister les images et les conteneurs :

```bash
docker image ls
docker ps -a
```

👉 Explication : `image ls` montre les images présentes localement (nom, étiquette, identifiant, taille) ; `ps -a` liste tous les conteneurs, y compris arrêtés (sans `-a`, seuls ceux qui tournent apparaissent).

Cycle de vie d'un conteneur : `create` → `start` → `stop` → `rm`. La commande `run` enchaîne création et démarrage. Un conteneur arrêté existe toujours (avec ses écritures) jusqu'à sa suppression par `docker rm`.

Options de `run` courantes : `-d` (arrière-plan), `--name` (nom lisible), `--rm` (supprime à l'arrêt), `-p 8080:80` (publie le port 80 du conteneur sur le 8080 de l'hôte), `-e CLE=valeur` (variable d'environnement), `-v nom:/chemin` (volume), `--network` (réseau), `-it` (terminal interactif).

Exemple complet, un serveur web de test :

```bash
docker run -d --name web1 -p 8080:80 nginx:1.27
curl -sI http://127.0.0.1:8080
```

👉 Explication : démarre nginx en arrière-plan et publie son port 80 sur le port 8080 de l'hôte ; `curl -sI` récupère les en-têtes [[Glossary:HTTP]] pour prouver que le service répond. Le port est accessible depuis le réseau de l'hôte : en laboratoire, c'est acceptable, ailleurs vérifiez le pare-feu.

## 3. Les couches : comprendre le cache et la taille

Une image n'est pas un bloc monolithique : c'est un **empilement de couches**. Chaque couche enregistre les différences (fichiers ajoutés, modifiés, supprimés) par rapport à la précédente. Quand vous lancez un conteneur, Docker ajoute une **couche inscriptible** tout en haut, propre à ce conteneur.

![Couches d'une image : base, paquets, dépendances, code en lecture seule, puis une couche inscriptible par conteneur](images/docker-fondamentaux-2.svg)
*Figure 2 — Chaque instruction du Dockerfile crée une couche ; chaque conteneur ajoute sa propre couche d'écriture.*

Trois propriétés : (1) les couches sont **partagées** entre conteneurs issus de la même image ; (2) le **cache de build** réutilise une couche tant que l'instruction et ses entrées sont inchangées, mais dès qu'une couche change, **toutes les suivantes sont reconstruites** ; (3) supprimer un fichier dans une couche ultérieure ne réduit **pas** la taille : il faut le supprimer dans la *même* instruction `RUN` qui l'a créé, ou ne jamais l'ajouter.

Voir les couches d'une image :

```bash
docker history nginx:1.27
```

👉 Explication : affiche, de la plus récente à la plus ancienne, les couches avec l'instruction qui les a créées et leur taille ; utile pour repérer une couche anormalement lourde.

Règle d'or de l'ordre : **mettez en haut du Dockerfile ce qui change rarement** (système, dépendances) et **en bas ce qui change souvent** (votre code). Ainsi, une modification du code ne force pas à réinstaller toutes les dépendances.

## 4. Le Dockerfile : la recette de l'image

Un Dockerfile est un fichier texte nommé `Dockerfile`, lu ligne par ligne. Voici un exemple pour une petite application Python (les noms et adresses sont fictifs) :

```dockerfile
# Image de base minimale, version précise
FROM python:3.12-slim

# Métadonnées lisibles
LABEL org.opencontainers.image.title="demo-api"

# Répertoire de travail dans l'image
WORKDIR /app

# Dépendances d'abord (rarement modifiées) pour profiter du cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Puis le code (souvent modifié)
COPY app/ .

# Utilisateur non privilégié
RUN useradd --system --uid 10001 appuser
USER 10001

# Documente le port d'écoute (ne publie rien à lui seul)
EXPOSE 8000

# Commande de démarrage au format « exec »
CMD ["python", "main.py"]
```

👉 Explication : chaque instruction est une étape de fabrication ; `FROM` choisit la base, `WORKDIR` fixe le dossier courant, `COPY` copie des fichiers du contexte de build, `RUN` exécute une commande pendant la construction, `USER` choisit l'utilisateur d'exécution, `EXPOSE` documente un port et `CMD` donne la commande lancée au démarrage du conteneur.

Pièges fréquents : `FROM …:latest` (non reproductible), copier tout le dossier (secrets compris), placer un secret dans `ENV` ou `ARG` (il reste dans l'image), oublier `USER` (tout tourne en root), croire qu'`EXPOSE` ouvre un port, préférer `ADD` à `COPY` (moins prévisible).

**ENTRYPOINT et CMD** : `ENTRYPOINT` définit le programme fixe, `CMD` ses arguments par défaut, que l'utilisateur peut remplacer à la fin de `docker run`. Préférez toujours la forme tableau [[Glossary:JSON]] (`["prog","arg"]`) qui lance directement le processus, sans shell intermédiaire : le processus reçoit alors correctement les signaux d'arrêt.

**Le contexte de build et `.dockerignore`** : la commande de build envoie au démon tout le dossier indiqué (le « contexte »). Pour éviter d'y inclure l'historique Git, des clés ou des dépendances locales, créez un fichier `.dockerignore` :

```text
.git
.env
*.pem
__pycache__/
node_modules/
```

👉 Explication : liste les motifs de fichiers exclus du contexte de build ; cela accélère la construction et évite de copier accidentellement des secrets dans une couche.

**Build multi-étapes** : pour obtenir une image finale légère, on compile dans une première étape puis on ne recopie que le résultat dans une image minimale :

```dockerfile
FROM golang:1.23 AS build
WORKDIR /src
COPY . .
RUN CGO_ENABLED=0 go build -o /out/serveur .

FROM gcr.io/distroless/static-debian12
COPY --from=build /out/serveur /serveur
USER 65532
ENTRYPOINT ["/serveur"]
```

👉 Explication : la première étape contient les outils de compilation lourds ; la seconde ne garde que le binaire dans une image sans shell ni gestionnaire de paquets, ce qui réduit la taille et la surface d'attaque.

## 5. Construire, étiqueter, lancer

Dans le dossier contenant le Dockerfile :

```bash
docker build -t demo-api:1.0 .
```

👉 Explication : construit une image à partir du Dockerfile du dossier courant (le point final est le contexte) et l'étiquette `demo-api:1.0` ; relancée sans changement, la commande réutilise le cache et se termine presque instantanément.

Ajouter une seconde étiquette sur la même image :

```bash
docker tag demo-api:1.0 demo-api:stable
```

👉 Explication : crée un alias, sans copier les données ; les deux étiquettes pointent vers la même image (même identifiant).

Lancer, lire les journaux, entrer dans le conteneur, l'arrêter :

```bash
docker run -d --name api1 -p 8000:8000 demo-api:1.0
docker logs --tail 20 api1
docker exec -it api1 sh
docker stop api1
```

👉 Explication : `logs` affiche les 20 dernières lignes de sortie standard du processus principal ; `exec -it … sh` ouvre un shell dans le conteneur en marche (si l'image en contient un) pour inspecter ; `stop` envoie un signal d'arrêt propre puis force au bout de dix secondes.

Un conteneur est **éphémère par conception** : on le recrée depuis l'image plutôt que de le réparer à la main avec `exec`.

## 6. Volumes : garder les données

Par défaut, tout fichier écrit dans un conteneur vit dans sa couche inscriptible et disparaît avec `docker rm`. Pour conserver des données (base, fichiers téléversés), on utilise :

- un **volume nommé** : espace géré par Docker, indépendant du conteneur. Recommandé pour les données applicatives ;
- un **bind mount** : un dossier précis de l'hôte monté dans le conteneur. Pratique en développement, mais dépend de la structure de l'hôte et de ses droits ;
- un **tmpfs** : stockage en mémoire vive, volatil, adapté à des fichiers temporaires ou sensibles.

```bash
umask 077
openssl rand -base64 18 > pg_pwd.txt
docker volume create dbdata
docker run -d --name db1 -v dbdata:/var/lib/postgresql/data -v "$PWD/pg_pwd.txt":/run/secrets/pg_pwd:ro -e POSTGRES_PASSWORD_FILE=/run/secrets/pg_pwd postgres:16
docker volume ls
```

👉 Explication : génère un mot de passe aléatoire dans un fichier lisible par vous seul (jamais dans la ligne de commande ni dans l'image), crée un volume nommé, puis lance PostgreSQL en lui donnant ce fichier en lecture seule ; `volume ls` confirme l'existence du volume. Ce fichier est un secret de laboratoire : ne le versionnez pas.

Vérifier la persistance (principe) :

```bash
docker rm -f db1
docker run -d --name db2 -v dbdata:/var/lib/postgresql/data postgres:16
docker volume inspect dbdata
```

👉 Explication : supprime le premier conteneur puis en crée un nouveau sur le même volume ; les données sont retrouvées. `volume inspect` montre le point de montage sur l'hôte et le pilote utilisé.

Un bind mount se monte avec `-v "$PWD/site":/usr/share/nginx/html:ro` ; le suffixe `:ro` interdit au conteneur d'écrire dans le dossier, ce qui limite les dégâts en cas de compromission.

**Attention** : un volume n'est **pas une sauvegarde**. Supprimer un volume détruit ses données ; sauvegardez-le séparément (copie de son contenu vers un autre support, ou sauvegarde applicative de la base).

## 7. Réseaux : faire parler les conteneurs

Docker crée des réseaux virtuels. Les trois pilotes à connaître :

- **bridge** (par défaut) : réseau privé interne à l'hôte, avec traduction d'adresses vers l'extérieur ;
- **host** : le conteneur utilise directement la pile réseau de l'hôte (pas d'isolation réseau) ;
- **none** : aucune interface hors boucle locale.

![Hôte Docker avec un réseau bridge nommé appnet reliant un conteneur web et un conteneur db, un port publié 8080 vers 80 et un volume pour la base](images/docker-fondamentaux-3.svg)
*Figure 3 — Un réseau défini par l'utilisateur, un seul port publié, un volume pour les données.*

Le réseau `bridge` par défaut est limité : pas de résolution de noms entre conteneurs. Un **réseau défini par l'utilisateur** offre un DNS interne : les conteneurs se joignent par leur *nom*.

```bash
docker network create appnet
docker run -d --name db --network appnet -v dbdata:/var/lib/postgresql/data postgres:16
docker run -d --name web --network appnet -p 8080:80 nginx:1.27
docker exec web getent hosts db
```

👉 Explication : crée un réseau `appnet`, y connecte une base et un serveur web, puis vérifie depuis le conteneur `web` que le nom `db` est résolu en adresse interne. Seul le port 8080 est publié sur l'hôte : la base n'est pas joignable de l'extérieur.

Bonnes pratiques : ne publiez que les ports nécessaires (jamais une base de données sans raison), liez à la boucle locale quand c'est possible (`-p 127.0.0.1:8080:80`), et sachez que Docker modifie lui-même les règles du pare-feu de l'hôte pour les ports publiés : testez depuis une autre machine.

## 8. Registres : stocker et distribuer les images

Un **registre** est un serveur d'images. Le registre public par défaut est Docker Hub ; d'autres existent (registres d'éditeurs, registre d'un fournisseur cloud, registre interne). Le nom complet d'une image est :

```text
registry.example.com:5000/equipe/demo-api:1.0
└───── hôte ──────────┘ └ dépôt ────┘ └étiquette┘
```

👉 Explication : sans hôte, le registre public par défaut est supposé ; sans étiquette, `latest`.

![Cycle de vie : Dockerfile vers image locale par build, push vers un registre, pull vers un autre hôte, puis run pour créer un conteneur](images/docker-fondamentaux-4.svg)
*Figure 4 — Du Dockerfile au conteneur, en passant par le registre.*

Publier une image dans un registre privé de laboratoire (adresse fictive) :

```bash
docker login registry.example.com
docker tag demo-api:1.0 registry.example.com/equipe/demo-api:1.0
docker push registry.example.com/equipe/demo-api:1.0
```

👉 Explication : `login` demande vos identifiants (saisis de façon interactive, jamais dans un script en clair) ; `tag` ajoute le nom complet du registre ; `push` envoie les couches manquantes. Le domaine `example.com` est fictif : cette commande échouera tant que vous ne l'adaptez pas à votre registre.

Récupérer l'image sur un autre hôte :

```bash
docker pull registry.example.com/equipe/demo-api:1.0
docker image inspect --format '{{index .RepoDigests 0}}' registry.example.com/equipe/demo-api:1.0
```

👉 Explication : `pull` télécharge l'image ; la seconde commande affiche son **digest** (`sha256:…`), l'empreinte unique du contenu. Référencer `depot@sha256:…` garantit de lancer exactement la même image, alors qu'une étiquette peut être déplacée par son propriétaire.

**Images de base** : privilégiez les images officielles, des étiquettes précises (`postgres:16.4`) et des variantes minimales ; une image inconnue s'exécute avec les droits du démon sur votre hôte. Avant tout nettoyage, `docker system df` (lecture seule) montre l'espace occupé ; `docker system prune` et `docker volume prune` **suppriment des données** : sauvegardez et vérifiez d'abord.

---

## Mise en pratique guidée

**Cadre** : VM Linux jetable de laboratoire, avec accès console de secours (console de l'hyperviseur). Aucune donnée réelle. Toutes les commandes ci-dessous sont **non testées sur la plateforme cible** par l'auteur.

**Avant de commencer — sécurité de la manipulation** : prenez un **snapshot** de la VM (nommé `avant-docker`). L'installation du moteur modifie les paquets, ajoute un démon et des règles de pare-feu. En cas de problème, retour au snapshot.

### Étape 1 — Installer Docker Engine (si autorisé)

Suivez la procédure officielle d'installation pour votre distribution (lien dans « Pour aller plus loin »). Elle ajoute le dépôt de paquets de l'éditeur, puis installe les paquets du moteur. Vérifiez ensuite :

```bash
docker --version
systemctl is-active docker
```

👉 Explication : affiche la version installée et confirme que le service tourne (`active`). Si `docker` n'est pas reconnu, l'installation n'est pas terminée.

Droits : l'appartenance au groupe `docker` équivaut à des droits administrateur sur l'hôte (le démon tourne en root). En laboratoire, utilisez `sudo docker …` ou le mode sans privilèges (« rootless ») plutôt que d'ajouter un compte partagé au groupe.

### Étape 2 — Votre première application conteneurisée

```bash
mkdir -p ~/lab-docker/app && cd ~/lab-docker
printf 'Bonjour depuis un conteneur\n' > app/index.html
```

👉 Explication : crée un dossier de travail et une page d'accueil minimale ; rien n'est écrit hors de votre dossier personnel.

Créez le fichier `Dockerfile` :

```dockerfile
FROM nginx:1.27-alpine
COPY app/ /usr/share/nginx/html/
```

👉 Explication : une image nginx légère dans laquelle on copie notre page ; deux instructions suffisent, donc deux couches ajoutées à celles de la base.

Construire et lancer :

```bash
docker build -t lab-web:1.0 .
docker run -d --name lab-web -p 127.0.0.1:8080:80 lab-web:1.0
curl -s http://127.0.0.1:8080
```

👉 Explication : construit l'image, la lance en publiant le port 8080 **uniquement sur la boucle locale** (pas d'exposition réseau), puis vérifie le contenu servi, qui doit afficher « Bonjour depuis un conteneur ».

### Étape 3 — Observer les couches et le cache

```bash
docker history lab-web:1.0
printf 'Version 2\n' > app/index.html
docker build -t lab-web:1.1 .
```

👉 Explication : l'historique montre les couches ; après modification de la page, la reconstruction ne refait que la dernière couche (les lignes « CACHED » en sortie du build indiquent les couches réutilisées).

### Étape 4 — Persistance avec un volume

```bash
docker volume create labdata
docker run --rm -v labdata:/data alpine:3.20 sh -c 'echo test > /data/fichier.txt'
docker run --rm -v labdata:/data alpine:3.20 cat /data/fichier.txt
```

👉 Explication : le premier conteneur écrit un fichier dans le volume puis disparaît ; le second, entièrement neuf, relit le fichier, ce qui prouve que la donnée a survécu au conteneur.

### Étape 5 — Nettoyage et retour arrière

```bash
docker rm -f lab-web
docker volume rm labdata
docker image rm lab-web:1.0 lab-web:1.1
```

👉 Explication : supprime uniquement les objets créés par ce labo, en les nommant un par un (pas de `prune` global). Si l'environnement reste instable, restaurez le snapshot `avant-docker`.

Résultat attendu : `docker ps -a` ne liste plus aucun objet du labo ; `docker volume ls` n'affiche plus `labdata`.

---

## Exercices

1. **(Facile)** Décrivez en trois phrases la différence entre une image et un conteneur. Qu'arrive-t-il aux fichiers écrits dans un conteneur lorsqu'on le supprime ?
2. **(Moyen)** Un Dockerfile contient `COPY . .` en deuxième ligne puis `RUN pip install -r requirements.txt`. Pourquoi chaque modification du code provoque-t-elle une réinstallation complète des dépendances ? Proposez l'ordre corrigé.
3. **(Moyen)** Écrivez la commande qui lance nginx en arrière-plan sous le nom `intranet`, avec un volume nommé `site` monté en lecture seule dans `/usr/share/nginx/html`, joignable uniquement depuis l'hôte sur le port 8088.
4. **(Moyen)** Deux conteneurs, `web` et `db`, doivent communiquer par nom. Expliquez pourquoi le réseau `bridge` par défaut ne suffit pas et quelles commandes mettre en œuvre.
5. **(Avancé)** Un développeur a ajouté `ENV DB_PASSWORD=Secret!` dans son Dockerfile puis a supprimé la ligne dans le commit suivant. Le secret est-il toujours exposé ? Que faire ?
6. **(Avancé)** Vous devez déployer `demo-api` sur trois serveurs à partir d'un registre interne. Décrivez la chaîne complète, et expliquez l'intérêt d'utiliser le digest plutôt que l'étiquette `latest`.

## Corrigés des exercices

1. Une image est un modèle immuable en couches ; un conteneur en est une instance avec une couche inscriptible et un processus. À la suppression du conteneur, ses écritures sont perdues, sauf dans un volume ou un bind mount.
2. `COPY . .` placé avant l'installation invalide la couche à chaque modification du code, donc aussi `pip install`. Ordre correct : `COPY requirements.txt .`, `RUN pip install -r requirements.txt`, puis `COPY . .`.
3. `docker run -d --name intranet -p 127.0.0.1:8088:80 -v site:/usr/share/nginx/html:ro nginx:1.27` : `127.0.0.1` limite l'accès à l'hôte, `:ro` interdit l'écriture.
4. Le `bridge` par défaut n'offre pas de DNS entre conteneurs. Créez `docker network create appnet`, puis lancez les deux conteneurs avec `--network appnet` : ils se joignent par `web` et `db`.
5. **Oui**, le secret reste exposé : il subsiste dans les couches des images déjà construites ou publiées et dans l'historique Git. Le considérer comme compromis et le renouveler, reconstruire et republier l'image sans lui, retirer les anciennes images, puis fournir les secrets à l'exécution.
6. `docker build -t registry.example.com/equipe/demo-api:1.0 .`, `docker login`, `docker push`, puis sur chaque serveur `login`, `pull`, `run`. Le digest (`@sha256:…`) désigne un contenu immuable ; `latest` peut donner des versions différentes selon la date du tirage.

## Quiz

**Q1. Que partagent les conteneurs d'un même hôte Linux ?** A) Le système de fichiers racine B) Le noyau C) Les adresses IP D) La mémoire des processus
**Réponse : B.** Chacun a ses espaces de noms et son système de fichiers ; seul le noyau est commun (d'où la légèreté, et la portée d'une faille du noyau).

**Q2. Qu'est-ce qui est en lecture seule ?** A) La couche du conteneur B) Les couches d'une image C) Un volume D) Un bind mount sans `:ro`
**Réponse : B.** Les couches d'image sont immuables ; le reste est inscriptible.

**Q3. Pourquoi copier `requirements.txt` avant le code ?** A) Syntaxe B) Taille finale C) Cache de build D) Réseau
**Réponse : C.** Les dépendances changent rarement : leur couche reste en cache quand seul le code évolue.

**Q4. `EXPOSE 8000` dans un Dockerfile…** A) Ouvre le port sur l'hôte B) Documente le port C) Active le pare-feu D) Rend le port privé
**Réponse : B.** C'est une métadonnée ; seule l'option `-p` publie un port.

**Q5. Quelle option conserve des données après suppression du conteneur ?** A) `--rm` B) `-v mesdonnees:/data` C) `docker stop` D) `docker commit`
**Réponse : B.** Un volume nommé vit indépendamment du conteneur ; `--rm` supprime au contraire le conteneur.

**Q6. Intérêt d'un réseau défini par l'utilisateur ?** A) Plus de débit B) DNS par nom de conteneur C) Pas de pare-feu D) Accès Internet direct
**Réponse : B.** On écrit `db` plutôt qu'une adresse IP variable.

**Q7. Pourquoi éviter `latest` en production ?** A) Payante B) Inexistante C) Étiquette mobile, déploiements non reproductibles D) Supprime le cache
**Réponse : C.** Elle désigne la dernière version publiée, qui change dans le temps.

**Q8. Où se retrouve un secret écrit par `ENV` dans un Dockerfile ?** A) Nulle part B) Seulement dans le conteneur C) Dans l'image (`docker history`/`inspect`) D) En [[Glossary:RAM]] uniquement
**Réponse : C.** `ENV` et `ARG` sont enregistrés dans les métadonnées de l'image.

**Q9. Que fait `docker volume prune` ?** A) Compresse B) Supprime les volumes non utilisés par un conteneur C) Sauvegarde D) Liste
**Réponse : B.** Opération destructrice : sauvegardez et vérifiez avant.

**Q10. Pourquoi le groupe `docker` est-il sensible ?** A) Accès Internet B) Équivaut à root sur l'hôte C) Bloque les mises à jour D) Chiffre les images
**Réponse : B.** Monter la racine de l'hôte dans un conteneur permet de la modifier ; limitez ce groupe, envisagez le mode rootless.

## Erreurs fréquentes et dépannage

| Symptôme | Cause probable | Piste de résolution |
|---|---|---|
| `permission denied … docker.sock` | pas d'accès au démon | `sudo` en laboratoire ou mode rootless |
| `Cannot connect to the Docker daemon` | démon arrêté | `systemctl status docker`, démarrer le service |
| `port is already allocated` | port hôte déjà pris | autre port ; `ss -ltn` pour trouver l'occupant |
| Le conteneur s'arrête aussitôt | processus principal terminé ou planté | `docker logs NOM` ; vérifier `CMD` et variables obligatoires |
| `executable file not found` pour `sh` | image minimale sans shell | s'appuyer sur `logs` ou un conteneur de débogage sur le même réseau |
| Données disparues | écriture hors volume | volume nommé au bon chemin ; `docker volume ls` |
| Build toujours lent | contexte trop gros, mauvais ordre | `.dockerignore`, code après les dépendances |
| `manifest unknown` / `pull access denied` | étiquette ou nom erroné, dépôt privé | vérifier le nom, `docker login` |
| Disque plein | images et journaux accumulés | `docker system df`, suppression ciblée |
| Service joignable à tort | port publié sur toutes les interfaces | lier à `127.0.0.1` ; tester depuis une autre machine |

Méthode : `docker ps -a` (état), `docker logs` (symptômes), `docker inspect` (configuration réelle), `docker exec` (observation interne). Ne « réparez » jamais un conteneur à la main : corrigez l'image ou la configuration et recréez-le.

## À retenir

- Conteneur = processus isolé partageant le noyau ; image = modèle en couches immuables.
- Écritures éphémères : données utiles dans un **volume**, sauvegardé à part.
- Dépendances d'abord, code ensuite : c'est l'ordre du cache.
- Aucun secret dans l'image ; ne publiez que les ports nécessaires, de préférence sur `127.0.0.1`.
- Épinglez les versions (étiquette précise, mieux : digest), images minimales de provenance connue.
- Snapshot avant toute modification d'hôte ; nettoyage ciblé plutôt que `prune` global.

## Pour aller plus loin

- Documentation officielle Docker : <https://docs.docker.com/>
- Installation de Docker Engine : <https://docs.docker.com/engine/install/>
- Référence du Dockerfile : <https://docs.docker.com/reference/dockerfile/>
- Bonnes pratiques de construction : <https://docs.docker.com/build/building/best-practices/>
- Volumes et réseaux : <https://docs.docker.com/engine/storage/volumes/> et <https://docs.docker.com/engine/network/>
- Spécifications OCI (images, distribution) : <https://opencontainers.org/>
- Suite de la série : [Compose, sécurité des conteneurs et introduction à Kubernetes](/fr/00-cours-theoriques/tout-en-un/06-virtualisation-conteneurs-cloud/lecons/lecon-compose-securite-kubernetes)

## Crédits des images

| Fichier | Source (URL Commons) | Auteur | Licence (nom + URL) | Modifications |
|---|---|---|---|---|
| `images/docker-fondamentaux-1.svg` à `-4.svg` | Création originale, aucune source externe | Projet Pack Master | CC0 1.0 — <https://creativecommons.org/publicdomain/zero/1.0/> | Sans objet |

Mention : « Création originale du projet Pack Master, dédiée au domaine public (CC0) ». Aucune image libre n'a pu être vérifiée sur Wikimedia Commons ([[Glossary:API]] indisponible, limitation de débit) ; des schémas originaux ont donc été créés.

## Historique de vérification

| Date | OS/logiciel | Testeur | Verdict |
|---|---|---|---|
| 2026-11-01 | Docker Engine (non installé sur la machine de rédaction ; aucune commande Docker exécutée) | Rédaction assistée par IA, relecture humaine à faire | Non testé sur plateforme cible |