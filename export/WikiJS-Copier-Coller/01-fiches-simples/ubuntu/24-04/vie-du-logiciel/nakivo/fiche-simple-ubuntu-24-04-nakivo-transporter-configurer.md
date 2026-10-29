# Fiche_Simple_-_Ubuntu_24.04_Nakivo_Transporter_Configurer

- **Environnement** : Ubuntu Server 24.04 LTS x64; NAKIVO Backup & Replication Transporter
- **OS / Version** : Ubuntu Server 24.04 LTS — explicitement listé dans les exigences NAKIVO consultées; valider la version du produit
- **Catégorie** : sauvegarde / configuration

---

## Problème précis à résoudre

Rattacher le Transporter Linux installé à une configuration NAKIVO et utiliser le nœud prévu pour les tâches de sauvegarde.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir l’interface web de NAKIVO avec un compte d’administration nominatif.
   👉 Explication : l’interface et les menus varient selon le build; utiliser le parcours officiel de déploiement des nœuds.

2. Dans les paramètres de nœuds/Transporters, vérifier que l’hôte Ubuntu 24.04 est répertorié avec l’état disponible; ajouter ou rattacher le nœud selon le parcours officiel correspondant à l’installation locale.
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

**Validation** : le nœud reste en ligne, le job pilote termine, le point de restauration apparaît dans le dépôt et un test de restauration ciblé réussit.
- **Retour arrière** : retirer le nœud du job/dépôt selon le guide NAKIVO; préserver les sauvegardes nécessaires à la rétention.

## Si le problème n’est pas résolu

- [NAKIVO — Deployment documentation](https://helpcenter.nakivo.com/User-Guide/Content/Deployment/Installing-NAKIVO-Backup-and-Replication/Installing-on-Linux/Installing-on-Linux.htm)
- [NAKIVO — Help Center](https://helpcenter.nakivo.com/)
- [Fiche d’entrée NAKIVO / Altaro](/01-fiches-simples/logiciels/07-sauvegarde-restauration-et-pra-pca/fiche-logiciel-nakivo-altaro)