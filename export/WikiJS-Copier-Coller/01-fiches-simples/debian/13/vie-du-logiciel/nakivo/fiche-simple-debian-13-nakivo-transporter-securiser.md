# Fiche_Simple_-_Debian_13_Nakivo_Transporter_Securiser

- **Environnement** : Debian 13 x64; NAKIVO Backup & Replication Transporter
- **OS / Version** : Debian 13 64-bit — explicitement listé dans les exigences de déploiement NAKIVO; valider le build produit
- **Catégorie** : sauvegarde / sécurité

---

## Problème précis à résoudre

Réduire l’exposition du serveur Debian 13 utilisé par le Transporter et protéger les communications et les comptes de service.

## 1. Hors-Production (Lab / Test / POC)

1. Autoriser seulement les flux explicitement requis par la version NAKIVO, entre les systèmes NAKIVO et l’hôte concerné.
   👉 Explication : ouvrir les ports strictement nécessaires selon la documentation courante; ne pas exposer l’accès SSH sur Internet.

2. Utiliser un compte d’administration dédié avec les privilèges nécessaires; conserver les identifiants dans le coffre approuvé, jamais dans cette fiche.
   👉 Explication : l’accès SSH permet l’administration distante du serveur.

3. Éviter d’autoriser l’accès SSH root si un compte avec sudo répond aux exigences NAKIVO; si root est retenu, appliquer les exigences de l’éditeur et une restriction réseau renforcée.
   👉 Explication : les permissions dépendent du scénario de déploiement; ne pas modifier la configuration SSH sans procédure de changement.

4. Maintenir Debian et le produit NAKIVO à jour selon leurs guides respectifs; sauvegarder la configuration et vérifier les alertes.
   👉 Explication : la fiche ne fixe pas de cadence ni de commande de mise à jour non fournie par l’éditeur.

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