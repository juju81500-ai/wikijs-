# Fiche_Simple_-_VM_Ubuntu_24.04_Vie_Systeme_41_Supervision_Metriques_Et_Inventaire

- **Environnement** : VM Ubuntu Server 24.04 LTS « noble »
- **OS / Version** : Ubuntu 24.04; étape 41 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Superviser la machine.

## 1. Hors-Production (Lab / Test / POC)

1. Installer un agent (exemple node_exporter) :
   ```bash
   sudo apt install prometheus-node-exporter
   sudo systemctl enable --now prometheus-node-exporter
   curl -s http://127.0.0.1:9100/metrics | head
   ```
   👉 Explication : expose les métriques système sur le port 9100.

2. Limiter l'accès au serveur de supervision :
   ```bash
   sudo ufw allow from 192.0.2.50 to any port 9100 proto tcp
   ```
   👉 Explication : remplacer l'IP du serveur de supervision.

## 2. Production — Contrôles

Alertes sur disque, mémoire, service et certificat.

## 3. Production — Sécurité

Ne pas exposer l'exporteur à tout le réseau.

## Validation et retour arrière

- **Validation** : La cible apparaît `UP` dans la supervision.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Fiche détaillée : VM Ubuntu 24.04 Supervision Zabbix Agent2](</01-fiches-simples/ubuntu/24-04/vie-du-logiciel/zabbix/fiche-simple-vm-ubuntu-24-04-supervision-zabbix-agent2>)
- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Ubuntu 24.04](/01-fiches-simples/ubuntu/24-04/vie-du-systeme/sommaire-vie-du-systeme-ubuntu-24-04)
- [Documentation officielle](https://documentation.ubuntu.com/server/)