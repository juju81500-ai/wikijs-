# Fiche_Simple_-_Debian_13_Nakivo_Transporter_Installer

- **Environnement** : Debian 13 x64; NAKIVO Backup & Replication Transporter
- **OS / Version** : Debian 13 64-bit — explicitement listé dans les exigences de déploiement NAKIVO; valider le build produit
- **Catégorie** : sauvegarde / installation

---

## Problème précis à résoudre

Installer uniquement le composant Transporter NAKIVO sur Debian 13 x64 avec la procédure Linux publiée par l’éditeur.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier les prérequis de la fiche [prérequis et limites](/01-fiches-simples/debian/13/vie-du-logiciel/nakivo/fiche-simple-debian-13-nakivo-transporter-prerequis).
   👉 Explication : confirmer que l’OS précis, le réseau et les packages requis sont compatibles avant l’installation.

2. Télécharger le paquet d’installation Linux depuis le portail NAKIVO officiel autorisé pour le compte; vérifier les informations d’intégrité publiées par l’éditeur lorsqu’elles sont fournies.
   👉 Explication : ne pas utiliser un miroir tiers ni un script provenant d’une source non validée.

3. Depuis le répertoire extrait du média officiel, exécuter la commande documentée pour une installation silencieuse du seul Transporter :
   ```bash
   ./installer.sh -t --eula-accept
   ```
   👉 Explication : `-t` sélectionne le Transporter seul et `--eula-accept` accepte le contrat après lecture; la syntaxe est publiée par NAKIVO.

4. Suivre la fin de l’installation et relever tout message d’erreur; ne pas inventer d’options ou chemins de paquets.
   👉 Explication : les journaux et options dépendent du média et du build NAKIVO.

## 2. Production — Contrôles

Prévoir une fenêtre de changement, une sauvegarde de configuration, des règles réseau restreintes et un test de restauration avant l’usage en production.

## 3. Production — Sécurité

- Garder le système et le Transporter dans le périmètre de mises à jour approuvé.
- Ne pas exposer SSH ou l’interface NAKIVO sur Internet sans architecture de sécurité explicitement approuvée.
- Ne jamais copier de secrets ou de clés privées dans les fiches ou journaux partagés.

## Validation et retour arrière

- **Validation** : Debian 13 x64 est confirmé dans la matrice de déploiement NAKIVO; le nœud est sain, les jobs pilotes et une restauration de test réussissent.
- **Retour arrière** : suivre uniquement la procédure de désinstallation ou de retour arrière indiquée par NAKIVO pour le build; préserver les dépôts et données de sauvegarde.

## Si le problème n’est pas résolu

- [NAKIVO — Deployment Requirements](https://helpcenter.nakivo.com/User-Guide/Content/Deployment/System-Requirements/Deployment-Requirements.htm)
- [NAKIVO — Installation on Linux](https://helpcenter.nakivo.com/User-Guide/Content/Deployment/Installing-NAKIVO-Backup-and-Replication/Installing-on-Linux/Installing-on-Linux.htm)
- [Fiche d’entrée NAKIVO / Altaro](/01-fiches-simples/logiciels/07-sauvegarde-restauration-et-pra-pca/fiche-logiciel-nakivo-altaro)