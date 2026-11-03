---
title: "Cadrer et durcir un pare-feu FortiGate, Palo Alto, Cisco ASA/Firepower ou Stormshield"
description: "Fiche de cadrage défensif multi-appliance : identifier la variante, préparer l'accès d'administration, sauvegarder, appliquer une politique de base, journaliser et prévoir le retour arrière. Elle ne remplace pas le guide du constructeur et ne fournit pas de syntaxe CLI unique : chaque famille a sa p"
published: true
date: 2026-11-03T09:36:14Z
tags: ["fortigate", "fortios", "pan-os", "palo-alto", "cisco-asa", "firepower", "stormshield", "durcissement"]
editor: markdown
dateCreated: 2026-11-03T09:36:14Z
dateModified: 2026-11-03T09:36:14Z
---

# Cadrer et durcir un pare-feu FortiGate, Palo Alto, Cisco ASA/Firepower ou Stormshield

- **OS / Version** : FortiOS, PAN-OS, Cisco ASA / Secure Firewall (FTD/FMC), Stormshield SNS — versions à préciser
- **Type de fiche** : Installation/Déploiement
- **Environnement** : Appliances physiques ou virtuelles, laboratoire puis production
- **Machine ciblée** : Pare-feu périmétrique / interne
- **Catégorie** : Sécurité réseau / pare-feu
- **Tags** : `fortigate`, `fortios`, `pan-os`, `palo-alto`, `cisco-asa`, `firepower`, `stormshield`, `durcissement`

## 1. Périmètre

Fiche de cadrage défensif multi-appliance : identifier la variante, préparer l'accès d'administration, sauvegarder, appliquer une politique de base, journaliser et prévoir le retour arrière. Elle ne remplace pas le guide du constructeur et ne fournit pas de syntaxe [[Glossary:CLI]] unique : chaque famille a sa propre interface.

## 2. Prérequis

- Modèle, version exacte du firmware et licence/support actifs (abonnements de sécurité éventuels).
- Accès console hors bande ou fenêtre de maintenance avec accès physique/virtuel de secours.
- Inventaire des zones, flux autorisés, plan d'adressage, serveurs [[Glossary:NTP]], syslog et annuaire d'authentification.
- Compte nominatif d'administration, [[Glossary:MFA]] si pris en charge, secrets dans un coffre.
- Laboratoire ou appliance virtuelle de test pour valider chaque changement.
- Produit commercial : la console, les droits d'accès au portail éditeur et la licence sont des prérequis. Aucune commande générique n'est donnée quand elle dépend de la console ou de la version; suivre la documentation de la version exacte.

## 3. Variantes éditeur à distinguer

| Famille | Système | Gestion principale | Point d'attention |
|---|---|---|---|
| Fortinet | FortiOS (FortiGate) | [[Glossary:GUI]] web, CLI FortiOS, FortiManager en option | Fonctions UTM/IPS liées aux abonnements FortiGuard |
| Palo Alto | PAN-OS | GUI web, CLI PAN-OS, Panorama en option | Modèle « candidate/commit » : rien n'est actif avant le commit |
| Cisco ASA | ASA software | CLI ASA, ASDM | ASA seul ne porte pas les fonctions IPS Firepower |
| Cisco Firepower | Secure Firewall Threat Defense (FTD) | Secure Firewall Management Center (FMC) ou gestionnaire local selon modèle | Déploiement de politiques depuis la console de gestion |
| Stormshield | SNS | Interface web d'administration, CLI/SSH | Politique de sécurité à activer explicitement; haute disponibilité par paire |

Ne pas transposer une commande d'une famille à l'autre.

## 4. Étapes vérifiables

### 4.1 Inventorier et choisir la variante

Relever pour chaque équipement : modèle, version, mode de gestion (local ou centralisé), licences, rôle (périmètre, interne, [[Glossary:VPN]]). Consulter la matrice de compatibilité et les notes de version de l'éditeur avant toute mise à jour.

### 4.2 Sécuriser l'administration

Dans la console de la famille concernée : restreindre l'accès de gestion à un réseau/une interface d'administration dédiée, imposer HTTPS et [[Glossary:SSH]] uniquement, désactiver les protocoles en clair (Telnet, [[Glossary:HTTP]]), créer des comptes nominatifs avec profils à moindre privilège, configurer une bannière légale et un délai d'expiration de session. Remplacer les identifiants par défaut.

### 4.3 Sauvegarder avant changement

Exporter la configuration par la fonction officielle de la console (sauvegarde de configuration, snapshot ou export de politique selon produit), chiffrer le fichier et le stocker hors de l'équipement. Noter le numéro de version et la somme de contrôle.

### 4.4 Appliquer une politique de base

Définir zones et interfaces, une règle finale de refus avec journalisation, des règles explicites par flux métier, la translation d'adresses documentée, et l'inspection (IPS, filtrage web, antimalware) uniquement si la licence la couvre. Appliquer d'abord en laboratoire, puis en production en fenêtre de maintenance.

### 4.5 Journalisation et temps

Configurer NTP, l'envoi syslog vers le collecteur et, si besoin, SNMPv3 (pas v1/v2c). Vérifier le fuseau horaire et la rétention locale.

### 4.6 Haute disponibilité et mises à jour

Documenter le mode de haute disponibilité propre à la famille, tester le basculement en laboratoire et mettre à jour d'abord le nœud secondaire selon la procédure éditeur.

## 5. Validation

- Accès d'administration possible uniquement depuis le réseau prévu; test d'accès refusé depuis un autre segment.
- Les flux autorisés fonctionnent et les flux interdits sont journalisés.
- Les journaux arrivent au collecteur avec l'heure correcte.
- Une sauvegarde de configuration a été restaurée avec succès sur un équipement de test.
- Basculement HA testé si la haute disponibilité est en place.

## 6. Retour arrière

- Revenir à la sauvegarde de configuration pré-changement via la console de la famille.
- Sur PAN-OS, ne pas valider (commit) tant que le test n'est pas concluant, ou charger la configuration précédente; sur les autres familles, utiliser les mécanismes d'annulation/rollback officiels de la version.
- Conserver l'accès console pour récupérer un équipement inaccessible après erreur de règle de gestion.

## 7. Limites de version et de licence

- Les fonctions, noms de menus et options changent d'une version à l'autre : se référer à la documentation de la version installée.
- Les fonctions de sécurité avancées dépendent des licences et abonnements.
- Une mise à jour majeure exige de vérifier le chemin de montée de version publié par l'éditeur.
- Aucune configuration d'exemple n'est fournie : elle doit être adaptée au plan d'adressage réel.

## 8. Verdict historique

**Non testé sur plateforme cible.** Cette fiche est une synthèse documentaire des sources officielles; aucune exécution n'a été réalisée sur les produits, versions ou licences visés. Valider en laboratoire isolé avant production.

## Sources

- [Fortinet Docs — FortiOS](https://docs.fortinet.com/product/fortigate)
- [Palo Alto Networks — documentation PAN-OS](https://docs.paloaltonetworks.com/pan-os)
- [Cisco — Secure Firewall ASA](https://www.cisco.com/c/en/us/support/security/adaptive-security-appliance-asa-software/series.html)
- [Cisco — Secure Firewall Threat Defense](https://www.cisco.com/c/en/us/support/security/firepower-ngfw/series.html)
- [Stormshield — documentation](https://documentation.stormshield.eu/)