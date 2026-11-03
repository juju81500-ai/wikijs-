---
title: "Kali Linux et Parrot OS : laboratoire défensif isolé"
description: "- Ces distributions contiennent des outils d'audit pouvant être illégaux ou dommageables s'ils sont utilisés sans autorisation. Toute action décrite ici s'exécute uniquement sur des systèmes que vous possédez ou pour lesquels vous disposez d'une autorisation écrite (périmètre, dates, contacts). L'us"
published: true
date: 2026-11-03T09:36:14Z
tags: ["kali", "parrot", "laboratoire", "blue-team", "isolation"]
editor: markdown
dateCreated: 2026-11-03T09:36:14Z
dateModified: 2026-11-03T09:36:14Z
---

# Kali Linux et Parrot OS : laboratoire défensif isolé

- **OS / Version** : Kali Linux et Parrot Security (VM de laboratoire)
- **Type de fiche** : Installation/Déploiement
- **Périmètre** : Poste de laboratoire isolé pour valider ses propres détections et durcissements, sans usage hors lab
- **Catégorie** : Laboratoire cybersécurité
- **Tags** : `kali`,`parrot`,`laboratoire`,`blue-team`,`isolation`

## 1. Portée, hypothèses et licences

- Ces distributions contiennent des outils d'audit pouvant être illégaux ou dommageables s'ils sont utilisés sans autorisation. Toute action décrite ici s'exécute uniquement sur des systèmes que vous possédez ou pour lesquels vous disposez d'une autorisation écrite (périmètre, dates, contacts). L'usage est limité à un réseau de laboratoire isolé, jamais sur le réseau de production ni sur Internet.
- Objectif défensif : générer des événements contrôlés pour vérifier la détection (SIEM, EDR, journaux), contrôler le durcissement de cibles de lab, et former les équipes.
- Licences : distributions libres avec des outils sous licences diverses ; consulter les conditions de chaque outil.
- Interdit : analyse de réseaux tiers, attaque de comptes réels, déploiement sur un poste de travail de production. Les profils des équipes sont signalés dans la charte d'usage.

## 2. Prérequis

- Hyperviseur du lab, réseau virtuel dédié (host-only ou interne) sans passerelle vers la production.
- Autorisation écrite interne précisant plage d'adresses du lab, durées et responsable.
- Machines cibles de lab (VM sacrifiables) et collecteur de journaux dans le même réseau isolé.
- Images officielles et sommes de contrôle.

## 3. Obtenir et vérifier l'image

1. Télécharger l'image VM ou ISO sur le site officiel de la distribution (Kali : page de téléchargement ; Parrot : page de téléchargement de l'édition Security).
2. Vérifier l'intégrité : somme SHA-256 publiée et, si fournie, la signature de la liste des sommes :

```bash
sha256sum kali-linux-*.7z
sha256sum -c SHA256SUMS --ignore-missing
gpg --verify SHA256SUMS.gpg SHA256SUMS
```

Récupérer la clé de signature depuis la source officielle de la distribution et vérifier son empreinte par un second canal.

## 4. Mise en place de la VM

1. Créer la VM, connecter uniquement l'interface au réseau isolé ; désactiver partage de presse-papiers et dossiers partagés avec l'hôte.
2. Changer les identifiants par défaut de l'image préconstruite dès le premier démarrage.
3. Prendre un instantané « propre ».
4. Mettre à jour pendant une fenêtre contrôlée, avec accès temporaire à un miroir interne si possible :

```bash
sudo apt update
sudo apt full-upgrade
```

5. Installer les seuls ensembles d'outils nécessaires plutôt que la collection complète : la distribution propose des méta-paquets (par exemple `kali-tools-top10` côté Kali) ; vérifier leur existence avec `apt-cache search kali-tools` et la liste côté Parrot via son gestionnaire de paquets.

## 5. Scénarios défensifs autorisés

- Générer un événement connu (tentative de connexion SSH échouée sur une cible de lab) et confirmer qu'il apparaît dans le SIEM.
- Vérifier les ports exposés d'une cible de lab avec un scanner de ports, puis comparer à la politique de pare-feu.
- Rejouer des tests de détection documentés dans un catalogue de techniques, sur des cibles de lab seulement.
- Chaque scénario consigne : cible, heure, commande, résultat attendu, alerte observée.

## 6. Validation

- L'interface réseau de la VM ne joint aucun réseau externe (test d'accès vers une adresse de production : échec attendu).
- L'instantané propre se restaure ; les identifiants par défaut sont changés.
- Les événements générés sont détectés ; les écarts sont notés dans un ticket d'amélioration.
- Journal des activités conservé.

## 7. Retour arrière

Restaurer l'instantané propre après chaque campagne, ou détruire la VM. Supprimer les captures et les résultats contenant des données sensibles selon la politique de rétention ; retirer les règles de pare-feu temporaires du lab.

## Sources officielles

- [Kali Linux — documentation](https://www.kali.org/docs/)
- [Kali — vérification des images](https://www.kali.org/docs/introduction/download-images-securely/)
- [Kali — méta-paquets](https://www.kali.org/docs/general-use/metapackages/)
- [Parrot — documentation](https://parrotsec.org/docs/)

Aucune VM Kali ou Parrot n'a été installée ni utilisée pendant la rédaction.

## Historique

| Date | Version | Changement | Statut de test |
|---|---|---|---|
| 2026-10-31 | 1.0 | Création de la fiche à partir de la documentation éditeur | Non testé sur plateforme cible |