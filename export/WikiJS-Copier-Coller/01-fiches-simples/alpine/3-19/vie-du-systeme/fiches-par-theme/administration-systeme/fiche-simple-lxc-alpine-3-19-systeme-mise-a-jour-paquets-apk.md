# 📄 Fiche_Simple_-_LXC_Alpine_3.19_Systeme_Mise_A_Jour_Paquets_APK.md

- **Environnement** : LXC Alpine administré depuis Proxmox VE
- **OS / Version** : Alpine Linux 3.19 avec `apk` et OpenRC (version legacy)
- **Catégorie** : Système / Maintenance

## 🎯 Problème précis à résoudre
Contrôler les dépôts et appliquer les mises à jour de paquets Alpine avec `apk`, sans mélanger les branches de versions ni confondre le noyau du conteneur avec celui de l'hôte.

> Alpine 3.19 n'est plus une cible à retenir pour un nouveau déploiement en production. Vérifier le support de la branche et planifier la migration vers une version maintenue.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Identifier la version, les dépôts configurés et les paquets susceptibles d'être mis à jour :
   ```sh
   cat /etc/alpine-release
   cat /etc/apk/repositories
   apk update
   apk list -u
   ```
2. Appliquer la mise à jour dans le laboratoire puis contrôler les changements :
   ```sh
   apk upgrade
   apk info -v
   ```
   👉 *Explication : `apk upgrade` met à jour les paquets selon les dépôts configurés; relire leur branche avant de confirmer en production.*

## ⚡ 2. Production — Façon Simplifiée
1. Sauvegarder les données et la configuration du CT; relever son état et vérifier l'espace disque.
2. Confirmer que `/etc/apk/repositories` ne mélange pas des versions de branches différentes, puis appliquer :
   ```sh
   apk update
   apk upgrade
   ```
3. Contrôler les services OpenRC concernés et tester les applications après la mise à jour :
   ```sh
   rc-status
   apk info -v
   ```
   👉 *Explication : un LXC partage le noyau de l'hôte; une mise à jour du noyau se gère côté Proxmox, pas par `apk` dans le CT.*

## 🔒 3. Production — Façon Sécurisée
1. Ne pas modifier les dépôts d'une ancienne version pour les pointer vers une autre branche majeure en guise de mise à niveau; suivre une procédure de migration testée.
2. Ne pas utiliser `apk upgrade --available` sans comprendre ses effets, notamment les éventuels changements de versions de paquets.
3. Planifier les redémarrages et valider les services; garder une sauvegarde restaurable et un accès console Proxmox.

## ✅ Validation et retour arrière
- Vérifier la version, les services, les journaux OpenRC et le fonctionnement applicatif après la mise à jour.
- Si un paquet casse un service, examiner les changements et restaurer le CT depuis la sauvegarde ou le snapshot cohérent validé.
- Ne pas considérer un snapshot seul comme une sauvegarde indépendante.