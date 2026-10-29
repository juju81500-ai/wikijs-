---
title: "Fiche Simple - Proxmox VE 8 Systeme Depots Mises A Jour"
description: "Configurer les dépôts APT de Proxmox VE 8 (abonnement entreprise ou dépôt sans abonnement), appliquer les mises à jour du système et du catalogue des modèles de conteneurs LXC, sans interrompre les machines virtuelles en cours."
published: true
date: 2026-10-29T20:22:42Z
tags: ["[proxmox-ve-8]", "[debian-bookworm]", "[apt]", "[depots]", "[hardening]"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# 📄 Fiche_Simple_-_Proxmox_VE_8_Systeme_Depots_Mises_A_Jour.md

- **Environnement** : Hyperviseur Proxmox VE 8 (nœud autonome ou membre de cluster)
- **OS / Version** : Proxmox VE 8.x - Debian 12 Bookworm
- **Catégorie** : Système & Services / Dépôts et mises à jour
- **Tags** : `[proxmox-ve-8]`, `[debian-bookworm]`, `[apt]`, `[depots]`, `[hardening]`

---

## 🎯 Problème précis à résoudre
Configurer les dépôts APT de Proxmox VE 8 (abonnement entreprise ou dépôt sans abonnement), appliquer les mises à jour du système et du catalogue des modèles de conteneurs LXC, sans interrompre les machines virtuelles en cours.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Vérifier la version de Proxmox VE et les dépôts déclarés :
```bash
pveversion -v
ls /etc/apt/sources.list.d/
```
👉 Explication : `pveversion -v` affiche la version du paquet `proxmox-ve` et de ses composants ; `ls` liste les fichiers de dépôts Proxmox et Debian présents.

2. Désactiver le dépôt entreprise et activer le dépôt sans abonnement :
```bash
sed -i 's/^deb /# deb /' /etc/apt/sources.list.d/pve-enterprise.list
echo "deb http://download.proxmox.com/debian/pve bookworm pve-no-subscription" > /etc/apt/sources.list.d/pve-no-subscription.list
```
👉 Explication : la première ligne commente le dépôt entreprise, réservé aux abonnés ; la seconde crée le dépôt `pve-no-subscription` pour Debian 12 Bookworm. Si le dépôt entreprise est au format deb822 (`pve-enterprise.sources`), ajouter la ligne `Enabled: no` dans son bloc au lieu de commenter.

3. Mettre à jour les index et appliquer les correctifs :
```bash
apt update && apt full-upgrade -y
```
👉 Explication : `apt update` recharge les index des dépôts ; `apt full-upgrade` installe les mises à jour, y compris celles qui modifient des dépendances (noyau Proxmox, `pve-manager`).

4. Rafraîchir le catalogue des modèles de conteneurs LXC :
```bash
pveam update
pveam available --section system
```
👉 Explication : `pveam update` télécharge la liste à jour des modèles de conteneurs ; `pveam available --section system` affiche les distributions système disponibles au téléchargement.

5. Contrôler la cohérence des paquets :
```bash
apt-get check && dpkg --audit
```
👉 Explication : `apt-get check` signale les dépendances cassées ; `dpkg --audit` liste les paquets partiellement installés ou en erreur (aucune sortie = état sain).

---

## ⚡ 2. Production — Façon Simplifiée
1. Vérifier l'état de l'abonnement avant d'utiliser le dépôt entreprise :
```bash
pvesubscription get
```
👉 Explication : affiche le statut de l'abonnement Proxmox du nœud ; un abonnement valide est requis pour le dépôt `pve-enterprise`.

2. Réactiver le dépôt entreprise sur un nœud abonné :
```bash
sed -i 's/^# deb /deb /' /etc/apt/sources.list.d/pve-enterprise.list
apt update
```
👉 Explication : rétablit la ligne du dépôt `pve-enterprise` puis recharge les index APT.

3. Vérifier le dépôt d'origine du paquet Proxmox :
```bash
apt-cache policy proxmox-ve
```
👉 Explication : affiche la version installée, la version candidate et l'URL du dépôt qui fournit `proxmox-ve`, pour confirmer le dépôt retenu.

4. Sauvegarder la configuration APT avant la mise à jour :
```bash
tar -czf /root/apt-sauvegarde-$(date +%F).tar.gz /etc/apt
```
👉 Explication : conserve une copie des fichiers de dépôts pour revenir en arrière en cas d'erreur de configuration.

5. Appliquer les mises à jour pendant une fenêtre de maintenance :
```bash
apt update && apt full-upgrade -y && pveversion
```
👉 Explication : applique les mises à jour après migration ou arrêt des VM sensibles ; `pveversion` confirme la version finale. Un nouveau noyau nécessite un redémarrage du nœud, à planifier séparément.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Simuler la mise à jour avant application :
```bash
apt-get -s full-upgrade
```
👉 Explication : l'option `-s` (simulation) affiche les paquets qui seraient installés, mis à jour, supprimés ou retenus, sans rien modifier.

2. Installer les correctifs de sécurité automatiques :
```bash
apt install -y unattended-upgrades
```
👉 Explication : installe le mécanisme de mise à jour automatique des correctifs de sécurité Debian ; la configuration se trouve dans `/etc/apt/apt.conf.d/50unattended-upgrades`. Les mises à jour du noyau et de `pve-manager` restent à redémarrer ou à valider manuellement.

3. Vérifier le fonctionnement sans rien appliquer :
```bash
unattended-upgrade --dry-run --debug
```
👉 Explication : simule un passage de mises à jour automatiques et affiche les origines autorisées ainsi que les paquets concernés.

4. Contrôler qu'aucun paquet critique n'est figé :
```bash
apt-mark showhold
```
👉 Explication : liste les paquets bloqués sur leur version actuelle ; un paquet `proxmox-ve` ou `pve-manager` figé empêche les correctifs de sécurité et doit être justifié et documenté.