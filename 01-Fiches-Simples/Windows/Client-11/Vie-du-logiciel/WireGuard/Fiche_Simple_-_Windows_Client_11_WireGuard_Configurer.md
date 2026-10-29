# Fiche_Simple_-_Windows_Client_11_WireGuard_Configurer

- **Environnement** : Poste Windows 11 (client WireGuard)
- **OS / Version** : Windows 11; version du client à vérifier sur la page officielle
- **Catégorie** : WireGuard client / configurer
- **Tags** : `wireguard`, `windows11`, `vie-du-logiciel`, `configurer`

---

## Problème précis à résoudre

Créer le tunnel client et transmettre sa clé publique.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : ouvrir WireGuard > Ajouter un tunnel > Ajouter un tunnel vide.
   👉 Explication : L'application génère la paire de clés; la clé privée reste dans l'application.

2. Compléter la configuration affichée :
   ```ini
   [Interface]
   PrivateKey = (générée par l'application, ne pas modifier)
   Address = CLIENT_VPN_ADDRESS/32

   [Peer]
   PublicKey = SERVER_PUBLIC_KEY
   Endpoint = SERVER_ENDPOINT:VPN_UDP_PORT
   AllowedIPs = ALLOWED_NETWORKS
   PersistentKeepalive = 25
   ```
   👉 Explication : Remplacer les valeurs en majuscules par celles de l'administrateur; limiter ALLOWED_NETWORKS aux réseaux approuvés (pas 0.0.0.0/0 sans accord). PersistentKeepalive n'est utile que derrière un NAT.

3. Copier uniquement la Clé publique affichée par l'application et la transmettre à l'administrateur par un canal approuvé.
   👉 Explication : L'administrateur l'ajoute comme pair (CLIENT_PUBLIC_KEY) sur le serveur.

## 2. Production — Contrôles

Faire relire AllowedIPs par l'administrateur.

## 3. Production — Sécurité

- La clé privée n'est jamais copiée, affichée en capture ni envoyée.

## Validation et retour arrière

- **Validation** : Tunnel créé et clé publique transmise.
- **Retour arrière** : GUI : sélectionner le tunnel > Supprimer.

## Si le problème n'est pas résolu

- [Étape suivante du guide](./Fiche_Simple_-_Windows_Client_11_WireGuard_Securiser.md)
- [Fiche d'entrée du logiciel](../../../../Logiciels/04-Reseau-et-cybersecurite/Fiche_Logiciel_-_WireGuard.md)
- [WireGuard — installation officielle](https://www.wireguard.com/install/)
- [WireGuard pour Windows — documentation](https://git.zx2c4.com/wireguard-windows/about/)
