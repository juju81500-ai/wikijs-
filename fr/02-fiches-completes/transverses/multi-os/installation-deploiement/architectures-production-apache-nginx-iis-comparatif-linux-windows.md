---
title: "Architectures de production Apache, Nginx et IIS : fiche comparative Linux/Windows"
description: "- Fiche de comparaison et d'architecture, qui complète sans les remplacer : [Apache HTTP Server sur Debian 13](../../../debian/13/installation-deploiement/124-deploiement-apache-http-server-debian-13.md), [pile LEMP Nginx sur Debian 13](../../../debian/13/installation-deploiement/02-pile-lemp-debian"
published: true
date: 2026-11-03T14:22:29Z
tags: ["apache", "nginx", "iis", "reverse-proxy", "tls", "production"]
editor: markdown
dateCreated: 2026-11-03T14:22:29Z
dateModified: 2026-11-03T14:22:29Z
---

# Architectures de production Apache, Nginx et IIS : fiche comparative Linux/Windows

- **OS / Version** : Linux (Debian/Ubuntu/RHEL) et Windows Server
- **Type de fiche** : Installation/Déploiement
- **Périmètre** : Choix d'architecture, durcissement, [[Glossary:TLS]], reverse proxy, haute disponibilité, exploitation
- **Catégorie** : Serveurs web
- **Tags** : `apache`,`nginx`,`iis`,`reverse-proxy`,`tls`,`production`

## 1. Portée, hypothèses et licences

- Fiche de comparaison et d'architecture, qui complète sans les remplacer : [Apache HTTP Server sur Debian 13](/fr/02-fiches-completes/debian/13/installation-deploiement/124-deploiement-apache-http-server-debian-13), [pile LEMP Nginx sur Debian 13](/fr/02-fiches-completes/debian/13/installation-deploiement/02-pile-lemp-debian-13-nginx-php-mariadb) et [IIS sur Windows Server 2022](/fr/02-fiches-completes/windows/server-2022/installation-deploiement/122-installation-iis-windows-server-2022). Les procédures d'installation s'y trouvent.
- Licences : Apache [[Glossary:HTTP]] Server (Apache 2.0) et Nginx (licence [[Glossary:BSD]] à deux clauses pour la version open source ; une offre commerciale existe) sont libres ; [[Glossary:IIS]] est un rôle de Windows Server, licencié avec Windows Server.
- Hypothèses : application déjà identifiée, exigences de disponibilité et de sécurité connues, environnement de préproduction disponible.

## 2. Critères de choix

| Critère | Apache | Nginx | IIS |
|---|---|---|---|
| Modèle | Processus/threads, modules MPM | Événementiel | Pool d'applications, modules natifs et managés |
| Configuration | Fichiers texte, `.htaccess` facultatif | Fichiers texte | Console, `applicationHost.config`, PowerShell |
| Atouts usuels | Flexibilité de modules, hérité large | Reverse proxy, fichiers statiques | .NET/ASP.NET, intégration [[Glossary:AD]] |
| Usage fréquent | Web applicatif PHP, mod_* | Frontal, répartiteur | Applications Windows |

Aucune de ces valeurs n'est une mesure de performance : les performances se mesurent sur votre charge.

## 3. Architectures de référence

1. **Instance unique** : réservée au développement et aux services peu critiques.
2. **Frontal + applicatif** : un reverse proxy (Nginx, Apache ou IIS avec Application Request Routing) termine le TLS et relaie vers des serveurs applicatifs en réseau privé.
3. **Cluster redondant** : au moins deux nœuds derrière un répartiteur (matériel, logiciel, [[Glossary:DNS]]) avec contrôles de santé, sessions sans état ou persistantes, contenu synchronisé par déploiement automatisé et non par copie manuelle.
4. **Zone [[Glossary:DMZ]]** : frontal en DMZ, applicatif et base de données dans des zones internes, flux explicitement ouverts.

## 4. Mise en œuvre commune

1. TLS : certificats gérés de façon centrale, protocoles et suites conformes à la politique (référence [[Glossary:ANSSI]] ou Mozilla), redirection HTTP vers HTTPS, [[Glossary:HSTS]] après validation.
2. Durcissement : masquer les versions, désactiver les modules/fonctionnalités inutiles, utilisateur de service sans privilèges, limiter la taille des requêtes, protéger les répertoires de gestion.
3. Journalisation : journaux d'accès et d'erreur centralisés, rotation, synchronisation du temps.
4. Sauvegarde : configuration et contenu versionnés ; test de restauration périodique.

## 5. Commandes de contrôle par plateforme

Apache (Debian/Ubuntu) :

```bash
apache2ctl configtest
systemctl reload apache2
```

Nginx :

```bash
nginx -t
systemctl reload nginx
```

IIS (PowerShell sur Windows Server) :

```powershell
Import-Module WebAdministration
Get-Website
Get-WebBinding
Get-WebAppPoolState
```

Toujours tester la configuration avant le rechargement. Sur [[Glossary:RHEL]]/Rocky, le service Apache s'appelle `httpd` ; vérifier les noms de service de la distribution.

## 6. Reverse proxy et haute disponibilité

- Apache : modules proxy (`mod_proxy`, `mod_proxy_http`, `mod_proxy_balancer`) à activer explicitement.
- Nginx : blocs `upstream`, paramètres de délai d'attente et en-têtes `X-Forwarded-*`.
- IIS : modules URL Rewrite et Application Request Routing, installés comme extensions Microsoft ; configuration partagée possible pour des fermes.
- Dans tous les cas, définir quelles en-têtes de transfert sont de confiance pour éviter l'usurpation d'adresse source.

## 7. Validation

- Configuration valide sans erreur ; TLS testé (certificat, chaîne, protocole) depuis un client interne.
- Bascule : arrêt d'un nœud sans interruption du service applicatif perceptible ; contrôle de santé le retire du pool.
- Journaux reçus par le point central ; scan de configuration interne sans service superflu.
- Test de charge dans le lab pour fixer les seuils, et restauration testée.

## 8. Retour arrière

Conserver la configuration précédente versionnée ; revenir au commit précédent et recharger après test de syntaxe. Réactiver l'ancien enregistrement DNS ou le pool du répartiteur. Pour IIS, exporter la configuration (sauvegarde `applicationHost.config` via la procédure Microsoft) avant modification et restaurer sur la fenêtre de maintenance.

## Sources officielles

- [Apache HTTP Server — documentation](https://httpd.apache.org/docs/current/)
- [Nginx — documentation](https://nginx.org/en/docs/)
- [IIS — documentation Microsoft](https://learn.microsoft.com/iis/)
- [Application Request Routing](https://learn.microsoft.com/iis/extensions/planning-for-arr/using-the-application-request-routing-module)
- [ANSSI — recommandations TLS](https://cyber.gouv.fr/publications/recommandations-de-securite-relatives-tls)

Aucun cluster de production n'a été déployé pendant la rédaction ; chaque configuration doit être testée sur la plateforme cible.

## Historique

| Date | Version | Changement | Statut de test |
|---|---|---|---|
| 2026-10-31 | 1.0 | Création de la fiche à partir de la documentation éditeur | Non testé sur plateforme cible |