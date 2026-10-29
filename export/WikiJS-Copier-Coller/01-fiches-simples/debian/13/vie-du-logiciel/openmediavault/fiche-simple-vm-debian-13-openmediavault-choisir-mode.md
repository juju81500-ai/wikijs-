# Fiche_Simple_-_VM_Debian_13_OpenMediaVault_Choisir_Mode.md

- **Environnement** : OpenMediaVault 8 sur Debian 13 minimal
- **OS / Version** : Debian 13; OpenMediaVault 8.0 Synchrony
- **Catégorie** : stockage / NAS

---

## Problème précis à résoudre

Décider si OMV s'installe sur une Debian 13 existante et vérifier les prérequis.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier qu'on n'est pas dans un conteneur :
   ```bash
   systemd-detect-virt
   ```
   👉 Explication : La réponse ne doit pas être `lxc` ni un autre conteneur : OMV ne s'y installe pas.

2. Lister les disques pour séparer système et données :
   ```bash
   lsblk -o NAME,SIZE,MODEL,SERIAL,TYPE
   ```
   👉 Explication : Un disque système dédié et des disques de données distincts sont requis.

3. Vérifier qu'aucun service critique ne tourne déjà sur l'hôte :
   ```bash
   systemctl list-units --type=service --state=running --no-pager
   ```
   👉 Explication : OMV peut remplacer la configuration réseau, SSH, Samba, Nginx et les montages.

## 2. Production — Contrôles

Prévoir accès console hors bande, sauvegarde, fenêtre de maintenance, IP statique, DNS et Ethernet filaire. Pour du matériel dédié, l'ISO OMV est recommandée.

## 3. Production — Sécurité

- Ne pas convertir un serveur Debian hébergeant des services critiques.
- Ne pas installer OMV dans LXC.

## Validation et retour arrière

- **Validation** : hôte non conteneurisé, disques identifiés, sauvegarde et console disponibles.
- **Retour arrière** : aucune modification; rien à annuler.

## Si le problème n'est pas résolu

- [OpenMediaVault — installation sur Debian](https://docs.openmediavault.org/en/latest/installation/on_debian.html)
- [OpenMediaVault — prérequis](https://docs.openmediavault.org/en/latest/prerequisites.html)
- [Guide complet OpenMediaVault Debian 13](/02-fiches-completes/debian/13/installation-deploiement/66-deploiement-openmediavault-8-debian-13#1-choisir-le-mode-de-deploiement)