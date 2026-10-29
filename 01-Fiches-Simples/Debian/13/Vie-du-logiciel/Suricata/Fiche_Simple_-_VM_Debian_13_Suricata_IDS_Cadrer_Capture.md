# Fiche_Simple_-_VM_Debian_13_Suricata_IDS_Cadrer_Capture.md

- **Environnement** : VM Debian 13 dédiée avec interface de gestion et interface de capture
- **OS / Version** : Debian 13 Trixie; Suricata 8.0.7 et suricata-update (Debian Backports)
- **Catégorie** : detection reseau / cadrage
- **Tags** : `suricata`, `debian13`, `ids`, `cadrage`

---

## Problème précis à résoudre

Cadrer l'observation passive et obtenir les autorisations avant d'installer la sonde.

## 1. Hors-Production (Lab / Test / POC)

1. Lister les interfaces pour distinguer gestion et capture :
   ```bash
   ip -br address
   ```
   👉 Explication : l'interface de capture doit être indépendante de celle de gestion.

2. Noter par écrit les sous-réseaux internes autorisés, la source de trafic (SPAN, TAP ou pcap) et l'approbation du propriétaire réseau.
   👉 Explication : ces CIDR serviront à renseigner `HOME_NET`; les captures peuvent contenir des données sensibles.

3. Contrôler les versions candidates après activation de `trixie-backports` :
   ```bash
   sudo apt update
   apt-cache policy suricata suricata-update
   ```
   👉 Explication : Trixie stable référence Suricata 7.0.10; Backports fournit 8.0.7. On utilise un jeu cohérent depuis Backports, sans compilation manuelle.

## 2. Production — Contrôles

Obtenir l'approbation du propriétaire réseau, définir la rétention et la sensibilité des données capturées.

## 3. Production — Sécurité

- Observation passive uniquement : pas de NFQUEUE, de bridge inline ni de règles `drop`/`reject`.
- Ne capturer que des réseaux autorisés.
- Les captures sont des données sensibles.

## Validation et retour arrière

- **Validation** : Périmètre, autorisation et versions candidates documentés.
- **Retour arrière** : Aucune modification n'a été faite; abandonner le projet si l'autorisation manque.

## Si le problème n'est pas résolu

- [Suricata — installation Debian](https://docs.suricata.io/en/latest/install/debian.html)
- [Suricata — démarrage rapide](https://docs.suricata.io/en/latest/quickstart.html)
- [Guide complet Suricata Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/71_Deploiement_Suricata_8_Debian_13_Backports.md#1-definir-le-perimetre-de-capture)
