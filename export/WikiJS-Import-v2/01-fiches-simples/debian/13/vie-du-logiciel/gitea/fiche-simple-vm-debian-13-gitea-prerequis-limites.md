---
title: "Fiche Simple - VM Debian 13 Gitea Prerequis Limites"
description: "Définir version, FQDN, ressources, stockage, base, ports et sauvegardes avant d’installer Gitea."
published: true
date: 2026-10-29T20:47:59Z
tags: ["debian13", "gitea", "forge-git", "tls", "sauvegarde"]
editor: markdown
dateCreated: 2026-10-29T20:47:59Z
dateModified: 2026-10-29T20:47:59Z
---

# Fiche_Simple_-_VM_Debian_13_Gitea_Prerequis_Limites

- **Environnement** : VM Debian 13 isolée; domaine et stockage définis
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : forge Git / administration
- **Tags** : `debian13`, `gitea`, `forge-git`, `tls`, `sauvegarde`
---

## Problème précis à résoudre

Définir version, FQDN, ressources, stockage, base, ports et sauvegardes avant d’installer Gitea.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier OS, capacité et ports
   ```bash
   cat /etc/os-release
   df -h /var/lib
   free -h
   sudo ss -lntp | grep -E ":(22|3000|443)\b" || true
   ```
   👉 Explication : confirmer Debian 13, ressources disponibles et absence de conflit de ports.

2. Consulter support et version stable
   ```text
   Navigateur > ouvrir la documentation officielle : https://docs.gitea.com/installation/install-from-binary
   ```
   👉 Explication : ne pas supposer que la dernière version convient; vérifier les notes officielles. Détail à confirmer dans la documentation officielle avant application : Consulter la documentation Gitea pour la version et l’architecture retenues. Version cible : 1.XX.Y (à remplacer après validation).

3. Choisir base et exposition
   ```text
   Navigateur > ouvrir la documentation officielle : https://docs.gitea.com/installation/install-from-binary
   ```
   👉 Explication : les limites de SQLite, base distante et stockage doivent être confirmées dans la documentation de la version. Détail à confirmer dans la documentation officielle avant application : Pilote isolé : base locale possible. Production : base supportée, proxy TLS, DNS et sauvegarde testée.

## 2. Production — Contrôles

Valider capacité, version, DNS, backend, politique de comptes et plan de restauration avant ouverture.

## 3. Production — Sécurité

- Le service doit fonctionner sous un compte dédié, non privilégié.
- Ne jamais ouvrir directement le port applicatif au réseau public.
- Protéger le fichier de configuration et les clés serveur.

## Validation et retour arrière

- **Validation** : Version, ressources, ports et méthode de sauvegarde sont documentés.
- **Retour arrière** : Reporter le déploiement tant que le domaine, la sauvegarde et le propriétaire du service ne sont pas définis.

## Si le problème n'est pas résolu

- [Gitea — installation depuis un binaire](https://docs.gitea.com/installation/install-from-binary)
- [Gitea — configuration](https://docs.gitea.com/administration/config-cheat-sheet)
- [Gitea — sauvegarde/restauration](https://docs.gitea.com/administration/backup-and-restore)
- [Fiche connexe](</01-fiches-simples/debian/13/vie-du-logiciel/gitea/fiche-simple-vm-debian-13-gitea-installer>)