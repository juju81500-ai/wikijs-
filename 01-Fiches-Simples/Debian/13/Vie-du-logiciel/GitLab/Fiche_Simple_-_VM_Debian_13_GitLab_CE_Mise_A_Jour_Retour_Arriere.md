# Fiche_Simple_-_VM_Debian_13_GitLab_CE_Mise_A_Jour_Retour_Arriere

- **Environnement** : VM Debian 13 de préproduction; FQDN et ressources confirmés
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : forge Git / administration
- **Tags** : `debian13`, `gitlab-ce`, `forge-git`, `tls`, `sauvegarde`
---

## Problème précis à résoudre

Appliquer un chemin GitLab supporté avec sauvegarde cohérente et tests post-migration.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier notes et étapes intermédiaires requises
   ```text
   Navigateur > ouvrir la documentation officielle : https://docs.gitlab.com/install/package/
   ```
   👉 Explication : ne jamais sauter un palier ou une migration requise. Détail à confirmer dans la documentation officielle avant application : Comparer versions actuelle/cible et les étapes obligatoires dans la documentation GitLab.

2. Créer backup et contrôler espace
   ```bash
   sudo gitlab-backup create
   sudo df -h /var/opt/gitlab /var/log/gitlab
   ```
   👉 Explication : sauvegarder aussi configuration et secrets.

3. Installer une version exacte approuvée
   ```bash
   apt-cache madison gitlab-ce
   sudo apt install gitlab-ce=18.X.Y-ce.0
   ```
   👉 Explication : remplacer la version à remplacer et suivre les paliers officiels.

4. Reconfigurer et répéter la recette
   ```bash
   sudo gitlab-ctl reconfigure
   sudo gitlab-ctl status
   sudo gitlab-rake gitlab:check SANITIZE=true
   ```
   👉 Explication : surveiller migrations, clone Git, utilisateurs et runners.

## 2. Production — Contrôles

Répéter sur préproduction; adapter la fenêtre à la migration et valider restauration avant l’intervention.

## 3. Production — Sécurité

- Ne pas rétrograder le paquet seul après migration de schéma.
- Conserver backup cohérent avec secrets et configuration.
- Arrêter si une migration est incomplète ou un plan de montée absent.

## Validation et retour arrière

- **Validation** : Version cible, contrôles et opérations Git passent après changement.
- **Retour arrière** : Restaurer une instance complète depuis une sauvegarde compatible; un simple downgrade n’est pas un rollback sûr.

## Si le problème n'est pas résolu

- [GitLab — installation paquet](https://docs.gitlab.com/install/package/)
- [GitLab — configuration Omnibus](https://docs.gitlab.com/omnibus/settings/)
- [GitLab — backup/restore](https://docs.gitlab.com/omnibus/backup-restore/)
- [Fiche connexe](<Fiche_Simple_-_VM_Debian_13_GitLab_CE_Prerequis_Limites.md>)
