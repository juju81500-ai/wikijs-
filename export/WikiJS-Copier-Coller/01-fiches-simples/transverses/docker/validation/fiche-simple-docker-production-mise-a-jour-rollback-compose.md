# 📄 Fiche_Simple_-_Docker_Production_Mise_A_Jour_Rollback_Compose.md

- **Environnement** : Hôte Docker Linux exécutant une stack Compose
- **OS / Version** : Docker Engine et Docker Compose v2
- **Catégorie** : Production / Maintenance / Déploiement

## 🎯 Problème précis à résoudre
Mettre à jour une stack Compose avec des images versionnées, sauvegarder les données, valider le service puis revenir en arrière sans détruire les volumes.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Relever les versions et l'état avant changement :
   ```bash
   docker compose ps
   docker compose images
   docker compose config -q
   ```
2. Créer une sauvegarde cohérente des bases et fichiers persistants; ne pas lancer la mise à jour sans méthode de restauration testée.
3. Modifier les tags vers une version approuvée, puis télécharger et appliquer :
   ```bash
   docker compose pull
   docker compose up -d
   docker compose ps
   ```
   👉 *Explication : épingler une version explicite; ne pas utiliser `latest` comme mécanisme de mise à jour ou de retour arrière.*

## ⚡ 2. Production — Façon Simplifiée
1. Programmer une fenêtre, vérifier l'espace disque, consigner les tags actuels et sauvegarder base de données et volumes.
2. Mettre à jour une dépendance à la fois si nécessaire; valider le rendu puis appliquer :
   ```bash
   docker compose config -q
   docker compose pull
   docker compose up -d --wait
   docker compose ps
   ```
3. Tester le parcours métier, la santé, les journaux et les connexions aux dépendances avant de fermer la fenêtre.
4. Pour un rollback, rétablir les tags précédents et redéployer :
   ```bash
   docker compose up -d
   docker compose ps
   ```
   👉 *Explication : si la nouvelle version a migré un schéma de base, revenir uniquement à l'ancienne image peut échouer; restaurer alors la sauvegarde cohérente selon le plan applicatif.*

## 🔒 3. Production — Façon Sécurisée
1. Lire les notes de version et vérifier les migrations incompatibles avant mise à jour.
2. Ne jamais utiliser `docker compose down -v` pendant une mise à jour : l'option supprime les volumes gérés concernés.
3. Garder les anciennes images et sauvegardes jusqu'à l'expiration de la période de validation; ne pas supprimer des données pour libérer de l'espace sans inventaire.

## ✅ Validation et retour arrière
- Confirmer les tags exacts, l'état des healthchecks, les journaux et le parcours applicatif depuis un client.
- Tester le rollback en préproduction, y compris les migrations et la restauration des données.
- Enregistrer l'heure, les versions, résultats et décisions de bascule.