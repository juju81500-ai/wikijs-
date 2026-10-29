# Fiche_Simple_-_VM_Rocky_9_OpenVPN_Mise_A_Jour_Retour_Arriere

- **Environnement** : VM Rocky Linux 9 dédiée à OpenVPN Community Edition (serveur)
- **OS / Version** : Rocky Linux 9; paquets openvpn et easy-rsa issus d'EPEL, version à vérifier
- **Catégorie** : OpenVPN Community Edition / mise à jour / retour arrière
- **Tags** : `openvpn`, `rocky9`, `vie-du-logiciel`, `mise-a-jour-retour-arriere`

---

## Problème précis à résoudre

Mettre à jour OpenVPN en gardant un retour arrière.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder puis noter la version actuelle :
   ```bash
   openvpn --version | head -n 1
   sudo install -d -m 0700 /var/backups/openvpn
   sudo tar czf /var/backups/openvpn/avant-maj-$(date +%F).tar.gz -C / etc/openvpn
   ```
   👉 Explication : La version de référence sert au retour arrière.

2. Mettre à jour :
   ```bash
   sudo dnf check-update openvpn easy-rsa
   sudo dnf upgrade openvpn easy-rsa
   openvpn --version
   ```
   👉 Explication : Ne mettre à jour que ces paquets, après sauvegarde; relire les notes de version avant la fenêtre.

3. Redémarrer et rejouer la recette :
   ```bash
   sudo systemctl restart openvpn-server@server
   systemctl status openvpn-server@server --no-pager
   ```
   👉 Explication : Rejouer la fiche de validation avec le client pilote.

4. Retour arrière si la recette échoue :
   ```bash
   dnf history list | head -n 5
   sudo dnf history undo TRANSACTION_ID
   ```
   👉 Explication : TRANSACTION_ID est l'identifiant de la transaction de mise à jour affiché par dnf history (à remplacer); sinon restaurer la VM/snapshot.

## 2. Production — Contrôles

Planifier la mise à jour hors pics et prévenir les utilisateurs; prendre un snapshot de la VM avant.

## 3. Production — Sécurité

- Ne mettre à jour qu'à partir de dépôts approuvés; lire les avis de sécurité de l'éditeur.

## Validation et retour arrière

- **Validation** : Service actif, version attendue, client pilote connecté.
- **Retour arrière** : Réinstaller la version précédente et restaurer l'archive avant-maj-DATE.tar.gz (DATE à remplacer), ou restaurer le snapshot.

## Si le problème n'est pas résolu

- [Première étape du guide](./Fiche_Simple_-_VM_Rocky_9_OpenVPN_Prerequis_Limites.md)
- [Fiche d'entrée du logiciel](../../../../Logiciels/04-Reseau-et-cybersecurite/Fiche_Logiciel_-_OpenVPN.md)
- [OpenVPN Community — documentation officielle](https://openvpn.net/community-resources/)
- [OpenVPN — manuel de référence 2.6](https://openvpn.net/community-resources/reference-manual-for-openvpn-2-6/)
