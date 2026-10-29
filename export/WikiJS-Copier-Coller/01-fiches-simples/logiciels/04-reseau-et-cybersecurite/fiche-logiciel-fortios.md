# 📄 FortiOS

- **Catégorie** : Réseau et cybersécurité
- **Plateforme** : Appliances
- **Produit (matrice)** : FortiOS / FortiGate, PAN-OS / Palo Alto, Cisco ASA / Firepower, Stormshield
- **Statut dans le pack** : Documentation défensive — administration et gouvernance

## 📚 Couverture dans le pack

Fiche défensive d’administration et de gouvernance. Elle ne remplace pas le guide éditeur spécifique à la version déployée et ne fournit pas de procédure offensive.

## 🧭 Périmètre

Administrer le plan de gestion, les comptes nominatifs et les politiques de sécurité via les interfaces prises en charge par l’éditeur. Séparer les interfaces d’administration du trafic utilisateur, limiter leur exposition aux postes d’administration autorisés, activer MFA lorsque disponible, appliquer RBAC et conserver une sauvegarde chiffrée avant changement. Examiner les journaux d’administration et les avis de sécurité Fortinet; planifier les mises à jour selon le modèle, la version supportée et les dépendances de l’organisation.

## ✅ Autorisation et préparation

Avant toute modification, consigner le propriétaire du service, les actifs et utilisateurs concernés, le ticket de changement, l’approbateur, la fenêtre, les dépendances, les critères d’arrêt et la personne à contacter. Toute évaluation active ou action sur un terminal/équipement exige une autorisation écrite explicite, limitée au périmètre et à la durée approuvés. Sans accord, rester sur l’inventaire géré, les journaux et les contrôles de configuration passifs.

## 🔎 Validation

La recette porte sur la connexion admin autorisée, la disponibilité des flux métier documentés, l’état HA si utilisé, les journaux et la capacité de restaurer la configuration. Aucune règle ou commande de test de trafic n’est fournie ici. Vérifier aussi l’horodatage, la journalisation et l’absence de secrets dans les tickets ou exports; faire approuver le résultat par le propriétaire du service.

## ↩️ Retour arrière

Avant changement, conserver une sauvegarde ou un état de référence protégé, vérifier la possibilité réelle de restauration et garder un accès d’administration de secours approuvé. Si la validation échoue, interrompre le déploiement, restaurer la dernière configuration/package supporté selon la procédure éditeur, vérifier les services dépendants et consigner la cause. Ne pas improviser une procédure de restauration non documentée.

## 🚨 Alertes et remédiation

Préserver les journaux utiles, corréler avec les sources de supervision autorisées et ouvrir un incident/ticket attribué. Prioriser selon impact métier, exposition et avis éditeur; appliquer une correction supportée après validation, puis documenter le résultat. Toute action de confinement, révocation ou blocage doit suivre le plan d’incident approuvé et être traçable.

## 📚 Sources officielles

- [Fortinet FortiGate administration portal](https://docs.fortinet.com/product/fortigate) — choisir la version, l’édition et le modèle correspondant au déploiement réel.
- [CIS Controls — documentation officielle](https://www.cisecurity.org/controls) — repères de gouvernance et gestion des actifs; adapter au contexte.

> Aucun numéro de version, niveau de licence ni prérequis produit n’est présumé dans cette fiche. Vérifier ces éléments dans le portail éditeur et le contrat de l’organisation avant toute mise en œuvre.