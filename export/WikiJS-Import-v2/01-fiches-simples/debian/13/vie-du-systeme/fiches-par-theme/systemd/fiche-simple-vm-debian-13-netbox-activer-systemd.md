---
title: "Fiche Simple - VM Debian 13 NetBox Activer Systemd"
description: "Activer Gunicorn et le worker de tâches NetBox avec les unités systemd prévues par la release."
published: true
date: 2026-10-29T20:22:42Z
tags: ["debian13", "netbox", "systemd", "gunicorn", "rq"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# Fiche_Simple_-_VM_Debian_13_NetBox_Activer_Systemd.md

- **Environnement** : Debian 13; unités systemd livrées avec NetBox 4.7.4
- **OS / Version** : Debian 13; NetBox 4.7.4
- **Catégorie** : IPAM / DCIM / services
- **Tags** : `debian13`, `netbox`, `systemd`, `gunicorn`, `rq`

---

## Problème précis à résoudre

Activer Gunicorn et le worker de tâches NetBox avec les unités systemd prévues par la release.

## 1. Hors-Production (Lab / Test / POC)

1. Examiner les unités livrées :
   ```bash
   ls /opt/netbox/contrib/*.service
   grep -E '^(User|Group|WorkingDirectory)=' /opt/netbox/contrib/netbox.service
   ```
   👉 Explication : l'utilisateur et le groupe doivent être `netbox`; adapter les chemins s'ils diffèrent.

2. Copier les unités et recharger systemd :
   ```bash
   sudo cp -v /opt/netbox/contrib/*.service /etc/systemd/system/
   sudo systemctl daemon-reload
   ```
   👉 Explication : on n'utilise jamais le serveur de développement.

3. Activer et démarrer les services :
   ```bash
   sudo systemctl enable --now netbox netbox-rq
   sudo systemctl --no-pager --full status netbox netbox-rq
   ```
   👉 Explication : les deux services doivent être `active (running)`.

4. En cas d'échec, lire les journaux :
   ```bash
   sudo journalctl -eu netbox
   sudo journalctl -eu netbox-rq
   ```
   👉 Explication : les erreurs fréquentes concernent `configuration.py`, la base ou Redis.

## 2. Production — Contrôles

Consigner les unités modifiées, les dépendances, les sondes d'état, l'astreinte et les conditions de redémarrage après mise à jour.

## 3. Production — Sécurité

- Conserver le compte et groupe de service non privilégiés.
- Ne pas lancer Gunicorn sous root ou exposer directement son port.
- Ne pas remplacer une unité par un service improvisé sans revue.
- Protéger les logs d'application contre la consultation non autorisée.

## Validation et retour arrière

- **Validation** : deux services actifs, journaux sans erreur bloquante et application accessible uniquement via le frontal.
- **Retour arrière** : restaurer les unités précédentes, recharger systemd puis confirmer les dépendances.

## Si le problème n'est pas résolu

- [NetBox — Gunicorn et systemd](https://netbox.readthedocs.io/en/stable/installation/4a-gunicorn/)
- [systemd — documentation](https://www.freedesktop.org/software/systemd/man/latest/systemctl.html)
- [Guide complet NetBox Debian 13](/02-fiches-completes/debian/13/installation-deploiement/73-deploiement-netbox-4-7-4-debian-13#6-activer-les-services-systemd)