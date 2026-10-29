# 📄 Fiche_Simple_-_Docker_Production_Reconstruire_Hote_Restaurer_Stacks.md

- **Environnement** : Nouvel hôte Linux Docker remplaçant un hôte indisponible
- **OS / Version** : Debian 12 ou Ubuntu 24.04 selon la plateforme Docker source
- **Catégorie** : Production / Reprise après sinistre

## 🎯 Problème précis à résoudre
Reconstruire un hôte Docker et restaurer ses stacks à partir des fichiers de déploiement, des secrets récupérés de façon contrôlée et des sauvegardes de données testées.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Préparer une VM isolée avec la distribution et les versions moteur/Compose documentées.
2. Restaurer les fichiers Compose depuis leur dépôt, puis récupérer les secrets depuis le coffre prévu; ne pas mettre les secrets dans Git ou dans le YAML.
3. Restaurer volumes et bases de données dans un projet isolé, adapter les ports/DNS de test, puis lancer :
   ```bash
   docker compose config -q
   docker compose up -d
   docker compose ps
   ```
4. Tester les fonctions métiers, données, healthchecks et journaux.
   👉 *Explication : un test isolé valide les sauvegardes sans créer de conflit d'IP, de DNS ou de nom de service avec la production.*

## ⚡ 2. Production — Façon Simplifiée
1. Installer un hôte propre et à jour; appliquer la fiche existante d'installation Docker Engine et valider le stockage, le réseau et le pare-feu.
2. Restaurer les dossiers Compose, données et configurations depuis des sources authentifiées; contrôler propriétaires, permissions, versions et espace disponible.
3. Restaurer les bases avec leurs outils natifs et les volumes arrêtés, puis démarrer les services selon l'ordre des dépendances.
4. Valider chaque service en local et depuis un client autorisé avant de basculer IP, DNS, proxy ou VIP.
   👉 *Explication : ne pas restaurer des fichiers de `/var/lib/docker` directement sur un moteur neuf, sauf procédure explicitement testée pour cette version.*

## 🔒 3. Production — Façon Sécurisée
1. Révoquer/remplacer les secrets qui ont pu être exposés avec l'ancien hôte et vérifier les accès administrateurs.
2. Appliquer le durcissement, les règles de pare-feu et la supervision avant d'exposer les services.
3. Maintenir l'ancien système isolé et éteint; éviter que les deux hôtes utilisent simultanément les mêmes adresses ou exécutent les mêmes tâches planifiées.

## ✅ Validation et retour arrière
- Comparer les inventaires de services, images, ports, volumes et données avec l'état source documenté.
- Tester l'accès client, les sauvegardes suivantes et un retour vers l'ancien hôte avant décommissionnement.
- Si la restauration est incomplète, conserver le nouvel hôte isolé et remettre l'ancien service seulement après confirmation de l'absence d'écritures concurrentes.