# Fiche_Simple_-_VM_Debian_13_HAProxy_Mettre_A_Jour

- **Environnement** : VM Debian 13 Trixie
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

- [HAProxy — Prérequis et limites](Fiche_Simple_-_VM_Debian_13_HAProxy_Prerequis_Limites.md)
- [HAProxy — Installer](Fiche_Simple_-_VM_Debian_13_HAProxy_Installer.md)
- [HAProxy — Configurer un frontend et des backends](Fiche_Simple_-_VM_Debian_13_HAProxy_Configurer.md)
- [HAProxy — Sécuriser (TLS, pare-feu, durcissement)](Fiche_Simple_-_VM_Debian_13_HAProxy_Securiser.md)
- [HAProxy — Valider (recette)](Fiche_Simple_-_VM_Debian_13_HAProxy_Valider.md)
- [HAProxy — Sauvegarder et restaurer](Fiche_Simple_-_VM_Debian_13_HAProxy_Sauvegarder_Restaurer.md)
- [Guide complet Keepalived VRRP + HAProxy](../../../../../02-Fiches-Completes/Transverses/Multi-OS/Autres/08_Haute_Disponibilite_Keepalived_VRRP_HAProxy.md)
- [HAProxy — documentation officielle](https://docs.haproxy.org/)
- [Série Keepalived + HAProxy (haute disponibilité)](../../../../Transverses/Multi-OS/Keepalived-HAProxy/Fiche_Simple_-_VM_Linux_Keepalived_HAProxy_Installer_Valider_HAProxy.md)
