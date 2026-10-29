# 📄 Fiche_Simple_-_VM_Rocky_9_Stockage_Configurer_Quotas_Projet_XFS.md

- **Environnement** : VM Rocky Linux avec système de fichiers XFS dédié aux données
- **OS / Version** : Rocky Linux 9 / RHEL 9
- **Catégorie** : Stockage / Administration

## 🎯 Problème précis à résoudre
Définir un quota de projet XFS pour limiter l'espace utilisé par un répertoire partagé, sans confondre les quotas de projet avec les quotas par utilisateur.

## 🧪 1. Hors-Production (Lab / Test / POC)

1. Vérifier le type de système de fichiers et installer les outils :
   ```bash
   findmnt -no SOURCE,FSTYPE,OPTIONS /srv/projets
   sudo dnf install xfsprogs
   ```
   👉 Explication : le quota de projet n'existe que sur XFS.

2. Monter XFS avec les quotas de projet en lab uniquement :
   ```bash
   sudo mount -o remount,prjquota /srv/projets
   findmnt -no OPTIONS /srv/projets
   ```
   👉 Explication : sur XFS, l'option de quota se change à chaud seulement selon le noyau; sinon l'ajouter dans `/etc/fstab` puis démonter/remonter hors production.

3. Définir un projet de test :
   ```bash
   echo '100:/srv/projets/equipe-a' | sudo tee -a /etc/projects
   echo 'equipe-a:100' | sudo tee -a /etc/projid
   ```
   👉 Explication : associe l'identifiant 100 au répertoire et au nom de projet `equipe-a`.

4. Initialiser puis appliquer un quota :
   ```bash
   sudo xfs_quota -x -c 'project -s equipe-a' /srv/projets
   sudo xfs_quota -x -c 'limit -p bsoft=9g bhard=10g equipe-a' /srv/projets
   sudo xfs_quota -x -c 'report -p -h' /srv/projets
   ```
   👉 Explication : limite douce 9 Go, limite dure 10 Go, puis rapport d'utilisation.

## ⚡ 2. Production — Façon Simplifiée
1. Sauvegarder `/etc/fstab`, confirmer que le point de montage est XFS et inscrire `prjquota` dans les options persistantes de la ligne concernée.
2. Planifier la prise en compte du montage, puis configurer `/etc/projects` et `/etc/projid` avec un identifiant unique et le chemin exact du projet.
3. Initialiser les métadonnées et appliquer des seuils adaptés au stockage :
   ```bash
   sudo xfs_quota -x -c 'project -s equipe-a' /srv/projets
   sudo xfs_quota -x -c 'limit -p bsoft=9g bhard=10g equipe-a' /srv/projets
   sudo xfs_quota -x -c 'report -p -h' /srv/projets
   ```
   👉 *Explication : la limite souple peut être dépassée temporairement; la limite dure bloque les nouvelles allocations lorsqu'elle est atteinte.*

## 🔒 3. Production — Façon Sécurisée
1. Ne pas appliquer ces options à ext4 ou à un point de montage différent; confirmer le volume cible avec `findmnt`.
2. Utiliser un identifiant projet unique et vérifier que le chemin ne chevauche pas un autre projet.
3. Avertir les utilisateurs et surveiller les seuils; un quota mal dimensionné peut interrompre des applications.

## ✅ Validation et retour arrière
- Vérifier les options de montage persistantes et le rapport `xfs_quota -x -c 'report -p -h' /srv/projets`.
- Tester avec un compte appartenant au projet et confirmer le comportement aux seuils en lab.
- Pour annuler, retirer la limite exacte et nettoyer uniquement l'entrée de projet validée après vérification des dépendances.