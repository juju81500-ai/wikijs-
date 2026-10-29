---
title: "Fiche Simple - VM Debian 13 Elastic Stack Installer Kibana"
description: "Installer Kibana et le relier à Elasticsearch avec un enrollment token."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "elastic", "kibana", "enrollment", "tls"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_Elastic_Stack_Installer_Kibana.md

- **Environnement** : Elasticsearch et Kibana sur Debian 13, nœud unique
- **OS / Version** : Debian 13; Elasticsearch et Kibana 9.5.x
- **Catégorie** : journalisation / kibana
- **Tags** : `debian13`, `elastic`, `kibana`, `enrollment`, `tls`

---

## Problème précis à résoudre

Installer Kibana et le relier à Elasticsearch avec un enrollment token.

## 1. Hors-Production (Lab / Test / POC)

1. Installer et démarrer Kibana :
   ```bash
   sudo apt-get install -y kibana
   sudo systemctl daemon-reload
   sudo systemctl enable kibana.service
   sudo systemctl start kibana.service
   sudo systemctl --no-pager status kibana
   ```
   👉 Explication : Installe le paquet de même version et lance le service.

2. Générer un enrollment token Kibana sur Elasticsearch :
   ```bash
   sudo /usr/share/elasticsearch/bin/elasticsearch-create-enrollment-token -s kibana
   ```
   👉 Explication : Le token expire; en regénérer un s'il n'est plus valide.

3. Obtenir le code de vérification affiché par Kibana :
   ```bash
   sudo /usr/share/kibana/bin/kibana-verification-code
   ```
   👉 Explication : À saisir dans le wizard Kibana avec le token, via **http://localhost:5601**.

4. Contrôler l'écoute de Kibana :
   ```bash
   sudo ss -tlnp | grep ':5601'
   ```
   👉 Explication : `server.host` doit rester en localhost avec un proxy local; sinon lier une adresse interne dédiée.

## 2. Production — Contrôles

Contrôler TLS/proxy et pare-feu avant toute ouverture réseau de Kibana.

## 3. Production — Sécurité

- Ne pas coller le token dans un ticket ou un journal.
- Limiter l'accès à Kibana aux administrateurs.

## Validation et retour arrière

- **Validation** : Kibana s'ouvre, l'enrôlement réussit et la connexion `elastic` fonctionne.
- **Retour arrière** : `sudo systemctl disable --now kibana.service`.

## Si le problème n'est pas résolu

- [Elastic — paquet Debian Elasticsearch](https://www.elastic.co/docs/deploy-manage/deploy/self-managed/install-elasticsearch-with-debian-package)
- [Elastic — paquet Debian Kibana](https://www.elastic.co/docs/deploy-manage/deploy/self-managed/install-kibana-with-debian-package)
- [Guide complet Elastic_Stack Debian 13](/02-fiches-completes/debian/13/installation-deploiement/50-deploiement-elastic-stack-9-5-debian-13#4-installer-et-enroler-kibana)