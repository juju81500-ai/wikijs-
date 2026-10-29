---
title: "Fiche Simple - VM Alpine 3.19 Vie Systeme 17 Resolution De Noms Client"
description: "Configurer les serveurs DNS du client."
published: true
date: 2026-10-29T20:22:10Z
tags: ["alpine319", "vie-du-systeme", "cycle-de-vie", "etape-17"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Alpine_3.19_Vie_Systeme_17_Resolution_De_Noms_Client

- **Environnement** : VM Alpine Linux 3.19 (serveur)
- **OS / Version** : Alpine Linux 3.19; étape 17 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `alpine319`, `vie-du-systeme`, `cycle-de-vie`, `etape-17`

---

## Problème précis à résoudre

Configurer les serveurs DNS du client.

## 1. Hors-Production (Lab / Test / POC)

1. Définir les serveurs et le domaine de recherche (remplacer `DNS_IP` et `DOMAINE`) :
   ```sh
   setup-dns -d DOMAINE DNS_IP
   ```
   👉 Explication : écrit `/etc/resolv.conf` (`search DOMAINE`, `nameserver DNS_IP`); on peut passer deux serveurs séparés par un espace.

2. Vérifier le contenu et la résolution :
   ```sh
   cat /etc/resolv.conf
   nslookup dl-cdn.alpinelinux.org
   ```
   👉 Explication : BusyBox `nslookup` interroge le DNS configuré; une réponse avec adresse confirme le fonctionnement.

3. Tester avec les outils complets :
   ```sh
   doas apk add bind-tools
   dig +short dl-cdn.alpinelinux.org
   ```
   👉 Explication : `dig` donne les résultats et le temps de réponse.

## 2. Production — Contrôles

Utiliser au moins deux serveurs DNS internes.

## 3. Production — Sécurité

Ne pas utiliser un résolveur public inconnu pour les noms internes.

## Validation et retour arrière

- **Validation** : Un nom interne et un nom externe se résolvent.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Alpine Linux 3.19](/01-fiches-simples/alpine/3-19/vie-du-systeme/sommaire-vie-du-systeme-alpine-3-19)
- [Documentation officielle](https://docs.alpinelinux.org/)