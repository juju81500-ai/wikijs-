---
title: "00-administration — index"
description: "Ce dossier regroupe la gouvernance, l'exploitation Wiki.js, les contrôles qualité et les référentiels du pack. Les fiches simples (01-fiches-simples/) et les fiches complètes (02-fiches-completes/) ne sont pas concernées par cette réorganisation ; leurs chemins restent inchangés."
published: true
date: 2026-11-03T09:36:13Z
tags: []
editor: markdown
dateCreated: 2026-11-03T09:36:13Z
dateModified: 2026-11-03T09:36:13Z
---

# 00-administration — index

Ce dossier regroupe la gouvernance, l'exploitation Wiki.js, les contrôles qualité et les référentiels du pack. Les fiches simples (`01-fiches-simples/`) et les fiches complètes (`02-fiches-completes/`) ne sont pas concernées par cette réorganisation ; leurs chemins restent inchangés.

## Arborescence

| Dossier | Rôle | Contenu |
|---|---|---|
| [01-gouvernance-architecture/](01-gouvernance-architecture) | Gouvernance et architecture | [Actions par phase](/fr/00-administration/01-gouvernance-architecture/actions-par-phase), [Cycle de vie en 50 étapes](/fr/00-administration/01-gouvernance-architecture/cycle-de-vie-50-etapes), [Vie du système](/fr/00-administration/01-gouvernance-architecture/vie-du-systeme), [Arborescence Debian et RedHat](/fr/00-administration/01-gouvernance-architecture/arborescence-mise-a-jour-familles-debian-et-redhat), [Parcours installation à production](/fr/00-administration/01-gouvernance-architecture/parcours-installation-production-couverture-fiches-simples) |
| [02-operations-wikijs/](02-operations-wikijs) | Opérations Wiki.js | [Import SSH Docker](/fr/00-administration/02-operations-wikijs/guide-import-wikijs-2-5-317-par-ssh-docker), [Intégration Git](/fr/00-administration/02-operations-wikijs/integration-wikijs-git), [Réinitialisation](/fr/00-administration/02-operations-wikijs/reinitialiser-wikijs-docker-et-stockage-local), [Gestion des IDs](/fr/00-administration/02-operations-wikijs/gestion-ids-import), [Règles d'automatisation](/fr/00-administration/02-operations-wikijs/script-et-regles-d-automatisation-wiki-js), scripts `prepare-wikijs-import.py` et `verify-command-import.py` |
| [03-qualite-tests/](03-qualite-tests) | Qualité et tests | [Liste de contrôle des tests](/fr/00-administration/03-qualite-tests/liste-controle-tests-fiches-simples), [Rapport de test statique](/fr/00-administration/03-qualite-tests/rapport-test-statique-fiches), [Rapport réel Debian 12](/fr/00-administration/03-qualite-tests/rapport-test-reel-debian-12-laboratoire), [Matrice de contrôle fiches complètes et Q/R](/fr/00-administration/03-qualite-tests/matrice-controle-fiches-completes-et-questions-reponses), scripts `verify-wiki.py` et `check-links.py` |
| [04-referentiels-mapping/](04-referentiels-mapping) | Référentiels et mappings | [Matrice de contrôle des fiches simples (46 tâches)](/fr/00-administration/04-referentiels-mapping/matrice-de-controle-des-fiches-simples-par-os-mise-a-jour-46-t), [Couverture logiciels](/fr/00-administration/04-referentiels-mapping/matrice-couverture-logiciels-production-tssr-ais), [Catalogue des fiches](/fr/00-administration/04-referentiels-mapping/catalogue-propositions-fiches-simples-par-os), [Compatibilité des versions](/fr/00-administration/04-referentiels-mapping/compatibilite-versions-os-paquets-base), [mapping/](04-referentiels-mapping/mapping), données `txt.txt` (command blocks) |
| [90-archives/](/fr/00-administration/90-archives/readme) | Archives | Documents remplacés ou obsolètes, conservés tels quels ; voir l'[index des archives](/fr/00-administration/90-archives/readme) |

## Scripts et rétrocompatibilité

Les scripts actifs sont dans les dossiers `02-` et `03-`. Des wrappers aux anciens chemins (`00-administration/prepare-wikijs-import.py`, `verify-command-import.py`, `verify-wiki.py`) délèguent aux scripts actifs : les anciennes commandes continuent de fonctionner.

```bash
python3 00-administration/03-qualite-tests/verify-wiki.py .
python3 00-administration/02-operations-wikijs/prepare-wikijs-import.py --check
python3 00-administration/02-operations-wikijs/prepare-wikijs-import.py --manual --check
python3 00-administration/03-qualite-tests/check-links.py .
```

L'outil [`pack-master.py`](../tools/pack-master/readme.md) contrôle les fiches et liens puis vérifie, sur demande, les sources publiques. Wiki.js synchronisant directement le dépôt Git, la commande `check` ne produit aucun export. `refresh` reste disponible uniquement pour générer un arbre d'import manuel optionnel.

Les arbres `export/` sont facultatifs et ne sont pas suivis dans ce flux. Après une modification documentaire, lancer `python3 tools/pack-master/pack-master.py check`.

## Conventions de nommage

- Dossiers de ce répertoire : `NN-Nom-Par-Role`, préfixe numérique à deux chiffres, `90-` réservé aux archives.
- Documents : `Sujet_En_Snake_Case.md`, sans date ni numéro de version dans le nom ; la version vit dans le contenu. Un document remplacé est archivé, pas renommé.
- Scripts : `verbe_objet.py` en minuscules, avec une ligne de documentation en tête ; tout déplacement laisse un wrapper à l'ancien chemin.
- Mappings : fichiers CSV séparés par `;`, nommés `mapping_*` (référentiel vivant) ou `deplacements_vN_*` (historique d'un déplacement).
- Liens internes : chemins relatifs, entre chevrons `<...>` si le nom contient espaces ou parenthèses.
- Aucun secret, mot de passe ou clé dans ce dossier : ils restent sur le serveur de l'administrateur, accessibles aux seules personnes autorisées.

## Maintenance périodique

À chaque ajout ou déplacement :
1. Placer le document dans le dossier correspondant à son rôle ; mettre à jour le tableau ci-dessus.
2. Lancer les quatre contrôles de la section « Scripts » et corriger tout écart avant de valider.

Chaque trimestre :
1. Relire les documents des dossiers `01-` à `04-` ; archiver dans `90-archives/` ceux remplacés (ajouter une ligne à l'[index des archives](/fr/00-administration/90-archives/readme) : origine, remplaçant, raison).
2. Vérifier la fraîcheur des versions d'OS dans la [compatibilité des versions](/fr/00-administration/04-referentiels-mapping/compatibilite-versions-os-paquets-base) et la matrice de contrôle.
3. Vérifier que la racine du dossier ne contient que `readme.md` et les wrappers.
4. Relancer `python3 tools/pack-master/pack-master.py check` après tout changement documentaire ; Wiki.js récupère les sources depuis Git.