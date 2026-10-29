# Fiche_Simple_-_Windows_Client_11_WireGuard_Valider

- **Environnement** : Poste Windows 11 (client WireGuard)
- **OS / Version** : Windows 11; version du client à vérifier sur la page officielle
- **Catégorie** : WireGuard client / valider
- **Tags** : `wireguard`, `windows11`, `vie-du-logiciel`, `valider`

---

## Problème précis à résoudre

Vérifier la connexion du tunnel.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : sélectionner le tunnel > Activer.
   👉 Explication : Le statut passe à Actif et la ligne Dernière poignée de main apparaît.

2. Contrôler l'interface et une ressource autorisée :
   ```powershell
   Get-NetAdapter | Where-Object { $_.InterfaceDescription -match 'WireGuard' }
   Test-NetConnection HOTE_INTERNE -Port PORT_INTERNE
   ```
   👉 Explication : HOTE_INTERNE et PORT_INTERNE désignent une ressource autorisée de test (à remplacer).

3. Désactiver le tunnel puis vérifier que la ressource n'est plus joignable.
   👉 Explication : Confirme que le trafic passait bien par le tunnel.

## 2. Production — Contrôles

Consigner le résultat.

## 3. Production — Sécurité

- Désactiver le tunnel après les tests si non nécessaire.

## Validation et retour arrière

- **Validation** : Poignée de main récente et ressource atteinte uniquement via le tunnel.
- **Retour arrière** : Désactiver et supprimer le tunnel.

## Si le problème n'est pas résolu

- [Étape suivante du guide](./Fiche_Simple_-_Windows_Client_11_WireGuard_Sauvegarder_Restaurer.md)
- [Fiche d'entrée du logiciel](../../../../Logiciels/04-Reseau-et-cybersecurite/Fiche_Logiciel_-_WireGuard.md)
- [WireGuard — installation officielle](https://www.wireguard.com/install/)
- [WireGuard pour Windows — documentation](https://git.zx2c4.com/wireguard-windows/about/)
