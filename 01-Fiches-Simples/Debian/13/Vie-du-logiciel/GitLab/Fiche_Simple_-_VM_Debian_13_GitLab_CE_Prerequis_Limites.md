# Fiche_Simple_-_VM_Debian_13_GitLab_CE_Prerequis_Limites

- **Environnement** : VM Debian 13 de préproduction; FQDN et ressources confirmés
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : forge Git / administration
- **Tags** : `debian13`, `gitlab-ce`, `forge-git`, `tls`, `sauvegarde`
---

## Problème précis à résoudre

Établir support Debian 13, ressources, FQDN, ports, sauvegardes et palier GitLab avant installation.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier OS, mémoire, stockage et ports
   ```bash
   cat /etc/os-release
   free -h
   df -h /var/opt /var/log
   sudo ss -lntp | grep -E ":(22|80|443)\b" || true
   ```
   👉 Explication : GitLab consomme des ressources importantes; comparer au dimensionnement officiel.

2. Confirmer la matrice officielle GitLab
   ```text
   Navigateur > ouvrir la documentation officielle : https://docs.gitlab.com/install/package/
   ```
   👉 Explication : si la matrice ne confirme pas Debian 13 et cette version, arrêter. Détail à confirmer dans la documentation officielle avant application : Vérifier dans la documentation officielle que Debian 13, l’architecture, l’édition CE et la version cible sont supportées. Version cible 18.X.Y-ce.0 : à remplacer après validation.

3. Définir DNS et accès réseau
   ```text
   Navigateur > ouvrir la documentation officielle : https://docs.gitlab.com/install/package/
   ```
   👉 Explication : ne pas exposer une instance non configurée. Détail à confirmer dans la documentation officielle avant application : Documenter FQDN, terminaison TLS, ports Web/SSH, réseaux clients et chemin de secours.

## 2. Production — Contrôles

Valider ressources, version prise en charge, édition, domaine, ports, stockage et procédure de reprise avant le changement.

## 3. Production — Sécurité

- Ne jamais improviser le chemin de mise à niveau GitLab.
- Protéger gitlab.rb, gitlab-secrets.json et les sauvegardes.
- Isoler le serveur et limiter les accès administrateurs.

## Validation et retour arrière

- **Validation** : La matrice confirme explicitement l’OS/version et le plan de capacité est approuvé.
- **Retour arrière** : Reporter si le support Debian 13 ou le chemin versionné n’est pas attesté.

## Si le problème n'est pas résolu

- [GitLab — installation paquet](https://docs.gitlab.com/install/package/)
- [GitLab — configuration Omnibus](https://docs.gitlab.com/omnibus/settings/)
- [GitLab — backup/restore](https://docs.gitlab.com/omnibus/backup-restore/)
- [Fiche connexe](<Fiche_Simple_-_VM_Debian_13_GitLab_CE_Installer.md>)
