# Preparer le pack pour Wiki.js

Le dossier `WikiJS-Import-v2` est une copie de travail preparee pour l'import par le stockage Git de Wiki.js 2.x. Les fichiers sources restent inchanges.

## Generer et controler l'arbre

Depuis la racine du pack :

```bash
python3 00-Administration/prepare_wikijs_import.py --dry-run
python3 00-Administration/prepare_wikijs_import.py
python3 00-Administration/prepare_wikijs_import.py --check
```

Le generateur transforme les fiches Markdown, y compris celles sans extension, en pages `.md` avec metadonnees Wiki.js (`title`, `description`, `published`, dates, `tags` et `editor`). Il normalise les chemins en minuscules ASCII, convertit les liens Markdown relatifs vers les pages incluses en routes Wiki.js, ajoute une page d'accueil et des index de rubrique, et refuse les routes en doublon. Les tags existants sont repris; l'absence de tags ne bloque pas la page.

Apres une modification des sources, simuler puis actualiser explicitement la sortie existante :

```bash
python3 00-Administration/prepare_wikijs_import.py --dry-run
python3 00-Administration/prepare_wikijs_import.py --refresh
python3 00-Administration/prepare_wikijs_import.py --check
```

Avec `--refresh`, les pages Markdown devenues obsolètes sont retirees de l'arbre genere; les fichiers non Markdown sont conserves.

Les dossiers `.git`, fichiers de configuration de navigation externes, scripts et exports non Markdown ne sont pas importes. Les pages du depot externe conservees sous `06-Documentation-ext/Github` sont copiees comme contenu, mais leurs donnees Git internes sont exclues.

## Copier-coller dans l'editeur Wiki.js

Si les pages sont creees une par une dans l'editeur Wiki.js, generer la variante sans front matter :

```bash
python3 00-Administration/prepare_wikijs_import.py --manual --dry-run
python3 00-Administration/prepare_wikijs_import.py --manual
python3 00-Administration/prepare_wikijs_import.py --manual --check
```

Ouvrir le fichier `.md` correspondant dans `WikiJS-Copier-Coller`, creer la page avec le chemin du fichier relatif a ce dossier (sans `.md`), puis coller le contenu du fichier dans l'editeur Markdown. Les chemins imbriques creent les rubriques, par exemple `01-fiches-simples/cloud-saas/fiche-simple-jira-service-management-creer-portail-itsm`. Reporter le titre et les tags depuis `IMPORT-MANIFEST.csv` dans les champs de la page. Cette variante ne contient pas de bloc YAML `---`.

Apres une modification des sources, actualiser la sortie manuelle avec :

```bash
python3 00-Administration/prepare_wikijs_import.py --manual --refresh
python3 00-Administration/prepare_wikijs_import.py --manual --check
```

## Importer avec le stockage Git

1. Utiliser un depot Git dedie au contenu Wiki.js; ne pas configurer le depot global du pack comme depot de stockage.
2. Copier le contenu de `WikiJS-Import-v2` a la racine de ce depot et le pousser sur le serveur Git cible.
3. Dans Wiki.js, configurer le module **Storage > Git** avec ce depot et verifier que son statut est sain.
4. Apres sauvegarde du wiki et verification du depot, lancer **Import Everything** depuis les actions du module Git.
5. Verifier l'accueil, les rubriques, quelques fiches avec accents et les tags dans Wiki.js avant d'activer la synchronisation habituelle.

Le generateur prepare les fichiers; il ne pousse pas de depot, ne connait pas l'URL de votre Wiki.js et ne declenche pas d'import distant. Les IDs internes des pages sont attribues par Wiki.js; ils ne doivent pas etre fabriques dans les fichiers Markdown.