# Fiche_Simple_-_VM_Debian_13_GitLab_CE_Configurer

- **Environnement** : VM Debian 13 de préproduction; FQDN et ressources confirmés
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : forge Git / administration
- **Tags** : `debian13`, `gitlab-ce`, `forge-git`, `tls`, `sauvegarde`
---

## Problème précis à résoudre

Configurer URL, paramètres Omnibus et premier compte administrateur nominatif.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder puis modifier le fichier Omnibus
   ```bash
   sudo cp -a /etc/gitlab/gitlab.rb /etc/gitlab/gitlab.rb.before
   sudoedit /etc/gitlab/gitlab.rb
   ```
   👉 Explication : protéger la copie; elle peut contenir des paramètres sensibles.

2. Définir la URL HTTPS canonique
   ```ruby
   external_url "https://gitlab.example.com"
   ```
   👉 Explication : remplacer le FQDN par le nom à remplacer; une terminaison proxy doit être configurée sans double TLS.

3. Appliquer et contrôler la configuration
   ```bash
   sudo gitlab-ctl reconfigure
   sudo gitlab-ctl status
   ```
   👉 Explication : analyser les erreurs de génération avant toute exposition réseau.

4. Créer compte nominatif et activer MFA
   ```text
   Navigateur > ouvrir la documentation officielle : https://docs.gitlab.com/install/package/
   ```
   👉 Explication : ne pas saisir de mot de passe ou secret dans un terminal ni dans ce guide. Détail à confirmer dans la documentation officielle avant application : Ouvrir https://gitlab.example.com depuis le réseau d’administration. Créer un compte nominatif et activer MFA dans les paramètres.

## 2. Production — Contrôles

Documenter réglages Omnibus, comptes, rôles, inscription, projets et sauvegarde avant ouverture aux équipes.

## 3. Production — Sécurité

- Restreindre les fichiers de configuration et secrets.
- Désactiver ou limiter l’inscription selon la politique.
- N’utiliser ni compte partagé ni token dans une URL ou un dépôt.

## Validation et retour arrière

- **Validation** : URL canonique répond et le compte administrateur autorisé se connecte avec MFA.
- **Retour arrière** : Restaurer le fichier précédent puis reconfigurer; traiter séparément toute migration de base.

## Si le problème n'est pas résolu

- [GitLab — installation paquet](https://docs.gitlab.com/install/package/)
- [GitLab — configuration Omnibus](https://docs.gitlab.com/omnibus/settings/)
- [GitLab — backup/restore](https://docs.gitlab.com/omnibus/backup-restore/)
- [Fiche connexe](<Fiche_Simple_-_VM_Debian_13_GitLab_CE_Prerequis_Limites.md>)
