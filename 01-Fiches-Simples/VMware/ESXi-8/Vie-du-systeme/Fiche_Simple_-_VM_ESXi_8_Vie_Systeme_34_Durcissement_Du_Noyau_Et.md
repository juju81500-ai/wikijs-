# Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_34_Durcissement_Du_Noyau_Et

- **Environnement** : Hôte VMware ESXi 8 (hyperviseur)
- **OS / Version** : VMware ESXi 8; étape 34 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `esxi8`, `vie-du-systeme`, `cycle-de-vie`, `etape-34`

---

## Problème précis à résoudre

Appliquer des paramètres de sécurité prudents.

## 1. Hors-Production (Lab / Test / POC)

1. Host Client : **Réseau > Commutateurs virtuels > vSwitch > Modifier > Sécurité** : mode promiscuous = Rejeter, modifications d'adresse MAC = Rejeter, transmissions forgées = Rejeter. En ligne de commande :
   ```sh
   esxcli network vswitch standard policy security set -v vSwitch0 --allow-promiscuous=false --allow-mac-change=false --allow-forged-transmits=false
   esxcli network vswitch standard policy security get -v vSwitch0
   ```
   👉 Explication : empêche l'espionnage et l'usurpation entre VM.

2. Désactiver les fonctions inutiles :
   ```sh
   esxcli system settings advanced set -o /UserVars/SuppressShellWarning -i 0
   esxcli system settings advanced set -o /Net/BlockGuestBPDU -i 1
   ```
   👉 Explication : garde l'avertissement de shell et bloque les BPDU venant des VM.

3. Activer `execInstalledOnly` si Secure Boot est actif :
   ```sh
   esxcli system settings kernel set -s execInstalledOnly -v TRUE
   ```
   👉 Explication : n'autorise que les binaires installés via VIB signé.

## 2. Production — Contrôles

Appliquer sur chaque vSwitch et groupe de ports.

## 3. Production — Sécurité

Documenter chaque exception (par exemple un pare-feu virtuel qui exige le mode promiscuous).

## Validation et retour arrière

- **Validation** : Les trois options de sécurité sont à `false`.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire VMware ESXi 8](./Sommaire_-_Vie_du_systeme_ESXi_8.md)
- [Documentation officielle](https://docs.vmware.com/)
