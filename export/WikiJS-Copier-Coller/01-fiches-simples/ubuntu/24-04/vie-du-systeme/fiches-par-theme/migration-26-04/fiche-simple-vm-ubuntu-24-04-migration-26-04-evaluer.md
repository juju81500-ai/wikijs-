# Fiche_Simple_-_VM_Ubuntu_24.04_Migration_26.04_Evaluer.md

- **Environnement** : VM ou serveur Ubuntu Server LTS
- **OS / Version** : Ubuntu Server 24.04 LTS (Noble) vers 26.04 LTS (Resolute)
- **Catégorie** : migration de version

---

## Problème précis à résoudre

Mesurer l'impact de la mise à niveau avant toute action.

## 1. Hors-Production (Lab / Test / POC)

1. Lire les notes de version 26.04 sur https://documentation.ubuntu.com/release-notes/26.04/.
   👉 Explication : elles donnent le chemin LTS exact et les changements.

2. Relever la version actuelle :
   ```bash
   cat /etc/os-release
   ```
   👉 Explication : on confirme partir de Ubuntu 24.04 (Noble).

3. Lister les applications installées et vérifier leur compatibilité avec 26.04.
   👉 Explication : PHP, PostgreSQL, OpenSSH, systemd, Netplan et APT changent de version.

## 2. Production — Contrôles

Décider go/no-go avec les responsables applicatifs.

## 3. Production — Sécurité

- Ne pas migrer un serveur de production sans test préalable sur une copie.

## Validation et retour arrière

- **Validation** : Le périmètre et les risques sont documentés.
- **Retour arrière** : Aucune modification : rien à annuler.

## Si le problème n'est pas résolu

- [Ubuntu 26.04 LTS — notes de version](https://documentation.ubuntu.com/release-notes/26.04/)
- [Ubuntu 24.04 LTS — notes de version](https://documentation.ubuntu.com/release-notes/24.04/)
- [Guide complet — évaluer la migration](/02-fiches-completes/ubuntu/24-04/installation-deploiement/22-migration-ubuntu-server-24-04-vers-26-04-lts#1-evaluer-la-migration)