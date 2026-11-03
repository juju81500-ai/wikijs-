# Fiche_Simple_-_VM_Debian_13_ISC-DHCP-Server_Sauvegarder_Restaurer

- **Environnement** : VM Debian 13; ISC DHCP déprécié, usage transitoire
- **OS / Version** : Debian 13
- **Catégorie** : Vie du logiciel / ISC-DHCP-Server — Sauvegarder / restaurer
- **Tags** : `isc-dhcp`, `serveur`, `vie-du-logiciel`, `sauvegarder_restaurer`

---

## Problème précis à résoudre

Sauvegarder configuration et baux avant transition Kea.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder / restaurer :
   ```bash
   sudo systemctl stop isc-dhcp-server
sudo tar --xattrs -czf /root/isc-dhcp-DATE.tgz /etc/dhcp /var/lib/dhcp
sudo chmod 600 /root/isc-dhcp-DATE.tgz
   ```
   👉 Explication : Remplacer DATE; service arrêté pour cohérence, archive chiffrée hors hôte.


## 2. Production — Contrôles

La config ISC ne se restaure pas directement sous Kea; convertir et tester selon la doc Kea.

## 3. Production — Sécurité

Protéger archives révélant inventaire réseau.

## Validation et retour arrière

- **Validation** : Restauration isolée passe dhcpd -t et un test client.
- **Retour arrière** : Ne jamais lancer ISC et Kea simultanément sur un même segment.

## Si le problème n'est pas résolu

- [Prérequis et limites](fiche-simple-vm-debian-13-isc-dhcp-server-prerequis-limites.md)
- [Installer](fiche-simple-vm-debian-13-isc-dhcp-server-installer.md)
- [Configurer](fiche-simple-vm-debian-13-isc-dhcp-server-configurer.md)
- [Sécuriser](fiche-simple-vm-debian-13-isc-dhcp-server-securiser.md)
- [Valider (recette)](fiche-simple-vm-debian-13-isc-dhcp-server-valider.md)
- [Mise à jour et retour arrière](fiche-simple-vm-debian-13-isc-dhcp-server-mise-a-jour-retour-arriere.md)
- [Documentation officielle](https://www.isc.org/blogs/isc-dhcp-eol/)
