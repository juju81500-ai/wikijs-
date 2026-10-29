---
title: "Déployer Bitwarden self-hosted sur Linux avec Docker"
description: "Fiche simple : [cadrer l'auto-hébergement](../../../../01-Fiches-Simples/Transverses/Docker/Bitwarden/FicheSimple-BitwardenSelfHostedDeploiementCadrerAutoHebergement.md)."
published: true
date: 2026-10-29T19:43:58Z
tags: ["bitwarden", "self-hosted", "docker", "linux", "tls", "secrets", "backup"]
editor: markdown
dateCreated: 2026-10-29T19:43:58Z
dateModified: 2026-10-29T19:43:58Z
---

# Déployer Bitwarden self-hosted sur Linux avec Docker

- **OS / Version** : Linux x86-64 supporté; Docker Engine 26+ et Compose; version Bitwarden courante validée
- **Type de fiche** : Installation/Déploiement
- **Périmètre** : Déploiement standard Bitwarden individuel/organisation, hors mode offline
- **Catégorie** : Coffre de mots de passe et partage sécurisé
- **Tags** : `bitwarden`, `self-hosted`, `docker`, `linux`, `tls`, `secrets`, `backup`

## 1. Cadrer l'auto-hébergement

Fiche simple : [cadrer l'auto-hébergement](/01-fiches-simples/transverses/docker/bitwarden/fiche-simple-bitwarden-self-hosted-deploiement-cadrer-auto-hebergement).

Comparer le besoin avec Bitwarden SaaS et vérifier les exigences de licence pour les fonctionnalités d'organisation. Prévoir un FQDN dédié, TLS valide, SMTP, stockage persistant, supervision, sauvegarde hors hôte et procédure de mise à jour. La procédure standard utilise une base MSSQL Express intégrée, limitée par ses spécifications; utiliser une base externe seulement selon les instructions Bitwarden.

Le guide Bitwarden annonce pour le déploiement standard 2 vCPU/4 Go de RAM et 12/25 Go de stockage minimum/recommandé; dimensionner davantage selon comptes, pièces jointes, sauvegardes et journalisation. Ne pas exposer l'administration Docker ni l'interface d'administration de Bitwarden sur Internet.

## 2. Préparer Linux et Docker

Fiche simple : [préparer Linux et Docker](/01-fiches-simples/transverses/docker/bitwarden/fiche-simple-bitwarden-self-hosted-deploiement-preparer-linux-docker).

Installer une distribution Linux supportée, corriger le système, configurer DNS/NTP et Docker Engine 26+ avec Compose. Prévoir un compte local `bitwarden` et un chemin persistant `/opt/bitwarden`, protégé par des permissions strictes.

Attention : appartenir au groupe `docker` confère généralement des privilèges équivalents à root sur l'hôte. Appliquer le modèle d'accès Docker approuvé et ne pas autoriser des utilisateurs ordinaires à contrôler le socket.

## 3. Télécharger et installer Bitwarden

Fiche simple : [télécharger et installer Bitwarden](/01-fiches-simples/transverses/docker/bitwarden/fiche-simple-bitwarden-self-hosted-deploiement-telecharger-installer).

Créer le compte de service et le répertoire conformément au guide officiel. Télécharger `bitwarden.sh` depuis l'URL officielle Bitwarden, enregistrer le fichier, contrôler son contenu et sa provenance, puis l'exécuter sous le compte `bitwarden` depuis `/opt/bitwarden`; ne pas le lancer avec root et ne pas le passer directement dans un shell depuis le réseau.

Lancer l'assistant d'installation et fournir le FQDN, l'option certificat (Let's Encrypt si les prérequis publics/ACME sont réunis, sinon certificat d'entreprise), l'installation ID et la clé obtenus dans le portail officiel, puis la région appropriée. Les identifiants sont sensibles : les transmettre depuis le coffre, éviter leur historique et ne pas les archiver dans la fiche.

## 4. Configurer la messagerie et l'organisation

Fiche simple : [configurer la messagerie et l'organisation](/01-fiches-simples/transverses/docker/bitwarden/fiche-simple-bitwarden-self-hosted-deploiement-configurer-messagerie-organisation).

Configurer SMTP dans `bwdata/env/global.override.env` pour les invitations et validations de compte. Si une organisation self-hosted est nécessaire, créer/lier la licence organisation selon les règles Bitwarden; régler explicitement inscription publique, communication cloud, rôles, collections, SSO/MFA et policy avant d'inviter les utilisateurs.

Appliquer les modifications par les commandes `restart` ou `rebuild` de l'installateur selon le type de configuration. Garder HTTP/HTTPS cohérent sur l'ensemble du déploiement et confirmer TLS pour l'accès client.

## 5. Démarrer et vérifier

Fiche simple : [démarrer et vérifier](/01-fiches-simples/transverses/docker/bitwarden/fiche-simple-bitwarden-self-hosted-deploiement-demarrer-verifier).

```bash
sudo -iu bitwarden /opt/bitwarden/bitwarden.sh start
sudo -iu bitwarden docker ps
```

Ouvrir `https://<fqdn>` depuis un poste pilote, vérifier le certificat, inscrire un compte de test, se connecter depuis un client approuvé et valider synchronisation/import de test et invitations SMTP. Ne jamais tester avec des secrets réels avant d'avoir validé sauvegarde et restauration.

## 6. Sauvegardes, mises à jour et reprise

Fiche simple : [sauvegardes, mises à jour et reprise](/01-fiches-simples/transverses/docker/bitwarden/fiche-simple-bitwarden-self-hosted-deploiement-sauvegardes-mises-a-jour-reprise).

Sauvegarder intégralement `bwdata`, notamment `env`, pièces jointes, base MSSQL, certificats et secrets de configuration, vers une destination chiffrée hors hôte. Bitwarden effectue des sauvegardes nocturnes de la base intégrée si son conteneur tourne, mais cela ne remplace pas la sauvegarde complète.

Tester une restauration sur un hôte/réseau isolé, sans DNS public ni clients utilisateurs. Mettre à jour avec la procédure officielle et une fenêtre contrôlée; conserver le précédent état de configuration et la sauvegarde avant migration de schéma. Contrôler les logs et la santé des conteneurs après chaque opération.

## Sources

- [Bitwarden — Déploiement Linux standard](https://bitwarden.com/help/install-on-premise-linux/)
- [Bitwarden — Héberger une organisation](https://bitwarden.com/help/self-host-an-organization/)
- [Bitwarden — Sauvegarder le serveur](https://bitwarden.com/help/backup-on-premise/)
- [Bitwarden — Mise à jour du serveur](https://bitwarden.com/help/updating-on-premise/)
- [Bitwarden — Exigences réseau](https://bitwarden.com/help/networking-requirements/)