# 📄 Authentik

- **Catégorie** : Réseau et cybersécurité
- **Plateforme** : Linux
- **Produit (matrice)** : Keycloak / Authelia / Authentik
- **Statut dans le pack** : Documentation défensive — administration et gouvernance
- **Tags** : `logiciel`, `04-Reseau-et-cybersecurite`, `defensif`, `administration`, `gouvernance`

## 📚 Couverture dans le pack

Fiche défensive d’administration et de gouvernance. Elle ne remplace pas le guide éditeur spécifique à la version déployée et ne fournit pas de procédure offensive.

## 🧭 Périmètre

Complément aux fiches existantes: déployer avec la configuration de production documentée, TLS via le frontal approuvé, stockage durable et sauvegardes protégées; utiliser comptes nominatifs, MFA et rôles minimaux. Protéger les clés, tokens et exports, maintenir les images/packages officiels et examiner les journaux d’administration. Limiter les connecteurs et applications aux besoins autorisés.

## ✅ Autorisation et préparation

Avant toute modification, consigner le propriétaire du service, les actifs et utilisateurs concernés, le ticket de changement, l’approbateur, la fenêtre, les dépendances, les critères d’arrêt et la personne à contacter. Toute évaluation active ou action sur un terminal/équipement exige une autorisation écrite explicite, limitée au périmètre et à la durée approuvés. Sans accord, rester sur l’inventaire géré, les journaux et les contrôles de configuration passifs.

## 🔎 Validation

Valider le flux d’authentification d’un utilisateur pilote, MFA, consentements/groupes, alertes et restauration de sauvegarde. En cas d’échec, revenir à la configuration et aux images précédemment validées, révoquer les jetons concernés et préserver les traces. Vérifier aussi l’horodatage, la journalisation et l’absence de secrets dans les tickets ou exports; faire approuver le résultat par le propriétaire du service.

## ↩️ Retour arrière

Avant changement, conserver une sauvegarde ou un état de référence protégé, vérifier la possibilité réelle de restauration et garder un accès d’administration de secours approuvé. Si la validation échoue, interrompre le déploiement, restaurer la dernière configuration/package supporté selon la procédure éditeur, vérifier les services dépendants et consigner la cause. Ne pas improviser une procédure de restauration non documentée.

## 🚨 Alertes et remédiation

Préserver les journaux utiles, corréler avec les sources de supervision autorisées et ouvrir un incident/ticket attribué. Prioriser selon impact métier, exposition et avis éditeur; appliquer une correction supportée après validation, puis documenter le résultat. Toute action de confinement, révocation ou blocage doit suivre le plan d’incident approuvé et être traçable.

## 📚 Sources officielles

- [authentik official documentation](https://docs.goauthentik.io/) — choisir la version, l’édition et le modèle correspondant au déploiement réel.
- [CIS Controls — documentation officielle](https://www.cisecurity.org/controls) — repères de gouvernance et gestion des actifs; adapter au contexte.

> Aucun numéro de version, niveau de licence ni prérequis produit n’est présumé dans cette fiche. Vérifier ces éléments dans le portail éditeur et le contrat de l’organisation avant toute mise en œuvre.
