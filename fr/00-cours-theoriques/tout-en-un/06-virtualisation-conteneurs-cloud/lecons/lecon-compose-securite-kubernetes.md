---
title: "Leçon — Docker Compose, sécurité des conteneurs et introduction à Kubernetes"
description: "À l'issue de cette leçon, vous saurez :"
published: true
date: 2026-11-03T14:22:28Z
tags: ["transverse", "tout-en-un", "lecon", "virtualisation", "conteneurs", "docker-compose", "securite", "kubernetes"]
editor: markdown
dateCreated: 2026-11-03T14:22:28Z
dateModified: 2026-11-03T14:22:28Z
---

# Leçon — Docker Compose, sécurité des conteneurs et introduction à Kubernetes

- **Tags** : `transverse`, `tout-en-un`, `lecon`, `virtualisation`, `conteneurs`, `docker-compose`, `securite`, `kubernetes`
- **Niveau** : intermédiaire (suite de la leçon sur les fondamentaux Docker)
- **Durée estimée** : 4 h (cours 1 h 45, labo guidé 1 h 30, exercices et quiz 45 min)

> **Avertissement de test** : Docker, Compose et Kubernetes n'étaient pas installés sur la machine de rédaction et rien n'y a été installé. **Toutes les commandes et tous les fichiers de cette leçon sont non testés sur la plateforme cible.** Validez-les dans une [[Glossary:VM]] jetable avant tout usage.

---

## Objectifs pédagogiques

À l'issue de cette leçon, vous saurez :

1. Décrire une application multi-conteneurs dans un fichier **Compose** (services, réseaux, volumes, secrets) et la piloter avec `docker compose`.
2. Appliquer le durcissement essentiel : **utilisateur non root**, lecture seule, capacités retirées, **secrets** hors de l'image, limites de ressources.
3. Choisir et vérifier des images **minimales**, **signées**, épinglées par digest et analysées.
4. Expliquer pourquoi et quand passer à **Kubernetes**, et décrire son architecture.
5. Lire et écrire un **Deployment** et un **Service**, puis réaliser une mise à jour progressive et un retour arrière.

## Prérequis et durée

- Avoir suivi la leçon [Docker : images, conteneurs, couches, volumes, réseaux, Dockerfile et registres](/fr/00-cours-theoriques/tout-en-un/06-virtualisation-conteneurs-cloud/lecons/lecon-docker-fondamentaux).
- Savoir lire du YAML (indentation par espaces, listes avec `-`, jamais de tabulations).
- Une VM Linux jetable avec accès console de secours, Docker Engine et le plugin Compose ; pour Kubernetes, minikube ou kind dans cette VM (4 Go de [[Glossary:RAM]] conseillés).
- Durée : 4 h.

## L'essentiel en bref

- **Compose** décrit une pile applicative dans `compose.yaml` et la démarre avec `docker compose up -d` : idéal sur **un seul hôte**.
- Un conteneur compromis hérite des privilèges qu'on lui a donnés : appliquez le **moindre privilège**.
- Un secret ne va **jamais** dans l'image ; on le monte en **fichier**.
- Une image sûre est **petite**, de provenance connue, **épinglée** par digest, **signée** et **analysée**.
- **Kubernetes** orchestre des conteneurs sur **plusieurs machines** : il maintient un état désiré et répare automatiquement.
- Objets de base : **Pod** (unité d'exécution), **Deployment** (maintient N Pods, gère les mises à jour), **Service** (adresse stable).

---

## 1. Docker Compose : une pile applicative dans un fichier

Enchaîner à la main trois `docker run` avec réseaux, volumes et options n'est ni reproductible ni documenté. Compose les remplace par un fichier **déclaratif** : vous décrivez l'état voulu, Compose le réalise. Le fichier se versionne avec le code (hors secrets).

![Pile Compose : un proxy sur le réseau front, une application sur front et back, une base de données sur back avec un volume et un secret](images/compose-securite-kubernetes-1.svg)
*Figure 1 — Trois services, deux réseaux (back est interne), un volume pour la base et un secret monté en fichier.*

Fichier correspondant (noms fictifs ; aucun secret en clair) :

```yaml
name: demo

services:
  proxy:
    image: nginxinc/nginx-unprivileged:1.27-alpine
    ports:
      - "127.0.0.1:8080:8080"
    volumes:
      - ./proxy.conf:/etc/nginx/conf.d/default.conf:ro
    networks: [front]
    depends_on: [app]
    read_only: true
    tmpfs: [/tmp]
    cap_drop: [ALL]
    security_opt: ["no-new-privileges:true"]

  app:
    image: demo-api:1.0
    build: ./app
    environment:
      DB_HOST: db
      DB_PASSWORD_FILE: /run/secrets/db_password
    secrets: [db_password]
    networks: [front, back]
    depends_on:
      db:
        condition: service_healthy
    user: "10001:10001"
    read_only: true
    tmpfs: [/tmp]
    cap_drop: [ALL]
    security_opt: ["no-new-privileges:true"]
    mem_limit: 256m
    pids_limit: 100

  db:
    image: postgres:16
    environment:
      POSTGRES_PASSWORD_FILE: /run/secrets/db_password
    secrets: [db_password]
    volumes:
      - dbdata:/var/lib/postgresql/data
    networks: [back]
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 3s
      retries: 5

networks:
  front:
  back:
    internal: true

volumes:
  dbdata:

secrets:
  db_password:
    file: ./secrets/db_password.txt
```

👉 Explication : `proxy` est le seul service à publier un port, et seulement sur la boucle locale ; `app` rejoint les deux réseaux et lit son mot de passe dans un fichier de secret ; `db` n'est que sur `back`, réseau `internal` donc sans accès sortant ; le `healthcheck` conditionne le démarrage de l'application. Les clés `read_only`, `cap_drop`, `security_opt`, `user`, `mem_limit` sont détaillées en section 4.

Le fichier `proxy.conf` associé :

```nginx
server {
    listen 8080;
    location / {
        proxy_pass http://app:8000;
    }
}
```

👉 Explication : nginx écoute sur le port 8080 (non privilégié, indispensable en non-root) et relaie vers le service `app`, résolu par le [[Glossary:DNS]] interne du réseau `front`.

À retenir sur la structure : `services` (un bloc par conteneur), `networks` (`internal: true` coupe l'accès extérieur), `volumes` (volumes nommés), `secrets` (fichiers montés en lecture seule dans `/run/secrets/<nom>`, absents de l'image). Pas de clé `version:` : elle est obsolète.

## 2. Piloter la pile avec `docker compose`

Préparer le secret, hors de Git :

```bash
mkdir -p secrets
umask 077
openssl rand -base64 18 > secrets/db_password.txt
printf 'secrets/\n' >> .gitignore
```

👉 Explication : génère un mot de passe aléatoire lisible par vous seul dans un fichier ignoré par Git ; en laboratoire c'est un secret jetable, en production on utilise un gestionnaire de secrets.

Valider, démarrer, observer, arrêter :

```bash
docker compose config --quiet && echo "compose.yaml valide"
docker compose up -d --build
docker compose ps
docker compose logs --tail 30 app
docker compose down
```

👉 Explication : `config --quiet` signale toute erreur de syntaxe ; `up -d --build` construit et démarre en arrière-plan ; `ps` montre l'état et la santé de chaque service ; `logs` affiche la fin des journaux ; `down` supprime conteneurs et réseaux **en conservant** les volumes.

**Attention** : `docker compose down -v` supprime aussi les volumes, donc les données de la base. À réserver au laboratoire.

Autres commandes utiles : `docker compose exec app sh`, `docker compose restart app`, `docker compose pull`, `docker compose up -d --force-recreate`. Compose lit aussi un fichier `.env` pour substituer `${VARIABLE}` (étiquette d'image, port) : utile pour la configuration, **pas** pour les secrets, car ce fichier finit souvent dans un dépôt.

Compose ne répartit pas la charge sur plusieurs machines, ne répare pas seul une panne d'hôte et ne met pas à jour sans interruption : ces besoins relèvent d'un orchestrateur (section 6).

## 3. Les risques propres aux conteneurs

Un conteneur est un processus de l'hôte avec des restrictions, pas une VM. Les erreurs graves viennent presque toujours de la configuration :

- **Processus en root** (image sans `USER`) : une faille applicative donne root dans le conteneur, premier pas d'une évasion.
- **`--privileged`** : quasiment plus d'isolement, accès aux périphériques de l'hôte.
- **Socket Docker montée** (`-v /var/run/docker.sock:…`) : le conteneur pilote le démon, donc l'hôte.
- **Secret dans l'image** (`ENV TOKEN=…`) : fuite pour quiconque récupère l'image.
- **Image non maîtrisée** (`FROM inconnu/image:latest`) : code vulnérable ou malveillant exécuté chez vous.
- **Ports publiés partout** (`-p 5432:5432`) : base exposée à tout le réseau.

La réponse commune est le **moindre privilège**.

![Empilement de protections autour d'un conteneur : hôte à jour, réseau restreint et limites, conteneur en lecture seule sans capacités, processus non root avec image minimale signée, secrets et volumes ciblés](images/compose-securite-kubernetes-2.svg)
*Figure 2 — Défense en profondeur : chaque couche réduit les dégâts si la précédente cède.*

## 4. Durcir un conteneur : les gestes concrets

**Utilisateur non root.** Par défaut le processus est root *dans son espace de noms*. Dans le Dockerfile, créez un compte et basculez avec `USER 10001` ; à défaut, forcez `--user 10001:10001` ou la clé `user:`. Un non-root ne peut pas écouter sous le port 1024 : utilisez 8080, 8000…

**Lecture seule.** Avec `read_only: true`, le conteneur ne peut plus modifier sa racine : un attaquant ne peut pas y déposer d'outils. L'écriture légitime passe par un `tmpfs` pour `/tmp` et par des volumes ciblés.

**Capacités et privilèges.** Le noyau découpe les pouvoirs de root en « capacités ». Retirez-les toutes (`cap_drop: [ALL]`) et ne rajoutez que le nécessaire ; `no-new-privileges` empêche de gagner des droits via un binaire setuid. Certaines images de bases de données démarrent en root puis abandonnent leurs droits : testez le retrait progressivement.

**Limites de ressources.** `mem_limit`, `cpus`, `pids_limit` évitent qu'un conteneur emballé épuise l'hôte.

**Réseau minimal.** Réseaux séparés par rôle, `internal: true` pour la base, ports publiés sur `127.0.0.1` ou derrière un proxy, jamais `network_mode: host` sans raison forte.

Équivalent en ligne de commande pour un conteneur isolé :

```bash
docker run -d --name api-secure \
  --user 10001:10001 \
  --read-only --tmpfs /tmp \
  --cap-drop ALL \
  --security-opt no-new-privileges:true \
  --memory 256m --pids-limit 100 \
  -p 127.0.0.1:8000:8000 \
  demo-api:1.0
```

👉 Explication : lance l'application avec un compte non privilégié, une racine en lecture seule, aucune capacité Linux, l'interdiction de gagner des privilèges, des plafonds mémoire et processus, et un port accessible seulement depuis l'hôte.

Vérifier le résultat réel :

```bash
docker exec api-secure id
docker inspect -f 'User={{.Config.User}} ReadOnly={{.HostConfig.ReadonlyRootfs}} CapDrop={{.HostConfig.CapDrop}}' api-secure
```

👉 Explication : `id` affiche l'identité effective du processus (10001, pas 0) ; `inspect` confirme les paramètres de sécurité réellement appliqués, plus fiable qu'une relecture du fichier.

## 5. Gérer les secrets correctement

De la pire à la meilleure pratique :

1. **À proscrire** : secret dans le Dockerfile (`ENV`, `ARG`, `COPY`) ou dans Git.
2. **Insuffisant** : variable `-e DB_PASSWORD=…`, visible via `docker inspect` et `/proc`.
3. **Correct en petite infrastructure** : secret **monté en fichier** (secrets Compose) et lu via une variable `*_FILE`.
4. **Recommandé en production** : coffre de secrets avec rotation, droits par application et journal d'accès.

Un secret exposé est **compromis** : on le révoque et on le renouvelle, on ne se contente pas de l'effacer du code.

## 6. Images minimales, signées et analysées

**Minimales** : variantes `-slim`, `alpine` ou distroless, build multi-étapes ; moins de logiciels, moins de vulnérabilités. **Épinglées** : une étiquette est mobile, un **digest** est immuable ; référencez `image: depot/nom@sha256:<empreinte>` et mettez à jour volontairement. **Tenues à jour** : reconstruisez régulièrement pour récupérer les correctifs.

**Signées** : une signature prouve l'éditeur et l'intégrité. Exemple avec Sigstore/cosign (identités fictives à adapter) :

```bash
cosign verify registry.example.com/equipe/demo-api:1.0 \
  --certificate-identity "https://example.com/equipe/ci" \
  --certificate-oidc-issuer "https://token.actions.example.com"
```

👉 Explication : vérifie que l'image est signée par l'identité attendue avant déploiement ; en cas d'échec, ne l'utilisez pas. Remplacez les valeurs `example.com` par celles de votre chaîne de livraison.

**Analysées** : un scanner compare les paquets de l'image aux vulnérabilités connues ; à lancer en intégration continue puis régulièrement, car de nouvelles failles apparaissent après publication.

```bash
trivy image --severity HIGH,CRITICAL demo-api:1.0
```

👉 Explication : liste les vulnérabilités hautes ou critiques de l'image ; c'est une aide à la décision, à croiser avec l'exploitabilité réelle (Docker Scout et Grype font la même chose).

---

## 7. Pourquoi Kubernetes ?

Compose gère un hôte. Si cet hôte tombe, si la charge augmente ou s'il faut mettre à jour sans coupure, il faut un **orchestrateur**. **Kubernetes** (K8s) reçoit **ce que vous voulez** (« trois copies de cette application en version 1.2 ») et décide **comment** : placement, relance, mise à jour. Analogie : Compose est un chef dans une cuisine ; Kubernetes est le directeur qui répartit les cuisiniers entre plusieurs cuisines et remplace aussitôt celui qui s'absente.

![Architecture d'un cluster : un administrateur dialogue en HTTPS avec le serveur d'API du plan de contrôle, composé d'etcd, du planificateur et de contrôleurs, qui pilote deux nœuds exécutant kubelet, kube-proxy et les Pods](images/compose-securite-kubernetes-3.svg)
*Figure 3 — Un plan de contrôle décide ; des nœuds de travail exécutent.*

Le principe central est la **boucle de réconciliation** : des contrôleurs comparent sans cesse l'état *désiré* à l'état *réel* et corrigent l'écart. Si un Pod disparaît, un autre est créé.

- **kube-apiserver** : porte d'entrée unique (kubectl, contrôleurs, kubelet).
- **etcd** : base clé-valeur de l'état du cluster, à sauvegarder impérativement.
- **scheduler** : choisit le nœud d'un nouveau Pod.
- **controller manager** : exécute les boucles de réconciliation.
- **kubelet** : agent du nœud, démarre les conteneurs ; **kube-proxy** : règles réseau des Services.

Kubernetes est puissant mais **complexe** (apprentissage, surface d'attaque, exploitation). Pour un petit service sur un serveur, Compose reste souvent le bon choix ; beaucoup d'organisations utilisent un Kubernetes **managé** par un fournisseur cloud qui gère le plan de contrôle.

## 8. Pods, Deployments et Services

![Un Ingress route vers un Service qui sélectionne par étiquette trois Pods web gérés par un ReplicaSet lui-même piloté par un Deployment](images/compose-securite-kubernetes-4.svg)
*Figure 4 — Deployment, ReplicaSet, Pods et Service : qui crée quoi, qui route vers qui.*

**Pod** : plus petite unité déployable, un ou plusieurs conteneurs partageant [[Glossary:IP]] et volumes. Il est **éphémère** : s'il disparaît, son adresse change. On le crée rarement à la main.

**Deployment** : état voulu d'une application sans état (image, réplicas, stratégie de mise à jour). Il crée un **ReplicaSet** qui maintient le bon nombre de Pods ; à chaque nouvelle version, un nouveau ReplicaSet prend progressivement le relais (*rolling update*).

**Service** : **adresse et nom DNS stables** devant des Pods choisis par **étiquettes**. Types : `ClusterIP` (interne, défaut), `NodePort`, `LoadBalancer` (fourni par le cloud). Un **Ingress** ajoute un routage [[Glossary:HTTP]] par nom d'hôte et chemin.

Manifeste `web.yaml` (noms fictifs) :

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web
  namespace: demo
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxUnavailable: 1
      maxSurge: 1
  template:
    metadata:
      labels:
        app: web
    spec:
      securityContext:
        runAsNonRoot: true
        runAsUser: 101
        seccompProfile:
          type: RuntimeDefault
      containers:
        - name: nginx
          image: nginxinc/nginx-unprivileged:1.27-alpine
          ports:
            - containerPort: 8080
          resources:
            requests: { cpu: "50m", memory: "64Mi" }
            limits: { cpu: "200m", memory: "128Mi" }
          readinessProbe:
            httpGet: { path: /, port: 8080 }
            initialDelaySeconds: 3
          securityContext:
            allowPrivilegeEscalation: false
            readOnlyRootFilesystem: true
            capabilities:
              drop: ["ALL"]
          volumeMounts:
            - { name: tmp, mountPath: /tmp }
      volumes:
        - name: tmp
          emptyDir: {}
---
apiVersion: v1
kind: Service
metadata:
  name: web
  namespace: demo
spec:
  type: ClusterIP
  selector:
    app: web
  ports:
    - port: 80
      targetPort: 8080
```

👉 Explication : le Deployment demande trois Pods nginx mis à jour un par un, chacun en non-root, sans élévation de privilèges, racine en lecture seule, capacités retirées ; `requests` aide le placement, `limits` plafonne ; la `readinessProbe` n'envoie du trafic qu'aux Pods prêts. Le Service `web` expose ces Pods sur le port 80 dans le cluster, via l'étiquette `app: web`. Le séparateur `---` met deux objets dans un seul fichier.

On retrouve les notions de Compose sous d'autres noms (`securityContext`, `resources`). Commandes de base :

```bash
kubectl create namespace demo
kubectl apply -f web.yaml
kubectl -n demo get deploy,po,svc
```

👉 Explication : crée un espace de noms, applique le manifeste de façon déclarative puis liste Deployment, Pods et Service ; les Pods doivent atteindre `Running` et `READY 1/1`.

```bash
kubectl -n demo describe pod -l app=web
kubectl -n demo logs deploy/web --tail=20
kubectl -n demo port-forward svc/web 8080:80
```

👉 Explication : `describe` détaille événements et erreurs (premier réflexe en panne) ; `logs` lit les journaux d'un Pod ; `port-forward` relaie temporairement le port local 8080 vers le Service pour tester avec `curl http://127.0.0.1:8080` sans rien exposer.

Mise à l'échelle, mise à jour, retour arrière :

```bash
kubectl -n demo scale deploy/web --replicas=5
kubectl -n demo set image deploy/web nginx=nginxinc/nginx-unprivileged:1.27.1-alpine
kubectl -n demo rollout status deploy/web
kubectl -n demo rollout undo deploy/web
```

👉 Explication : passe à cinq réplicas ; déploie une nouvelle image progressivement ; suit l'avancement ; `undo` revient à la révision précédente si la nouvelle version pose problème. En pratique, on modifie le manifeste versionné et on le réapplique.

À connaître ensuite : **ConfigMap** (configuration non sensible), **Secret** (encodé en base64, **non chiffré par défaut** dans etcd : activez le chiffrement au repos et restreignez l'accès), **Namespace**, **PersistentVolumeClaim**, **NetworkPolicy** (pare-feu entre Pods) et **[[Glossary:RBAC]]** (qui peut faire quoi sur l'[[Glossary:API]]).

---

## Mise en pratique guidée

**Cadre** : VM Linux jetable avec accès console de secours, sans donnée réelle. Commandes **non testées sur la plateforme cible**.

**Sécurité de la manipulation** : prenez un **snapshot** de la VM (`avant-compose-k8s`) ; un Kubernetes local modifie le réseau et des paramètres noyau. Retour arrière : restauration du snapshot.

### Partie A — Pile Compose durcie

Créez `~/lab-compose` avec `compose.yaml` et `proxy.conf` (section 1), un dossier `app/` contenant le Dockerfile de `demo-api`, puis le secret :

```bash
mkdir -p ~/lab-compose/secrets && cd ~/lab-compose
umask 077 && openssl rand -base64 18 > secrets/db_password.txt
```

👉 Explication : prépare le dossier de travail et un secret aléatoire jetable, dans votre dossier personnel.

Validez, démarrez, contrôlez :

```bash
docker compose config --quiet && docker compose up -d --build
docker compose ps
curl -s -o /dev/null -w '%{http_code}\n' http://127.0.0.1:8080
```

👉 Explication : valide la syntaxe, démarre la pile, vérifie que les services sont `running` (et la base `healthy`), puis teste le proxy ; le code HTTP attendu dépend de votre application (200 si elle répond correctement).

Prouvez l'isolation :

```bash
docker compose port db 5432 || echo "aucun port publié pour db (attendu)"
docker compose exec app id
```

👉 Explication : confirme qu'aucun port de la base n'est publié sur l'hôte et que l'application ne tourne pas en root (identité 10001).

Nettoyage :

```bash
docker compose down
```

👉 Explication : arrête la pile et supprime conteneurs et réseaux ; le volume `dbdata` est conservé (ajoutez `-v` seulement pour tout effacer en fin de labo).

### Partie B — Premier déploiement Kubernetes local

Installez minikube ou kind (documentation officielle, liens ci-dessous), puis vérifiez :

```bash
kubectl cluster-info
kubectl get nodes
```

👉 Explication : confirme que le client joint l'API et que le nœud est `Ready` ; en cas d'échec, ne poursuivez pas.

Créez l'espace de noms `demo` s'il n'existe pas (`kubectl create namespace demo`), puis appliquez `web.yaml` :

```bash
kubectl apply -f web.yaml
kubectl -n demo rollout status deploy/web
kubectl -n demo get po -o wide
```

👉 Explication : crée le Deployment et le Service, attend la fin du déploiement et affiche les Pods avec leur nœud et leur adresse interne.

Testez l'auto-réparation en supprimant un seul Pod (laboratoire uniquement) :

```bash
kubectl -n demo delete pod "$(kubectl -n demo get pod -l app=web -o name | head -n 1)"
kubectl -n demo get po
```

👉 Explication : supprime un Pod ; le Deployment en recrée aussitôt un autre pour revenir à trois copies, ce que le second affichage doit montrer.

Retour arrière du labo :

```bash
kubectl delete namespace demo
```

👉 Explication : supprime tout l'espace de noms `demo` (Deployment, Pods, Service) ; destructif, à ne jamais lancer sur un espace inconnu.

---

## Exercices

1. **(Facile)** Citez trois clés Compose de durcissement et dites ce que chacune empêche.
2. **(Facile)** Différence entre `docker compose down` et `docker compose down -v` ?
3. **(Moyen)** La base est publiée par `ports: ["5432:5432"]`. Pourquoi est-ce un problème, et comment corriger ?
4. **(Moyen)** Un collègue veut monter `/var/run/docker.sock` dans un conteneur de supervision. Évaluez le risque, proposez une alternative.
5. **(Moyen)** Classez du plus faible au plus fort : variable `-e`, secret en fichier monté, secret écrit dans le Dockerfile, coffre de secrets.
6. **(Avancé)** Quelles trois précautions combinez-vous pour vérifier qu'une image vient bien de votre chaîne de build ?
7. **(Avancé)** Avec `replicas: 3`, un seul Pod est `Running`, les autres `Pending`. Deux causes probables et les commandes de diagnostic ?

## Corrigés des exercices

1. `read_only: true` (pas d'écriture dans la racine), `cap_drop: [ALL]` (retire les pouvoirs de root), `user: "10001:10001"` (évite le root) ; aussi `no-new-privileges`, `mem_limit`.
2. `down` supprime conteneurs et réseaux et garde les volumes ; `down -v` supprime aussi les volumes nommés : les données sont perdues.
3. La base devient joignable depuis tout le réseau de l'hôte (force brute, failles). Supprimer `ports:` : les services du réseau `back` la joignent par son nom ; pour l'administration, `docker compose exec db psql` ou temporairement `127.0.0.1:5432:5432`.
4. Qui contrôle ce conteneur contrôle le démon, donc l'hôte (création de conteneur privilégié, montage de `/`). Alternatives : exporteur de métriques dédié, proxy de socket restreint en lecture, ou métriques exposées par les applications.
5. Secret dans le Dockerfile < variable `-e` < secret en fichier monté < coffre de secrets avec rotation et audit.
6. Construire l'image dans une chaîne maîtrisée qui la **signe** ; vérifier la signature (cosign) au déploiement ; référencer par **digest** (et la scanner).
7. Ressources insuffisantes (requests supérieures à la capacité), nœud indisponible ou volume introuvable. Diagnostic : `kubectl -n demo describe pod <nom>` (section Events), `kubectl get nodes`, `kubectl describe node`.

## Quiz

**Q1. À quoi sert `docker compose config` ?** A) Démarrer la pile B) Valider et afficher la configuration résolue C) Supprimer les volumes D) Mettre à jour les images
**Réponse : B.** Elle analyse le fichier et signale les erreurs sans rien démarrer.

**Q2. Quel réseau Compose n'a pas d'accès extérieur ?** A) `internal: true` B) Le réseau par défaut C) `network_mode: host` D) Un réseau avec ports publiés
**Réponse : A.** `internal` coupe la connexion vers l'extérieur, idéal pour une base.

**Q3. Pourquoi un conteneur non root ne peut-il pas écouter sur le port 80 ?** A) Docker l'interdit B) Les ports inférieurs à 1024 sont privilégiés C) Déjà utilisé D) Pare-feu
**Réponse : B.** Écoutez sur 8080 dans le conteneur et publiez 80 à l'extérieur si besoin.

**Q4. Que fait `cap_drop: [ALL]` ?** A) Supprime les volumes B) Retire les capacités Linux spéciales C) Désactive le réseau D) Interdit le shell
**Réponse : B.** On ne rajoute que celles strictement nécessaires.

**Q5. Où un secret Compose est-il monté ?** A) `/etc/passwd` B) `/run/secrets/<nom>` C) `/root/.env` D) Dans l'image
**Réponse : B.** Fichier en lecture seule, absent de l'image.

**Q6. Qu'est-ce qui est immuable ?** A) `latest` B) Un digest `sha256:…` C) Le nom du dépôt D) Une étiquette de version
**Réponse : B.** C'est l'empreinte du contenu ; les étiquettes peuvent être déplacées.

**Q7. Un Pod est…** A) Un nœud physique B) Le plus petit objet déployable, éphémère C) Un volume D) Un réseau
**Réponse : B.** Il partage IP et volumes entre ses conteneurs et peut être remplacé à tout moment.

**Q8. Quel objet maintient trois copies et gère les mises à jour progressives ?** A) Service B) ConfigMap C) Deployment D) Namespace
**Réponse : C.** Il pilote un ReplicaSet et orchestre le *rolling update*.

**Q9. À quoi sert un Service ?** A) Stocker des secrets B) Adresse et nom stables devant des Pods choisis par étiquettes C) Construire des images D) Planifier
**Réponse : B.** Les Pods changent d'adresse ; le Service reste constant.

**Q10. Les `Secret` Kubernetes sont-ils chiffrés par défaut dans etcd ?** A) Oui B) Non, seulement encodés en base64 sauf chiffrement au repos activé C) Ils n'y sont pas D) Oui, par kubelet
**Réponse : B.** Le base64 n'est pas du chiffrement : activez le chiffrement au repos et restreignez le RBAC.

## Erreurs fréquentes et dépannage

| Symptôme | Cause probable | Piste de résolution |
|---|---|---|
| Erreur YAML « cannot start any token » | tabulation ou indentation | espaces uniquement ; `docker compose config` |
| L'application démarre avant la base | pas de `healthcheck` | `depends_on` avec `service_healthy` |
| `permission denied` en écriture après `read_only` | écriture hors `/tmp` | ajouter un `tmpfs` ou un volume |
| `bind: permission denied` sur le port 80 | processus non root | écouter sur 8080, publier 80 |
| Secret introuvable | chemin ou nom incorrect | `docker compose exec app ls /run/secrets` |
| `ImagePullBackOff` | image ou étiquette fausse, registre privé | `kubectl describe pod` ; `imagePullSecrets` |
| `CrashLoopBackOff` | plantage au démarrage | `kubectl logs <pod> --previous` |
| Pod `Pending` | ressources ou volume indisponibles | Events de `describe`, `kubectl get nodes` |
| Service sans réponse | sélecteur différent des étiquettes | `kubectl -n demo get endpoints web` doit lister des adresses |
| Connexion à l'API refusée | cluster arrêté, mauvais contexte | `kubectl config current-context` ; redémarrer le cluster |

Méthode : état (`ps` / `get`), détails (`inspect` / `describe`), journaux (`logs`), test depuis l'intérieur du réseau. Corrigez le fichier source et réappliquez ; ne modifiez pas à la main les objets en production.

## À retenir

- Compose décrit une pile sur un hôte ; `config` pour valider, `down` sans `-v` pour garder les données.
- Durcissement minimal : non root, `read_only`, `cap_drop: [ALL]`, `no-new-privileges`, limites, ports publiés seulement si nécessaire.
- Pas de secret dans l'image, le dépôt ou `.env` : fichiers montés, puis coffre de secrets.
- Image sûre : minimale, épinglée par digest, signée, analysée, reconstruite régulièrement.
- Jamais `--privileged` ni socket Docker montée sans raison absolue.
- Kubernetes réconcilie un état désiré : Deployment → ReplicaSet → Pods ; Service = adresse stable.
- Snapshot avant d'installer un cluster, namespace dédié, suppression ciblée.

## Pour aller plus loin

- Compose : <https://docs.docker.com/compose/> et référence du fichier : <https://docs.docker.com/reference/compose-file/>
- Sécurité Docker : <https://docs.docker.com/engine/security/>
- Kubernetes, concepts : <https://kubernetes.io/docs/concepts/> et tutoriel : <https://kubernetes.io/docs/tutorials/kubernetes-basics/>
- Pod Security Standards : <https://kubernetes.io/docs/concepts/security/pod-security-standards/>
- Installation : <https://kind.sigs.k8s.io/> et <https://minikube.sigs.k8s.io/docs/>
- Sigstore / cosign : <https://docs.sigstore.dev/>
- Leçons de la série : [Docker : fondamentaux](/fr/00-cours-theoriques/tout-en-un/06-virtualisation-conteneurs-cloud/lecons/lecon-docker-fondamentaux) ; [Cloud, Microsoft 365 et Entra ID](/fr/00-cours-theoriques/tout-en-un/06-virtualisation-conteneurs-cloud/lecons/lecon-cloud-m365-entra)

## Crédits des images

| Fichier | Source (URL Commons) | Auteur | Licence (nom + URL) | Modifications |
|---|---|---|---|---|
| `images/compose-securite-kubernetes-1.svg` à `-4.svg` | Création originale, aucune source externe | Projet Pack Master | CC0 1.0 — <https://creativecommons.org/publicdomain/zero/1.0/> | Sans objet |

Mention : « Création originale du projet Pack Master, dédiée au domaine public (CC0) ». Aucune image libre n'a pu être vérifiée sur Wikimedia Commons (API indisponible, limitation de débit) ; des schémas originaux ont donc été créés.

## Historique de vérification

| Date | OS/logiciel | Testeur | Verdict |
|---|---|---|---|
| 2026-11-01 | Docker Engine, Compose, Kubernetes, cosign, trivy (absents de la machine de rédaction ; aucune commande exécutée) | Rédaction assistée par IA, relecture humaine à faire | Non testé sur plateforme cible |