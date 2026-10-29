# Fiche_Simple_-_Cloud_Dynatrace_OneAgent_Generer_Installateur.md

- **Environnement** : Dynatrace SaaS et hôte Linux administré
- **OS / Version** : Distribution et architecture Linux prises en charge par la version OneAgent du tenant
- **Catégorie** : observabilité / installation
- **Tags** : `dynatrace`, `saas`, `oneagent`, `linux`, `observabilite`

---

## Problème précis à résoudre

Générer la commande d'installation officielle sans exposer de token.

## 1. Hors-Production (Lab / Test / POC)

1. Dans Dynatrace : **Discovery & Coverage > Install > Install OneAgent**, choisir **Linux** et l'architecture de l'hôte.
   👉 Explication : l'interface génère la commande et un token de téléchargement limité au tenant.

2. Connaître l'architecture :
   ```bash
   uname -m
   ```
   👉 Explication : `x86_64` ou `aarch64` selon l'hôte; à reporter dans l'interface.

3. Sélectionner options de surveillance, groupe, tags et ActiveGate/proxy attendus.
   👉 Explication : ces choix sont intégrés à la commande générée.

4. Examiner origine, destination et paramètres des commandes générées avant exécution root, puis lancer la vérification de signature officielle avant l'installateur.
   👉 Explication : évite d'exécuter un binaire altéré.

5. Ne pas enregistrer la commande complète ni ses tokens dans logs, tickets, dépôts ou captures.
   👉 Explication : le token donne accès au tenant.

## 2. Production — Contrôles

Si les prérequis de privilèges manquent, décider explicitement de la configuration au lieu de changer silencieusement le mode non privilégié.

## 3. Production — Sécurité

- Token jamais copié hors du terminal; rôles pouvant générer un installateur restreints.

## Validation et retour arrière

- **Validation** : commande générée, signature vérifiée, aucun token stocké.
- **Retour arrière** : révoquer le token généré s'il a été exposé.

## Si le problème n'est pas résolu

- [Dynatrace — Personnaliser l'installation Linux](https://docs.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux)
- [Dynatrace — Mode non privilégié Linux](https://docs.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/linux-non-privileged)
- [Dynatrace — Installer OneAgent sur Linux](https://docs.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/install-oneagent-on-linux)
- [Guide complet — étape 2](../../../../02-Fiches-Completes/Transverses/Cloud-SaaS/Installation-Deploiement/53_Deploiement_Dynatrace_OneAgent_Linux_SaaS.md#2-generer-linstallateur-officiel)
