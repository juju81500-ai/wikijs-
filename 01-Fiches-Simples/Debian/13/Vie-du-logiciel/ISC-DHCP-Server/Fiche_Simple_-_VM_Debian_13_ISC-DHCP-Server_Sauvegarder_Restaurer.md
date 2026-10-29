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

- [Prérequis et limites](Fiche_Simple_-_VM_Debian_13_ISC-DHCP-Server_Prerequis_Limites.md)
- [Installer](Fiche_Simple_-_VM_Debian_13_ISC-DHCP-Server_Installer.md)
- [Configurer](Fiche_Simple_-_VM_Debian_13_ISC-DHCP-Server_Configurer.md)
- [Sécuriser](Fiche_Simple_-_VM_Debian_13_ISC-DHCP-Server_Securiser.md)
- [Valider (recette)](Fiche_Simple_-_VM_Debian_13_ISC-DHCP-Server_Valider.md)
- [Mise à jour et retour arrière](Fiche_Simple_-_VM_Debian_13_ISC-DHCP-Server_Mise_A_Jour_Retour_Arriere.md)
- [Documentation officielle](https://www.isc.org/blogs/isc-dhcp-eol/)
