# 📄 Fiche_Simple_-_VM_Debian_13_Installation_OS_Premier_Demarrage.md

- **Environnement** : VM sur Proxmox VE, KVM ou VMware
- **OS / Version** : Debian GNU/Linux 13 (Trixie)
- **Catégorie** : Installation / Système
- **Tags** : `[debian13]`, `[debian]`, `[installation]`, `[vm]`, `[systemd]`, `[premier-demarrage]`

## 🎯 Problème précis à résoudre
Installer Debian 13 sur une nouvelle VM avec un partitionnement adapté au rôle, un compte administrateur nominatif et un accès de secours documenté.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Créer une VM et monter l'ISO Debian 13 vérifié; définir CPU, mémoire, disque, firmware et carte réseau selon le lab.
2. Dans l'installateur, choisir langue, région, clavier, nom d'hôte et domaine; configurer le réseau DHCP ou les valeurs du plan IP.
3. Choisir le partitionnement guidé pour le lab ou le partitionnement séparé justifié pour le rôle; vérifier les disques sélectionnés avant validation.
4. Créer un compte nominatif; éviter la connexion SSH root directe. Installer le serveur SSH et les utilitaires système nécessaires.
5. Redémarrer sans l'ISO puis vérifier :
   ```bash
   cat /etc/debian_version
   hostnamectl
   ip -br address
   systemctl --failed
   ```
   👉 *Explication : le nom exact des interfaces, la taille et la structure des volumes dépendent de la VM et du rôle.*

## ⚡ 2. Production — Façon Simplifiée
1. Vérifier l'ISO, les ressources, le contrôleur disque, le réseau virtuel et la méthode de sauvegarde de la VM avant l'installation.
2. Utiliser un schéma de partitionnement cohérent avec les besoins de stockage et de restauration; consigner les volumes et points de montage.
3. Après l'installation, configurer mises à jour, hostname, compte `sudo`, SSH par clé, réseau et synchronisation horaire en suivant les fiches Debian correspondantes.
4. Installer uniquement les paquets du rôle, puis prendre une sauvegarde initiale après validation du système.

## 🔒 3. Production — Façon Sécurisée
1. Ne pas réutiliser une image non vérifiée; contrôler la provenance de l'ISO et son empreinte selon la procédure Debian.
2. Garder une console hyperviseur et un compte de secours; ne pas basculer le réseau en statique à distance sans accès de retour.
3. Séparer les données applicatives du système lorsque le besoin de restauration et la conception le justifient.

## ✅ Validation et retour arrière
- Confirmer version, hostname, stockage, adresse, résolution DNS, SSH et état systemd.
- Tester une restauration de VM ou de sauvegarde de fichiers avant d'héberger des données de production.
- Si l'installation est incorrecte, conserver les journaux utiles puis reconstruire la VM depuis l'ISO validé plutôt que réparer des couches inconnues.