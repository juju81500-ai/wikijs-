# Fiche_Simple_-_Debian_13_Nakivo_Transporter_Prerequis

- **Environnement** : Debian 13 x64; NAKIVO Backup & Replication Transporter
- **OS / Version** : Debian 13 64-bit — explicitement listé dans les exigences de déploiement NAKIVO; valider le build produit
- **Catégorie** : sauvegarde / prérequis
- **Tags** : `debian-13`, `nakivo`, `transporter`, `prerequis`

---

## Problème précis à résoudre

Vérifier qu’un hôte Debian 13 x64 remplit les prérequis publiés par NAKIVO pour héberger un Transporter Linux.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier l’OS et l’architecture :
   ```bash
   . /etc/os-release && printf '%s %s
' "$NAME" "$VERSION_ID"
   uname -m
   ```
   👉 Explication : la matrice de déploiement NAKIVO liste explicitement Debian 13 64-bit; l’architecture doit correspondre.

2. Vérifier la présence de SSH et l’accès réseau requis avant d’ajouter le Transporter :
   ```bash
   systemctl is-active ssh
   ```
   👉 Explication : utiliser les exigences de communication et les ports documentés pour le build NAKIVO retenu.

3. Comparer les prérequis matériels, logiciels, ports et paquets requis à la page d’exigences NAKIVO actuelle.
   👉 Explication : la matrice « Deployment Requirements » décrit l’OS du serveur servant de composant d’infrastructure; ne pas la confondre avec la liste des OS protégés par un job.

4. Confirmer le build NAKIVO et les exigences de version avant d’installer.
   👉 Explication : la prise en charge OS est explicite pour Debian 13 x64, mais les dépendances et limitations restent celles de la version courante.

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
- [Fiche d’entrée NAKIVO / Altaro](../../../../Logiciels/07-Sauvegarde-restauration-et-PRA-PCA/Fiche_Logiciel_-_Nakivo-Altaro.md)
