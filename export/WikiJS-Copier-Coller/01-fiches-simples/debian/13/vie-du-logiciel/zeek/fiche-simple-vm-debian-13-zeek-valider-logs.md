# Fiche_Simple_-_VM_Debian_13_Zeek_Valider_Logs.md

- **Environnement** : VM Debian 13 capteur passif Zeek standalone sur interface miroir approuvée
- **OS / Version** : Debian 13 Trixie; Zeek 8.0 LTS (dépôt OBS officiel)
- **Catégorie** : supervision / analyse passive du trafic

---

## Problème précis à résoudre

Confirmer que Zeek reçoit des paquets et produit des journaux exploitables.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler les compteurs et la présence des logs :
   ```bash
   sudo -u zeek /opt/zeek/bin/zeekctl netstats
   sudo -u zeek /opt/zeek/bin/zeekctl status
   sudo ls -lah /opt/zeek/logs/current
   ```
   👉 Explication : `conn.log` et les logs de protocoles observés doivent apparaître.

2. Lire un échantillon de `conn.log` et comparer avec un flux connu et autorisé :
   ```bash
   sudo head -n 20 /opt/zeek/logs/current/conn.log
   ```
   👉 Explication : vérifie UID, adresses, ports et horodatages.

3. Essai hors ligne avec une capture PCAP légale de laboratoire (`capture.pcap` est un exemple à remplacer) :
   ```bash
   install -d -m 0700 "$HOME/zeek-pcap-test"
   cd "$HOME/zeek-pcap-test"
   /opt/zeek/bin/zeek -r /chemin/autorise/capture.pcap LogAscii::use_json=T
   ```
   👉 Explication : rejoue la capture sans surveiller d'interface; comparer avec la documentation du PCAP.

## 2. Production — Contrôles

Résultat de validation consigné, avec le flux de référence utilisé.

## 3. Production — Sécurité

- Protéger les logs comme des données réseau sensibles.
- Ne pas utiliser un PCAP d'un réseau tiers sans autorisation écrite.

## Validation et retour arrière

- **Validation** : Un flux autorisé connu apparaît dans `conn.log` avec les bons champs.
- **Retour arrière** : Supprimer le répertoire d'essai `$HOME/zeek-pcap-test`.

## Si le problème n'est pas résolu

- [Zeek — démarrage et logs](https://docs.zeek.org/en/stable/quickstart.html)
- [Zeek — logs](https://docs.zeek.org/en/stable/logs/index.html)
- [Guide complet Zeek 8 LTS Debian 13](/02-fiches-completes/debian/13/installation-deploiement/72-deploiement-zeek-8-lts-debian-13#6-valider-les-logs-avec-du-trafic-autorise)