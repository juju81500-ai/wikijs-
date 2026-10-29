# Fiche_Simple_-_VM_Debian_13_Vie_Systeme_41_Supervision_Metriques_Et_Inventaire

- **Environnement** : VM Debian 13 « trixie » (serveur)
- **OS / Version** : Debian 13; étape 41 sur 50 de la vie du système
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
   sudo nft add rule inet filter input ip saddr 192.0.2.50 tcp dport 9100 accept
   ```
   👉 Explication : remplacer l'IP; suppose une table `inet filter` avec une chaîne `input`.

## 2. Production — Contrôles

Alertes sur disque, mémoire, service et certificat.

## 3. Production — Sécurité

Ne pas exposer l'exporteur à tout le réseau.

## Validation et retour arrière

- **Validation** : La cible apparaît `UP` dans la supervision.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Debian 13](/01-fiches-simples/debian/13/vie-du-systeme/sommaire-vie-du-systeme-debian-13)
- [Documentation officielle](https://www.debian.org/doc/)