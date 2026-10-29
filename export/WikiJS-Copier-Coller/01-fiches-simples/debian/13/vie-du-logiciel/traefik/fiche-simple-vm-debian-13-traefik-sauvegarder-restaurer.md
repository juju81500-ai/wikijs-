# Fiche_Simple_-_VM_Debian_13_Traefik_Sauvegarder_Restaurer

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; Traefik v3 (binaire officiel)
- **Catégorie** : reverse proxy / Traefik / Sauvegarder et restaurer

---

## Problème précis à résoudre

Sauvegarder configuration, certificats ACME et unité systemd de Traefik et prouver la restauration.

## 1. Hors-Production (Lab / Test / POC)

1. Archiver :
   ```bash
   sudo install -d -m 0700 /var/backups/traefik
   sudo tar -czpf /var/backups/traefik/traefik-$(date +%F).tar.gz /etc/traefik /var/lib/traefik/acme.json /etc/systemd/system/traefik.service
   ```
   👉 Explication : `acme.json` contient les clés des certificats : droits `0700`, copie externe chiffrée. Le binaire se retélécharge, il n'est pas sauvegardé.

2. Relire l'archive :
   ```bash
   sudo tar -tzf /var/backups/traefik/traefik-$(date +%F).tar.gz
   ```
   👉 Explication : contrôle de lisibilité.

3. Restaurer sur VM pilote :
   ```bash
   sudo systemctl stop traefik
   sudo tar -xzpf /var/backups/traefik/traefik-DATE.tar.gz -C /
   sudo chown traefik:traefik /var/lib/traefik/acme.json && sudo chmod 0600 /var/lib/traefik/acme.json
   sudo systemctl daemon-reload && sudo systemctl start traefik
   ```
   👉 Explication : remplacer `DATE` (à remplacer) ; contrôler les droits de `acme.json` après restauration.

## 2. Production — Contrôles

Sauvegarde planifiée et chiffrée, générations multiples, test de restauration périodique.

## 3. Production — Sécurité

- Chiffrer toute copie de `acme.json`.
- Ne pas stocker sur le même disque.
- Restreindre l'accès au dossier de sauvegarde.

## Validation et retour arrière

- **Validation** : service redémarré et certificat servi après restauration.
- **Retour arrière** : reprendre l'archive précédente.

## Si le problème n'est pas résolu

- [Traefik — Prérequis et limites](/01-fiches-simples/debian/13/vie-du-logiciel/traefik/fiche-simple-vm-debian-13-traefik-prerequis-limites)
- [Traefik — Installer](/01-fiches-simples/debian/13/vie-du-logiciel/traefik/fiche-simple-vm-debian-13-traefik-installer)
- [Traefik — Configurer (statique, dynamique, premier service)](/01-fiches-simples/debian/13/vie-du-logiciel/traefik/fiche-simple-vm-debian-13-traefik-configurer)
- [Traefik — Sécuriser (TLS, redirection, pare-feu)](/01-fiches-simples/debian/13/vie-du-logiciel/traefik/fiche-simple-vm-debian-13-traefik-securiser)
- [Traefik — Valider (recette)](/01-fiches-simples/debian/13/vie-du-logiciel/traefik/fiche-simple-vm-debian-13-traefik-valider)
- [Traefik — Mise à jour et retour arrière](/01-fiches-simples/debian/13/vie-du-logiciel/traefik/fiche-simple-vm-debian-13-traefik-mettre-a-jour)
- [Guide complet Traefik v3.1 et Let's Encrypt (variante Docker)](/02-fiches-completes/transverses/docker/installation-deploiement/06-reverse-proxy-traefik-v31-letsencrypt-docker)
- [Traefik — documentation officielle](https://doc.traefik.io/traefik/)
- [Série Traefik sous Docker](/01-fiches-simples/transverses/docker/traefik/fiche-simple-docker-conteneur-traefik-configuration-statique)