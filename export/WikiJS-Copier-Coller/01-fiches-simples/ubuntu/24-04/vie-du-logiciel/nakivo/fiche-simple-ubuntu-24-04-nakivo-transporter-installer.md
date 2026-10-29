# Fiche_Simple_-_Ubuntu_24.04_Nakivo_Transporter_Installer

- **Environnement** : Ubuntu Server 24.04 LTS x64; NAKIVO Backup & Replication Transporter
- **OS / Version** : Ubuntu Server 24.04 LTS — explicitement listé dans les exigences NAKIVO consultées; valider la version du produit
- **Catégorie** : sauvegarde / installation

---

## Problème précis à résoudre

Installer uniquement le composant Transporter NAKIVO sur Ubuntu Server 24.04 LTS x64 avec la procédure Linux publiée par l’éditeur.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier les prérequis de la fiche [prérequis et limites](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/nakivo/fiche-simple-ubuntu-24-04-nakivo-transporter-prerequis).
   👉 Explication : confirmer que l’OS précis, le réseau et les packages requis sont compatibles avant l’installation.

2. Télécharger le paquet d’installation Linux depuis le portail NAKIVO officiel autorisé pour votre compte; vérifier les informations d’intégrité publiées par l’éditeur lorsqu’elles sont fournies.
   👉 Explication : ne pas utiliser un miroir tiers ni un script provenant d’une source non validée.

3. Depuis le répertoire extrait du média officiel, exécuter la commande documentée pour une installation silencieuse du seul Transporter :
   ```bash
   ./installer.sh -t --eula-accept
   ```
   👉 Explication : `-t` sélectionne le Transporter seul et `--eula-accept` accepte le contrat après lecture; cette syntaxe provient de la documentation Linux NAKIVO.

4. Suivre la fin de l’assistant ou de l’installation et relever tout message d’erreur; ne pas inventer d’options ou chemins de paquets.
   👉 Explication : les journaux et options dépendent du média et du build NAKIVO.

## 2. Production — Contrôles

Prévoir une fenêtre de changement, une sauvegarde de configuration, des règles réseau restreintes et un test de restauration avant l’usage en production.

## 3. Production — Sécurité

- Garder le système et le Transporter dans le périmètre de mises à jour approuvé.
- Ne pas exposer SSH ou l’interface NAKIVO sur Internet sans architecture de sécurité explicitement approuvée.
- Ne jamais copier de secrets ou de clés privées dans les fiches ou journaux partagés.

## Validation et retour arrière

**Validation** : le nœud Transporter est visible et opérationnel dans NAKIVO; aucun échec d’installation ne reste sans analyse.
- **Retour arrière** : utiliser la procédure de désinstallation documentée pour le build installé; ne pas supprimer manuellement des fichiers de programme.

## Si le problème n’est pas résolu

- [NAKIVO — Installation on Linux (options -t)](https://helpcenter.nakivo.com/User-Guide/Content/Deployment/Installing-NAKIVO-Backup-and-Replication/Installing-on-Linux/Installing-on-Linux.htm)
- [NAKIVO — Deployment Requirements](https://helpcenter.nakivo.com/User-Guide/Content/Deployment/System-Requirements/Deployment-Requirements.htm)
- [Fiche d’entrée NAKIVO / Altaro](/01-fiches-simples/logiciels/07-sauvegarde-restauration-et-pra-pca/fiche-logiciel-nakivo-altaro)