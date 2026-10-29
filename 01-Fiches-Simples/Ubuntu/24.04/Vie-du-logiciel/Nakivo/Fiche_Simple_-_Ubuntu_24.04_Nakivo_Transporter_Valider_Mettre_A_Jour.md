# Fiche_Simple_-_Ubuntu_24.04_Nakivo_Transporter_Valider_Mettre_A_Jour

- **Environnement** : Ubuntu Server 24.04 LTS x64; NAKIVO Backup & Replication Transporter
- **OS / Version** : Ubuntu Server 24.04 LTS — explicitement listé dans les exigences NAKIVO consultées; valider la version du produit
- **Catégorie** : sauvegarde / maintenance
- **Tags** : `ubuntu-24.04`, `nakivo`, `transporter`, `transporter-valider-mettre-a-jour`

---

## Problème précis à résoudre

Contrôler que le Transporter fonctionne correctement et appliquer ses mises à jour en suivant la documentation NAKIVO actuelle.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler l’état du nœud depuis la console NAKIVO et examiner les journaux si le statut n’est pas sain.
   👉 Explication : la console confirme l’état utile au Director; le nom local du service peut varier selon le build.

2. Exécuter un job pilote, puis restaurer un objet ou une machine de test dans une destination isolée.
   👉 Explication : le succès de sauvegarde seul ne prouve pas que le parcours de restauration est opérationnel.

3. Avant mise à jour, relever le build actuel, confirmer la compatibilité dans les notes de version et vérifier une sauvegarde/rétention valide.
   👉 Explication : les notes de version déterminent le chemin et l’ordre de mise à jour.

4. Appliquer la mise à jour du Transporter par une méthode explicitement décrite par NAKIVO pour la version déployée; ne pas lancer de commande générique sans vérifier ses options.
   👉 Explication : le mode d’update dépend du build et du type d’installation.

## 2. Production — Contrôles

Prévoir une fenêtre de changement, une sauvegarde de configuration, des règles réseau restreintes et un test de restauration avant l’usage en production.

## 3. Production — Sécurité

- Garder le système et le Transporter dans le périmètre de mises à jour approuvé.
- Ne pas exposer SSH ou l’interface NAKIVO sur Internet sans architecture de sécurité explicitement approuvée.
- Ne jamais copier de secrets ou de clés privées dans les fiches ou journaux partagés.

## Validation et retour arrière

**Validation** : build cible enregistré, nœud en ligne après maintenance, jobs et restauration pilote réussis.
- **Retour arrière** : suivre uniquement la procédure de retour arrière indiquée par NAKIVO pour le build; conserver les dépôts et données de sauvegarde.

## Si le problème n’est pas résolu

- [NAKIVO — Updating NAKIVO Backup & Replication](https://helpcenter.nakivo.com/User-Guide/Content/Deployment/Updating-NAKIVO-Backup-and-Replication/Updating-NAKIVO-Backup-and-Replication.htm)
- [NAKIVO — Release Notes](https://helpcenter.nakivo.com/Release-Notes/Content/Release-Notes.htm)
- [Fiche d’entrée NAKIVO / Altaro](../../../../Logiciels/07-Sauvegarde-restauration-et-PRA-PCA/Fiche_Logiciel_-_Nakivo-Altaro.md)
