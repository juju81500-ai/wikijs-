# Fiche_Simple_-_VM_Debian_13_GitLab_CE_Securiser_TLS

- **Environnement** : VM Debian 13 de préproduction; FQDN et ressources confirmés
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : forge Git / administration

---

## Problème précis à résoudre

Configurer HTTPS, restrictions réseau et contrôles de compte avant exposition.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier ports et santé
   ```bash
   sudo ss -lntp
   sudo gitlab-ctl status
   ```
   👉 Explication : n’exposer que les ports du plan réseau.

2. Installer le certificat via le mode de terminaison approuvé
   ```text
   Navigateur > ouvrir la documentation officielle : https://docs.gitlab.com/install/package/
   ```
   👉 Explication : ne pas configurer deux terminaisons TLS non coordonnées; suivre le guide GitLab correspondant. Détail à confirmer dans la documentation officielle avant application : Confirmer si TLS termine dans Omnibus ou dans un reverse proxy. Configurer un certificat valide couvrant le FQDN et la redirection HTTP vers HTTPS.

3. Vérifier certificat et URL
   ```bash
   openssl s_client -connect gitlab.example.com:443 -servername gitlab.example.com </dev/null
   curl -I https://gitlab.example.com/
   ```
   👉 Explication : remplacer le FQDN à remplacer; contrôler chaîne, nom, expiration et redirection.

4. Appliquer les ACL validées
   ```text
   Navigateur > ouvrir la documentation officielle : https://docs.gitlab.com/install/package/
   ```
   👉 Explication : faire valider les règles par l’équipe réseau. Détail à confirmer dans la documentation officielle avant application : Autoriser HTTPS depuis les segments approuvés. Autoriser SSH Git uniquement si utilisé. Restreindre administration et ports de backend.

## 2. Production — Contrôles

Vérifier renouvellement TLS, MFA, accès anonyme, runners, ports, sauvegardes et tests d’accès refusé.

## 3. Production — Sécurité

- Forcer HTTPS et activer MFA.
- Ne pas exposer les interfaces internes ou backend.
- Ne pas exécuter de code non fiable dans un runner privilégié.

## Validation et retour arrière

- **Validation** : TLS est valide, l’instance est joignable depuis les segments voulus et refusée depuis les autres.
- **Retour arrière** : Rétablir proxy/certificat antérieurs; ne pas désactiver le contrôle TLS.

## Si le problème n'est pas résolu

- [GitLab — installation paquet](https://docs.gitlab.com/install/package/)
- [GitLab — configuration Omnibus](https://docs.gitlab.com/omnibus/settings/)
- [GitLab — backup/restore](https://docs.gitlab.com/omnibus/backup-restore/)
- [Fiche connexe](</01-fiches-simples/debian/13/vie-du-logiciel/gitlab/fiche-simple-vm-debian-13-gitlab-ce-prerequis-limites>)