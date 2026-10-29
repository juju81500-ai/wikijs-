# Fiche_Simple_-_VM_Ubuntu_24.04_WireGuard_Mise_A_Jour_Retour_Arriere

- **Environnement** : VM Ubuntu 24.04 dédiée à un serveur WireGuard natif
- **OS / Version** : Ubuntu 24.04 LTS Noble; noyau avec module WireGuard et paquet wireguard, versions à vérifier
- **Catégorie** : WireGuard natif / mise à jour / retour arrière
- **Tags** : `wireguard`, `ubuntu24-04`, `vie-du-logiciel`, `mise-a-jour-retour-arriere`

---

## Problème précis à résoudre

Mettre à jour WireGuard en gardant un retour arrière.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder et noter la version :
   ```bash
   wg --version
   sudo install -d -m 0700 /var/backups/wireguard
   sudo tar czf /var/backups/wireguard/avant-maj-$(date +%F).tar.gz -C / etc/wireguard
   ```
   👉 Explication : La version et l'archive servent au retour arrière.

2. Mettre à jour les outils :
   ```bash
   sudo apt update
   sudo apt install --only-upgrade wireguard wireguard-tools
   wg --version
   ```
   👉 Explication : Un nouveau noyau demande un redémarrage planifié.

3. Rejouer la recette : voir la fiche de validation.
   ```bash
   sudo systemctl restart wg-quick@wg0
   sudo wg show
   ```
   👉 Explication : Vérifier le handshake du pair pilote.

4. Retour arrière si la recette échoue :
   ```bash
   apt-cache policy wireguard-tools
   sudo apt install wireguard-tools=VERSION_PRECEDENTE
   ```
   👉 Explication : VERSION_PRECEDENTE (ou TRANSACTION_ID) est la version ou la transaction notée avant la mise à jour (à remplacer); sinon restaurer le snapshot.

## 2. Production — Contrôles

Prévenir les utilisateurs et prendre un snapshot.

## 3. Production — Sécurité

- Dépôts approuvés uniquement.

## Validation et retour arrière

- **Validation** : Tunnel actif, version attendue.
- **Retour arrière** : Réinstaller la version précédente et restaurer avant-maj-DATE.tar.gz (DATE à remplacer).

## Si le problème n'est pas résolu

- [Première étape du guide](./Fiche_Simple_-_VM_Ubuntu_24.04_WireGuard_Prerequis_Limites.md)
- [Fiche d'entrée du logiciel](../../../../Logiciels/04-Reseau-et-cybersecurite/Fiche_Logiciel_-_WireGuard.md)
- [WireGuard — installation officielle](https://www.wireguard.com/install/)
- [WireGuard — démarrage rapide](https://www.wireguard.com/quickstart/)
