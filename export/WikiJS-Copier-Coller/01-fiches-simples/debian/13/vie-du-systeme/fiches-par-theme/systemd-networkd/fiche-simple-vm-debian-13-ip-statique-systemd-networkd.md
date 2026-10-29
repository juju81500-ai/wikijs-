# 📄 VM_Debian_13_Reseau_Fixer-IP-Systemd-Networkd.md

- **Environnement** : VM (Proxmox VE 8+ / KVM / Hyper-V)
- **OS / Version** : Debian 13 (Trixie) - Famille Debian
- **Catégorie** : Réseau / Configuration IP

## 🎯 Problème précis à résoudre
Configurer une adresse IP statique permanente, les serveurs DNS et la passerelle par défaut sur Debian 13 (Trixie) en utilisant le moteur natif `systemd-networkd` et `systemd-resolved`, tout en désactivant la configuration automatique via DHCP et IPv6 Router Advertisement.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Affichage des interfaces réseau disponibles :
   `ip link show`
   👉 Explication : Identifie le nom exact de la carte réseau (ex: `eth0` ou `enp0s3`).

2. Attribution manuelle et volatile de l'IP :
   `ip addr add 192.168.1.130/24 dev eth0`
   👉 Explication : Assigne l'IP 192.168.1.130/24 temporairement sur l'interface eth0 sans persistance au reboot.

3. Ajout de la passerelle par défaut temporaire :
   `ip route add default via 192.168.1.1 dev eth0`
   👉 Explication : Définit la route de sortie par défaut pour la connectivité hors du sous-réseau local.

4. Test de connectivité IP immédiat :
   `ping -c 3 192.168.1.1`
   👉 Explication : Envoie 3 paquets ICMP pour vérifier la joignabilité de la passerelle.

---

## ⚡ 2. Production — Façon Simplifiée
1. Activation des services réseau systemd natifs :
   `systemctl enable --now systemd-networkd systemd-resolved`
   👉 Explication : Démarre et active les démons modernes d'administration réseau et de résolution DNS de systemd.

2. Création du fichier de configuration réseau `/etc/systemd/network/10-eth0-static.network` :
   [Match]
   Name=eth0

   [Network]
   Address=192.168.1.130/24
   Gateway=192.168.1.1
   DNS=192.168.1.1 1.1.1.1
   👉 Explication : Définit l'adresse IP statique, le masque, la passerelle et les serveurs DNS de secours pour l'interface eth0.

3. Rechargement de la configuration réseau systemd :
   `networkctl reload`
   👉 Explication : Applique immédiatement les paramètres réseau du fichier `.network` sans interrompre l'ensemble du système.

4. Création du lien symbolique pour le gestionnaire DNS `systemd-resolved` :
   `ln -sf /run/systemd/resolve/stub-resolv.conf /etc/resolv.conf`
   👉 Explication : Pointe la résolution DNS système globale vers le résolveur local stub sécurisé de systemd.

---

## 🔒 3. Production — Façon Sécurisée
1. Désactiver les annonces de routeur IPv6 uniquement si l'architecture n'utilise pas SLAAC/RA. Éditer l'unique section `[Network]` existante dans `/etc/systemd/network/10-eth0-static.network` :
   ```ini
   IPv6AcceptRA=no
   ```
   👉 Explication : Empêche l'interface d'apprendre une route par défaut via RA sans désactiver IPv6 ni casser automatiquement les adresses link-local. Ne pas ajouter une seconde section `[Network]`.

2. N'activer DNSSEC ou DNS-over-TLS que si les résolveurs configurés les prennent en charge et si la politique réseau l'exige. Sauvegarder `/etc/systemd/resolved.conf`, régler les options dans sa section `[Resolve]`, puis vérifier la résolution avant de fermer la session distante.
   👉 Explication : Les options strictes peuvent rendre la résolution indisponible si le DNS amont n'est pas compatible.

3. Vérifier la configuration et le gestionnaire qui possède `/etc/resolv.conf` :
   ```bash
   ls -l /etc/resolv.conf
   networkctl status eth0
   resolvectl status
   ```
   👉 Explication : `systemd-resolved` ou un autre gestionnaire peut recréer ce fichier. Ne pas appliquer `chattr +i` et ne pas remplacer le lien symbolique sans vérifier le propriétaire.

4. Appliquer et tester depuis une console ou une session de secours :
   ```bash
   sudo networkctl reload
   sudo networkctl reconfigure eth0
   ip route
   resolvectl query deb.debian.org
   ```
   👉 Explication : Vérifie l'adresse, la route et le DNS après le changement. Restaurer la sauvegarde si le test échoue.