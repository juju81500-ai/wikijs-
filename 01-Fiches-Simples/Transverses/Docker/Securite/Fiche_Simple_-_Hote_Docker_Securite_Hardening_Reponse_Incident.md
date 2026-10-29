# Fiche_Simple_-_Hote_Docker_Securite_Hardening_Reponse_Incident.md

- **Environnement** : Hôte Linux dédié exécutant Docker Engine et des stacks Compose
- **OS / Version** : Distribution Linux maintenue; Docker Engine supporté
- **Catégorie** : docker / incident
- **Tags** : `docker`, `hardening`, `securite`, `compose`, `production`

---

## Problème précis à résoudre

Réagir à un conteneur compromis ou à un accès suspect au socket.

## 1. Hors-Production (Lab / Test / POC)

1. Isoler l'hôte du réseau sans l'éteindre, par la console ou le pare-feu de l'infrastructure.
   👉 Explication : préserve les artefacts utiles à l'analyse.

2. Préserver les journaux et métadonnées (remplacer `mon-conteneur`) :
   ```bash
   docker ps -a --no-trunc > incident-conteneurs.txt
   docker logs --timestamps mon-conteneur > incident-logs.txt 2>&1
   ```
   👉 Explication : conserve l'état pour l'enquête.

3. Révoquer les secrets exposés (mots de passe, jetons, clés).
   👉 Explication : on suppose qu'ils sont compromis.

4. Reconstruire depuis des images et sauvegardes vérifiées.
   👉 Explication : un redémarrage ne supprime pas une compromission.

## 2. Production — Contrôles

Prévenir le responsable sécurité et suivre le plan de réponse à incident.

## 3. Production — Sécurité

- Ne pas détruire les preuves avant analyse.
- Stocker les exports d'incident en accès restreint.

## Validation et retour arrière

- **Validation** : Hôte reconstruit, secrets renouvelés, accès contrôlés.
- **Retour arrière** : Restaurer depuis les sauvegardes vérifiées, jamais depuis l'hôte compromis.

## Si le problème n'est pas résolu

- [Docker — sécurité du moteur](https://docs.docker.com/engine/security/)
- [Docker — bonnes pratiques de build](https://docs.docker.com/build/building/best-practices/)
- [Guide complet — 7. Réponse à incident](../../../../02-Fiches-Completes/Transverses/Docker/Autres/32_Hardening_Hote_Docker_Production.md#7-reponse-a-incident)
