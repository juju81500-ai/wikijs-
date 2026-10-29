# 📄 Defender for Endpoint

- **Catégorie** : Réseau et cybersécurité
- **Plateforme** : SaaS / agents
- **Produit (matrice)** : CrowdStrike Falcon / SentinelOne / Defender for Endpoint
- **Statut dans le pack** : Documentation défensive — administration et gouvernance

## 📚 Couverture dans le pack

Fiche défensive d’administration et de gouvernance. Elle ne remplace pas le guide éditeur spécifique à la version déployée et ne fournit pas de procédure offensive.

## 🧭 Périmètre

Utiliser les rôles RBAC Microsoft Entra/Defender et MFA, onboarder uniquement les terminaux appartenant au périmètre, suivre la santé et la configuration de sécurité via les outils Microsoft supportés. Déployer les stratégies par anneaux et contrôler les conflits avec les autres agents de protection. Les actions de réponse (isolation, collecte, suppression) doivent être décidées dans un incident autorisé.

## ✅ Autorisation et préparation

Avant toute modification, consigner le propriétaire du service, les actifs et utilisateurs concernés, le ticket de changement, l’approbateur, la fenêtre, les dépendances, les critères d’arrêt et la personne à contacter. Toute évaluation active ou action sur un terminal/équipement exige une autorisation écrite explicite, limitée au périmètre et à la durée approuvés. Sans accord, rester sur l’inventaire géré, les journaux et les contrôles de configuration passifs.

## 🔎 Validation

Valider la remontée d’un poste pilote, la conformité des politiques, le flux d’alertes et les exclusions approuvées. Retour arrière par réversion contrôlée des affectations/politiques selon la documentation Microsoft; consigner les incidents de compatibilité. Vérifier aussi l’horodatage, la journalisation et l’absence de secrets dans les tickets ou exports; faire approuver le résultat par le propriétaire du service.

## ↩️ Retour arrière

Avant changement, conserver une sauvegarde ou un état de référence protégé, vérifier la possibilité réelle de restauration et garder un accès d’administration de secours approuvé. Si la validation échoue, interrompre le déploiement, restaurer la dernière configuration/package supporté selon la procédure éditeur, vérifier les services dépendants et consigner la cause. Ne pas improviser une procédure de restauration non documentée.

## 🚨 Alertes et remédiation

Préserver les journaux utiles, corréler avec les sources de supervision autorisées et ouvrir un incident/ticket attribué. Prioriser selon impact métier, exposition et avis éditeur; appliquer une correction supportée après validation, puis documenter le résultat. Toute action de confinement, révocation ou blocage doit suivre le plan d’incident approuvé et être traçable.

## 📚 Sources officielles

- [Microsoft Defender for Endpoint documentation](https://learn.microsoft.com/microsoft-365/security/defender-endpoint/) — choisir la version, l’édition et le modèle correspondant au déploiement réel.
- [CIS Controls — documentation officielle](https://www.cisecurity.org/controls) — repères de gouvernance et gestion des actifs; adapter au contexte.

> Aucun numéro de version, niveau de licence ni prérequis produit n’est présumé dans cette fiche. Vérifier ces éléments dans le portail éditeur et le contrat de l’organisation avant toute mise en œuvre.