# Fiche_Simple_-_VM_Debian_12_Splunk_Installer_Sans_Root.md

- **Environnement** : VM Debian 12 dédiée à Splunk Enterprise autonome (laboratoire)
- **OS / Version** : Debian 12 Bookworm; Splunk Enterprise 10.2
- **Catégorie** : journaux / installation

---

## Problème précis à résoudre

Installer le paquet et réaliser le premier démarrage avec le compte `splunk`.

## 1. Hors-Production (Lab / Test / POC)

1. Installer le paquet (nom d'exemple à remplacer) :
   ```bash
   sudo dpkg -i ./splunk-10.2.0-*-linux-amd64.deb
   ```
   👉 Explication : le paquet Debian s'installe dans `/opt/splunk`.

2. Donner la propriété au compte de service :
   ```bash
   sudo chown -R splunk:splunk /opt/splunk
   ```
   👉 Explication : Splunk 10.2 refuse root par défaut.

3. Démarrer sous le compte `splunk` :
   ```bash
   sudo -H -u splunk /opt/splunk/bin/splunk start
   ```
   👉 Explication : accepter la licence et créer interactivement l'admin avec un secret fort du coffre.

## 2. Production — Contrôles

Accorder seulement les accès aux fichiers surveillés qui ont été approuvés.

## 3. Production — Sécurité

- Ne jamais passer le mot de passe dans la ligne de commande.
- Utiliser un admin distinct de l'identité système.

## Validation et retour arrière

- **Validation** : `splunk status` indique Splunk en fonctionnement.
- **Retour arrière** : `sudo -H -u splunk /opt/splunk/bin/splunk stop` puis `sudo dpkg -r splunk` (les données restent dans `/opt/splunk`).

## Si le problème n'est pas résolu

- [Splunk 10.2 — installer sur Linux](https://help.splunk.com/en/splunk-enterprise/get-started/install-and-upgrade/10.2/install-splunk-enterprise-on-linux-or-macos/install-on-linux)
- [Guide complet Splunk Debian 12](/02-fiches-completes/debian/12/installation-deploiement/54-deploiement-splunk-enterprise-10-2-debian-12#3-installer-sans-demarrer-en-root)