---
title: "Leçon — NAS, SAN et iSCSI : stockage réseau en mode fichier et en mode bloc"
description: "À l'issue de cette leçon, vous saurez :"
published: true
date: 2026-11-03T09:36:13Z
tags: ["transverse", "tout-en-un", "lecon", "nas", "san", "iscsi", "multipath", "snapshots", "replication", "dimensionnement"]
editor: markdown
dateCreated: 2026-11-03T09:36:13Z
dateModified: 2026-11-03T09:36:13Z
---

# Leçon — NAS, SAN et iSCSI : stockage réseau en mode fichier et en mode bloc

- **Tags** : `transverse`, `tout-en-un`, `lecon`, `nas`, `san`, `iscsi`, `multipath`, `snapshots`, `replication`, `dimensionnement`
- **Niveau** : Intermédiaire (technicien systèmes et réseaux)
- **Durée estimée** : 3 h 30 (lecture 1 h 30, laboratoire 1 h, exercices et quiz 1 h)

---

## Objectifs pédagogiques

À l'issue de cette leçon, vous saurez :

1. distinguer **DAS, [[Glossary:NAS]] et [[Glossary:SAN]]**, et la différence fondamentale entre stockage **en mode fichier** et **en mode bloc** ;
2. choisir le protocole adapté (SMB, [[Glossary:NFS]], iSCSI, Fibre Channel, NVMe over Fabrics) à un besoin donné ;
3. décrire l'architecture iSCSI (initiateur, cible, portail, IQN, [[Glossary:LUN]], CHAP, masquage) et réaliser un montage iSCSI de laboratoire ;
4. expliquer le **multipath** (chemins redondants, bascule, politiques) et savoir le vérifier ;
5. différencier **snapshot** et **réplication**, définir [[Glossary:RPO]] et [[Glossary:RTO]], et placer ces mécanismes dans une stratégie de protection ;
6. dimensionner un stockage (capacité, [[Glossary:IOPS]], débit, latence) et reconnaître les pièges de performance classiques.

## Prérequis et durée

- Notions de réseau [[Glossary:IP]] (adresse, masque, [[Glossary:VLAN]], [[Glossary:MTU]]) et de ligne de commande Linux.
- Avoir lu les leçons voisines : [Stockage local](/fr/00-cours-theoriques/tout-en-un/03-services-d-infrastructure/lecons/lecon-stockage-local) ([[Glossary:RAID]], [[Glossary:LVM]], systèmes de fichiers) et [Partage de fichiers](/fr/00-cours-theoriques/tout-en-un/03-services-d-infrastructure/lecons/lecon-partage-fichiers) (SMB, NFS).
- Une [[Glossary:VM]] Linux **jetable** (Debian/Ubuntu Server récent, 2 Go de [[Glossary:RAM]], 3 Go de disque libre) pour la partie pratique.
- Durée totale : environ 3 h 30.

Convention : adresses de documentation (`192.0.2.0/24` pour les serveurs, `198.51.100.0/24` pour le réseau de stockage, `203.0.113.0/24` pour un site distant), domaine `example.test`. Les identifiants iSCSI (IQN) sont fictifs.

## L'essentiel en bref

- **NAS** (*Network Attached Storage*) : un équipement qui **partage des fichiers** (SMB, NFS). Le NAS gère le système de fichiers ; le client voit un dossier.
- **SAN** (*Storage Area Network*) : un réseau dédié qui **présente des disques bruts** (LUN) à des serveurs en **mode bloc** (iSCSI, Fibre Channel). Le serveur crée et gère lui-même son système de fichiers.
- **iSCSI** transporte les commandes SCSI sur [[Glossary:TCP]]/IP (port 3260) : un SAN accessible avec du matériel Ethernet standard.
- **Multipath** : plusieurs chemins entre serveur et baie, regroupés en un périphérique unique ; il protège d'une panne de carte, de câble, de commutateur ou de contrôleur.
- **Snapshot** = photographie locale d'un état (protège des erreurs) ; **réplication** = copie vers un autre site (protège des sinistres) ; ni l'un ni l'autre n'est une sauvegarde complète.
- Le dimensionnement se fait sur **quatre axes** : capacité, IOPS, débit, latence. Les pièges majeurs : réseau partagé ou mal configuré (MTU), chemin unique, RAID 5 sur charge d'écritures aléatoires, snapshots oubliés, sur-allocation (thin provisioning) non surveillée.

---

## 1. Trois façons d'offrir du stockage

Le disque interne ne suffit plus dès qu'il faut partager, protéger, faire évoluer les données ou héberger des machines virtuelles mobiles : on a sorti le stockage du serveur.

- **DAS** (*Direct Attached Storage*) : le stockage est relié directement à un seul serveur (disques internes, baie SAS reliée en direct). Simple, rapide, mais non partagé.
- **NAS** : un équipement dédié, relié au réseau local, qui **partage des fichiers**. Analogie : un **service d'archives** auquel on demande « apportez-moi le dossier Dupont » ; l'archiviste connaît son rangement.
- **SAN** : un réseau de stockage qui présente des **volumes bruts** (*LUN* — *Logical Unit Number*) comme s'il s'agissait de disques locaux. Analogie : un **entrepôt de casiers vides** que l'on loue ; chaque locataire (serveur) installe son propre rangement.

![Schéma comparatif : à gauche le NAS expose un dossier partagé via SMB/NFS et gère le système de fichiers ; à droite la baie SAN présente des LUN brutes via iSCSI ou Fibre Channel et le serveur crée son propre système de fichiers](images/nas-san-iscsi-1.svg)

*NAS (niveau fichier) contre SAN (niveau bloc) : la frontière de responsabilité n'est pas au même endroit.*

### 1.1 Fichier contre bloc : la distinction essentielle

| Critère | NAS (fichier) | SAN (bloc) |
|---|---|---|
| Ce que voit le client | Un dossier ou un lecteur réseau | Un disque (`/dev/sdb`, disque 2) |
| Qui gère le système de fichiers | Le NAS | Le serveur client |
| Protocoles | SMB, NFS | iSCSI, Fibre Channel, FCoE, NVMe-oF |
| Partage simultané par plusieurs clients | Natif (verrous gérés par le serveur) | **Non** sans système de fichiers de cluster (VMFS, CSV, GFS2, OCFS2) |
| Permissions | Utilisateurs/groupes, [[Glossary:ACL]] | Masquage de LUN (qui voit quel volume), pas de notion de fichier |
| Usage typique | Dossiers utilisateurs, partages de service, sauvegardes | Bases de données, machines virtuelles, clusters |
| Complexité | Faible | Plus élevée |
| Latence | Plus élevée (couche de protocole fichier) | Plus faible |

Une même baie peut proposer **les deux** (stockage « unifié »).

### 1.2 Quand choisir quoi ?

Dossiers partagés d'utilisateurs : NAS. Bases de données à faible latence : SAN en flash. Disques de machines virtuelles : NFS sur NAS ou SAN selon l'hyperviseur. Cluster accédant au même volume : SAN avec système de fichiers de cluster. Sauvegarde : NAS ou stockage objet.

## 2. Les protocoles du stockage réseau

### 2.1 Famille fichier : SMB et NFS

SMB (TCP 445) et NFS (TCP 2049), vus dans la leçon sur le partage de fichiers. Le NAS applique les droits au niveau fichier ; les petits fichiers souffrent de la latence réseau, chaque opération faisant un aller-retour.

### 2.2 Famille bloc : SCSI et ses transports

Le **SCSI** est le langage historique des commandes de disque (« lis N blocs à l'adresse X ») ; le réseau ne fait que les **transporter** :

- **SAS** : liaison directe point à point (DAS), non routable ;
- **Fibre Channel (FC)** : réseau dédié à haute fiabilité (fibre optique, commutateurs FC, cartes [[Glossary:HBA]]), très utilisé dans les grandes entreprises, avec des débits de 16, 32 ou 64 Gbit/s ; l'isolement des accès se fait par **zoning** ;
- **FCoE** : Fibre Channel encapsulé dans Ethernet, en net recul ;
- **iSCSI** : SCSI sur TCP/IP, normalisé par la **RFC 7143** ; il s'appuie sur l'Ethernet banalisé (10, 25, 100 GbE), d'où un coût moindre ;
- **NVMe over Fabrics (NVMe-oF)** : prolonge le protocole NVMe (flash) sur le réseau (RDMA, Fibre Channel ou TCP) pour des latences très basses ; technologie récente, à envisager pour les charges les plus exigeantes.

| Transport | Réseau | Coût | Latence | Complexité | Usage typique |
|---|---|---|---|---|---|
| iSCSI | Ethernet/IP | Faible à moyen | Bonne | Moyenne | PME, virtualisation, labos |
| Fibre Channel | Réseau FC dédié | Élevé | Très bonne | Élevée | Grands centres de données |
| NVMe-oF | RDMA/FC/TCP | Moyen à élevé | Excellente | Élevée | Charges critiques, flash |

### 2.3 Le vocabulaire iSCSI

- **Initiateur** : le client qui utilise le disque ; **cible** : le serveur de stockage qui expose les volumes ; **LUN** : volume numéroté exposé par une cible.
- **Portail** : adresse IP + port TCP (3260). **IQN** (*iSCSI Qualified Name*) : nom unique de la forme `iqn.AAAA-MM.domaine-inversé:identifiant`, par exemple `iqn.2026-11.test.example:srv1`.
- **Découverte** (`SendTargets`) : l'initiateur demande à un portail la liste des cibles ; **session** : connexion TCP authentifiée.
- **CHAP** : authentification par défi/réponse à secret partagé. **Masquage de LUN** (ACL) : la cible n'expose une LUN qu'aux IQN listés, barrière d'accès essentielle.

![Schéma d'une session iSCSI : un initiateur identifié par un IQN se connecte via un réseau IP dédié au portail d'une cible qui présente deux LUN](images/nas-san-iscsi-2.svg)

*Session iSCSI : l'initiateur (serveur) ouvre une session TCP vers le portail 3260 de la cible, qui lui présente des LUN apparaissant comme des disques locaux.*

### 2.4 Sécurité d'un SAN iSCSI

iSCSI n'est **pas chiffré** par défaut. Règles : **réseau dédié** (VLAN ou commutateurs séparés) non routé vers les postes ; **masquage de LUN** par IQN et CHAP (voire CHAP mutuel) ; aucune cible sur un réseau non maîtrisé ; IPsec ou [[Glossary:VPN]] pour traverser un réseau non fiable (au prix de la performance).

Côté Fibre Channel, l'équivalent est le **zoning** sur les commutateurs et le masquage de LUN sur la baie.

## 3. Une cible et un initiateur iSCSI sous Linux

Le noyau Linux fournit une cible iSCSI (**LIO**, pilotée par `targetcli`) et l'initiateur est fourni par le paquet **open-iscsi** (`iscsiadm`). Ce schéma est parfait pour un laboratoire ; en production, la cible est souvent une baie dédiée.

### 3.1 Côté cible

Installation et préparation d'un volume de 512 Mio dans un simple fichier :

```bash
sudo apt update && sudo apt install -y targetcli-fb
sudo mkdir -p /srv/iscsi
sudo truncate -s 512M /srv/iscsi/lun0.img
```

👉 Explication : installe l'outil d'administration de la cible LIO (`targetcli-fb`), crée un dossier de travail et un fichier creux de 512 Mio qui servira de disque virtuel.

Création du *backstore*, de la cible et de la LUN :

```bash
sudo targetcli /backstores/fileio create name=lun0 file_or_dev=/srv/iscsi/lun0.img
sudo targetcli /iscsi create iqn.2026-11.test.example:labo.cible1
sudo targetcli /iscsi/iqn.2026-11.test.example:labo.cible1/tpg1/luns create /backstores/fileio/lun0
```

👉 Explication : déclare le fichier comme stockage (*backstore*), crée une cible iSCSI avec son IQN et rattache la LUN 0 à cette cible ; par défaut, la cible écoute sur le port 3260 de toutes les adresses.

Autoriser l'initiateur (masquage de LUN) :

```bash
sudo targetcli /iscsi/iqn.2026-11.test.example:labo.cible1/tpg1/acls create iqn.2026-11.test.example:client1
sudo targetcli saveconfig
```

👉 Explication : n'autorise que l'initiateur d'IQN `iqn.2026-11.test.example:client1` à voir la LUN ; `saveconfig` enregistre la configuration pour qu'elle survive au redémarrage.

Contrôler l'état :

```bash
sudo targetcli ls
ss -tlnp | grep 3260
```

👉 Explication : affiche l'arborescence de la cible (backstores, cibles, LUN, ACL) et vérifie que le port 3260 est bien à l'écoute ; commandes en lecture seule.

### 3.2 Côté initiateur

```bash
sudo apt install -y open-iscsi
echo 'InitiatorName=iqn.2026-11.test.example:client1' | sudo tee /etc/iscsi/initiatorname.iscsi
sudo systemctl restart iscsid
```

👉 Explication : installe l'initiateur, définit son nom IQN (qui doit correspondre à l'ACL de la cible) et relance le service ; sur une machine déjà utilisée, sauvegardez d'abord le fichier existant.

Découverte, connexion, vérification :

```bash
sudo iscsiadm -m discovery -t sendtargets -p 192.0.2.30
sudo iscsiadm -m node -T iqn.2026-11.test.example:labo.cible1 -p 192.0.2.30 --login
sudo iscsiadm -m session -P 1
lsblk
```

👉 Explication : interroge le portail `192.0.2.30:3260` pour lister les cibles, ouvre la session avec la cible choisie puis affiche l'état de la session ; un nouveau disque (par exemple `/dev/sdb`) apparaît dans `lsblk`. En laboratoire sur une seule VM, utilisez `127.0.0.1` à la place de l'adresse du portail.

Le disque présenté est **brut** : il faut le partitionner (ou pas), le formater et le monter, comme n'importe quel disque local.

```bash
sudo mkfs.ext4 -L SAN_LABO /dev/sdb
sudo mkdir -p /mnt/san && sudo mount /dev/sdb /mnt/san
```

👉 Explication : crée un système de fichiers sur la LUN présentée (remplacez `/dev/sdb` par le nom réellement affiché dans `lsblk`) et monte-la ; **vérifiez le nom du disque deux fois** pour ne pas formater un disque local.

Rendre la connexion automatique au démarrage :

```bash
sudo iscsiadm -m node -T iqn.2026-11.test.example:labo.cible1 -p 192.0.2.30 --op update -n node.startup -v automatic
```

👉 Explication : indique que la session doit être rétablie automatiquement au démarrage ; pour le montage, utilisez `_netdev` et un identifiant stable (UUID, ou chemin `/dev/disk/by-path/`) dans `fstab`, car l'ordre des disques `/dev/sdX` n'est pas garanti.

### 3.3 Côté Windows

Windows Server inclut un initiateur iSCSI (service `MSiSCSI`) :

```powershell
Set-Service -Name MSiSCSI -StartupType Automatic
Start-Service MSiSCSI
New-IscsiTargetPortal -TargetPortalAddress 192.0.2.30
Get-IscsiTarget
```

👉 Explication : active le service iSCSI, déclare le portail de la cible et liste les cibles découvertes ; ces commandes configurent l'initiateur de la machine, à exécuter sur une VM de test.

```powershell
Connect-IscsiTarget -NodeAddress "iqn.2026-11.test.example:labo.cible1" -IsPersistent $true
Get-Disk | Where-Object BusType -eq 'iSCSI'
```

👉 Explication : ouvre la session de façon persistante (reconnexion au redémarrage) puis liste les disques arrivés par iSCSI ; ils doivent ensuite être initialisés ([[Glossary:GPT]]), partitionnés et formatés comme tout disque.

### 3.4 Le danger du volume partagé

Présenter la même LUN à **deux** serveurs avec ext4 ou [[Glossary:NTFS]] est le moyen le plus sûr de **détruire** les données : chacun corrompt les métadonnées de l'autre. Il faut un **système de fichiers de cluster** (VMFS, CSV, GFS2, OCFS2) ; d'où le masquage de LUN.

## 4. Multipath : plusieurs chemins, un seul disque

Un SAN est souvent le cœur de l'infrastructure : un câble débranché, une carte réseau morte ou un commutateur en panne ne doit pas l'interrompre. On construit donc **plusieurs chemins** entre le serveur et la baie.

![Schéma multipath : un serveur à deux cartes réseau reliées à deux commutateurs, eux-mêmes reliés à deux contrôleurs de la baie ; le périphérique unique /dev/mapper/mpatha regroupe les deux chemins](images/nas-san-iscsi-3.svg)

*Multipath : deux chemins complets et indépendants, regroupés par le système en un périphérique unique.*

Sans multipath, le système verrait **deux disques** différents (`/dev/sdb` et `/dev/sdc`) qui sont en réalité la même LUN : chacun serait vu comme un disque indépendant, avec un risque de corruption si on les utilise tous deux. Le **service multipath** (`dm-multipath` sous Linux, MPIO sous Windows) :

1. reconnaît, grâce à l'identifiant unique (WWID) de la LUN, que plusieurs chemins mènent au même volume ;
2. les regroupe en un périphérique unique (`/dev/mapper/mpatha` ou un alias) ;
3. répartit la charge ou bascule en cas de panne selon une **politique**.

### 4.1 Politiques de chemins

- **Failover** (actif/passif) : un seul chemin actif, l'autre prend le relais.
- **Round-robin** : E/S réparties entre les chemins actifs.
- **Queue-length / service-time** : vers le chemin le moins chargé ou le plus rapide.
- **ALUA** : la baie signale les chemins « optimisés » (contrôleur propriétaire de la LUN) à privilégier.

### 4.2 Mettre en œuvre sous Linux

```bash
sudo apt install -y multipath-tools
sudo systemctl enable --now multipathd
```

👉 Explication : installe et démarre le service multipath (`multipathd`).

Un fichier minimal `/etc/multipath.conf` (à adapter au modèle de baie ; consultez la documentation du constructeur) :

```ini
defaults {
    user_friendly_names yes
    find_multipaths yes
}
```

👉 Explication : active des noms lisibles (`mpatha`…) et n'applique multipath qu'aux disques ayant plusieurs chemins ; le disque système local est ainsi laissé de côté.

```bash
sudo multipath -ll
```

👉 Explication : affiche chaque périphérique multipath, son WWID, la politique et l'état de chaque chemin (`active ready running` = sain, `failed faulty` = chemin en panne) ; commande en lecture seule, première chose à regarder en cas de doute.

Pour **iSCSI** en multipath, on ouvre une session **par chemin** (par portail ou par interface réseau) vers la même cible :

```bash
sudo iscsiadm -m discovery -t sendtargets -p 192.0.2.30
sudo iscsiadm -m discovery -t sendtargets -p 198.51.100.30
sudo iscsiadm -m node --login
sudo iscsiadm -m session
```

👉 Explication : découvre la cible par deux portails (deux réseaux distincts), ouvre toutes les sessions connues puis liste les sessions ; deux sessions vers la même cible produisent deux disques `sd*` fusionnés par multipath en un seul périphérique.

Sous Windows Server : `Install-WindowsFeature Multipath-IO` puis activation de la prise en charge iSCSI par MPIO (`Enable-MSDSMAutomaticClaim -BusType iSCSI`, ou le panneau « MPIO ») et redémarrage.

### 4.3 Tester sa résilience

En **préproduction**, débranchez un chemin pendant une copie de gros fichier : la copie doit continuer, `multipath -ll` doit montrer le chemin `failed` puis de nouveau `active`, et la supervision doit alerter.

## 5. Snapshots et réplication

### 5.1 Snapshot

Un **snapshot** (instantané) fige l'état d'un volume à un instant donné. Il n'occupe presque rien au départ ; l'espace consommé croît avec les modifications. Deux techniques principales :

- **copie sur écriture** (*copy-on-write*) : avant d'écraser un bloc, on copie l'ancien dans une zone réservée ; les écritures sont plus lourdes tant que le snapshot existe ;
- **redirection sur écriture** (*redirect-on-write*, [[Glossary:ZFS]], nombreuses baies) : les nouvelles données sont écrites ailleurs et le snapshot continue de pointer sur les anciens blocs ; l'impact sur les performances est faible.

Un snapshot est **cohérent après plantage** (*crash-consistent*). Pour une base de données, on veut un état **cohérent applicativement** : l'application vide ses tampons ([[Glossary:VSS]] sous Windows, scripts de pré-gel sous Linux) juste avant.

Utilité : retour arrière rapide, source figée pour une sauvegarde. Limites : même équipement (**pas une sauvegarde**), espace consommé, chaîne qui ralentit en vieillissant.

### 5.2 Réplication

La **réplication** copie les données (ou les changements) vers un autre équipement, souvent sur un autre site.

- **Synchrone** : une écriture n'est acquittée au serveur qu'après l'écriture sur les **deux** baies. **RPO = 0** (aucune perte), mais la latence de la liaison s'ajoute à chaque écriture : distance limitée (quelques dizaines de kilomètres).
- **Asynchrone** : l'écriture est acquittée dès qu'elle est sur la baie locale, puis envoyée au site distant. Aucun impact de latence, mais **RPO > 0** (on peut perdre les derniers instants).
- **Semi-synchrone / périodique** : réplication de snapshots à intervalles réguliers (par exemple toutes les 15 minutes).

![Schéma : un volume de production avec trois snapshots à 08:00, 12:00 et 18:00 réplique de façon asynchrone vers un site de secours qui contient les copies correspondantes](images/nas-san-iscsi-4.svg)

*Snapshots locaux (protection contre l'erreur) et réplication distante asynchrone (protection contre le sinistre).*

Deux mesures guident le choix :

- **RPO** (*Recovery Point Objective*) : la quantité de données que l'on accepte de perdre, exprimée en temps (RPO = 4 h : on tolère de perdre jusqu'à 4 h de travail) ;
- **RTO** (*Recovery Time Objective*) : le délai maximal de reprise acceptable (RTO = 2 h : le service doit être de retour en 2 heures).

Plus ces objectifs sont stricts, plus la solution coûte cher : on dimensionne d'après la criticité métier.

### 5.3 Snapshot, réplication, sauvegarde : trois protections différentes

| Mécanisme | Protège contre | Ne protège pas contre |
|---|---|---|
| RAID | Panne de disque | Suppression, corruption logique, sinistre |
| Snapshot | Erreur humaine récente, mise à jour ratée | Panne de la baie, sinistre, corruption propagée avant détection |
| Réplication | Panne de site, sinistre | Suppression ou chiffrement malveillant (répliqués aussi !) |
| Sauvegarde (hors ligne / immuable) | Presque tout, y compris rançongiciel | Rien si elle n'est jamais testée |

Conclusion à mémoriser : la réplication **copie aussi les erreurs et les attaques**. Une stratégie sérieuse combine RAID, snapshots, réplication **et** sauvegarde isolée (règle 3-2-1, copie immuable ou hors ligne), avec **test de restauration** régulier.

### 5.4 Allocation fine, déduplication, compression

L'**allocation fine** (*thin provisioning*) promet plus d'espace que le physique ; **surveillez le remplissage du pool** : un pool plein bloque tous les volumes. La **déduplication** et la **compression** économisent de l'espace (gain variable, coût en calcul).

## 6. Dimensionner un stockage

### 6.1 Quatre grandeurs à ne pas confondre

1. **Capacité** : combien de To utiles aujourd'hui, et dans 3 à 5 ans (croissance). Compter les snapshots et réplicas, un volume libre de 20 à 30 %.
2. **IOPS** (opérations d'entrée/sortie par seconde) : indicateur clé pour les petits accès aléatoires (bases de données, machines virtuelles).
3. **Débit** (Mo/s) : volume de données par seconde, pertinent pour les gros transferts séquentiels (sauvegardes, vidéo).
4. **Latence** (ms) : temps de réponse d'une opération ; c'est ce que ressent l'application.

Ordres de grandeur indicatifs (à valider par mesure) : plateaux 7 200 tr/min ≈ 80 à 100 IOPS aléatoires ; 15 000 tr/min ≈ 180 à 200 ; [[Glossary:SSD]] [[Glossary:SATA]] ≈ dizaines de milliers ; NVMe ≈ centaines de milliers.

Lien entre IOPS et débit : **débit ≈ IOPS × taille d'une opération**. Exemple : 5 000 IOPS en blocs de 8 Kio = 40 000 Kio/s, soit environ 40 Mo/s ; la même charge en blocs de 64 Kio demanderait ~320 Mo/s.

### 6.2 Effet du RAID sur les écritures

Chaque niveau RAID multiplie le nombre d'accès disque par écriture logique (« pénalité d'écriture ») : RAID 0 ≈ 1, RAID 1 et RAID 10 ≈ 2, RAID 5 ≈ 4, RAID 6 ≈ 6.

Exemple : 2 000 IOPS dont 70 % de lectures. En RAID 10, la charge disque est 1 400 + 600 × 2 = 2 600 IOPS ; en RAID 5, 1 400 + 600 × 4 = 3 800. Avec des disques de 150 IOPS, il en faut environ 18 contre 26. Le flash et les caches de contrôleur atténuent beaucoup cet écart.

### 6.3 Dimensionner le réseau de stockage

- **Débit** : 10 GbE ≈ 1,1 Go/s utile au mieux, 25 GbE ≈ 2,8 Go/s ; plusieurs serveurs se partagent les liens vers la baie.
- **Redondance** : deux liens par serveur, deux commutateurs, deux contrôleurs ; trafic de stockage isolé.
- **Trames jumbo** (MTU 9000) : utiles **seulement si** configurées de bout en bout ; une extrémité en 1500 provoque pertes et blocages.

### 6.4 Méthode

Recenser les charges, **mesurer** l'existant sur plusieurs jours (pics compris : `iostat -x`, compteurs Windows, outils de la baie), fixer capacité, IOPS, débit, latence avec 30 à 50 % de marge, choisir média et RAID, puis **valider par un test de charge** avant production.

Mesure de référence (sur une machine de test, avec un fichier de test **jetable** dans un dossier dédié) :

```bash
fio --name=test-aleatoire --filename=/mnt/san/fio.test --size=256M --rw=randrw --rwmixread=70 --bs=8k --iodepth=16 --runtime=30 --time_based --direct=1
```

👉 Explication : génère une charge aléatoire 70 % lecture / 30 % écriture en blocs de 8 Kio pendant 30 s sur un fichier de test et affiche IOPS, débit et latences ; ne jamais lancer un test d'écriture sur un volume de production sans accord et fenêtre de maintenance, car il peut dégrader le service.

## 7. Pièges de performance et d'exploitation

1. **Réseau partagé** avec le trafic utilisateur ou les sauvegardes. → VLAN dédié, QoS.
2. **MTU incohérent** : jumbo frames d'un seul côté. → `ping -M do -s 8972 198.51.100.30` (8972 + 28 = 9000).
3. **Chemin unique** malgré le multipath. → `multipath -ll`, supervision du nombre de chemins.
4. **Politique de chemins inadaptée** (round-robin sur chemin non optimisé ALUA). → suivre le constructeur.
5. **Pénalité d'écriture RAID** non anticipée (RAID 5/6 en écritures aléatoires).
6. **Pool à allocation fine plein** : toutes les LUN en erreur. → alertes à 70 % et 85 %.
7. **Snapshots oubliés** : espace et performances dégradés. → rétention et suppression automatique.
8. **Désalignement de partitions**. → partitions démarrant à 1 Mio.
9. **Petits fichiers sur NAS**, antivirus ou indexation, chiffrement sans accélération matérielle.
10. **[[Glossary:DNS]]/NTP** défaillants (portail lent, Kerberos). → IP fixes pour les portails, heure synchronisée.
11. **Aucun test de restauration** ni de plan de reprise joué.

Supervisez ensemble **latence**, **occupation** (pool, volumes, snapshots), **santé des chemins** et **erreurs réseau** : une latence qui monte est souvent le premier signe d'un problème.

---

## Mise en pratique guidée

**Cadre** : une VM Linux jetable, utilisée à la fois comme cible et initiateur via `127.0.0.1`. Instantané avant de commencer. Aucune autre machine n'est contactée. Si votre distribution ne propose pas `targetcli-fb`, utilisez le paquet équivalent (`targetcli`).

**Étape 1 — créer la LUN virtuelle et la cible.**

```bash
sudo apt update && sudo apt install -y targetcli-fb open-iscsi
sudo mkdir -p /srv/iscsi && sudo truncate -s 512M /srv/iscsi/lun0.img
sudo targetcli /backstores/fileio create name=lun0 file_or_dev=/srv/iscsi/lun0.img
sudo targetcli /iscsi create iqn.2026-11.test.example:labo.cible1
sudo targetcli /iscsi/iqn.2026-11.test.example:labo.cible1/tpg1/luns create /backstores/fileio/lun0
```

👉 Explication : installe les outils, crée le fichier de 512 Mio, le déclare comme stockage et crée la cible avec sa LUN 0.

**Étape 2 — masquer la LUN (ACL).**

```bash
echo 'InitiatorName=iqn.2026-11.test.example:client1' | sudo tee /etc/iscsi/initiatorname.iscsi
sudo systemctl restart iscsid
sudo targetcli /iscsi/iqn.2026-11.test.example:labo.cible1/tpg1/acls create iqn.2026-11.test.example:client1
sudo targetcli saveconfig
```

👉 Explication : donne un IQN à l'initiateur local, autorise uniquement cet IQN sur la cible, puis sauvegarde la configuration.

**Étape 3 — découverte et connexion.**

```bash
sudo iscsiadm -m discovery -t sendtargets -p 127.0.0.1
sudo iscsiadm -m node -T iqn.2026-11.test.example:labo.cible1 -p 127.0.0.1 --login
lsblk -o NAME,SIZE,TYPE,TRAN,MODEL
sudo iscsiadm -m session -P 3 | head -40
```

👉 Explication : découvre la cible, ouvre la session puis affiche un nouveau disque d'environ 512 Mio (colonne `TRAN` = `iscsi`) et le détail de la session. Notez son nom (par exemple `sdb`).

**Étape 4 — formater et utiliser.**

```bash
sudo mkfs.ext4 -L SAN_LABO /dev/sdb
sudo mkdir -p /mnt/san && sudo mount /dev/sdb /mnt/san
echo "essai iscsi" | sudo tee /mnt/san/essai.txt
df -h /mnt/san
```

👉 Explication : crée un système de fichiers sur la LUN (remplacez `/dev/sdb` par le vrai nom relevé à l'étape 3), le monte et vérifie qu'on peut écrire.

**Étape 5 — mesurer.**

```bash
sudo apt install -y fio
sudo fio --name=essai --filename=/mnt/san/fio.test --size=128M --rw=randrw --rwmixread=70 --bs=8k --iodepth=8 --runtime=20 --time_based --direct=1
```

👉 Explication : lance une petite charge de test sur le volume de laboratoire et relevez IOPS et latence moyenne ; comparez en refaisant avec `--bs=64k` et `--rw=read` pour observer l'effet de la taille de bloc et du mode séquentiel.

**Étape 6 — constater le masquage de LUN.** Après déconnexion, mettez `InitiatorName=iqn.2026-11.test.example:intrus` dans `/etc/iscsi/initiatorname.iscsi`, redémarrez `iscsid` et reconnectez-vous :

```bash
sudo umount /mnt/san
sudo iscsiadm -m node -T iqn.2026-11.test.example:labo.cible1 -p 127.0.0.1 --logout
sudo iscsiadm -m node -T iqn.2026-11.test.example:labo.cible1 -p 127.0.0.1 --login
```

👉 Explication : avec l'IQN « intrus » non autorisé, la connexion doit échouer (échec d'autorisation) : preuve du masquage de LUN. Remettez ensuite l'IQN `client1`.

**Étape 7 — nettoyage.**

```bash
sudo umount /mnt/san 2>/dev/null
sudo iscsiadm -m node -T iqn.2026-11.test.example:labo.cible1 -p 127.0.0.1 --logout
sudo iscsiadm -m node -T iqn.2026-11.test.example:labo.cible1 -p 127.0.0.1 --op delete
sudo targetcli /iscsi delete iqn.2026-11.test.example:labo.cible1
sudo targetcli /backstores/fileio delete lun0
sudo targetcli saveconfig
sudo rm -f /srv/iscsi/lun0.img
```

👉 Explication : ferme la session, supprime l'entrée de découverte, supprime la cible puis le backstore, sauvegarde et efface le fichier de la LUN ; ou restaurez l'instantané de la VM.

**Critères de réussite** : disque iSCSI visible puis formaté, écriture réussie, mesure fio relevée, connexion refusée avec un IQN non autorisé, nettoyage complet.

## Exercices

1. **(Vocabulaire)** Définissez en une phrase chacun des termes : LUN, IQN, initiateur, portail.
2. **(Classification)** Pour chaque cas, indiquez « NAS » ou « SAN » et justifiez : (a) dossiers personnels de 200 utilisateurs, (b) volume de base de données [[Glossary:SQL]] en cluster, (c) répertoire partagé d'images pour une équipe graphique sur postes macOS et Windows, (d) disque d'un hyperviseur utilisant VMFS.
3. **(Protocoles)** Pourquoi iSCSI est-il souvent choisi par les PME face au Fibre Channel ? Donnez deux avantages et deux précautions de sécurité.
4. **(Danger)** Un technicien présente la même LUN (ext4) à deux serveurs « pour partager les données ». Expliquez le risque et proposez deux solutions correctes.
5. **(Multipath)** Un serveur voit `/dev/sdb` et `/dev/sdc` de même taille et `multipath -ll` n'affiche rien. Que supposez-vous ? Quelles vérifications ?
6. **(RPO/RTO)** Un site e-commerce accepte au plus 15 minutes de commandes perdues et 1 heure d'indisponibilité. Quel type de réplication choisir ? Que valent RPO et RTO ?
7. **(Dimensionnement)** Une application génère 4 000 IOPS dont 60 % de lectures. Calculez la charge côté disques en RAID 10 puis en RAID 5 (pénalités 2 et 4), puis le nombre de disques à 150 IOPS nécessaires dans chaque cas.
8. **(Diagnostic)** Après passage au MTU 9000 sur le serveur, le montage iSCSI se connecte mais les transferts se bloquent. Proposez une démarche de diagnostic en 4 étapes.

## Corrigés des exercices

1. **LUN** : volume (identifié par un numéro) exposé par une cible. **IQN** : nom unique d'un initiateur ou d'une cible iSCSI. **Initiateur** : le client iSCSI qui utilise le disque. **Portail** : adresse IP et port (3260) où la cible écoute.
2. (a) **NAS** : partage de fichiers par utilisateur, droits par dossier. (b) **SAN** (mode bloc), faible latence ; le cluster impose un système de fichiers partagé ou des volumes dédiés. (c) **NAS** : accès par des clients hétérogènes, SMB (voire NFS), la gestion des verrous est côté serveur. (d) **SAN** (iSCSI ou FC) : VMFS est un système de fichiers de cluster qui exige des LUN en mode bloc ; NFS reste une alternative sur NAS selon l'hyperviseur.
3. Avantages : utilise l'Ethernet existant (coût réduit), compétences réseau courantes, routable si nécessaire. Précautions : réseau dédié/VLAN séparé et masquage de LUN avec CHAP (ou IPsec sur réseau non maîtrisé), pas d'exposition sur Internet.
4. Chaque serveur écrit ses propres métadonnées ext4 sans connaître l'autre : **corruption quasi certaine**. Solutions : (1) système de fichiers de cluster (GFS2, OCFS2, VMFS, CSV) avec gestionnaire de verrous ; (2) un NAS (SMB/NFS) où le serveur de fichiers arbitre ; (3) une LUN par serveur.
5. Le multipath n'est pas actif (service arrêté, paquet absent, `blacklist`, LUN non reconnue). Vérifier `systemctl status multipathd`, `multipath -v3`, le WWID (`/lib/udev/scsi_id -g -u -d /dev/sdb`, identique pour les deux disques) et `/etc/multipath.conf`. **Ne pas utiliser** les deux disques en parallèle.
6. Perte tolérée 15 min : réplication **asynchrone** ou périodique toutes les 5 à 10 minutes suffit. **RPO = 15 min**, **RTO = 1 h**. Une réplication synchrone ne se justifie que si RPO = 0 est exigé (coût et latence).
7. Lectures : 2 400 ; écritures : 1 600. RAID 10 : 2 400 + 1 600 × 2 = 5 600 IOPS → 5 600 / 150 ≈ 37,3 → **38 disques** (arrondi supérieur, pairs : 38). RAID 5 : 2 400 + 1 600 × 4 = 8 800 IOPS → 8 800 / 150 ≈ 58,7 → **59 disques**. Le flash ou un cache permet de réduire fortement ces chiffres.
8. (1) Vérifier le MTU à chaque saut (carte, commutateurs, baie). (2) `ping -M do -s 8972 <portail>` : un échec révèle un équipement en 1500. (3) Corriger ou revenir à 1500 partout. (4) Relancer la session, mesurer, consulter `ip -s link` et `ethtool -S`.

## Quiz

**Q1. Quelle est la différence principale entre un NAS et un SAN ?**
a) Le NAS est toujours plus rapide  b) Le NAS partage des fichiers, le SAN présente des volumes en mode bloc  c) Le SAN n'utilise que du Wi-Fi  d) Aucune différence
**Réponse : b.** Le NAS gère le système de fichiers et expose des fichiers ; le SAN expose des blocs, le serveur gère son système de fichiers.

**Q2. Sur quel port TCP écoute normalement une cible iSCSI ?**
a) 445  b) 2049  c) 3260  d) 443
**Réponse : c.** 3260 est le port iSCSI par défaut ; 445 = SMB, 2049 = NFS.

**Q3. Que désigne un IQN ?**
a) Une adresse MAC  b) Le nom unique d'un initiateur ou d'une cible iSCSI  c) Un type de câble  d) Une version de SMB
**Réponse : b.** Format `iqn.AAAA-MM.domaine-inversé:identifiant`.

**Q4. À quoi sert le masquage de LUN ?**
a) Chiffrer les données  b) Limiter les initiateurs autorisés à voir une LUN  c) Compresser les volumes  d) Répliquer vers un autre site
**Réponse : b.** Seuls les IQN autorisés ont accès à la LUN.

**Q5. Que se passe-t-il si deux serveurs montent la même LUN en ext4 en écriture ?**
a) Les performances doublent  b) Les données sont partagées proprement  c) Risque élevé de corruption  d) Un NAS est créé automatiquement
**Réponse : c.** ext4 n'est pas un système de fichiers de cluster ; les métadonnées se corrompent mutuellement.

**Q6. Quel est l'intérêt principal du multipath ?**
a) Chiffrer le trafic  b) Disposer de plusieurs chemins redondants vers la même LUN, avec bascule en cas de panne  c) Augmenter la capacité des disques  d) Remplacer la sauvegarde
**Réponse : b.** Il offre redondance et parfois répartition de charge.

**Q7. Quelle réplication garantit un RPO de zéro ?**
a) Asynchrone  b) Périodique toutes les heures  c) Synchrone  d) Snapshot local
**Réponse : c.** L'écriture n'est acquittée qu'après avoir été écrite sur les deux sites ; la latence de la liaison est le prix à payer.

**Q8. Un snapshot sur la même baie protège-t-il d'une panne totale de cette baie ?**
a) Oui  b) Non, il réside sur le même équipement  c) Oui si la baie est en RAID 6  d) Oui si on utilise CHAP
**Réponse : b.** Un snapshot n'est pas une sauvegarde externe.

**Q9. Quelle est la pénalité d'écriture classique du RAID 5 ?**
a) 1  b) 2  c) 4  d) 8
**Réponse : c.** Une écriture logique entraîne environ quatre accès disque (lire donnée et parité, écrire donnée et parité).

**Q10. Quel est le risque principal de l'allocation fine (thin provisioning) non surveillée ?**
a) Les snapshots sont interdits  b) Le pool physique peut se remplir et bloquer tous les volumes qui en dépendent  c) Le réseau devient plus lent  d) L'authentification échoue
**Réponse : b.** On promet plus d'espace que ce qui existe physiquement ; sans alertes, un pool plein provoque des erreurs d'écriture.

## Erreurs fréquentes et dépannage

| Symptôme | Cause probable | Vérification / action |
|---|---|---|
| `iscsiadm: initiator reported error (24 - iSCSI login failed due to authorization failure)` | IQN non autorisé ou CHAP incorrect | Comparer `/etc/iscsi/initiatorname.iscsi` à l'ACL de la cible |
| La découverte ne renvoie rien | Pare-feu 3260, portail incorrect, cible arrêtée | `ss -tlnp \| grep 3260`, `nc -zv <portail> 3260` |
| Le disque iSCSI change de nom à chaque redémarrage | Utilisation de `/dev/sdX` | Utiliser `/dev/disk/by-id/`, UUID ou alias multipath |
| Le montage au démarrage échoue | Le réseau n'est pas prêt, pas de `_netdev` | `_netdev`, `node.startup = automatic`, `nofail` |
| Deux disques identiques apparaissent | Multipath non actif | `systemctl status multipathd`, `multipath -ll` |
| Performances faibles par intermittence | Réseau partagé, MTU incohérent, snapshots empilés | Mesurer la latence, `ip -s link`, lister les snapshots |
| Volumes en erreur d'écriture | Pool à allocation fine plein | Libérer de l'espace, étendre le pool, alertes à 70/85 % |
| Données corrompues sur une LUN partagée | Même LUN en ext4/NTFS sur deux hôtes | Restaurer, appliquer masquage et système de cluster |
| Réplication « en retard » | Liaison saturée ou latence | Mesurer le délai de réplication (RPO réel), augmenter la bande passante |

Réflexes : **documenter** (IQN, portails, WWID, chemins), **tester** une panne de chemin et une restauration chaque année, **superviser** latence, remplissage, chemins et erreurs réseau.

## À retenir

- **NAS = fichiers** (SMB/NFS, le NAS gère le système de fichiers) ; **SAN = blocs** (iSCSI/FC/NVMe-oF, le serveur gère son système de fichiers).
- iSCSI : initiateur, cible, portail (3260), IQN, LUN, CHAP, **masquage de LUN** ; réseau dédié obligatoire en pratique.
- Une LUN ne se partage entre plusieurs serveurs qu'avec un **système de fichiers de cluster**.
- Multipath = plusieurs chemins indépendants, un périphérique unique ; **tester** la bascule et surveiller `multipath -ll`.
- Snapshot = erreur humaine ; réplication = sinistre ; sauvegarde isolée et testée = tout le reste. La réplication copie aussi les erreurs.
- **RPO** (perte acceptable) et **RTO** (reprise acceptable) pilotent le choix technique.
- Dimensionner sur quatre axes : capacité, IOPS, débit, latence ; tenir compte de la pénalité d'écriture RAID.
- Pièges : MTU incohérent, chemin unique, thin provisioning non surveillé, snapshots oubliés, réseau partagé.

## Pour aller plus loin

Documentations officielles et RFC :

- RFC 7143 — Internet Small Computer System Interface (iSCSI) Protocol : <https://www.rfc-editor.org/rfc/rfc7143>
- RFC 3720 (version originale d'iSCSI, remplacée par la RFC 7143) : <https://www.rfc-editor.org/rfc/rfc3720>
- RFC 8881 — NFS Version 4.1 : <https://www.rfc-editor.org/rfc/rfc8881>
- Projet open-iscsi (initiateur Linux) : <https://github.com/open-iscsi/open-iscsi>
- Documentation du noyau Linux — cible SCSI (LIO) : <https://docs.kernel.org/target/index.html>
- Documentation du noyau Linux — Device Mapper Multipath : <https://docs.kernel.org/admin-guide/device-mapper/index.html>
- Page de manuel `multipath.conf` : <https://man7.org/linux/man-pages/man5/multipath.conf.5.html>
- Documentation Microsoft — Initiateur iSCSI et applet de commande `Connect-IscsiTarget` : <https://learn.microsoft.com/fr-fr/powershell/module/iscsi/connect-iscsitarget>
- Documentation Microsoft — Multipath I/O (MPIO) : <https://learn.microsoft.com/fr-fr/windows-server/storage/mpio/mpio-overview>
- Documentation `fio` (tests de performance) : <https://fio.readthedocs.io/>

## Crédits des images

| Fichier | Source (URL de la page) | Auteur | Licence | Modifications |
|---|---|---|---|---|
| `images/nas-san-iscsi-1.svg` | Fichier original de ce dépôt | Pack Master | Création originale du projet Pack Master, dédiée au domaine public (CC0) — <https://creativecommons.org/publicdomain/zero/1.0/> | Sans objet |
| `images/nas-san-iscsi-2.svg` | Fichier original de ce dépôt | Pack Master | Création originale du projet Pack Master, dédiée au domaine public (CC0) — <https://creativecommons.org/publicdomain/zero/1.0/> | Sans objet |
| `images/nas-san-iscsi-3.svg` | Fichier original de ce dépôt | Pack Master | Création originale du projet Pack Master, dédiée au domaine public (CC0) — <https://creativecommons.org/publicdomain/zero/1.0/> | Sans objet |
| `images/nas-san-iscsi-4.svg` | Fichier original de ce dépôt | Pack Master | Création originale du projet Pack Master, dédiée au domaine public (CC0) — <https://creativecommons.org/publicdomain/zero/1.0/> | Sans objet |

Aucune image tierce n'est utilisée dans cette leçon.

## Historique de vérification

| Date | OS/logiciel | Testeur | Verdict |
|---|---|---|---|
| 2026-11-01 | Linux (Debian/Ubuntu) — LIO/targetcli, open-iscsi, multipath-tools, fio ; Windows Server — initiateur iSCSI, MPIO | Rédaction assistée (Copilot) | Non testé sur plateforme cible |

Précision : aucune commande de cette leçon n'a été exécutée lors de la rédaction ; les procédures sont à valider en VM jetable avant tout usage en production.