# Fiche_Simple_-_VM_Debian_12_GLPI_Maintenir_Restaurer.md

- **Environnement** : instance GLPI Debian en production; base et fichiers sauvegardés de façon cohérente
- **OS / Version** : Debian 12 ou 13; version GLPI supportée
- **Catégorie** : GLPI / exploitation et restauration
- **Tags** : `debian12`, `glpi`, `backup`, `upgrade`, `restore`, `rollback`

---

## Problème précis à résoudre

Mettre à niveau ou revenir en arrière en conservant la cohérence entre la base GLPI et ses fichiers.

## 1. Hors-Production (Lab / Test / POC)

1. Avant mise à niveau, activer le mode maintenance : **Configuration > Générale > Mode maintenance**.
   👉 Explication : évite les écritures pendant la sauvegarde.

2. Sauvegarder base et fichiers :
   ```bash
   sudo mariadb-dump --single-transaction glpi | gzip > /root/glpi-db-$(date +%F).sql.gz
   sudo tar czf /root/glpi-files-$(date +%F).tgz /var/lib/glpi /etc/glpi
   ```
   👉 Explication : copier hors serveur et tester la restauration.

3. Mettre en place la nouvelle version en gardant l'ancienne :
   ```bash
   sudo ln -sfn /var/www/glpi/releases/NOUVELLE_VERSION /var/www/glpi/current
   sudo php /var/www/glpi/current/bin/console database:update
   ```
   👉 Explication : conserver l'ancienne version jusqu'à validation fonctionnelle.

4. En cas d'échec, revenir en arrière :
   ```bash
   sudo ln -sfn /var/www/glpi/releases/ANCIENNE_VERSION /var/www/glpi/current
   gunzip -c /root/glpi-db-AAAA-MM-JJ.sql.gz | sudo mariadb glpi
   sudo tar xzf /root/glpi-files-AAAA-MM-JJ.tgz -C /
   sudo systemctl reload nginx
   ```
   👉 Explication : remplacer versions et date; la restauration de la base écrase l'état courant.

## 2. Production — Contrôles

Faire approuver fenêtre, mode maintenance, sauvegarde, test de restauration, version cible, critères de validation et responsable métier.

## 3. Production — Sécurité

- Ne pas restaurer base et fichiers de dates différentes sans procédure de cohérence.
- Ne pas supprimer l'ancienne version avant validation.
- Protéger les sauvegardes et documents GLPI selon leur classification.
- Ne pas désactiver le mode maintenance avant les contrôles d'intégrité et de fonction.

## Validation et retour arrière

- **Validation** : connexion, tickets, documents, tâches planifiées et courriels contrôlés après changement.
- **Retour arrière** : restaurer ensemble base et fichiers de la même sauvegarde, puis valider le parcours métier avant réouverture.

## Si le problème n'est pas résolu

- [GLPI — documentation](https://glpi-install.readthedocs.io/en/latest/)
- [MariaDB — sauvegarde et restauration](https://mariadb.com/kb/en/backup-and-restore-overview/)
- [Guide complet GLPI Debian](../../../../../02-Fiches-Completes/Debian/12/Installation-Deploiement/03_Helpdesk_ITSM_GLPI_11_12_Debian_12_13.md)
