# Fiche_Simple_-_VM_Ubuntu_24.04_WireGuard_Valider

- **Environnement** : VM Ubuntu 24.04 dédiée à un serveur WireGuard natif
- **OS / Version** : Ubuntu 24.04 LTS Noble; noyau avec module WireGuard et paquet wireguard, versions à vérifier
- **Catégorie** : WireGuard natif / valider

---

## Problème précis à résoudre

Recetter le tunnel avec un pair pilote.

## 1. Hors-Production (Lab / Test / POC)

1. Démarrer l'interface :
   ```bash
   sudo systemctl enable --now wg-quick@wg0
   systemctl status wg-quick@wg0 --no-pager
   ```
   👉 Explication : wg0 est le nom du fichier de configuration (à adapter).

2. Contrôler l'état du tunnel :
   ```bash
   sudo wg show
   sudo ss -ulnp | grep VPN_UDP_PORT
   ```
   👉 Explication : Après connexion du pair pilote, wg show doit indiquer un latest handshake récent et des compteurs transfer.

3. Tester une ressource autorisée depuis le pair :
   ```bash
   ping -c 3 ADRESSE_AUTORISEE
   ```
   👉 Explication : ADRESSE_AUTORISEE est une IP de test autorisée (à remplacer); vérifier qu'une destination non autorisée reste inaccessible.

## 2. Production — Contrôles

Consigner l'heure et le résultat de la recette.

## 3. Production — Sécurité

- Supprimer le pair pilote s'il est temporaire.

## Validation et retour arrière

- **Validation** : Handshake récent et trafic conforme aux AllowedIPs.
- **Retour arrière** : sudo systemctl disable --now wg-quick@wg0.

## Si le problème n'est pas résolu

- [Étape suivante du guide](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/wireguard/fiche-simple-vm-ubuntu-24-04-wireguard-sauvegarder-restaurer)
- [Fiche d'entrée du logiciel](/01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-wireguard)
- [WireGuard — installation officielle](https://www.wireguard.com/install/)
- [WireGuard — démarrage rapide](https://www.wireguard.com/quickstart/)