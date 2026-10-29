# Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_22_Synchronisation_Horaire_Ntp

- **Environnement** : Hôte VMware ESXi 8 (hyperviseur)
- **OS / Version** : VMware ESXi 8; étape 22 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `esxi8`, `vie-du-systeme`, `cycle-de-vie`, `etape-22`

---

## Problème précis à résoudre

Garder l'heure exacte.

## 1. Hors-Production (Lab / Test / POC)

1. Host Client : **Gérer > Système > Heure et date > Modifier les paramètres NTP** (Utiliser le protocole NTP, démarrage avec l'hôte, serveur NTP). En ligne de commande :
   ```sh
   esxcli system ntp set -s IP_NTP -e true
   esxcli system ntp get
   /etc/init.d/ntpd restart
   ```
   👉 Explication : `IP_NTP` = serveur NTP interne; `-e true` active le service (ESXi 8.0 U1 et supérieur).

2. Pour les versions antérieures : `vim-cmd hostsvc/datetime/info` et contrôle du service :
   ```sh
   vim-cmd hostsvc/datetime/info
   chkconfig ntpd on
   ```
   👉 Explication : vérifie l'heure et active le service au démarrage.

3. Appliquer la même source à tous les hôtes.
   👉 Explication : un écart perturbe vCenter, vSAN et les certificats.

## 2. Production — Contrôles

Au moins deux sources NTP internes.

## 3. Production — Sécurité

Autoriser NTP sortant uniquement vers les sources approuvées.

## Validation et retour arrière

- **Validation** : Le service NTP est démarré et l'heure est correcte.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire VMware ESXi 8](./Sommaire_-_Vie_du_systeme_ESXi_8.md)
- [Documentation officielle](https://docs.vmware.com/)
