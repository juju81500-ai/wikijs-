# 📄 Fiche_Simple_-_Docker_Reseau_Diagnostic_Reseaux_Compose.md

- **Environnement** : Hôte Docker Linux
- **OS / Version** : Docker Engine et Docker Compose v2
- **Catégorie** : Réseau / Diagnostic
- **Tags** : `[docker]`, `[compose]`, `[reseau]`, `[dns]`, `[diagnostic]`

## 🎯 Problème précis à résoudre
Diagnostiquer la connectivité et la résolution de noms entre services Docker Compose et l'hôte, sans supprimer ni contourner les règles de pare-feu du moteur.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Identifier les conteneurs, leurs réseaux et leurs adresses :
   ```bash
   docker compose ps
   docker network ls
   docker network inspect <nom-reseau-compose>
   ```
2. Tester la résolution du nom de service depuis un conteneur du même réseau :
   ```bash
   docker compose exec app getent hosts db
   ```
   👉 *Explication : remplacer `app` et `db` par les noms de services; l'image doit contenir `getent`.*

## ⚡ 2. Production — Façon Simplifiée
1. Contrôler que les services attendus sont attachés au même réseau Compose :
   ```bash
   docker inspect --format '{{json .NetworkSettings.Networks}}' "$(docker compose ps -q app)"
   docker network inspect <nom-reseau-compose>
   ```
2. Depuis un conteneur de diagnostic autorisé et attaché au réseau, vérifier DNS et port applicatif :
   ```bash
   docker run --rm --network <nom-reseau-compose> busybox nslookup db
   docker run --rm --network <nom-reseau-compose> busybox nc -zvw 3 db 5432
   ```
3. Vérifier les ports publiés et l'adresse d'écoute du service :
   ```bash
   docker compose port app 8080
   docker compose logs --tail 100 app
   ```
   👉 *Explication : tester le port interne depuis le réseau Docker et le port publié depuis une machine cliente; ils ne sont pas nécessairement identiques.*

## 🔒 3. Production — Façon Sécurisée
1. Ne pas publier un port de base de données sur toutes les interfaces si seuls les conteneurs internes en ont besoin.
2. Ne pas appliquer `iptables -F`, `nft flush ruleset` ou désactiver le pare-feu pour diagnostiquer Docker; cela peut interrompre des services et exposer l'hôte.
3. Limiter le nombre de réseaux et les services connectés; un réseau partagé donne une connectivité directe entre ses membres.

## ✅ Validation et retour arrière
- Confirmer la résolution par nom de service, la connectivité au port requis et l'exposition attendue depuis l'hôte.
- Si un changement Compose échoue, restaurer le fichier précédent puis redéployer; ne pas supprimer un réseau utilisé par d'autres services.
- Examiner les règles et journaux du pare-feu de l'hôte si le trafic reste bloqué.