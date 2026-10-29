# Fiche_Simple_-_Debian_13_Nakivo_Transporter_Configurer

- **Environnement** : Debian 13 x64; NAKIVO Backup & Replication Transporter
- **OS / Version** : Debian 13 64-bit — explicitement listé dans les exigences de déploiement NAKIVO; valider le build produit
- **Catégorie** : sauvegarde / configuration
- **Tags** : `debian-13`, `nakivo`, `transporter`, `configurer`

---

## Problème précis à résoudre

Rattacher le Transporter Debian 13 installé à une configuration NAKIVO et utiliser le nœud prévu pour les tâches de sauvegarde.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir l’interface web de NAKIVO avec un compte d’administration nominatif.
   👉 Explication : l’interface et les menus varient selon le build; utiliser le parcours officiel de déploiement des nœuds.

2. Dans les paramètres de nœuds/Transporters, vérifier que l’hôte Debian 13 est répertorié avec l’état disponible; ajouter ou rattacher le nœud selon le parcours officiel correspondant à l’installation locale.
   👉 Explication : ne pas supposer que le nœud est associé automatiquement si le build exige une étape d’enregistrement.

3. Associer le Transporter au dépôt ou au job uniquement après avoir vérifié son rôle, sa capacité réseau et sa localisation.
   👉 Explication : placer les transferts au bon emplacement évite un chemin de données non prévu.

4. Créer un job pilote de faible portée et lancer une sauvegarde de test.
   👉 Explication : confirmer qu’il n’y a ni erreur de connexion ni saturation du lien avant les charges de production.

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
