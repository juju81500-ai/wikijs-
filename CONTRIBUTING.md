# Contribuer au Pack Master Wiki.js

Merci de votre intérêt ! Le projet est collaboratif : toute personne peut proposer une fiche, une correction ou une amélioration via une Pull Request.

## Prérequis

- Git et un compte GitHub
- Python 3 (pour les scripts de vérification et d'export)
- Un éditeur Markdown ; optionnel : une instance Wiki.js de test (Docker)

## 1. Fork et clone

```bash
# Forker le dépôt sur GitHub, puis :
git clone https://github.com/<votre-compte>/wikijs-.git
cd wikijs-
git remote add upstream https://github.com/juju81500-ai/wikijs-.git
git fetch upstream
```

## 2. Créer une branche

```bash
git switch -c fiche/<os>-<sujet-court>      # ex. fiche/debian-13-nftables
```
Préfixes conseillés : `fiche/`, `fix/`, `docs/`, `tools/`.

## 3. Rédiger une fiche selon la charte

1. Partir du modèle officiel du dossier [03-Templates-Machines](03-Templates-Machines/) (fiche simple ou complète).
2. Placer la fiche dans le dossier correspondant (`01-Fiches-Simples/<OS>/…`, `02-Fiches-Completes/…`, etc.) et reprendre le nommage des fiches voisines.
3. Renseigner l'en-tête (environnement, OS/version, catégorie, tags) et le problème précis à résoudre.
4. **Chaque étape = une commande réelle dans un bloc de code, suivie d'une ligne `👉 Explication`** :

   ````markdown
   1. Vérifier l'état du service SSH :
      ```bash
      systemctl is-active ssh
      ```
      👉 Explication : retourne `active` si le service tourne ; sinon consulter `journalctl -u ssh`.
   ````
5. Pas de placeholders (`[Commande]`, `NOM_DU_FICHIER`…), pas de commande générique non adaptée à l'OS.
6. Prévoir validation et retour arrière, et signaler les commandes destructives.
7. Aucun secret, mot de passe, IP interne réelle ou donnée client : utiliser des valeurs d'exemple (`192.0.2.10`, `exemple.local`, `<MOT_DE_PASSE>`).

## 4. Sources et citations

- Citer ses sources : lien vers la documentation officielle ou la page consultée, avec la version concernée.
- **Ne pas copier les textes des sites** (articles, tutoriels, blogs, dépôts tiers) : reformuler avec ses propres mots, vérifier chaque commande sur un lab, et ne garder que de très courtes citations clairement attribuées si nécessaire.
- Ne pas importer de contenu tiers dont la licence n'est pas claire.

## 5. Validation

Depuis la racine du dépôt :

```bash
python3 00-Administration/03-Qualite-Tests/verify_wiki.py
```
Le script effectue des contrôles structurels en lecture seule ; corriger toutes les erreurs signalées. Si les scripts ont été déplacés, les retrouver dans le dossier `00-Administration`.

## 6. Génération et test des exports

Les exports sont **générés** ; ne jamais les modifier à la main.

```bash
python3 00-Administration/02-Operations-WikiJS/prepare_wikijs_import.py --dry-run
python3 00-Administration/02-Operations-WikiJS/prepare_wikijs_import.py --check
```
Pour tester réellement, importer l'arbre généré dans une instance Wiki.js de test (jamais en production) et vérifier que les pages s'affichent avec leurs blocs de code. N'ajoutez les exports régénérés à votre PR que si le mainteneur le demande.

## 7. Commit et Pull Request

```bash
git add <fichiers concernés>
git commit -m "docs(debian): ajoute la fiche nftables Debian 13"
git push -u origin fiche/<os>-<sujet-court>
```
- Un commit = un changement logique, message court et explicite en français.
- Ouvrir la PR vers `main` en décrivant : le sujet, l'OS/version testés, les sources, et le résultat de `verify_wiki.py`.
- Avant de pousser : relire le diff pour s'assurer qu'aucun secret ni fichier local n'est inclus (voir [SECURITY.md](SECURITY.md)).

## 8. Revue

- Le mainteneur vérifie la conformité à la charte, l'exactitude technique, les sources et l'absence de contenu copié ou sensible.
- Des modifications peuvent être demandées : poussez-les sur la même branche.
- Synchroniser régulièrement avec `upstream` (`git fetch upstream && git rebase upstream/main`).

## Licence

Aucun fichier `LICENSE` n'existe actuellement : le projet ne déclare donc pas de licence. Il est recommandé au mainteneur d'en préciser une. D'ici là, ne contribuez que du contenu dont vous détenez les droits, et jamais de contenu tiers recopié.
