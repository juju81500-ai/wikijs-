# 📄 Fiche_Simple_-_VM_Rocky_9_Supervision_Zabbix_Agent2.md

- **Environnement** : VM ou serveur Rocky Linux supervisé par Zabbix
- **OS / Version** : Rocky Linux 9 / RHEL 9 (Zabbix 7.0 LTS, dépôt officiel Zabbix)
- **Catégorie** : Supervision / Agent de supervision
- **Tags** : `[rocky9]`, `[rhel9]`, `[zabbix]`, `[monitoring]`, `[firewalld]`, `[psk]`

## 🎯 Problème précis à résoudre
Installer l'agent Zabbix 2 sur Rocky Linux 9, le déclarer auprès du serveur Zabbix, n'autoriser que le serveur de supervision à l'interroger et chiffrer les échanges.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Ajouter le dépôt officiel Zabbix 7.0 pour Rocky Linux 9 :
   ```bash
   sudo rpm -Uvh https://repo.zabbix.com/zabbix/7.0/rocky/9/x86_64/zabbix-release-latest-7.0.el9.noarch.rpm
   sudo dnf clean all
   ```
   👉 Explication : Le dépôt EPEL ou BaseOS ne fournit pas toujours la version Zabbix souhaitée. Adapter `7.0` à la version de serveur Zabbix déployée, un agent doit être compatible avec le serveur.

2. Installer l'agent et vérifier la version :
   ```bash
   sudo dnf install -y zabbix-agent2
   zabbix_agent2 -V
   ```
   👉 Explication : Installe le binaire `zabbix_agent2`, son fichier de configuration `/etc/zabbix/zabbix_agent2.conf` et le service systemd `zabbix-agent2`.

3. Configurer le serveur et le nom de l'hôte dans `/etc/zabbix/zabbix_agent2.conf` :
   ```text
   Server=<ip_serveur_zabbix>
   ServerActive=<ip_serveur_zabbix>
   Hostname=<nom_du_serveur>
   ```
   👉 Explication : `Server` autorise les requêtes passives. `ServerActive` sert aux contrôles actifs. `Hostname` doit correspondre exactement au nom de l'hôte déclaré dans l'interface Zabbix.

4. Activer le service et tester un élément :
   ```bash
   sudo systemctl enable --now zabbix-agent2
   sudo zabbix_agent2 -t agent.ping
   ```
   👉 Explication : `zabbix_agent2 -t` évalue un élément localement sans passer par le réseau. La valeur `1` confirme que l'agent fonctionne.

---

## ⚡ 2. Production — Façon Simplifiée
1. Autoriser le port 10050/TCP uniquement depuis le serveur Zabbix :
   ```bash
   sudo firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="<ip_serveur_zabbix>" port port="10050" protocol="tcp" accept'
   sudo firewall-cmd --reload
   ```
   👉 Explication : Une règle générale sur le port 10050 exposerait l'agent à tout le réseau. La règle riche limite l'accès à l'adresse du serveur.

2. Tester depuis le serveur Zabbix, avec le paquet `zabbix-get` installé sur ce serveur :
   ```bash
   zabbix_get -s <ip_de_la_machine> -k agent.ping
   ```
   👉 Explication : La réponse `1` confirme que le port est ouvert et que l'agent répond à la bonne adresse.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Chiffrer les échanges avec une clé pré-partagée (PSK) :
   ```bash
   sudo sh -c 'umask 027; openssl rand -hex 32 > /etc/zabbix/zabbix_agent2.psk'
   sudo chown root:zabbix /etc/zabbix/zabbix_agent2.psk
   ```
   👉 Explication : La clé est stockée avec des droits limités au groupe `zabbix`. Elle doit être copiée à l'identique dans la configuration de l'hôte côté serveur Zabbix.

2. Ajouter les paramètres TLS dans `/etc/zabbix/zabbix_agent2.conf` :
   ```text
   TLSConnect=psk
   TLSAccept=psk
   TLSPSKIdentity=<identite_psk>
   TLSPSKFile=/etc/zabbix/zabbix_agent2.psk
   ```
   👉 Explication : `TLSAccept` refuse les connexions non chiffrées. `TLSPSKIdentity` doit correspondre au champ « PSK identity » de l'hôte dans Zabbix.

3. Interdire l'exécution de commandes distantes arbitraires :
   ```text
   DenyKey=system.run[*]
   ```
   👉 Explication : Empêche le serveur Zabbix, ou un attaquant qui le compromet, de lancer des commandes shell sur la machine via l'élément `system.run`.

4. Redémarrer l'agent et vérifier qu'il écoute :
   ```bash
   sudo systemctl restart zabbix-agent2
   sudo ss -tlnp | grep 10050
   ```
   👉 Explication : Le port 10050 doit apparaître en écoute pour le processus `zabbix_agent2`. Vérifier ensuite l'état `ZBX` de l'hôte dans l'interface Zabbix.

---

## ✅ Contrôle
```bash
systemctl is-active zabbix-agent2
```
👉 Explication : Doit retourner `active`. Une alerte de disponibilité dans Zabbix indique une règle pare-feu ou une clé PSK incorrecte.
