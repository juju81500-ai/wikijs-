# Fiche_Simple_-_VM_Proxmox_VE_8_Vie_Systeme_10_Compte_Super_Administrateur

- **Environnement** : Hôte Proxmox VE 8 (hyperviseur)
- **OS / Version** : Proxmox VE 8; étape 10 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Définir le mot de passe root de l'hôte.

## 1. Hors-Production (Lab / Test / POC)

1. Dans l'installateur : champ **Password** et **Email** (l'adresse reçoit les alertes).
   👉 Explication : ce compte est `root@pam`; il se connecte à l'interface web avec le domaine **Linux PAM**.

2. Après installation, changer le mot de passe au besoin :
   ```bash
   passwd root
   ```
   👉 Explication : demande le nouveau mot de passe deux fois.

3. Stocker le mot de passe dans le coffre-fort de l'équipe et activer le 2FA sur le compte (GUI : **Datacenter > Permissions > Two Factor**).
   👉 Explication : le 2FA protège l'accès à l'interface web.

## 2. Production — Contrôles

Mot de passe long (14 caractères ou plus), unique, dans le coffre-fort.

## 3. Production — Sécurité

Ne pas utiliser root au quotidien : créer des comptes nominatifs à l'étape suivante.

## Validation et retour arrière

- **Validation** : Connexion à https://IP_HOTE:8006 réussie.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Proxmox VE 8](/01-fiches-simples/proxmox/ve-8/vie-du-systeme/sommaire-vie-du-systeme-proxmox-ve-8)
- [Documentation officielle](https://pve.proxmox.com/pve-docs/)