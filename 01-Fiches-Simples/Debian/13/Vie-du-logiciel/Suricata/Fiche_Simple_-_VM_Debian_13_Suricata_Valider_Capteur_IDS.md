# Fiche_Simple_-_VM_Debian_13_Suricata_Valider_Capteur_IDS.md

- **Environnement** : Suricata 8.0.7 depuis Debian 13 Backports, sonde passive autorisée
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : Détection réseau / IDS
- **Tags** : `debian13`, `suricata`, `backports`, `ids`, `af-packet`, `eve-json`, `test`

---

## Problème précis à résoudre

Vérifier que Suricata reçoit du trafic d'une interface miroir approuvée, charge les règles et écrit des événements sans bloquer ni modifier les flux.

## 1. Hors-Production (Lab / Test / POC)

1. Confirmer l'interface miroir et séparer capture et gestion :
   ```bash
   ip -br link
   ip -s link show INTERFACE_MIROIR
   ```
   👉 Explication : remplacer l'interface; consigner VLAN et CIDR surveillés.

2. Vérifier version, configuration et unité :
   ```bash
   suricata --build-info | head -5
   systemctl cat suricata | head -15
   ```
   👉 Explication : repérer l'unité réellement utilisée et l'interface configurée dans `/etc/suricata/suricata.yaml` (`af-packet`).

3. Mettre à jour et tester les règles :
   ```bash
   sudo suricata-update
   sudo suricata -T -c /etc/suricata/suricata.yaml
   ```
   👉 Explication : `-T` valide la configuration sans démarrer le capteur.

4. Démarrer et contrôler :
   ```bash
   sudo systemctl enable --now suricata
   systemctl --no-pager status suricata
   sudo journalctl -u suricata --since '-10 minutes' --no-pager
   sudo tail -n 5 /var/log/suricata/stats.log
   sudo jq -c 'select(.event_type=="flow")' /var/log/suricata/eve.json | tail -3
   ```
   👉 Explication : générer un flux connu du lab puis constater les événements dans `eve.json`.

5. Vérifier le mode passif :
   ```bash
   grep -nE 'nfqueue|ips|drop' /etc/suricata/suricata.yaml | grep -v '^\s*#' | head
   sudo iptables -S 2>/dev/null | grep -i nfqueue || echo "aucune NFQUEUE"
   ```
   👉 Explication : aucun mode inline ni action de blocage activés.

## 2. Production — Contrôles

Surveiller perte de paquets, CPU, rotation/rétention, règles, événements EVE et stabilité de l'interface de capture. Mettre à jour les règles après revue et test de chargement.

## 3. Production — Sécurité

- Capturer exclusivement les réseaux approuvés et limiter les droits sur PCAP, EVE et journaux.
- Éviter la journalisation de payload et l'extraction de fichiers par défaut.
- Transporter EVE JSON vers le SIEM avec TLS et compte de service minimal.
- Un IDS passif alerte mais n'est ni un IPS ni une preuve isolée d'incident.

## Validation et retour arrière

- **Validation** : service actif, compteurs de capture en hausse, règles chargées, événements visibles, trafic métier inchangé.
- **Retour arrière** : arrêter le service, retirer la configuration de l'interface miroir et restaurer le fichier YAML sauvegardé.

## Si le problème n'est pas résolu

- [Suricata — Quickstart](https://docs.suricata.io/en/latest/quickstart.html)
- [Suricata — options de ligne de commande](https://docs.suricata.io/en/latest/command-line-options.html)
- [Guide complet Suricata IDS Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/71_Deploiement_Suricata_8_Debian_13_Backports.md)