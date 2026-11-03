# 📄 VM_Debian_12_Securite_Configuration-Fail2ban-SSH.md

- **Environnement** : VM (Proxmox VE / KVM)
- **OS / Version** : Debian 12 (Bookworm) - Famille Debian
- **Catégorie** : Sécurité & Prevention d'Intrusion
- **Tags** : `[debian12]`, `[debian-family]`, `[fail2ban]`, `[ssh]`, `[nftables]`, `[hardening]`

## 🎯 Problème précis à résoudre
Installer et configurer Fail2ban sur Debian 12 pour détecter et bannir automatiquement les adresses IP effectuant des attaques par force brute SSH via `nftables`.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation rapide du paquet Fail2ban :
   `apt-get update && apt-get install -y fail2ban`
   👉 Explication : Installe le service de surveillance des journaux système.
2. Démarrage et vérification de l'état du service :
   `systemctl status fail2ban`
   👉 Explication : Contrôle que le démon Fail2ban est actif.
3. Test manuel du bannissement d'une IP de test :
   `fail2ban-client set sshd banip 192.168.1.250`
   👉 Explication : Applique un bannissement immédiat de l'IP désignée pour valider le fonctionnement du moteur.

---

## ⚡ 2. Production — Façon Simplifiée
1. Création du fichier de configuration local `/etc/fail2ban/jail.local` :
   `cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local`
   👉 Explication : Copie la trame officielle pour créer le fichier de surcharge locale.
2. Activation du filtre SSH dans `/etc/fail2ban/jail.local` :
   `fail2ban-client reload`
   👉 Explication : Recharge la configuration pour surveiller le service SSH avec un temps de bannissement par défaut.

---

## 🔒 3. Production — Façon Sécurisée (Hardening Enterprise & Bannissement Récidiviste)
1. Exemption des IP d'administration internes (Whitelist) :
   `fail2ban-client status sshd`
   👉 Explication : Affiche l'état des prisons et s'assure que les adresses du réseau d'administration local sont exemptées de bannissement.
2. Bannissement renforcé et intégration native avec nftables :
   `systemctl restart fail2ban`
   👉 Explication : Redémarre Fail2ban pour injecter dynamiquement les règles de blocage d'IP dans le pare-feu kernel nftables.
3. Consultation des statistiques de blocage :
   `fail2ban-client status`
   👉 Explication : Permet à l'administrateur de surveiller en temps réel le nombre total d'IP bannies.