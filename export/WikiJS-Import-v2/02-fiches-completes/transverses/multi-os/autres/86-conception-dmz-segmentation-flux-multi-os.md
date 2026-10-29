---
title: "Concevoir et valider une DMZ réseau"
description: "Une DMZ est une zone de confiance distincte destinée aux services qui doivent communiquer avec des réseaux moins fiables, notamment Internet. Elle limite les chemins de communication vers le réseau interne; elle ne rend pas à elle seule un service exposé sûr et ne remplace ni le durcissement des hôt"
published: true
date: 2026-10-29T20:14:10Z
tags: ["dmz", "segmentation", "firewall", "reseau", "ipv4", "ipv6", "durcissement"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Concevoir et valider une DMZ réseau

- **Type de fiche** : Architecture / Sécurité / Réseau
- **Environnement** : Réseau d'entreprise ou laboratoire isolé; pare-feu physique ou virtuel
- **Périmètre** : définition des zones, politique de flux, tests et exploitation d'une DMZ
- **Plateformes** : Multi-OS; les noms de menus et fonctions dépendent du pare-feu et de sa version
- **Tags** : `dmz`, `segmentation`, `firewall`, `reseau`, `ipv4`, `ipv6`, `durcissement`

## 1. Objectif et limites

Une DMZ est une zone de confiance distincte destinée aux services qui doivent communiquer avec des réseaux moins fiables, notamment Internet. Elle limite les chemins de communication vers le réseau interne; elle ne rend pas à elle seule un service exposé sûr et ne remplace ni le durcissement des hôtes, ni la supervision, ni la gestion des correctifs.

Cette fiche donne une méthode de conception sans constructeur. Elle ne fournit pas de règle à copier-coller : adresses, interfaces, routage, fonctions de NAT et ordre des règles varient selon le produit. Confirmer le comportement effectif avec la documentation de la version déployée et une revue de changement.

## 2. Définir les zones et les actifs

Avant de créer des VLAN ou des règles, inventorier les services, les utilisateurs, les dépendances, les administrateurs, les adresses IPv4/IPv6 et les chemins de données. Pour chaque actif, identifier son propriétaire, sa criticité, ses ports/protocoles et le sens des connexions initiées.

Zones courantes à distinguer selon le besoin :

- **WAN / réseaux non fiables** : clients Internet et autres réseaux externes.
- **DMZ publique** : reverse proxy, relais SMTP, DNS autoritatif ou service explicitement publié.
- **DMZ applicative** : composants intermédiaires qui n'ont pas besoin d'accéder librement au LAN.
- **LAN / données** : postes, annuaire, bases de données et services internes.
- **Administration** : bastion et postes d'administration, séparés des services publiés.
- **Services d'infrastructure** : DNS, NTP, mises à jour, sauvegarde, journalisation et supervision, selon leur architecture.

Le nombre de zones dépend des frontières de confiance et des besoins de flux. Une zone dédiée n'a de valeur que si son cloisonnement est appliqué et vérifié sur les pare-feu, commutateurs, hyperviseurs et hôtes concernés.

## 3. Écrire la matrice de flux avant les règles

Documenter au minimum l'initiateur, la source, la destination, le protocole/port, le motif métier, le propriétaire, le journal requis, la date de revue et la décision. Utiliser des adresses ou objets réseau précis, jamais une règle générale « DMZ vers LAN ».

| Source | Destination | Décision par défaut | Exceptions possibles, à justifier |
|---|---|---|---|
| Internet | Service publié en DMZ | Refuser | Flux entrant strictement nécessaires vers un frontal public; publier uniquement les ports attendus. |
| Internet | LAN, administration, gestion | Refuser | Aucune ouverture directe pour un usage courant; accès d'administration via une solution dédiée et authentifiée. |
| DMZ | LAN / zone de données | Refuser | Un service applicatif peut initier un flux précis vers une dépendance nommée, sur le port attendu, si l'architecture l'exige. |
| DMZ | Internet | Refuser par défaut ou contrôler | Résolution DNS, synchronisation horaire, dépôts de mises à jour ou API explicitement identifiés. Limiter destinations et méthodes lorsque le pare-feu le permet. |
| Administration | Équipements et hôtes de la DMZ | Refuser depuis les réseaux utilisateurs | Administration depuis le bastion/poste de gestion, avec comptes nominatifs, MFA si disponible et journalisation. |
| Supervision / collecte de logs | Actifs DMZ | Flux requis uniquement | Collecte initiée par le collecteur ou envoi vers une destination de logs connue; protéger le transport et les données. |
| LAN | Service DMZ | Refuser par défaut | Accès utilisateur ou applicatif requis, limité aux groupes, hôtes, ports et usages explicitement recensés. |

Pour chaque autorisation, consigner le besoin, le propriétaire, la date de création, la date d'expiration ou de revue et le ticket de changement. Ne pas ajouter de flux de retour génériques si le pare-feu est stateful et que le retour de session est déjà géré par son moteur d'état.

## 4. Concevoir les contrôles

- Définir un refus par défaut aux frontières interzones et ajouter uniquement les exceptions documentées. Examiner les règles implicites, automatiques, flottantes et celles héritées des équipements.
- Séparer les interfaces/VLAN et les chemins d'administration. Éviter les hôtes à double interface qui peuvent router ou ponter la DMZ vers le LAN; tout besoin de routage doit être explicite, contrôlé et supervisé.
- Ne pas placer une base de données ou un contrôleur de domaine dans la zone publique par facilité. Si un composant DMZ doit accéder à un service interne, limiter la connexion à ce service et évaluer un relais, proxy ou composant intermédiaire.
- Contrôler aussi les flux sortants de la DMZ; un serveur public compromis ne doit pas obtenir un accès général à Internet ou aux services internes.
- Appliquer la même intention de cloisonnement à IPv4 et IPv6. Vérifier les routes, annonces, règles, NAT éventuelles et chemins alternatifs; ne pas supposer que l'absence de NAT signifie absence d'exposition.
- Distinguer plan de gestion, plan de données, réseau de stockage et trafic de cluster lorsque le rôle et la plateforme le justifient.
- Journaliser les refus significatifs et les autorisations sensibles, avec une rétention maîtrisée. Une règle de journalisation trop large peut produire du bruit, révéler des métadonnées ou consommer l'espace disque.
- Synchroniser l'heure, protéger les interfaces d'administration, appliquer les mises à jour et sauvegarder de manière chiffrée la configuration du pare-feu et les éléments nécessaires à sa restauration.

Les plages privées de RFC 1918 sont réutilisables à l'intérieur d'un réseau, mais ne constituent pas une mesure de sécurité ni une frontière de confiance. Éviter les chevauchements avec les réseaux VPN, partenaires, filiales ou environnements cloud.

## 5. Tester en laboratoire

Construire une maquette isolée avec au minimum un segment WAN simulé, une DMZ, un LAN de test et un pare-feu. Utiliser des services et des données fictifs; ne pas raccorder directement la maquette à un réseau tiers ou de production.

1. Sauvegarder la configuration initiale et consigner le plan d'adressage, le routage, les interfaces et la version du pare-feu.
2. Vérifier les flux attendus depuis chaque zone, y compris les ports, les initiateurs et les réponses de session.
3. Vérifier les refus : Internet vers LAN et administration, DMZ vers LAN hors exception, et sorties DMZ non requises.
4. Tester les mêmes attentes pour IPv4 et IPv6, la résolution DNS, les routes, le NAT éventuel et les chemins alternatifs.
5. Examiner les compteurs, journaux et captures du laboratoire pour confirmer quelle règle correspond au flux; vérifier qu'aucune règle plus générale ne le permet par ailleurs.
6. Après toute modification, refaire les tests positifs et négatifs, puis tester le retour à la configuration sauvegardée.

## 6. Mise en service et exploitation

Avant mise en service, faire relire la matrice de flux par les propriétaires applicatifs, réseau et sécurité. Prévoir une fenêtre de changement, une console ou un accès hors bande, une sauvegarde restaurable et un plan de retour arrière. Déployer progressivement et vérifier les services métier depuis des points de test autorisés.

À chaque revue périodique : supprimer les exceptions expirées, confirmer les propriétaires, vérifier les objets d'adresses et de ports, examiner les règles jamais utilisées, rechercher les changements d'architecture et contrôler la journalisation. Un compteur nul ne suffit pas à supprimer une règle sans validation du propriétaire.

## 7. Critères d'acceptation

- Chaque service publié a un propriétaire, une destination documentée et une exposition minimale.
- Les flux nécessaires fonctionnent et les flux interdits sont effectivement bloqués dans les deux familles IP.
- Les exceptions DMZ vers LAN sont spécifiques, justifiées et journalisées selon la politique.
- Aucun chemin de contournement (interface secondaire, route, VLAN mal configuré, accès d'administration public) n'est identifié.
- Les journaux, sauvegardes, versions, responsable de revue et procédure de retour arrière sont documentés.
- Les résultats du lab et les limites restant à traiter sont consignés; un essai en lab ne certifie pas à lui seul la production.

## Sources officielles

- [NIST SP 800-41 Rev. 1 — Guidelines on Firewalls and Firewall Policy](https://csrc.nist.gov/pubs/sp/800/41/r1/final) : document de référence publié en 2009; le compléter par les recommandations actuelles de l'organisation et du fournisseur.
- [NIST SP 800-207 — Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final) : principes d'accès centrés sur les ressources et le contexte, non un guide de configuration DMZ.
- [IETF RFC 1918 — Address Allocation for Private Internets](https://datatracker.ietf.org/doc/html/rfc1918) : espaces IPv4 privés et considérations d'interconnexion; ne définit pas la sécurité d'une DMZ.
- [OPNsense — Firewall rules](https://docs.opnsense.org/manual/firewall.html) et [aliases](https://docs.opnsense.org/manual/aliases.html) : documentation spécifique au produit, à vérifier selon sa version.
- [Proxmox VE — Firewall](https://pve.proxmox.com/pve-docs/chapter-pve-firewall.html) et [SDN](https://pve.proxmox.com/pve-docs/chapter-pvesdn.html) : fonctions et limites de la version documentée; le support du firewall au niveau VNet dépend notamment du backend et de l'état de support indiqué par Proxmox.
- [Référence pédagogique DMZ du dépôt nivvlem-TSSR](https://github.com/kipit/nivvlem-TSSR/blob/main/fiches-r%C3%A9f%C3%A9rences/dmz.md) : support complémentaire, non utilisé comme source normative.

## Fiche de contrôle

- [Valider les flux DMZ en laboratoire](/01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/fiches-par-theme/administration-systeme/fiche-simple-dmz-valider-flux-zone-lab)

La conception décrite ici n'a pas été testée sur un pare-feu réel. Adapter et faire approuver toute politique avant son déploiement.