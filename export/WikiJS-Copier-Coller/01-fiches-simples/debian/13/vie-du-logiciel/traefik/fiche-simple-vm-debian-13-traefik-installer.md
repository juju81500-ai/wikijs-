# Fiche_Simple_-_VM_Debian_13_Traefik_Installer

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; Traefik v3 (binaire officiel)
- **Catégorie** : reverse proxy / Traefik / Installer

---

## Problème précis à résoudre

Installer le binaire officiel de Traefik avec vérification de somme de contrôle et service systemd dédié.

## 1. Hors-Production (Lab / Test / POC)

1. Créer l'utilisateur de service et les dossiers :
   ```bash
   sudo useradd --system --home /var/lib/traefik --shell /usr/sbin/nologin traefik
   sudo install -d -o root -g traefik -m 0750 /etc/traefik /etc/traefik/dynamic
   sudo install -d -o traefik -g traefik -m 0750 /var/lib/traefik /var/log/traefik
   ```
   👉 Explication : compte sans shell, sans mot de passe.

2. Télécharger l'archive et la somme de contrôle :
   ```bash
   cd ~ && VERSION=VERSION_TRAEFIK
   curl -fLO https://github.com/traefik/traefik/releases/download/v${VERSION}/traefik_v${VERSION}_linux_amd64.tar.gz
   curl -fLO https://github.com/traefik/traefik/releases/download/v${VERSION}/traefik_v${VERSION}_checksums.txt
   ```
   👉 Explication : remplacer `VERSION_TRAEFIK` par la version stable publiée (à vérifier sur la page des releases) et `amd64` par l'architecture.

3. Vérifier l'intégrité :
   ```bash
   sha256sum --ignore-missing -c traefik_v${VERSION}_checksums.txt
   ```
   👉 Explication : `OK` est obligatoire avant installation.

4. Installer le binaire :
   ```bash
   tar -xzf traefik_v${VERSION}_linux_amd64.tar.gz traefik
   sudo install -o root -g root -m 0755 traefik /usr/local/bin/traefik
   sudo setcap 'cap_net_bind_service=+ep' /usr/local/bin/traefik
   traefik version
   ```
   👉 Explication : la capacité permet d'écouter sur 80/443 sans être root.

5. Créer l'unité systemd :
   ```bash
   sudo tee /etc/systemd/system/traefik.service >/dev/null <<'EOF'
   [Unit]
   Description=Traefik
   After=network-online.target
   Wants=network-online.target

   [Service]
   User=traefik
   Group=traefik
   ExecStart=/usr/local/bin/traefik --configFile=/etc/traefik/traefik.yml
   Restart=on-failure
   AmbientCapabilities=CAP_NET_BIND_SERVICE
   NoNewPrivileges=true
   ProtectSystem=full
   ProtectHome=true

   [Install]
   WantedBy=multi-user.target
   EOF
   sudo systemctl daemon-reload
   ```
   👉 Explication : le service n'est démarré qu'après la configuration (fiche suivante).

## 2. Production — Contrôles

Consigner la version, la somme de contrôle vérifiée et l'origine ; planifier la veille des publications de sécurité.

## 3. Production — Sécurité

- Toujours vérifier la somme de contrôle ; ne pas exécuter un binaire d'origine inconnue.
- Service sans privilèges root, `NoNewPrivileges` actif.
- Ne pas laisser l'archive téléchargée dans un dossier partagé.

## Validation et retour arrière

- **Validation** : `traefik version` affiche la version attendue et l'unité est chargée.
- **Retour arrière** : `sudo rm /usr/local/bin/traefik /etc/systemd/system/traefik.service`, `sudo systemctl daemon-reload`, `sudo userdel traefik`.

## Si le problème n'est pas résolu

- [Traefik — Prérequis et limites](/01-fiches-simples/debian/13/vie-du-logiciel/traefik/fiche-simple-vm-debian-13-traefik-prerequis-limites)
- [Traefik — Configurer (statique, dynamique, premier service)](/01-fiches-simples/debian/13/vie-du-logiciel/traefik/fiche-simple-vm-debian-13-traefik-configurer)
- [Traefik — Sécuriser (TLS, redirection, pare-feu)](/01-fiches-simples/debian/13/vie-du-logiciel/traefik/fiche-simple-vm-debian-13-traefik-securiser)
- [Traefik — Valider (recette)](/01-fiches-simples/debian/13/vie-du-logiciel/traefik/fiche-simple-vm-debian-13-traefik-valider)
- [Traefik — Sauvegarder et restaurer](/01-fiches-simples/debian/13/vie-du-logiciel/traefik/fiche-simple-vm-debian-13-traefik-sauvegarder-restaurer)
- [Traefik — Mise à jour et retour arrière](/01-fiches-simples/debian/13/vie-du-logiciel/traefik/fiche-simple-vm-debian-13-traefik-mettre-a-jour)
- [Guide complet Traefik v3.1 et Let's Encrypt (variante Docker)](/02-fiches-completes/transverses/docker/installation-deploiement/06-reverse-proxy-traefik-v31-letsencrypt-docker)
- [Traefik — documentation officielle](https://doc.traefik.io/traefik/)
- [Série Traefik sous Docker](/01-fiches-simples/transverses/docker/traefik/fiche-simple-docker-conteneur-traefik-configuration-statique)