# Hardening d'un hôte Docker en production

- **Type de fiche** : Autres — sécurité / exploitation
- **Environnement** : Hôte Linux dédié exécutant Docker Engine et des stacks Compose
- **OS / Version** : Distribution Linux maintenue; Docker Engine supporté par l'éditeur de la distribution
- **Rôle** : Réduire les risques d'escalade, d'exposition réseau et de perte de données liés aux conteneurs

## 1. Inventorier et protéger le plan de contrôle

Fiche simple : [inventorier et protéger le plan de contrôle](/01-fiches-simples/transverses/docker/securite/fiche-simple-hote-docker-securite-hardening-inventaire-plan-controle).

Le socket Docker donne un contrôle privilégié de l'hôte. Ne jamais le monter dans une application ordinaire; éviter son exposition TCP, et limiter l'accès au groupe `docker` comme un accès root.

```bash
docker version
docker info
docker ps --no-trunc
ss -lntup
```

Inventorier les utilisateurs autorisés, ports publiés, volumes, images, réseaux, extensions et tâches de maintenance. Utiliser un compte d'administration nominatif et une console de secours.

## 2. Réduire les privilèges des conteneurs

Fiche simple : [réduire les privilèges des conteneurs](/01-fiches-simples/transverses/docker/securite/fiche-simple-hote-docker-securite-hardening-reduire-privileges).

Pour chaque service, exécuter sous un UID non-root lorsque l'image le permet, retirer les capacités Linux non nécessaires, activer `no-new-privileges`, appliquer un profil seccomp/AppArmor, et ajouter `read_only` uniquement si l'application fonctionne avec des répertoires temporaires explicites.

Éviter `privileged: true`, les montages de `/`, `/var/run/docker.sock`, `/proc` ou `/sys` et les périphériques hôte sans justification documentée. Ne pas imposer ces options en bloc sans vérifier le comportement du service.

## 3. Maîtriser les images et les mises à jour

Fiche simple : [maîtriser les images et les mises à jour](/01-fiches-simples/transverses/docker/securite/fiche-simple-hote-docker-securite-hardening-images-mises-a-jour).

- Utiliser des images officielles ou provenant d'un registre approuvé; épingler une version ou un digest validé.
- Scanner les images, vérifier provenance et notes de version, puis reconstruire/redéployer via une fenêtre contrôlée.
- Éviter les mises à jour automatiques non supervisées pour les services critiques; maintenir un retour arrière avec images/configuration antérieures.
- Ne pas placer les secrets dans l'image, les labels, le dépôt Compose ou les logs; utiliser Docker secrets ou le coffre de la plateforme.

## 4. Segmenter les réseaux et protéger les données

Fiche simple : [segmenter les réseaux et protéger les données](/01-fiches-simples/transverses/docker/securite/fiche-simple-hote-docker-securite-hardening-segmentation-donnees).

Exposer uniquement les ports indispensables via le pare-feu ou le reverse proxy. Ne pas publier les ports de bases de données ou d'administration sur toutes les interfaces. Séparer réseau frontal, applicatif et stockage selon le besoin; ne pas considérer un réseau Docker comme une frontière suffisante contre un hôte compromis.

Utiliser des volumes nommés ou des bind mounts explicitement protégés. Sauvegarder les données applicatives de manière cohérente, y compris les bases avec leurs outils dédiés; tester la restauration indépendamment de la sauvegarde de l'hôte.

## 5. Limiter les ressources et journaux

Fiche simple : [limiter les ressources et les journaux](/01-fiches-simples/transverses/docker/securite/fiche-simple-hote-docker-securite-hardening-ressources-journaux).

Définir des plafonds CPU/mémoire adaptés aux services et une politique de rotation des logs Docker. Superviser l'espace de `/var/lib/docker`, les erreurs de stockage, les redémarrages et les ports exposés. Ne pas lancer `docker system prune --volumes` sur un hôte de production sans inventaire et validation explicite.

## 6. Vérifier et exploiter

Fiche simple : [vérifier et exploiter](/01-fiches-simples/transverses/docker/securite/fiche-simple-hote-docker-securite-hardening-verifier-exploiter).

```bash
docker compose config --quiet
docker compose ps
docker inspect <CONTENEUR>
docker system df
```

Conserver les exports d'inventaire et les changements de configuration. Après une mise à jour, tester connectivité, santé applicative, persistance, sauvegarde et redémarrage.

## 7. Réponse à incident

Fiche simple : [répondre à un incident](/01-fiches-simples/transverses/docker/securite/fiche-simple-hote-docker-securite-hardening-reponse-incident).

En cas d'accès suspect au socket ou de conteneur compromis, isoler l'hôte du réseau sans détruire les artefacts, préserver journaux et métadonnées, révoquer les secrets exposés, puis reconstruire depuis des images et sauvegardes vérifiées. Ne pas supposer qu'un redémarrage a supprimé la compromission.

## Sources

- [Docker — Sécurité du moteur](https://docs.docker.com/engine/security/)
- [Docker — Bonnes pratiques de build](https://docs.docker.com/build/building/best-practices/)
- [Docker — Secrets Compose](https://docs.docker.com/compose/how-tos/use-secrets/)
- [Docker — Stockage et volumes](https://docs.docker.com/engine/storage/volumes/)