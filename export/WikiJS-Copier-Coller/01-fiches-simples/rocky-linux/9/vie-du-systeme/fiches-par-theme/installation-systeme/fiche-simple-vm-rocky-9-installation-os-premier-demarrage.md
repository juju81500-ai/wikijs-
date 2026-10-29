# 📄 Fiche_Simple_-_VM_Rocky_9_Installation_OS_Premier_Demarrage.md

- **Environnement** : VM sur Proxmox VE, KVM ou VMware
- **OS / Version** : Rocky Linux 9
- **Catégorie** : Installation / Système

## 🎯 Problème précis à résoudre
Installer Rocky Linux 9 sur une nouvelle VM depuis une image officielle, préparer le disque et créer un accès d'administration sans exposer le système avant les premiers contrôles.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Télécharger l'ISO depuis une source officielle Rocky et vérifier son empreinte selon les instructions du projet.
2. Créer une VM avec firmware, contrôleur disque, CPU, mémoire et carte réseau adaptés au lab; monter l'ISO.
3. Dans l'installateur, choisir langue, disque cible, profil logiciel minimal, interface réseau et mot de passe administrateur; créer un compte nominatif avec droits d'administration.
4. Après le premier démarrage, vérifier :
   ```bash
   cat /etc/rocky-release
   hostnamectl
   lsblk -f
   nmcli -f NAME,DEVICE connection show --active
   getenforce
   ```
   👉 *Explication : noms de profils, tailles de disque et interfaces sont propres à la VM.*

## ⚡ 2. Production — Façon Simplifiée
1. Vérifier l'ISO, les ressources, le plan de stockage, le réseau virtuel, le hostname et la méthode de sauvegarde.
2. Installer avec le schéma de partitionnement validé pour le rôle; n'activer que les logiciels nécessaires.
3. Appliquer les mises à jour et les fiches correspondantes pour DNF, utilisateur `wheel`, NetworkManager, Chrony et outils invités.
4. Garder SELinux en `Enforcing`; configurer firewalld pour les flux requis avant d'installer les rôles applicatifs.

## 🔒 3. Production — Façon Sécurisée
1. Utiliser une image vérifiée et une branche maintenue; contrôler la provenance des dépôts.
2. Conserver l'accès console pendant les changements réseau et éviter l'ouverture générale de services.
3. Séparer données applicatives et système si le plan de sauvegarde/restauration le justifie.

## ✅ Validation et retour arrière
- Confirmer version, disque, hostname, adresse, résolution, état SELinux, pare-feu et absence de services en échec.
- Tester une restauration de sauvegarde dans une VM isolée avant le déploiement d'applications.
- En cas d'installation incorrecte, conserver les journaux puis reconstruire à partir de l'image officielle vérifiée.