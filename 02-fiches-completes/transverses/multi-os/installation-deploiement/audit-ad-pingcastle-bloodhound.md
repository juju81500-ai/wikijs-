# Auditer Active Directory avec PingCastle et BloodHound en mode défensif

- **OS / Version** : Windows (PingCastle); BloodHound Community Edition multiplateforme, collecteurs selon version
- **Type de fiche** : Installation/Déploiement
- **Environnement** : Domaine AD de laboratoire ou domaine audité avec accord écrit
- **Machine ciblée** : Poste d'audit sécurisé
- **Catégorie** : Audit Active Directory
- **Tags** : `pingcastle`, `bloodhound`, `active-directory`, `audit`, `defensif`

## 1. Périmètre

Évaluer l'hygiène et les chemins d'attaque d'un domaine pour corriger les faiblesses, sans exploitation. La collecte ne se fait que sur un domaine autorisé, avec accord du responsable de l'annuaire et du RSSI.

## 2. Prérequis

- Autorisation écrite précisant domaines, comptes utilisés, durée et traitement des résultats.
- Poste d'audit dédié, durci et chiffré; rapports classés comme données sensibles.
- Compte de lecture du domaine à moindre privilège; éviter les comptes d'administration de domaine.
- Pour BloodHound CE : Docker ou déploiement officiel, jeu de données stocké hors réseau partagé.
- Vérifier les licences de PingCastle (version gratuite pour usage interne, modalités éditeur) avant utilisation dans un cadre commercial.
- Informer l'équipe de détection (EDR/SIEM) : les collecteurs peuvent générer des alertes légitimes.

## 3. Variantes éditeur à distinguer

| Outil | Rôle | Sortie |
|---|---|---|
| PingCastle | Contrôle de santé et score de risque AD | Rapport HTML/XML du domaine |
| BloodHound Community Edition | Cartographie des relations et chemins de privilèges | Graphe consulté dans l'interface web |

Les collecteurs (SharpHound, AzureHound) et leurs options varient selon la version de BloodHound; utiliser ceux publiés avec la version installée.

## 4. Étapes vérifiables

### 4.1 Cadrer et préparer le poste

Isoler le poste d'audit, vérifier l'heure, la résolution DNS du domaine et la connectivité vers un contrôleur de domaine autorisé.

### 4.2 Exécuter PingCastle

Télécharger depuis le site officiel, vérifier la provenance, puis lancer l'outil en mode de contrôle de santé avec un compte autorisé selon la documentation. Conserver le rapport chiffré.

### 4.3 Installer BloodHound CE

Suivre le guide officiel de la version choisie (déploiement conteneurisé), changer immédiatement les mots de passe initiaux et limiter l'accès à localhost ou au réseau d'administration.

### 4.4 Collecter les données

Lancer le collecteur officiel correspondant à la version, avec options minimales et fenêtre convenue. Importer le fichier dans BloodHound.

### 4.5 Analyser défensivement

Prioriser : comptes à privilèges excessifs, délégations non contraintes, chemins vers les groupes sensibles, comptes de service faibles, délégations ACL. Convertir chaque constat en action de remédiation.

### 4.6 Corriger et rescanner

Appliquer les corrections (réduction des droits, modèle d'administration en niveaux, rotation des secrets), puis rejouer l'audit pour mesurer l'amélioration.

## 5. Validation

- Le rapport PingCastle est produit et son score documenté.
- BloodHound affiche les données du domaine autorisé uniquement.
- Chaque constat critique a un propriétaire et une échéance.
- Les données de collecte sont chiffrées ou détruites selon la politique convenue.

## 6. Retour arrière

- Supprimer la base BloodHound et les fichiers de collecte à la fin de la mission.
- Révoquer le compte de lecture utilisé.
- Détruire le poste d'audit ou restaurer son instantané.

## 7. Limites de version et de licence

- Les noms de collecteurs, formats et API évoluent entre versions de BloodHound.
- PingCastle a des conditions de licence à vérifier selon l'usage.
- Les résultats ne remplacent pas une revue manuelle ni une analyse de risque.
- Aucune exploitation des chemins découverts n'est dans le périmètre de cette fiche.

## 8. Verdict historique

**Non testé sur plateforme cible.** Cette fiche est une synthèse documentaire des sources officielles; aucune exécution n'a été réalisée sur les produits, versions ou licences visés. Valider en laboratoire isolé avant production.

## Sources

- [PingCastle — site officiel](https://www.pingcastle.com/)
- [BloodHound Community Edition — documentation](https://bloodhound.specterops.io/)
- [ANSSI — recommandations Active Directory](https://cyber.gouv.fr/)
