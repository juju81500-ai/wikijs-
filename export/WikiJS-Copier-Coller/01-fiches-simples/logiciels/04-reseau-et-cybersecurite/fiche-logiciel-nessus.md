# 📄 Nessus

- **Catégorie** : Réseau et cybersécurité
- **Plateforme** : Linux
- **Produit (matrice)** : Nessus / OpenVAS
- **Statut dans le pack** : Documentation défensive — administration et gouvernance

## 📚 Couverture dans le pack

Fiche défensive d’administration et de gouvernance. Elle ne remplace pas le guide éditeur spécifique à la version déployée et ne fournit pas de procédure offensive.

## 🧭 Périmètre

Cette fiche complète la fiche simple Debian existante par la gouvernance; elle ne décrit pas la création ni le lancement d’analyses. Restreindre l’interface aux administrateurs autorisés, utiliser des comptes nominatifs et les rôles disponibles, protéger sauvegardes, résultats et identifiants, et tenir à jour les composants selon les instructions Tenable et les droits de licence effectivement acquis. Les évaluations actives doivent faire l’objet d’une autorisation écrite séparée, avec périmètre et fenêtre bornés.

## ✅ Autorisation et préparation

Avant toute modification, consigner le propriétaire du service, les actifs et utilisateurs concernés, le ticket de changement, l’approbateur, la fenêtre, les dépendances, les critères d’arrêt et la personne à contacter. Toute évaluation active ou action sur un terminal/équipement exige une autorisation écrite explicite, limitée au périmètre et à la durée approuvés. Sans accord, rester sur l’inventaire géré, les journaux et les contrôles de configuration passifs.

## 🔎 Validation

Valider l’accès d’administration, le chargement normal des données de détection, les journaux, la sauvegarde restaurable et les contrôles d’accès. En cas de mise à jour défaillante, suspendre toute activité, conserver les journaux et revenir à la version/configuration supportée selon Tenable; ne pas restaurer des résultats non fiables. Vérifier aussi l’horodatage, la journalisation et l’absence de secrets dans les tickets ou exports; faire approuver le résultat par le propriétaire du service.

## ↩️ Retour arrière

Avant changement, conserver une sauvegarde ou un état de référence protégé, vérifier la possibilité réelle de restauration et garder un accès d’administration de secours approuvé. Si la validation échoue, interrompre le déploiement, restaurer la dernière configuration/package supporté selon la procédure éditeur, vérifier les services dépendants et consigner la cause. Ne pas improviser une procédure de restauration non documentée.

## 🚨 Alertes et remédiation

Préserver les journaux utiles, corréler avec les sources de supervision autorisées et ouvrir un incident/ticket attribué. Prioriser selon impact métier, exposition et avis éditeur; appliquer une correction supportée après validation, puis documenter le résultat. Toute action de confinement, révocation ou blocage doit suivre le plan d’incident approuvé et être traçable.

## 📚 Sources officielles

- [Tenable Nessus documentation](https://docs.tenable.com/nessus/) — choisir la version, l’édition et le modèle correspondant au déploiement réel.
- [CIS Controls — documentation officielle](https://www.cisecurity.org/controls) — repères de gouvernance et gestion des actifs; adapter au contexte.

> Aucun numéro de version, niveau de licence ni prérequis produit n’est présumé dans cette fiche. Vérifier ces éléments dans le portail éditeur et le contrat de l’organisation avant toute mise en œuvre.