# Fiche_Simple_-_VM_Rocky_9_Suricata_Installer

- **Environnement** : VM Rocky Linux 9 dédiée à Suricata
- **OS / Version** : Rocky Linux 9 (compatible RHEL 9); version des paquets à vérifier sur l’hôte
- **Catégorie** : Suricata / installation
- **Tags** : `suricata`, `rocky9`, `vie-du-logiciel`, `installer`

---

## Problème précis à résoudre

Installer Suricata depuis les dépôts de Rocky Linux 9 avec EPEL.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier le candidat :
   ```bash
   sudo dnf install epel-release
   sudo dnf makecache
   dnf info suricata
   ```
   👉 Explication : Suricata est fourni par EPEL 9; vérifier la version publiée. Le dépôt COPR de l’OISF est une alternative à valider par la politique de dépôts.

2. Installer et consigner la version :
   ```bash
   sudo dnf install suricata jq
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
- **Retour arrière** : Désinstaller : `sudo dnf remove suricata` (conserver `/etc/suricata` si une sauvegarde est nécessaire).

## Si le problème n’est pas résolu

- [Suricata — documentation officielle](https://docs.suricata.io/en/latest/)
- [Fiche d’entrée du logiciel](../../../../Logiciels/04-Reseau-et-cybersecurite/Fiche_Logiciel_-_Suricata.md)
- [Étape suivante du guide](./Fiche_Simple_-_VM_Rocky_9_Suricata_Configurer.md)
- [Étape précédente du guide](./Fiche_Simple_-_VM_Rocky_9_Suricata_Prerequis_Limites.md)
