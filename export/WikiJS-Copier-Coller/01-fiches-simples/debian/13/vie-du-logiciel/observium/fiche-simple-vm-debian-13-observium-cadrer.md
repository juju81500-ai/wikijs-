# Fiche_Simple_-_VM_Debian_13_Observium_Cadrer.md

- **Environnement** : Observium Community sur Debian 13 (Apache/PHP, MariaDB, SNMPv3)
- **OS / Version** : Debian 13 Trixie x86-64; Observium Community
- **Catégorie** : supervision réseau / cadrage

---

## Problème précis à résoudre

Vérifier le périmètre Community, les prérequis et le dimensionnement avant d'installer.

## 1. Hors-Production (Lab / Test / POC)

1. Relever la version du système et les ressources de la VM :
   ```bash
   cat /etc/os-release | head -3
   nproc && free -h && df -h /opt
   ```
   👉 Explication : repère publié : 2 cœurs, 4 Go de RAM et 20 Go SSD pour environ 50 appareils; adapter au volume réel de RRD.

2. Vérifier l'heure et la résolution DNS de la VM (nom d'exemple à remplacer) :
   ```bash
   timedatectl status | grep -E 'synchronized|NTP'
   getent hosts observium.mgmt.example
   ```
   👉 Explication : une heure fiable et un nom stable sont nécessaires aux graphiques et au certificat HTTPS.

3. Noter par écrit l'édition (Community uniquement), la liste des équipements pilotes, le réseau d'administration et le plan de sauvegarde.
   👉 Explication : les fonctions d'alerting avancées peuvent être réservées à l'édition Subscription; le périmètre doit le refléter.

## 2. Production — Contrôles

VM dédiée, adresse de gestion stable, NTP, certificat HTTPS, sauvegarde MariaDB/`config.php`/`rrd` et restauration testée.

## 3. Production — Sécurité

- Ne pas exposer l'interface sur Internet.
- Prévoir un accès web restreint au réseau d'administration.

## Validation et retour arrière

- **Validation** : prérequis relevés et périmètre écrit et validé.
- **Retour arrière** : aucune modification système à annuler.

## Si le problème n'est pas résolu

- [Observium — installation Debian/Ubuntu](https://docs.observium.org/install_debian/)
- [Observium — prérequis logiciels](https://docs.observium.org/software_requirements/)
- [Observium — ajouter un équipement](https://docs.observium.org/add_device/)
- [Guide complet — étape 1](/02-fiches-completes/debian/13/installation-deploiement/69-deploiement-observium-community-debian-13#1-definir-le-perimetre-et-dimensionner)