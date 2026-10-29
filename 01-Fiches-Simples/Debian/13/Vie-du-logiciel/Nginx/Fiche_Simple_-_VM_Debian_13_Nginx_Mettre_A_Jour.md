# Fiche_Simple_-_VM_Debian_13_Nginx_Mettre_A_Jour

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; Nginx des dépôts Debian
- **Catégorie** : serveur Web / Nginx / Mise à jour et retour arrière
- **Tags** : `debian13`, `nginx`, `mise-a-jour`

---

## Problème précis à résoudre

Mettre à jour Nginx sans interruption prolongée et savoir revenir à la version précédente.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder avant toute mise à jour :
   ```bash
   sudo tar -czpf /var/backups/nginx/avant-maj-$(date +%F).tar.gz /etc/nginx
   ```
   👉 Explication : la configuration est le seul élément à restaurer après un échec.

2. Lister la mise à jour disponible et lire les notes de version :
   ```bash
   sudo apt update
   apt list --upgradable 2>/dev/null | grep -i nginx
   apt-cache policy nginx
   ```
   👉 Explication : noter la version actuelle et la version cible.

3. Appliquer la mise à jour :
   ```bash
   sudo apt install --only-upgrade nginx
   sudo nginx -t && sudo systemctl restart nginx
   nginx -v
   ```
   👉 Explication : tester la syntaxe avant le redémarrage.

4. Revenir à la version précédente si nécessaire :
   ```bash
   sudo apt install nginx=VERSION_PRECEDENTE
   sudo apt-mark hold nginx
   ```
   👉 Explication : remplacer `VERSION_PRECEDENTE` par la version relevée à l'étape 2 (vérifier qu'elle est disponible dans `apt-cache policy`) ; `apt-mark unhold nginx` une fois le correctif disponible.

## 2. Production — Contrôles

Tester sur un pilote, planifier une fenêtre, prévenir les utilisateurs, conserver la sauvegarde de configuration et surveiller les journaux après la mise à jour.

## 3. Production — Sécurité

- Ne pas mettre à jour directement un service de production sans pilote.
- N'utiliser `apt-mark hold` que temporairement et le consigner.
- Relire les notes de sécurité Debian (DSA) avant d'attendre la fenêtre.

## Validation et retour arrière

- **Validation** : `nginx -v` affiche la version cible, `nginx -t` réussit, le site répond.
- **Retour arrière** : réinstaller la version précédente, restaurer `/etc/nginx` depuis l'archive d'avant mise à jour, `nginx -t`, redémarrer.

## Si le problème n'est pas résolu

- [Nginx — Prérequis et limites](Fiche_Simple_-_VM_Debian_13_Nginx_Prerequis_Limites.md)
- [Nginx — Installer](Fiche_Simple_-_VM_Debian_13_Nginx_Installer.md)
- [Nginx — Configurer un site](Fiche_Simple_-_VM_Debian_13_Nginx_Configurer.md)
- [Nginx — Sécuriser (TLS, en-têtes, pare-feu)](Fiche_Simple_-_VM_Debian_13_Nginx_Securiser.md)
- [Nginx — Valider (recette)](Fiche_Simple_-_VM_Debian_13_Nginx_Valider.md)
- [Nginx — Sauvegarder et restaurer](Fiche_Simple_-_VM_Debian_13_Nginx_Sauvegarder_Restaurer.md)
- [Guide complet LEMP Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/02_Pile_LEMP_Debian_13_Nginx_PHP_MariaDB.md)
- [Nginx — documentation officielle](https://nginx.org/en/docs/)
