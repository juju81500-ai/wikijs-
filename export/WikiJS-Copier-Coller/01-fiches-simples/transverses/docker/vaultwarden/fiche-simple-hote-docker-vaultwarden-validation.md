# Fiche_Simple_-_Hote_Docker_Vaultwarden_Validation.md

- **Environnement** : Hôte Linux avec Docker Engine et plugin Compose, Vaultwarden SQLite derrière un reverse proxy HTTPS
- **OS / Version** : Hôte Linux + Docker; image vaultwarden/server (tag à figer après validation)
- **Catégorie** : gestionnaire de mots de passe auto-hébergé

---

## Problème précis à résoudre

Contrôler que le service est joignable en HTTPS, fermé aux tiers et restaurable.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler le conteneur :
   ```bash
   docker compose ps
   docker compose logs --tail 50
   ```
   👉 Explication : le conteneur doit tourner et les journaux ne montrent pas d'erreur.

2. Tester l'accès HTTPS (remplacer le domaine) :
   ```bash
   curl -I https://vault.example.net
   ```
   👉 Explication : une réponse HTTP valide confirme le reverse proxy et le certificat.

3. Depuis un autre hôte, tester l'accès direct au port 11001 (remplacer `192.0.2.10` par l'IP de l'hôte) :
   ```bash
   curl -m 5 http://192.0.2.10:11001
   ```
   👉 Explication : la connexion doit échouer : le port n'est ouvert que sur la boucle locale.

4. Avec un client Bitwarden, se connecter au serveur personnalisé, créer, modifier et lire un élément de test.
   👉 Explication : on valide le fonctionnement de bout en bout.

5. Vérifier que l'inscription est refusée et que `/admin` est refusé sans bon jeton ou désactivé.
   👉 Explication : on confirme la fermeture des accès sensibles.

## 2. Production — Contrôles

Archiver le résultat de la recette et la version déployée.

## 3. Production — Sécurité

- Ne pas valider tant que `/admin` ou les inscriptions sont accessibles.
- Contrôler qu'aucun port n'est publié sur toutes les interfaces.

## Validation et retour arrière

- **Validation** : Tous les contrôles ci-dessus sont conformes et une restauration a été testée.
- **Retour arrière** : Reprendre l'étape fautive; si besoin `docker compose down` puis restaurer la sauvegarde.

## Si le problème n'est pas résolu

- [Vaultwarden — Using Docker Compose](https://github.com/dani-garcia/vaultwarden/wiki/Using-Docker-Compose)
- [Vaultwarden — Backing up your vault](https://github.com/dani-garcia/vaultwarden/wiki/Backing-up-your-vault)
- [Guide complet — validation](/02-fiches-completes/transverses/docker/installation-deploiement/94-deploiement-vaultwarden-docker-compose#7-validation)