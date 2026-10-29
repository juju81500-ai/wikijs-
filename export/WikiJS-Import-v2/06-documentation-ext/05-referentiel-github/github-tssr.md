---
title: "Référentiel GitHub externe — Sysadmin et TSSR"
description: "Répertoire de ressources externes pour retrouver rapidement une syntaxe, comparer des exemples et repérer des logiciels. Ce catalogue est une liste de pistes, pas une validation des commandes ni une procédure de production."
published: true
date: 2026-10-27T20:01:13Z
tags: ["documentation-externe", "github", "sysadmin", "tssr", "cheat-sheets", "proxmox"]
editor: markdown
dateCreated: 2026-10-27T20:01:13Z
dateModified: 2026-10-27T20:01:13Z
---

# Référentiel GitHub externe — Sysadmin et TSSR

- **Tags** : `documentation-externe`, `github`, `sysadmin`, `tssr`, `cheat-sheets`, `proxmox`

Répertoire de ressources externes pour retrouver rapidement une syntaxe, comparer des exemples et repérer des logiciels. Ce catalogue est une liste de pistes, pas une validation des commandes ni une procédure de production.

**Vérification des liens et états : 27 octobre 2026.** Les dépôts et leur contenu évoluent; vérifier le README, l'activité, la licence, les versions compatibles et les avis de sécurité avant utilisation. Les résumés ci-dessous sont descriptifs; le contenu des dépôts reste la propriété de leurs auteurs.

## 1. Mémos et cheat sheets

| Dépôt | Usage repéré | Vigilance |
|---|---|---|
| [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) | Collection de références et outils pour l'administration système et réseau | Grand volume de liens et d'exemples hétérogènes; vérifier chaque commande dans la documentation de l'outil et sur la version réellement utilisée. |
| [LeCoupa/awesome-cheatsheets](https://github.com/LeCoupa/awesome-cheatsheets) | Fiches synthétiques de langages, outils, bases de données et frameworks | Ressource communautaire en évolution, principalement développement; ne remplace ni les manuels officiels ni une procédure locale. |
| [cheat/cheat](https://github.com/cheat/cheat) | Lecteur et gestionnaire de fiches interactives en terminal | Le programme ne fournit pas lui-même les fiches communautaires; examiner les sources et le contenu avant de les importer ou exécuter. |
| [rstacruz/cheatsheets (Devhints)](https://github.com/rstacruz/cheatsheets) | Références synthétiques, surtout orientées développement | Certaines pages changent régulièrement; vérifier la date, la version et l'applicabilité au système cible. |
| [denisidoro/navi](https://github.com/denisidoro/navi) | Navigateur interactif de fiches pouvant proposer des commandes | Le projet annonce un **mode maintenance** sans nouvelles fonctionnalités; une fiche peut lancer une commande. Lire et éditer la commande avant exécution. |

## 2. Scripts et exemples de déploiement

| Dépôt | Usage repéré | Vigilance |
|---|---|---|
| [Community Scripts — Proxmox VE](https://github.com/community-scripts/ProxmoxVE) | Scripts communautaires de création de VM/LXC et d'installation d'applications Proxmox | Successeur actif de l'ancien dépôt tteck; le projet précise que les scripts s'exécutent avec les privilèges root sur l'hôte Proxmox. Lire le script **et son moteur appelé**, tester sur un hôte de lab sauvegardé; aucun script n'est réputé prêt pour la production par sa seule présence dans ce dépôt. |
| [tteck/Proxmox (archivé)](https://github.com/tteck/Proxmox) | Ancien dépôt Helper-Scripts Proxmox | Archivé en novembre 2024, en lecture seule. Le dépôt annonce [Community Scripts — Proxmox VE](https://github.com/community-scripts/ProxmoxVE) comme nouvelle maison du projet; ne pas suivre ses anciennes commandes comme instructions à jour. |
| [ChristianLempa/cheat-sheets](https://github.com/ChristianLempa/cheat-sheets) | Références, extraits de configuration et documentation personnelle pour outils et homelabs | Équivalent direct pour les mémos. Le lien initial `ChristianLempa/scripts` ne correspond pas à un dépôt accessible; revoir les versions et hypothèses de chaque exemple avant adaptation. |
| [ChristianLempa/boilerplates](https://github.com/ChristianLempa/boilerplates) | Gabarits réutilisables Docker, Kubernetes, Terraform, Ansible et scripts | Alternative pour créer et configurer des modèles, pas un dépôt de scripts prêts à lancer. Le format a évolué en v0.2; contrôler format, génération, variables et secrets avant usage. |
| [DoTheEvo/selfhosted-apps-docker](https://github.com/DoTheEvo/selfhosted-apps-docker) | Exemples de piles auto-hébergées et configurations Compose | Certaines configurations peuvent être anciennes ou orientées homelab; contrôler les secrets, volumes, versions d'images, ports, sauvegardes et exposition avant adaptation. |
| [alexanderepstein/Bash-Snippets](https://github.com/alexanderepstein/Bash-Snippets) | Petits scripts Bash utilitaires | Activité et publications peu récentes; le README indique que le maintien est limité. Éviter un déploiement sans revue, test et confirmation que les API utilisées fonctionnent encore. |

## 3. Cybersécurité — référence uniquement

| Dépôt | Objet | Cadre de consultation |
|---|---|---|
| [swisskyrepo/PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings) | Référentiel de sécurité applicative et de tests d'intrusion, pouvant contenir des payloads et techniques d'exploitation | À consulter pour la compréhension défensive et la rédaction de règles de détection. Aucune procédure de copie/exécution de payloads ou de test contre un tiers n'est fournie dans ce pack. Les essais actifs nécessitent un lab isolé et une autorisation explicite. |
| [peass-ng/PEASS-ng](https://github.com/peass-ng/PEASS-ng) | Outils d'audit local de configuration et de chemins de privilèges sur Linux/Windows | Le projet indique un usage pour des tests autorisés ou l'éducation. N'exécuter que sur un système possédé ou explicitement autorisé, de préférence en lab; les résultats peuvent exposer des données sensibles et signaler des faux positifs. Ne pas traiter une sortie comme preuve automatique d'exploitabilité. |

Ces liens ne constituent pas une approbation d'usage offensif. Le pack conserve le périmètre défensif défini dans sa [matrice de couverture](/00-administration/matrice-couverture-logiciels-production-tssr-ais) : inventaire, détection, durcissement, analyse autorisée et traitement des constats.

## 4. Listes de logiciels sysadmin

| Dépôt | Usage repéré | Vigilance |
|---|---|---|
| [awesome-foss/awesome-sysadmin](https://github.com/awesome-foss/awesome-sysadmin) | Liste organisée de logiciels libres pour l'administration système | Index communautaire, pas une certification de maintenance, sécurité, licence ou adéquation aux besoins. Confirmer chaque projet à sa source primaire. |
| [Corsinvest/awesome-proxmox-ve](https://github.com/Corsinvest/awesome-proxmox-ve) | Équivalent recommandé pour une liste organisée de documentation, outils, API, sauvegarde, stockage, réseau et scripts Proxmox VE | Liste communautaire CC0, mise à jour régulièrement au 27 octobre 2026. Vérifier les dépôts vers lesquels elle renvoie; la présence dans une liste ne vaut pas validation de sécurité ou de production. |
| [alexgoesgit/awesome-proxmox-ve-virtualization](https://github.com/alexgoesgit/awesome-proxmox-ve-virtualization) | Deuxième liste Proxmox organisée par thèmes, avec site de recherche/filtrage | Dépôt actif au 27 octobre 2026 et sous CC0; contrôler chaque outil lié et sa licence propre. |
| [vzamora/Proxmox-Cheatsheet](https://github.com/vzamora/Proxmox-Cheatsheet) | Notes et guides pratiques d'installation Proxmox et de services homelab | Équivalent plus proche d'une collection de fiches personnelles, mais plusieurs contenus sont explicitement en cours ou déclarés incomplets; versions et sécurité à revoir. |

Le lien fourni `kiler129/awesome-proxmox` répond 404 au contrôle du 27 octobre 2026. Les dépôts ci-dessus ont été retrouvés par recherche GitHub; ils sont des alternatives par contenu, sans lien de succession établi avec le dépôt disparu.

## 5. Requêtes de recherche GitHub

Sélectionner le type de recherche approprié (**Repositories** pour trouver des dépôts, **Code** pour rechercher dans le code ou les Markdown) et contrôler le propriétaire du résultat.

```text
topic:tssr
topic:bts-sio
"Technicien Supérieur Systèmes et Réseaux" language:Markdown
(cours OR fiches) topic:sysadmin language:Markdown
"cheat sheet" (bash OR powershell)
```

Les opérateurs disponibles diffèrent selon la recherche GitHub choisie. Si une requête ne renvoie pas de résultat, essayer séparément les termes ou sélectionner explicitement le filtre de langue/type; un résultat de recherche n'est pas une validation de confiance.

## Règles minimales avant de réutiliser un exemple

1. Identifier l'auteur, le dépôt canonique, la licence, les versions prises en charge, les dernières publications et les avis de sécurité.
2. Lire l'intégralité du script et de ses dépendances; ne jamais exécuter aveuglément `curl | sh`, `wget | bash`, un one-liner distant ou un script tiers en root/administrateur.
3. Vérifier les changements apportés, les privilèges, les connexions réseau, les téléchargements, les dépôts, les identifiants, les volumes, les ports ouverts et les mécanismes de mise à jour.
4. Tester en VM/lab isolé avec sauvegarde et retour arrière; adapter à la version et aux politiques locales; faire relire avant la production.
5. Ne pas publier de secrets, journaux sensibles, données client ou informations d'infrastructure dans les issues, captures, commits ou services externes.

## Sources de statut consultées

- [Community Scripts — Proxmox VE](https://github.com/community-scripts/ProxmoxVE) et [annonce d'archive tteck](https://github.com/tteck/Proxmox)
- [Christian Lempa — dépôts et liens canoniques](https://github.com/ChristianLempa)
- [Christian Lempa — cheat sheets](https://github.com/ChristianLempa/cheat-sheets) et [boilerplates](https://github.com/ChristianLempa/boilerplates)
- [navi — dépôt et état de maintenance](https://github.com/denisidoro/navi)
- [PEASS-ng — dépôt et avis d'utilisation autorisée](https://github.com/peass-ng/PEASS-ng)
- [Awesome Sysadmin](https://github.com/awesome-foss/awesome-sysadmin)
- [Awesome Proxmox VE — Corsinvest](https://github.com/Corsinvest/awesome-proxmox-ve) et [Awesome Proxmox VE Virtualization](https://github.com/alexgoesgit/awesome-proxmox-ve-virtualization)