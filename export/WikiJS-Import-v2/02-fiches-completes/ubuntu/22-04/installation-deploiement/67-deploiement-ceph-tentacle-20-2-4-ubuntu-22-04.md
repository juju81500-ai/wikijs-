---
title: "Déployer un cluster Ceph Tentacle avec cephadm sur Ubuntu 22.04"
description: "Fiche simple : [cadrer le périmètre Ceph](../../../../01-Fiches-Simples/Ubuntu/Toutes-versions/Vie-du-logiciel/Ceph/FicheSimple-VMUbuntuCephCadrerPerimetre.md)."
published: true
date: 2026-10-29T20:14:10Z
tags: ["ubuntu2204", "ceph", "tentacle", "cephadm", "rados", "rbd", "storage"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Déployer un cluster Ceph Tentacle avec cephadm sur Ubuntu 22.04

- **OS / Version** : Ubuntu Server 22.04 LTS; Ceph Tentacle 20.2.4
- **Type de fiche** : Installation/Déploiement
- **Rôle** : Cluster Ceph de laboratoire avec MON, MGR, OSD et pool RBD pilote
- **Tags** : `ubuntu2204`, `ceph`, `tentacle`, `cephadm`, `rados`, `rbd`, `storage`

## 1. Périmètre et prérequis

Fiche simple : [cadrer le périmètre Ceph](/01-fiches-simples/ubuntu/toutes-versions/vie-du-logiciel/ceph/fiche-simple-vm-ubuntu-ceph-cadrer-perimetre).

Ce guide crée un cluster de test avec trois nœuds, trois domaines de panne distincts et stockage dédié aux OSD. Il ne couvre ni CephFS, ni RGW, ni iSCSI, ni l'intégration de production avec Proxmox ou OpenStack. Une VM mono-nœud n'est pas un cluster HA et ne valide pas la résilience.

La documentation de Ceph Tentacle classe Ubuntu 22.04 parmi les plateformes sur lesquelles Ceph fournit des paquets et réalise des tests complets. La documentation Ceph ne liste pas Debian 13 pour cette version.

Préparer trois hôtes `ceph01`, `ceph02`, `ceph03`, résolus par DNS, synchronisés par Chrony/NTP et administrables par SSH. Chaque hôte doit avoir un disque système séparé et au moins un disque de données inutilisé, dédié à Ceph. Prévoir une interface/réseau public Ceph et, pour ce cluster de test, une seconde interface dédiée au trafic de réplication. Utiliser des adresses RFC1918 réservées au lab; ne pas copier les exemples tels quels.

Ceph demande beaucoup de ressources disque, RAM et réseau. Un réseau de production 10 Gb/s ou supérieur et du matériel de stockage avec protection contre la perte d'alimentation sont des recommandations de Ceph, pas des exigences que ce petit lab prouve.

## 2. Préparer les nœuds

Fiche simple : [préparer les nœuds Ceph](/01-fiches-simples/ubuntu/toutes-versions/vie-du-logiciel/ceph/fiche-simple-vm-ubuntu-ceph-preparer-noeuds).

Sur chaque hôte, fixer les noms, adresses, résolutions réciproques, DNS, NTP et routes des deux réseaux. Remplacer les exemples suivants par le plan du lab :

| Hôte | Réseau public Ceph | Réseau cluster |
|---|---|---|
| ceph01 | 10.20.0.11/24 | 10.30.0.11/24 |
| ceph02 | 10.20.0.12/24 | 10.30.0.12/24 |
| ceph03 | 10.20.0.13/24 | 10.30.0.13/24 |

Sur chacun :

```bash
hostnamectl
timedatectl status
ip -br address
ip route
getent hosts ceph01 ceph02 ceph03
sudo apt update
sudo apt full-upgrade
sudo apt install chrony lvm2 podman
sudo systemctl enable --now chrony
```

Redémarrer si le noyau ou des bibliothèques critiques ont été mis à jour, puis vérifier que Chrony est synchronisé et que les noms retournent les bonnes adresses. Préparer une règle de pare-feu entre les nœuds pour les ports Ceph de la version sélectionnée; au minimum prévoir les ports Monitor 3300/6789 et les ports daemon Ceph de la plage 6800-7568/TCP. Restreindre l'accès aux interfaces et sous-réseaux Ceph, sans exposition Internet.

Ne pas installer les paquets `ceph-osd` indépendamment sur les nœuds gérés par cephadm : la documentation met en garde contre les conflits de gestion. Laisser cephadm préparer les dépendances requises.

## 3. Installer cephadm et amorcer le cluster

Fiche simple : [installer cephadm et amorcer le cluster](/01-fiches-simples/ubuntu/toutes-versions/vie-du-logiciel/ceph/fiche-simple-vm-ubuntu-ceph-installer-cephadm-bootstrap).

Sur `ceph01`, suivre la méthode cephadm officielle correspondant à la version retenue. La documentation décrit `apt install cephadm` pour Ubuntu, puis l'ajout du dépôt de release et l'installation de l'outil :

```bash
sudo apt update
sudo apt install cephadm
cephadm --version
sudo cephadm add-repo --release tentacle
sudo cephadm install cephadm
sudo cephadm install ceph-common
ceph -v
```

Avant le bootstrap, vérifier que les deux adresses du nœud sont locales et que les réseaux sont corrects. Le bootstrap crée le premier MON et MGR, une clé SSH de gestion, le fichier de configuration et un trousseau `client.admin` privilégié : protéger `/etc/ceph`, les clés SSH et les copies du trousseau comme des secrets d'administration.

```bash
sudo cephadm bootstrap \
  --mon-ip 10.20.0.11 \
  --cluster-network 10.30.0.0/24
```

Si le lab n'a pas un réseau de réplication distinct, omettre `--cluster-network`; ne pas inventer ce réseau. Conserver l'URL Dashboard donnée à la fin, puis se connecter au CLI :

```bash
sudo ceph -s
sudo ceph orch status
sudo ceph orch host ls
```

La disponibilité initiale peut être `HEALTH_WARN` tant que les OSD ou Monitor supplémentaires ne sont pas déployés.

## 4. Ajouter les nœuds et les Monitors

Fiche simple : [ajouter les nœuds et les Monitors](/01-fiches-simples/ubuntu/toutes-versions/vie-du-logiciel/ceph/fiche-simple-vm-ubuntu-ceph-ajouter-noeuds-monitors).

Récupérer la clé publique SSH et l'installer sur les deux nœuds secondaires; le canal SSH et l'accès root/sudo sans interaction doivent être approuvés et vérifiés avant ajout :

```bash
sudo ssh-copy-id -f -i /etc/ceph/ceph.pub root@ceph02
sudo ssh-copy-id -f -i /etc/ceph/ceph.pub root@ceph03
```

Ajouter les hôtes en précisant leur adresse de réseau public, puis vérifier l'inventaire :

```bash
sudo ceph orch host add ceph02 10.20.0.12
sudo ceph orch host add ceph03 10.20.0.13
sudo ceph cephadm check-host ceph02
sudo ceph cephadm check-host ceph03
sudo ceph orch host ls --detail
```

Étendre les MON à trois hôtes et vérifier l'aperçu de placement :

```bash
sudo ceph orch apply mon --placement="ceph01,ceph02,ceph03" --dry-run
```

Examiner l'aperçu, puis appliquer le même placement sans `--dry-run` :

```bash
sudo ceph orch apply mon --placement="ceph01,ceph02,ceph03"
sudo ceph quorum_status --format json-pretty
```

Ne pas retirer de MON pendant que le quorum n'est pas confirmé. Le nombre impair de MON répartis sur des hôtes distincts est nécessaire pour tolérer une panne sans perdre la majorité.

## 5. Ajouter des OSD sans consommer le mauvais disque

Fiche simple : [ajouter des OSD sans consommer le mauvais disque](/01-fiches-simples/ubuntu/toutes-versions/vie-du-logiciel/ceph/fiche-simple-vm-ubuntu-ceph-ajouter-osd).

Sur tous les hôtes, vérifier l'identité, le numéro de série, les partitions et l'absence de données à conserver :

```bash
lsblk -o NAME,SIZE,MODEL,SERIAL,FSTYPE,MOUNTPOINTS
sudo ceph orch device ls --wide
```

Un disque disponible pour un OSD doit être vide, non monté et sans partitions, système de fichiers, LVM ou ancien OSD. **Ne pas utiliser `--all-available-devices` dans cette procédure** : les spécifications `ceph orch apply` sont persistantes et peuvent consommer automatiquement les disques disponibles ajoutés plus tard.

Ne continuer qu'après validation physique des disques de données et de leurs chemins stables `/dev/disk/by-id/`. Un chemin n'est valide que sur l'hôte où le périphérique a été identifié. Exemple de fichier multi-document, avec une spécification par hôte et un unique disque de données dédié par nœud :

```yaml
service_type: osd
service_id: lab-ceph01
placement:
  hosts: [ceph01]
spec:
  data_devices:
    paths:
      - /dev/disk/by-id/<ceph01-data-disk-id>
---
service_type: osd
service_id: lab-ceph02
placement:
  hosts: [ceph02]
spec:
  data_devices:
    paths:
      - /dev/disk/by-id/<ceph02-data-disk-id>
---
service_type: osd
service_id: lab-ceph03
placement:
  hosts: [ceph03]
spec:
  data_devices:
    paths:
      - /dev/disk/by-id/<ceph03-data-disk-id>
```

Chaque `service_id` est unique et chaque spécification cible un seul hôte. D'abord examiner l'aperçu :

```bash
sudo ceph orch apply -i /root/osd-lab.yaml --dry-run
```

Comparer chaque disque prévu à l'inventaire par hôte. L'application efface les métadonnées et le contenu du périphérique ciblé; ne continuer qu'avec des disques vierges autorisés et un aperçu correspondant exactement. Puis appliquer :

```bash
sudo ceph orch apply -i /root/osd-lab.yaml --dry-run
sudo ceph orch apply -i /root/osd-lab.yaml
sudo ceph orch ps --daemon-type osd
sudo ceph osd tree
```

La création d'OSD efface les métadonnées et le contenu du disque sélectionné. Ne pas l'exécuter sur un disque système, un disque monté, un disque partagé avec une VM ou un volume contenant des données. Suivre la progression jusqu'à la fin de la récupération avant tout autre changement.

## 6. Créer un pool RBD pilote

Fiche simple : [créer un pool RBD pilote](/01-fiches-simples/ubuntu/toutes-versions/vie-du-logiciel/ceph/fiche-simple-vm-ubuntu-ceph-pool-rbd-pilote).

Ne créer le pool qu'après vérification de la capacité totale et de la distribution des OSD. Un pool répliqué par défaut de trois copies nécessite plusieurs domaines de panne capables de contenir ces copies.

```bash
sudo ceph osd pool create lab-rbd
sudo rbd pool init lab-rbd
sudo rbd create lab-rbd/test-image --size 1G
sudo rbd ls lab-rbd
sudo rbd rm lab-rbd/test-image
```

Ce test crée puis supprime un petit objet RBD. En production, choisir une règle CRUSH, le nombre de copies, le quota, les capacités et les droits des clients selon les exigences du service; ne pas réutiliser `client.admin` pour des clients applicatifs.

## 7. Contrôler et exploiter

Fiche simple : [contrôler et exploiter le cluster](/01-fiches-simples/ubuntu/toutes-versions/vie-du-logiciel/ceph/fiche-simple-vm-ubuntu-ceph-controler-exploiter).

```bash
sudo ceph -s
sudo ceph health detail
sudo ceph orch host ls --detail
sudo ceph orch ps
sudo ceph orch device ls
sudo ceph osd tree
sudo ceph df
```

Avant de déclarer le cluster prêt, vérifier les trois hôtes, le quorum des MON, la présence d'un MGR actif, les OSD `up` et `in`, des PG `active+clean`, l'absence de health check inexpliqué et l'espace restant. Surveiller les journaux avec `journalctl -u ceph-<fsid>@<daemon>`, la latence, les erreurs disque et les événements de récupération.

Pour un essai d'indisponibilité, ne couper qu'un seul hôte ou OSD à la fois, et seulement après confirmation que la redondance reste suffisante. Ce test doit avoir une procédure de retour arrière et ne doit pas viser une charge de production.

## 8. Sauvegarde, mise à niveau et retrait

Fiche simple : [sauvegarde, mise à niveau et retrait](/01-fiches-simples/ubuntu/toutes-versions/vie-du-logiciel/ceph/fiche-simple-vm-ubuntu-ceph-sauvegarde-upgrade-retrait).

La réplication Ceph protège contre certaines pannes de composants; **elle ne remplace pas une sauvegarde indépendante**. Sauvegarder les données par le mécanisme de l'application cliente et tester leur restauration depuis un système distinct. Protéger séparément les clés d'administration, l'inventaire et les spécifications de service.

Avant toute mise à niveau, confirmer que la version est active, lire les release notes et la procédure d'upgrade de cephadm; vérifier que le cluster est sain et que les clients sont compatibles. Ne jamais mettre à niveau les nœuds individuellement avec un `apt full-upgrade` non coordonné.

Le retrait d'un hôte/OSD déclenche une migration de données. Lire le statut `ceph orch osd rm status`, attendre que les PG soient redistribués et que la capacité restante soit suffisante. Ne pas employer `--force`, `--zap`, `ceph orch host rm --offline --force` ni une purge de cluster pour du dépannage courant : ces options peuvent provoquer une perte de données.

## 9. Limites de validation

Fiche simple : [limites de validation](/01-fiches-simples/ubuntu/toutes-versions/vie-du-logiciel/ceph/fiche-simple-vm-ubuntu-ceph-limites-validation).

Le guide cible Ceph Tentacle 20.2.4 et Ubuntu 22.04, répertorié dans la matrice Ceph comme plateforme testée. Les adresses de réseau et disques sont des exemples de lab. Aucune commande de cluster ni opération de stockage n'a été exécutée dans ce workspace; l'installation, le placement CRUSH, l'OSD et la restauration doivent être testés sur des VM/disques vierges dédiés avant usage.

## Sources

- [Ceph Tentacle — Versions actives](https://docs.ceph.com/en/tentacle/releases/)
- [Ceph Tentacle — Recommandations OS](https://docs.ceph.com/en/tentacle/start/os-recommendations/)
- [Ceph Tentacle — Déployer un cluster avec cephadm](https://docs.ceph.com/en/tentacle/cephadm/install/)
- [Ceph Tentacle — Gestion des hôtes](https://docs.ceph.com/en/tentacle/cephadm/host-management/)
- [Ceph Tentacle — Service MON](https://docs.ceph.com/en/tentacle/cephadm/services/mon/)
- [Ceph Tentacle — Service OSD](https://docs.ceph.com/en/tentacle/cephadm/services/osd/)
- [Ceph Tentacle — Recommandations matérielles et réseau](https://docs.ceph.com/en/tentacle/start/hardware-recommendations/)
- [Ceph Tentacle — Vérifications de santé](https://docs.ceph.com/en/tentacle/rados/operations/health-checks/)