---
title: "Fiche Simple - VM Ubuntu 24.04 Dovecot Securiser"
description: "Limiter connexions réseau et protéger TLS et comptes de Dovecot."
published: true
date: 2026-10-29T21:13:54Z
tags: ["dovecot", "serveur", "vie-du-logiciel", "securiser"]
editor: markdown
dateCreated: 2026-10-29T21:13:54Z
dateModified: 2026-10-29T21:13:54Z
---

# Fiche_Simple_-_VM_Ubuntu_24.04_Dovecot_Securiser

- **Environnement** : VM Ubuntu Server 24.04; Dovecot depuis les dépôts de la distribution
- **OS / Version** : Ubuntu Server 24.04
- **Catégorie** : Vie du logiciel / Dovecot — Sécuriser
- **Tags** : `dovecot`, `serveur`, `vie-du-logiciel`, `securiser`

---

## Problème précis à résoudre

Limiter connexions réseau et protéger TLS et comptes de Dovecot.

## 1. Hors-Production (Lab / Test / POC)

1. Sécuriser :
   ```bash
   sudo tar --xattrs -czf /root/dovecot-pre-tls-DATE.tgz /etc/dovecot
sudo tee /etc/dovecot/conf.d/99-tls.conf >/dev/null <<'EOF'
ssl = required
disable_plaintext_auth = yes
ssl_cert = </etc/ssl/certs/IMAP_FULLCHAIN.pem
ssl_key = </etc/ssl/private/IMAP_PRIVATE_KEY.pem
EOF
sudo doveconf -n
sudo systemctl reload dovecot
sudo doveconf -n | grep -E "ssl|disable_plaintext_auth|auth_mechanisms" || true
sudo ufw allow from ADMIN_CIDR to any port 22 proto tcp
sudo ufw allow 993/tcp
sudo ufw status verbose
   ```
   👉 Explication : Impose TLS et refuse l’authentification en clair; `IMAP_FULLCHAIN.pem`, `IMAP_PRIVATE_KEY.pem` et `ADMIN_CIDR` sont à remplacer. Installer les certificats avant rechargement; sur Rocky, ne pas désactiver SELinux.


## 2. Production — Contrôles

Ubuntu : UFW si prévu; Rocky : firewalld et SELinux enforcing. Autoriser uniquement les flux documentés.

## 3. Production — Sécurité

Protéger clés, limiter sources, empêcher le relais ouvert. Ouvrir 587 uniquement si authentification/TLS configurés.

## Validation et retour arrière

- **Validation** : Ports, certificat, restrictions et journaux correspondent à la matrice de flux.
- **Retour arrière** : Remplacer `DATE` par la date de l’archive, restaurer `/etc/dovecot`, vérifier les certificats puis recharger Dovecot; rétablir les règles pare-feu précédentes sans couper l’administration.

## Si le problème n'est pas résolu

- [Prérequis et limites](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/dovecot/fiche-simple-vm-ubuntu-24-04-dovecot-prerequis-limites)
- [Installer](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/dovecot/fiche-simple-vm-ubuntu-24-04-dovecot-installer)
- [Configurer](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/dovecot/fiche-simple-vm-ubuntu-24-04-dovecot-configurer)
- [Valider (recette)](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/dovecot/fiche-simple-vm-ubuntu-24-04-dovecot-valider)
- [Sauvegarder / restaurer](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/dovecot/fiche-simple-vm-ubuntu-24-04-dovecot-sauvegarder-restaurer)
- [Mise à jour et retour arrière](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/dovecot/fiche-simple-vm-ubuntu-24-04-dovecot-mise-a-jour-retour-arriere)
- [Documentation officielle](https://doc.dovecot.org/)