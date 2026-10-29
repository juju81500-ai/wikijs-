# Fiche_Simple_-_Hote_Docker_Vaultwarden_Restaurer.md

- **Environnement** : Hôte Linux avec Docker Engine et plugin Compose, Vaultwarden SQLite derrière un reverse proxy HTTPS
- **OS / Version** : Hôte Linux + Docker; image vaultwarden/server (tag à figer après validation)
- **Catégorie** : gestionnaire de mots de passe auto-hébergé
- **Tags** : `docker`, `vaultwarden`, `restauration`

---

## Problème précis à résoudre

Vérifier qu'une sauvegarde est restaurable sans toucher à la production.

## 1. Hors-Production (Lab / Test / POC)

1. Sur un hôte ou réseau isolé, créer un nouveau répertoire et y copier la sauvegarde :
   ```bash
   mkdir -p /opt/vaultwarden-test/vw-data
   cp -a sauvegarde/. /opt/vaultwarden-test/vw-data/
   ```
   👉 Explication : `sauvegarde/` est un exemple de dossier à remplacer par l'emplacement réel de la sauvegarde.

2. Placer le même `compose.yaml` (même `DOMAIN`) dans `/opt/vaultwarden-test` puis démarrer :
   ```bash
   cd /opt/vaultwarden-test
   docker compose up -d
   ```
   👉 Explication : la configuration identique garantit un test réaliste.

3. Ajouter une entrée DNS de test et se connecter avec un compte de test.
   👉 Explication : on retrouve l'élément de test sans toucher à la production.

4. Si une restauration en production est nécessaire : arrêter le conteneur et conserver une copie de l'état actuel avant d'écraser `vw-data`.
   👉 Explication : on garde toujours un moyen de revenir en arrière.

## 2. Production — Contrôles

Planifier un test de restauration périodique et consigner le temps de reprise.

## 3. Production — Sécurité

- Ne jamais restaurer par-dessus `vw-data` de production sans arrêt du conteneur et copie préalable.
- Isoler l'hôte de test : il contient des données réelles.

## Validation et retour arrière

- **Validation** : Connexion réussie sur l'hôte de test et élément de test retrouvé.
- **Retour arrière** : Arrêter et supprimer l'environnement de test : `docker compose down` puis supprimer `/opt/vaultwarden-test`.

## Si le problème n'est pas résolu

- [Vaultwarden — Using Docker Compose](https://github.com/dani-garcia/vaultwarden/wiki/Using-Docker-Compose)
- [Vaultwarden — Backing up your vault](https://github.com/dani-garcia/vaultwarden/wiki/Backing-up-your-vault)
- [Guide complet — restaurer (test sur hôte isolé)](../../../../02-Fiches-Completes/Transverses/Docker/Installation-Deploiement/94_Deploiement_Vaultwarden_Docker_Compose.md#6-restaurer-test-sur-hote-isole)
