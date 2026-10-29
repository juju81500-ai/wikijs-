# Fiche_Simple_-_VM_Debian_13_ownCloud_Installer

- **Environnement** : VM Debian 13; ownCloud Infinite Scale (oCIS), binaire officiel, Nginx
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : Messagerie et collaboratif / ownCloud — Installer

---

## Problème précis à résoudre

Installer le binaire officiel ownCloud Infinite Scale sous un compte système dédié, avec un service systemd.

## 1. Hors-Production (Lab / Test / POC)

1. Créer l'utilisateur et les dossiers :
   ```bash
   sudo useradd --system --home-dir /var/lib/ocis --shell /usr/sbin/nologin ocis
   sudo install -d -o ocis -g ocis -m 0750 /var/lib/ocis /etc/ocis
   ```
   👉 Explication : compte sans shell ; configuration dans `/etc/ocis`, données dans `/var/lib/ocis`.

2. Télécharger le binaire de la version choisie :
   ```bash
   OCIS_VERSION=X.Y.Z
   curl -fL -o /tmp/ocis https://download.owncloud.com/ocis/ocis/stable/${OCIS_VERSION}/ocis-${OCIS_VERSION}-linux-amd64
   sudo install -m 0755 /tmp/ocis /usr/local/bin/ocis
   rm /tmp/ocis
   ```
   👉 Explication : `X.Y.Z` est à remplacer par la version relevée à la fiche Prérequis. Vérifier l'empreinte si l'éditeur en publie une pour cette version.

3. Contrôler le binaire :
   ```bash
   ocis version
   ```
   👉 Explication : affiche la version installée.

4. Initialiser la configuration (génère secrets et mot de passe administrateur) :
   ```bash
   sudo -u ocis env OCIS_CONFIG_DIR=/etc/ocis ocis init
   ```
   👉 Explication : répondre aux questions : le mot de passe administrateur est généré (à noter dans un gestionnaire de mots de passe) ou saisi ; ne pas accepter le mode « insecure » en production.

5. Créer le service systemd :
   ```bash
   sudo tee /etc/systemd/system/ocis.service >/dev/null <<'EOF'
   [Unit]
   Description=ownCloud Infinite Scale
   After=network-online.target

   [Service]
   User=ocis
   Group=ocis
   Environment=OCIS_CONFIG_DIR=/etc/ocis
   Environment=OCIS_BASE_DATA_PATH=/var/lib/ocis
   Environment=OCIS_URL=https://OCIS.EXAMPLE.NET:9200
   ExecStart=/usr/local/bin/ocis server
   Restart=on-failure
   NoNewPrivileges=true
   ProtectSystem=full

   [Install]
   WantedBy=multi-user.target
   EOF
   sudo systemctl daemon-reload
   sudo systemctl enable --now ocis
   ```
   👉 Explication : `OCIS_URL` doit correspondre à l'URL réellement utilisée par les clients (à remplacer). En lab, oCIS publie en HTTPS auto-signé sur 9200.

## 2. Production — Contrôles

Vérifier l'état du service, la version, la propriété des dossiers (`ocis:ocis`), l'absence de secrets dans l'unité systemd.

## 3. Production — Sécurité

- Les secrets sont dans `/etc/ocis/ocis.yaml` : droits 0600 `ocis`, ne pas diffuser.
- Ne pas exécuter le service en root.

## Validation et retour arrière

- **Validation** : `systemctl is-active ocis` renvoie `active`.
- **Retour arrière** : `sudo systemctl disable --now ocis`, supprimer l'unité, le binaire, `/etc/ocis` et `/var/lib/ocis`, ou restaurer le snapshot.

## Si le problème n'est pas résolu

- [ownCloud — Prérequis et limites](/01-fiches-simples/debian/13/vie-du-logiciel/owncloud/fiche-simple-vm-debian-13-owncloud-prerequis-limites)
- [ownCloud — Configurer](/01-fiches-simples/debian/13/vie-du-logiciel/owncloud/fiche-simple-vm-debian-13-owncloud-configurer)
- [ownCloud Infinite Scale — documentation officielle](https://doc.owncloud.com/ocis/next/)
- [ownCloud — téléchargements](https://owncloud.com/download-server/)