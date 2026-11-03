# pack-master — CLI « tout-en-un »

Outil en bibliothèque standard Python (3.9+), sans dépendance tierce. Il détecte la racine du pack
(dossier contenant `00-administration/03-qualite-tests/verify-wiki.py`) et **invoque** les scripts existants de
`00-administration/` par sous-processus, sans les copier ni les déplacer.

```bash
python3 tools/pack-master/pack-master.py <commande> [options]
```

| Commande | Action |
|---|---|
| `check` | Vérifie les fiches source avec `verify-wiki.py` et les liens Markdown avec `check-links.py`. Ne crée aucun export. |
| `refresh` | Génère les arbres d'import Wiki.js optionnels avec `prepare-wikijs-import.py`. Écrit dans `export/`; ne pas lancer si Wiki.js synchronise directement le dépôt GitHub. |
| `sources` | Liste les URL du manifeste ; avec `--test`, les interroge en HTTPS. |
| `all` | `check` puis test des sources publiques. Aucun export n'est généré. |

Options de `sources`/`all` : `--manifest FICHIER` (défaut `sources.json`), `--timeout S` (10),
`--max-bytes N` (1 048 576), `--method HEAD|GET` (HEAD), `--only ID` (répétable).
Code retour non nul si une source répond ≥ 400 ou échoue.

## Garanties de `sources`

- Uniquement HTTPS `GET`/`HEAD` ; HTTP et redirections hors HTTPS refusés ; certificat et nom d'hôte vérifiés.
- Timeout et taille bornés ; le corps (GET) est lu par blocs, compté puis jeté : **rien n'est stocké**,
  aucun texte n'est affiché, aucune ingestion ni reproduction de contenu.
- Aucune donnée privée, cookie, jeton ou secret envoyé (seul un `User-Agent` générique).
- Sortie : status, URL finale, type de contenu, longueur.
- Les URL du manifeste sont validées : HTTPS, sans identifiants, requête ni fragment.

## Utilisation directe avec GitHub

Quand Wiki.js synchronise la branche GitHub, les dossiers source (`01-fiches-simples`,
`02-fiches-completes`, etc.) sont la source de vérité. Aucun dossier `export/` n'est nécessaire.
Utiliser `check` avant de pousser ; ne lancer `refresh` que pour un besoin explicite d'import
manuel ou d'arbre intermédiaire.

## Manifeste `sources.json`

```json
{"version": 1, "sources": [{"id": "zentssr", "name": "ZenTSSR", "url": "https://zentssr.com/"}]}
```

Sources d'origine (`idee-incorporer-en-attente/reorganisation-fichier`) : GitHub kipit/nivvlem-tssr,
zentssr.com, stephane-robert.info, jousseaume.online. Ce sont des références à vérifier ; toute
intégration de leur contenu doit rester manuelle et respecter leurs licences.

## Tests

```bash
python3 -m unittest discover -s tools/pack-master/tests -v
```

Les tests utilisent un serveur HTTP local (loopback, via un paramètre interne non exposé au CLI) et des mocks.
