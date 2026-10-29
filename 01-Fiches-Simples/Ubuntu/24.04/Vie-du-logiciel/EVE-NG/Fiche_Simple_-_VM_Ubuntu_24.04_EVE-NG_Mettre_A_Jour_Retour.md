# Fiche_Simple_-_VM_Ubuntu_24.04_EVE-NG_Mettre_A_Jour_Retour

- **Environnement** : VM EVE-NG (appliance basée sur Ubuntu Server 24.04 LTS) hébergée sur un poste ou serveur de virtualisation
- **OS / Version** : EVE-NG 7.x (7.2.0-18 au contrôle du 29/10/2026), Ubuntu 24.04 LTS embarqué; Community 6.2.0-4 (Ubuntu 22.04) en fin de support juin 2026
- **Catégorie** : simulation réseau / mise à jour
- **Tags** : `ubuntu24.04`, `eve-ng`, `mise-a-jour`, `snapshot`, `retour-arriere`, `upgrade`

---

## Problème précis à résoudre

Mettre à jour EVE-NG 7.x avec un point de retour, et planifier la migration depuis 6.x/Community en fin de support.

## 1. Hors-Production (Lab / Test / POC)

1. Arrêter tous les nœuds : **System > Stop All Nodes**, puis faire une sauvegarde (fiche Sauvegarder et restaurer).
   👉 Explication : toutes les sources officielles exigent des nœuds arrêtés avant la mise à jour.

2. Prendre un instantané de la VM dans l'hyperviseur (VMware Workstation : **VM > Snapshot > Take Snapshot**, nom `AVANT-MAJ-EVE`).
   👉 Explication : l'éditeur recommande un instantané comme filet de sécurité; c'est le seul retour arrière documenté (aucun downgrade officiel n'a été trouvé).

3. Se connecter en SSH (idéalement dans `screen` ou `tmux`) et contrôler la place et le DNS :
   ```bash
   screen -S eve-maj
   df -h
   apt autoremove
   ping -c 3 www.eve-ng.net
   ```
   👉 Explication : le disque racine et `/boot` ne doivent pas être pleins.

4. Lancer la mise à jour documentée :
   ```bash
   apt update
   apt -y dist-upgrade
   ```
   👉 Explication : séquence indiquée par la page officielle de mise à jour; ⚠️ NE PAS accepter une montée de version d'Ubuntu proposée par le système. En cas de questions, la doc indique « N » et « Keep the local version currently installed » pour GRUB.

5. Redémarrer puis vider le cache du navigateur :
   ```bash
   reboot
   ```
   👉 Explication : la doc officielle demande de vider cache, cookies et historique après redémarrage.

6. Migration 6.x vers 7.x : utiliser uniquement le paquet `.run` officiel « EVE-NG 7 Upgrade Assistant » depuis la page Download, après sauvegarde et instantané; l'assistant migre Ubuntu 22.04 vers 24.04. ⚠️ Cette procédure est documentée pour EVE-NG Pro; pour l'édition Community 6.2.0-4 (fin de support), aucune migration publique n'a été confirmée : prévoir une nouvelle installation 7.x et une restauration.
   👉 Explication : le nom exact du paquet évolue avec la version (7.2.0-18 au 29/10/2026).

## 2. Production — Contrôles

- Réserver une fenêtre de maintenance et informer les utilisateurs.
- Après redémarrage, vérifier la licence, l'ouverture des labs et le démarrage des nœuds.
- Garder l'instantané jusqu'à validation complète, puis le supprimer pour libérer l'espace.

## 3. Production — Sécurité

- Télécharger les mises à jour uniquement depuis le site officiel eve-ng.net et contrôler les empreintes publiées.
- Ne jamais lancer la mise à jour depuis la console HTML5 Desktop.
- Ne pas exécuter de script d'un forum pour contourner une erreur de mise à jour.

## Validation et retour arrière

- **Validation** : `dpkg -l eve-ng-pro` affiche la nouvelle version, l'interface web s'ouvre et un lab de test démarre.
- **Retour arrière** : arrêter la VM puis restaurer l'instantané `AVANT-MAJ-EVE` (VMware Workstation : **VM > Snapshot > Revert**).

## Si le problème n'est pas résolu

- [EVE-NG — mise à jour Pro/LC](https://www.eve-ng.net/index.php/1845-2/)
- [EVE-NG — migration v6 vers v7](https://www.eve-ng.net/index.php/1845-2/eve-pro-upgrade-from-v6-x-to-v7-x/)
- [EVE-NG — notes de version](https://www.eve-ng.net/index.php/documentation/release-notes/)
[EVE-NG — documentation officielle](https://www.eve-ng.net/index.php/documentation/)
- [Fiche logiciel EVE-NG](../../../../Logiciels/15-Topologie-IPAM-et-outils-metiers/Fiche_Logiciel_-_EVE-NG.md)
- [Sauvegarder et restaurer](./Fiche_Simple_-_VM_Ubuntu_24.04_EVE-NG_Sauvegarder_Restaurer.md)
