# Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_09_Identite_De_La_Machine

- **Environnement** : Hôte VMware ESXi 8 (hyperviseur)
- **OS / Version** : VMware ESXi 8; étape 09 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Nommer l'hôte avec un FQDN résolvable.

## 1. Hors-Production (Lab / Test / POC)

1. Host Client : **Gérer > Système > Mise en réseau > Pile TCP/IP par défaut > Modifier les paramètres** (nom d'hôte, domaine). Ou DCUI : **Configure Management Network > DNS Configuration**. En ligne de commande :
   ```sh
   esxcli system hostname set --host=esx01 --domain=domaine.local
   esxcli system hostname get
   ```
   👉 Explication : définit le nom court et le domaine (`esx01.domaine.local`).

2. Créer les enregistrements A et PTR correspondants dans le DNS.
   ```sh
   nslookup esx01.domaine.local
   ```
   👉 Explication : vCenter et les certificats exigent que le FQDN se résolve.

3. Changer le nom avant d'ajouter l'hôte à vCenter : le certificat est régénéré à ce moment.
   👉 Explication : un renommage après coup demande de régénérer le certificat.

## 2. Production — Contrôles

Nom conforme à la convention de nommage.

## 3. Production — Sécurité

Un nom explicite simplifie l'audit.

## Validation et retour arrière

- **Validation** : `esxcli system hostname get` renvoie le FQDN attendu.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire VMware ESXi 8](/01-fiches-simples/vmware/esxi-8/vie-du-systeme/sommaire-vie-du-systeme-esxi-8)
- [Documentation officielle](https://docs.vmware.com/)