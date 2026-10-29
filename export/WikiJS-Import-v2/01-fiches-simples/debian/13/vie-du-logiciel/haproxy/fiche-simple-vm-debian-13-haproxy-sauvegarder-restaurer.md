---
title: "Fiche Simple - VM Debian 13 HAProxy Sauvegarder Restaurer"
description: "Sauvegarder configuration et certificats HAProxy et prouver la restauration."
published: true
date: 2026-10-29T20:34:00Z
tags: ["debian13", "haproxy", "sauvegarde"]
editor: markdown
dateCreated: 2026-10-29T20:34:00Z
dateModified: 2026-10-29T20:34:00Z
---

# Fiche_Simple_-_VM_Debian_13_HAProxy_Sauvegarder_Restaurer

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; HAProxy des dépôts Debian
- **Catégorie** : répartiteur de charge / HAProxy / Sauvegarder et restaurer
- **Tags** : `debian13`, `haproxy`, `sauvegarde`

---

## Problème précis à résoudre

Sauvegarder configuration et certificats HAProxy et prouver la restauration.

## 1. Hors-Production (Lab / Test / POC)

1. Archiver :
   ```bash
   sudo install -d -m 0700 /var/backups/haproxy
   sudo tar -czpf /var/backups/haproxy/haproxy-$(date +%F).tar.gz /etc/haproxy
   ```
   👉 Explication : contient les clés privées : dossier en `0700`, copie externe chiffrée.

2. Relire l'archive :
   ```bash
   sudo tar -tzf /var/backups/haproxy/haproxy-$(date +%F).tar.gz
   ```
   👉 Explication : contrôle de lisibilité.

3. Restaurer sur VM pilote :
   ```bash
   sudo systemctl stop haproxy
   sudo tar -xzpf /var/backups/haproxy/haproxy-DATE.tar.gz -C /
   sudo haproxy -c -f /etc/haproxy/haproxy.cfg && sudo systemctl start haproxy
   ```
   👉 Explication : remplacer `DATE` (à remplacer).

## 2. Production — Contrôles

Sauvegarde planifiée, générations multiples, copie chiffrée hors site, test de restauration périodique.

## 3. Production — Sécurité

- Chiffrer les copies contenant des clés.
- Ne pas stocker sur le même disque.
- Limiter l'accès au dossier de sauvegarde.

## Validation et retour arrière

- **Validation** : restauration testée avec `haproxy -c` valide.
- **Retour arrière** : reprendre l'archive précédente.

## Si le problème n'est pas résolu

- [HAProxy — Prérequis et limites](/01-fiches-simples/debian/13/vie-du-logiciel/haproxy/fiche-simple-vm-debian-13-haproxy-prerequis-limites)
- [HAProxy — Installer](/01-fiches-simples/debian/13/vie-du-logiciel/haproxy/fiche-simple-vm-debian-13-haproxy-installer)
- [HAProxy — Configurer un frontend et des backends](/01-fiches-simples/debian/13/vie-du-logiciel/haproxy/fiche-simple-vm-debian-13-haproxy-configurer)
- [HAProxy — Sécuriser (TLS, pare-feu, durcissement)](/01-fiches-simples/debian/13/vie-du-logiciel/haproxy/fiche-simple-vm-debian-13-haproxy-securiser)
- [HAProxy — Valider (recette)](/01-fiches-simples/debian/13/vie-du-logiciel/haproxy/fiche-simple-vm-debian-13-haproxy-valider)
- [HAProxy — Mise à jour et retour arrière](/01-fiches-simples/debian/13/vie-du-logiciel/haproxy/fiche-simple-vm-debian-13-haproxy-mettre-a-jour)
- [Guide complet Keepalived VRRP + HAProxy](/02-fiches-completes/transverses/multi-os/autres/08-haute-disponibilite-keepalived-vrrp-haproxy)
- [HAProxy — documentation officielle](https://docs.haproxy.org/)
- [Série Keepalived + HAProxy (haute disponibilité)](/01-fiches-simples/transverses/multi-os/keepalived-haproxy/fiche-simple-vm-linux-keepalived-haproxy-installer-valider-haproxy)