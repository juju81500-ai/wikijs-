# Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_30_Protection_Contre_Le_Brute

- **Environnement** : Hôte VMware ESXi 8 (hyperviseur)
- **OS / Version** : VMware ESXi 8; étape 30 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Bloquer les tentatives répétées de connexion.

## 1. Hors-Production (Lab / Test / POC)

1. Host Client : **Gérer > Avancé** : rechercher `Security.AccountLockFailures`. En ligne de commande :
   ```sh
   esxcli system settings advanced set -o /Security/AccountLockFailures -i 5
   esxcli system settings advanced set -o /Security/AccountUnlockTime -i 900
   ```
   👉 Explication : verrouille le compte après 5 échecs pendant 15 minutes.

2. Contrôler les valeurs :
   ```sh
   esxcli system settings advanced list -o /Security/AccountLockFailures
   ```
   👉 Explication : valeur `5` attendue.

3. Surveiller les échecs de connexion :
   ```sh
   grep -i 'authentication failure\|Failed password' /var/log/auth.log /var/log/hostd.log | tail
   ```
   👉 Explication : repère une tentative d'attaque.

## 2. Production — Contrôles

Alerter sur les verrouillages de compte.

## 3. Production — Sécurité

Compte `root` surveillé en priorité.

## Validation et retour arrière

- **Validation** : Après 5 échecs, le compte est verrouillé.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire VMware ESXi 8](/01-fiches-simples/vmware/esxi-8/vie-du-systeme/sommaire-vie-du-systeme-esxi-8)
- [Documentation officielle](https://docs.vmware.com/)