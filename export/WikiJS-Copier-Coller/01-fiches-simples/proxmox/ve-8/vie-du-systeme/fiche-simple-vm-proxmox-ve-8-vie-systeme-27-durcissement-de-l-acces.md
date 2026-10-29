# Fiche_Simple_-_VM_Proxmox_VE_8_Vie_Systeme_27_Durcissement_De_L_Acces

- **Environnement** : Hôte Proxmox VE 8 (hyperviseur)
- **OS / Version** : Proxmox VE 8; étape 27 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Réduire l'exposition de SSH et de l'interface web.

## 1. Hors-Production (Lab / Test / POC)

1. Éditer `/etc/ssh/sshd_config` :
   ```bash
   PermitRootLogin prohibit-password
   PasswordAuthentication no
   MaxAuthTries 3
   AllowUsers ADMIN1
   # puis :
   sshd -t && systemctl reload ssh
   ```
   👉 Explication : interdit le mot de passe, limite les essais, restreint les utilisateurs; `sshd -t` valide la syntaxe.

2. Limiter l'accès à l'interface web 8006 (GUI : **Datacenter > Firewall > Add** : Macro/Port 8006, source = réseau d'administration).
   👉 Explication : l'interface n'est joignable que depuis le VLAN d'administration.

3. Contrôler la configuration effective :
   ```bash
   sshd -T | grep -E 'permitrootlogin|passwordauthentication|allowusers'
   ```
   👉 Explication : affiche les valeurs réellement appliquées.

## 2. Production — Contrôles

Garder une session ouverte pendant le test.

## 3. Production — Sécurité

Accès via VPN ou machine de rebond.

## Validation et retour arrière

- **Validation** : La connexion par mot de passe est refusée.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Proxmox VE 8](/01-fiches-simples/proxmox/ve-8/vie-du-systeme/sommaire-vie-du-systeme-proxmox-ve-8)
- [Documentation officielle](https://pve.proxmox.com/pve-docs/)