# 📄 VM_Debian_12_Reseau_Hosts-Resolv.md

- **Environnement** : VM (Proxmox VE / KVM)
- **OS / Version** : Debian 12 (Bookworm) - Famille Debian
- **Catégorie** : Réseau & Services / Résolution de noms

## 🎯 Problème précis à résoudre
Gérer la résolution de noms d'un serveur Debian 12 : table locale `/etc/hosts`, serveurs DNS dans `/etc/resolv.conf` et ordre de résolution défini par `/etc/nsswitch.conf`, pour joindre les machines du domaine sans dépendre d'une requête DNS externe.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Consultation du résolveur actuel :
   `cat /etc/resolv.conf`
   👉 Explication : Affiche les serveurs DNS (`nameserver`) et le domaine de recherche (`search`) utilisés par la machine.
2. Installation des outils de test DNS :
   `sudo apt-get install -y dnsutils`
   👉 Explication : Installe `dig` et `host` pour interroger directement les serveurs DNS.
3. Test de résolution d'un nom local :
   `getent hosts <nom_hote>`
   👉 Explication : Teste la résolution réelle selon l'ordre NSS, exactement comme les applications la voient.

---

## ⚡ 2. Production — Façon Simplifiée
1. Ajout des noms internes dans la table locale :
   `sudoedit /etc/hosts`
   👉 Explication : Ajoute des lignes `<adresse_ip> <nom_hote>.<nom_du_domaine> <nom_hote>` pour les serveurs critiques, utiles en cas d'indisponibilité du DNS.
2. Définition des serveurs DNS et du domaine de recherche :
   `sudoedit /etc/resolv.conf`
   👉 Explication : Renseigner `nameserver <ip_dns_primaire>`, `nameserver <ip_dns_secondaire>` et `search <nom_du_domaine>` (fichier statique, adapté si la configuration réseau n'est pas gérée par un démon DNS).
3. Contrôle de la résolution via le DNS interne :
   `dig +short <nom_hote>.<nom_du_domaine> @<ip_dns_primaire>`
   👉 Explication : Interroge directement le serveur DNS interne et affiche l'adresse IP enregistrée.

---

## 🔒 3. Production — Façon Sécurisée (Ordre de résolution & Contrôle)
1. Vérification de l'ordre de résolution NSS :
   `grep '^hosts:' /etc/nsswitch.conf`
   👉 Explication : La ligne attendue est `hosts: files dns`, ce qui impose la lecture de `/etc/hosts` avant toute requête DNS et limite les détournements par un DNS externe.
2. Contrôle de l'état du fichier de résolveur :
   `ls -l /etc/resolv.conf`
   👉 Explication : Vérifie qu'il s'agit d'un fichier attendu (fichier statique ou lien vers le résolveur systemd) et qu'il n'a pas été remplacé silencieusement par un DHCP.
3. Contrôle de la résolution inverse depuis le DNS interne :
   `dig -x <adresse_ip_du_serveur> +short @<ip_dns_primaire>`
   👉 Explication : Vérifie que le PTR correspond au FQDN attendu, condition de cohérence avec la fiche d'identité de la machine.