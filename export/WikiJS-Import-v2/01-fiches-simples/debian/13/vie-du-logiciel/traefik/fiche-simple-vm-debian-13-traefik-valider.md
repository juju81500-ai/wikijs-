---
title: "Fiche Simple - VM Debian 13 Traefik Valider"
description: "Prouver que Traefik route correctement, présente un certificat valide et résiste au redémarrage."
published: true
date: 2026-10-29T20:33:54Z
tags: ["debian13", "traefik", "recette"]
editor: markdown
dateCreated: 2026-10-29T20:33:54Z
dateModified: 2026-10-29T20:33:54Z
---

# Fiche_Simple_-_VM_Debian_13_Traefik_Valider

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; Traefik v3 (binaire officiel)
- **Catégorie** : reverse proxy / Traefik / Valider (recette)
- **Tags** : `debian13`, `traefik`, `recette`

---

## Problème précis à résoudre

Prouver que Traefik route correctement, présente un certificat valide et résiste au redémarrage.

## 1. Hors-Production (Lab / Test / POC)

1. État du service et ports :
   ```bash
   systemctl is-active traefik
   sudo ss -tlnp | grep traefik
   ```
   👉 Explication : écoute sur 80 et 443 uniquement.

2. Tester HTTP, redirection et HTTPS :
   ```bash
   curl -sI http://APP.example.net/ | head -3
   curl -sI https://APP.example.net/ | head -5
   ```
   👉 Explication : `301` puis `200` attendus.

3. Contrôler le certificat :
   ```bash
   echo | openssl s_client -connect APP.example.net:443 -servername APP.example.net 2>/dev/null | openssl x509 -noout -subject -issuer -dates
   ```
   👉 Explication : vérifier sujet, émetteur et échéance.

4. Tester un redémarrage :
   ```bash
   sudo systemctl restart traefik
   sleep 3; curl -s -o /dev/null -w '%{http_code}\n' https://APP.example.net/
   ```
   👉 Explication : le service revient sans intervention.

## 2. Production — Contrôles

Conserver la preuve (date, version, résultats) et superviser le certificat et le code HTTP.

## 3. Production — Sécurité

- Pas de certificat de préproduction en production.
- Ne pas exposer les journaux.
- Vérifier l'absence de routeur imprévu.

## Validation et retour arrière

- **Validation** : tous les contrôles réussis.
- **Retour arrière** : restaurer la configuration sauvegardée et redémarrer.

## Si le problème n'est pas résolu

- [Traefik — Prérequis et limites](/01-fiches-simples/debian/13/vie-du-logiciel/traefik/fiche-simple-vm-debian-13-traefik-prerequis-limites)
- [Traefik — Installer](/01-fiches-simples/debian/13/vie-du-logiciel/traefik/fiche-simple-vm-debian-13-traefik-installer)
- [Traefik — Configurer (statique, dynamique, premier service)](/01-fiches-simples/debian/13/vie-du-logiciel/traefik/fiche-simple-vm-debian-13-traefik-configurer)
- [Traefik — Sécuriser (TLS, redirection, pare-feu)](/01-fiches-simples/debian/13/vie-du-logiciel/traefik/fiche-simple-vm-debian-13-traefik-securiser)
- [Traefik — Sauvegarder et restaurer](/01-fiches-simples/debian/13/vie-du-logiciel/traefik/fiche-simple-vm-debian-13-traefik-sauvegarder-restaurer)
- [Traefik — Mise à jour et retour arrière](/01-fiches-simples/debian/13/vie-du-logiciel/traefik/fiche-simple-vm-debian-13-traefik-mettre-a-jour)
- [Guide complet Traefik v3.1 et Let's Encrypt (variante Docker)](/02-fiches-completes/transverses/docker/installation-deploiement/06-reverse-proxy-traefik-v31-letsencrypt-docker)
- [Traefik — documentation officielle](https://doc.traefik.io/traefik/)
- [Série Traefik sous Docker](/01-fiches-simples/transverses/docker/traefik/fiche-simple-docker-conteneur-traefik-configuration-statique)