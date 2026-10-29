# Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_17_Resolution_De_Noms_Client

- **Environnement** : Hôte VMware ESXi 8 (hyperviseur)
- **OS / Version** : VMware ESXi 8; étape 17 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Configurer les serveurs DNS de l'hôte.

## 1. Hors-Production (Lab / Test / POC)

1. Host Client : **Réseau > Pile TCP/IP > Pile TCP/IP par défaut > Modifier les paramètres** (DNS primaire/secondaire, domaine). En ligne de commande :
   ```sh
   esxcli network ip dns server add --server=IP_DNS
   esxcli network ip dns search add --domain=domaine.local
   esxcli network ip dns server list
   ```
   👉 Explication : `IP_DNS` = serveur DNS interne; ajouter un second serveur.

2. Tester la résolution :
   ```sh
   nslookup vcenter.domaine.local
   nslookup esx01.domaine.local
   ```
   👉 Explication : le FQDN de l'hôte et de vCenter doivent se résoudre.

3. Prévoir deux serveurs DNS.
   👉 Explication : évite une panne totale si un serveur tombe.

## 2. Production — Contrôles

Utiliser les DNS internes.

## 3. Production — Sécurité

Ne pas utiliser de DNS public non maîtrisé.

## Validation et retour arrière

- **Validation** : `nslookup` renvoie une adresse.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire VMware ESXi 8](/01-fiches-simples/vmware/esxi-8/vie-du-systeme/sommaire-vie-du-systeme-esxi-8)
- [Documentation officielle](https://docs.vmware.com/)