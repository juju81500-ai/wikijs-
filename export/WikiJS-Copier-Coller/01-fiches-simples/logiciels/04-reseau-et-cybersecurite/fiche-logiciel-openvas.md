# 📄 OpenVAS

- **Catégorie** : Réseau et cybersécurité
- **Plateforme** : Linux
- **Produit (matrice)** : Nessus / OpenVAS
- **Statut dans le pack** : Documentation défensive — administration et gouvernance

## 📚 Couverture dans le pack

Fiche défensive d’administration et de gouvernance. Elle ne remplace pas le guide éditeur spécifique à la version déployée et ne fournit pas de procédure offensive.

## 🧭 Périmètre

Complément de gouvernance à la fiche GVM existante; aucun flux, cible, tâche ou lancement d’analyse n’est décrit ici. Restreindre la console au réseau d’administration, appliquer RBAC et comptes nominatifs, protéger les sauvegardes et rapports qui peuvent révéler des vulnérabilités internes. Vérifier l’origine et l’état des flux selon la documentation et l’édition réellement déployée; ne pas supposer qu’un type de flux, support ou licence s’applique à toutes les éditions.

## ✅ Autorisation et préparation

Avant toute modification, consigner le propriétaire du service, les actifs et utilisateurs concernés, le ticket de changement, l’approbateur, la fenêtre, les dépendances, les critères d’arrêt et la personne à contacter. Toute évaluation active ou action sur un terminal/équipement exige une autorisation écrite explicite, limitée au périmètre et à la durée approuvés. Sans accord, rester sur l’inventaire géré, les journaux et les contrôles de configuration passifs.

## 🔎 Validation

Contrôler l’état des composants et des flux, les journaux de service, les permissions et la restauration de configuration. Toute activité de test nécessite un accord écrit du propriétaire avec plage, fenêtre, limites et point de contact. En cas d’impact inattendu, arrêter l’activité et suivre l’escalade convenue. Vérifier aussi l’horodatage, la journalisation et l’absence de secrets dans les tickets ou exports; faire approuver le résultat par le propriétaire du service.

## ↩️ Retour arrière

Avant changement, conserver une sauvegarde ou un état de référence protégé, vérifier la possibilité réelle de restauration et garder un accès d’administration de secours approuvé. Si la validation échoue, interrompre le déploiement, restaurer la dernière configuration/package supporté selon la procédure éditeur, vérifier les services dépendants et consigner la cause. Ne pas improviser une procédure de restauration non documentée.

## 🚨 Alertes et remédiation

Préserver les journaux utiles, corréler avec les sources de supervision autorisées et ouvrir un incident/ticket attribué. Prioriser selon impact métier, exposition et avis éditeur; appliquer une correction supportée après validation, puis documenter le résultat. Toute action de confinement, révocation ou blocage doit suivre le plan d’incident approuvé et être traçable.

## 📚 Sources officielles

- [Greenbone official documentation](https://docs.greenbone.net/) — choisir la version, l’édition et le modèle correspondant au déploiement réel.
- [CIS Controls — documentation officielle](https://www.cisecurity.org/controls) — repères de gouvernance et gestion des actifs; adapter au contexte.

> Aucun numéro de version, niveau de licence ni prérequis produit n’est présumé dans cette fiche. Vérifier ces éléments dans le portail éditeur et le contrat de l’organisation avant toute mise en œuvre.