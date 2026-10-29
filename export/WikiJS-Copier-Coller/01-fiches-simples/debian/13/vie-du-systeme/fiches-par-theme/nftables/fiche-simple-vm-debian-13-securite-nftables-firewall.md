# 📄 VM_Debian_13_Securite_Configuration-NFTables-Firewall.md

- **Environnement** : VM (Debian 13 Trixie / Kernel 6.x)
- **OS / Version** : Debian 13 (Trixie) - Famille Debian
- **Catégorie** : Sécurité / Pare-feu Kernel (nftables)

## 🎯 Problème précis à résoudre
Configurer le pare-feu natif `nftables` sur Debian 13 (Trixie) avec une politique par défaut fermée (Zero Trust drop), filtrer les flux entrants SSH et HTTP/HTTPS, et assurer la persistance des règles au redémarrage.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation du paquet nftables :
   `apt-get update && apt-get install -y nftables`
   👉 Explication : Installe l'outil CLI et le service d'administration des règles du filtre paquet Linux kernel.

2. Ajout temporaire d'une table et d'une chaîne de filtrage en mémoire :
   `nft add table inet filter && nft add chain inet filter input { type filter hook input priority 0 \; policy accept \; }`
   👉 Explication : Crée une table globale inet (IPv4 + IPv6) et une chaîne d'entrée permissive pour effectuer des tests sans risque de blocage.

3. Affichage des règles actives en mémoire :
   `nft list ruleset`
   👉 Explication : Liste l'intégralité du jeu de règles `nftables` actuellement chargées dans le noyau.

---

## ⚡ 2. Production — Façon Simplifiée
Avant toute politique `drop`, garder une console hyperviseur et une session de secours. Vérifier qu'aucun autre gestionnaire (Docker, Proxmox ou pare-feu d'entreprise) ne possède déjà le ruleset. Le fichier suivant remplace toutes les règles : ne pas l'utiliser tel quel sur un hôte Docker.

Dans `/etc/nftables.conf`, adapter le réseau d'administration et supprimer les ports inutiles :
```nft
#!/usr/sbin/nft -f
flush ruleset
table inet filter {
   chain input {
      type filter hook input priority filter; policy drop;
      iifname "lo" accept
      ct state invalid drop
      ct state established,related accept
      ip protocol icmp accept
      meta l4proto ipv6-icmp accept
      ip saddr 192.0.2.0/24 tcp dport 22 accept
      tcp dport { 80, 443 } accept
   }
   chain forward { type filter hook forward priority filter; policy drop; }
   chain output { type filter hook output priority filter; policy accept; }
}
```
`192.0.2.0/24` est un exemple documentaire : remplacer par le vrai réseau d'administration. Retirer HTTP/HTTPS s'ils ne sont pas utilisés.

2. Activation et démarrage du service nftables au boot :
   `systemctl enable --now nftables`
   👉 Explication : Charge les règles du fichier `/etc/nftables.conf` au démarrage de la machine.

---

## 🔒 3. Production — Validation et application contrôlées

1. Sauvegarder la configuration et valider sa syntaxe sans charger les règles :
   ```bash
   sudo cp -a /etc/nftables.conf /etc/nftables.conf.bak
   sudo nft -c -f /etc/nftables.conf
   ```
2. Depuis la console ou une fenêtre de maintenance, appliquer le fichier et activer le chargement au démarrage :
   ```bash
   sudo nft -f /etc/nftables.conf
   sudo systemctl enable --now nftables
   sudo nft list ruleset
   ```
3. Vérifier depuis un second terminal que SSH et les services prévus restent accessibles. Conserver la session de secours ouverte jusqu'à cette validation.

Les commandes `nft add rule` ajoutent des règles temporaires et peuvent créer des doublons ; ne pas les utiliser comme méthode de configuration. Ne pas appliquer un limiteur SSH générique sans test : privilégier la restriction aux réseaux d'administration, une authentification par clé et un outil de bannissement configuré.