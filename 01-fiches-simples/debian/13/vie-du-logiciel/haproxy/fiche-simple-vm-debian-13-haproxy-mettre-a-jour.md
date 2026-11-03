# Fiche_Simple_-_VM_Debian_13_HAProxy_Mettre_A_Jour

- **Environnement** : [[Glossary:VM]] Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; HAProxy des dépôts Debian
- **Catégorie** : répartiteur de charge / HAProxy / Mise à jour et retour arrière
- **Tags** : `debian13`, `haproxy`, `mise-a-jour`

---

## Problème précis à résoudre

Mettre à jour HAProxy et revenir à la version précédente si nécessaire.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder :
   ```bash
   sudo tar -czpf /var/backups/haproxy/avant-maj-$(date +%F).tar.gz /etc/haproxy
   ```
   👉 Explication : base du retour arrière.

2. Identifier la mise à jour :
   ```bash
   sudo apt update
   apt list --upgradable 2>/dev/null | grep -i haproxy
   apt-cache policy haproxy
   ```
   👉 Explication : noter versions actuelle et cible.

3. Appliquer :
   ```bash
   sudo apt install --only-upgrade haproxy
   sudo haproxy -c -f /etc/haproxy/haproxy.cfg && sudo systemctl restart haproxy
   haproxy -v
   ```
   👉 Explication : valider avant le redémarrage.

4. Retour arrière :
   ```bash
   sudo apt install haproxy=VERSION_PRECEDENTE
   sudo apt-mark hold haproxy
   ```
   👉 Explication : remplacer `VERSION_PRECEDENTE` (vérifier la disponibilité) ; `apt-mark unhold haproxy` ensuite.

## 2. Production — Contrôles

Pilote, fenêtre approuvée, sauvegarde préalable, surveillance des backends après la mise à jour.

## 3. Production — Sécurité

- Ne pas mettre à jour sans pilote.
- Consigner tout `apt-mark hold`.
- Lire les notes de version (changements de directives).

## Validation et retour arrière

- **Validation** : `haproxy -v` affiche la version cible, backends `UP`.
- **Retour arrière** : réinstaller la version précédente et restaurer `/etc/haproxy`.

## Si le problème n'est pas résolu

- [HAProxy — Prérequis et limites](fiche-simple-vm-debian-13-haproxy-prerequis-limites.md)
- [HAProxy — Installer](fiche-simple-vm-debian-13-haproxy-installer.md)
- [HAProxy — Configurer un frontend et des backends](fiche-simple-vm-debian-13-haproxy-configurer.md)
- [HAProxy — Sécuriser (TLS, pare-feu, durcissement)](fiche-simple-vm-debian-13-haproxy-securiser.md)
- [HAProxy — Valider (recette)](fiche-simple-vm-debian-13-haproxy-valider.md)
- [HAProxy — Sauvegarder et restaurer](fiche-simple-vm-debian-13-haproxy-sauvegarder-restaurer.md)
- [Guide complet Keepalived VRRP + HAProxy](../../../../../02-fiches-completes/transverses/multi-os/autres/08-haute-disponibilite-keepalived-vrrp-haproxy.md)
- [HAProxy — documentation officielle](https://docs.haproxy.org/)
- [Série Keepalived + HAProxy (haute disponibilité)](../../../../transverses/multi-os/keepalived-haproxy/fiche-simple-vm-linux-keepalived-haproxy-installer-valider-haproxy.md)
