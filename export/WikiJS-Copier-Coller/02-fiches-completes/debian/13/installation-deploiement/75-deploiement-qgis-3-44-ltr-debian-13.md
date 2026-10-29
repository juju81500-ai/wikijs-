# Déployer QGIS 3.44 LTR sur Debian 13

- **OS / Version** : Debian 13 Trixie amd64; QGIS 3.44 LTR
- **Type de fiche** : Installation/Déploiement
- **Périmètre** : QGIS Desktop, dépôt officiel signé, projets et données locales
- **Catégorie** : SIG / cartographie

## 1. Choix de version et périmètre

Fiche simple : [choisir la version et le périmètre](/01-fiches-simples/debian/13/vie-du-logiciel/qgis/fiche-simple-vm-debian-13-qgis-choisir-version).

Au 27 octobre 2026, le dernier correctif LTR publié est QGIS 3.44.15 (Solothurn); QGIS 4.2.3 est la version stable courante. L'équipe QGIS recommande le LTR pour sa période de maintenance et ses tests plus poussés. Son dépôt Debian officiel liste Trixie comme cible à partir de QGIS 3.44.0. Ce guide installe donc le LTR depuis `qgis.org/debian-ltr`; il ne prétend pas que QGIS 4.x est empaqueté pour Debian 13.

Périmètre limité à QGIS Desktop sur Debian 13 amd64. QGIS Server, les plugins tiers, les scripts Python, les services de données distants et les données géographiques sensibles nécessitent une revue distincte. Préparer un poste avec environnement graphique, les jeux de données autorisés, le CRS validé par le responsable des données et un emplacement de projet sauvegardé.

## 2. Ajouter la clé et le dépôt officiels

Fiche simple : [ajouter la clé et le dépôt officiels](/01-fiches-simples/debian/13/vie-du-logiciel/qgis/fiche-simple-vm-debian-13-qgis-depot-apt).

Installer les outils, télécharger la clé publique depuis le site officiel et contrôler son empreinte avant de la référencer dans APT :

```bash
sudo apt update
sudo apt install -y ca-certificates curl gnupg
curl --fail --location --proto '=https' --tlsv1.2 -o /tmp/qgis-archive-keyring.gpg https://download.qgis.org/downloads/qgis-archive-keyring.gpg
gpg --show-keys --with-fingerprint /tmp/qgis-archive-keyring.gpg
```

Vérifier que l'empreinte affichée est `2D7E 3441 A707 FDB3 E705 9441 D155 B8E6 A419 C5BE`, clé QGIS Archive Automatic Signing Key (2022-2027). Si l'empreinte diffère ou si la clé est expirée, interrompre l'installation et consulter les instructions QGIS actualisées.

Installer la clé puis créer la source dédiée à Trixie :

```bash
sudo install -d -m 0755 /etc/apt/keyrings
sudo install -m 0644 /tmp/qgis-archive-keyring.gpg /etc/apt/keyrings/qgis-archive-keyring.gpg
sudoedit /etc/apt/sources.list.d/qgis.sources
```

Contenu du fichier `qgis.sources` :

```text
Types: deb
URIs: https://qgis.org/debian-ltr
Suites: trixie
Architectures: amd64
Components: main
Signed-By: /etc/apt/keyrings/qgis-archive-keyring.gpg
```

La configuration limite cette clé au dépôt QGIS grâce à `Signed-By`. Ne pas ajouter de dépôt nightly ou `testing` sur un poste de production.

## 3. Installer QGIS Desktop

Fiche simple : [installer QGIS Desktop](/01-fiches-simples/debian/13/vie-du-logiciel/qgis/fiche-simple-vm-debian-13-qgis-installer-qgis).

Mettre à jour l'index APT, contrôler le candidat, puis installer le logiciel et le fournisseur GRASS si ce dernier est requis par le cours ou le métier :

```bash
sudo apt update
apt-cache policy qgis
sudo apt install -y qgis qgis-plugin-grass
qgis --version
```

Vérifier que la version installée appartient à la branche 3.44 LTR. En cas de candidat inattendu, de conflit entre dépôts ou d'erreur de dépendance, ne pas forcer une installation en mélangeant des paquets Debian et QGIS. Les dépôts QGIS contiennent plusieurs branches; en environnement géré, prévoir un dépôt miroir ou une stratégie d'actualisation et de validation avant de mettre à jour les postes.

## 4. Préparer un projet reproductible

Fiche simple : [préparer un projet reproductible](/01-fiches-simples/debian/13/vie-du-logiciel/qgis/fiche-simple-vm-debian-13-qgis-projet-reproductible).

1. Lancer QGIS depuis le menu de l'environnement graphique.
2. Créer un dossier de travail avec un sous-dossier `data/` et un sous-dossier `exports/`; conserver les sources originales en lecture seule ou dans un emplacement contrôlé.
3. Charger une copie de travail d'un jeu de données autorisé, par exemple un GeoPackage de test fourni par l'équipe SIG.
4. Ouvrir les propriétés de la couche et vérifier le CRS déclaré, l'étendue, les champs et le nombre d'entités avant toute analyse.
5. Régler le CRS du projet selon le système de référence approuvé pour la zone et le livrable. Une reprojection à la volée à l'écran ne modifie pas le CRS ni les coordonnées de la source.
6. Enregistrer le projet au format compressé `.qgz` à côté de ses données quand le projet est autonome. Choisir les chemins relatifs pour faciliter un déplacement contrôlé du dossier.

Ne pas corriger un CRS inconnu en attribuant arbitrairement un EPSG. Distinguer « définir le CRS source » (interpréter les coordonnées existantes) de « reprojeter » (calculer de nouvelles coordonnées dans un autre CRS). Pour les transformations géodésiques, choisir une opération appropriée et vérifier si les grilles de transformation nécessaires sont installées.

## 5. Contrôler plugins, scripts et secrets

Fiche simple : [contrôler plugins, scripts et secrets](/01-fiches-simples/debian/13/vie-du-logiciel/qgis/fiche-simple-vm-debian-13-qgis-plugins-secrets).

- Installer uniquement les plugins nécessaires depuis le dépôt officiel ou un dépôt organisationnel approuvé; consigner leurs versions et responsables.
- Ne pas ouvrir un projet de provenance inconnue avec exécution de macros Python autorisée. Garder la demande d'autorisation de macros et paramètres par défaut restrictifs.
- Ne pas stocker de mots de passe, tokens ou données de connexion sensibles en clair dans les fichiers de projet, les chemins de source ou les scripts.
- Utiliser le gestionnaire d'authentification QGIS pour les connexions prises en charge; protéger son fichier de base d'authentification et sauvegarder le mot de passe principal séparément.
- Respecter les licences, la confidentialité et les restrictions de redistribution des données, fonds de carte, grilles et plugins.

## 6. Vérifier la chaîne projet-données-sortie

Fiche simple : [vérifier la chaîne projet, données et sortie](/01-fiches-simples/debian/13/vie-du-logiciel/qgis/fiche-simple-vm-debian-13-qgis-valider-chaine).

Pour un essai sans données opérationnelles :

1. Charger la couche test et confirmer que son rendu n'indique ni source manquante ni avertissement CRS non résolu.
2. Sauvegarder puis fermer le projet; le rouvrir depuis son emplacement final et vérifier que les couches sont toujours valides.
3. Ouvrir la table attributaire et confirmer que les valeurs attendues correspondent à la source.
4. Créer une mise en page de test avec titre, échelle, légende et sources; exporter un PDF dans `exports/`.
5. Comparer les CRS, l'emprise et quelques attributs source/sortie, puis consigner l'auteur, la version de QGIS, les données, le CRS et la date.

La validation n'établit pas l'exactitude métier des données, la validité juridique d'une carte ou la précision d'un levé. Pour toute modification de données maîtresses, travailler sur une copie/version de contrôle, appliquer une revue par un second opérateur et préserver la source.

## 7. Mise à jour et sauvegarde

Fiche simple : [mise à jour et sauvegarde](/01-fiches-simples/debian/13/vie-du-logiciel/qgis/fiche-simple-vm-debian-13-qgis-maj-sauvegarde).

Mettre QGIS à jour avec le processus APT de l'organisation après un essai sur un poste pilote. Vérifier la compatibilité des plugins, modèles de traitement, styles, chemins de données et projets avant généralisation. Les projets sauvegardés par une version récente peuvent utiliser des fonctionnalités absentes de versions plus anciennes.

Sauvegarder le projet `.qgz` avec toutes les données nécessaires ou documenter les sources distantes, les styles, grilles requises, modèles et fichiers auxiliaires. Sauvegarder le profil utilisateur séparément si l'organisation doit préserver configurations, plugins et authentifications. Tester une copie restaurée sur un poste propre; ne pas considérer la sauvegarde du seul projet comme une sauvegarde des données externes.

## Sources

- [QGIS — releases officielles](https://github.com/qgis/QGIS/releases)
- [QGIS — installation Linux et dépôts Debian, versions supportées](https://qgis.org/resources/installation-guide/)
- [QGIS — guide utilisateur 3.44, fichiers de projet et chemins de couches](https://docs.qgis.org/3.44/en/docs/user_manual/introduction/project_files.html)
- [QGIS — guide utilisateur 3.44, options, CRS et profils](https://docs.qgis.org/3.44/en/docs/user_manual/introduction/qgis_configuration.html)
- [QGIS — guide utilisateur 3.44, projections et transformations](https://docs.qgis.org/3.44/en/docs/user_manual/working_with_projections/working_with_projections.html)
- [QGIS — guide utilisateur 3.44, authentification](https://docs.qgis.org/3.44/en/docs/user_manual/auth_system/index.html)

Le dépôt amont et le poste graphique n'ont pas été installés ni testés par cette fiche. Valider le candidat APT, les dépendances graphiques, les CRS et les données sur un poste pilote avant déploiement.