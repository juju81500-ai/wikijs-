# Fiche_Simple_-_Windows_Client_11_WireGuard_Sauvegarder_Restaurer

- **Environnement** : Poste Windows 11 (client WireGuard)
- **OS / Version** : Windows 11; version du client à vérifier sur la page officielle
- **Catégorie** : WireGuard client / sauvegarder / restaurer

---

## Problème précis à résoudre

Conserver les paramètres du tunnel sans exposer la clé privée.

## 1. Hors-Production (Lab / Test / POC)

1. Noter les paramètres non secrets (adresse, endpoint, AllowedIPs, clé publique du serveur) dans le ticket.
   👉 Explication : Ne pas noter la clé privée.

2. Restauration : réinstaller le client et recréer un tunnel vide.
   👉 Explication : Une nouvelle paire de clés est générée : transmettre la nouvelle clé publique à l'administrateur, qui remplace l'ancienne.

## 2. Production — Contrôles

Pas d'archive de clé privée : la perte d'un poste se traite par régénération.

## 3. Production — Sécurité

- Aucun export de clé privée dans un cloud personnel.

## Validation et retour arrière

- **Validation** : Un tunnel recréé se connecte après remplacement du pair côté serveur.
- **Retour arrière** : Supprimer le tunnel recréé si la connexion échoue.

## Si le problème n'est pas résolu

- [Étape suivante du guide](/01-fiches-simples/windows/client-11/vie-du-logiciel/wireguard/fiche-simple-windows-client-11-wireguard-mise-a-jour-retour-arriere)
- [Fiche d'entrée du logiciel](/01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-wireguard)
- [WireGuard — installation officielle](https://www.wireguard.com/install/)
- [WireGuard pour Windows — documentation](https://git.zx2c4.com/wireguard-windows/about/)