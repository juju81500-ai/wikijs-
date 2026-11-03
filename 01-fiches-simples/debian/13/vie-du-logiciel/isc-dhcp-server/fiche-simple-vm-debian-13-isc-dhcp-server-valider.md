# Fiche_Simple_-_VM_Debian_13_ISC-DHCP-Server_Valider

- **Environnement** : [[Glossary:VM]] Debian 13; ISC [[Glossary:DHCP]] déprécié, usage transitoire
- **OS / Version** : Debian 13
- **Catégorie** : Vie du logiciel / ISC-DHCP-Server — Valider (recette)
- **Tags** : `isc-dhcp`, `serveur`, `vie-du-logiciel`, `valider`

---

## Problème précis à résoudre

Tester syntaxe, service et bail dans un réseau isolé.

## 1. Hors-Production (Lab / Test / POC)

1. Valider (recette) :
   ```bash
   sudo dhcpd -t -cf /etc/dhcp/dhcpd.conf
sudo systemctl restart isc-dhcp-server
systemctl is-active isc-dhcp-server
sudo journalctl -u isc-dhcp-server -n 60 --no-pager
sudo tail -n 30 /var/lib/dhcp/dhcpd.leases
   ```
   👉 Explication : Redémarrer uniquement dans [[Glossary:VLAN]] test; les baux sont des données réseau à protéger.


## 2. Production — Contrôles

Valider DISCOVER/OFFER/REQUEST/ACK et absence d’un serveur concurrent.

## 3. Production — Sécurité

Pas de test de saturation/usurpation; recette contrôlée.

## Validation et retour arrière

- **Validation** : Client reçoit l’adresse prévue et logs confirment le bail.
- **Retour arrière** : Arrêter en cas d’offre inattendue et restaurer état validé.

## Si le problème n'est pas résolu

- [Prérequis et limites](fiche-simple-vm-debian-13-isc-dhcp-server-prerequis-limites.md)
- [Installer](fiche-simple-vm-debian-13-isc-dhcp-server-installer.md)
- [Configurer](fiche-simple-vm-debian-13-isc-dhcp-server-configurer.md)
- [Sécuriser](fiche-simple-vm-debian-13-isc-dhcp-server-securiser.md)
- [Sauvegarder / restaurer](fiche-simple-vm-debian-13-isc-dhcp-server-sauvegarder-restaurer.md)
- [Mise à jour et retour arrière](fiche-simple-vm-debian-13-isc-dhcp-server-mise-a-jour-retour-arriere.md)
- [Documentation officielle](https://www.isc.org/blogs/isc-dhcp-eol/)
