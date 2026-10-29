# Fiche simple — Ubuntu : vérifier la santé d'un cluster Ceph

- **OS / Version** : Ubuntu Server, compatible avec les commandes Ceph du cluster
- **Catégorie** : Stockage distribué / diagnostic

## Avant les contrôles

Exécuter les commandes depuis un hôte d'administration disposant du CLI et d'une identité Ceph autorisée. Protéger `client.admin` et les keyrings; ne pas les copier dans un ticket ou une session partagée.

## État général

```bash
ceph -s
ceph health detail
ceph quorum_status --format json-pretty
ceph orch host ls --detail
```
   👉 Explication : donne l'état global, le détail des alertes, le quorum et les hôtes du cluster.

Interpréter `HEALTH_WARN` ou `HEALTH_ERR` avec le détail complet; ne pas masquer une alerte pour obtenir artificiellement `HEALTH_OK`.

## OSD, capacité et services

```bash
ceph osd tree
ceph orch ps
ceph orch device ls
ceph df
ceph pg stat
```
   👉 Explication : affiche arbre OSD, services, disques, capacité et groupes de placement.

Contrôler que les OSD attendus sont `up` et `in`, que les PG sont `active+clean`, que les hôtes sont présents et que l'espace permet la récupération après une panne.

## Logs et interventions

```bash
ceph log last cephadm
sudo journalctl -u 'ceph-*' --since '30 minutes ago' --no-pager
```
   👉 Explication : lit les journaux cephadm et des services Ceph des 30 dernières minutes.

Privilégier la collecte d'état et de journaux avant toute action. Ne pas redémarrer plusieurs OSD ensemble, retirer un hôte, purger le cluster, lancer `--zap` ou appliquer `--all-available-devices` sans procédure approuvée, sauvegarde et aperçu vérifié.

## Source

- [Ceph Tentacle — Health checks](https://docs.ceph.com/en/tentacle/rados/operations/health-checks/)
- Guide complet : `02-Fiches-Completes/Ubuntu-Server/Installation-Deploiement/67_Deploiement_Ceph_Tentacle_20_2_4_Ubuntu_22_04.md`