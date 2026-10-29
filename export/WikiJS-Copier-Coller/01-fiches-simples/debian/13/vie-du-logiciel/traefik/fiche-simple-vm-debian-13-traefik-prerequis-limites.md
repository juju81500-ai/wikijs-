# Fiche_Simple_-_VM_Debian_13_Traefik_Prerequis_Limites

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; Traefik v3 (binaire officiel)
- **Catégorie** : reverse proxy / Traefik / Prérequis et limites

---

## Problème précis à résoudre

Cadrer l'installation de Traefik en service systemd sur un hôte Debian 13 (hors conteneur).

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler l'OS, l'architecture et les ports :
   ```bash
   cat /etc/os-release | grep PRETTY_NAME
   uname -m
   sudo ss -tlnp | grep -E ':(80|443)\b' || echo 'ports libres'
   ```
   👉 Explication : l'archive officielle dépend de l'architecture (`x86_64` → `amd64`).

2. Lister les services à publier :
   👉 Explication : adresse, port, protocole et nom DNS de chaque application ; Traefik les atteint via le fournisseur de fichiers (file provider).

3. Noter les limites :
   👉 Explication : cette série installe Traefik v3 en binaire sous systemd ; la variante Docker est dans la série `Docker/Traefik` du pack ; la version est à vérifier sur la page des publications officielles.

## 2. Production — Contrôles

Consigner DNS, certificats (ACME ou fichiers), responsable, fenêtre de maintenance, sauvegarde.

## 3. Production — Sécurité

- Ne pas utiliser le fournisseur Docker avec un accès non protégé au socket Docker.
- Ne pas exposer le tableau de bord.
- Prévoir la validation DNS ou le port 80 pour ACME.

## Validation et retour arrière

- **Validation** : ports libres, architecture et périmètre consignés.
- **Retour arrière** : aucune modification effectuée.

## Si le problème n'est pas résolu

- [Traefik — Installer](/01-fiches-simples/debian/13/vie-du-logiciel/traefik/fiche-simple-vm-debian-13-traefik-installer)
- [Traefik — Configurer (statique, dynamique, premier service)](/01-fiches-simples/debian/13/vie-du-logiciel/traefik/fiche-simple-vm-debian-13-traefik-configurer)
- [Traefik — Sécuriser (TLS, redirection, pare-feu)](/01-fiches-simples/debian/13/vie-du-logiciel/traefik/fiche-simple-vm-debian-13-traefik-securiser)
- [Traefik — Valider (recette)](/01-fiches-simples/debian/13/vie-du-logiciel/traefik/fiche-simple-vm-debian-13-traefik-valider)
- [Traefik — Sauvegarder et restaurer](/01-fiches-simples/debian/13/vie-du-logiciel/traefik/fiche-simple-vm-debian-13-traefik-sauvegarder-restaurer)
- [Traefik — Mise à jour et retour arrière](/01-fiches-simples/debian/13/vie-du-logiciel/traefik/fiche-simple-vm-debian-13-traefik-mettre-a-jour)
- [Guide complet Traefik v3.1 et Let's Encrypt (variante Docker)](/02-fiches-completes/transverses/docker/installation-deploiement/06-reverse-proxy-traefik-v31-letsencrypt-docker)
- [Traefik — documentation officielle](https://doc.traefik.io/traefik/)
- [Série Traefik sous Docker](/01-fiches-simples/transverses/docker/traefik/fiche-simple-docker-conteneur-traefik-configuration-statique)