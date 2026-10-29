# Fiche_Simple_-_Hote_Docker_Securite_Hardening_Ressources_Journaux.md

- **Environnement** : Hôte Linux dédié exécutant Docker Engine et des stacks Compose
- **OS / Version** : Distribution Linux maintenue; Docker Engine supporté
- **Catégorie** : docker / exploitation
- **Tags** : `docker`, `hardening`, `securite`, `compose`, `production`

---

## Problème précis à résoudre

Éviter qu'un conteneur sature CPU, mémoire ou disque.

## 1. Hors-Production (Lab / Test / POC)

1. Tester des plafonds (exemple à adapter) :
   ```bash
   docker run -d --name test-limite --memory 256m --cpus 0.5 --log-opt max-size=10m --log-opt max-file=3 nginx:1.27
   ```
   👉 Explication : limite mémoire et CPU et fait tourner les logs.

2. Mesurer l'utilisation :
   ```bash
   docker stats --no-stream
   docker system df
   ```
   👉 Explication : vérifie la consommation et l'espace de `/var/lib/docker`.

3. Superviser espace disque, redémarrages et ports exposés.
   👉 Explication : détecte les dérives avant la panne.

## 2. Production — Contrôles

Définir les plafonds selon les mesures réelles.

## 3. Production — Sécurité

- Ne jamais lancer `docker system prune --volumes` en production sans inventaire et validation explicite.

## Validation et retour arrière

- **Validation** : Les limites sont visibles dans `docker inspect` et la rotation des logs est active.
- **Retour arrière** : Supprimer le conteneur de test : `docker rm -f test-limite`.

## Si le problème n'est pas résolu

- [Docker — sécurité du moteur](https://docs.docker.com/engine/security/)
- [Docker — bonnes pratiques de build](https://docs.docker.com/build/building/best-practices/)
- [Guide complet — 5. Limiter les ressources et journaux](../../../../02-Fiches-Completes/Transverses/Docker/Autres/32_Hardening_Hote_Docker_Production.md#5-limiter-les-ressources-et-journaux)
