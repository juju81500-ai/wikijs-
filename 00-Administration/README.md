# 00-Administration — index

Ce dossier regroupe la gouvernance, l'exploitation Wiki.js, les contrôles qualité et les référentiels du pack. Les fiches simples (`01-Fiches-Simples/`) et les fiches complètes (`02-Fiches-Completes/`) ne sont pas concernées par cette réorganisation ; leurs chemins restent inchangés.

## Arborescence

| Dossier | Rôle | Contenu |
|---|---|---|
| [01-Gouvernance-Architecture/](<01-Gouvernance-Architecture/>) | Gouvernance et architecture | [Actions par phase](<01-Gouvernance-Architecture/Actions_par_phase.md>), [Cycle de vie en 50 étapes](<01-Gouvernance-Architecture/Cycle_de_vie_50_etapes.md>), [Vie du système](<01-Gouvernance-Architecture/Vie_du_systeme.md>), [Arborescence Debian et RedHat](<01-Gouvernance-Architecture/Arborescence_Mise_a_Jour_-_Familles_Debian_et_RedHat.md>), [Parcours installation à production](<01-Gouvernance-Architecture/Parcours_Installation_Production_Couverture_Fiches_Simples.md>) |
| [02-Operations-WikiJS/](<02-Operations-WikiJS/>) | Opérations Wiki.js | [Import SSH Docker](<02-Operations-WikiJS/Guide_Import_WikiJS_2.5.317_Par_SSH_Docker.md>), [Intégration Git](<02-Operations-WikiJS/Integration_WikiJS_Git.md>), [Réinitialisation](<02-Operations-WikiJS/Reinitialiser_WikiJS_Docker_Et_Stockage_Local.md>), [Gestion des IDs](<02-Operations-WikiJS/Gestion_IDs_Import.md>), [Règles d'automatisation](<02-Operations-WikiJS/Script_et_Regles_d_Automatisation_Wiki.js>), scripts `prepare_wikijs_import.py` et `verify_command_import.py` |
| [03-Qualite-Tests/](<03-Qualite-Tests/>) | Qualité et tests | [Liste de contrôle des tests](<03-Qualite-Tests/Liste_Controle_Tests_Fiches_Simples.md>), [Rapport de test statique](<03-Qualite-Tests/Rapport_Test_Statique_Fiches.md>), [Rapport réel Debian 12](<03-Qualite-Tests/Rapport_Test_Reel_Debian_12_Laboratoire.md>), [Matrice de contrôle fiches complètes et Q/R](<03-Qualite-Tests/Matrice_Controle_Fiches_Completes_et_Questions_Reponses.md>), scripts `verify_wiki.py` et `check_links.py` |
| [04-Referentiels-Mapping/](<04-Referentiels-Mapping/>) | Référentiels et mappings | [Matrice de contrôle des fiches simples (46 tâches)](<04-Referentiels-Mapping/Matrice_de_Controle_des_Fiches_Simples_par_OS_(Mise_a_jour_46_T.md>), [Couverture logiciels](<04-Referentiels-Mapping/Matrice_Couverture_Logiciels_Production_TSSR_AIS.md>), [Catalogue des fiches](<04-Referentiels-Mapping/Catalogue_Propositions_Fiches_Simples_par_OS.md>), [Compatibilité des versions](<04-Referentiels-Mapping/Compatibilite_Versions_OS_Paquets_Base.md>), [mapping/](<04-Referentiels-Mapping/mapping/>), données `TXT.txt` (command blocks) |
| [90-Archives/](<90-Archives/README.md>) | Archives | Documents remplacés ou obsolètes, conservés tels quels ; voir l'[index des archives](<90-Archives/README.md>) |

## Scripts et rétrocompatibilité

Les scripts actifs sont dans les dossiers `02-` et `03-`. Des wrappers aux anciens chemins (`00-Administration/prepare_wikijs_import.py`, `verify_command_import.py`, `verify_wiki.py`) délèguent aux scripts actifs : les anciennes commandes continuent de fonctionner.

```bash
python3 00-Administration/03-Qualite-Tests/verify_wiki.py .
python3 00-Administration/02-Operations-WikiJS/prepare_wikijs_import.py --check
python3 00-Administration/02-Operations-WikiJS/prepare_wikijs_import.py --manual --check
python3 00-Administration/03-Qualite-Tests/check_links.py .
```

L'outil [`pack_master.py`](../tools/pack_master/README.md) contrôle les fiches et liens puis vérifie, sur demande, les sources publiques. Wiki.js synchronisant directement le dépôt Git, la commande `check` ne produit aucun export. `refresh` reste disponible uniquement pour générer un arbre d'import manuel optionnel.

Les arbres `export/` sont facultatifs et ne sont pas suivis dans ce flux. Après une modification documentaire, lancer `python3 tools/pack_master/pack_master.py check`.

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
1. Relire les documents des dossiers `01-` à `04-` ; archiver dans `90-Archives/` ceux remplacés (ajouter une ligne à l'[index des archives](<90-Archives/README.md>) : origine, remplaçant, raison).
2. Vérifier la fraîcheur des versions d'OS dans la [compatibilité des versions](<04-Referentiels-Mapping/Compatibilite_Versions_OS_Paquets_Base.md>) et la matrice de contrôle.
3. Vérifier que la racine du dossier ne contient que `README.md` et les wrappers.
4. Relancer `python3 tools/pack_master/pack_master.py check` après tout changement documentaire ; Wiki.js récupère les sources depuis Git.
