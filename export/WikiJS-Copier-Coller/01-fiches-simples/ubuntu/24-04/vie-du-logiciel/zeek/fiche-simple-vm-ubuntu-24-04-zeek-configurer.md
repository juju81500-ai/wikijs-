# Fiche_Simple_-_VM_Ubuntu_24.04_Zeek_Configurer

- **Environnement** : VM Ubuntu Server 24.04 LTS dédiée à Zeek
- **OS / Version** : Ubuntu Server 24.04 LTS (Noble Numbat); version des paquets à vérifier sur l’hôte
- **Catégorie** : Zeek / capteur passif standalone

---

## Problème précis à résoudre

Configurer et exploiter Zeek en capteur passif standalone sur l’interface autorisée.

## 1. Hors-Production (Lab / Test / POC)

1. Définir l’interface et le nœud :
   ```bash
   sudoedit /opt/zeek/etc/node.cfg
   ```
   👉 Explication : Dans le bloc `[zeek]` (standalone) : `type=standalone`, `host=localhost`, `interface=af_packet::INTERFACE_AUTORISEE`. INTERFACE_AUTORISEE est à remplacer.

2. Définir les réseaux locaux :
   ```bash
   sudoedit /opt/zeek/etc/networks.cfg
   ```
   👉 Explication : Y mettre LOCAL_NET_AUTORISE (CIDR, à remplacer) pour que Zeek distingue interne/externe.

3. Vérifier la configuration :
   ```bash
   sudo /opt/zeek/bin/zeekctl check
   ```
   👉 Explication : Contrôle syntaxe et scripts sans démarrer la capture.

4. Déployer et démarrer :
   ```bash
   sudo /opt/zeek/bin/zeekctl deploy
   sudo /opt/zeek/bin/zeekctl status
   ```
   👉 Explication : Installe la configuration et démarre le capteur; `status` doit indiquer `running`.

5. Observer les journaux :
   ```bash
   sudo ls -l /opt/zeek/logs/current
   sudo tail -n 5 /opt/zeek/logs/current/conn.log
   ```
   👉 Explication : Les journaux `conn.log`, `dns.log`, etc. alimentent l’analyse; `zeek-cut` aide à extraire des colonnes.

## 2. Production — Contrôles

Faire relire interface et réseaux locaux; surveiller l’espace disque et les pertes de paquets.

## 3. Production — Sécurité

- Aucune action de blocage.
- Journaux accessibles aux seuls comptes habilités.
- AppArmor : en cas de refus, `sudo journalctl -k | grep DENIED`.

## Validation et retour arrière

- **Validation** : Les journaux conn.log (et dns.log si du DNS est observé) sont produits sans erreur.
- **Retour arrière** : `sudo /opt/zeek/bin/zeekctl stop`, restaurer `node.cfg` et `networks.cfg` sauvegardés, puis `zeekctl deploy`.

## Si le problème n’est pas résolu

- [Zeek — documentation officielle](https://docs.zeek.org/en/master/install.html)
- [Fiche d’entrée du logiciel](/01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-zeek)
- [Étape suivante du guide](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/zeek/fiche-simple-vm-ubuntu-24-04-zeek-securiser)
- [Étape précédente du guide](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/zeek/fiche-simple-vm-ubuntu-24-04-zeek-installer)