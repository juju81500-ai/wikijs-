# Fiche_Simple_-_VM_Debian_13_HAProxy_Valider

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; HAProxy des dépôts Debian
- **Catégorie** : répartiteur de charge / HAProxy / Valider (recette)
- **Tags** : `debian13`, `haproxy`, `recette`

---

## Problème précis à résoudre

Prouver la répartition de charge, le contrôle de santé et la tolérance à la perte d'un backend.

## 1. Hors-Production (Lab / Test / POC)

1. Valider la configuration et le service :
   ```bash
   sudo haproxy -c -f /etc/haproxy/haproxy.cfg
   systemctl is-active haproxy
   ```
   👉 Explication : configuration valide et service actif.

2. Tester la répartition :
   ```bash
   for i in 1 2 3 4; do curl -s http://127.0.0.1/ | head -1; done
   ```
   👉 Explication : chaque backend doit répondre à tour de rôle si leur contenu diffère.

3. Simuler la perte d'un backend :
   ```bash
   # arrêter l'application sur IP_APP1 puis :
   sleep 10; curl -s http://127.0.0.1/ | head -1
   ```
   👉 Explication : le serveur tombé passe `DOWN` dans les statistiques et le trafic reste servi par l'autre.

4. Consulter les statistiques via tunnel SSH :
   ```bash
   ssh -L 8404:127.0.0.1:8404 ADMIN@IP_HAPROXY
   # puis ouvrir http://127.0.0.1:8404/stats
   ```
   👉 Explication : remplacer `ADMIN` et `IP_HAPROXY` (à remplacer).

## 2. Production — Contrôles

Conserver la preuve (date, version, résultats) et activer la supervision des états `UP/DOWN` des backends.

## 3. Production — Sécurité

- Rétablir le backend arrêté après le test.
- Ne pas exposer les statistiques pendant la recette.
- Vérifier les journaux (`journalctl -u haproxy`) sans y exposer d'informations sensibles.

## Validation et retour arrière

- **Validation** : répartition constatée, perte d'un backend sans coupure.
- **Retour arrière** : restaurer la configuration précédente et recharger.

## Si le problème n'est pas résolu

- [HAProxy — Prérequis et limites](Fiche_Simple_-_VM_Debian_13_HAProxy_Prerequis_Limites.md)
- [HAProxy — Installer](Fiche_Simple_-_VM_Debian_13_HAProxy_Installer.md)
- [HAProxy — Configurer un frontend et des backends](Fiche_Simple_-_VM_Debian_13_HAProxy_Configurer.md)
- [HAProxy — Sécuriser (TLS, pare-feu, durcissement)](Fiche_Simple_-_VM_Debian_13_HAProxy_Securiser.md)
- [HAProxy — Sauvegarder et restaurer](Fiche_Simple_-_VM_Debian_13_HAProxy_Sauvegarder_Restaurer.md)
- [HAProxy — Mise à jour et retour arrière](Fiche_Simple_-_VM_Debian_13_HAProxy_Mettre_A_Jour.md)
- [Guide complet Keepalived VRRP + HAProxy](../../../../../02-Fiches-Completes/Transverses/Multi-OS/Autres/08_Haute_Disponibilite_Keepalived_VRRP_HAProxy.md)
- [HAProxy — documentation officielle](https://docs.haproxy.org/)
- [Série Keepalived + HAProxy (haute disponibilité)](../../../../Transverses/Multi-OS/Keepalived-HAProxy/Fiche_Simple_-_VM_Linux_Keepalived_HAProxy_Installer_Valider_HAProxy.md)
