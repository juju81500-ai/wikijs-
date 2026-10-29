# Fiche_Simple_-_VM_Debian_12_Zabbix_Installer_Configurer.md

- **Environnement** : serveur Debian 12 avec base Zabbix créée et dépôt officiel validé
- **OS / Version** : Debian 12 Bookworm; serveur et frontend Zabbix 7.0 LTS
- **Catégorie** : supervision / serveur et frontend
- **Tags** : `debian12`, `zabbix`, `frontend`, `apache`, `php`, `systemd`

---

## Problème précis à résoudre

Installer les composants Zabbix et configurer serveur, frontend et services sans exposer de secrets.

## 1. Hors-Production (Lab / Test / POC)

1. Installer serveur, interface et agent :
   ```bash
   sudo apt install zabbix-server-mysql zabbix-frontend-php zabbix-apache-conf zabbix-sql-scripts zabbix-agent
   sudo zabbix_server -V | head -1
   ```
   👉 Explication : pour Nginx, remplacer `zabbix-apache-conf` par `zabbix-nginx-conf`.

2. Renseigner le mot de passe de la base sans l'afficher :
   ```bash
   read -rsp "Mot de passe base zabbix : " ZPW; echo
   sudo sed -i "s|^# DBPassword=.*|DBPassword=${ZPW}|; s|^DBPassword=.*|DBPassword=${ZPW}|" /etc/zabbix/zabbix_server.conf
   unset ZPW
   sudo grep -E '^(DBName|DBUser)' /etc/zabbix/zabbix_server.conf
   sudo chmod 0640 /etc/zabbix/zabbix_server.conf
   ```
   👉 Explication : vérifier `DBName=zabbix` et `DBUser=zabbix`; ne jamais committer ce fichier.

3. Démarrer et activer :
   ```bash
   sudo systemctl restart zabbix-server zabbix-agent apache2
   sudo systemctl enable zabbix-server zabbix-agent apache2
   ```
   👉 Explication : démarrer seulement après la configuration.

4. Valider les journaux :
   ```bash
   sudo journalctl -u zabbix-server --since '-5 minutes' --no-pager
   ```
   👉 Explication : aucune erreur de connexion à la base.

## 2. Production — Contrôles

Contrôler versions candidates, services, configuration DB, propriétaire/permissions des secrets, fuseau, serveur Web et journaux.

## 3. Production — Sécurité

- Ne jamais committer `DBPassword` ni l'inscrire dans une fiche ou un ticket.
- Restreindre l'accès au fichier de configuration serveur.
- N'activer les services qu'après configuration et validation.
- Ne pas mélanger paquets serveur Web incompatibles ou de distributions différentes.

## Validation et retour arrière

- **Validation** : serveur, agent et serveur Web démarrent; journaux sans erreur de schéma ou d'authentification.
- **Retour arrière** : restaurer la configuration précédente, vérifier les services et conserver la base sans suppression.

## Si le problème n'est pas résolu

- [Zabbix — installation depuis les paquets](https://www.zabbix.com/documentation/7.0/en/manual/installation/install)
- [Zabbix — documentation 7.0](https://www.zabbix.com/documentation/7.0/en/manual)
- [Guide complet Zabbix Debian 12](../../../../../02-Fiches-Completes/Debian/12/Installation-Deploiement/04_Supervision_Centralisee_Zabbix_70_LTS_Debian_12.md)
