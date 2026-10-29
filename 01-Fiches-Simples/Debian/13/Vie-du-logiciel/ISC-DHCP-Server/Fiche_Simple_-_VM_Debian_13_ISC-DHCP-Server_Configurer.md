# Fiche_Simple_-_VM_Debian_13_ISC-DHCP-Server_Configurer

- **Environnement** : VM Debian 13; ISC DHCP déprécié, usage transitoire
- **OS / Version** : Debian 13
- **Catégorie** : Vie du logiciel / ISC-DHCP-Server — Configurer
- **Tags** : `isc-dhcp`, `serveur`, `vie-du-logiciel`, `configurer`

---

## Problème précis à résoudre

Limiter dhcpd à l’interface et plage du lab.

## 1. Hors-Production (Lab / Test / POC)

1. Configurer :
   ```bash
   ip -br addr
sudoedit /etc/default/isc-dhcp-server
sudoedit /etc/dhcp/dhcpd.conf
sudo dhcpd -t -cf /etc/dhcp/dhcpd.conf
   ```
   👉 Explication : Définir `INTERFACESv4` et les options réseau exactes; valider syntaxe avant démarrage.


## 2. Production — Contrôles

Vérifier chevauchements, réservations, relais et VLAN avec l’équipe réseau.

## 3. Production — Sécurité

Une plage erronée peut perturber le VLAN; préparer arrêt d’urgence.

## Validation et retour arrière

- **Validation** : Syntaxe valide et écoute limitée à l’interface attendue.
- **Retour arrière** : Restaurer les fichiers sauvegardés puis valider la syntaxe.

## Si le problème n'est pas résolu

- [Prérequis et limites](Fiche_Simple_-_VM_Debian_13_ISC-DHCP-Server_Prerequis_Limites.md)
- [Installer](Fiche_Simple_-_VM_Debian_13_ISC-DHCP-Server_Installer.md)
- [Sécuriser](Fiche_Simple_-_VM_Debian_13_ISC-DHCP-Server_Securiser.md)
- [Valider (recette)](Fiche_Simple_-_VM_Debian_13_ISC-DHCP-Server_Valider.md)
- [Sauvegarder / restaurer](Fiche_Simple_-_VM_Debian_13_ISC-DHCP-Server_Sauvegarder_Restaurer.md)
- [Mise à jour et retour arrière](Fiche_Simple_-_VM_Debian_13_ISC-DHCP-Server_Mise_A_Jour_Retour_Arriere.md)
- [Documentation officielle](https://www.isc.org/blogs/isc-dhcp-eol/)
