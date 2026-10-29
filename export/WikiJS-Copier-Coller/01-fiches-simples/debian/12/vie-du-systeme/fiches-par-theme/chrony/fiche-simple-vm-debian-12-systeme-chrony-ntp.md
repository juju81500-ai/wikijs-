# 📄 VM_Debian_12_Systeme_Chrony-NTP.md

- **Environnement** : VM (Proxmox VE / KVM)
- **OS / Version** : Debian 12 (Bookworm) - Famille Debian
- **Catégorie** : Système & Services / Synchronisation horaire

## 🎯 Problème précis à résoudre
Synchroniser l'horloge d'un serveur Debian 12 avec des sources NTP fiables au moyen de `chrony`, condition nécessaire à la validité des certificats, de Kerberos (AD) et à la corrélation des journaux.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation du démon chrony :
   `sudo apt-get update && sudo apt-get install -y chrony`
   👉 Explication : Installe `chrony` qui remplace le client NTP simple et ajoute `chronyc` pour le diagnostic.
2. Contrôle de l'état de synchronisation :
   `chronyc tracking`
   👉 Explication : Affiche le décalage (`System time`), la strate (`Stratum`) et la source de référence utilisée.
3. Liste des sources NTP et de leur qualité :
   `chronyc sources -v`
   👉 Explication : Les sources marquées `^*` sont les sources actives ; `^?` indique une source non joignable.

---

## ⚡ 2. Production — Façon Simplifiée
1. Désactivation de l'horloge concurrente systemd (si présente) :
   `sudo systemctl disable --now systemd-timesyncd`
   👉 Explication : Évite deux clients NTP qui se disputent l'horloge ; sans effet si l'unité n'est pas installée.
2. Définition des sources NTP :
   `sudoedit /etc/chrony/chrony.conf`
   👉 Explication : Garder `pool 2.debian.pool.ntp.org iburst` ou remplacer par `server <serveur_ntp_interne> iburst` lorsque le réseau interne dispose d'un serveur de temps.
3. Application de la configuration :
   `sudo systemctl restart chrony`
   👉 Explication : Recharge `chrony.conf` et relance la synchronisation avec les nouvelles sources.

---

## 🔒 3. Production — Façon Sécurisée (Serveur NTP Interne & Contrôle)
1. Autorisation limitée des clients NTP du réseau d'administration :
   `sudoedit /etc/chrony/chrony.conf`
   👉 Explication : Ajouter `allow <reseau_clients_ntp>` (ex. `10.10.0.0/24`) ; sans cette directive, chrony ne répond à aucun client.
2. Vérification de l'écoute UDP 123 restreinte :
   `sudo ss -ulpn | grep ':123'`
   👉 Explication : Confirme que le service n'écoute que sur les interfaces prévues et que le port NTP n'est pas exposé à tout le réseau.
3. Vérification de la synchronisation système :
   `timedatectl`
   👉 Explication : Doit afficher `System clock synchronized: yes` et `NTP service: active`.