# Fiche_Simple_-_VM_Ubuntu_Ceph_Installer_Cephadm_Bootstrap.md

- **Environnement** : Cluster Ceph de laboratoire à trois nœuds (ceph01, ceph02, ceph03) géré par cephadm
- **OS / Version** : Ubuntu Server 22.04 LTS; Ceph Tentacle 20.2.4
- **Catégorie** : stockage / cluster Ceph
- **Tags** : `ubuntu2204`, `ceph`, `tentacle`, `cephadm`

---

## Problème précis à résoudre

Installer cephadm et créer le premier MON/MGR du cluster avec `cephadm bootstrap`.

## 1. Hors-Production (Lab / Test / POC)

1. Sur `ceph01`, installer cephadm :
   ```bash
   sudo apt update
   sudo apt install cephadm
   cephadm --version
   ```
   👉 Explication : installe l'outil de déploiement depuis les dépôts Ubuntu et contrôle sa version.

2. Ajouter le dépôt de la release Tentacle et installer les outils :
   ```bash
   sudo cephadm add-repo --release tentacle
   sudo cephadm install cephadm
   sudo cephadm install ceph-common
   ceph -v
   ```
   👉 Explication : aligne cephadm sur la version Tentacle retenue et installe la commande `ceph`.

3. Amorcer le cluster (remplacer l'IP du MON et le réseau de réplication par ceux du lab) :
   ```bash
   sudo cephadm bootstrap \
     --mon-ip 10.20.0.11 \
     --cluster-network 10.30.0.0/24
   ```
   👉 Explication : crée le premier MON et MGR, la clé SSH de gestion, la configuration et le trousseau `client.admin`; omettre `--cluster-network` si le lab n'a pas de réseau de réplication distinct.

4. Noter l'URL du Dashboard affichée à la fin, sans consigner le mot de passe dans un document.
   👉 Explication : le mot de passe initial est un secret à placer dans le coffre.

5. Contrôler l'état du cluster :
   ```bash
   sudo ceph -s
   sudo ceph orch status
   sudo ceph orch host ls
   ```
   👉 Explication : `HEALTH_WARN` est normal tant que les OSD et MON supplémentaires ne sont pas déployés.

## 2. Production — Contrôles

Vérifier avant bootstrap que les deux adresses du nœud sont locales et que les réseaux sont corrects; planifier la protection de `/etc/ceph` et des clés.

## 3. Production — Sécurité

- Protéger `/etc/ceph`, les clés SSH et toute copie du trousseau `client.admin` comme des secrets d'administration.
- Ne jamais afficher ni coller le mot de passe du Dashboard dans un ticket.

## Validation et retour arrière

- **Validation** : `sudo ceph -s` répond et `sudo ceph orch host ls` liste `ceph01`.
- **Retour arrière** : en lab uniquement, supprimer le cluster avec la procédure officielle `cephadm rm-cluster` après avoir confirmé qu'aucune donnée n'est à conserver; jamais sur un cluster utile.

## Si le problème n'est pas résolu

- [Ceph — bootstrap](https://docs.ceph.com/en/tentacle/cephadm/install/#bootstrap-a-new-cluster)
- [Ceph Tentacle — cephadm](https://docs.ceph.com/en/tentacle/cephadm/install/)
- [Guide complet](../../../../../02-Fiches-Completes/Ubuntu/22.04/Installation-Deploiement/67_Deploiement_Ceph_Tentacle_20_2_4_Ubuntu_22_04.md#3-installer-cephadm-et-amorcer-le-cluster)
