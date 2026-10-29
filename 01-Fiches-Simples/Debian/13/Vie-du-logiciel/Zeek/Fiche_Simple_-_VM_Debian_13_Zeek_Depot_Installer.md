# Fiche_Simple_-_VM_Debian_13_Zeek_Depot_Installer.md

- **Environnement** : VM Debian 13 capteur passif Zeek standalone sur interface miroir approuvée
- **OS / Version** : Debian 13 Trixie; Zeek 8.0 LTS (dépôt OBS officiel)
- **Catégorie** : supervision / analyse passive du trafic
- **Tags** : `debian13`, `zeek`, `zeekctl`, `af-packet`, `network-monitoring`

---

## Problème précis à résoudre

Installer Zeek 8.0 LTS depuis le dépôt OBS officiel pour Debian 13.

## 1. Hors-Production (Lab / Test / POC)

1. Installer les prérequis et le répertoire de clés :
   ```bash
   sudo apt update
   sudo apt install -y ca-certificates curl gnupg libcap2-bin
   sudo install -d -m 0755 /etc/apt/keyrings
   ```
   👉 Explication : prépare l'import de la clé dans un keyring dédié.

2. Importer la clé et déclarer la source APT liée à ce keyring :
   ```bash
   curl -fsSL https://download.opensuse.org/repositories/security:/zeek/Debian_13/Release.key | sudo gpg --dearmor --yes -o /etc/apt/keyrings/zeek-obs.gpg
   echo 'deb [signed-by=/etc/apt/keyrings/zeek-obs.gpg] https://download.opensuse.org/repositories/security:/zeek/Debian_13/ /' | sudo tee /etc/apt/sources.list.d/zeek-obs.list
   ```
   👉 Explication : `signed-by` limite la confiance de la clé à ce seul dépôt.

3. Mettre à jour et vérifier que le candidat vient de `security:zeek` pour `Debian_13` :
   ```bash
   sudo apt update
   apt-cache policy zeek-8.0
   ```
   👉 Explication : contrôle l'origine avant installation.

4. Installer la ligne LTS et contrôler les binaires :
   ```bash
   sudo apt install zeek-8.0
   dpkg-query -W 'zeek*'
   command -v zeek
   command -v zeekctl
   zeek --version
   zeek -N Zeek::AF_Packet
   ```
   👉 Explication : les paquets OBS utilisent habituellement `/opt/zeek`; la dernière commande doit lister AF_PACKET. Si zeek n'est pas dans le `PATH`, ajouter `/opt/zeek/bin` au `PATH` plutôt que créer un lien dans `/usr/bin`.

## 2. Production — Contrôles

Figer la ligne LTS 8.0; documenter la source du dépôt et la procédure de mise à jour.

## 3. Production — Sécurité

- Ne pas utiliser la ligne roulante `zeek`.
- Vérifier l'origine du paquet avant installation.

## Validation et retour arrière

- **Validation** : `zeek --version` affiche 8.0 et AF_PACKET est listé.
- **Retour arrière** : `sudo apt remove zeek-8.0`, puis supprimer `/etc/apt/sources.list.d/zeek-obs.list` et `/etc/apt/keyrings/zeek-obs.gpg`.

## Si le problème n'est pas résolu

- [Zeek — installation](https://docs.zeek.org/en/stable/install.html)
- [OBS — dépôt Zeek Debian 13](https://download.opensuse.org/repositories/security:/zeek/Debian_13/)
- [Guide complet Zeek 8 LTS Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/72_Deploiement_Zeek_8_LTS_Debian_13.md#2-ajouter-le-depot-officiel-zeek-80-lts-pour-debian-13)
