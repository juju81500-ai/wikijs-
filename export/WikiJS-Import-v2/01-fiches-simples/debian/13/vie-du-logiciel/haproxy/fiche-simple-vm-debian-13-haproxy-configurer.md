---
title: "Fiche Simple - VM Debian 13 HAProxy Configurer"
description: "Écrire une configuration HAProxy minimale répartissant le trafic HTTP sur deux backends avec contrôle de santé."
published: true
date: 2026-10-29T20:34:00Z
tags: ["debian13", "haproxy", "configuration"]
editor: markdown
dateCreated: 2026-10-29T20:34:00Z
dateModified: 2026-10-29T20:34:00Z
---

# Fiche_Simple_-_VM_Debian_13_HAProxy_Configurer

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; HAProxy des dépôts Debian
- **Catégorie** : répartiteur de charge / HAProxy / Configurer un frontend et des backends
- **Tags** : `debian13`, `haproxy`, `configuration`

---

## Problème précis à résoudre

Écrire une configuration HAProxy minimale répartissant le trafic HTTP sur deux backends avec contrôle de santé.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder la configuration d'origine :
   ```bash
   sudo cp -a /etc/haproxy/haproxy.cfg /etc/haproxy/haproxy.cfg.orig
   ```
   👉 Explication : point de retour.

2. Ajouter frontend et backend :
   ```bash
   sudo tee -a /etc/haproxy/haproxy.cfg >/dev/null <<'EOF'

   frontend fe_http
       bind *:80
       mode http
       option forwardfor
       default_backend be_app

   backend be_app
       mode http
       balance roundrobin
       option httpchk GET /
       http-check expect status 200
       server app1 IP_APP1:PORT_APP check
       server app2 IP_APP2:PORT_APP check
   EOF
   ```
   👉 Explication : remplacer `IP_APP1`, `IP_APP2` et `PORT_APP` (à remplacer) ; les sections `global` et `defaults` de Debian sont conservées.

3. Valider puis recharger :
   ```bash
   sudo haproxy -c -f /etc/haproxy/haproxy.cfg && sudo systemctl reload haproxy
   ```
   👉 Explication : le rechargement n'interrompt pas les connexions en cours.

4. Ajouter une page de statistiques limitée à l'administration :
   ```bash
   sudo tee -a /etc/haproxy/haproxy.cfg >/dev/null <<'EOF'

   listen stats
       bind 127.0.0.1:8404
       mode http
       stats enable
       stats uri /stats
       stats refresh 10s
   EOF
   sudo haproxy -c -f /etc/haproxy/haproxy.cfg && sudo systemctl reload haproxy
   ```
   👉 Explication : liée à loopback ; y accéder par tunnel SSH, jamais directement exposée.

## 2. Production — Contrôles

Configuration versionnée, relue, validée par `haproxy -c` et testée sur pilote avant chaque changement.

## 3. Production — Sécurité

- Écoute des statistiques limitée à `127.0.0.1` ou à un réseau d'administration.
- Ne pas inscrire de mot de passe dans le fichier : utiliser un compte dédié à faible privilège si l'authentification des stats est requise.
- Toujours valider avant `reload`.

## Validation et retour arrière

- **Validation** : `curl -I http://127.0.0.1/` atteint un backend et les deux serveurs sont `UP`.
- **Retour arrière** : `sudo cp /etc/haproxy/haproxy.cfg.orig /etc/haproxy/haproxy.cfg`, valider, recharger.

## Si le problème n'est pas résolu

- [HAProxy — Prérequis et limites](/01-fiches-simples/debian/13/vie-du-logiciel/haproxy/fiche-simple-vm-debian-13-haproxy-prerequis-limites)
- [HAProxy — Installer](/01-fiches-simples/debian/13/vie-du-logiciel/haproxy/fiche-simple-vm-debian-13-haproxy-installer)
- [HAProxy — Sécuriser (TLS, pare-feu, durcissement)](/01-fiches-simples/debian/13/vie-du-logiciel/haproxy/fiche-simple-vm-debian-13-haproxy-securiser)
- [HAProxy — Valider (recette)](/01-fiches-simples/debian/13/vie-du-logiciel/haproxy/fiche-simple-vm-debian-13-haproxy-valider)
- [HAProxy — Sauvegarder et restaurer](/01-fiches-simples/debian/13/vie-du-logiciel/haproxy/fiche-simple-vm-debian-13-haproxy-sauvegarder-restaurer)
- [HAProxy — Mise à jour et retour arrière](/01-fiches-simples/debian/13/vie-du-logiciel/haproxy/fiche-simple-vm-debian-13-haproxy-mettre-a-jour)
- [Guide complet Keepalived VRRP + HAProxy](/02-fiches-completes/transverses/multi-os/autres/08-haute-disponibilite-keepalived-vrrp-haproxy)
- [HAProxy — documentation officielle](https://docs.haproxy.org/)
- [Série Keepalived + HAProxy (haute disponibilité)](/01-fiches-simples/transverses/multi-os/keepalived-haproxy/fiche-simple-vm-linux-keepalived-haproxy-installer-valider-haproxy)