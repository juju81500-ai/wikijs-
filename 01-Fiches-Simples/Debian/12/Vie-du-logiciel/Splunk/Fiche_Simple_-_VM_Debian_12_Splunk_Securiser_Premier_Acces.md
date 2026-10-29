# Fiche_Simple_-_VM_Debian_12_Splunk_Securiser_Premier_Acces.md

- **Environnement** : VM Debian 12 dédiée à Splunk Enterprise autonome (laboratoire)
- **OS / Version** : Debian 12 Bookworm; Splunk Enterprise 10.2
- **Catégorie** : journaux / sécurité
- **Tags** : `debian12`, `splunk`, `logs`, `tls`, `systemd`

---

## Problème précis à résoudre

Restreindre l'accès Web et configurer le démarrage systemd.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler l'écoute de Splunk Web :
   ```bash
   sudo ss -tlnp | grep -E ':(8000|8089)\b'
   ```
   👉 Explication : l'accès reste local ou sur le réseau d'administration.

2. Activer le démarrage systemd avec la méthode officielle (service sous l'utilisateur `splunk`) :
   ```bash
   sudo /opt/splunk/bin/splunk enable boot-start -systemd-managed 1 -user splunk
   ```
   👉 Explication : remplace tout démarrage manuel.

3. Examiner l'unité générée :
   ```bash
   systemctl cat Splunkd.service
   ```
   👉 Explication : vérifie utilisateur et limites de ressources.

## 2. Production — Contrôles

Utiliser un reverse proxy HTTPS ou activer TLS selon la procédure Splunk avant tout accès hors localhost; vérifier certificats, DNS, MFA/SSO.

## 3. Production — Sécurité

- Ne pas lancer une seconde instance manuelle si systemd gère déjà le processus.

## Validation et retour arrière

- **Validation** : service systemd actif sous `splunk`.
- **Retour arrière** : `sudo /opt/splunk/bin/splunk disable boot-start`.

## Si le problème n'est pas résolu

- [Splunk 10.2 — installer sur Linux](https://help.splunk.com/en/splunk-enterprise/get-started/install-and-upgrade/10.2/install-splunk-enterprise-on-linux-or-macos/install-on-linux)
- [Guide complet Splunk Debian 12](../../../../../02-Fiches-Completes/Debian/12/Installation-Deploiement/54_Deploiement_Splunk_Enterprise_10.2_Debian_12.md#4-securiser-le-premier-acces)
