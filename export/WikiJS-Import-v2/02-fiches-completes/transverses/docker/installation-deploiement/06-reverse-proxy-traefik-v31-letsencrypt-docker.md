---
title: "Reverse proxy Traefik et certificats ACME avec Docker"
description: "Fiche simple : [préparer DNS et exposition](../../../../01-Fiches-Simples/Transverses/Docker/Traefik/FicheSimple-DockerConteneurTraefikPreparerDNS.md)."
published: true
date: 2026-10-29T19:41:42Z
tags: ["traefik", "docker", "reverse-proxy", "acme", "tls"]
editor: markdown
dateCreated: 2026-10-29T19:41:42Z
dateModified: 2026-10-29T19:41:42Z
---

# Reverse proxy Traefik et certificats ACME avec Docker

- **Environnement** : Hôte Docker Linux dédié ou contrôlé
- **Version** : le nom historique mentionne Traefik 3.1 ; vérifier son statut de support et privilégier une version maintenue
- **Tags** : `traefik`, `docker`, `reverse-proxy`, `acme`, `tls`

## 1. Préparer DNS et exposition

Fiche simple : [préparer DNS et exposition](/01-fiches-simples/transverses/docker/traefik/fiche-simple-docker-conteneur-traefik-preparer-dns).

Définir les noms DNS, les adresses publiques, les ports entrants 80/443 et le mécanisme de renouvellement ACME. Vérifier que les enregistrements A/AAAA correspondent réellement à l'hôte. Protéger la clé ACME et conserver `acme.json` sur un stockage persistant, sauvegardé et lisible uniquement par le compte requis.

Ne pas exposer le tableau de bord sans authentification et filtrage. L'accès brut au socket Docker donne des privilèges équivalents à root : préférer un fournisseur de configuration maîtrisé ou un proxy de socket restreint.

## 2. Configuration statique de départ

Fiche simple : [poser la configuration statique](/01-fiches-simples/transverses/docker/traefik/fiche-simple-docker-conteneur-traefik-configuration-statique).

Épingler une version maintenue de Traefik dans Compose. Publier uniquement 80/443, créer des réseaux Docker dédiés, activer les journaux et déclarer les resolvers ACME selon les exigences du fournisseur. Ne pas copier une configuration v3.1 sans vérifier la compatibilité avec la version retenue.

Avant le démarrage :

```bash
docker compose config --quiet
docker compose pull
```

Les secrets ACME et identifiants DNS ne doivent pas apparaître dans le dépôt, les labels publics ou les journaux.

## 3. Déployer un premier service

Fiche simple : [déployer un premier service](/01-fiches-simples/transverses/docker/traefik/fiche-simple-docker-conteneur-traefik-premier-service).

Commencer avec une application de test non sensible. Ajouter un routeur HTTPS, un service, un middleware de redirection HTTP vers HTTPS et une politique de sécurité appropriée. Les labels de l'application doivent désigner le réseau et le resolver corrects.

```bash
docker compose up -d
docker compose ps
docker compose logs --tail 100 traefik
```

## 4. Vérifications et exploitation

Fiche simple : [vérifier et exploiter](/01-fiches-simples/transverses/docker/traefik/fiche-simple-docker-conteneur-traefik-verifier-exploiter).

- Vérifier la réponse HTTPS, le nom du certificat, sa chaîne et son expiration.
- Confirmer que le port du tableau de bord n'est pas publié sur l'interface publique.
- Tester le renouvellement ACME en environnement de staging avant la production.
- Surveiller les erreurs de résolution DNS, les limites de requêtes ACME et la capacité du stockage persistant.

## 5. Mise à jour et retour arrière

Fiche simple : [mettre à jour et revenir en arrière](/01-fiches-simples/transverses/docker/traefik/fiche-simple-docker-conteneur-traefik-mise-a-jour-retour).

Sauvegarder la configuration et le stockage ACME, puis valider la restauration. Mettre à niveau une version à la fois après lecture des changements incompatibles. En cas d'échec, revenir à l'image et à la configuration précédentes ; ne pas effacer `acme.json` pour résoudre un simple problème de routage.