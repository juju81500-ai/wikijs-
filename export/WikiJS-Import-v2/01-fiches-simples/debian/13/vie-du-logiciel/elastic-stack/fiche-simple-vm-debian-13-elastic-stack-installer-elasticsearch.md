---
title: "Fiche Simple - VM Debian 13 Elastic Stack Installer Elasticsearch"
description: "Installer Elasticsearch, démarrer le service et sécuriser l'accès à l'API HTTPS."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "elastic", "elasticsearch", "systemd", "tls"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_Elastic_Stack_Installer_Elasticsearch.md

- **Environnement** : Elasticsearch et Kibana sur Debian 13, nœud unique
- **OS / Version** : Debian 13; Elasticsearch et Kibana 9.5.x
- **Catégorie** : journalisation / elasticsearch
- **Tags** : `debian13`, `elastic`, `elasticsearch`, `systemd`, `tls`

---

## Problème précis à résoudre

Installer Elasticsearch, démarrer le service et sécuriser l'accès à l'API HTTPS.

## 1. Hors-Production (Lab / Test / POC)

1. Installer et démarrer le service :
   ```bash
   sudo apt-get install -y elasticsearch
   sudo systemctl daemon-reload
   sudo systemctl enable --now elasticsearch.service
   sudo systemctl --no-pager status elasticsearch
   ```
   👉 Explication : Au premier démarrage, la sécurité, les certificats TLS et le token Kibana sont générés automatiquement.

2. Définir le mot de passe du superutilisateur (saisi de façon interactive, jamais en argument) :
   ```bash
   sudo /usr/share/elasticsearch/bin/elasticsearch-reset-password -i -u elastic
   ```
   👉 Explication : L'option `-i` demande le mot de passe au clavier; le stocker dans le coffre de l'organisation.

3. Tester l'API HTTPS avec le certificat CA local :
   ```bash
   curl --cacert /etc/elasticsearch/certs/http_ca.crt -u elastic https://localhost:9200
   ```
   👉 Explication : `curl` demande le mot de passe; n'utiliser jamais `-k` qui désactive la vérification TLS.

## 2. Production — Contrôles

Régler `cluster.name` et `node.name`; garder les interfaces locales tant qu'un besoin réseau n'est pas approuvé.

## 3. Production — Sécurité

- Conserver certificats et secrets hors des journaux et du wiki.
- Ne pas désactiver la vérification TLS.

## Validation et retour arrière

- **Validation** : le service est `active (running)` et l'API répond en HTTPS avec le CA local.
- **Retour arrière** : `sudo systemctl disable --now elasticsearch.service`; supprimer le paquet seulement après sauvegarde des données.

## Si le problème n'est pas résolu

- [Elastic — paquet Debian Elasticsearch](https://www.elastic.co/docs/deploy-manage/deploy/self-managed/install-elasticsearch-with-debian-package)
- [Elastic — paquet Debian Kibana](https://www.elastic.co/docs/deploy-manage/deploy/self-managed/install-kibana-with-debian-package)
- [Guide complet Elastic_Stack Debian 13](/02-fiches-completes/debian/13/installation-deploiement/50-deploiement-elastic-stack-9-5-debian-13#3-installer-et-demarrer-elasticsearch)