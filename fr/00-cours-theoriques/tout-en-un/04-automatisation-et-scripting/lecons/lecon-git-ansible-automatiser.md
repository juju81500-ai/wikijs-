---
title: "Leçon — Git et Ansible pour automatiser : versionner ses scripts et configurer des machines"
description: "À la fin de cette leçon, vous serez capable de :"
published: true
date: 2026-11-03T09:36:13Z
tags: ["transverse", "tout-en-un", "lecon", "automatisation", "git", "ansible", "idempotence", "vault", "secrets"]
editor: markdown
dateCreated: 2026-11-03T09:36:13Z
dateModified: 2026-11-03T09:36:13Z
---

# Leçon — Git et Ansible pour automatiser : versionner ses scripts et configurer des machines

- **Tags** : `transverse`, `tout-en-un`, `lecon`, `automatisation`, `git`, `ansible`, `idempotence`, `vault`, `secrets`
- **Niveau** : Intermédiaire (ligne de commande et [[Glossary:SSH]] de base)
- **Durée estimée** : 4 h (cours 1 h 45, laboratoire 1 h 15, exercices et quiz 1 h)

---

## Objectifs pédagogiques

À la fin de cette leçon, vous serez capable de :

1. expliquer pourquoi et comment **versionner** des scripts avec Git (dépôt, commit, branche, fusion) ;
2. écrire un `.gitignore` adapté et appliquer la règle « **un secret ne se versionne jamais** », y compris savoir réagir si cela arrive ;
3. décrire l'architecture d'Ansible (nœud de contrôle, **inventaire**, modules, **playbooks**) ;
4. rédiger un inventaire et un playbook simples et les valider avec `--syntax-check`, `--check` et `--diff` ;
5. expliquer l'**idempotence** et reconnaître les tâches qui la brisent ;
6. protéger des données sensibles avec **Ansible Vault** (principe) ;

## Prérequis et durée

- Terminal Linux et SSH par clé (notions).
- Un laboratoire **jetable** : un nœud de contrôle Linux ([[Glossary:VM]]) et deux machines cibles Debian/Ubuntu de test, par exemple 192.0.2.11 et 192.0.2.12. Prenez des instantanés avant d'appliquer.
- Aucune adresse réelle, aucun compte réel : cette leçon n'emploie que des valeurs de documentation (192.0.2.0/24, 198.51.100.0/24, 203.0.113.0/24, 2001:db8::/32, `example.com`, `example.test`).
- Durée : environ 4 h.

## L'essentiel en bref

- **Git** garde l'historique de vos fichiers ; **Ansible** décrit l'état souhaité de vos machines. Ensemble : une infrastructure décrite par du texte, relue, testée, traçable.
- Le cycle Git de base : modifier → `git add` → `git commit`. Les **branches** isolent un travail avant fusion.
- `.gitignore` empêche d'ajouter des fichiers par erreur ; il ne protège pas un secret déjà commité. Un secret exposé est **à révoquer**.
- Ansible fonctionne **sans agent**, par SSH, depuis un nœud de contrôle.
- Un playbook déclare un **état** (« ce paquet est présent ») et non une suite de gestes : c'est l'**idempotence**.
- Avant d'appliquer : `--syntax-check`, puis `--check --diff`, sur un petit périmètre (`--limit`).
- **Ansible Vault** chiffre des fichiers ou valeurs ; le mot de passe du coffre reste hors du dépôt.

---

## 1. Pourquoi versionner ses scripts ?

Sans gestion de versions, on obtient `script_final2.ps1`, `script_final_VRAI.ps1`. Git apporte l'**historique** (qui, quand, pourquoi), le **retour en arrière**, le **travail en parallèle** et la **relecture** des différences.

**Analogie.** Git est un carnet de laboratoire à pages numérotées : on n'efface jamais, on ajoute une page datée à chaque changement, et l'on peut rouvrir n'importe quelle page.

![Les trois zones de Git : dossier de travail, index, dépôt local, dépôt distant](images/git-ansible-1.svg)

*Figure 1 — Du fichier modifié au commit, puis au dépôt distant ; le `.gitignore` tient les fichiers sensibles à l'écart. Création originale du projet Pack Master (CC0).*

## 2. Git : les commandes essentielles

### 2.1 Configurer et initialiser

```bash
git --version
git config --global user.name "Prénom Nom"
git config --global user.email "prenom.nom@example.com"
git init -b main ~/labo-scripts
cd ~/labo-scripts
```

👉 Explication : vérifie la présence de Git, déclare l'identité enregistrée dans chaque commit (valeurs fictives ici), puis crée un dépôt dont la branche initiale s'appelle `main`. Un dossier caché `.git` contient tout l'historique : ne le supprimez ni ne le modifiez à la main.

### 2.2 Le cycle modifier → ajouter → valider

```bash
printf '#!/usr/bin/env bash\necho "sauvegarde"\n' > sauvegarde.sh
git status
git add sauvegarde.sh
git commit -m "Ajoute le script de sauvegarde initial"
git log --oneline
```

👉 Explication : crée un fichier, observe qu'il est « non suivi », l'ajoute à l'**index** (zone de préparation) puis l'enregistre dans un **commit**. `git log --oneline` liste les commits récents (identifiant court + message). Le message décrit le **pourquoi** en une phrase claire à l'impératif.

```bash
git diff
git diff --staged
git restore sauvegarde.sh
git restore --staged sauvegarde.sh
```

👉 Explication : `git diff` montre les changements non indexés, `--staged` ceux déjà préparés ; `git restore` annule une modification du dossier de travail (**définitif** pour une modification non commitée, relisez avant), et `git restore --staged` retire un fichier de l'index sans toucher son contenu.

Un commit = un changement cohérent, avec un message qui explique l'intention.

### 2.3 Les branches

Une **branche** est une ligne de développement indépendante. On travaille sur une branche, on teste, puis on fusionne dans `main`.

![Branches Git : une branche de correction part de main puis est fusionnée](images/git-ansible-2.svg)

*Figure 2 — Branche de travail puis fusion dans main. Création originale du projet Pack Master (CC0).*

```bash
git switch -c correction-journal
printf 'echo "fin"\n' >> sauvegarde.sh
git add sauvegarde.sh
git commit -m "Ajoute un message de fin au script"
git switch main
git merge correction-journal
git branch -d correction-journal
git log --oneline --graph --all
```

👉 Explication : crée et change de branche (`-c`), commite dessus, revient sur `main`, fusionne puis supprime la branche devenue inutile ; le journal en graphe visualise l'ensemble. En cas de **conflit** (deux modifications de la même ligne), Git marque le fichier : éditez-le pour garder la bonne version, puis `git add` et `git commit` pour terminer la fusion.

### 2.4 Dépôt distant

```bash
git remote add origin https://git.example.com/infra/scripts.git
git push -u origin main
git pull --ff-only
```

👉 Explication : déclare le dépôt distant (adresse fictive), envoie la branche `main` et mémorise le suivi ; `git pull --ff-only` récupère les nouveautés **sans créer de fusion imprévue** (la commande échoue si l'historique a divergé, ce qui vous prévient). Pour annuler un commit déjà partagé, préférez `git revert <id>` à une réécriture d'historique.

## 3. Secrets : ne jamais les versionner

Un mot de passe, une clé privée SSH, un jeton d'[[Glossary:API]], un fichier d'environnement ou une chaîne de connexion avec identifiants **ne doivent jamais** entrer dans un dépôt. Même supprimé plus tard, il reste dans l'**historique** et dans chaque copie du dépôt déjà clonée.

### 3.1 Le fichier .gitignore

```bash
cat > .gitignore <<'EOF'
# Secrets et clés
*.key
*.pem
id_rsa*
id_ed25519*
.env
*.vault_pass
.vault_pass*
secrets.*

# Fichiers produits
*.log
*.retry
__pycache__/
.venv/
*.tmp
EOF
git check-ignore -v .env
git add .gitignore
git commit -m "Ajoute un .gitignore pour secrets et fichiers produits"
```

👉 Explication : crée la liste des motifs à ignorer (le `'EOF'` entre apostrophes empêche toute interprétation du contenu), vérifie avec `check-ignore -v` quelle règle s'applique à un nom, puis versionne le `.gitignore` lui-même. Les motifs ne concernent que les fichiers **non encore suivis** : un fichier déjà commité reste suivi.

```bash
git rm --cached chemin/vers/fichier
git ls-files | head
```

👉 Explication : `git rm --cached` retire un fichier du suivi sans le supprimer du disque ; `git ls-files` liste ce que Git suit réellement. Cela n'efface pas l'historique passé.

### 3.2 Si un secret a été commité

1. **Considérez-le compromis**, même si le dépôt est privé : révoquez-le et remplacez-le (nouveau mot de passe, nouvelle clé, jeton régénéré).
2. Prévenez le responsable de la sécurité selon la procédure de votre organisation.
3. Seulement ensuite, nettoyez l'historique avec un outil prévu pour cela (par exemple `git filter-repo`) et demandez aux collaborateurs de recloner : c'est une opération lourde, jamais suffisante à elle seule.
4. Ajoutez la règle `.gitignore` et, idéalement, un contrôle automatique avant commit pour éviter la récidive.

Alternatives saines : **Ansible Vault** (section 9), gestionnaire de secrets d'entreprise, variables d'environnement injectées à l'exécution, fichier `config.example` **sans valeurs réelles** versionné à la place du vrai.

## 4. Ansible : l'architecture en un coup d'œil

Ansible configure des machines **sans agent** : un **nœud de contrôle** se connecte en SSH aux **hôtes gérés**, y envoie de petits programmes (les **modules**), les exécute puis les retire.

![Architecture Ansible : un nœud de contrôle avec inventaire et playbook, relié en SSH à des groupes d'hôtes](images/git-ansible-3.svg)

*Figure 3 — Un contrôleur, un inventaire, des hôtes gérés ; les modules sont poussés puis retirés. Création originale du projet Pack Master (CC0).*

Vocabulaire :

| Terme | Signification |
|---|---|
| **Nœud de contrôle** | machine Linux où l'on lance `ansible` et `ansible-playbook` |
| **Inventaire** | liste des hôtes et des groupes à gérer |
| **Module** | unité de travail (installer un paquet, copier un fichier…) |
| **Tâche** | un appel de module avec ses paramètres |
| **Playbook** | fichier YAML qui associe des hôtes à une liste de tâches |
| **Handler** | tâche déclenchée seulement si une autre a changé quelque chose (ex. redémarrer) |

**Analogie.** L'inventaire est la liste des invités, le playbook est la recette, chaque module est un ustensile spécialisé, et le contrôleur est le chef qui passe de table en table.

### 4.1 Installer dans un environnement isolé

```bash
python3 -m venv ~/.venvs/ansible
source ~/.venvs/ansible/bin/activate
python3 -m pip install ansible-core
ansible --version
```

👉 Explication : installe `ansible-core` dans un environnement virtuel (sans toucher aux paquets système) ; `ansible --version` indique la version, le fichier de configuration chargé et le chemin des modules. Le principe : **épingler** la version utilisée par l'équipe.

## 5. L'inventaire

Fichier `inventory.yml` :

```yaml
all:
  children:
    web:
      hosts:
        lab01:
          ansible_host: 192.0.2.11
        lab02:
          ansible_host: 192.0.2.12
    bdd:
      hosts:
        lab03:
          ansible_host: 192.0.2.21
  vars:
    ansible_user: automation
```

👉 Explication : définit deux groupes (`web` et `bdd`) avec trois hôtes fictifs de la plage de documentation ; `ansible_host` donne l'adresse de connexion, `ansible_user` le compte SSH commun. Aucune clé ni mot de passe n'apparaît : l'authentification passe par une **clé SSH** et un agent.

```bash
ansible-inventory -i inventory.yml --graph
ansible-inventory -i inventory.yml --host lab01
ansible -i inventory.yml web --list-hosts
```

👉 Explication : affiche l'arbre des groupes, les variables d'un hôte, puis les hôtes ciblés par `web`, **sans se connecter à aucun serveur**. Vérifiez toujours le périmètre ainsi avant d'agir.

```bash
ansible -i inventory.yml web -m ansible.builtin.ping
```

👉 Explication : teste la connexion SSH et la présence de Python sur les cibles du groupe `web` ; ce n'est pas un ping réseau. À lancer vers le laboratoire uniquement.

## 6. Un premier playbook

Fichier `site.yml` :

```yaml
---
- name: Synchronisation horaire des serveurs web
  hosts: web
  become: true
  vars:
    chrony_conf: /etc/chrony/chrony.conf
    chrony_service: chrony
    serveurs_ntp:
      - 192.0.2.1
      - 198.51.100.1
  tasks:
    - name: Installer chrony
      ansible.builtin.package:
        name: chrony
        state: present

    - name: Déposer la configuration
      ansible.builtin.template:
        src: chrony.conf.j2
        dest: "{{ chrony_conf }}"
        owner: root
        group: root
        mode: "0644"
      notify: Redémarrer chrony

    - name: Activer et démarrer le service
      ansible.builtin.service:
        name: "{{ chrony_service }}"
        state: started
        enabled: true

  handlers:
    - name: Redémarrer chrony
      ansible.builtin.service:
        name: "{{ chrony_service }}"
        state: restarted
```

👉 Explication : le *play* cible le groupe `web` en élévation de privilèges (`become`). Trois tâches **déclarent un état** : paquet présent, fichier de configuration conforme, service démarré et activé au boot. Le *handler* ne redémarre le service **que si** le fichier a réellement changé (`notify`). Les noms de fichiers et de services sont des variables, car ils diffèrent selon les distributions.

Modèle `templates/chrony.conf.j2` :

```text
# Fichier géré par Ansible : ne pas modifier à la main
{% for serveur in serveurs_ntp %}
server {{ serveur }} iburst
{% endfor %}
makestep 1.0 3
```

👉 Explication : un modèle Jinja2 qui produit une ligne `server …` par adresse de la variable.

### 6.1 Valider avant d'appliquer

```bash
ansible-playbook -i inventory.yml site.yml --syntax-check
ansible-playbook -i inventory.yml site.yml --list-tasks
ansible-playbook -i inventory.yml site.yml --limit lab01 --check --diff
```

👉 Explication : la première commande vérifie la syntaxe sans contacter les hôtes ; la deuxième liste les tâches ; la troisième **simule** sur un seul hôte (`--limit lab01`) en affichant les différences de fichiers. Le mode `--check` ne prévoit pas tout (certaines tâches, comme `command`, ne sont pas simulables) : il réduit le risque mais ne remplace pas un essai en laboratoire.

### 6.2 Appliquer progressivement

```bash
ansible-playbook -i inventory.yml site.yml --limit lab01
ansible-playbook -i inventory.yml site.yml --limit lab01
ansible-playbook -i inventory.yml site.yml
```

👉 Explication : applique d'abord à un hôte pilote, relance pour constater que rien ne change (idempotence), puis étend au groupe entier.

## 7. L'idempotence

Un playbook est **idempotent** quand l'exécuter une, deux ou dix fois mène au même état final, et que les passages suivants ne modifient rien.

![Idempotence : changed au premier passage puis ok aux passages suivants, avec check et diff](images/git-ansible-4.svg)

*Figure 4 — Au premier passage Ansible modifie (`changed`), ensuite il constate (`ok`). Création originale du projet Pack Master (CC0).*

Au second passage, `changed=0` dans le récapitulatif est le signe attendu (les autres compteurs : `ok`, `failed`, `unreachable`, `skipped`).

**Les pièges** : les modules `command` et `shell` exécutent une commande à chaque fois et déclarent toujours `changed`, sauf indication contraire :

```yaml
- name: Initialiser la base une seule fois
  ansible.builtin.command: /usr/local/bin/init-base --force
  args:
    creates: /var/lib/appli/.initialisee
```

👉 Explication : le paramètre `creates` dit à Ansible de **ne pas exécuter** la commande si le fichier existe déjà, rendant la tâche idempotente. On peut aussi utiliser `changed_when` pour décrire quand un changement a réellement eu lieu. Avant d'utiliser `command` ou `shell`, cherchez un module dédié (`package`, `user`, `file`, `lineinfile`, `service`…) : il gère l'état à votre place.

Autres règles : décrire l'état final, éviter dates et valeurs aléatoires dans les fichiers produits, **nommer toutes les tâches**.

## 8. Versionner son code Ansible avec Git

Arborescence recommandée du dépôt :

```text
infra-lab/
├── .gitignore
├── ansible.cfg
├── inventory.yml
├── site.yml
├── group_vars/
│   └── all/
│       ├── vars.yml
│       └── vault.yml      (chiffré par Ansible Vault)
├── templates/
│   └── chrony.conf.j2
└── readme.md
```

👉 Explication : tout ce qui décrit l'infrastructure est dans Git, y compris le fichier **chiffré** ; jamais le mot de passe du coffre, les clés privées ni les journaux.

Flux de travail type pour une modification :

```bash
git switch -c chrony-nouveau-serveur
# modifier site.yml ou group_vars
ansible-playbook -i inventory.yml site.yml --syntax-check
ansible-playbook -i inventory.yml site.yml --limit lab01 --check --diff
git add site.yml group_vars/all/vars.yml
git commit -m "Ajoute le serveur NTP 198.51.100.2 au groupe web"
git switch main && git merge chrony-nouveau-serveur
ansible-playbook -i inventory.yml site.yml --limit lab01
```

👉 Explication : branche, modification, validations, commit **ciblé** (on ajoute les fichiers nommément plutôt que `git add .`, pour ne pas embarquer un fichier non voulu), fusion et application sur l'hôte pilote.

## 9. Ansible Vault : protéger les données sensibles (principe)

**Ansible Vault** chiffre des fichiers (ou des valeurs) afin de pouvoir les stocker dans Git sans exposer leur contenu. Le dépôt contient le fichier chiffré ; le **mot de passe du coffre** reste hors du dépôt.

```bash
ansible-vault create group_vars/all/vault.yml
ansible-vault view group_vars/all/vault.yml
ansible-vault edit group_vars/all/vault.yml
```

👉 Explication : crée un fichier chiffré (le mot de passe du coffre est demandé, puis l'éditeur s'ouvre), le lit ou le modifie. Un fichier chiffré commence par un en-tête `$ANSIBLE_VAULT;1.1;AES256`.

Convention : variables préfixées `vault_` dans le fichier chiffré, référencées depuis `vars.yml` (en clair).

```yaml
# group_vars/all/vars.yml (en clair, versionné)
db_password: "{{ vault_db_password }}"
```

👉 Explication : le nom de la variable reste visible et relisible, sa valeur reste dans le coffre. Pour l'exécution :

```bash
ansible-playbook -i inventory.yml site.yml --ask-vault-pass
ansible-playbook -i inventory.yml site.yml --vault-password-file ~/.config/infra-lab/vault_pass
```

👉 Explication : la première commande demande le mot de passe au clavier ; la seconde le lit dans un fichier **situé hors du dépôt**, protégé par des droits stricts (`chmod 600`). Ce fichier est aussi listé dans `.gitignore` par sécurité.

Précautions :
- `no_log: true` sur les tâches qui manipulent un secret, pour qu'il n'apparaisse pas dans la sortie ;
- partage du mot de passe du coffre par un canal sûr, et changement (`ansible-vault rekey`) au départ d'un collaborateur ;
- Vault protège un fichier **au repos**, pas un secret affiché dans un journal.

## Mise en pratique guidée

**Contexte.** Nœud de contrôle (VM Linux) et deux cibles de test (192.0.2.11 et 192.0.2.12) avec SSH par clé, un compte `automation` et `sudo`. Instantanés pris.

1. **Dépôt et .gitignore.**
   ```bash
   git init -b main ~/infra-lab && cd ~/infra-lab
   printf '.vault_pass*\n*.retry\n*.log\n.env\n' > .gitignore
   git add .gitignore && git commit -m "Initialise le dépôt et le .gitignore"
   ```
   👉 Explication : premier commit avec les règles d'exclusion.

2. **Inventaire et vérification du périmètre.** Créez `inventory.yml` (section 5) puis :
   ```bash
   ansible-inventory -i inventory.yml --graph
   ansible -i inventory.yml web --list-hosts
   ```
   👉 Explication : vérifie le périmètre sans aucune connexion.

3. **Connexion de test.**
   ```bash
   ansible -i inventory.yml web -m ansible.builtin.ping
   ```
   👉 Explication : attendez `SUCCESS` et `pong` pour chaque hôte ; sinon corrigez SSH (clé, utilisateur, adresse) avant de continuer.

4. **Playbook, simulation, application.** Créez `site.yml` et `templates/chrony.conf.j2` (section 6), validez, puis :
   ```bash
   ansible-playbook -i inventory.yml site.yml --syntax-check
   ansible-playbook -i inventory.yml site.yml --limit lab01 --check --diff
   ansible-playbook -i inventory.yml site.yml --limit lab01
   ansible-playbook -i inventory.yml site.yml --limit lab01
   ```
   👉 Explication : le premier passage indique `changed`, le second doit indiquer `changed=0`. Si ce n'est pas le cas, une tâche n'est pas idempotente : trouvez laquelle.

5. **Commit** des fichiers nommés (`git add inventory.yml site.yml templates/chrony.conf.j2`, puis `git commit` et `git status`).

6. **Vault.** Créez `group_vars/all/vault.yml` avec une variable factice, vérifiez qu'il est illisible avec `cat`, lisible avec `ansible-vault view`, puis ajoutez-le au commit. Contrôlez que `.vault_pass` est bien ignoré :
   ```bash
   git check-ignore -v .vault_pass
   ```
   👉 Explication : confirme que le fichier de mot de passe ne sera jamais ajouté.

7. **Retour arrière.** Modifiez `site.yml`, committez, puis exécutez `git revert HEAD` : un nouveau commit annule le précédent sans réécrire l'historique. Réappliquez le playbook.

8. **Nettoyage.** Restaurez les instantanés des VM de test.

## Exercices

1. **(facile)** Créez un dépôt, ajoutez un fichier `notes.txt`, faites deux commits et affichez l'historique en une ligne par commit.
2. **(facile)** Écrivez un `.gitignore` qui exclut les fichiers `.env`, les clés `.pem` et le dossier `secrets/`, puis prouvez qu'il fonctionne.
3. **(moyen)** Créez une branche `essai`, modifiez un fichier, fusionnez dans `main`, puis supprimez la branche.
4. **(moyen)** Un fichier `config.ini` contenant un mot de passe a été commité hier et poussé. Décrivez, dans l'ordre, ce que vous faites.
5. **(moyen)** Écrivez un inventaire YAML avec deux groupes et une variable de groupe, puis la commande qui liste les hôtes du second groupe.
6. **(moyen)** Écrivez une tâche qui garantit que le paquet `tree` est présent, et la commande qui la simule sur `lab02` avec différences.
7. **(avancé)** Une tâche `command` ajoute une ligne à un fichier à chaque exécution. Corrigez-la pour qu'elle soit idempotente de deux façons différentes.
8. **(avancé)** Décrivez comment stocker un mot de passe de base de données pour un playbook versionné, avec Ansible Vault, sans jamais l'exposer dans Git ni dans la sortie.

## Corrigés des exercices

1. ```bash
   git init -b main ~/exo1 && cd ~/exo1
   echo "première ligne" > notes.txt && git add notes.txt && git commit -m "Crée notes.txt"
   echo "deuxième ligne" >> notes.txt && git commit -am "Complète notes.txt"
   git log --oneline
   ```
   👉 Explication : `commit -am` valide les fichiers **déjà suivis** (pas les nouveaux).

2. ```bash
   printf '.env\n*.pem\nsecrets/\n' > .gitignore
   touch .env cle.pem && mkdir -p secrets && touch secrets/a.txt
   git status --short
   git check-ignore -v .env cle.pem secrets/a.txt
   ```
   👉 Explication : `git status` ne montre que `.gitignore` ; `check-ignore -v` indique la règle appliquée.

3. ```bash
   git switch -c essai
   echo "test" >> notes.txt && git commit -am "Essai"
   git switch main && git merge essai && git branch -d essai
   ```
   👉 Explication : la fusion est ici « en avance rapide » (*fast-forward*) car `main` n'a pas bougé.

4. Réponse : (1) considérer le mot de passe comme compromis et le **changer immédiatement** ; (2) prévenir le responsable sécurité ; (3) `git rm --cached config.ini`, règle `.gitignore`, fichier `config.ini.example` sans valeur réelle ; (4) nettoyer l'historique avec un outil adapté et faire recloner l'équipe ; (5) examiner les journaux d'accès.
   👉 Explication : changer le secret passe **avant** le nettoyage.

5. ```yaml
   all:
     children:
       web:
         hosts:
           lab01: {}
       bdd:
         hosts:
           lab03: {}
         vars:
           port_bdd: 5432
   ```
   👉 Explication : deux groupes, la variable `port_bdd` appartient au groupe `bdd`.
   ```bash
   ansible -i inventory.yml bdd --list-hosts
   ```
   👉 Explication : liste les hôtes du groupe sans se connecter.

6. ```yaml
   - name: S'assurer que tree est présent
     ansible.builtin.package:
       name: tree
       state: present
   ```
   👉 Explication : `state: present` décrit l'état souhaité, pas un geste.
   ```bash
   ansible-playbook -i inventory.yml site.yml --limit lab02 --check --diff
   ```
   👉 Explication : simule sur le seul hôte `lab02`, avec différences.

7. Solution A : `ansible.builtin.lineinfile` avec `path`, `line` et `state: present` (le module n'ajoute la ligne que si elle manque). Solution B : conserver `command` ou `shell` mais ajouter `args: creates:` ou une tâche préalable de vérification avec `changed_when: false` et `when:`.
   👉 Explication : un module d'état est préférable ; `creates` et `when` servent quand une commande est indispensable.

8. Réponse : créer `group_vars/all/vault.yml` avec `ansible-vault create`, y mettre `vault_db_password`, référencer cette variable depuis un fichier clair, mettre `no_log: true` sur les tâches concernées, garder le mot de passe du coffre hors du dépôt (`.gitignore` + droits `600`) et l'injecter par `--ask-vault-pass` ou `--vault-password-file`.
   👉 Explication : le dépôt n'héberge que du texte chiffré.

## Quiz

**1. Que fait `git add` ?**
a) Il envoie au dépôt distant ; b) il place les modifications dans l'index pour le prochain commit ; c) il supprime des fichiers ; d) il crée une branche.
**Réponse : b.** L'index est la zone de préparation ; l'enregistrement se fait avec `git commit`.

**2. Un fichier `.env` est déjà suivi par Git. L'ajouter ensuite à `.gitignore` suffit-il à l'exclure ?**
a) Oui, toujours ; b) non, il faut aussi le retirer du suivi (`git rm --cached`) ; c) oui, après un `git pull` ; d) non, `.gitignore` n'existe pas.
**Réponse : b.** `.gitignore` n'agit que sur les fichiers non suivis ; l'historique garde en outre l'ancienne version.

**3. Premier réflexe après le commit d'un mot de passe poussé ?**
a) Supprimer le fichier et continuer ; b) révoquer et remplacer le mot de passe ; c) renommer la branche ; d) ne rien faire si le dépôt est privé.
**Réponse : b.** Le secret est présent dans l'historique et les copies ; il doit être considéré comme compromis.

**4. Pourquoi Ansible est-il dit « sans agent » ?**
a) Il ne nécessite aucun serveur ; b) il utilise SSH et n'installe pas de démon permanent sur les cibles ; c) il ne marche qu'en local ; d) il n'a pas de modules.
**Réponse : b.** Le contrôleur se connecte aux cibles et exécute des modules temporaires.

**5. Que signifie `changed=0` au deuxième passage d'un playbook ?**
a) Les hôtes sont injoignables ; b) rien n'a eu besoin d'être modifié : idempotence ; c) le playbook est vide ; d) une erreur silencieuse.
**Réponse : b.** L'état souhaité était déjà atteint.

**6. Que fait `--check --diff` ?**
a) Applique puis annule ; b) simule et affiche les différences prévues ; c) vérifie seulement la syntaxe ; d) chiffre les fichiers.
**Réponse : b.** C'est une simulation avec comparaison, mais elle n'est pas fiable à 100 % pour `command`/`shell`.

**7. Quel module est préférable à `shell: apt install tree` ?**
a) `ansible.builtin.package` avec `state: present` ; b) `ansible.builtin.debug` ; c) `ansible.builtin.ping` ; d) aucun.
**Réponse : a.** Le module gère l'état (déjà installé ou non) et rend la tâche idempotente.

**8. Où doit se trouver le mot de passe du coffre Ansible Vault ?**
a) Dans `vars.yml` ; b) dans le dépôt, dans un fichier `.vault_pass` ; c) hors du dépôt, avec des droits restreints ou saisi à l'exécution ; d) dans le message de commit.
**Réponse : c.** Le dépôt ne doit contenir que le contenu chiffré.

**9. Quel est le rôle d'un handler ?**
a) Faire un test de connexion ; b) s'exécuter seulement si une tâche notificatrice a changé quelque chose ; c) gérer les erreurs SSH ; d) définir l'inventaire.
**Réponse : b.** Typiquement : redémarrer un service uniquement si sa configuration a été modifiée.

**10. Pourquoi utiliser `--limit` lors de la première application ?**
a) Pour accélérer le réseau ; b) pour restreindre à un hôte pilote et limiter l'impact d'une erreur ; c) pour contourner SSH ; d) pour désactiver l'idempotence.
**Réponse : b.** On valide sur un hôte avant d'étendre au groupe.

## Erreurs fréquentes et dépannage

| Symptôme | Cause probable | Remède |
|---|---|---|
| `Permission denied (publickey)` | Clé absente, mauvais utilisateur | Vérifier `ansible_user`, la clé, l'agent SSH, les droits sur `~/.ssh` |
| `UNREACHABLE` | Pare-feu, mauvaise adresse, hôte éteint | Tester `ssh automation@192.0.2.11`, contrôler l'inventaire |
| `changed` à chaque passage | Tâche `command`/`shell` ou modèle variable | Utiliser un module d'état, `creates`, `changed_when` |
| `Decryption failed` | Mauvais mot de passe du coffre | Fournir le bon mot de passe ; vérifier l'identifiant de coffre |
| Fusion en conflit | Même ligne modifiée deux fois | Éditer les marqueurs `<<<<<<<`, `git add`, `git commit` |

## À retenir

- Git versionne le texte : un commit par intention, des messages utiles, des branches pour isoler et fusionner.
- **Un secret ne se versionne jamais** ; s'il fuit, on le révoque d'abord.
- `.gitignore` empêche l'ajout futur, ne répare pas le passé.
- Ansible : inventaire + playbook + modules, par SSH, sans agent.
- Écrire l'**état souhaité** rend un playbook **idempotent** ; préférer les modules aux commandes brutes.
- Avant d'appliquer : `--syntax-check`, `--list-hosts`, `--check --diff`, `--limit`.
- Ansible Vault chiffre les données sensibles ; le mot de passe du coffre reste hors du dépôt ; `no_log: true` évite les fuites à l'affichage.
- Flux sain : branche → validation → hôte pilote → fusion → déploiement général.

## Pour aller plus loin

- Documentation de Git : <https://git-scm.com/docs>
- Documentation d'Ansible : <https://docs.ansible.com/ansible/latest/>
- Mode check et diff : <https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_checkmode.html>
- Ansible Vault : <https://docs.ansible.com/ansible/latest/vault_guide/index.html>
- Adresses réservées à la documentation (RFC 5737) : <https://www.rfc-editor.org/rfc/rfc5737>

## Crédits des images

Aucune image libre adaptée n'a été retenue (logos de Git et d'Ansible exclus car marques déposées) : les quatre schémas ont été dessinés pour cette leçon.

| Fichier | Source (URL de la page) | Auteur | Licence | Modifications |
|---|---|---|---|---|
| `images/git-ansible-1.svg` | Création originale du projet Pack Master | Projet Pack Master | CC0 1.0, dédiée au domaine public — <https://creativecommons.org/publicdomain/zero/1.0/deed.fr> | Aucune |
| `images/git-ansible-2.svg` | Création originale du projet Pack Master | Projet Pack Master | CC0 1.0 — <https://creativecommons.org/publicdomain/zero/1.0/deed.fr> | Aucune |
| `images/git-ansible-3.svg` | Création originale du projet Pack Master | Projet Pack Master | CC0 1.0 — <https://creativecommons.org/publicdomain/zero/1.0/deed.fr> | Aucune |
| `images/git-ansible-4.svg` | Création originale du projet Pack Master | Projet Pack Master | CC0 1.0 — <https://creativecommons.org/publicdomain/zero/1.0/deed.fr> | Aucune |

Création originale du projet Pack Master, dédiée au domaine public (CC0).

## Historique de vérification

| Date | OS/logiciel | Testeur | Verdict |
|---|---|---|---|
| 2026-11-01 | Linux (Debian/Ubuntu) / Git / ansible-core | Rédaction assistée (agent Copilot) — relecture statique ; seule la commande `git --version` a été exécutée (lecture seule) | Non testé sur plateforme cible |