# Fiche_Simple_-_VM_Ubuntu_24.04_WireGuard_Installer

- **Environnement** : VM Ubuntu 24.04 dédiée à un serveur WireGuard natif
- **OS / Version** : Ubuntu 24.04 LTS Noble; noyau avec module WireGuard et paquet wireguard, versions à vérifier
- **Catégorie** : WireGuard natif / installer

---

## Problème précis à résoudre

Installer WireGuard natif sans activer d'interface non configurée.

## 1. Hors-Production (Lab / Test / POC)

1. Installer les outils :
   ```bash
   sudo apt update
   apt-cache policy wireguard wireguard-tools
   sudo apt install wireguard
   wg --version
   ```
   👉 Explication : Le paquet wireguard installe wireguard-tools (commandes wg et wg-quick); le module est fourni par le noyau Ubuntu. Consigner les versions.

2. Contrôler les unités fournies :
   ```bash
   systemctl list-unit-files | grep -i wg-quick
   ```
   👉 Explication : Le modèle wg-quick@.service (NOM_INTERFACE = nom de wg0.conf) pilote chaque interface; vérifier le nom sur l'hôte.

## 2. Production — Contrôles

Consigner versions et origine des paquets.

## 3. Production — Sécurité

- Ne pas activer d'interface ni ouvrir de port avant validation de la configuration.

## Validation et retour arrière

- **Validation** : wg --version répond.
- **Retour arrière** : Désinstaller : sudo apt remove wireguard (aucune configuration créée).

## Si le problème n'est pas résolu

- [Étape suivante du guide](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/wireguard/fiche-simple-vm-ubuntu-24-04-wireguard-configurer)
- [Fiche d'entrée du logiciel](/01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-wireguard)
- [WireGuard — installation officielle](https://www.wireguard.com/install/)
- [WireGuard — démarrage rapide](https://www.wireguard.com/quickstart/)