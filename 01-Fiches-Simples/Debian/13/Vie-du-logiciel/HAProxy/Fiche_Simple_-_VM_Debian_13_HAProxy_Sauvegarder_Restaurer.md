# Fiche_Simple_-_VM_Debian_13_HAProxy_Sauvegarder_Restaurer

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; HAProxy des dépôts Debian
- **Catégorie** : répartiteur de charge / HAProxy / Sauvegarder et restaurer
- **Tags** : `debian13`, `haproxy`, `sauvegarde`

---

## Problème précis à résoudre

Sauvegarder configuration et certificats HAProxy et prouver la restauration.

## 1. Hors-Production (Lab / Test / POC)

1. Archiver :
   ```bash
   sudo install -d -m 0700 /var/backups/haproxy
   sudo tar -czpf /var/backups/haproxy/haproxy-$(date +%F).tar.gz /etc/haproxy
   ```
   👉 Explication : contient les clés privées : dossier en `0700`, copie externe chiffrée.

2. Relire l'archive :
   ```bash
   sudo tar -tzf /var/backups/haproxy/haproxy-$(date +%F).tar.gz
   ```
   👉 Explication : contrôle de lisibilité.

3. Restaurer sur VM pilote :
   ```bash
   sudo systemctl stop haproxy
   sudo tar -xzpf /var/backups/haproxy/haproxy-DATE.tar.gz -C /
   sudo haproxy -c -f /etc/haproxy/haproxy.cfg && sudo systemctl start haproxy
   ```
   👉 Explication : remplacer `DATE` (à remplacer).

## 2. Production — Contrôles

Sauvegarde planifiée, générations multiples, copie chiffrée hors site, test de restauration périodique.

## 3. Production — Sécurité

- Chiffrer les copies contenant des clés.
- Ne pas stocker sur le même disque.
- Limiter l'accès au dossier de sauvegarde.

## Validation et retour arrière

- **Validation** : restauration testée avec `haproxy -c` valide.
- **Retour arrière** : reprendre l'archive précédente.

## Si le problème n'est pas résolu

- [HAProxy — Prérequis et limites](Fiche_Simple_-_VM_Debian_13_HAProxy_Prerequis_Limites.md)
- [HAProxy — Installer](Fiche_Simple_-_VM_Debian_13_HAProxy_Installer.md)
- [HAProxy — Configurer un frontend et des backends](Fiche_Simple_-_VM_Debian_13_HAProxy_Configurer.md)
- [HAProxy — Sécuriser (TLS, pare-feu, durcissement)](Fiche_Simple_-_VM_Debian_13_HAProxy_Securiser.md)
- [HAProxy — Valider (recette)](Fiche_Simple_-_VM_Debian_13_HAProxy_Valider.md)
- [HAProxy — Mise à jour et retour arrière](Fiche_Simple_-_VM_Debian_13_HAProxy_Mettre_A_Jour.md)
- [Guide complet Keepalived VRRP + HAProxy](../../../../../02-Fiches-Completes/Transverses/Multi-OS/Autres/08_Haute_Disponibilite_Keepalived_VRRP_HAProxy.md)
- [HAProxy — documentation officielle](https://docs.haproxy.org/)
- [Série Keepalived + HAProxy (haute disponibilité)](../../../../Transverses/Multi-OS/Keepalived-HAProxy/Fiche_Simple_-_VM_Linux_Keepalived_HAProxy_Installer_Valider_HAProxy.md)
