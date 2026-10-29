# 📄 VM_Debian_12_Reseau_Diagnostique-Netcat-SS-Tcpdump.md

- **Environnement** : VM / LXC (Debian 12 Bookworm)
- **OS / Version** : Debian 12 - Famille Debian
- **Catégorie** : Réseau & Dépannage / Diagnostic Flux
- **Tags** : `[debian12]`, `[netcat]`, `[ss]`, `[tcpdump]`, `[reseau]`, `[depannage]`, `[hardening]`

## 🎯 Problème précis à résoudre
Diagnostiquer les pannes de connectivité réseau, analyser les sockets en écoute et capturer le trafic paquet par paquet sur Debian 12 avec les outils `ss`, `netcat` (`nc`), `tcpdump` et `traceroute`.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Test rapide de portée d'un port TCP distant avec netcat :
   `nc -zvw3 192.168.1.50 80`
   👉 Explication : Tente une connexion sur le port 80 avec un délai d'attente de 3 secondes sans envoyer de données.
2. Écoute temporaire sur un port pour simuler un service :
   `nc -lvp 4444`
   👉 Explication : Ouvre le port TCP 4444 en écoute locale pour vérifier la traversée d'un pare-feu.

---

## ⚡ 2. Production — Façon Simplifiée
1. Inspection de tous les ports TCP/UDP en écoute avec processus associés :
   `ss -tulnp`
   👉 Explication : Affiche la liste exacte des démons réseau actifs, leurs IP d'écoute et leurs numéros de PID.
2. Capture en direct des paquets sur une interface spécifique :
   `tcpdump -i eth0 -n host 192.168.1.50 and port 443`
   👉 Explication : Filtre et affiche le trafic HTTPS échangé spécifiquement avec la machine 192.168.1.50.
3. Analyse du chemin réseau étape par étape :
   `traceroute -n 8.8.8.8`
   👉 Explication : Identifie les routeurs et sauts intermédiaires traversés vers la destination.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Export d'une capture de paquets dans un fichier `.pcap` pour analyse sous Wireshark :
   `tcpdump -i eth0 -s 0 -w /var/log/capture-incidents.pcap port 22 or port 443`
   👉 Explication : Enregistre l'intégralité du contenu des paquets pour un audit de sécurité ultérieur.
2. Verrouillage immédiat des accès au fichier de capture :
   `chmod 600 /var/log/capture-incidents.pcap && chown root:root /var/log/capture-incidents.pcap`
   👉 Explication : Empêche la lecture des captures réseau pouvant contenir des données sensibles.
3. Nettoyage et suppression sécurisée des fichiers de capture après la phase d'investigation :
   `rm -f /var/log/capture-incidents.pcap`
   👉 Explication : Purge les traces d'audit réseau de la machine de production.