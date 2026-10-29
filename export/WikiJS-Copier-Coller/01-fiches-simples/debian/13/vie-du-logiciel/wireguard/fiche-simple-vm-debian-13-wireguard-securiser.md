# Fiche_Simple_-_VM_Debian_13_WireGuard_Securiser

- **Environnement** : VM Debian 13 dédiée à WireGuard natif
- **OS / Version** : Debian 13 Trixie; version des dépôts à vérifier sur l’hôte
- **Catégorie** : WireGuard natif / sécuriser

---

## Problème précis à résoudre

Limiter pairs et flux, protéger clés privées et port UDP.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler permissions du répertoire et des clés :
   ```bash
   sudo namei -l /etc/wireguard/wg0.conf
   sudo stat -c "%a %U:%G %n" /etc/wireguard/wg0.conf /etc/wireguard/server.key
   ```
   👉 Explication : Configuration et clés privées doivent être `600`, détenues par root.

2. Examiner le pare-feu existant avant d’ajouter une règle :
   ```bash
   sudo nft list ruleset
   ```
   👉 Explication : La règle doit respecter le gestionnaire déjà en place, l’interface et les sources prévues.

3. Si UFW est déjà le pare-feu actif et que le flux est approuvé, limiter le port d’écoute :
   ```bash
   sudo ufw allow from VPN_SOURCE_CIDR to any port VPN_UDP_PORT proto udp
   sudo ufw status numbered
   ```
   👉 Explication : remplacer VPN_SOURCE_CIDR et VPN_UDP_PORT par les valeurs validées; ne pas activer UFW ni superposer un gestionnaire de pare-feu.

4. Vérifier que wg-quick peut lire la configuration :
   ```bash
   sudo wg-quick strip wg0 >/dev/null
   ```
   👉 Explication : La sortie est supprimée pour ne pas afficher la clé privée; corriger toute erreur et publier seulement les réseaux nécessaires pour chaque pair.

## 2. Production — Contrôles

Prévoir rotation/révocation rapide des pairs, sauvegarde sécurisée et accès administratif indépendant du VPN.

## 3. Production — Sécurité

- Ne jamais sauvegarder les clés privées dans un dépôt de code; transférer chaque clé par canal protégé.

## Validation et retour arrière

- **Validation** : Droits root-only confirmés, pairs restreints et seul le flux UDP approuvé prévu.
- **Retour arrière** : restaurer la configuration antérieure vérifiée et arrêter le service ou la capture si la recette échoue; consigner le changement.

## Si le problème n’est pas résolu

- [WireGuard natif — documentation officielle](https://www.wireguard.com/quickstart/)
- [Étape suivante du guide](/01-fiches-simples/debian/13/vie-du-logiciel/wireguard/fiche-simple-vm-debian-13-wireguard-valider)