# Fiche_Simple_-_VM_Debian_13_ISC-DHCP-Server_Mise_A_Jour_Retour_Arriere

- **Environnement** : VM Debian 13; ISC DHCP déprécié, usage transitoire
- **OS / Version** : Debian 13
- **Catégorie** : Vie du logiciel / ISC-DHCP-Server — Mise à jour et retour arrière
- **Tags** : `isc-dhcp`, `serveur`, `vie-du-logiciel`, `mise_a_jour_retour_arriere`

---

## Problème précis à résoudre

Contrôler mises à jour Debian et accélérer le remplacement par Kea.

## 1. Hors-Production (Lab / Test / POC)

1. Mise à jour et retour arrière :
   ```bash
   sudo apt update
apt-cache policy isc-dhcp-server
apt list --upgradable 2>/dev/null | grep isc-dhcp || true
sudo dhcpd -t -cf /etc/dhcp/dhcpd.conf
   ```
   👉 Explication : Paquet présent ne signifie pas maintenance upstream; archive de config avant migration.


## 2. Production — Contrôles

Prioriser migration Kea et tester plage, réservations/options en lab.

## 3. Production — Sécurité

Appliquer seulement mises à jour Debian disponibles; réduire usage du logiciel EOL.

## Validation et retour arrière

- **Validation** : Plan de migration/repli testé et approuvé.
- **Retour arrière** : Réactiver ISC uniquement après arrêt Kea et validation du propriétaire DHCP.

## Si le problème n'est pas résolu

- [Prérequis et limites](Fiche_Simple_-_VM_Debian_13_ISC-DHCP-Server_Prerequis_Limites.md)
- [Installer](Fiche_Simple_-_VM_Debian_13_ISC-DHCP-Server_Installer.md)
- [Configurer](Fiche_Simple_-_VM_Debian_13_ISC-DHCP-Server_Configurer.md)
- [Sécuriser](Fiche_Simple_-_VM_Debian_13_ISC-DHCP-Server_Securiser.md)
- [Valider (recette)](Fiche_Simple_-_VM_Debian_13_ISC-DHCP-Server_Valider.md)
- [Sauvegarder / restaurer](Fiche_Simple_-_VM_Debian_13_ISC-DHCP-Server_Sauvegarder_Restaurer.md)
- [Documentation officielle](https://www.isc.org/blogs/isc-dhcp-eol/)
