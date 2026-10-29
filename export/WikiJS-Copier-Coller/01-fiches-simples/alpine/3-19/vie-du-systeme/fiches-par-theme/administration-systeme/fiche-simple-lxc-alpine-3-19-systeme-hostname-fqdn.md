# 📄 Fiche_Simple_-_LXC_Alpine_3.19_Systeme_Hostname_FQDN.md

- **Environnement** : LXC (Proxmox VE)
- **OS / Version** : Alpine Linux 3.19 - Famille Alpine (OpenRC, apk)
- **Catégorie** : Système & Services / Identité réseau

## 🎯 Problème précis à résoudre
Définir le nom d'hôte court et le nom de domaine complet (FQDN) d'un conteneur Alpine Linux, en gardant cohérents `/etc/hostname`, `/etc/hosts` et la configuration du conteneur sur Proxmox.

> Alpine 3.19 est en fin de support : valider cette procédure sur une branche maintenue avant tout usage en production.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Afficher l'identité actuelle du conteneur :
   ```sh
   hostname
   hostname -f
   cat /etc/hostname
   ```
   👉 Explication : `hostname` renvoie le nom court, `hostname -f` le nom complet résolu, et `/etc/hostname` contient la valeur relue au démarrage par OpenRC.

2. Définir le nom court et l'appliquer immédiatement :
   ```sh
   echo "<nom_du_conteneur>" > /etc/hostname
   rc-service hostname restart
   ```
   👉 Explication : Le service OpenRC `hostname` applique le contenu de `/etc/hostname` sans redémarrer le conteneur.

3. Déclarer le FQDN dans la table d'hôtes locale :
   ```text
   127.0.0.1    localhost
   <ip_du_conteneur>    <nom_du_conteneur>.<domaine> <nom_du_conteneur>
   ```
   👉 Explication : `/etc/hosts` assure la résolution locale du FQDN même si le DNS est indisponible. Remplacer `<domaine>` par le suffixe DNS interne réel (par exemple `lab.example.lan`).

4. Vérifier la résolution locale :
   ```sh
   getent hosts <nom_du_conteneur>
   hostname -f
   ```
   👉 Explication : `getent` interroge la même chaîne de résolution que les applications (fichiers `/etc/hosts` puis DNS, selon `/etc/nsswitch.conf`).

---

## ⚡ 2. Production — Façon Simplifiée
1. Régler le nom du conteneur depuis l'hôte Proxmox, puis redémarrer le CT :
   ```sh
   pct set <vmid> --hostname <nom_du_conteneur>.<domaine>
   pct reboot <vmid>
   ```
   👉 Explication : Proxmox conserve le nom d'hôte dans la configuration `/etc/pve/lxc/<vmid>.conf`. Régler le nom depuis l'hôte évite les divergences entre l'inventaire Proxmox et le conteneur.

2. Contrôler le nom court et le FQDN après redémarrage :
   ```sh
   hostname -s
   hostname -f
   ```
   👉 Explication : `hostname -s` doit donner `<nom_du_conteneur>` et `hostname -f` le FQDN attendu par le DNS interne.

---

## 🔒 3. Production — Façon Sécurisée
1. Créer les enregistrements A et PTR correspondants dans le DNS interne, puis vérifier la correspondance inverse depuis le conteneur :
   ```sh
   getent hosts <ip_du_conteneur>
   ```
   👉 Explication : une correspondance directe et inverse cohérente évite les erreurs de certificats TLS et les mauvaises attributions dans les journaux.

2. Ne garder dans `/etc/hosts` que les entrées locales nécessaires, sans adresses de tiers ni secrets, et reporter le nom du conteneur dans l'inventaire (étape 49 du cycle de vie).