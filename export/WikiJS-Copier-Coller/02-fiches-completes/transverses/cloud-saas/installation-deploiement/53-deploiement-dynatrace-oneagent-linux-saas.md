# Déployer Dynatrace OneAgent sur Linux avec Dynatrace SaaS

- **OS / Version** : Distribution et architecture Linux prises en charge par la version OneAgent du tenant
- **Type de fiche** : Installation/Déploiement
- **Périmètre** : Déploiement hôte pilote, puis extension contrôlée
- **Catégorie** : Observabilité / infrastructure et applications

## 1. Préparer l'hôte et le tenant

Fiche simple : [préparer l'hôte et le tenant Dynatrace](/01-fiches-simples/transverses/cloud-saas/dynatrace/fiche-simple-cloud-dynatrace-oneagent-preparer-hote-tenant).

Vérifier la prise en charge OS/architecture, les ressources disque/mémoire, les processus applicatifs et les contraintes de redémarrage. Confirmer si l'hôte communique directement avec Dynatrace SaaS ou via ActiveGate, et ouvrir seulement les flux sortants indiqués par le tenant.

Choisir un groupe d'hôtes, des tags, la zone réseau et le mode de surveillance (Full-Stack, Infrastructure ou Discovery). Identifier l'impact potentiel de l'injection automatique sur les processus avant installation et prévoir une fenêtre de redémarrage si nécessaire.

## 2. Générer l'installateur officiel

Fiche simple : [générer l'installateur officiel OneAgent](/01-fiches-simples/transverses/cloud-saas/dynatrace/fiche-simple-cloud-dynatrace-oneagent-generer-installateur).

Dans Dynatrace **Discovery & Coverage > Install > Install OneAgent**, choisir Linux et l'architecture correspondant à l'hôte. Sélectionner les options de surveillance, groupe, tags et ActiveGate/proxy attendus. L'interface génère une commande de téléchargement et un token de téléchargement limité au périmètre du tenant.

Télécharger et exécuter les commandes générées depuis le tenant authentifié. Examiner l'origine, la destination et les paramètres avant exécution root. Après téléchargement, exécuter la commande de vérification de signature officielle avant l'installateur. Ne pas enregistrer la commande complète ou ses tokens dans des logs, tickets, dépôts ou captures.

OneAgent requiert des privilèges élevés lors de l'installation; le mode non privilégié est activé par défaut pour les processus compatibles dans les versions prises en charge. Si les prérequis ne sont pas réunis, décider explicitement de la configuration de privilèges au lieu de changer silencieusement le mode.

## 3. Installer un pilote

Fiche simple : [installer un pilote OneAgent](/01-fiches-simples/transverses/cloud-saas/dynatrace/fiche-simple-cloud-dynatrace-oneagent-installer-pilote).

```bash
sudo systemctl --no-pager status oneagent
```

Utiliser d'abord un hôte de test. L'interface de déploiement fournit la commande spécifique et les contrôles de statut adaptés au tenant/version; ne pas inventer ni réutiliser un token d'un autre environnement. Vérifier l'arrivée du host dans Dynatrace, les métadonnées et le mode sélectionné.

Redémarrer les processus applicatifs seulement si nécessaire pour activer le monitoring profond et dans une fenêtre approuvée. Contrôler l'impact sur CPU, mémoire, processus et disponibilité avant le déploiement à l'échelle.

## 4. Généraliser et exploiter

Fiche simple : [généraliser et exploiter OneAgent](/01-fiches-simples/transverses/cloud-saas/dynatrace/fiche-simple-cloud-dynatrace-oneagent-generaliser-exploiter).

Déployer par groupes via Fleet/outil de configuration approuvé. Utiliser des groupes et tags normalisés; contrôler l'état de connexion, la version, les mises à jour et les problèmes signalés par OneAgent. Réévaluer le mode de surveillance et les fonctions d'accès aux logs selon le besoin métier.

Garder les tokens d'installation/download distincts des tokens de communication du tenant. Révoquer ou faire tourner les tokens selon la politique d'accès; restreindre les rôles pouvant générer un installateur. Pour les environnements sensibles ou isolés, préférer ActiveGate si prévu par l'architecture.

## 5. Sécurité, mise à jour et retour arrière

Fiche simple : [sécurité, mise à jour et retour arrière OneAgent](/01-fiches-simples/transverses/cloud-saas/dynatrace/fiche-simple-cloud-dynatrace-oneagent-securite-maj-retour).

- Ne pas forcer une installation sur une plateforme non supportée avec `SKIP_OS_SUPPORT_CHECK`.
- Protéger les chemins de configuration, données et journaux OneAgent et limiter l'accès à l'administration du tenant.
- Vérifier la signature de chaque binaire récupéré et garder les communications TLS validées.
- Tester les upgrades sur un groupe pilote; coordonner les redémarrages d'applications et contrôler les changements de capacité.
- Pour rollback, suivre la procédure officielle de désinstallation de la version, retirer l'hôte du groupe d'automatisation si besoin et confirmer que l'ingestion cesse.

## Sources

- [Dynatrace — Installer OneAgent sur Linux](https://docs.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/install-oneagent-on-linux)
- [Dynatrace — Personnaliser l'installation Linux](https://docs.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux)
- [Dynatrace — Mode non privilégié Linux](https://docs.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/linux-non-privileged)
- [Dynatrace — Désinstaller OneAgent Linux](https://docs.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/uninstall-oneagent-on-linux)
- [Dynatrace — Support des technologies](https://docs.dynatrace.com/docs/ingest-from/technology-support)