# Fiche_Simple_-_VM_Debian_13_HAProxy_Installer

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; HAProxy des dépôts Debian
- **Catégorie** : répartiteur de charge / HAProxy / Installer
- **Tags** : `debian13`, `haproxy`, `installation`

---

## Problème précis à résoudre

Installer HAProxy depuis le dépôt Debian et vérifier la version et le service.

## 1. Hors-Production (Lab / Test / POC)

1. Relever la version candidate :
   ```bash
   sudo apt update
   apt-cache policy haproxy
   ```
   👉 Explication : consigner la version avant installation.

2. Installer le paquet :
   ```bash
   sudo apt install -y haproxy
   ```
   👉 Explication : crée l'unité systemd et `/etc/haproxy/haproxy.cfg`.

3. Activer le service :
   ```bash
   sudo systemctl enable --now haproxy
   systemctl status haproxy --no-pager
   ```
   👉 Explication : service actif.

4. Vérifier la version et la configuration :
   ```bash
   haproxy -v
   sudo haproxy -c -f /etc/haproxy/haproxy.cfg
   ```
   👉 Explication : `-c` ne démarre rien et valide la syntaxe ; à répéter avant chaque rechargement.

## 2. Production — Contrôles

Consigner version, origine des paquets et cadence de mise à jour.

## 3. Production — Sécurité

- Dépôt Debian officiel uniquement (ou dépôt éditeur approuvé).
- Ne pas ouvrir le pare-feu avant la recette.
- Ne pas modifier `haproxy.cfg` sans sauvegarde.

## Validation et retour arrière

- **Validation** : `haproxy -c` renvoie `Configuration file is valid` et le service est actif.
- **Retour arrière** : `sudo apt purge haproxy` après avoir sauvegardé `/etc/haproxy`.

## Si le problème n'est pas résolu

- [HAProxy — Prérequis et limites](Fiche_Simple_-_VM_Debian_13_HAProxy_Prerequis_Limites.md)
- [HAProxy — Configurer un frontend et des backends](Fiche_Simple_-_VM_Debian_13_HAProxy_Configurer.md)
- [HAProxy — Sécuriser (TLS, pare-feu, durcissement)](Fiche_Simple_-_VM_Debian_13_HAProxy_Securiser.md)
- [HAProxy — Valider (recette)](Fiche_Simple_-_VM_Debian_13_HAProxy_Valider.md)
- [HAProxy — Sauvegarder et restaurer](Fiche_Simple_-_VM_Debian_13_HAProxy_Sauvegarder_Restaurer.md)
- [HAProxy — Mise à jour et retour arrière](Fiche_Simple_-_VM_Debian_13_HAProxy_Mettre_A_Jour.md)
- [Guide complet Keepalived VRRP + HAProxy](../../../../../02-Fiches-Completes/Transverses/Multi-OS/Autres/08_Haute_Disponibilite_Keepalived_VRRP_HAProxy.md)
- [HAProxy — documentation officielle](https://docs.haproxy.org/)
- [Série Keepalived + HAProxy (haute disponibilité)](../../../../Transverses/Multi-OS/Keepalived-HAProxy/Fiche_Simple_-_VM_Linux_Keepalived_HAProxy_Installer_Valider_HAProxy.md)
