---
title: "Fiche Simple - VM Ubuntu 26.04 Journaux Journald Logrotate"
description: "Limiter la taille et la durée de conservation du journal systemd (journald) et faire tourner les journaux des applications avec logrotate, pour éviter qu'un disque se remplisse tout en gardant les événements nécessaires à l'analyse."
published: true
date: 2026-10-29T20:22:42Z
tags: ["ubuntu2604", "journald", "logrotate", "systemd", "retention", "journaux"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# 📄 Fiche_Simple_-_VM_Ubuntu_26.04_Journaux_Journald_Logrotate

- **Environnement** : VM ou serveur Ubuntu avec journaux systemd et services applicatifs
- **OS / Version** : Ubuntu Server 26.04 LTS (systemd 259)
- **Catégorie** : Journaux / Rétention et rotation
- **Tags** : `ubuntu2604`, `journald`, `logrotate`, `systemd`, `retention`, `journaux`

---

## 🎯 Problème précis à résoudre

Limiter la taille et la durée de conservation du journal systemd (journald) et faire tourner les journaux des applications avec logrotate, pour éviter qu'un disque se remplisse tout en gardant les événements nécessaires à l'analyse.

## 🧪 1. Hors-Production (Lab / Test / POC)

1. Mesurer l'espace utilisé par le journal :
```bash
sudo journalctl --disk-usage
```
👉 Explication : Affiche la taille actuelle des journaux archivés et actifs, point de départ avant toute limite.

2. Vérifier si le journal est persistant entre les redémarrages :
```bash
ls -ld /var/log/journal
```
👉 Explication : Si le dossier n'existe pas, journald n'écrit qu'en mémoire (`/run/log/journal`) et perd l'historique à chaque redémarrage.

3. Créer une configuration dédiée :
```bash
sudo mkdir -p /etc/systemd/journald.conf.d
sudo nano /etc/systemd/journald.conf.d/99-retention.conf
```
Contenu :
```text
[Journal]
Storage=persistent
SystemMaxUse=1G
MaxRetentionSec=1month
```
👉 Explication : `Storage=persistent` force l'écriture sur disque. `SystemMaxUse` plafonne la taille totale, `MaxRetentionSec` supprime les entrées plus anciennes. Le fichier `.d` évite de modifier `journald.conf`.

4. Appliquer la configuration :
```bash
sudo systemctl restart systemd-journald
sudo journalctl --disk-usage
```
👉 Explication : Redémarre journald pour relire la configuration. La taille affichée doit rester sous la limite après la prochaine rotation.

5. Créer une règle logrotate pour une application :
```bash
sudo nano /etc/logrotate.d/<nom_application>
```
Contenu :
```text
/var/log/<nom_application>/*.log {
    daily
    rotate 14
    compress
    delaycompress
    missingok
    notifempty
    create 0640 <compte_service> adm
}
```
👉 Explication : Pivote les journaux chaque jour, conserve 14 archives compressées et recrée le fichier avec les droits attendus. `create` doit correspondre au compte qui écrit réellement dans le fichier.

6. Tester la règle sans rien modifier :
```bash
sudo logrotate -d /etc/logrotate.d/<nom_application>
```
👉 Explication : Le mode `-d` (debug) affiche les actions prévues sans les exécuter. Aucune erreur ne doit apparaître.

## ⚡ 2. Production — Façon Simplifiée

1. Forcer une rotation réelle pour vérifier le résultat :
```bash
sudo logrotate -f /etc/logrotate.d/<nom_application>
ls -lh /var/log/<nom_application>/
```
👉 Explication : `-f` force la rotation immédiatement. Le fichier courant doit être recréé vide et une archive doit apparaître.

2. Vérifier le planificateur de logrotate :
```bash
systemctl list-timers logrotate.timer --no-pager
```
👉 Explication : Sur Ubuntu 26.04, logrotate est déclenché par un timer systemd. Son prochain passage doit apparaître dans la liste.

## 🔒 3. Production — Façon Sécurisée

1. Expédier les journaux vers un collecteur central plutôt que de les conserver longtemps localement : configurer `ForwardToSyslog=` ou un agent (Promtail, Vector) selon l'architecture. Documenter le choix dans la fiche du serveur.
👉 Explication : Un journal local est effaçable par un attaquant disposant de root. La copie distante préserve la preuve d'une intrusion.

2. Restreindre les droits des journaux applicatifs :
```bash
sudo ls -l /var/log/<nom_application>/
```
👉 Explication : Les fichiers doivent appartenir au compte de service et au groupe `adm`, sans lecture pour les autres utilisateurs (`0640`).

3. Surveiller l'occupation disque des journaux :
```bash
sudo journalctl --disk-usage
df -h /var/log
```
👉 Explication : Permet de détecter une dérive avant saturation, à intégrer à la supervision.

## ✅ Validation et retour arrière

- **Précontrôles** : espace disque disponible relevé, sauvegarde de la configuration existante de logrotate, compte propriétaire des journaux identifié.
- **Validation** : `sudo logrotate -d` sans erreur ; `sudo journalctl --disk-usage` sous la limite définie ; un redémarrage conserve l'historique.
- **Retour arrière** : supprimer `/etc/systemd/journald.conf.d/99-retention.conf` puis `sudo systemctl restart systemd-journald` ; supprimer la règle `/etc/logrotate.d/<nom_application>`.