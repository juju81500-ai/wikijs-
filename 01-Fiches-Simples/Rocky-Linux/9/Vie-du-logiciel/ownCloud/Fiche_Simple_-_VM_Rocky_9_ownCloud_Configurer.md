# Fiche_Simple_-_VM_Rocky_9_ownCloud_Configurer

- **Environnement** : VM Rocky Linux 9; ownCloud Infinite Scale (oCIS), binaire officiel
- **OS / Version** : Rocky Linux 9
- **Catégorie** : Vie du logiciel / ownCloud — Configurer
- **Tags** : `owncloud`, `serveur`, `vie-du-logiciel`, `configurer`

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

- [Prérequis et limites](Fiche_Simple_-_VM_Rocky_9_ownCloud_Prerequis_Limites.md)
- [Installer](Fiche_Simple_-_VM_Rocky_9_ownCloud_Installer.md)
- [Sécuriser](Fiche_Simple_-_VM_Rocky_9_ownCloud_Securiser.md)
- [Valider (recette)](Fiche_Simple_-_VM_Rocky_9_ownCloud_Valider.md)
- [Sauvegarder / restaurer](Fiche_Simple_-_VM_Rocky_9_ownCloud_Sauvegarder_Restaurer.md)
- [Mise à jour et retour arrière](Fiche_Simple_-_VM_Rocky_9_ownCloud_Mise_A_Jour_Retour_Arriere.md)
- [Documentation officielle](https://owncloud.dev/ocis/deployment/systemd/)
