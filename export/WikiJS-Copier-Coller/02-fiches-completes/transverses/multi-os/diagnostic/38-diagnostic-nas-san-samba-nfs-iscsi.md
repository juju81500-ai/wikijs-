# Diagnostiquer un incident NAS/SAN : SMB, NFS et iSCSI

- **Type de fiche** : Diagnostic
- **Environnement** : Serveur Linux, NAS ou SAN; client de test autorisé
- **OS / Version** : Linux client/serveur ou appliance de stockage; adapter les commandes à la version et au constructeur
- **Rôle** : Isoler les pannes de stockage sans provoquer de perte de données ni de split-brain

## 1. Protéger les données et définir l'incident

Fiche simple : [protéger les données et cadrer l'incident](/01-fiches-simples/transverses/multi-os/nas-san/fiche-simple-hote-multi-os-nas-san-proteger-donnees-incident).

Identifier service, partage/LUN, hôtes touchés, heure de début, erreurs, changements récents et état des sauvegardes. Suspendre les migrations et écritures non nécessaires si des erreurs I/O ou un risque de corruption sont observés.

Ne pas formater, forcer un démontage, réinitialiser une baie, supprimer une session iSCSI ou remonter une LUN en écriture depuis plusieurs hôtes. En cluster, vérifier le propriétaire actif et le mécanisme de réservation avant action.

## 2. Vérifier l'appliance et le réseau

Fiche simple : [vérifier l'appliance et le réseau](/01-fiches-simples/transverses/multi-os/nas-san/fiche-simple-hote-multi-os-nas-san-verifier-appliance-reseau).

Sur la baie/NAS, examiner les alertes constructeur, état des disques, pools, contrôleurs, interfaces, ventilateurs, capacité et réplication. Côté client, vérifier adresse, route, DNS, MTU, VLAN et accessibilité de l'adresse de stockage depuis le bon réseau.

```bash
ip -br address
ip route
ping -c 4 <IP_STOCKAGE>
df -h
lsblk -f
dmesg --level=err,warn | tail -n 80
```

Un ping réussi ne prouve pas qu'un partage ou une LUN est opérationnel; vérifier ensuite le protocole et le port réellement utilisés.

## 3. Diagnostiquer SMB/Samba

Fiche simple : [diagnostiquer SMB/Samba](/01-fiches-simples/transverses/multi-os/nas-san/fiche-simple-hote-multi-os-nas-san-diagnostiquer-smb-samba).

Sur le serveur Samba, contrôler configuration et service :

```bash
sudo testparm -s
sudo systemctl --no-pager status smbd
sudo smbstatus
sudo journalctl -u smbd --since "30 minutes ago" --no-pager
```

Depuis un client autorisé, vérifier la découverte et l'authentification avec `smbclient` ou l'outil natif. Contrôler nom de partage, ACL/permissions, résolution DNS et dialecte/signature SMB. Ne pas assouplir la signature ou le chiffrement globalement pour rétablir un seul client incompatible.

## 4. Diagnostiquer NFSv4

Fiche simple : [diagnostiquer NFSv4](/01-fiches-simples/transverses/multi-os/nas-san/fiche-simple-hote-multi-os-nas-san-diagnostiquer-nfsv4).

Sur le serveur, examiner exports, service et journaux :

```bash
sudo exportfs -v
sudo systemctl --no-pager status nfs-server
sudo journalctl -u nfs-server --since "30 minutes ago" --no-pager
```

Sur le client, vérifier la version et les options du montage avec `nfsstat -m`, le point de montage avec `findmnt` et la résolution du serveur. Contrôler réseau autorisé, export, UID/GID, ACL et éventuel problème de verrouillage. Ne pas ajouter `no_root_squash` pour contourner un refus d'accès.

## 5. Diagnostiquer iSCSI et multipath

Fiche simple : [diagnostiquer iSCSI et multipath](/01-fiches-simples/transverses/multi-os/nas-san/fiche-simple-hote-multi-os-nas-san-diagnostiquer-iscsi-multipath).

```bash
sudo iscsiadm -m session
sudo multipath -ll
lsblk -o NAME,TYPE,SIZE,FSTYPE,MOUNTPOINTS
sudo journalctl -b --no-pager | grep -Ei 'iscsi|multipath|scsi|I/O error'
```

Comparer les sessions et chemins aux IQN, LUN, ACL, VLAN et contrôleurs attendus. Vérifier multipath et réservations persistantes selon la conception. Si un chemin est perdu, ne pas déconnecter les autres chemins ni forcer une bascule sans procédure constructeur et validation de l'application.

## 6. Tester une correction de manière sûre

Fiche simple : [tester une correction de manière sûre](/01-fiches-simples/transverses/multi-os/nas-san/fiche-simple-hote-multi-os-nas-san-tester-correction-sure).

Capturer les logs et états avant changement. Tester lecture/écriture uniquement dans un répertoire ou fichier de contrôle approuvé, avec un nom unique et suppression limitée à ce fichier. Valider permissions, latence, intégrité, reprise après reconnexion et comportement des autres clients.

Pour une erreur de capacité, quotas et snapshots, vérifier l'espace du pool, les réservations et l'espace réellement consommé : un snapshot peut retenir des blocs même si le partage paraît vide.

## 7. Escalade et clôture

Fiche simple : [escalader et clôturer](/01-fiches-simples/transverses/multi-os/nas-san/fiche-simple-hote-multi-os-nas-san-escalade-cloture).

En cas d'erreurs matérielles, corruption, chemins multiples incohérents ou cluster non propriétaire, arrêter les écritures selon le runbook et contacter l'équipe stockage/constructeur. Consigner sorties non sensibles, topologie, versions, volumes impactés et dernière sauvegarde vérifiée.

## Sources

- [Samba — Documentation officielle](https://www.samba.org/samba/docs/)
- [Linux man-pages — exports(5)](https://man7.org/linux/man-pages/man5/exports.5.html)
- [open-iscsi — Documentation du projet](https://github.com/open-iscsi/open-iscsi)
- [Docker — Réseau et stockage](https://docs.docker.com/engine/storage/)