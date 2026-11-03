# Pack Master Wiki.js — TSSR / AIS / Cyber

Pack de documentation technique en français, destiné à être importé dans [Wiki.js](https://js.wiki/) (2.x) : fiches pratiques d'administration systèmes et réseaux, guides d'installation, durcissement (hardening) et aide-mémoire.

Chaque fiche suit une charte simple : **une commande dans un bloc de code, suivie d'une ligne `👉 Explication`** qui dit à quoi elle sert et ce qu'il faut vérifier.

C'est un projet **collaboratif et open source dans son esprit** : les contributions sont les bienvenues (voir [contributing.md](contributing.md)).
> ⚠️ **Licence** : aucun fichier `LICENSE` n'est présent à ce jour, donc aucune licence n'est accordée explicitement. Le mainteneur doit en choisir une (par ex. MIT, Apache-2.0 pour le code ; CC BY-SA 4.0 pour la documentation) et l'ajouter avant toute réutilisation. Le contenu de tiers ne doit jamais être recopié (voir CONTRIBUTING).

## Arborescence actuelle

| Dossier | Contenu |
|---|---|
| [00-cours-theoriques](00-cours-theoriques) | Parcours théoriques originaux, [bases et leçons tout-en-un](00-cours-theoriques/tout-en-un/readme.md), et liens vers les cours, animations et illustrations hébergés chez leurs auteurs. |
| [00-administration](00-administration) | Pilotage du pack : guides d'import Wiki.js, matrices de contrôle, scripts de vérification et de préparation de l'import. Consulter les documents de ce dossier pour la structure à jour. |
| [01-fiches-simples](01-fiches-simples) | Fiches courtes, une tâche = une fiche, classées par OS/plateforme (Debian, Ubuntu, Rocky Linux, Alpine, Proxmox, VMware, TrueNAS, pfSense, OPNsense, logiciels, transverses). Les bases tout-en-un sont dans `00-cours-theoriques/Tout-en-un` et se déclinent en copies propres à chaque OS/version concerné. |
| [02-fiches-completes](02-fiches-completes) | Procédures complètes d'installation/configuration (présentation, paramètres machine, protocole, validation, retour arrière). |
| [03-templates-machines](03-templates-machines) | Modèles officiels de fiches (simple, complète) et synthèse d'architecture. |
| [04-questions-reponses](04-questions-reponses) | Fiches Q/R et de réparation/dépannage. |
| [05-hardening-ais-cyber](05-hardening-ais-cyber) | Durcissement et bonnes pratiques de cybersécurité. |
| [06-documentation-ext](06-documentation-ext) | Aide-mémoire, liens vers documentations officielles, communautés, veille CVE (liens et résumés, pas de copie). |

La structure et les responsabilités de `00-administration` sont décrites dans son [index](00-administration/readme.md).

## Cloner le dépôt

```bash
git clone https://github.com/juju81500-ai/wikijs-.git
cd wikijs-
```

## Importer dans Wiki.js

Prérequis : une instance Wiki.js 2.x fonctionnelle, Python 3.

1. **Vérifier le pack** avant tout import, avec le script `verify-wiki.py` (dossier d'administration) :
   ```bash
   python3 00-administration/03-qualite-tests/verify-wiki.py
   ```
2. **Synchroniser depuis GitHub** : dans Wiki.js, **Administration → Stockage → Git**, renseigner l'URL du dépôt, la branche et une clé de déploiement (jamais committée), puis activer la synchronisation.
3. **Contrôler les sources avant publication** :
   ```bash
   python3 tools/pack-master/pack-master.py check
   ```
4. Les exports pour import manuel restent optionnels ; la commande `refresh` les recrée dans `export/`. Ne pas l'utiliser pour le flux de synchronisation GitHub directe.
5. Les guides détaillés (import par SSH/Docker, intégration Git, réinitialisation) se trouvent dans le dossier [00-administration](00-administration).

> L'organisation des documents et les anciens chemins compatibles sont récapitulés dans l'[index de `00-administration`](00-administration/readme.md).

Pour lancer les contrôles et suivre les sources publiques, consulter l'[outil CLI Pack Master](tools/pack-master/readme.md).

## Contribuer, sécurité

- Contribuer : [contributing.md](contributing.md)
- Signaler une faille ou une fuite : [security.md](security.md)
- Les mots de passe et données sensibles ne sont **jamais** stockés dans ce dépôt ; ils restent sur le serveur du mainteneur, accessibles aux seules personnes autorisées.
