---
title: "Déployer Suricata 8.0.7 en IDS passif sur Debian 13"
description: "Fiche simple : [définir le périmètre de capture](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Suricata/FicheSimple-VMDebian13SuricataIDSCadrerCapture.md)."
published: true
date: 2026-10-29T20:14:10Z
tags: ["suricata", "debian13", "backports", "ids", "af-packet", "eve-json", "et-open"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Déployer Suricata 8.0.7 en IDS passif sur Debian 13

- **OS / Version** : Debian 13 Trixie avec Suricata 8.0.7 et suricata-update Debian Backports
- **Type de fiche** : Installation/Déploiement
- **Périmètre** : sonde IDS passive AF_PACKET sur une interface miroir autorisée; aucune action IPS
- **Catégorie** : Détection réseau et analyse d'événements
- **Tags** : `suricata`, `debian13`, `backports`, `ids`, `af-packet`, `eve-json`, `et-open`

## 1. Définir le périmètre de capture

Fiche simple : [définir le périmètre de capture](/01-fiches-simples/debian/13/vie-du-logiciel/suricata/fiche-simple-vm-debian-13-suricata-ids-cadrer-capture).

Suricata peut analyser des captures hors ligne, fonctionner en IDS passif ou agir comme IPS inline. Cette fiche n'autorise que l'observation passive d'un réseau dont l'organisation possède ou a explicitement autorisé la supervision. Elle ne configure ni NFQUEUE, ni bridge inline, ni règles `drop`/`reject`.

Prérequis : VM Debian 13 dédiée avec une interface de gestion et une interface de capture indépendante; une source de trafic approuvée (port miroir/SPAN, TAP ou pcap de laboratoire); assez de stockage pour les journaux; et une liste des sous-réseaux internes autorisés à placer dans `HOME_NET`. Un hôte avec une seule interface de gestion ne suffit pas pour reproduire une sonde réseau fidèle. Obtenir l'approbation du propriétaire réseau avant d'activer le port miroir : les captures peuvent contenir des données sensibles.

Debian Trixie stable référence Suricata 7.0.10; Trixie Backports fournit la génération 8.0.7 au moment de la rédaction. Utiliser une paire de paquets cohérente depuis Backports, sans mélange de fichiers de configuration ni compilation manuelle.

## 2. Vérifier la version candidate et installer

Fiche simple : [installer Suricata depuis Backports](/01-fiches-simples/debian/13/vie-du-logiciel/suricata/fiche-simple-vm-debian-13-suricata-ids-installer).

Activer le dépôt officiel `trixie-backports` selon la documentation Debian, puis contrôler les versions candidates :

```bash
sudo apt update
apt-cache policy suricata suricata-update
```

Pour ce guide, les versions attendues sont Suricata `1:8.0.7-1~bpo13+1` et suricata-update `1.3.8-1~bpo13+1`. Si ces versions ne sont plus les candidates ou ne proviennent pas de Trixie Backports, relever les versions réellement disponibles et suivre la documentation correspondante avant de continuer.

```bash
sudo apt install -t trixie-backports suricata suricata-update jq
suricata --build-info
suricata-update -V
systemctl cat suricata.service
```

Lire l'unité systemd fournie par le paquet pour comprendre les arguments et le mode de démarrage avant de la modifier. Ne pas remplacer l'unité du paquet par un exemple d'une autre distribution.

## 3. Identifier l'interface et limiter la visibilité

Fiche simple : [identifier l'interface de capture](/01-fiches-simples/debian/13/vie-du-logiciel/suricata/fiche-simple-vm-debian-13-suricata-ids-interface).

Repérer l'interface de capture et sa topologie; vérifier qu'elle est bien séparée du réseau de gestion :

```bash
ip -br address
ip -d link show
```

L'interface miroir ne doit recevoir que le trafic que l'organisation a approuvé. Documenter le sens du miroir et les VLAN visibles, et éviter les ports de gestion/hyperviseur. Sur une VM, valider auprès de l'équipe virtualisation que le pont ou vSwitch délivre réellement le trafic miroir et le mode promiscuous autorisé; une interface virtuelle n'observe pas spontanément les flux des autres VM.

## 4. Configurer AF_PACKET en écoute passive

Fiche simple : [configurer AF_PACKET passif](/01-fiches-simples/debian/13/vie-du-logiciel/suricata/fiche-simple-vm-debian-13-suricata-ids-config-af-packet).

Sauvegarder le fichier initial avant modification :

```bash
sudo cp -a /etc/suricata/suricata.yaml /etc/suricata/suricata.yaml.pre-lab
```

Dans `/etc/suricata/suricata.yaml`, régler `HOME_NET` sur les seuls réseaux internes autorisés et configurer l'interface de capture existante dans la section `af-packet`. Exemple à adapter :

```yaml
vars:
  address-groups:
    HOME_NET: "[10.40.0.0/16,192.0.2.0/24]"
    EXTERNAL_NET: "!$HOME_NET"

af-packet:
  - interface: enp2s0
    cluster-id: 99
    cluster-type: cluster_flow
    tpacket-v3: yes
```

Les réseaux ci-dessus sont des exemples documentaires; remplacer par les CIDR réellement autorisés. Ne pas capturer sur l'interface de gestion. En mode `af-packet` sans configuration de copie/inline, Suricata inspecte le trafic vu sur la sonde sans être le chemin de transfert des paquets. Garder les sorties payload/PCAP et l'extraction de fichiers désactivées sauf besoin approuvé, car elles stockent des données réseau sensibles.

Vérifier que le mode de lancement utilisé par l'unité Debian correspond à cette section YAML et n'ajoute pas `-q` (NFQUEUE) ou une autre capture active :

```bash
systemctl cat suricata.service
```

## 5. Mettre à jour et valider les règles

Fiche simple : [mettre à jour et valider les règles](/01-fiches-simples/debian/13/vie-du-logiciel/suricata/fiche-simple-vm-debian-13-suricata-ids-regles).

`suricata-update` utilise par défaut le jeu Emerging Threats Open, sans clé payante. Consulter les sources activées, puis télécharger et fusionner les règles :

```bash
sudo suricata-update list-sources --enabled
sudo suricata-update
```

Le fichier produit est généralement `/var/lib/suricata/rules/suricata.rules`. Confirmer dans `suricata.yaml` que `default-rule-path` et `rule-files` désignent ce chemin. Ne pas activer des sources tierces inconnues ou des règles non relues.

Tester la configuration et le chargement complet des règles avant de démarrer ou redémarrer le service :

```bash
sudo suricata -T -c /etc/suricata/suricata.yaml
```

Ne pas continuer si la commande retourne une erreur YAML, un SID invalide, un fichier de règles absent ou une interface inconnue.

## 6. Démarrer le service et contrôler l'observation

Fiche simple : [démarrer et contrôler l'observation](/01-fiches-simples/debian/13/vie-du-logiciel/suricata/fiche-simple-vm-debian-13-suricata-ids-demarrer-observer).

Activer l'unité fournie par Debian et inspecter les journaux :

```bash
sudo systemctl enable --now suricata.service
sudo systemctl --no-pager --full status suricata.service
sudo journalctl -u suricata.service -b --no-pager
```

Après génération de trafic légitime sur le réseau de laboratoire, vérifier que les compteurs évoluent et que les événements JSON sont lisibles :

```bash
sudo tail -n 50 /var/log/suricata/suricata.log
sudo jq -c 'select(.event_type == "stats")' /var/log/suricata/eve.json | tail -n 5
```

Pour valider la chaîne de règles sans toucher un réseau externe, traiter un pcap issu d'un test autorisé et stocké dans un répertoire protégé :

```bash
sudo install -d -o suricata -g suricata -m 0750 /var/tmp/suricata-lab
sudo -u suricata suricata -T -c /etc/suricata/suricata.yaml
```

Un test de configuration confirme le chargement des règles, pas le fonctionnement de la carte miroir. Pour un test fonctionnel, faire jouer un pcap de laboratoire approuvé avec `suricata -r <capture.pcap> -c /etc/suricata/suricata.yaml -l /var/tmp/suricata-lab`, puis lire uniquement les alertes et stats générées. Protéger la capture et les sorties comme des données sensibles.

## 7. Exploitation et durcissement

Fiche simple : [exploiter et durcir la sonde](/01-fiches-simples/debian/13/vie-du-logiciel/suricata/fiche-simple-vm-debian-13-suricata-ids-exploitation).

- Garder le capteur et les règles à jour; relire les changements et exécuter `suricata -T` avant chaque redémarrage après mise à jour.
- Surveiller la perte de paquets, la charge CPU, l'espace disque, la rotation des journaux, les changements d'interface et le retard des règles.
- Transférer EVE JSON vers un collecteur uniquement via un canal chiffré et un compte à privilèges minimaux; définir une durée de rétention conforme à la politique de données.
- Évaluer les alertes en contexte et ajuster localement seuils/exclusions approuvés; une signature n'établit pas à elle seule qu'une intrusion a eu lieu.
- Ne jamais passer en IPS inline ou activer des règles de blocage sans conception, fenêtre de changement, chemin de retour et test isolé distincts.
- Surveiller Suricata, Zeek et Snort comme outils complémentaires, sans supposer qu'un capteur passif constitue à lui seul un IDS complet ou une réponse à incident.

## Sources

- [Debian Backports — paquet Suricata 8.0.7](https://manpages.debian.org/trixie-backports/suricata/suricata.1.en.html)
- [Debian Backports — paquet suricata-update 1.3.8](https://manpages.debian.org/trixie-backports/suricata-update/suricata-update.1.en.html)
- [Suricata — installation de paquets Debian](https://docs.suricata.io/en/latest/install/debian.html)
- [Suricata — guide de démarrage et configuration IDS](https://docs.suricata.io/en/latest/quickstart.html)
- [Suricata — configuration YAML et EVE JSON](https://docs.suricata.io/en/latest/configuration/suricata-yaml.html)
- [Suricata — documentation AF_PACKET](https://docs.suricata.io/en/latest/capture-hardware/af-packet.html)
- [Suricata — gestion des règles et suricata-update](https://docs.suricata.io/en/latest/rule-management/suricata-update.html)
- [Suricata — options CLI et validation `-T`](https://docs.suricata.io/en/latest/command-line-options.html)
- [OISF — démarrage rapide de suricata-update](https://suricata-update.readthedocs.io/en/latest/quickstart.html)

Aucune sonde ou capture réelle n'a été exécutée par cette fiche. L'installation des paquets, le service systemd et l'observation d'un port miroir restent à éprouver dans le réseau cible autorisé.