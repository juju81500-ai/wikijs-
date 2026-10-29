# Fiche_Simple_-_VM_Debian_13_HAProxy_Installer

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; HAProxy des dépôts Debian
- **Catégorie** : répartiteur de charge / HAProxy / Installer

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

- [HAProxy — Prérequis et limites](/01-fiches-simples/debian/13/vie-du-logiciel/haproxy/fiche-simple-vm-debian-13-haproxy-prerequis-limites)
- [HAProxy — Configurer un frontend et des backends](/01-fiches-simples/debian/13/vie-du-logiciel/haproxy/fiche-simple-vm-debian-13-haproxy-configurer)
- [HAProxy — Sécuriser (TLS, pare-feu, durcissement)](/01-fiches-simples/debian/13/vie-du-logiciel/haproxy/fiche-simple-vm-debian-13-haproxy-securiser)
- [HAProxy — Valider (recette)](/01-fiches-simples/debian/13/vie-du-logiciel/haproxy/fiche-simple-vm-debian-13-haproxy-valider)
- [HAProxy — Sauvegarder et restaurer](/01-fiches-simples/debian/13/vie-du-logiciel/haproxy/fiche-simple-vm-debian-13-haproxy-sauvegarder-restaurer)
- [HAProxy — Mise à jour et retour arrière](/01-fiches-simples/debian/13/vie-du-logiciel/haproxy/fiche-simple-vm-debian-13-haproxy-mettre-a-jour)
- [Guide complet Keepalived VRRP + HAProxy](/02-fiches-completes/transverses/multi-os/autres/08-haute-disponibilite-keepalived-vrrp-haproxy)
- [HAProxy — documentation officielle](https://docs.haproxy.org/)
- [Série Keepalived + HAProxy (haute disponibilité)](/01-fiches-simples/transverses/multi-os/keepalived-haproxy/fiche-simple-vm-linux-keepalived-haproxy-installer-valider-haproxy)