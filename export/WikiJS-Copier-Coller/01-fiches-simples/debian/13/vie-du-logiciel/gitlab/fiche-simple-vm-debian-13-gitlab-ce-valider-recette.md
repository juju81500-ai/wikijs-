# Fiche_Simple_-_VM_Debian_13_GitLab_CE_Valider_Recette

- **Environnement** : VM Debian 13 de préproduction; FQDN et ressources confirmés
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : forge Git / administration

---

## Problème précis à résoudre

Tester santé, clonage, permissions et logs avant ouverture.

## 1. Hors-Production (Lab / Test / POC)

1. Exécuter les contrôles GitLab
   ```bash
   sudo gitlab-ctl status
   sudo gitlab-rake gitlab:check SANITIZE=true
   ```
   👉 Explication : corréler le résultat avec la version GitLab installée.

2. Tester clone d’un projet privé pilote
   ```bash
   git ls-remote https://gitlab.example.com/GROUPE/PROJET.git
   ```
   👉 Explication : remplacer les champs à remplacer; ne pas intégrer de jeton dans l’URL.

3. Tester une identité sans rôle
   ```text
   Navigateur > ouvrir la documentation officielle : https://docs.gitlab.com/install/package/
   ```
   👉 Explication : ne pas tester avec des secrets ni dépôt de production. Détail à confirmer dans la documentation officielle avant application : Depuis une session de recette non autorisée, ouvrir le projet privé. Résultat attendu : accès refusé.

4. Contrôler logs et volumes
   ```bash
   sudo gitlab-ctl tail --lines 50
   df -h /var/opt/gitlab /var/log/gitlab
   ```
   👉 Explication : surveiller erreurs et capacité.

## 2. Production — Contrôles

Archiver version, comptes test, accès refusé, résultat des tests et validation métier/exploitation.

## 3. Production — Sécurité

- Ne pas activer de runner non isolé pour code non fiable.
- Supprimer les projets et comptes de recette ou les convertir selon le processus.
- Masquer identifiants dans les journaux.

## Validation et retour arrière

- **Validation** : Un compte autorisé clone, un compte non autorisé est bloqué et les contrôles de santé sont conformes.
- **Retour arrière** : Désactiver comptes de test et revenir à l’instantané pilote.

## Si le problème n'est pas résolu

- [GitLab — installation paquet](https://docs.gitlab.com/install/package/)
- [GitLab — configuration Omnibus](https://docs.gitlab.com/omnibus/settings/)
- [GitLab — backup/restore](https://docs.gitlab.com/omnibus/backup-restore/)
- [Fiche connexe](</01-fiches-simples/debian/13/vie-du-logiciel/gitlab/fiche-simple-vm-debian-13-gitlab-ce-prerequis-limites>)