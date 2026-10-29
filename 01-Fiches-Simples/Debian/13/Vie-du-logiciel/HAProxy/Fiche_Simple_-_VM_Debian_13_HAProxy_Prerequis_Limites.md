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

- [HAProxy — Installer](Fiche_Simple_-_VM_Debian_13_HAProxy_Installer.md)
- [HAProxy — Configurer un frontend et des backends](Fiche_Simple_-_VM_Debian_13_HAProxy_Configurer.md)
- [HAProxy — Sécuriser (TLS, pare-feu, durcissement)](Fiche_Simple_-_VM_Debian_13_HAProxy_Securiser.md)
- [HAProxy — Valider (recette)](Fiche_Simple_-_VM_Debian_13_HAProxy_Valider.md)
- [HAProxy — Sauvegarder et restaurer](Fiche_Simple_-_VM_Debian_13_HAProxy_Sauvegarder_Restaurer.md)
- [HAProxy — Mise à jour et retour arrière](Fiche_Simple_-_VM_Debian_13_HAProxy_Mettre_A_Jour.md)
- [Guide complet Keepalived VRRP + HAProxy](../../../../../02-Fiches-Completes/Transverses/Multi-OS/Autres/08_Haute_Disponibilite_Keepalived_VRRP_HAProxy.md)
- [HAProxy — documentation officielle](https://docs.haproxy.org/)
- [Série Keepalived + HAProxy (haute disponibilité)](../../../../Transverses/Multi-OS/Keepalived-HAProxy/Fiche_Simple_-_VM_Linux_Keepalived_HAProxy_Installer_Valider_HAProxy.md)
