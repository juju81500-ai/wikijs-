# 📄 VM_Debian_12_Systeme_Hostname-FQDN.md

- **Environnement** : VM (Proxmox VE / KVM)
- **OS / Version** : Debian 12 (Bookworm) - Famille Debian
- **Catégorie** : Système & Services / Identité de la machine
- **Tags** : `[debian12]`, `[debian-family]`, `[hostname]`, `[fqdn]`, `[hosts]`, `[systemd]`

## 🎯 Problème précis à résoudre
Définir le nom d'hôte statique et le FQDN d'un serveur Debian 12 de façon cohérente entre systemd (`hostnamectl`), `/etc/hosts` et le DNS, afin que `hostname -f` et les services (Zabbix, Samba, certificats, journaux) renvoient le même nom.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Consultation de l'identité actuelle de la machine :
   `hostnamectl status`
   👉 Explication : Affiche le nom d'hôte statique, le nom transitoire, l'identifiant de machine et le noyau avant toute modification.
2. Application d'un nom d'hôte court de test :
   `sudo hostnamectl set-hostname <nom_du_serveur>`
   👉 Explication : Écrit le nom statique dans `/etc/hostname` et l'applique immédiatement, sans redémarrage.
3. Vérification du nom court :
   `hostname`
   👉 Explication : Confirme que les nouveaux processus utilisent bien le nouveau nom.

---

## ⚡ 2. Production — Façon Simplifiée
1. Ajout du FQDN dans la table d'hôtes locale :
   `sudoedit /etc/hosts`
   👉 Explication : Ajoute la ligne `127.0.1.1 <nom_du_serveur>.<nom_du_domaine> <nom_du_serveur>` (format Debian par défaut) pour que la machine résolve son propre FQDN sans dépendre du DNS.
2. Vérification du FQDN :
   `hostname -f`
   👉 Explication : Doit renvoyer `<nom_du_serveur>.<nom_du_domaine>`. Sinon, la ligne `/etc/hosts` est absente ou mal formée.

---

## 🔒 3. Production — Façon Sécurisée (Cohérence DNS & Traçabilité)
1. Contrôle de la résolution directe du FQDN :
   `getent hosts <nom_du_serveur>.<nom_du_domaine>`
   👉 Explication : Interroge la chaîne NSS (fichiers puis DNS) et vérifie que l'adresse IP publiée correspond à la machine.
2. Contrôle de la résolution inverse (PTR) :
   `getent hosts <adresse_ip_du_serveur>`
   👉 Explication : Vérifie que la recherche inverse renvoie le même FQDN, condition attendue par Kerberos, les certificats et les journaux centralisés.
3. Relevé du nom statique pour la CMDB :
   `hostnamectl hostname`
   👉 Explication : Affiche uniquement le nom statique à reporter dans l'inventaire (étape 49 du cycle de vie).
