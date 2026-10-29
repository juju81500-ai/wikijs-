# Fiche_Simple_-_VM_Ubuntu_24.04_Graylog_Installer_Data_Node.md

- **Environnement** : Ubuntu Server 24.04: nœud Graylog + MongoDB et Data Node (laboratoire)
- **OS / Version** : Ubuntu Server 24.04 LTS; Graylog 7.2; MongoDB 8.0
- **Catégorie** : journaux / stockage
- **Tags** : `ubuntu2404`, `graylog`, `datanode`, `mongodb`, `datanode`, `sysctl`

---

## Problème précis à résoudre

Installer le Data Node Graylog sur son hôte dédié.

## 1. Hors-Production (Lab / Test / POC)

1. Installer le paquet de dépôt Graylog 7.2 récupéré depuis `packages.graylog2.org` (origine contrôlée), puis `graylog-datanode` :
   ```bash
   sudo apt update
   sudo apt install graylog-datanode
   ```
   👉 Explication : ne pas déployer OpenSearch séparément avec cette architecture.

2. Définir `vm.max_map_count` à au moins 262144 :
   ```bash
   echo 'vm.max_map_count=262144' | sudo tee /etc/sysctl.d/99-graylog-datanode.conf
   sudo sysctl --system
   ```
   👉 Explication : exigence du moteur de recherche du Data Node.

3. Renseigner `/etc/graylog/datanode/datanode.conf` (secret partagé, URI MongoDB authentifiée, taille de heap) :
   ```bash
   sudoedit /etc/graylog/datanode/datanode.conf
   ```
   👉 Explication : le heap vaut environ la moitié de la RAM, plafonné à 31 Go.

4. Activer le service puis contrôler l'état :
   ```bash
   sudo systemctl enable --now graylog-datanode
   sudo systemctl --no-pager status graylog-datanode
   ```
   👉 Explication : démarre le Data Node.

## 2. Production — Contrôles

Utiliser un stockage dédié, idéalement XFS, pour les données du Data Node.

## 3. Production — Sécurité

- Ne pas mettre le secret en clair dans un ticket.

## Validation et retour arrière

- **Validation** : `graylog-datanode` actif.
- **Retour arrière** : `sudo systemctl disable --now graylog-datanode` et supprimer le fichier sysctl ajouté.

## Si le problème n'est pas résolu

- [Graylog 7.2 — installation Ubuntu](https://go2docs.graylog.org/current/downloading_and_installing_graylog/ubuntu_installation.htm)
- [Graylog — sécuriser l'environnement](https://go2docs.graylog.org/current/planning_your_deployment/secure_your_graylog_environment.htm)
- [Guide complet Graylog Ubuntu 24.04](../../../../../02-Fiches-Completes/Ubuntu/24.04/Installation-Deploiement/49_Deploiement_Graylog_7.2_Ubuntu_24.04.md#4-installer-data-node)
