# Fiche_Simple_-_VM_Proxmox_VE_8_Vie_Systeme_38_Isolation_Des_Comptes_De

- **Environnement** : Hôte Proxmox VE 8 (hyperviseur)
- **OS / Version** : Proxmox VE 8; étape 38 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Séparer les accès techniques (supervision, sauvegarde) des comptes humains.

## 1. Hors-Production (Lab / Test / POC)

1. Créer un jeton d'API pour la supervision ou la sauvegarde (GUI : **Datacenter > Permissions > API Tokens > Add**) :
   ```bash
   pveum user add svc-supervision@pve
   pveum user token add svc-supervision@pve zabbix --privsep 1
   pveum acl modify / --users svc-supervision@pve --roles PVEAuditor
   ```
   👉 Explication : le jeton a un rôle lecture seule; la valeur secrète n'est affichée qu'une fois : la stocker dans le coffre-fort.

2. Lister les jetons :
   ```bash
   pveum user token list svc-supervision@pve
   ```
   👉 Explication : vérifie le compte et le jeton créés.

3. Ne pas donner `Administrator` à un compte de service.
   👉 Explication : un jeton volé ne doit permettre que la lecture.

## 2. Production — Contrôles

Un compte de service par usage; expiration des jetons si possible.

## 3. Production — Sécurité

Rotation régulière des jetons.

## Validation et retour arrière

- **Validation** : Le compte de service ne peut que lire (`PVEAuditor`).
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Fiche détaillée : Proxmox VE 8 Supervision Zabbix Snmp](</01-fiches-simples/proxmox/ve-8/vie-du-logiciel/zabbix/fiche-simple-proxmox-ve-8-supervision-zabbix-snmp>)
- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Proxmox VE 8](/01-fiches-simples/proxmox/ve-8/vie-du-systeme/sommaire-vie-du-systeme-proxmox-ve-8)
- [Documentation officielle](https://pve.proxmox.com/pve-docs/)