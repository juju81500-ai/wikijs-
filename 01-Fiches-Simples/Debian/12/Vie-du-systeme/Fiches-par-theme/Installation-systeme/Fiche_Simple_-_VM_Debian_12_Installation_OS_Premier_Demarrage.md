# 📄 Fiche_Simple_-_VM_Debian_12_Installation_OS_Premier_Demarrage.md

- **Environnement** : VM sur Proxmox VE, KVM ou VMware
- **OS / Version** : Debian GNU/Linux 12 (Bookworm)
- **Catégorie** : Installation / Système
- **Tags** : `[debian12]`, `[bookworm]`, `[debian]`, `[installation]`, `[vm]`, `[premier-demarrage]`

## 🎯 Problème précis à résoudre
Installer Debian 12 Bookworm sur une VM, choisir stockage et réseau, créer un compte d'administration et vérifier la version réelle avant l'installation de rôles.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Télécharger l'ISO depuis Debian et vérifier son empreinte publiée.
2. Créer une VM avec firmware, disque, CPU, mémoire et carte réseau adaptés au lab; monter l'ISO.
3. Dans l'installateur, choisir langue, hostname, réseau DHCP/statique et partitionnement guidé ou adapté au rôle.
4. Créer un compte nominatif et installer OpenSSH si requis. Redémarrer sans l'ISO.
5. Vérifier la machine :
   ```bash
   cat /etc/debian_version
   hostnamectl
   lsblk -f
   ip -br address
   systemctl --failed
   ```
   👉 *Explication : Debian 12 fournit les séries de paquets Bookworm; ne pas suivre automatiquement une fiche Debian 13.*

## ⚡ 2. Production — Façon Simplifiée
1. Vérifier l'édition ISO, la cible disque, l'espace `/boot`, les ressources et le plan IP/DNS avant l'installation.
2. Configurer dépôts Bookworm officiels et appliquer les mises à jour de la version cible avant les rôles.
3. Créer compte `sudo`, hostname, SSH par clé, réseau et heure avec les fiches Debian 12 correspondantes.
4. Installer uniquement les paquets nécessaires au rôle; relever les versions avec `apt-cache policy`.

## 🔒 3. Production — Façon Sécurisée
1. Vérifier la provenance du média et séparer les données applicatives du système selon le besoin de restauration.
2. Garder un accès console pendant les changements réseau et utiliser un accès SSH de secours.
3. Prévoir le cycle de support de Bookworm; utiliser les sources et correctifs adaptés à Debian 12.

## ✅ Validation et retour arrière
- Confirmer Bookworm, les dépôts, compte, stockage, adresse, DNS, SSH et services systemd.
- Prendre une sauvegarde initiale et vérifier sa présence avant d'installer les services critiques.
- Si l'installation est incorrecte, conserver les journaux puis reconstruire depuis l'ISO vérifié.