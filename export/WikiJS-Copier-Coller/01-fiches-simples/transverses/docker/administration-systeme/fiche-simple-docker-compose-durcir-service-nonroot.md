# 📄 Fiche_Simple_-_Docker_Compose_Durcir_Service_NonRoot.md

- **Environnement** : Hôte Docker Linux
- **OS / Version** : Docker Engine avec Docker Compose v2
- **Catégorie** : Déploiement / Sécurité

## 🎯 Problème précis à résoudre
Réduire les privilèges d'un service Compose avec un utilisateur non-root, un système de fichiers racine en lecture seule et les seules capacités nécessaires.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Vérifier que l'image supporte l'utilisateur choisi et identifier ses besoins d'écriture.
2. Ajouter au service Compose une configuration initiale :
   ```yaml
   services:
     app:
       image: exemple/app:version-fixee
       user: "10001:10001"
       read_only: true
       tmpfs:
         - /tmp:rw,noexec,nosuid,size=64m
       cap_drop:
         - ALL
       security_opt:
         - no-new-privileges:true
       pids_limit: 256
       volumes:
         - app_data:/var/lib/app
   volumes:
     app_data:
   ```
3. Vérifier le fichier et tester le démarrage :
   ```bash
   docker compose config
   docker compose up -d
   docker compose ps
   docker compose logs --tail 100 app
   ```
   👉 *Explication : un service peut nécessiter un chemin temporaire ou une capacité explicite; ne pas ajouter de permissions sans identifier le besoin.*

## ⚡ 2. Production — Façon Simplifiée
1. Confirmer l'UID/GID, les répertoires d'écriture, les ports et les capacités documentés par l'image.
2. Déployer d'abord en préproduction avec `read_only`, `tmpfs` et `cap_drop: ALL`; ajouter ensuite seulement les exceptions nécessaires.
3. Épingler une version d'image approuvée, valider le rendu Compose et contrôler l'état de santé et les journaux après redémarrage.

## 🔒 3. Production — Façon Sécurisée
1. Ne pas utiliser `privileged: true`, le socket Docker hôte ou des montages de système hôte pour contourner les problèmes de permissions.
2. Éviter les tags d'image mobiles comme `latest`; définir les quotas mémoire et CPU selon l'usage attendu.
3. Garder les données persistantes dans des volumes dédiés et limiter les montages en écriture aux seuls chemins requis.

## ✅ Validation et retour arrière
- Confirmer que le processus tourne avec l'UID attendu, que les écritures nécessaires fonctionnent et que les autres chemins sont en lecture seule.
- En cas de régression, restaurer le fichier Compose précédent et redéployer; documenter l'exception de sécurité retenue.
- Ne jamais désactiver le confinement Docker global pour corriger un service isolé.