---
title: "Fiche Simple - LXC Alpine Proxmox Telecharger Creer"
description: "Télécharger un template Alpine maintenu et créer un CT LXC avec configuration minimale, non privilégiée et adaptée au service."
published: true
date: 2026-10-29T20:14:10Z
tags: ["alpine", "proxmox", "lxc", "template", "unprivileged"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_LXC_Alpine_Proxmox_Telecharger_Creer.md

- **Environnement** : nœud Proxmox VE avec stockage de templates et bridge/VLAN prévus
- **OS / Version** : template Alpine maintenu proposé par Proxmox VE
- **Catégorie** : virtualisation / création LXC
- **Tags** : `alpine`, `proxmox`, `lxc`, `template`, `unprivileged`

---

## Problème précis à résoudre

Télécharger un template Alpine maintenu et créer un CT LXC avec configuration minimale, non privilégiée et adaptée au service.

## 1. Hors-Production (Lab / Test / POC)

1. Mettre à jour le catalogue et choisir une branche maintenue :
   ```bash
   pveam update
   pveam available | grep -i alpine
   ```
   👉 Explication : repérer le nom exact du template.

2. Télécharger le template (remplacer les deux valeurs) :
   ```bash
   pveam download local NOM_TEMPLATE_ALPINE
   pveam list local
   ```
   👉 Explication : `local` est le stockage de templates du nœud; le template doit apparaître dans la liste.

3. Interface Proxmox : cliquer **Créer CT** (en haut à droite) et renseigner : ID unique, hostname, mot de passe/clé SSH.
   👉 Explication : le compte initial est temporaire; passer ensuite à un compte nominatif.

4. Onglet **Template** : sélectionner le template Alpine téléchargé. Onglet **Disks** : stockage et taille. Onglet **CPU** et **Memory** : selon la charge.
   👉 Explication : dimensionner au plus juste.

5. Onglet **General** : cocher **Unprivileged container**.
   👉 Explication : limite l'impact d'une évasion de conteneur.

6. Onglet **Network** : bridge, **VLAN Tag**, IP statique ou DHCP, passerelle; onglet **DNS** : serveur.
   👉 Explication : laisser nesting, FUSE et périphériques hôte désactivés sauf besoin documenté.

7. Onglet **Confirm** : vérifier le résumé puis **Finish**.
   👉 Explication : contrôler en ligne de commande avec `pct config CTID`.

## 2. Production — Contrôles

Faire valider l'ID, le template, le stockage, les quotas, les options d'isolation, les paramètres réseau et l'identité initiale.

## 3. Production — Sécurité

- Transmettre les secrets initiaux par un canal sécurisé et les remplacer selon la procédure.
- Ne pas créer un CT privilégié pour simplifier les permissions.
- Ne pas activer nesting, FUSE ou les périphériques hôte sans justification documentée.
- Ne pas réutiliser un ID ou une IP déjà attribués.

## Validation et retour arrière

- **Validation** : CT créé avec le bon template, statut non privilégié, ressources et réseau conformes.
- **Retour arrière** : arrêter le CT; avant suppression, vérifier l'ID, les données et l'existence d'une sauvegarde.

## Si le problème n'est pas résolu

- [Proxmox VE — documentation](https://pve.proxmox.com/pve-docs/)
- [Alpine Linux — documentation](https://docs.alpinelinux.org/)
- [Guide complet LXC Alpine sur Proxmox](/02-fiches-completes/alpine/toutes-versions/installation-deploiement/16-installation-lxc-alpine-proxmox#3-telecharger-et-creer-le-conteneur)