---
title: "Suricata"
description: "Installer Suricata en IDS passif sur une interface miroir autorisée, mettre à jour les règles, vérifier la configuration et la remontée d'une alerte de test. Cette fiche ne configure ni NFQUEUE ni mode inline, et ne crée aucune règle drop ou reject. Les tests ne se font que sur votre propre réseau d"
published: true
date: 2026-10-29T12:23:21Z
tags: ["[debian-12]", "[suricata]", "[ids]", "[hardening]"]
editor: markdown
dateCreated: 2026-10-29T12:23:21Z
dateModified: 2026-10-29T12:23:21Z
---

# 📄 Suricata

- **Environnement** : VM (Debian 12)
- **OS / Version** : Debian 12 (bookworm)
- **Version** : Suricata 6.0.x (paquet `suricata` de bookworm ; une version plus récente en bookworm-backports est possible, à vérifier avec `apt-cache policy suricata`)
- **Catégorie** : Réseau et cybersécurité
- **Tags** : `[debian-12]`, `[suricata]`, `[ids]`, `[hardening]`

## 🎯 Objectif
Installer Suricata en IDS passif sur une interface miroir autorisée, mettre à jour les règles, vérifier la configuration et la remontée d'une alerte de test. Cette fiche ne configure ni NFQUEUE ni mode inline, et ne crée aucune règle `drop` ou `reject`. Les tests ne se font que sur votre propre réseau de laboratoire.

---

## 🧪 1. Hors-Production (laboratoire)
1. Installation de Suricata et des outils de mise à jour des règles :
```bash
sudo apt update
sudo apt install -y suricata suricata-update jq
```
👉 Explication : `suricata-update` télécharge les règles, `jq` lit les journaux JSON. La disponibilité de `suricata-update` dans bookworm est à vérifier ; sinon, utiliser bookworm-backports.

2. Vérification des versions et de l'interface :
```bash
suricata -V
suricata-update -V
ip -br address
```
👉 Explication : Confirme la version installée et repère l'interface miroir, par exemple `ens33`, distincte de l'interface de gestion.

3. Configuration de l'interface et du réseau interne :
```bash
sudo cp -a /etc/suricata/suricata.yaml /etc/suricata/suricata.yaml.pre-lab
sudo nano /etc/suricata/suricata.yaml
```
Dans le fichier, régler les valeurs suivantes :
```yaml
vars:
  address-groups:
    HOME_NET: "[192.168.10.0/24]"
af-packet:
  - interface: ens33
```
👉 Explication : Le fichier d'origine est sauvegardé. `HOME_NET` doit contenir uniquement les réseaux internes autorisés. Dans la section `af-packet`, remplacer la valeur d'exemple par l'interface miroir réelle.

4. Règle locale de test :
```bash
sudo nano /var/lib/suricata/rules/local.rules
```
Ajouter cette ligne, puis dans `suricata.yaml` ajouter `- local.rules` sous `rule-files:` :
```
alert icmp any any -> $HOME_NET any (msg:"LAB ICMP echo vers HOME_NET"; itype:8; sid:1000001; rev:1;)
```
👉 Explication : Règle de laboratoire qui signale un ping vers le réseau interne. Le fichier se trouve dans le répertoire de règles par défaut, et `suricata-update` ne le modifie pas. Le `sid` 1000001 est réservé aux règles locales.

5. Téléchargement des règles et test de la configuration :
```bash
sudo suricata-update
sudo suricata -T -c /etc/suricata/suricata.yaml -v
```
👉 Explication : `suricata-update` produit `/var/lib/suricata/rules/suricata.rules`. Le test `-T` doit afficher `Configuration provided was successfully loaded. Exiting.` Ne pas démarrer le service si une erreur YAML ou de règle apparaît.

6. Démarrage du service et contrôle :
```bash
sudo systemctl enable suricata
sudo systemctl restart suricata
systemctl status suricata --no-pager
```
👉 Explication : Le service Debian lit l'interface dans `/etc/default/suricata` (variable `IFACE`, à vérifier avec `systemctl cat suricata.service`). La ligne `Active: active (running)` est attendue.

7. Génération d'un ping depuis une autre machine du laboratoire, puis lecture de l'alerte :
```bash
ping -c 3 192.168.10.20
sudo tail -n 5 /var/log/suricata/fast.log
sudo tail -n 200 /var/log/suricata/eve.json | jq -c 'select(.event_type == "alert") | .alert.signature'
```
👉 Explication : L'adresse `192.168.10.20` est un exemple interne. La signature `LAB ICMP echo vers HOME_NET` doit apparaître dans `fast.log` et dans `eve.json`, ce qui confirme la remontée d'alerte.

---

## ⚡ 2. Production — Façon Simplifiée
1. Mise à jour des règles puis test de configuration :
```bash
sudo suricata-update list-sources --enabled
sudo suricata-update
sudo suricata -T -c /etc/suricata/suricata.yaml -v
```
👉 Explication : Liste les sources activées, met à jour les règles, puis valide la configuration. Ne pas activer de source tierce non relue.

2. Redémarrage après mise à jour :
```bash
sudo systemctl restart suricata
systemctl status suricata --no-pager
sudo journalctl -u suricata --since "10 minutes ago" --no-pager
```
👉 Explication : Recharge le service avec les nouvelles règles, puis contrôle son état et les erreurs récentes.

3. Vérification de la remontée des alertes :
```bash
ping -c 3 192.168.10.20
sudo tail -n 20 /var/log/suricata/fast.log
```
👉 Explication : Contrôle qu'une alerte de test apparaît après redémarrage. Les alertes réelles sont relues et corrélées avant toute action.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Restriction des droits sur la configuration :
```bash
sudo chmod 640 /etc/suricata/suricata.yaml
ls -l /etc/suricata/suricata.yaml
```
👉 Explication : Le fichier n'est plus lisible par tout utilisateur. Le service démarre sous `root` puis lit ce fichier avant tout changement de compte ; à vérifier sur la version déployée.

2. Vérification que l'interface miroir n'a pas d'adresse IP :
```bash
ip -br address show ens33
```
👉 Explication : L'interface de capture doit être dédiée à l'écoute passive. Aucune adresse ne doit lui être attribuée.

3. Désactivation des sorties PCAP et payload non nécessaires :
```bash
sudo grep -n -A2 "pcap-log:" /etc/suricata/suricata.yaml
```
👉 Explication : Affiche la section `pcap-log`. Elle doit rester `enabled: no` sauf besoin approuvé, car une capture contient des données sensibles. Modifier le fichier seulement après validation.

4. Protection du répertoire des journaux :
```bash
sudo chmod 750 /var/log/suricata
sudo ls -ld /var/log/suricata
```
👉 Explication : Les journaux `eve.json` contiennent adresses, noms et métadonnées réseau. Seuls `root` et le groupe propriétaire peuvent les lire.

5. Contrôle des erreurs du moteur :
```bash
sudo tail -n 50 /var/log/suricata/suricata.log
sudo grep -i -E "error|warn" /var/log/suricata/suricata.log | tail -n 10
```
👉 Explication : Repère les erreurs de capture, de règles ou de permissions. Une perte de paquets répétée signale un problème de dimensionnement ou de miroir.

6. Sauvegarde de la configuration et des règles :
```bash
sudo tar czf /root/suricata-conf-$(date +%F).tgz /etc/suricata /var/lib/suricata/rules
sudo ls -l /root/suricata-conf-*.tgz
```
👉 Explication : Archive datée de la configuration et des règles. La stocker hors du serveur, dans un emplacement protégé, car elle décrit le réseau interne.

---