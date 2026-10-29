# Fiche_Simple_-_Windows_Client_11_WireGuard_Sauvegarder_Restaurer

- **Environnement** : Poste Windows 11 (client WireGuard)
- **OS / Version** : Windows 11; version du client à vérifier sur la page officielle
- **Catégorie** : WireGuard client / sauvegarder / restaurer
- **Tags** : `wireguard`, `windows11`, `vie-du-logiciel`, `sauvegarder-restaurer`

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

- [Étape suivante du guide](./Fiche_Simple_-_Windows_Client_11_WireGuard_Mise_A_Jour_Retour_Arriere.md)
- [Fiche d'entrée du logiciel](../../../../Logiciels/04-Reseau-et-cybersecurite/Fiche_Logiciel_-_WireGuard.md)
- [WireGuard — installation officielle](https://www.wireguard.com/install/)
- [WireGuard pour Windows — documentation](https://git.zx2c4.com/wireguard-windows/about/)
