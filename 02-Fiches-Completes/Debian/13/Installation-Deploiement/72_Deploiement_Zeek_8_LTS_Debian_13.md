# Déployer Zeek 8.0 LTS en capteur passif sur Debian 13

- **OS / Version** : Debian 13 Trixie; Zeek 8.0 LTS depuis le dépôt officiel OBS du projet
- **Type de fiche** : Installation/Déploiement
- **Périmètre** : un nœud standalone ZeekControl sur une interface miroir approuvée; pas de cluster ni d'IPS
- **Catégorie** : Supervision et analyse passive du trafic réseau
- **Tags** : `zeek`, `debian13`, `lTS`, `network-monitoring`, `af-packet`, `zeekctl`, `lab`

## 1. Définir le périmètre et la source réseau

Fiche simple : [définir périmètre et source réseau](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Zeek/Fiche_Simple_-_VM_Debian_13_Zeek_Cadrer.md).

Zeek analyse les métadonnées des protocoles et génère des journaux structurés; il complète un IDS à signatures tel que Suricata ou Snort, mais ne les remplace pas et ne bloque pas le trafic dans cette procédure.

Déployer une VM Debian 13 dédiée avec une interface de gestion et une interface de capture séparée. Connecter la capture à un port miroir/SPAN ou à un TAP approuvé, et faire confirmer par l'équipe réseau les VLAN visibles, le sens du miroir et la liste des sous-réseaux internes. Une interface connectée à un commutateur ordinaire ne reçoit généralement que le trafic de la VM elle-même. La capture peut contenir des données sensibles; définir qui accède aux journaux et leur durée de conservation avant mise en service.

Cette fiche vise un nœud standalone de laboratoire. Elle ne couvre pas le provisionnement du SPAN/TAP, le dimensionnement haute performance, un cluster, l'investigation d'incidents ou la capture de réseaux tiers.

## 2. Ajouter le dépôt officiel Zeek 8.0 LTS pour Debian 13

Fiche simple : [ajouter le dépôt Zeek 8.0 LTS et installer](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Zeek/Fiche_Simple_-_VM_Debian_13_Zeek_Depot_Installer.md).

Le projet Zeek publie ses paquets binaires Linux via Open Build Service et recommande une ligne LTS explicite plutôt que la ligne `zeek` roulante. La page du dépôt pour `security:zeek` confirme le répertoire Debian 13. Importer la clé du dépôt dans un keyring dédié et associer explicitement ce keyring à la source APT :

```bash
sudo apt update
sudo apt install -y ca-certificates curl gnupg libcap2-bin
sudo install -d -m 0755 /etc/apt/keyrings
curl -fsSL https://download.opensuse.org/repositories/security:/zeek/Debian_13/Release.key | sudo gpg --dearmor --yes -o /etc/apt/keyrings/zeek-obs.gpg
echo 'deb [signed-by=/etc/apt/keyrings/zeek-obs.gpg] https://download.opensuse.org/repositories/security:/zeek/Debian_13/ /' | sudo tee /etc/apt/sources.list.d/zeek-obs.list
sudo apt update
apt-cache policy zeek-8.0
```

Vérifier que le candidat provient du dépôt `security:zeek` pour `Debian_13`, puis installer la ligne LTS :

```bash
sudo apt install zeek-8.0
```

Confirmer les binaires et préfixe réels avant de configurer le service; les paquets Zeek OBS utilisent habituellement `/opt/zeek` :

```bash
dpkg-query -W 'zeek*'
command -v zeek
command -v zeekctl
zeek --version
zeek -N Zeek::AF_Packet
```

La dernière commande doit lister la source de capture AF_PACKET intégrée au binaire. Si le binaire n'est pas dans le `PATH`, ajouter `/opt/zeek/bin` au `PATH` du compte de service et des commandes d'administration au lieu de créer un lien arbitraire dans `/usr/bin`.

## 3. Créer un compte de service et vérifier l'interface

Fiche simple : [créer le compte de service et les capacités](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Zeek/Fiche_Simple_-_VM_Debian_13_Zeek_Compte_Service.md).

Utiliser un compte système dédié pour ZeekControl et les journaux; ne pas donner au compte d'exploitation l'écriture sur les binaires :

```bash
sudo adduser --system --group --home /opt/zeek zeek
sudo install -d -o zeek -g zeek -m 0750 /opt/zeek/logs /opt/zeek/spool
sudo setcap cap_net_raw,cap_net_admin=+eip /opt/zeek/bin/zeek
getcap /opt/zeek/bin/zeek
ip -br address
ip -d link show
```

Le binaire et les chemins ci-dessus correspondent au préfixe habituel des paquets OBS et doivent être remplacés par les chemins effectivement installés si différents. Les capacités sont nécessaires à AF_PACKET sans lancer ZeekControl comme root; une mise à jour du binaire peut les effacer, vérifier `getcap` après chaque mise à niveau. Avant toute capture, identifier précisément le nom de l'interface miroir, son état de lien et les adresses qu'elle porte. Elle ne doit pas servir à l'administration ni au trafic utilisateur. Ne pas modifier le pont, le VLAN ou l'interface de capture sur l'hôte sans un changement réseau autorisé.

Vérifier les permissions de l'arborescence fournie par le paquet. Le compte `zeek` doit pouvoir écrire dans les répertoires `logs` et `spool`, et lire les exécutables et politiques. Ne pas rendre `/opt/zeek` globalement inscriptible. Les interfaces live requièrent des privilèges de capture; préférer les capacités minimales Linux documentées pour AF_PACKET au lancement complet de Zeek en root. Contrôler les capacités après une mise à niveau, car une mise à jour de binaire peut les supprimer.

## 4. Configurer un nœud standalone

Fiche simple : [configurer un nœud standalone](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Zeek/Fiche_Simple_-_VM_Debian_13_Zeek_Noeud_Standalone.md).

Sauvegarder les configurations avant modification :

```bash
sudo cp -a /opt/zeek/etc/node.cfg /opt/zeek/etc/node.cfg.pre-lab
sudo cp -a /opt/zeek/etc/networks.cfg /opt/zeek/etc/networks.cfg.pre-lab
```

Dans `/opt/zeek/etc/node.cfg`, conserver un seul nœud standalone et remplacer l'interface d'exemple par l'interface miroir réellement autorisée :

```ini
[zeek]
type=standalone
host=localhost
interface=enp2s0
```

Dans `/opt/zeek/etc/networks.cfg`, remplacer les sous-réseaux privés par les CIDR réellement suivis. N'ajouter aucun réseau qui n'est pas dans le périmètre approuvé; Zeek s'en sert pour distinguer l'espace local dans les analyses et journaux.

Configurer les options d'archivage dans `/opt/zeek/etc/zeekctl.cfg` : nom de contact opérationnel et rétention de logs conforme à la politique de stockage. Les logs peuvent contenir des noms d'hôtes, des adresses, des métadonnées HTTP/DNS/TLS et des éléments d'enquête. Ne pas activer l'extraction de fichiers ou des scripts locaux non relus.

## 5. Vérifier la configuration et déployer ZeekControl

Fiche simple : [vérifier et déployer ZeekControl](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Zeek/Fiche_Simple_-_VM_Debian_13_Zeek_Deployer.md).

Confirmer le préfixe et les chemins réellement installés par le paquet, puis vérifier la configuration du nœud avant le déploiement :

```bash
sudo -u zeek /opt/zeek/bin/zeekctl config
sudo -u zeek /opt/zeek/bin/zeekctl check
```

La commande `check` doit réussir avant le premier démarrage. Déployer ensuite le nœud :

```bash
sudo -u zeek /opt/zeek/bin/zeekctl deploy
sudo -u zeek /opt/zeek/bin/zeekctl status
```

Si ZeekControl n'est pas installé sous `/opt/zeek/bin`, utiliser le chemin affiché par `command -v zeekctl`; ne pas deviner un autre préfixe. Si la capture échoue par permission, consulter `journalctl`, les capacités de capture et les permissions, sans basculer le capteur en root comme contournement permanent.

## 6. Valider les logs avec du trafic autorisé

Fiche simple : [valider les logs avec du trafic autorisé](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Zeek/Fiche_Simple_-_VM_Debian_13_Zeek_Valider_Logs.md).

Générer ou attendre du trafic normal dans le laboratoire, puis vérifier que Zeek reçoit les paquets et produit des journaux de connexions :

```bash
sudo -u zeek /opt/zeek/bin/zeekctl netstats
sudo -u zeek /opt/zeek/bin/zeekctl status
sudo ls -lah /opt/zeek/logs/current
```

Les fichiers attendus incluent généralement `conn.log`, ainsi que les logs de protocoles observés. Lire un échantillon de `conn.log` et confirmer les UID, adresses, ports et timestamps avec un flux connu et autorisé. Si les logs sont au format TSV, consulter les métadonnées de colonnes en tête; si le format JSON est configuré, valider une ligne avec un parseur JSON. Protéger les logs comme des données réseau sensibles.

Pour un essai hors ligne sans surveiller une interface, utiliser une capture PCAP de laboratoire obtenue légalement :

```bash
install -d -m 0700 /tmp/zeek-pcap-test
cd /tmp/zeek-pcap-test
/opt/zeek/bin/zeek -r /chemin/autorise/capture.pcap LogAscii::use_json=T
```

Comparer le nombre de connexions et les événements à la documentation du PCAP. Ne pas utiliser une capture issue d'un réseau tiers sans autorisation écrite.

## 7. Exploitation et durcissement

Fiche simple : [exploiter et durcir Zeek](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Zeek/Fiche_Simple_-_VM_Debian_13_Zeek_Exploiter.md).

- Vérifier régulièrement `zeekctl status`, `zeekctl netstats`, les messages de capture/perte et la capacité du répertoire logs.
- Configurer `zeekctl cron` à intervalles réguliers pour l'état des nœuds, le contrôle d'espace et la rotation/rétention; exécuter ce cron sous le même compte `zeek` et selon la configuration validée.
- Mettre à jour Zeek dans la même ligne LTS, tester d'abord les scripts locaux et les journaux, puis lancer `zeekctl deploy` après vérification.
- Transférer les logs vers un collecteur protégé avec un transport chiffré, des permissions minimales et une rétention documentée.
- Ne pas présenter les sorties `notice.log` comme preuve automatique d'intrusion; corréler avec les systèmes et événements autorisés.
- Pour une charge élevée, dimensionner CPU, mémoire, NIC, buffer/capture et stockage avec des mesures de perte réelles; les performances d'un seul worker sont limitées par son cœur.

## Sources

- [Zeek — installation et lignes binaires LTS](https://docs.zeek.org/en/stable/install.html)
- [Zeek 8.0 — paquets OBS du projet](https://software.opensuse.org/download.html?project=security%3Azeek&package=zeek-8.0)
- [OBS — dépôt Zeek Debian 13](https://download.opensuse.org/repositories/security:/zeek/Debian_13/)
- [Zeek — guide de démarrage et logs](https://docs.zeek.org/en/stable/quickstart.html)
- [Zeek — supervision passive et sources réseau](https://docs.zeek.org/en/stable/monitoring.html)
- [Zeek — cluster et acquisition AF_PACKET](https://docs.zeek.org/en/stable/cluster-setup.html)
- [Zeek — logs communs](https://docs.zeek.org/en/stable/logs/index.html)
- [ZeekControl — configuration et commandes](https://github.com/zeek/zeekctl)

Les paquets Zeek OBS et la documentation « stable » évoluent; relever la version exacte du paquet candidat et du binaire installé. Aucun port miroir, déploiement ZeekControl ou essai de charge n'est validé par cette fiche.