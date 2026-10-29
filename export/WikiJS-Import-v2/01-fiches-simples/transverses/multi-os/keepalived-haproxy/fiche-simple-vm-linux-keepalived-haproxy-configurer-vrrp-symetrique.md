---
title: "Fiche Simple - VM Linux Keepalived HAProxy Configurer VRRP Symetrique"
description: "Configurer Keepalived identiquement sur les deux nœuds avec des priorités différentes."
published: true
date: 2026-10-29T19:45:07Z
tags: ["ha", "keepalived", "vrrp", "haproxy", "linux"]
editor: markdown
dateCreated: 2026-10-29T19:45:07Z
dateModified: 2026-10-29T19:45:07Z
---

# Fiche_Simple_-_VM_Linux_Keepalived_HAProxy_Configurer_VRRP_Symetrique.md

- **Environnement** : Deux nœuds Linux sur le même segment L2, serveurs applicatifs redondés
- **OS / Version** : Linux (Debian/Ubuntu); HAProxy et Keepalived des dépôts de la distribution
- **Catégorie** : haute disponibilité / réseau
- **Tags** : `ha`, `keepalived`, `vrrp`, `haproxy`, `linux`

---

## Problème précis à résoudre

Configurer Keepalived identiquement sur les deux nœuds avec des priorités différentes.

## 1. Hors-Production (Lab / Test / POC)

1. Installer Keepalived sur les deux nœuds :
   ```bash
   sudo apt install keepalived
   ```
   👉 Explication : fournit VRRP.

2. Éditer `/etc/keepalived/keepalived.conf` : même `virtual_router_id`, même interface et même groupe d'adresses, avec des priorités distinctes.
   👉 Explication : le nœud de plus forte priorité détient l'IP virtuelle.

3. Ajouter une sonde (`vrrp_script`) qui retire l'éligibilité si HAProxy est indisponible.
   👉 Explication : évite de garder l'IP sur un nœud sans service.

4. Utiliser une méthode d'authentification compatible avec la version.
   👉 Explication : une clé VRRP n'est pas un chiffrement.

5. Vérifier que les deux configurations ne revendiquent pas des adresses différentes et que le filtrage laisse passer VRRP entre pairs seulement.
   👉 Explication : évite le split-brain.

6. Tester la configuration puis activer :
   ```bash
   sudo keepalived --config-test -f /etc/keepalived/keepalived.conf
   sudo systemctl enable --now keepalived
   ip addr show
   ```
   👉 Explication : si `--config-test` n'existe pas dans le paquet, valider d'après la page de manuel locale et activer en fenêtre de maintenance.

## 2. Production — Contrôles

Activer en fenêtre de maintenance et surveiller les deux nœuds.

## 3. Production — Sécurité

- Filtrer VRRP entre les seuls pairs.

## Validation et retour arrière

- **Validation** : l'IP virtuelle est portée par un seul nœud.
- **Retour arrière** : `sudo systemctl disable --now keepalived` sur le nœud fautif et restaurer le fichier précédent.

## Si le problème n'est pas résolu

- [Keepalived — configuration](https://keepalived.readthedocs.io/en/latest/configuration_synopsis.html)
- [Keepalived — documentation](https://keepalived.readthedocs.io/en/latest/)
- [Guide complet](/02-fiches-completes/transverses/multi-os/autres/08-haute-disponibilite-keepalived-vrrp-haproxy#3-configurer-vrrp-de-facon-symetrique)