---
title: "Fiche Simple - VM Debian 13 Caddy Configurer Proxy"
description: "Configurer un reverse proxy Caddy vers un service amont local après sauvegarde de la configuration."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "caddy", "reverse-proxy", "caddyfile", "https"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_Caddy_Configurer_Proxy.md

- **Environnement** : VM Debian 13, application amont de test approuvée
- **OS / Version** : Debian 13; Caddy stable
- **Catégorie** : serveur Web / reverse proxy
- **Tags** : `debian13`, `caddy`, `reverse-proxy`, `caddyfile`, `https`

---

## Problème précis à résoudre

Configurer un reverse proxy Caddy vers un service amont local après sauvegarde de la configuration.

## 1. Hors-Production (Lab / Test / POC)

1. Confirmer l'amont et sauvegarder le Caddyfile :
   ```bash
   sudo ss -ltnp | grep 127.0.0.1:8080
   sudo cp -a /etc/caddy/Caddyfile /etc/caddy/Caddyfile.pre-change
   ```
   👉 Explication : adapter adresse et port si besoin.

2. Écrire le Caddyfile (adapter nom et amont) :
   ```bash
   sudo tee /etc/caddy/Caddyfile >/dev/null <<'EOF'
   app.example.net {
       reverse_proxy 127.0.0.1:8080
   }
   EOF
   ```
   👉 Explication : Caddy obtient et renouvelle le certificat automatiquement si le nom et les challenges sont valides.

3. Valider puis recharger :
   ```bash
   sudo caddy validate --config /etc/caddy/Caddyfile --adapter caddyfile
   sudo systemctl reload caddy
   sudo systemctl --no-pager status caddy
   ```
   👉 Explication : ne pas recharger si la validation échoue; n'ouvrir que les ports entrants nécessaires.

## 2. Production — Contrôles

Faire valider FQDN, routage, amont, DNS, en-têtes transmis, limites de requêtes et dépendances par les propriétaires réseau et applicatif.

## 3. Production — Sécurité

- Ne jamais pointer un nom de production vers un service de test.
- Isoler l'amont et filtrer ses accès directs depuis les réseaux non autorisés.
- Ne pas modifier le Caddyfile sans sauvegarde et validation syntaxique.
- Protéger journaux et configuration; ne pas stocker de secrets dans le Caddyfile.

## Validation et retour arrière

- **Validation** : `caddy validate` réussit, Caddy est sain et l'amont pilote répond via le nom attendu.
- **Retour arrière** : restaurer le Caddyfile sauvegardé, valider, puis recharger; vérifier le service.

## Si le problème n'est pas résolu

- [Caddy — reverse_proxy](https://caddyserver.com/docs/caddyfile/directives/reverse_proxy)
- [Caddy — commande validate](https://caddyserver.com/docs/command-line#caddy-validate)
- [Guide complet Caddy Debian 13](/02-fiches-completes/debian/13/installation-deploiement/91-deploiement-caddy-debian-13#3-configurer-un-reverse-proxy-local)