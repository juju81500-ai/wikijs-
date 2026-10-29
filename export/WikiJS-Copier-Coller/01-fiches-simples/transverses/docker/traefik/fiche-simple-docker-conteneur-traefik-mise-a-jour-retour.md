# Fiche_Simple_-_Docker_Conteneur_Traefik_Mise_A_Jour_Retour.md

- **Environnement** : Hôte Docker Linux dédié ou contrôlé
- **OS / Version** : Linux avec Docker Engine et Compose; version Traefik maintenue (3.x)
- **Catégorie** : reverse proxy / maintenance

---

## Problème précis à résoudre

Mettre à niveau Traefik avec un retour arrière sûr.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder configuration et stockage ACME :
   ```bash
   cp -a acme.json acme.json.sauvegarde
   cp -a compose.yaml compose.yaml.sauvegarde
   ```
   👉 Explication : copies à stocker aussi hors de l'hôte.

2. Passer à la version suivante dans `compose.yaml` (une seule à la fois) après lecture des changements incompatibles, puis :
   ```bash
   docker compose pull
   docker compose up -d
   ```
   👉 Explication : applique la nouvelle image.

3. Contrôler les journaux :
   ```bash
   docker compose logs --tail 100 traefik
   ```
   👉 Explication : vérifie l'absence d'erreur.

4. En cas d'échec, restaurer l'ancien `compose.yaml` et redéployer :
   ```bash
   cp compose.yaml.sauvegarde compose.yaml
   docker compose up -d
   ```
   👉 Explication : retour à l'image et à la configuration précédentes.

## 2. Production — Contrôles

Valider la restauration de la sauvegarde.

## 3. Production — Sécurité

- Ne pas effacer `acme.json` pour résoudre un simple problème de routage.

## Validation et retour arrière

- **Validation** : La nouvelle version route correctement.
- **Retour arrière** : Utiliser l'ancien `compose.yaml` et l'ancienne image.

## Si le problème n'est pas résolu

- [Traefik — documentation officielle](https://doc.traefik.io/traefik/)
- [Traefik — ACME / Let's Encrypt](https://doc.traefik.io/traefik/https/acme/)
- [Guide complet — 5. Mise à jour et retour arrière](/02-fiches-completes/transverses/docker/installation-deploiement/06-reverse-proxy-traefik-v31-letsencrypt-docker#5-mise-a-jour-et-retour-arriere)