# Fiche_Simple_-_VM_Debian_13_WireGuard_Valider

- **Environnement** : VM Debian 13 dédiée à WireGuard natif
- **OS / Version** : Debian 13 Trixie; version des dépôts à vérifier sur l’hôte
- **Catégorie** : WireGuard natif / valider

---

## Problème précis à résoudre

Démarrer un tunnel WireGuard natif et vérifier le pair pilote.

## 1. Hors-Production (Lab / Test / POC)

1. Valider la configuration transformée et le modèle systemd :
   ```bash
   sudo wg-quick strip wg0 >/dev/null
   systemctl list-unit-files | grep wg-quick
   ```
   👉 Explication : La sortie est supprimée pour ne pas afficher la clé privée; corriger toute erreur avant démarrage et confirmer le modèle systemd installé.

2. Après approbation, activer wg0 :
   ```bash
   sudo systemctl enable --now wg-quick@wg0
   systemctl status wg-quick@wg0 --no-pager
   sudo wg show wg0
   ip -br address show wg0
   ```
   👉 Explication : L’interface porte l’adresse prévue; vérifier qu’aucun pair non approuvé n’apparaît.

3. Depuis le client pilote autorisé, vérifier la poignée de main et les routes :
   ```bash
   sudo wg show wg0
   ip route
   ```
   👉 Explication : Tester uniquement une adresse ou ressource approuvée.

## 2. Production — Contrôles

Consigner handshake récent, routes, absence d’accès inattendu et résultats du client pilote.

## 3. Production — Sécurité

- Ne pas tester des réseaux distants hors périmètre approuvé.

## Validation et retour arrière

- **Validation** : Un pair pilote échange, la route prévue fonctionne, les journaux ne signalent pas d’erreur.
- **Retour arrière** : restaurer la configuration antérieure vérifiée et arrêter le service ou la capture si la recette échoue; consigner le changement.

## Si le problème n’est pas résolu

- [WireGuard natif — documentation officielle](https://www.wireguard.com/quickstart/)
- [Étape suivante du guide](/01-fiches-simples/debian/13/vie-du-logiciel/wireguard/fiche-simple-vm-debian-13-wireguard-sauvegarder-restaurer)