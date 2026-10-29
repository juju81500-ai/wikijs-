# Fiche_Simple_-_VM_Debian_13_ISC-DHCP-Server_Installer

- **Environnement** : VM Debian 13; ISC DHCP déprécié, usage transitoire
- **OS / Version** : Debian 13
- **Catégorie** : Vie du logiciel / ISC-DHCP-Server — Installer

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

- [Prérequis et limites](/01-fiches-simples/debian/13/vie-du-logiciel/isc-dhcp-server/fiche-simple-vm-debian-13-isc-dhcp-server-prerequis-limites)
- [Configurer](/01-fiches-simples/debian/13/vie-du-logiciel/isc-dhcp-server/fiche-simple-vm-debian-13-isc-dhcp-server-configurer)
- [Sécuriser](/01-fiches-simples/debian/13/vie-du-logiciel/isc-dhcp-server/fiche-simple-vm-debian-13-isc-dhcp-server-securiser)
- [Valider (recette)](/01-fiches-simples/debian/13/vie-du-logiciel/isc-dhcp-server/fiche-simple-vm-debian-13-isc-dhcp-server-valider)
- [Sauvegarder / restaurer](/01-fiches-simples/debian/13/vie-du-logiciel/isc-dhcp-server/fiche-simple-vm-debian-13-isc-dhcp-server-sauvegarder-restaurer)
- [Mise à jour et retour arrière](/01-fiches-simples/debian/13/vie-du-logiciel/isc-dhcp-server/fiche-simple-vm-debian-13-isc-dhcp-server-mise-a-jour-retour-arriere)
- [Documentation officielle](https://www.isc.org/blogs/isc-dhcp-eol/)