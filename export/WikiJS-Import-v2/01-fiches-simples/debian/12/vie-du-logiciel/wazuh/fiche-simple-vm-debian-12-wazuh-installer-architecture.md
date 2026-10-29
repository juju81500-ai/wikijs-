---
title: "Fiche Simple - VM Debian 12 Wazuh Installer Architecture"
description: "Déployer les composants Wazuh en suivant les procédures officielles correspondant exactement à la version et à l'architecture choisies."
published: true
date: 2026-10-29T19:55:10Z
tags: ["debian12", "wazuh", "siem", "installation", "tls"]
editor: markdown
dateCreated: 2026-10-29T19:55:10Z
dateModified: 2026-10-29T19:55:10Z
---

# Fiche_Simple_-_VM_Debian_12_Wazuh_Installer_Architecture.md

- **Environnement** : Debian 12; Wazuh manager, indexer et dashboard selon architecture validée
- **OS / Version** : version Wazuh 4.x maintenue depuis les sources officielles
- **Catégorie** : SIEM/XDR / déploiement
- **Tags** : `debian12`, `wazuh`, `siem`, `installation`, `tls`

---

## Problème précis à résoudre

Déployer les composants Wazuh en suivant les procédures officielles correspondant exactement à la version et à l'architecture choisies.

## 1. Hors-Production (Lab / Test / POC)

1. Télécharger l'assistant exact de la version retenue (remplacer `4.X`) :
   ```bash
   cd /tmp
   curl -fsSLO https://packages.wazuh.com/4.X/wazuh-install.sh
   curl -fsSLO https://packages.wazuh.com/4.X/config.yml
   ```
   👉 Explication : n'utiliser que le domaine officiel; relever la version correspondante dans la documentation.

2. Lire le script avant exécution et contrôler la somme/signature publiée :
   ```bash
   less wazuh-install.sh
   sha256sum wazuh-install.sh
   ```
   👉 Explication : comparer à la valeur publiée par Wazuh si disponible.

3. Lab : installation all-in-one :
   ```bash
   sudo bash ./wazuh-install.sh -a
   ```
   👉 Explication : la production utilise les procédures multi-nœuds et certificats dédiés; ne pas convertir un lab en HA par clonage.

4. Récupérer et ranger les mots de passe générés :
   ```bash
   sudo tar -O -xf wazuh-install-files.tar wazuh-install-files/wazuh-passwords.txt
   ```
   👉 Explication : les placer dans un coffre, jamais dans les logs ni dans le dépôt documentaire; supprimer ensuite l'archive de `/tmp`.

5. Vérifier les services :
   ```bash
   systemctl --no-pager status wazuh-manager wazuh-indexer wazuh-dashboard
   ```
   👉 Explication : les trois doivent être `active (running)`.

## 2. Production — Contrôles

Valider la version, les sources, la signature, l'architecture, la procédure d'installation, les certificats et l'inventaire des composants.

## 3. Production — Sécurité

- Ne pas exécuter un script distant non vérifié avec privilèges root.
- Ne pas réutiliser les secrets générés entre environnements.
- Ne pas committer certificats, clés privées, mots de passe ou logs d'installation sensibles.
- Ne pas transformer un nœud de lab en cluster HA par clonage improvisé.

## Validation et retour arrière

- **Validation** : composants conformes à l'architecture, certificats protégés et journaux sans erreur critique.
- **Retour arrière** : conserver les versions/configurations précédentes et suivre la procédure officielle de désinstallation/reprise.

## Si le problème n'est pas résolu

- [Wazuh — installation](https://documentation.wazuh.com/current/installation-guide/index.html)
- [Wazuh — déploiement](https://documentation.wazuh.com/current/deployment-options/index.html)
- [Guide complet Wazuh Debian 12](/02-fiches-completes/debian/12/installation-deploiement/11-siem-xdr-centralise-wazuh-4x-debian-12)