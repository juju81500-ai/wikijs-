---
title: "Sources publiques TSSR pour les fiches tout-en-un"
description: "Cette note cartographie les rubriques publiques consultées le 31 octobre 2026 pour orienter les nouvelles fiches. Elle ne reproduit pas les cours, textes ou procédures des sites. Les sources sont des pistes de veille ; les procédures opérationnelles du pack doivent être vérifiées sur la documentatio"
published: true
date: 2026-11-03T09:36:14Z
tags: ["sources", "tssr", "veille", "tout-en-un"]
editor: markdown
dateCreated: 2026-11-03T09:36:14Z
dateModified: 2026-11-03T09:36:14Z
---

# Sources publiques TSSR pour les fiches tout-en-un

- **Tags** : `sources`, `tssr`, `veille`, `tout-en-un`

Cette note cartographie les rubriques publiques consultées le 31 octobre 2026 pour orienter les nouvelles fiches. Elle ne reproduit pas les cours, textes ou procédures des sites. Les sources sont des pistes de veille ; les procédures opérationnelles du pack doivent être vérifiées sur la documentation officielle du produit et sur un laboratoire correspondant à la version visée.

## Sites et rubriques consultées

| Source | Rubriques publiques pertinentes | Utilisation dans le pack |
|---|---|---|
| [kipit/nivvlem-tssr](https://github.com/kipit/nivvlem-TSSR) | [Index des modules, figé au commit `11bb1c6`](https://github.com/kipit/nivvlem-TSSR/blob/11bb1c6af3c4034099e285b193ba633dc7bea9af/modules.md), [index des fiches de référence](https://github.com/kipit/nivvlem-TSSR/blob/11bb1c6af3c4034099e285b193ba633dc7bea9af/fiches-r%C3%A9f%C3%A9rences/README.md) | Repérer des sujets TSSR : systèmes, réseau, virtualisation, Bash/PowerShell, sauvegarde, supervision et sécurité. Le lien épinglé rend la source reproductible. |
| [ZenTSSR](https://zentssr.com/) | [Modules](https://zentssr.com/modules), [installation](https://zentssr.com/installation), [exemple de route ports](https://zentssr.com/modules/ports) | Source de veille et d'idées d'apprentissage. Le contenu détaillé des routes n'était pas exposé par l'outil de consultation ; ne pas en déduire une taxonomie non vérifiée. |
| [Stephane-Robert.info](https://www.stephane-robert.info/docs/) | [DevOps/DevSecOps](https://www.stephane-robert.info/docs/devops/), [conteneurisation](https://www.stephane-robert.info/docs/conteneurisation/), [Kubernetes](https://www.stephane-robert.info/docs/conteneurs/orchestrateurs/kubernetes/), [CI/CD](https://www.stephane-robert.info/docs/pipeline-cicd/) | Repérer les thèmes d'automatisation, conteneurs, orchestration, sécurité intégrée et livraison logicielle. |
| [Root & Code — jousseaume.online](https://www.jousseaume.online/) | [Réseau](https://www.jousseaume.online/categorie/reseau/), [fondamentaux](https://www.jousseaume.online/categorie/fondamentaux/), [bases de données](https://www.jousseaume.online/categorie/bases-de-donnees/), [systèmes](https://www.jousseaume.online/categorie/systemes/), [cybersécurité](https://www.jousseaume.online/categorie/cybersecurite/) | Repérer des besoins transverses de diagnostic, de systèmes, réseau, bases de données et sécurité. |
| [Root & Code — jousseaume.online](https://www.jousseaume.online/) | [Réseau](https://www.jousseaume.online/categorie/reseau/), [voyage d'un paquet TCP/IP](https://www.jousseaume.online/cours/voyage-dun-paquet-tcp-ip/), [adressage IPv4](https://www.jousseaume.online/cours/adressage-ipv4-introduction/), [VLAN](https://www.jousseaume.online/cours/switch-et-vlan-animation/), [DHCP](https://www.jousseaume.online/cours/dhcp-en-4-temps/), [pare-feu](https://www.jousseaume.online/cours/pare-feu-et-regles/), [configuration réseau Linux](https://www.jousseaume.online/cours/configurer-reseau-linux/) et [Windows](https://www.jousseaume.online/cours/configurer-reseau-windows/) | Repérer des besoins transverses de diagnostic, de systèmes, réseau, bases de données et sécurité. Les animations restent accessibles sur le site source; le [parcours théorique réseau du pack](/fr/00-cours-theoriques/parcours-theorique-reseaux-tssr) en propose une synthèse originale et des liens directs. |

Les pages peuvent évoluer. Les liens ne constituent pas une approbation, une garantie d'exactitude ni une autorisation de copier leur contenu. Avant une fiche de produit, remplacer les sources d'inspiration par des références officielles du fournisseur et de la version.

## Taxonomie des fiches tout-en-un

Les sites consultés servent à repérer des thèmes de formation et des tâches récurrentes, pas à fournir des procédures prêtes pour la production. Chaque fiche tout-en-un doit traiter un seul OS et une seule version, puis renvoyer vers les fiches simples ou complètes de la même cible. Les huit catégories restent des sous-classements sous le dossier OS/version : `01-fiches-simples/<OS>/<version>/Tout-en-un/<categorie>/`.

| Catégorie | Périmètre |
|---|---|
| Réseaux et protocoles | Adressage, ports, DNS, DHCP, VLAN, VPN, proxy |
| Identités et accès | Comptes, annuaires, groupes, privilèges, stratégies |
| Services d'infrastructure | Web, fichiers, bases de données, services réseau |
| Automatisation et scripting | Bash, PowerShell, tâches planifiées, gestion d'erreurs |
| Sécurité et durcissement | Mises à jour, accès, configuration sûre, contrôles |
| Virtualisation, conteneurs et cloud | Hôtes, VM, conteneurs, plateformes cloud |
| Exploitation, supervision et sauvegarde | Journaux, alertes, maintenance, restauration, reprise |
| Support et gestion de service | Triage, procédure de support, inventaire, ITSM |

### Règle de classement

- Créer une fiche distincte par OS/version cible et la ranger dans `01-fiches-simples/<OS>/<version>/Tout-en-un/<categorie>/`.
- Si une procédure s'applique à plusieurs OS ou à plusieurs versions, dupliquer la fiche pour chaque cible, puis adapter et vérifier les commandes, prérequis, chemins et validations.
- Ne pas remplacer ces copies par une fiche multi-OS unique ; chaque fiche doit pouvoir être suivie et maintenue pour sa cible.
- Une procédure spécifique à un produit reste liée aux fiches du produit dans `Vie-du-logiciel/<Produit>/`.
- Les catégories servent au tri thématique ; elles ne déterminent pas les OS concernés.

## Cycle de création et de maintenance

1. Relever un besoin de tâche récurrente, puis vérifier les fiches simples et complètes déjà présentes.
2. Consulter les sources publiques pour le cadrage, sans aspirer ni recopier leurs textes. Chercher ensuite la documentation officielle de l'éditeur et les pages correspondant à l'OS/version visés.
3. Rédiger avec le [modèle de fiche tout-en-un](/fr/03-templates-machines/template-fiche-tout-en-un), créer une copie par cible OS/version, et consigner dans chacune les sources et la date de vérification.
4. Tester chaque commande sur un laboratoire jetable ; pour une fiche P0, faire relire par une seconde personne et tester le retour arrière.
5. Vérifier les liens et la structure, relire le diff pour secrets et contenu tiers, puis soumettre une Pull Request.
6. Vérifier les liens sources chaque trimestre ; revoir les commandes sensibles aux versions chaque trimestre et les fiches stables chaque semestre.
7. Après une mise à jour majeure ou une alerte de sécurité pertinente, déclencher une revue sans attendre l'échéance.
8. Retirer des étapes actives les commandes obsolètes, documenter le remplacement, et épingler les références GitHub à un commit. Ne jamais présenter le contrôle d'URL du CLI comme une validation technique du contenu.