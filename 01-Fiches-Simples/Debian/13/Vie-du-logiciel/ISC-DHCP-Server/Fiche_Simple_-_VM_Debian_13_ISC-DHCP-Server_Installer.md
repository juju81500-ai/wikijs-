# Fiche_Simple_-_VM_Debian_13_ISC-DHCP-Server_Installer

- **Environnement** : VM Debian 13; ISC DHCP déprécié, usage transitoire
- **OS / Version** : Debian 13
- **Catégorie** : Vie du logiciel / ISC-DHCP-Server — Installer
- **Tags** : `isc-dhcp`, `serveur`, `vie-du-logiciel`, `installer`

---

## Problème précis à résoudre

Installer le paquet uniquement en lab si candidat Debian officiel disponible.

## 1. Hors-Production (Lab / Test / POC)

1. Installer :
   ```bash
   apt-cache policy isc-dhcp-server
sudo apt update
sudo apt install isc-dhcp-server
dpkg-query -W -f="${Version} ${Status}\n" isc-dhcp-server
   ```
   👉 Explication : Ne poursuivre que si le candidat vient d’un dépôt Debian officiel; ne pas utiliser de paquet externe.


## 2. Production — Contrôles

Nouveau déploiement : privilégier Kea. Existant : migration transitoire limitée.

## 3. Production — Sécurité

Ne pas présumer d’un support upstream; ne pas exposer avant configuration.

## Validation et retour arrière

- **Validation** : Paquet installé depuis dépôt officiel et limité au lab.
- **Retour arrière** : Arrêter service et restaurer snapshot après vérification des dépendances.

## Si le problème n'est pas résolu

- [Prérequis et limites](Fiche_Simple_-_VM_Debian_13_ISC-DHCP-Server_Prerequis_Limites.md)
- [Configurer](Fiche_Simple_-_VM_Debian_13_ISC-DHCP-Server_Configurer.md)
- [Sécuriser](Fiche_Simple_-_VM_Debian_13_ISC-DHCP-Server_Securiser.md)
- [Valider (recette)](Fiche_Simple_-_VM_Debian_13_ISC-DHCP-Server_Valider.md)
- [Sauvegarder / restaurer](Fiche_Simple_-_VM_Debian_13_ISC-DHCP-Server_Sauvegarder_Restaurer.md)
- [Mise à jour et retour arrière](Fiche_Simple_-_VM_Debian_13_ISC-DHCP-Server_Mise_A_Jour_Retour_Arriere.md)
- [Documentation officielle](https://www.isc.org/blogs/isc-dhcp-eol/)
