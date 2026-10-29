# Fiche_Simple_-_VM_Debian_13_ISC-DHCP-Server_Valider

- **Environnement** : VM Debian 13; ISC DHCP déprécié, usage transitoire
- **OS / Version** : Debian 13
- **Catégorie** : Vie du logiciel / ISC-DHCP-Server — Valider (recette)

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
   👉 Explication : Redémarrer uniquement dans VLAN test; les baux sont des données réseau à protéger.

## 2. Production — Contrôles

Valider DISCOVER/OFFER/REQUEST/ACK et absence d’un serveur concurrent.

## 3. Production — Sécurité

Pas de test de saturation/usurpation; recette contrôlée.

## Validation et retour arrière

- **Validation** : Client reçoit l’adresse prévue et logs confirment le bail.
- **Retour arrière** : Arrêter en cas d’offre inattendue et restaurer état validé.

## Si le problème n'est pas résolu

- [Prérequis et limites](/01-fiches-simples/debian/13/vie-du-logiciel/isc-dhcp-server/fiche-simple-vm-debian-13-isc-dhcp-server-prerequis-limites)
- [Installer](/01-fiches-simples/debian/13/vie-du-logiciel/isc-dhcp-server/fiche-simple-vm-debian-13-isc-dhcp-server-installer)
- [Configurer](/01-fiches-simples/debian/13/vie-du-logiciel/isc-dhcp-server/fiche-simple-vm-debian-13-isc-dhcp-server-configurer)
- [Sécuriser](/01-fiches-simples/debian/13/vie-du-logiciel/isc-dhcp-server/fiche-simple-vm-debian-13-isc-dhcp-server-securiser)
- [Sauvegarder / restaurer](/01-fiches-simples/debian/13/vie-du-logiciel/isc-dhcp-server/fiche-simple-vm-debian-13-isc-dhcp-server-sauvegarder-restaurer)
- [Mise à jour et retour arrière](/01-fiches-simples/debian/13/vie-du-logiciel/isc-dhcp-server/fiche-simple-vm-debian-13-isc-dhcp-server-mise-a-jour-retour-arriere)
- [Documentation officielle](https://www.isc.org/blogs/isc-dhcp-eol/)