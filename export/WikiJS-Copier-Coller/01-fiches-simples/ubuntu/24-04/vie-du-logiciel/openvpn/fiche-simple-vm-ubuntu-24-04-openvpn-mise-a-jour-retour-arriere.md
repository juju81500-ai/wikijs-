# Fiche_Simple_-_VM_Ubuntu_24.04_OpenVPN_Mise_A_Jour_Retour_Arriere

- **Environnement** : VM Ubuntu 24.04 dédiée à OpenVPN Community Edition (serveur)
- **OS / Version** : Ubuntu 24.04 LTS Noble; version des dépôts à vérifier sur l'hôte
- **Catégorie** : OpenVPN Community Edition / mise à jour / retour arrière

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
   sudo apt update
   apt list --upgradable 2>/dev/null | grep -E 'openvpn|easy-rsa'
   sudo apt install --only-upgrade openvpn easy-rsa
   openvpn --version
   ```
   👉 Explication : Ne mettre à jour que ces paquets, après sauvegarde; relire les notes de version du paquet avant la fenêtre.

3. Redémarrer et rejouer la recette :
   ```bash
   sudo systemctl restart openvpn-server@server
   systemctl status openvpn-server@server --no-pager
   ```
   👉 Explication : Rejouer la fiche de validation avec le client pilote.

4. Retour arrière si la recette échoue :
   ```bash
   apt-cache policy openvpn
   sudo apt install openvpn=VERSION_PRECEDENTE
   ```
   👉 Explication : VERSION_PRECEDENTE est la version précédemment installée (à remplacer, relevée avant la mise à jour); elle doit encore être disponible dans un dépôt approuvé, sinon restaurer la VM/snapshot.

## 2. Production — Contrôles

Planifier la mise à jour hors pics et prévenir les utilisateurs; prendre un snapshot de la VM avant.

## 3. Production — Sécurité

- Ne mettre à jour qu'à partir de dépôts approuvés; lire les avis de sécurité de l'éditeur.

## Validation et retour arrière

- **Validation** : Service actif, version attendue, client pilote connecté.
- **Retour arrière** : Réinstaller la version précédente et restaurer l'archive avant-maj-DATE.tar.gz (DATE à remplacer), ou restaurer le snapshot.

## Si le problème n'est pas résolu

- [Première étape du guide](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/openvpn/fiche-simple-vm-ubuntu-24-04-openvpn-prerequis-limites)
- [Fiche d'entrée du logiciel](/01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-openvpn)
- [OpenVPN Community — documentation officielle](https://openvpn.net/community-resources/)
- [OpenVPN — manuel de référence 2.6](https://openvpn.net/community-resources/reference-manual-for-openvpn-2-6/)