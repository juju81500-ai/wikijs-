# Fiche_Simple_-_Hote_Multi-OS_NAS_SAN_Verifier_Appliance_Reseau.md

- **Environnement** : Hôte Linux client ou serveur de stockage (Samba, NFSv4, iSCSI) et baie/NAS
- **OS / Version** : Multi-OS; clients et serveurs Linux, appliance de stockage
- **Catégorie** : diagnostic / stockage

---

## Problème précis à résoudre

Contrôler la baie/NAS puis la connectivité réseau côté client.

## 1. Hors-Production (Lab / Test / POC)

1. Sur la baie/NAS, examiner alertes constructeur, état des disques, pools, contrôleurs, interfaces, ventilateurs, capacité et réplication (interface d'administration du constructeur).
   👉 Explication : une panne matérielle explique la plupart des erreurs I/O.

2. Côté client, vérifier adresse, route et capacité (IP_STOCKAGE est une adresse d'exemple à remplacer par celle de la baie) :
   ```bash
   ip -br address
   ip route
   ping -c 4 IP_STOCKAGE
   df -h
   lsblk -f
   ```
   👉 Explication : on contrôle adresse, route, accessibilité et systèmes de fichiers vus.

3. Lire les erreurs noyau récentes :
   ```bash
   dmesg --level=err,warn | tail -n 80
   ```
   👉 Explication : les erreurs disque ou réseau récentes apparaissent.

4. Vérifier aussi DNS, MTU et VLAN de l'adresse de stockage depuis le bon réseau.
   👉 Explication : un ping réussi ne prouve pas que le partage ou la LUN fonctionne.

## 2. Production — Contrôles

Vérifier ensuite le protocole et le port réellement utilisés.

## 3. Production — Sécurité

- Ne pas modifier le réseau de stockage en production sans fenêtre de changement.

## Validation et retour arrière

- **Validation** : Baie saine ou anomalie identifiée; accès réseau à l'adresse de stockage confirmé.
- **Retour arrière** : Aucune modification; commandes en lecture seule.

## Si le problème n'est pas résolu

- [Samba — Documentation officielle](https://www.samba.org/samba/docs/)
- [Linux man-pages — exports(5)](https://man7.org/linux/man-pages/man5/exports.5.html)
- [open-iscsi — Documentation du projet](https://github.com/open-iscsi/open-iscsi)
- [Guide complet diagnostic NAS/SAN Samba NFS iSCSI](/02-fiches-completes/transverses/multi-os/diagnostic/38-diagnostic-nas-san-samba-nfs-iscsi#2-verifier-lappliance-et-le-reseau)