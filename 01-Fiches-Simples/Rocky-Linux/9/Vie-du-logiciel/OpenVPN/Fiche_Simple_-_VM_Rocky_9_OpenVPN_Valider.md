# Fiche_Simple_-_VM_Rocky_9_OpenVPN_Valider

- **Environnement** : VM Rocky Linux 9 dédiée à OpenVPN Community Edition (serveur)
- **OS / Version** : Rocky Linux 9; paquets openvpn et easy-rsa issus d'EPEL, version à vérifier
- **Catégorie** : OpenVPN Community Edition / valider
- **Tags** : `openvpn`, `rocky9`, `vie-du-logiciel`, `valider`

---

## Problème précis à résoudre

Recetter le serveur avec un client pilote avant ouverture aux utilisateurs.

## 1. Hors-Production (Lab / Test / POC)

1. Démarrer l'instance et contrôler son état :
   ```bash
   sudo systemctl enable --now openvpn-server@server
   systemctl status openvpn-server@server --no-pager
   ip -br address show tun0
   ```
   👉 Explication : server est le nom du fichier server.conf (à adapter); l'interface tun0 doit exister (nom pouvant varier selon la configuration).

2. Vérifier l'écoute UDP :
   ```bash
   sudo ss -ulnp | grep openvpn
   ```
   👉 Explication : Le port VPN_UDP_PORT doit être à l'écoute.

3. Connecter un client pilote puis lire le journal :
   ```bash
   sudo journalctl -u openvpn-server@server -n 50 --no-pager
   ```
   👉 Explication : Confirmer la connexion TLS, l'authentification du certificat pilote et l'accès aux seules routes autorisées; tester aussi qu'un certificat révoqué est refusé.

## 2. Production — Contrôles

Consigner le résultat de la recette, l'heure et l'approbation du propriétaire du service.

## 3. Production — Sécurité

- Supprimer le client pilote et son certificat à la fin du test s'il n'est pas destiné à la production.

## Validation et retour arrière

- **Validation** : Client pilote connecté, routes conformes, certificat révoqué refusé.
- **Retour arrière** : sudo systemctl disable --now openvpn-server@server puis restaurer la configuration antérieure.

## Si le problème n'est pas résolu

- [Étape suivante du guide](./Fiche_Simple_-_VM_Rocky_9_OpenVPN_Sauvegarder_Restaurer.md)
- [Fiche d'entrée du logiciel](../../../../Logiciels/04-Reseau-et-cybersecurite/Fiche_Logiciel_-_OpenVPN.md)
- [OpenVPN Community — documentation officielle](https://openvpn.net/community-resources/)
- [OpenVPN — manuel de référence 2.6](https://openvpn.net/community-resources/reference-manual-for-openvpn-2-6/)
