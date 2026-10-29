# Fiche_Simple_-_VM_Debian_13_Suricata_IDS_Config_AF_Packet.md

- **Environnement** : VM Debian 13 avec Suricata installé
- **OS / Version** : Debian 13 Trixie; Suricata 8.0.7 et suricata-update (Debian Backports)
- **Catégorie** : detection reseau / configuration
- **Tags** : `suricata`, `debian13`, `af-packet`, `yaml`

---

## Problème précis à résoudre

Configurer HOME_NET et la capture AF_PACKET sans mode inline.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder le fichier initial :
   ```bash
   sudo cp -a /etc/suricata/suricata.yaml /etc/suricata/suricata.yaml.pre-lab
   ```
   👉 Explication : on garde une copie pour revenir en arrière.

2. Éditer le fichier de configuration :
   ```bash
   sudo nano /etc/suricata/suricata.yaml
   ```
   👉 Explication : on y règle `HOME_NET` et la section `af-packet`.

3. Adapter ces blocs (réseaux et interface `enp2s0` d'exemple à remplacer par vos CIDR et votre interface) :
   ```bash
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
   👉 Explication : `HOME_NET` liste les réseaux internes autorisés; AF_PACKET écoute passivement l'interface choisie. Garder désactivés payload, PCAP et extraction de fichiers sauf besoin approuvé.

4. Vérifier que l'unité n'ajoute pas de capture active :
   ```bash
   systemctl cat suricata.service
   ```
   👉 Explication : il ne doit pas y avoir `-q` (NFQUEUE) ni autre mode inline.

## 2. Production — Contrôles

Faire relire `HOME_NET`, l'interface et les sorties activées; versionner le fichier de configuration.

## 3. Production — Sécurité

- Ne pas capturer sur l'interface de gestion.
- Garder désactivés payload, PCAP et extraction de fichiers sauf besoin approuvé.
- Pas de mode IPS.

## Validation et retour arrière

- **Validation** : `suricata.yaml` modifié et testé à l'étape suivante.
- **Retour arrière** : `sudo cp -a /etc/suricata/suricata.yaml.pre-lab /etc/suricata/suricata.yaml`.

## Si le problème n'est pas résolu

- [Suricata — configuration YAML](https://docs.suricata.io/en/latest/configuration/suricata-yaml.html)
- [Suricata — AF_PACKET](https://docs.suricata.io/en/latest/capture-hardware/af-packet.html)
- [Guide complet Suricata Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/71_Deploiement_Suricata_8_Debian_13_Backports.md#4-configurer-afpacket-en-ecoute-passive)
