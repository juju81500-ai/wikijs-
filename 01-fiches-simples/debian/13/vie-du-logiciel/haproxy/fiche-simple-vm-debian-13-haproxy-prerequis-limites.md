# Fiche_Simple_-_VM_Debian_13_HAProxy_Prerequis_Limites

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; HAProxy des dépôts Debian
- **Catégorie** : répartiteur de charge / HAProxy / Prérequis et limites
- **Tags** : `debian13`, `haproxy`, `prerequis`

---

## Problème précis à résoudre

Cadrer un HAProxy seul sur Debian 13 (répartiteur de charge / reverse proxy) avant installation.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler l'OS et les ports :
   ```bash
   cat /etc/os-release | grep PRETTY_NAME
   sudo ss -tlnp | grep -E ':(80|443|8404)\b' || echo 'ports libres'
   ```
   👉 Explication : 80/443 pour le trafic, 8404 (exemple) pour les statistiques.

2. Lister les serveurs d'arrière-plan :
   👉 Explication : dresser la liste des applications à publier (adresse IP, port, protocole, chemin de santé) ; chacun doit répondre depuis la VM.

3. Tester l'accessibilité d'un backend :
   ```bash
   curl -sI http://IP_BACKEND:PORT_BACKEND/ | head -3
   ```
   👉 Explication : remplacer `IP_BACKEND` et `PORT_BACKEND` (à remplacer) ; sans réponse, corriger le réseau avant d'installer.

4. Noter les limites :
   👉 Explication : série pour un nœud unique (la haute disponibilité VRRP est dans la série Keepalived-HAProxy) ; version Debian à vérifier avec `apt-cache policy haproxy`.

## 2. Production — Contrôles

Consigner IP/DNS, backends, mode (HTTP ou TCP), certificats, responsable, fenêtre de maintenance.

## 3. Production — Sécurité

- Prévoir un pare-feu autorisant seulement les flux utiles.
- Un nœud unique est un point de défaillance : documenter le risque ou mettre en place la série HA.
- Ne pas publier les statistiques sur Internet.

## Validation et retour arrière

- **Validation** : ports libres, backends joignables, périmètre consigné.
- **Retour arrière** : aucune modification effectuée.

## Si le problème n'est pas résolu

- [HAProxy — Installer](fiche-simple-vm-debian-13-haproxy-installer.md)
- [HAProxy — Configurer un frontend et des backends](fiche-simple-vm-debian-13-haproxy-configurer.md)
- [HAProxy — Sécuriser (TLS, pare-feu, durcissement)](fiche-simple-vm-debian-13-haproxy-securiser.md)
- [HAProxy — Valider (recette)](fiche-simple-vm-debian-13-haproxy-valider.md)
- [HAProxy — Sauvegarder et restaurer](fiche-simple-vm-debian-13-haproxy-sauvegarder-restaurer.md)
- [HAProxy — Mise à jour et retour arrière](fiche-simple-vm-debian-13-haproxy-mettre-a-jour.md)
- [Guide complet Keepalived VRRP + HAProxy](../../../../../02-fiches-completes/transverses/multi-os/autres/08-haute-disponibilite-keepalived-vrrp-haproxy.md)
- [HAProxy — documentation officielle](https://docs.haproxy.org/)
- [Série Keepalived + HAProxy (haute disponibilité)](../../../../transverses/multi-os/keepalived-haproxy/fiche-simple-vm-linux-keepalived-haproxy-installer-valider-haproxy.md)
