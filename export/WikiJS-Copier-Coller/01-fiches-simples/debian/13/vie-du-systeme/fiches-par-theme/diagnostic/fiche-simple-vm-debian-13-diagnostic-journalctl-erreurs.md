# 📄 Fiche_Simple_-_VM_Debian_13_Diagnostic_Journalctl_Erreurs

- **Environnement** : VM ou serveur Debian 13 avec systemd
- **OS / Version** : Debian 13 (Trixie) avec systemd - Famille Debian
- **Catégorie** : Diagnostic / Analyse des journaux d'erreurs

## 🎯 Problème précis à résoudre
Identifier rapidement les erreurs système, les services en échec et les messages critiques du noyau sur Debian 13, en filtrant par niveau de gravité, par unité et par démarrage avec `journalctl` et `dmesg`.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Lister les services en échec et les erreurs de la session de démarrage courante :
   ```bash
   systemctl --failed --no-pager
   journalctl -p err -b --no-pager
   ```
   👉 Explication : `--failed` liste les unités en échec. `-p err` filtre les messages de niveau `err` ou plus grave, et `-b` limite l'analyse au démarrage courant.

2. Consulter les erreurs du noyau :
   ```bash
   sudo dmesg --level=err,crit,alert,emerg
   ```
   👉 Explication : Affiche les erreurs matérielles et pilotes (disque, réseau, mémoire). Les messages `I/O error` ou `EXT4-fs error` sont prioritaires.

3. Analyser le démarrage précédent après un plantage ou un reboot inattendu :
   ```bash
   journalctl --list-boots
   journalctl -b -1 -p warning --no-pager | tail -n 50
   ```
   👉 Explication : `--list-boots` liste les démarrages enregistrés (requiert un journal persistant). `-b -1` désigne le démarrage précédent.

---

## ⚡ 2. Production — Façon Simplifiée
1. Cibler un service précis sur la dernière heure :
   ```bash
   journalctl -u <service> --since "1 hour ago" -p warning --no-pager
   ```
   👉 Explication : Filtre sur l'unité systemd et sur la gravité minimale `warning`. Remplacer `<service>` par le nom exact de l'unité (par exemple `ssh` ou `nginx`).

2. Vérifier le temps de démarrage et les unités lentes ou bloquantes :
   ```bash
   systemd-analyze
   systemd-analyze blame | head -n 15
   ```
   👉 Explication : `systemd-analyze` donne la durée du démarrage ; `blame` classe les unités par temps d'initialisation, ce qui révèle un montage réseau ou disque qui attend trop longtemps.

3. Confirmer l'espace et la santé du journal :
   ```bash
   journalctl --disk-usage
   journalctl --verify
   ```
   👉 Explication : Un journal saturé peut masquer les erreurs les plus récentes. `--verify` détecte une corruption des fichiers de journal.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Exporter l'analyse pour la conserver dans le dossier d'incident, sans modifier les journaux d'origine :
   ```bash
   journalctl -p err -b --no-pager > /tmp/diagnostic-erreurs-$(hostname)-$(date +%F).txt
   ```
   👉 Explication : Capture une photo horodatée de l'état. Déplacer ensuite le fichier hors de `/tmp` vers un répertoire réservé à l'équipe, car ce fichier peut contenir des données sensibles.

2. Limiter l'accès aux journaux complets : un compte non administrateur doit recevoir un accès via un groupe dédié, jamais via `sudo` sans restriction.
   ```bash
   getent group systemd-journal adm
   ```
   👉 Explication : Les membres de ces groupes lisent l'intégralité des journaux, y compris les commandes sensibles. Vérifier régulièrement leur composition.

3. Ne pas redémarrer un serveur de production pour « effacer » une erreur : identifier d'abord la cause dans `journalctl -b -1` et `dmesg`, puis appliquer la correction documentée.
   👉 Explication : Un redémarrage efface l'état en mémoire et peut masquer la cause de la panne. Le démarrage précédent reste consultable tant que le journal est persistant.