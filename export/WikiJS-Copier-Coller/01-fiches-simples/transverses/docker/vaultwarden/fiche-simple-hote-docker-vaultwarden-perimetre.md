# Fiche_Simple_-_Hote_Docker_Vaultwarden_Perimetre.md

- **Environnement** : Hôte Linux avec Docker Engine et plugin Compose, Vaultwarden SQLite derrière un reverse proxy HTTPS
- **OS / Version** : Hôte Linux + Docker; image vaultwarden/server (tag à figer après validation)
- **Catégorie** : gestionnaire de mots de passe auto-hébergé

---

## Problème précis à résoudre

Confirmer que Vaultwarden (serveur communautaire) est le bon choix et que les prérequis Docker, DNS et HTTPS sont réunis.

## 1. Hors-Production (Lab / Test / POC)

1. Décider explicitement du choix : Vaultwarden est communautaire, pas le produit officiel Bitwarden.
   👉 Explication : support, licence et politique de mise à jour doivent être validés par la sécurité.

2. Vérifier Docker et le plugin Compose :
   ```bash
   docker --version
   docker compose version
   ```
   👉 Explication : le déploiement utilise `docker compose`.

3. Vérifier que le nom DNS dédié existe (remplacer `vault.example.net` par le vrai nom) :
   ```bash
   getent hosts vault.example.net
   ```
   👉 Explication : le reverse proxy HTTPS a besoin de ce nom.

4. Prévoir un reverse proxy HTTPS (par exemple Traefik) devant le conteneur.
   👉 Explication : l'interface web utilise des API de chiffrement du navigateur qui exigent un contexte sécurisé.

## 2. Production — Contrôles

Valider le périmètre : SQLite uniquement, sans SSO ni conformité particulière. Hôte Docker durci au préalable.

## 3. Production — Sécurité

- Ne pas exposer le conteneur directement sur Internet sans HTTPS.
- Faire valider le choix communautaire par la sécurité.

## Validation et retour arrière

- **Validation** : Docker répond, le DNS résout, le reverse proxy HTTPS est prévu.
- **Retour arrière** : Aucune modification : rien à annuler.

## Si le problème n'est pas résolu

- [Vaultwarden — Using Docker Compose](https://github.com/dani-garcia/vaultwarden/wiki/Using-Docker-Compose)
- [Vaultwarden — Backing up your vault](https://github.com/dani-garcia/vaultwarden/wiki/Backing-up-your-vault)
- [Guide complet — périmètre et distinction avec Bitwarden](/02-fiches-completes/transverses/docker/installation-deploiement/94-deploiement-vaultwarden-docker-compose#1-perimetre-et-distinction-avec-bitwarden)