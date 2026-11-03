---
title: "Déployer l'ingestion de données vers Splunk Cloud Platform (Universal Forwarder et HEC)"
description: "- Couvre l'usage d'un tenant Splunk Cloud Platform (service géré par Splunk). Le déploiement logiciel autohébergé est traité dans le [guide Splunk Enterprise Debian 12](../../../debian/12/installation-deploiement/54-deploiement-splunk-enterprise-10-2-debian-12.md) et ne s'applique pas ici : vous n'i"
published: true
date: 2026-11-03T09:36:14Z
tags: ["splunk-cloud", "saas", "universal-forwarder", "hec", "siem"]
editor: markdown
dateCreated: 2026-11-03T09:36:14Z
dateModified: 2026-11-03T09:36:14Z
---

# Déployer l'ingestion de données vers Splunk Cloud Platform (Universal Forwarder et HEC)

- **OS / Version** : Tenant Splunk Cloud Platform (SaaS) ; Universal Forwarder sur Linux ou Windows
- **Type de fiche** : Installation/Déploiement
- **Périmètre** : Onboarding d'un tenant existant, index, rôles, envoi par Universal Forwarder et [[Glossary:HTTP]] Event Collector (HEC), contrôle de réception
- **Catégorie** : [[Glossary:SIEM]] / observabilité
- **Tags** : `splunk-cloud`,`saas`,`universal-forwarder`,`hec`,`siem`

## 1. Portée, hypothèses et licences

- Couvre l'usage d'un **tenant Splunk Cloud Platform** (service géré par Splunk). Le déploiement logiciel autohébergé est traité dans le [guide Splunk Enterprise Debian 12](/fr/02-fiches-completes/debian/12/installation-deploiement/54-deploiement-splunk-enterprise-10-2-debian-12) et ne s'applique pas ici : vous n'installez ni n'administrez les serveurs de recherche ou d'indexation.
- **Souscription requise** : Splunk Cloud Platform est vendu sur abonnement (volume d'ingestion ou charge de travail selon l'offre). Un essai peut exister mais ses limites sont fixées par l'éditeur au moment de l'inscription ; les confirmer avant de planifier.
- Hypothèses : le tenant est provisionné, un compte avec le rôle `sc_admin` (ou équivalent) est disponible, les sources à collecter sont inventoriées et leur collecte est autorisée par la politique de l'organisation (données personnelles, rétention).
- Les fonctions disponibles (Admin Config Service, expérience « Victoria » ou « Classic », gestion des listes d'autorisation d'[[Glossary:IP]]) dépendent de l'offre et de la région : vérifier dans la documentation de votre stack.

## 2. Prérequis

- Nom du stack (`<stack>.splunkcloud.com`), région, type d'expérience (visible dans le support/portail).
- Flux sortants autorisés du réseau interne vers le stack (récepteur de forwarders, par défaut [[Glossary:TCP]] 9997 pour la réception Splunk-to-Splunk selon la documentation Splunk Cloud ; HTTPS 443 pour HEC) : valider les ports exacts dans la documentation « Splunk Cloud Platform » car ils dépendent de l'expérience.
- Plan de nommage : index (`os_linux`, `os_windows`, `app_<nom>`), sourcetypes, rôles et rétention validés avec le [[Glossary:RSSI]].
- Moyens de gestion des secrets pour tokens HEC et identifiants.

## 3. Préparer le tenant (index, rôles, accès)

1. Se connecter à l'interface web du stack avec un compte administrateur nominatif ; activer l'authentification forte / [[Glossary:SAML]] selon la politique.
2. Créer les index (Settings > Indexes) avec rétention et taille adaptées. Ne pas utiliser l'index `main` par défaut pour tout.
3. Créer des rôles à moindre privilège (lecture par index) et les rattacher aux groupes [[Glossary:SSO]]. Éviter les comptes partagés.
4. Si l'accès à l'[[Glossary:API]] ou à HEC est restreint par liste d'autorisation, ajouter les adresses de sortie ([[Glossary:NAT]]) de l'organisation via l'interface prévue (Admin Config Service ou page « IP allow list »), après validation de la documentation applicable à votre offre.

## 4. Chemin A — Universal Forwarder

1. Télécharger l'Universal Forwarder depuis le portail officiel Splunk (compte Splunk requis) et vérifier la somme de contrôle publiée.
2. Télécharger depuis le stack le **paquet d'identifiants du Universal Forwarder** (application « Universal Forwarder Credentials », fichier `.spl` ; le nom exact figure sur la page de téléchargement de votre stack). Il contient certificats et destinations ; le traiter comme un secret.
3. Installer le forwarder (Linux : paquet `.deb`/`.rpm` ; Windows : [[Glossary:MSI]]) en suivant la procédure « Install a universal forwarder » de la documentation. Démarrer avec un compte de service dédié, pas root/SYSTEM quand c'est évitable.
4. Installer le paquet d'identifiants :

```bash
/opt/splunkforwarder/bin/splunk install app /chemin/vers/paquet_identifiants.spl -auth <admin_local>:<mot_de_passe>
/opt/splunkforwarder/bin/splunk restart
```

5. Déclarer les entrées dans `inputs.conf` avec l'index cible :

```ini
[monitor:///var/log/auth.log]
index = os_linux
sourcetype = linux_secure
```

Valider chaque nom de sourcetype contre les Add-ons Splunk adaptés à la source.

## 5. Chemin B — HTTP Event Collector (HEC)

1. Dans Settings > Data inputs > HTTP Event Collector, créer un token par application, limité aux index autorisés, avec nom explicite.
2. L'URL de l'endpoint HEC dépend de l'offre et du stack : la lire dans la documentation « Send data to HTTP Event Collector on Splunk Cloud Platform » ; ne pas la deviner.
3. Test d'envoi d'un événement (le token reste dans une variable, jamais dans un script versionné) :

```bash
curl -sS "https://<endpoint_hec_documente>/services/collector/event" \
  -H "Authorization: Splunk ${HEC_TOKEN}" \
  -d '{"event":"test onboarding","sourcetype":"manual","index":"app_test"}'
```

Réponse attendue : `{"text":"Success","code":0}`.

## 6. Validation

- Recherche `index=os_linux earliest=-15m | stats count by host, sourcetype` retourne les hôtes attendus.
- `index=_internal source=*metrics.log host=<hote_forwarder>` (si votre rôle le permet) montre que le forwarder envoie.
- Seuls les index autorisés sont alimentés ; un token HEC sur un index non autorisé est rejeté.
- Volumes journaliers comparés à la licence/consommation affichée dans la console de supervision de licence.
- Un utilisateur de test voit uniquement ses index.

## 7. Retour arrière

- Désactiver (et non supprimer d'abord) le token HEC ; arrêter le forwarder (`splunk stop`) et retirer l'application d'identifiants (`splunk remove app <nom>`), puis désinstaller le paquet.
- Révoquer les tokens/identifiants exposés et régénérer le paquet d'identifiants en cas de fuite.
- Les données déjà indexées restent dans Splunk Cloud selon la rétention ; toute suppression est une demande distincte validée (commande `delete` ou support Splunk selon l'offre).
- Les sauvegardes des configurations locales (`inputs.conf`, `outputs.conf`) sont conservées hors hôte.

## Sources officielles

- [Splunk Cloud Platform — documentation](https://docs.splunk.com/Documentation/SplunkCloud/latest)
- [Splunk Universal Forwarder — manuel](https://docs.splunk.com/Documentation/Forwarder/latest/Forwarder/Abouttheuniversalforwarder)
- [Splunk — HTTP Event Collector](https://docs.splunk.com/Documentation/Splunk/latest/Data/UsetheHTTPEventCollector)
- [Splunk Cloud Platform — Admin Config Service](https://docs.splunk.com/Documentation/SplunkCloud/latest/Config/ACSIntro)

Aucune connexion à un tenant Splunk Cloud n'a été réalisée pendant la rédaction. Les versions, ports et URL doivent être confirmés dans la documentation de votre stack.

## Historique

| Date | Version | Changement | Statut de test |
|---|---|---|---|
| 2026-10-31 | 1.0 | Création de la fiche à partir de la documentation éditeur | Non testé sur plateforme cible |