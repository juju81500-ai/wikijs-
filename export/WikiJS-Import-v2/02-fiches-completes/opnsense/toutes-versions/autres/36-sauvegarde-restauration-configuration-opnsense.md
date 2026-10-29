---
title: "Sauvegarder et restaurer la configuration OPNsense"
description: "Fiche simple : [préparer l'accès et le périmètre](../../../../01-Fiches-Simples/OPNsense/Toutes-versions/Vie-du-systeme/Fiches-par-theme/Sauvegarde-restauration/FicheSimple-VMOPNsenseConfigPreparer.md)."
published: true
date: 2026-10-29T20:14:10Z
tags: ["opnsense", "sauvegarde", "restauration", "configuration", "ha", "reprise"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Sauvegarder et restaurer la configuration OPNsense

- **Type de fiche** : Autres — sauvegarde / reprise
- **Environnement** : Appliance OPNsense physique ou virtuelle, seule ou en HA
- **OS / Version** : OPNsense Community ou Business Edition maintenue
- **Rôle** : Protéger la configuration et restaurer le pare-feu après erreur ou remplacement
- **Tags** : `opnsense`, `sauvegarde`, `restauration`, `configuration`, `ha`, `reprise`

## 1. Préparer l'accès et le périmètre

Fiche simple : [préparer l'accès et le périmètre](/01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/fiches-par-theme/sauvegarde-restauration/fiche-simple-vm-opnsense-config-preparer).

Inventorier interfaces, VLAN, règles, NAT, certificats, VPN, comptes, secrets, plugins et rôle CARP. Conserver un accès console et noter l'ordre des interfaces matérielles. Les identifiants, clés privées, PSK et certificats contenus dans la configuration doivent être traités comme des secrets.

En HA, la synchronisation entre nœuds ne remplace pas une copie indépendante. Prévoir un export par appliance et documenter l'état MASTER/BACKUP, les adresses propres et les VIP.

## 2. Exporter une sauvegarde chiffrée

Fiche simple : [exporter une sauvegarde chiffrée](/01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/fiches-par-theme/sauvegarde-restauration/fiche-simple-vm-opnsense-config-exporter).

Dans **System > Configuration > Backups**, créer et télécharger un export complet, protégé par un mot de passe fort et unique. Stocker le fichier et le mot de passe séparément, dans un coffre sécurisé. Définir une fréquence après chaque changement majeur et un historique conforme aux besoins d'audit.

Pour automatiser les exports, utiliser une méthode officielle sécurisée (SFTP ou intégration approuvée), vérifier l'authenticité du serveur distant et appliquer une rétention. Ne pas exposer l'interface Web sur Internet pour automatiser la sauvegarde.

## 3. Vérifier la sauvegarde

Fiche simple : [vérifier la sauvegarde](/01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/fiches-par-theme/sauvegarde-restauration/fiche-simple-vm-opnsense-config-verifier).

- Vérifier date, taille, version source et appareil concerné.
- Confirmer que l'export est lisible et que le mot de passe est conservé dans le coffre.
- Copier la sauvegarde hors de l'appliance et hors de son stockage local.
- Tester périodiquement la restauration sur une VM ou appliance isolée de même version.

Un snapshot ZFS peut accélérer un retour arrière local sur une installation compatible, mais ne remplace ni l'export de configuration hors appliance, ni la sauvegarde des données externes.

## 4. Restaurer

Fiche simple : [restaurer](/01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/fiches-par-theme/sauvegarde-restauration/fiche-simple-vm-opnsense-config-restaurer).

1. Vérifier le modèle de matériel, les interfaces et la version cible; installer une release compatible.
2. Restaurer l'export complet depuis **System > Configuration > Backups** ou la console selon la procédure OPNsense.
3. Sur du matériel différent, conserver l'accès console : les noms d'interface peuvent nécessiter une réaffectation manuelle.
4. Redémarrer si la procédure le demande, puis valider WAN/LAN, règles, DNS, VPN, certificats et administration avant reconnexion au réseau.

Privilégier la restauration complète. Les restaurations partielles peuvent créer des incohérences entre composants dépendants.

## 5. Recette et clôture

Fiche simple : [recette et clôture](/01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/fiches-par-theme/sauvegarde-restauration/fiche-simple-vm-opnsense-config-recette).

Tester clients, routage, DHCP/DNS, NAT, VPN et règles de blocage/autorisation. En HA, rétablir la synchronisation seulement après avoir confirmé les rôles et les adresses propres des deux nœuds. Consigner version, sauvegarde, résultat du test et prochaines échéances.

## Sources

- [OPNsense — Sauvegardes de configuration](https://docs.opnsense.org/manual/backups.html)
- [OPNsense — Sauvegarde via SFTP](https://docs.opnsense.org/manual/sftp-backup.html)
- [OPNsense — Snapshots système](https://docs.opnsense.org/manual/snapshots.html)