# Fiche_Simple_-_VM_Debian_12_Splunk_Telecharger_Verifier_Paquet.md

- **Environnement** : VM Debian 12 dédiée à Splunk Enterprise autonome (laboratoire)
- **OS / Version** : Debian 12 Bookworm; Splunk Enterprise 10.2
- **Catégorie** : journaux / téléchargement

---

## Problème précis à résoudre

Obtenir le paquet officiel et contrôler son intégrité.

## 1. Hors-Production (Lab / Test / POC)

1. Télécharger le `.deb` Linux x86-64 et son fichier SHA-512 depuis la page officielle Splunk : **https://www.splunk.com > Free Trials and Downloads > Splunk Enterprise > Linux .deb**
   👉 Explication : le fichier de hash est publié avec le paquet.

2. Vérifier l'empreinte (nom de fichier d'exemple à remplacer) :
   ```bash
   sha512sum splunk-10.2.0-example-linux-amd64.deb
   ```
   👉 Explication : si elle diffère, supprimer le téléchargement et arrêter.

3. Créer groupe et compte de service dédiés (sauf s'ils existent déjà) :
   ```bash
   sudo groupadd --system splunk
   sudo useradd --system --gid splunk --home-dir /opt/splunk --shell /usr/sbin/nologin splunk
   ```
   👉 Explication : Splunk ne doit pas tourner en root.

4. Vérifier que `/opt/splunk` n'est pas un lien symbolique :
   ```bash
   sudo test ! -L /opt/splunk
   sudo test ! -e /opt/splunk || sudo test -d /opt/splunk
   ```
   👉 Explication : le paquet exige un vrai répertoire.

## 2. Production — Contrôles

Passer par une source de paquets contrôlée et archiver le hash.

## 3. Production — Sécurité

- Ne pas créer de doublon si un compte `splunk` existe.

## Validation et retour arrière

- **Validation** : hash identique à celui publié.
- **Retour arrière** : supprimer le fichier téléchargé; `sudo userdel splunk && sudo groupdel splunk` si créés pour rien.

## Si le problème n'est pas résolu

- [Splunk 10.2 — installer sur Linux](https://help.splunk.com/en/splunk-enterprise/get-started/install-and-upgrade/10.2/install-splunk-enterprise-on-linux-or-macos/install-on-linux)
- [Guide complet Splunk Debian 12](/02-fiches-completes/debian/12/installation-deploiement/54-deploiement-splunk-enterprise-10-2-debian-12#2-telecharger-et-verifier-le-paquet)