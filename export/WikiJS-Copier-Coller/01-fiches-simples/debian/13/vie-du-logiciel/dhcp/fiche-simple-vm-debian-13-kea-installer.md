# Fiche_Simple_-_VM_Debian_13_Kea_Installer.md

- **Environnement** : VM Debian 13 serveur DHCPv4 sur un VLAN de test isolé
- **OS / Version** : Debian 13 Trixie x86-64; ISC Kea (canal stable)
- **Catégorie** : réseau / DHCP

---

## Problème précis à résoudre

Installer Kea DHCPv4 depuis le dépôt stable ISC et repérer l'unité systemd Debian.

## 1. Hors-Production (Lab / Test / POC)

1. Configurer le dépôt **stable** ISC Cloudsmith pour Debian 13 en suivant son instruction « Set Me Up », puis contrôler origine et version :
   ```bash
   apt-cache policy isc-kea isc-kea-dhcp4
   sudo apt update
   ```
   👉 Explication : la version candidate doit provenir du canal stable ISC.

2. Installer les paquets DHCPv4 et d'administration :
   ```bash
   sudo apt install isc-kea-dhcp4 isc-kea-admin
   ```
   👉 Explication : `isc-kea-dhcp-ddns` n'est à ajouter que si les mises à jour DNS sont prévues.

3. Repérer l'unité systemd réelle :
   ```bash
   systemctl cat isc-kea-dhcp4-server.service
   sudo systemctl status isc-kea-dhcp4-server.service --no-pager
   ```
   👉 Explication : sur Debian l'unité s'appelle `isc-kea-dhcp4-server.service`.

## 2. Production — Contrôles

Figer le canal stable et la série majeure; documenter la procédure de mise à niveau.

## 3. Production — Sécurité

- Éviter le dépôt de développement.
- Ne pas changer de série majeure sans plan de mise à jour.

## Validation et retour arrière

- **Validation** : `apt-cache policy` montre un paquet stable ISC installé et l'unité existe.
- **Retour arrière** : `sudo apt remove isc-kea-dhcp4 isc-kea-admin` puis retirer le dépôt ISC si inutile.

## Si le problème n'est pas résolu

- [ISC Kea — Installation](https://kea.readthedocs.io/en/latest/arm/install.html)
- [Guide complet Kea DHCPv4 Debian 13](/02-fiches-completes/debian/13/installation-deploiement/64-deploiement-kea-dhcpv4-debian-13#2-installer-le-paquet-isc-stable)