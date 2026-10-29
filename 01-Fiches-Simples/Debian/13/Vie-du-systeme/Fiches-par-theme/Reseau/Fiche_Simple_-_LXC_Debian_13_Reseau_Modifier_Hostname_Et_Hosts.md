# 📄 LXC_Debian_13_Reseau_Modifier-Hostname-Et-Hosts.md

- **Environnement** : LXC (Proxmox VE / Debian 13)
- **OS / Version** : Debian 13 (Trixie) - Famille Debian
- **Catégorie** : Système & Réseau / Hostname
- **Tags** : `[debian13]`, `[lxc]`, `[hostname]`, `[hosts]`, `[proxmox]`, `[hardening]`

## 🎯 Problème précis à résoudre
Modifier le nom d'hôte d'un conteneur LXC Debian 13 en conservant Proxmox VE comme source de configuration et en gardant cohérents le DNS et `/etc/hosts`.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Sur l'hôte Proxmox, définir un nom de test pour le conteneur :
   `pct set CTID --hostname lxc-test`
   👉 Explication : Le changement reste géré par Proxmox et ne modifie pas directement les fichiers générés du CT.

2. Contrôle de l'affichage du nom d'hôte :
   `hostname -f`
   👉 Explication : Affiche le nom FQDN actuellement résolu localement.

---

## ⚡ 2. Production — Façon Simplifiée
1. Sur l'hôte Proxmox, relever la configuration du conteneur puis modifier son hostname via l'outil de gestion :
   ```bash
   pct config CTID
   pct set CTID --hostname lxc-app-01 --searchdomain lab.local
   ```
   👉 Explication : Remplacer `CTID` et le nom de domaine par les valeurs réelles. Proxmox reste la source de vérité pour le conteneur.

2. Vérifier la résolution DNS du nom depuis le réseau, puis vérifier le hostname dans le CT :
   ```bash
   pct exec CTID -- hostname
   pct exec CTID -- hostname -f
   pct exec CTID -- getent hosts lxc-app-01.lab.local
   ```
   👉 Explication : Le DNS interne doit contenir l'enregistrement correspondant ; `/etc/hosts` ne remplace pas une entrée DNS partagée.

3. Si une entrée locale est nécessaire, éditer `/etc/hosts` sans remplacer le fichier complet. Conserver les lignes localhost et IPv6, et sauvegarder avant modification.

---

## 🔒 3. Production — Façon Sécurisée
1. Documenter l'ID du CT, son hostname, le domaine de recherche et les enregistrements DNS direct/inverse dans l'inventaire.
2. Ne pas créer de marqueur Proxmox non documenté ni appliquer `chattr +i` à `/etc/hostname` ou `/etc/hosts`. Si la régénération des fichiers par Proxmox doit être modifiée, suivre la documentation correspondant à la version et tester après redémarrage en lab.
3. Vérifier le nom court et le FQDN après redémarrage et depuis un client :
   ```bash
   pct exec CTID -- hostnamectl status
   getent hosts lxc-app-01.lab.local
   ```
4. En cas d'incohérence, corriger la configuration Proxmox et le DNS interne, puis préserver les lignes localhost/IPv6 plutôt que remplacer tout le fichier.