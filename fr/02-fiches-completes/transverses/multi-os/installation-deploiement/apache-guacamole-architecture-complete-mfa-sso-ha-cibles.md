---
title: "Architecture complète Apache Guacamole : MFA, SSO, haute disponibilité et connexions cibles"
description: "- Prolonge la fiche de base [Déploiement Apache Guacamole 1.6 Docker](../../docker/installation-deploiement/121-deploiement-apache-guacamole-1-6-docker.md), qu'il faut avoir réalisée ou lue : instance simple avec PostgreSQL, guacd et reverse proxy. Aucun de ses contenus n'est répété ici."
published: true
date: 2026-11-03T09:36:14Z
tags: ["guacamole", "mfa", "sso", "ha", "rdp", "ssh", "bastion"]
editor: markdown
dateCreated: 2026-11-03T09:36:14Z
dateModified: 2026-11-03T09:36:14Z
---

# Architecture complète Apache Guacamole : MFA, SSO, haute disponibilité et connexions cibles

- **OS / Version** : Apache Guacamole 1.6.0 (version utilisée par la fiche Docker existante) ; Linux, conteneurs
- **Type de fiche** : Installation/Déploiement
- **Périmètre** : Extension de l'architecture : MFA, SSO, redondance, connexions RDP/SSH/VNC vers des cibles autorisées
- **Catégorie** : Accès distant / bastion
- **Tags** : `guacamole`,`mfa`,`sso`,`ha`,`rdp`,`ssh`,`bastion`

## 1. Portée, hypothèses et licences

- Prolonge la fiche de base [Déploiement Apache Guacamole 1.6 Docker](/fr/02-fiches-completes/transverses/docker/installation-deploiement/121-deploiement-apache-guacamole-1-6-docker), qu'il faut avoir réalisée ou lue : instance simple avec PostgreSQL, guacd et reverse proxy. Aucun de ses contenus n'est répété ici.
- Apache Guacamole est sous licence Apache 2.0 ; l'éventuel fournisseur d'identité ou de MFA est sous sa propre licence.
- Toute action décrite ici s'exécute uniquement sur des systèmes que vous possédez ou pour lesquels vous disposez d'une autorisation écrite (périmètre, dates, contacts). Les connexions vers des cibles ne sont créées que pour des machines autorisées.
- Les noms de variables et d'extensions ci-dessous sont tirés du manuel 1.6.0 ; les confirmer sur la version déployée.

## 2. Architecture cible

```
Utilisateur -> Reverse proxy HTTPS (WAF/LB) -> Guacamole web (n instances)
                                              -> PostgreSQL (primaire + réplique)
                                              -> guacd (n instances) -> cibles RDP/SSH/VNC
IdP (SAML/OpenID) <-> Guacamole web
```

- Les couches web et guacd peuvent être multipliées. La base PostgreSQL est le point d'état unique : sa redondance relève de PostgreSQL (réplication, Patroni, service managé).
- Les sessions HTTP sont locales à chaque instance : prévoir l'affinité de session (sticky) au niveau du répartiteur ou valider un test de bascule.

## 3. Prérequis

- Environnement de la fiche 121 opérationnel et sauvegardé ; clone de test pour les changements.
- Un IdP compatible OpenID Connect ou SAML 2.0 ; une application TOTP pour le MFA local.
- Cibles de laboratoire autorisées (VM Windows RDP, Linux SSH) dans un réseau segmenté.

## 4. MFA (TOTP)

1. Activer l'extension TOTP fournie avec la même version que le serveur (variable d'environnement `TOTP_ENABLED=true` dans l'image Docker officielle, ou fichier JAR dans le dossier `extensions` de Guacamole).
2. Redémarrer le service web, puis vérifier dans les journaux le chargement de l'extension.
3. À la première connexion d'un utilisateur de test, enregistrer le code QR dans l'application d'authentification.
4. Documenter la procédure de réinitialisation du MFA et réserver un compte de secours protégé.

## 5. SSO (OpenID Connect ou SAML)

1. Créer dans l'IdP une application dont l'URI de redirection est celle de Guacamole en HTTPS.
2. Renseigner la configuration de l'extension OpenID (variables `OPENID_AUTHORIZATION_ENDPOINT`, `OPENID_JWKS_ENDPOINT`, `OPENID_ISSUER`, `OPENID_CLIENT_ID`, `OPENID_REDIRECT_URI`) ou SAML (extension SAML, métadonnées de l'IdP, identifiant d'entité, URL de callback) selon le manuel de la version.
3. Gérer l'ordre des extensions (`EXTENSION_PRIORITY`) pour conserver l'authentification JDBC comme secours.
4. Les droits sur les connexions restent dans la base Guacamole : prévoir le provisionnement des utilisateurs/groupes correspondants (un utilisateur SSO peut ne pas avoir de permission tant qu'ils ne sont pas créés).
5. Tester avec un utilisateur non administrateur ; vérifier que la déconnexion et l'expiration de session sont conformes à la politique.

## 6. Haute disponibilité

1. Base de données : mettre en place la réplication PostgreSQL et un mécanisme de bascule documenté ; tester la restauration.
2. Web : au moins deux conteneurs Guacamole derrière un répartiteur avec contrôle de santé HTTP et affinité de session.
3. guacd : plusieurs instances ; chaque instance web pointe vers sa cible guacd (variable `GUACD_HOSTNAME`) ou via un répartiteur TCP. Les sessions en cours sont perdues lors de la perte d'une instance guacd : informer les utilisateurs.
4. Reverse proxy : redondance avec adresse virtuelle ou DNS selon l'infrastructure ; certificats gérés de façon centrale.
5. Sauvegardes : base, configuration, extensions et certificats, restauration testée.

## 7. Connexions cibles

- Créer les connexions dans l'interface (Paramètres > Connexions) avec le protocole, le nom d'hôte, le port, l'utilisateur ; ne pas enregistrer de mots de passe partagés : préférer la saisie utilisateur ou un coffre.
- RDP : préférer la sécurité NLA et des certificats valides ; n'activer « ignorer le certificat » qu'en lab, avec une note de risque.
- SSH : utiliser des clés et restreindre les comptes ; désactiver le transfert de fichiers et le presse-papiers si la politique l'exige.
- Segmentation : guacd n'atteint que les cibles prévues par pare-feu ; journaliser les accès et activer l'enregistrement de session seulement si la base légale et l'information des utilisateurs le permettent.

## 8. Validation

- Connexion locale avec TOTP ; connexion SSO ; compte de secours fonctionnel.
- Arrêt d'une instance web : la session reprend (ou une reconnexion propre est constatée) ; arrêt d'une guacd : les nouvelles connexions passent par l'autre.
- Bascule de la base testée sur le laboratoire ; aucun port interne (PostgreSQL, guacd, Tomcat) n'est exposé.
- Les connexions cibles pilotes fonctionnent, et les accès interdits sont bloqués.

## 9. Retour arrière

Retirer l'extension (variable ou JAR) et redémarrer pour revenir à l'authentification de base ; restaurer la configuration Compose et la base sauvegardée sur le clone ; réactiver l'ancienne configuration du reverse proxy ; supprimer l'application SSO de l'IdP si l'essai est abandonné. Conserver l'accès du compte de secours pendant toute la période de changement.

## Sources officielles

- [Guacamole — manuel 1.6.0](https://guacamole.apache.org/doc/gug/)
- [Authentification TOTP](https://guacamole.apache.org/doc/gug/totp-auth.html)
- [Authentification OpenID Connect](https://guacamole.apache.org/doc/gug/openid-auth.html)
- [Authentification SAML](https://guacamole.apache.org/doc/gug/saml-auth.html)
- [Guacamole avec Docker](https://guacamole.apache.org/doc/gug/guacamole-docker.html)

Aucun cluster Guacamole n'a été exécuté pendant la rédaction ; le comportement de bascule, les variables et les extensions doivent être validés sur la version déployée.

## Historique

| Date | Version | Changement | Statut de test |
|---|---|---|---|
| 2026-10-31 | 1.0 | Création de la fiche à partir de la documentation éditeur | Non testé sur plateforme cible |