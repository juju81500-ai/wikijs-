# Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_27_Durcissement_De_L_Acces

- **Environnement** : Hôte VMware ESXi 8 (hyperviseur)
- **OS / Version** : VMware ESXi 8; étape 27 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Réduire l'exposition de SSH et de la console.

## 1. Hors-Production (Lab / Test / POC)

1. Host Client : **Gérer > Services > TSM-SSH > Arrêter** et stratégie **Démarrer et arrêter manuellement**; durcir sshd dans `/etc/ssh/sshd_config` (`PermitRootLogin`, `PasswordAuthentication no`). En ligne de commande :
   ```sh
   esxcli system settings advanced set -o /UserVars/ESXiShellInteractiveTimeout -i 900
   esxcli system settings advanced set -o /UserVars/ESXiShellTimeout -i 900
   vim-cmd hostsvc/stop_ssh
   ```
   👉 Explication : ferme automatiquement les sessions inactives (900 s) et arrête SSH.

2. Activer le mode verrouillage (Host Client : **Hôte > Actions > Services > Activer le mode de verrouillage** si vCenter gère l'hôte) :
   ```sh
   vim-cmd -U dcui vimsvc/auth/lockdown_mode_enter
   ```
   👉 Explication : lockdown : l'hôte n'est géré que par vCenter.

3. Limiter l'accès au Host Client par adresse (étape 29).
   👉 Explication : réduit l'exposition de l'interface web.

## 2. Production — Contrôles

Garder l'accès DCUI en secours.

## 3. Production — Sécurité

Accès via VPN ou machine de rebond.

## Validation et retour arrière

- **Validation** : SSH est arrêté et le timeout appliqué.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire VMware ESXi 8](/01-fiches-simples/vmware/esxi-8/vie-du-systeme/sommaire-vie-du-systeme-esxi-8)
- [Documentation officielle](https://docs.vmware.com/)