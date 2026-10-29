# Fiche_Simple_-_VM_Debian_13_ISC-DHCP-Server_Prerequis_Limites

- **Environnement** : VM Debian 13; ISC DHCP déprécié, usage transitoire
- **OS / Version** : Debian 13
- **Catégorie** : Vie du logiciel / ISC-DHCP-Server — Prérequis et limites

---

## Problème précis à résoudre

Maintenir un ISC DHCP existant à titre transitoire et planifier Kea.

## 1. Hors-Production (Lab / Test / POC)

1. Prérequis et limites :
   ```bash
   apt-cache policy isc-dhcp-server
apt show isc-dhcp-server
ip -br addr
sudo dhcpd -t -cf /etc/dhcp/dhcpd.conf 2>&1 || true
   ```
   👉 Explication : Le paquet Trixie est deprecated; confirmer provenance et avis Debian. ISC DHCP est EOL upstream depuis 2022.

## 2. Production — Contrôles

Réserver à la maintenance existante; documenter date de migration Kea.

## 3. Production — Sécurité

Limiter l’écoute au VLAN autorisé et surveiller avis Debian.

## Validation et retour arrière

- **Validation** : Risque EOL, réseau et migration approuvés.
- **Retour arrière** : Aucun changement pendant l’inventaire.

## Si le problème n'est pas résolu

- [Installer](/01-fiches-simples/debian/13/vie-du-logiciel/isc-dhcp-server/fiche-simple-vm-debian-13-isc-dhcp-server-installer)
- [Configurer](/01-fiches-simples/debian/13/vie-du-logiciel/isc-dhcp-server/fiche-simple-vm-debian-13-isc-dhcp-server-configurer)
- [Sécuriser](/01-fiches-simples/debian/13/vie-du-logiciel/isc-dhcp-server/fiche-simple-vm-debian-13-isc-dhcp-server-securiser)
- [Valider (recette)](/01-fiches-simples/debian/13/vie-du-logiciel/isc-dhcp-server/fiche-simple-vm-debian-13-isc-dhcp-server-valider)
- [Sauvegarder / restaurer](/01-fiches-simples/debian/13/vie-du-logiciel/isc-dhcp-server/fiche-simple-vm-debian-13-isc-dhcp-server-sauvegarder-restaurer)
- [Mise à jour et retour arrière](/01-fiches-simples/debian/13/vie-du-logiciel/isc-dhcp-server/fiche-simple-vm-debian-13-isc-dhcp-server-mise-a-jour-retour-arriere)
- [Documentation officielle](https://www.isc.org/blogs/isc-dhcp-eol/)