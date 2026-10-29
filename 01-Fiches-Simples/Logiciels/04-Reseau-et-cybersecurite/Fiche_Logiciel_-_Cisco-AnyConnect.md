# 📄 Cisco AnyConnect

- **Catégorie** : Réseau et cybersécurité
- **Plateforme** : Multiplateforme
- **Produit (matrice)** : Cisco AnyConnect / FortiClient / GlobalProtect
- **Statut dans le pack** : Documentation défensive — administration et gouvernance
- **Tags** : `logiciel`, `04-Reseau-et-cybersecurite`, `defensif`, `administration`, `gouvernance`

## 📚 Couverture dans le pack

Fiche défensive d’administration et de gouvernance. Elle ne remplace pas le guide éditeur spécifique à la version déployée et ne fournit pas de procédure offensive.

## 🧭 Périmètre

Déployer les clients depuis les canaux officiels et le profil géré, avec authentification forte, groupes d’accès minimaux, vérification des certificats et politiques adaptées aux terminaux gérés. Contrôler la compatibilité de la version avec la passerelle et le système avant diffusion; éviter les profils génériques partagés et protéger les journaux utilisateurs.

## ✅ Autorisation et préparation

Avant toute modification, consigner le propriétaire du service, les actifs et utilisateurs concernés, le ticket de changement, l’approbateur, la fenêtre, les dépendances, les critères d’arrêt et la personne à contacter. Toute évaluation active ou action sur un terminal/équipement exige une autorisation écrite explicite, limitée au périmètre et à la durée approuvés. Sans accord, rester sur l’inventaire géré, les journaux et les contrôles de configuration passifs.

## 🔎 Validation

Déployer d’abord sur un groupe pilote, valider connexion des utilisateurs autorisés, MFA, accès aux seules ressources attendues, mise à jour et remontée des journaux. En cas d’incident, suspendre le lot, rétablir le package/profil précédent supporté et révoquer les accès concernés. Vérifier aussi l’horodatage, la journalisation et l’absence de secrets dans les tickets ou exports; faire approuver le résultat par le propriétaire du service.

## ↩️ Retour arrière

Avant changement, conserver une sauvegarde ou un état de référence protégé, vérifier la possibilité réelle de restauration et garder un accès d’administration de secours approuvé. Si la validation échoue, interrompre le déploiement, restaurer la dernière configuration/package supporté selon la procédure éditeur, vérifier les services dépendants et consigner la cause. Ne pas improviser une procédure de restauration non documentée.

## 🚨 Alertes et remédiation

Préserver les journaux utiles, corréler avec les sources de supervision autorisées et ouvrir un incident/ticket attribué. Prioriser selon impact métier, exposition et avis éditeur; appliquer une correction supportée après validation, puis documenter le résultat. Toute action de confinement, révocation ou blocage doit suivre le plan d’incident approuvé et être traçable.

## 📚 Sources officielles

- [Cisco AnyConnect Secure Mobility Client support and documentation](https://www.cisco.com/c/en/us/support/security/anyconnect-secure-mobility-client/series.html) — choisir la version, l’édition et le modèle correspondant au déploiement réel.
- [CIS Controls — documentation officielle](https://www.cisecurity.org/controls) — repères de gouvernance et gestion des actifs; adapter au contexte.

> Aucun numéro de version, niveau de licence ni prérequis produit n’est présumé dans cette fiche. Vérifier ces éléments dans le portail éditeur et le contrat de l’organisation avant toute mise en œuvre.
