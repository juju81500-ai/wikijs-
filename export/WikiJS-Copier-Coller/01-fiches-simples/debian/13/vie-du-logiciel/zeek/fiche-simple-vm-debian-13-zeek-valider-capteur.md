# Fiche_Simple_-_VM_Debian_13_Zeek_Valider_Capteur.md

- **Environnement** : Zeek 8.0 LTS, Debian 13, nœud standalone et interface miroir autorisée
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : Analyse passive réseau

---

## Problème précis à résoudre

Confirmer que Zeek reçoit les paquets d'une interface miroir approuvée, tourne sous un compte dédié et génère des logs lisibles sans modifier le trafic.

## 1. Hors-Production (Lab / Test / POC)

1. Confirmer l'interface de capture et les réseaux suivis :
   ```bash
   ip -br link
   ```
   👉 Explication : relever l'interface miroir/TAP; consigner VLAN visibles et CIDR dans `networks.cfg`.

2. Vérifier la version et AF_PACKET :
   ```bash
   /opt/zeek/bin/zeek --version
   /opt/zeek/bin/zeek -N Zeek::AF_Packet
   ```
   👉 Explication : adapter le préfixe `/opt/zeek` à l'installation.

3. Configurer un nœud standalone :
   ```bash
   sudo tee /opt/zeek/etc/node.cfg >/dev/null <<'EOF'
   [zeek]
   type=standalone
   host=localhost
   interface=af_packet::INTERFACE_MIROIR
   EOF
   ```
   👉 Explication : remplacer l'interface; elle est séparée du réseau de gestion.

4. Vérifier et déployer :
   ```bash
   sudo -u zeek /opt/zeek/bin/zeekctl check
   sudo -u zeek /opt/zeek/bin/zeekctl deploy
   sudo -u zeek /opt/zeek/bin/zeekctl status
   ```
   👉 Explication : le compte de service doit être celui prévu; `Running` attendu.

5. Contrôler les journaux après un flux de test autorisé :
   ```bash
   sudo -u zeek /opt/zeek/bin/zeekctl netstats
   sudo tail -5 /opt/zeek/logs/current/conn.log
   ```
   👉 Explication : des lignes de connexion doivent apparaître; vérifier aussi `dns.log` et `http.log`.

## 2. Production — Contrôles

Surveiller pertes de capture, CPU, rotation/rétention des logs, espace disque et état ZeekControl. Tester les changements de scripts et de ligne LTS sur un capteur de recette avant `deploy` en production.

## 3. Production — Sécurité

- Capturer uniquement les segments autorisés; limiter la lecture des logs qui révèlent des métadonnées réseau.
- Exécuter ZeekControl sous un compte dédié et accorder uniquement les capacités de capture nécessaires.
- Éviter la capture de contenu ou l'extraction de fichiers sans approbation et règles de rétention.
- Un capteur Zeek n'est ni un IPS ni un moteur d'alertes à signatures équivalent à Suricata/Snort.

## Validation et retour arrière

- **Validation** : nœud `running`, compteurs de capture en hausse, logs frais et cohérents, aucune perturbation réseau.
- **Retour arrière** : `zeekctl stop`, restaurer les fichiers de configuration sauvegardés et retirer l'interface du miroir si nécessaire.

## Si le problème n'est pas résolu

- [Zeek — quick start](https://docs.zeek.org/en/stable/quickstart.html)
- [Zeek — déploiement et interface AF_PACKET](https://docs.zeek.org/en/stable/cluster-setup.html)
- [Guide complet Zeek 8 LTS Debian 13](/02-fiches-completes/debian/13/installation-deploiement/72-deploiement-zeek-8-lts-debian-13)