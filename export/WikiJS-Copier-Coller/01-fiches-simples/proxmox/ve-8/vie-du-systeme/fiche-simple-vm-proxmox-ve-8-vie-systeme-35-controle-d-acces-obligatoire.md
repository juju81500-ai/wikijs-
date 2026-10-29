# Fiche_Simple_-_VM_Proxmox_VE_8_Vie_Systeme_35_Controle_D_Acces_Obligatoire

- **Environnement** : Hôte Proxmox VE 8 (hyperviseur)
- **OS / Version** : Proxmox VE 8; étape 35 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Choisir le contrôle d'accès adapté à Debian/Proxmox.

## 1. Hors-Production (Lab / Test / POC)

1. Proxmox VE (Debian) n'utilise pas SELinux. Vérifier ce qui est actif :
   ```bash
   aa-status 2>/dev/null | head
   getenforce 2>/dev/null || echo 'SELinux absent'
   ```
   👉 Explication : AppArmor est peu utilisé sur l'hôte; l'isolation passe par KVM et les conteneurs non privilégiés.

2. Créer les conteneurs LXC en mode non privilégié (GUI : **Create CT > Unprivileged container** coché).
   ```bash
   pct config CTID | grep unprivileged
   ```
   👉 Explication : `CTID` = numéro du conteneur; `unprivileged: 1` attendu.

3. Limiter les droits via les rôles (GUI : **Datacenter > Permissions > Roles**).
   👉 Explication : le contrôle d'accès se fait au niveau de l'API Proxmox.

## 2. Production — Contrôles

Documenter l'absence de SELinux et le choix retenu.

## 3. Production — Sécurité

Ne pas installer SELinux sur l'hôte Proxmox (non pris en charge).

## Validation et retour arrière

- **Validation** : Conteneurs en mode non privilégié.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Proxmox VE 8](/01-fiches-simples/proxmox/ve-8/vie-du-systeme/sommaire-vie-du-systeme-proxmox-ve-8)
- [Documentation officielle](https://pve.proxmox.com/pve-docs/)