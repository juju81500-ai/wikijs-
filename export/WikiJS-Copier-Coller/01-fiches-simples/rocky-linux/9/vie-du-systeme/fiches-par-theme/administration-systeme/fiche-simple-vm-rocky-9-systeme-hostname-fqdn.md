# 📄 Fiche_Simple_-_VM_Rocky_9_Systeme_Hostname_FQDN.md

- **Environnement** : VM ou serveur Rocky Linux
- **OS / Version** : Rocky Linux 9 / RHEL 9 avec systemd
- **Catégorie** : Système & Services / Identité de la machine

## 🎯 Problème précis à résoudre
Définir le nom d'hôte statique et le FQDN d'une VM Rocky Linux 9 avec `hostnamectl`, afin que les journaux, les certificats, l'annuaire et le DNS utilisent le même nom.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Afficher l'identité actuelle de la machine :
   ```bash
   hostnamectl status
   ```
   👉 Explication : Affiche le nom statique, le nom transitoire, l'identifiant de machine et la version de l'OS.

2. Définir le nom d'hôte complet (FQDN) :
   ```bash
   sudo hostnamectl set-hostname <nom_du_serveur>.<domaine>
   ```
   👉 Explication : Écrit le nom statique dans `/etc/hostname` et l'applique immédiatement au noyau. Le nom court correspond à la partie située avant le premier point.

---

## ⚡ 2. Production — Façon Simplifiée
1. Vérifier le nom statique et le FQDN retourné par le système :
   ```bash
   hostnamectl --static
   hostname -s
   hostname -f
   ```
   👉 Explication : `hostname -s` donne le nom court, `hostname -f` le FQDN. Si `hostname -f` échoue, la résolution du nom n'est pas encore configurée (voir la fiche DNS et /etc/hosts).

2. Ajouter le FQDN local dans `/etc/hosts` pour ne pas dépendre du DNS au démarrage :
   ```bash
   sudo vi /etc/hosts
   getent hosts <nom_du_serveur>
   ```
   👉 Explication : Ajouter une ligne du type `<ip_du_serveur> <nom_du_serveur>.<domaine> <nom_du_serveur>`. `getent hosts` interroge les sources de `/etc/nsswitch.conf` et confirme la résolution.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Contrôler les droits des fichiers d'identité :
   ```bash
   ls -l /etc/hostname /etc/hosts
   ```
   👉 Explication : Les deux fichiers doivent appartenir à `root` avec des droits `-rw-r--r--`. Un fichier modifiable par un autre utilisateur permettrait de changer l'identité du serveur.

2. Ne pas renommer un serveur déjà joint à un domaine sans procédure :
   ```bash
   sudo realm list
   ```
   👉 Explication : Si la commande affiche un domaine, le compte machine Active Directory est lié au nom actuel. Il faut le recréer ou le réinitialiser avant de changer le nom (voir la fiche jonction AD et sssd).