# Fiche_Simple_-_Hote_Docker_Securite_Hardening_Reduire_Privileges.md

- **Environnement** : Hôte Linux dédié exécutant Docker Engine et des stacks Compose
- **OS / Version** : Distribution Linux maintenue; Docker Engine supporté
- **Catégorie** : docker / durcissement

---

## Problème précis à résoudre

Limiter ce qu'un conteneur peut faire sur l'hôte.

## 1. Hors-Production (Lab / Test / POC)

1. Tester un conteneur restreint (image d'exemple `alpine`, à remplacer par la vôtre) :
   ```bash
   docker run --rm --user 1000:1000 --cap-drop ALL --security-opt no-new-privileges --read-only --tmpfs /tmp alpine id
   ```
   👉 Explication : UID non-root, aucune capacité Linux, pas d'élévation et système de fichiers en lecture seule avec `/tmp` explicite.

2. Dans Compose, appliquer les équivalents `user`, `cap_drop`, `security_opt: [no-new-privileges:true]` et `read_only`, un service à la fois.
   👉 Explication : chaque option peut casser une application : on teste séparément.

3. Rechercher les conteneurs privilégiés :
   ```bash
   docker ps -q | xargs -r docker inspect --format '{{.Name}} privileged={{.HostConfig.Privileged}}'
   ```
   👉 Explication : liste les conteneurs avec `privileged=true` à justifier ou supprimer.

## 2. Production — Contrôles

Documenter toute exception (`privileged`, périphériques, montages sensibles).

## 3. Production — Sécurité

- Éviter `privileged: true` et les montages de `/`, `/var/run/docker.sock`, `/proc`, `/sys`.
- Ne pas imposer toutes les options en bloc sans test.

## Validation et retour arrière

- **Validation** : Le service démarre avec les restrictions et fonctionne.
- **Retour arrière** : Retirer l'option qui bloque le service puis redéployer.

## Si le problème n'est pas résolu

- [Docker — sécurité du moteur](https://docs.docker.com/engine/security/)
- [Docker — bonnes pratiques de build](https://docs.docker.com/build/building/best-practices/)
- [Guide complet — 2. Réduire les privilèges des conteneurs](/02-fiches-completes/transverses/docker/autres/32-hardening-hote-docker-production#2-reduire-les-privileges-des-conteneurs)