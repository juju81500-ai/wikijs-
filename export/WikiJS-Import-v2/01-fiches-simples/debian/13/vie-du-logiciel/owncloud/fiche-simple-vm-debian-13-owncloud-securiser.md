---
title: "Fiche Simple - VM Debian 13 ownCloud Securiser"
description: "Activer HTTPS valide, filtrer le réseau et protéger les secrets d'ownCloud Infinite Scale."
published: true
date: 2026-10-29T21:07:46Z
tags: ["debian13", "owncloud", "ocis", "cloud", "securiser"]
editor: markdown
dateCreated: 2026-10-29T21:07:46Z
dateModified: 2026-10-29T21:07:46Z
---

# Fiche_Simple_-_VM_Debian_13_ownCloud_Securiser

- **Environnement** : VM Debian 13; ownCloud Infinite Scale (oCIS), binaire officiel, Nginx
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : Messagerie et collaboratif / ownCloud — Sécuriser
- **Tags** : `debian13`, `owncloud`, `ocis`, `cloud`, `securiser`

---

## Problème précis à résoudre

Activer HTTPS valide, filtrer le réseau et protéger les secrets d'ownCloud Infinite Scale.

## 1. Hors-Production (Lab / Test / POC)

1. Obtenir le certificat pour le proxy (fiche Certbot du pack) :
   ```bash
   sudo apt install -y certbot python3-certbot-nginx
   sudo certbot --nginx -d OCIS.EXAMPLE.NET
   ```
   👉 Explication : ajoute le bloc 443 et la redirection ; renouvellement par timer systemd.

2. Filtrer le pare-feu :
   ```bash
   sudo ufw allow 80/tcp
   sudo ufw allow 443/tcp
   sudo ufw deny 9200/tcp
   ```
   👉 Explication : 9200 ne doit pas être joignable depuis le réseau ; il n'est utilisé qu'en local par le proxy.

3. Protéger les secrets de configuration :
   ```bash
   sudo chown -R ocis:ocis /etc/ocis
   sudo chmod 0700 /etc/ocis
   sudo chmod 0600 /etc/ocis/ocis.yaml
   ```
   👉 Explication : contient clés et secrets d'authentification.

4. Changer le mot de passe administrateur initial après première connexion : GUI.
   👉 Explication : Profil > Compte > Changer le mot de passe (chemin à vérifier sur la version publiée).

5. Ajouter les en-têtes de sécurité dans Nginx (bloc 443) :
   ```bash
   sudo sed -i '/server_name OCIS.EXAMPLE.NET;/a\    add_header Strict-Transport-Security "max-age=15552000" always;' /etc/nginx/sites-available/ocis
   sudo nginx -t && sudo systemctl reload nginx
   ```
   👉 Explication : active HSTS ; à n'appliquer qu'une fois HTTPS validé (la ligne s'insère dans chaque bloc server contenant le nom).

## 2. Production — Contrôles

Vérifier renouvellement du certificat, accès externe au port 9200 refusé, droits de `/etc/ocis`, politique de mots de passe et journalisation.

## 3. Production — Sécurité

- Secrets jamais copiés dans des tickets ou des dépôts.
- Compte administrateur nominatif et MFA/politiques selon les capacités de la version.
- Protéger le proxy avec [Fail2ban](/01-fiches-simples/debian/13/vie-du-logiciel/fail2ban/fiche-simple-vm-debian-13-securite-fail2ban) si les journaux le permettent.

## Validation et retour arrière

- **Validation** : HTTPS valide, port 9200 non joignable depuis l'extérieur, secrets en 0600.
- **Retour arrière** : restaurer `/etc/nginx/sites-available/ocis` d'origine, supprimer les règles ufw ajoutées et relancer les services.

## Si le problème n'est pas résolu

- [ownCloud — Prérequis et limites](/01-fiches-simples/debian/13/vie-du-logiciel/owncloud/fiche-simple-vm-debian-13-owncloud-prerequis-limites)
- [ownCloud — Installer](/01-fiches-simples/debian/13/vie-du-logiciel/owncloud/fiche-simple-vm-debian-13-owncloud-installer)
- [Certbot — TLS](/01-fiches-simples/debian/13/vie-du-logiciel/certbot/fiche-simple-vm-debian-13-securite-certbot-tls)
- [Fail2ban](/01-fiches-simples/debian/13/vie-du-logiciel/fail2ban/fiche-simple-vm-debian-13-securite-fail2ban)
- [ownCloud Infinite Scale — documentation officielle](https://doc.owncloud.com/ocis/next/)
- [ownCloud — téléchargements](https://owncloud.com/download-server/)