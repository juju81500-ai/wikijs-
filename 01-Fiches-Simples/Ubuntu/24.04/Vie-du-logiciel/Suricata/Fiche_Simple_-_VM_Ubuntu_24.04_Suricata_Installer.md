# Fiche_Simple_-_VM_Ubuntu_24.04_Suricata_Installer

- **Environnement** : VM Ubuntu Server 24.04 LTS dédiée à Suricata
- **OS / Version** : Ubuntu Server 24.04 LTS (Noble Numbat); version des paquets à vérifier sur l’hôte
- **Catégorie** : Suricata / installation
- **Tags** : `suricata`, `ubuntu24.04`, `vie-du-logiciel`, `installer`

---

## Problème précis à résoudre

Installer Suricata depuis les dépôts de Ubuntu 24.04 (universe).

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier le candidat :
   ```bash
   sudo apt update
   apt-cache policy suricata
   ```
   👉 Explication : La version d’Ubuntu 24.04 peut être en retrait de l’amont; vérifier la version publiée. Le PPA OISF (`ppa:oisf/suricata-stable`) est une alternative officielle à n’utiliser qu’après validation de la politique de dépôts.

2. Installer et consigner la version :
   ```bash
   sudo apt install suricata jq
   suricata --build-info | head -n 20
   suricata -V
   ```
   👉 Explication : Installe le moteur, suricata-update et jq (lecture des journaux JSON). `--build-info` montre les fonctions compilées dont AF_PACKET.

3. Ne pas démarrer avant configuration :
   ```bash
   sudo systemctl disable --now suricata 2>/dev/null; systemctl is-enabled suricata
   ```
   👉 Explication : Évite un démarrage avec la configuration par défaut non adaptée.

## 2. Production — Contrôles

Consigner version, origine, interface prévue et chemins : `/etc/suricata`, `/var/lib/suricata`, `/var/log/suricata`.

## 3. Production — Sécurité

- Installer depuis un dépôt signé uniquement.
- Ne pas activer IPS/NFQUEUE.

## Validation et retour arrière

- **Validation** : `suricata -V` répond, AF_PACKET est listé dans la build.
- **Retour arrière** : Désinstaller : `sudo apt remove suricata` (conserver `/etc/suricata` si une sauvegarde est nécessaire).

## Si le problème n’est pas résolu

- [Suricata — documentation officielle](https://docs.suricata.io/en/latest/)
- [Fiche d’entrée du logiciel](../../../../Logiciels/04-Reseau-et-cybersecurite/Fiche_Logiciel_-_Suricata.md)
- [Étape suivante du guide](./Fiche_Simple_-_VM_Ubuntu_24.04_Suricata_Configurer.md)
- [Étape précédente du guide](./Fiche_Simple_-_VM_Ubuntu_24.04_Suricata_Prerequis_Limites.md)
