# Fiche_Simple_-_VM_Debian_13_OpenMediaVault_Premiere_Connexion.md

- **Environnement** : OpenMediaVault 8 sur Debian 13 minimal
- **OS / Version** : Debian 13; OpenMediaVault 8.0 Synchrony
- **Catégorie** : stockage / réseau
- **Tags** : `debian13`, `openmediavault`, `interface-web`, `reseau`, `nginx`

---

## Problème précis à résoudre

Sécuriser la première connexion et fixer le réseau depuis OMV.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir l'adresse IP affichée par la console depuis le réseau d'administration, puis changer immédiatement le mot de passe du compte `admin`.
   👉 Explication : Le mot de passe initial est public dans la documentation.

2. Configurer IPv4 statique et DNS : **Network > Interfaces**, puis appliquer depuis la console locale.
   👉 Explication : Une session SSH peut être coupée quand le réseau est redéployé.

3. Vérifier adresse et passerelle depuis la VM, puis l'accès Web depuis une seconde machine :
   ```bash
   sudo ip -br address
   sudo ip route
   ```
   👉 Explication : Confirme que la nouvelle configuration est active.

4. Vérifier qu'aucun autre serveur Web n'est installé :
   ```bash
   dpkg -l apache2 2>/dev/null | grep '^ii' || echo "apache2 absent"
   ```
   👉 Explication : OMV utilise Nginx; installer le paquet Apache peut supprimer OMV.

## 2. Production — Contrôles

Créer un compte nominatif de gestion; limiter l'interface et SSH au réseau d'administration.

## 3. Production — Sécurité

- Ne pas installer un autre serveur Web sur l'hôte.
- Ne pas exposer l'interface Web sur Internet.

## Validation et retour arrière

- **Validation** : interface atteignable avec le nouveau mot de passe depuis le réseau d'administration.
- **Retour arrière** : depuis la console locale, `sudo omv-firstaid` permet de reprendre le réseau.

## Si le problème n'est pas résolu

- [OpenMediaVault — installation sur Debian](https://docs.openmediavault.org/en/latest/installation/on_debian.html)
- [OpenMediaVault — prérequis](https://docs.openmediavault.org/en/latest/prerequisites.html)
- [Guide complet OpenMediaVault Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/66_Deploiement_OpenMediaVault_8_Debian_13.md#4-premiere-connexion-et-reseau)
