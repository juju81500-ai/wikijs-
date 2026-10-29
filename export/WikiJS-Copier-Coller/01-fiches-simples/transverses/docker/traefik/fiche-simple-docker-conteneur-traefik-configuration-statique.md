# Fiche_Simple_-_Docker_Conteneur_Traefik_Configuration_Statique.md

- **Environnement** : Hôte Docker Linux dédié ou contrôlé
- **OS / Version** : Linux avec Docker Engine et Compose; version Traefik maintenue (3.x)
- **Catégorie** : reverse proxy / configuration

---

## Problème précis à résoudre

Préparer la configuration de départ de Traefik dans Compose.

## 1. Hors-Production (Lab / Test / POC)

1. Épingler une version maintenue de Traefik dans `compose.yaml` (publier uniquement 80 et 443, réseaux dédiés, journaux, resolver ACME).
   👉 Explication : évite les surprises d'une version flottante.

2. Valider la syntaxe :
   ```bash
   docker compose config --quiet
   ```
   👉 Explication : aucune sortie signifie fichier valide.

3. Télécharger l'image :
   ```bash
   docker compose pull
   ```
   👉 Explication : prépare le démarrage.

4. Garder identifiants DNS et secrets ACME hors dépôt, labels et journaux.
   👉 Explication : évite leur fuite.

## 2. Production — Contrôles

Ne pas copier une configuration 3.1 sans vérifier la compatibilité avec la version retenue.

## 3. Production — Sécurité

- Secrets ACME et identifiants DNS jamais dans le dépôt, les labels ou les logs.

## Validation et retour arrière

- **Validation** : `docker compose config --quiet` ne retourne aucune erreur.
- **Retour arrière** : Restaurer la version précédente du fichier Compose.

## Si le problème n'est pas résolu

- [Traefik — documentation officielle](https://doc.traefik.io/traefik/)
- [Traefik — ACME / Let's Encrypt](https://doc.traefik.io/traefik/https/acme/)
- [Guide complet — 2. Configuration statique de départ](/02-fiches-completes/transverses/docker/installation-deploiement/06-reverse-proxy-traefik-v31-letsencrypt-docker#2-configuration-statique-de-depart)