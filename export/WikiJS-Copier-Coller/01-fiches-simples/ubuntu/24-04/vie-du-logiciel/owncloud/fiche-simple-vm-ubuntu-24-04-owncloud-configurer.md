# Fiche_Simple_-_VM_Ubuntu_24.04_ownCloud_Configurer

- **Environnement** : VM Ubuntu Server 24.04; ownCloud Infinite Scale (oCIS), binaire officiel
- **OS / Version** : Ubuntu Server 24.04
- **Catégorie** : Vie du logiciel / ownCloud — Configurer

---

## Problème précis à résoudre

Initialiser oCIS et l’exécuter via systemd en compte non privilégié.

## 1. Hors-Production (Lab / Test / POC)

1. Configurer :
   ```bash
   sudo -u ocis /usr/local/bin/ocis init --config-path /etc/ocis
sudo tee /etc/ocis/ocis.env >/dev/null <<'EOF'
OCIS_URL=https://CLOUD.EXAMPLE.NET
PROXY_HTTP_ADDR=127.0.0.1:9200
OCIS_INSECURE=false
OCIS_CONFIG_DIR=/etc/ocis
OCIS_BASE_DATA_PATH=/var/lib/ocis
EOF
sudo chown root:ocis /etc/ocis/ocis.env
sudo chmod 0640 /etc/ocis/ocis.env
sudo tee /etc/systemd/system/ocis.service >/dev/null <<'EOF'
[Unit]
Description=ownCloud Infinite Scale
After=network-online.target
Wants=network-online.target
[Service]
Type=simple
User=ocis
Group=ocis
EnvironmentFile=/etc/ocis/ocis.env
ExecStart=/usr/local/bin/ocis server
Restart=on-failure
[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable --now ocis
   ```
   👉 Explication : `CLOUD.EXAMPLE.NET` est un placeholder à remplacer. Backend sur loopback derrière le proxy; service inspiré de la procédure systemd officielle.

## 2. Production — Contrôles

Séparer config `/etc/ocis`, données `/var/lib/ocis` et terminaison TLS du proxy.

## 3. Production — Sécurité

Ne pas activer `OCIS_INSECURE=true`; protéger l’environnement.

## Validation et retour arrière

- **Validation** : `systemctl is-active ocis` renvoie active, processus sous `ocis`.
- **Retour arrière** : Restaurer unité/environnement précédents et redémarrer avec ancien binaire.

## Si le problème n'est pas résolu

- [Prérequis et limites](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/owncloud/fiche-simple-vm-ubuntu-24-04-owncloud-prerequis-limites)
- [Installer](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/owncloud/fiche-simple-vm-ubuntu-24-04-owncloud-installer)
- [Sécuriser](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/owncloud/fiche-simple-vm-ubuntu-24-04-owncloud-securiser)
- [Valider (recette)](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/owncloud/fiche-simple-vm-ubuntu-24-04-owncloud-valider)
- [Sauvegarder / restaurer](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/owncloud/fiche-simple-vm-ubuntu-24-04-owncloud-sauvegarder-restaurer)
- [Mise à jour et retour arrière](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/owncloud/fiche-simple-vm-ubuntu-24-04-owncloud-mise-a-jour-retour-arriere)
- [Documentation officielle](https://owncloud.dev/ocis/deployment/systemd/)