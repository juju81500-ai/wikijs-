# Pack Master Wiki.js — TSSR / AIS / Cyber

Pack de documentation technique en français, destiné à être importé dans [Wiki.js](https://js.wiki/) (2.x) : fiches pratiques d'administration systèmes et réseaux, guides d'installation, durcissement (hardening) et aide-mémoire.

Chaque fiche suit une charte simple : **une commande dans un bloc de code, suivie d'une ligne `👉 Explication`** qui dit à quoi elle sert et ce qu'il faut vérifier.

C'est un projet **collaboratif et open source dans son esprit** : les contributions sont les bienvenues (voir [CONTRIBUTING.md](CONTRIBUTING.md)).
> ⚠️ **Licence** : aucun fichier `LICENSE` n'est présent à ce jour, donc aucune licence n'est accordée explicitement. Le mainteneur doit en choisir une (par ex. MIT, Apache-2.0 pour le code ; CC BY-SA 4.0 pour la documentation) et l'ajouter avant toute réutilisation. Le contenu de tiers ne doit jamais être recopié (voir CONTRIBUTING).

## Arborescence actuelle

| Dossier | Contenu |
|---|---|
| [00-Cours-Theoriques](00-Cours-Theoriques/) | Parcours théoriques originaux, [bases et leçons tout-en-un](00-Cours-Theoriques/Tout-en-un/README.md), et liens vers les cours, animations et illustrations hébergés chez leurs auteurs. |
| [00-Administration](00-Administration/) | Pilotage du pack : guides d'import Wiki.js, matrices de contrôle, scripts de vérification et de préparation de l'import. Consulter les documents de ce dossier pour la structure à jour. |
| [01-Fiches-Simples](01-Fiches-Simples/) | Fiches courtes, une tâche = une fiche, classées par OS/plateforme (Debian, Ubuntu, Rocky Linux, Alpine, Proxmox, VMware, TrueNAS, pfSense, OPNsense, logiciels, transverses). Les bases tout-en-un sont dans `00-Cours-Theoriques/Tout-en-un` et se déclinent en copies propres à chaque OS/version concerné. |
| [02-Fiches-Completes](02-Fiches-Completes/) | Procédures complètes d'installation/configuration (présentation, paramètres machine, protocole, validation, retour arrière). |
| [03-Templates-Machines](03-Templates-Machines/) | Modèles officiels de fiches (simple, complète) et synthèse d'architecture. |
| [04-Questions-Reponses](04-Questions-Reponses/) | Fiches Q/R et de réparation/dépannage. |
| [05-Hardening-AIS-Cyber](05-Hardening-AIS-Cyber/) | Durcissement et bonnes pratiques de cybersécurité. |
| [06-Documentation-ext](06-Documentation-ext/) | Aide-mémoire, liens vers documentations officielles, communautés, veille CVE (liens et résumés, pas de copie). |

La structure et les responsabilités de `00-Administration` sont décrites dans son [index](00-Administration/README.md).

## Cloner le dépôt

```bash
git clone https://github.com/juju81500-ai/wikijs-.git
cd wikijs-
```

## Importer dans Wiki.js

Prérequis : une instance Wiki.js 2.x fonctionnelle, Python 3.

1. **Vérifier le pack** avant tout import, avec le script `verify_wiki.py` (dossier d'administration) :
   ```bash
   python3 00-Administration/03-Qualite-Tests/verify_wiki.py
   ```
2. **Synchroniser depuis GitHub** : dans Wiki.js, **Administration → Stockage → Git**, renseigner l'URL du dépôt, la branche et une clé de déploiement (jamais committée), puis activer la synchronisation.
3. **Contrôler les sources avant publication** :
   ```bash
   python3 tools/pack_master/pack_master.py check
   ```
4. Les exports pour import manuel restent optionnels ; la commande `refresh` les recrée dans `export/`. Ne pas l'utiliser pour le flux de synchronisation GitHub directe.
5. Les guides détaillés (import par SSH/Docker, intégration Git, réinitialisation) se trouvent dans le dossier [00-Administration](00-Administration/).

> L'organisation des documents et les anciens chemins compatibles sont récapitulés dans l'[index de `00-Administration`](00-Administration/README.md).

Pour lancer les contrôles et suivre les sources publiques, consulter l'[outil CLI Pack Master](tools/pack_master/README.md).

## Contribuer, sécurité

- Contribuer : [CONTRIBUTING.md](CONTRIBUTING.md)
- Signaler une faille ou une fuite : [SECURITY.md](SECURITY.md)
- Les mots de passe et données sensibles ne sont **jamais** stockés dans ce dépôt ; ils restent sur le serveur du mainteneur, accessibles aux seules personnes autorisées.
