# Fiche_Simple_-_Cloud_Dynatrace_OneAgent_Securite_MaJ_Retour.md

- **Environnement** : Dynatrace SaaS et hôte Linux administré
- **OS / Version** : Distribution et architecture Linux prises en charge par la version OneAgent du tenant
- **Catégorie** : observabilité / sécurité

---

## Problème précis à résoudre

Sécuriser OneAgent, le mettre à jour et savoir le retirer.

## 1. Hors-Production (Lab / Test / POC)

1. Ne jamais forcer l'installation sur une plateforme non supportée avec `SKIP_OS_SUPPORT_CHECK`.
   👉 Explication : une plateforme non supportée n'a pas de garantie de fonctionnement.

2. Vérifier la signature de chaque binaire récupéré et garder les communications TLS validées.
   👉 Explication : garantit l'intégrité et la confidentialité.

3. Protéger les chemins de configuration, données et journaux OneAgent et limiter l'accès à l'administration du tenant.
   👉 Explication : contiennent des informations d'environnement.

4. Tester les mises à jour sur un groupe pilote, coordonner les redémarrages d'applications et contrôler la capacité.
   👉 Explication : évite les régressions à grande échelle.

5. Contrôler le service :
   ```bash
   sudo systemctl --no-pager status oneagent
   ```
   👉 Explication : Contrôle le service après mise à jour ou après désinstallation (il ne doit plus exister).

## 2. Production — Contrôles

Pour le rollback, suivre la procédure officielle de désinstallation de la version et retirer l'hôte du groupe d'automatisation si besoin.

## 3. Production — Sécurité

- Pas de `SKIP_OS_SUPPORT_CHECK`; TLS toujours validé.

## Validation et retour arrière

- **Validation** : mise à jour validée sur le pilote, ou ingestion arrêtée après désinstallation.
- **Retour arrière** : désinstaller via la procédure officielle puis confirmer dans le tenant que l'hôte n'envoie plus de données.

## Si le problème n'est pas résolu

- [Dynatrace — Désinstaller OneAgent Linux](https://docs.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/uninstall-oneagent-on-linux)
- [Dynatrace — Installer OneAgent sur Linux](https://docs.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/install-oneagent-on-linux)
- [Guide complet — étape 5](/02-fiches-completes/transverses/cloud-saas/installation-deploiement/53-deploiement-dynatrace-oneagent-linux-saas#5-securite-mise-a-jour-et-retour-arriere)