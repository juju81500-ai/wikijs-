# Fiche_Simple_-_VM_Debian_13_ISC-DHCP-Server_Securiser

- **Environnement** : VM Debian 13; ISC DHCP déprécié, usage transitoire
- **OS / Version** : Debian 13
- **Catégorie** : Vie du logiciel / ISC-DHCP-Server — Sécuriser
- **Tags** : `isc-dhcp`, `serveur`, `vie-du-logiciel`, `securiser`

---

## Problème précis à résoudre

Restreindre DHCP UDP 67 et les accès d’administration.

## 1. Hors-Production (Lab / Test / POC)

1. Sécuriser :
   ```bash
   grep -E "^INTERFACESv4" /etc/default/isc-dhcp-server
sudo ss -lunp | grep ":67" || true
sudo ufw allow from ADMIN_CIDR to any port 22 proto tcp
sudo ufw allow in on INTERFACE_LAB to any port 67 proto udp
sudo ufw status numbered
   ```
   👉 Explication : `ADMIN_CIDR` et `INTERFACE_LAB` sont des placeholders à remplacer; vérifier SSH avant activation.


## 2. Production — Contrôles

Filtrer par VLAN/interface et ACL réseau; valider les relais indépendamment.

## 3. Production — Sécurité

EOL upstream : limiter exposition, protéger journaux/baux et migrer Kea.

## Validation et retour arrière

- **Validation** : Seuls segments autorisés reçoivent une offre DHCP.
- **Retour arrière** : Retirer règles ajoutées en préservant l’accès admin.

## Si le problème n'est pas résolu

- [Prérequis et limites](Fiche_Simple_-_VM_Debian_13_ISC-DHCP-Server_Prerequis_Limites.md)
- [Installer](Fiche_Simple_-_VM_Debian_13_ISC-DHCP-Server_Installer.md)
- [Configurer](Fiche_Simple_-_VM_Debian_13_ISC-DHCP-Server_Configurer.md)
- [Valider (recette)](Fiche_Simple_-_VM_Debian_13_ISC-DHCP-Server_Valider.md)
- [Sauvegarder / restaurer](Fiche_Simple_-_VM_Debian_13_ISC-DHCP-Server_Sauvegarder_Restaurer.md)
- [Mise à jour et retour arrière](Fiche_Simple_-_VM_Debian_13_ISC-DHCP-Server_Mise_A_Jour_Retour_Arriere.md)
- [Documentation officielle](https://www.isc.org/blogs/isc-dhcp-eol/)
