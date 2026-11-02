# Guide — scripts de référencement des machines

- **Tags** : `template`, `fiche-machine`, `script`, `referentiel`

Trois scripts de ce dossier facilitent le référencement. Ils sont en lecture seule : ils ne modifient ni la machine ni le dépôt, hormis le fichier de sortie qu'ils écrivent. Les champs qu'ils ne peuvent pas détecter restent à compléter à la main.

## Vue d'ensemble

| Script | S'exécute | Rôle | Produit |
|---|---|---|---|
| `generer_referentiel_machines.py` | Sur le poste qui contient le dépôt | Compte les fiches par OS/version | `Referentiel_Machines.md` |
| `collecter_machine.sh` | Sur chaque machine Linux | Relève les infos de la machine | Fiche machine `.md` |
| `collecter_machine.ps1` | Sur chaque machine Windows | Relève les infos de la machine | Fiche machine `.md` |

Le premier script ne lit que les dossiers du dépôt : le copier sur une machine ne donne aucune information sur elle. Seuls les scripts `collecter_machine.*` interrogent la machine où ils tournent.

## 1. Référentiel OS/version

```bash
python3 03-Templates-Machines/generer_referentiel_machines.py
```

Chaque ligne du tableau correspond à un couple OS/version.

| Colonne | Remplissage |
|---|---|
| OS, Version, Famille | Automatique |
| Simples, Complètes | Automatique : nombre de fiches et lien vers le dossier |
| Rôle, Template utilisé, Statut, Notes | Manuel, conservé à chaque régénération |

Les cases manuelles sont retrouvées grâce au couple OS/Version : ne pas renommer ces deux colonnes dans le tableau.

## 2. Fiche machine pré-remplie

À copier sur la machine à documenter, puis à lancer.

| Système | Commande |
|---|---|
| Linux | `sudo ./collecter_machine.sh [fiche.md]` |
| Windows (PowerShell administrateur) | `.\collecter_machine.ps1 [-Out fiche.md]` |

Sans droits élevés, les ports et le pare-feu peuvent être vides ou « non détectés ».

Sans argument, le fichier est nommé `fiche-machine_<nom-hôte>.md` dans le dossier courant.

### Champs relevés automatiquement

Nom d'hôte, type (VM, LXC ou physique), OS et version, vCPU, RAM, disques, adresses IP, services actifs, ports en écoute, état du pare-feu local, date de dernière modification.

### Champs à compléter à la main

Marqués `[à compléter]` dans la fiche : machine physique/hôte, environnement, statut opérationnel, rôle et utilisation, pare-feu externe, date de création.

La section 5 « Mode d'Exécution Appliqué » du modèle n'est pas générée : à ajouter si nécessaire en reprenant le modèle de [Templates_Officiels_Wiki](Templates_Officiels_Wiki.md).

## Flux conseillé

1. Lancer `collecter_machine.*` sur la machine et récupérer le fichier produit.
2. Compléter les champs `[à compléter]` et renommer le fichier selon la nomenclature `[MachinePhysique]_[Env]_[Type]_[NomMachine]_[OS]_[Statut]`.
3. Ranger la fiche dans le dépôt.
4. Relancer `generer_referentiel_machines.py` pour mettre à jour les compteurs, puis remplir à la main les colonnes manuelles du référentiel.

## Limites

- Les valeurs relevées sont un instantané : relancer le script après un changement.
- Le nom de la fiche n'est pas généré au format de la nomenclature officielle, car il dépend de champs manuels.
- Les services et ports listés sont ceux en cours d'exécution, pas la liste complète des paquets installés.
- Le script PowerShell n'a pas encore été testé sur une machine Windows.
