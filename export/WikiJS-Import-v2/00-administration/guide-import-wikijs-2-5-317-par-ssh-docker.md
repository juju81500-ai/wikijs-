---
title: "Importer des fiches dans Wiki.js 2.5.317 avec SSH et Docker"
description: "Le module SFTP de Wiki.js est une cible de stockage pour conserver une copie des pages; deposer des fichiers par SFTP ne les cree pas automatiquement dans la base Wiki.js. Pour importer un depot de Markdown, utiliser le module Git avec une URI SSH et l'action Import Everything."
published: true
date: 2026-10-28T18:59:31Z
tags: ["wikijs", "docker", "git", "ssh", "import", "markdown"]
editor: markdown
dateCreated: 2026-10-28T18:59:31Z
dateModified: 2026-10-28T18:59:31Z
---

# Importer des fiches dans Wiki.js 2.5.317 avec SSH et Docker

- **Objectif** : importer les fiches du pack dans Wiki.js sans les coller une par une
- **Environnement** : Wiki.js 2.5.317 dans Docker Compose
- **Methode** : stockage Git de Wiki.js, connexion SSH
- **Corpus** : dossier `WikiJS-Import-v2`
- **Tags** : `wikijs`, `docker`, `git`, `ssh`, `import`, `markdown`

## Choisir le bon transfert

Le module **SFTP** de Wiki.js est une cible de stockage pour conserver une copie des pages; deposer des fichiers par SFTP ne les cree pas automatiquement dans la base Wiki.js. Pour importer un depot de Markdown, utiliser le module **Git** avec une URI SSH et l'action **Import Everything**.

Le volume Docker `wiki_data:/wiki/data` contient les donnees persistantes de l'application. Ne pas le remplacer par le corpus de fiches. Le depot de contenu Wiki.js est distinct de ce volume.

## 1. Controler le corpus

Depuis la racine du pack :

```bash
python3 00-Administration/prepare_wikijs_import.py --dry-run
python3 00-Administration/prepare_wikijs_import.py --check
```

Le dossier `WikiJS-Import-v2` contient les pages Markdown et leurs metadonnees Wiki.js. Le controle actuel porte sur 650 pages, dont les index de rubriques et la page d'accueil.

## 2. Creer le depot de contenu

Creer un depot Git prive, vide et dedie au contenu du wiki. Depuis le terminal, a la racine du pack :

```bash
cd WikiJS-Import-v2
git init
git add .
git commit -m "Import initial du pack Wiki.js"
git branch -M main
git remote add origin git@github.com:ORGANISATION/DEPOT-WIKI.git
git push -u origin main
```

Remplacer l'URI d'exemple par l'URI SSH du depot chez le fournisseur choisi. Le depot doit contenir directement les dossiers `01-fiches-simples`, `02-fiches-completes`, etc.; ne pas y placer un second dossier `WikiJS-Import-v2`.

Le premier `git push` utilise l'identite SSH deja configuree sur ton poste. La cle de l'etape suivante est une cle distincte, dediee au conteneur Wiki.js; ne copie jamais la cle privee personnelle de ton poste dans le conteneur.

## 3. Creer une cle dediee a Wiki.js

Sur l'hote Docker, creer une cle de deploiement specifique. La cle privee ne doit pas etre ajoutee au depot.

```bash
sudo install -d -m 0700 /opt/docker/wikijs/secrets
sudo ssh-keygen -t rsa -b 4096 -N "" -f /opt/docker/wikijs/secrets/wikijs_git
sudo chmod 0444 /opt/docker/wikijs/secrets/wikijs_git
sudo cat /opt/docker/wikijs/secrets/wikijs_git.pub
```

Enregistrer le contenu de la cle publique comme **Deploy key** du depot. L'autorisation d'ecriture est necessaire si Wiki.js doit aussi publier ses changements. Garder le dossier parent accessible uniquement a root.

## 4. Monter la cle en lecture seule

Dans le service `wiki` de `docker-compose.yml`, conserver le volume de donnees et ajouter le montage de la cle :

```yaml
services:
  wiki:
    volumes:
      - wiki_data:/wiki/data
      - ./secrets/wikijs_git:/run/secrets/wikijs_git:ro
```

Appliquer la modification puis verifier que le conteneur peut lire la cle :

```bash
cd /opt/docker/wikijs
sudo docker compose up -d wiki
sudo docker compose exec wiki test -r /run/secrets/wikijs_git
```

La derniere commande doit se terminer sans erreur. En cas d'echec, corriger le chemin ou les permissions avant de continuer.

## 5. Configurer le stockage Git

Dans l'administration Wiki.js, ouvrir **Storage**, activer **Git**, puis renseigner :

| Parametre | Valeur |
|---|---|
| Authentication Type | `ssh` |
| Repository URI | URI SSH du depot dedie |
| Branch | `main` |
| SSH Private Key Path | `/run/secrets/wikijs_git` |
| Username / Password | Vides pour SSH |
| Sync Direction | `Bi-directional` si Wiki.js doit publier les modifications |
| Verify SSL Certificate | Active |

Renseigner egalement le nom et l'adresse email de l'auteur des commits. Enregistrer avec **Apply Changes** et attendre que l'etat Git passe au vert.

## 6. Importer les pages

Faire une sauvegarde restaurable de la base Wiki.js. Si le wiki contient deja des pages, tester d'abord sur une instance de recette et verifier les collisions de chemins avant l'import.

Quand la connexion Git est au vert, ouvrir les actions du module Git et lancer **Import Everything**. Verifier ensuite la page d'accueil, les rubriques `01`, `03`, `04`, `05`, quelques fiches et les liens internes.

Ne pas utiliser **Add Untracked Changes** pour importer le depot : cette action exporte les pages de la base vers le stockage.

## Depannage


## References