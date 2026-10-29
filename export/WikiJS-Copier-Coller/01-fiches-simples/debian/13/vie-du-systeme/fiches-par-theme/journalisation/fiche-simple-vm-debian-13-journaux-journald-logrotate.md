# 📄 Fiche_Simple_-_VM_Debian_13_Journaux_Journald_Logrotate

- **Environnement** : VM ou serveur Debian 13 avec systemd
- **OS / Version** : Debian 13 (Trixie) avec systemd-journald et logrotate - Famille Debian
- **Catégorie** : Système & Services / Journaux et rotation

## 🎯 Problème précis à résoudre
Rendre le journal systemd persistant avec une taille et une durée de rétention maîtrisées sur Debian 13, et configurer la rotation des journaux applicatifs dans `/var/log` avec `logrotate`, pour que le disque ne se remplisse pas sans perdre l'historique utile.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Contrôler l'état actuel du journal et son emplacement :
   ```bash
   journalctl --disk-usage
   ls -ld /var/log/journal
   grep -E "^#?(Storage|SystemMaxUse|MaxRetentionSec)" /etc/systemd/journald.conf
   ```
   👉 Explication : Sous Debian 13, le répertoire `/var/log/journal` doit exister pour que le journal soit persistant. S'il est absent, les journaux disparaissent au redémarrage.

2. Créer le répertoire persistant et tester la rotation sur un fichier fictif :
   ```bash
   sudo mkdir -p /var/log/journal
   sudo systemd-tmpfiles --create --prefix /var/log/journal
   sudo logrotate -d /etc/logrotate.conf
   ```
   👉 Explication : `systemd-tmpfiles` applique les droits attendus par systemd. `logrotate -d` simule la rotation sans modifier les fichiers et affiche les erreurs de configuration.

3. Redémarrer le service de journalisation et vérifier la persistance :
   ```bash
   sudo systemctl restart systemd-journald
   journalctl --list-boots
   ```
   👉 Explication : La liste des démarrages doit s'allonger après un reboot de test, ce qui prouve que le journal est persistant.

---

## ⚡ 2. Production — Façon Simplifiée
1. Configurer le journal systemd via un fichier drop-in (sans modifier `/etc/systemd/journald.conf`) :
   ```bash
   sudo mkdir -p /etc/systemd/journald.conf.d
   sudo tee /etc/systemd/journald.conf.d/50-tssr.conf >/dev/null <<'EOF'
   [Journal]
   Storage=persistent
   SystemMaxUse=500M
   MaxRetentionSec=1month
   EOF
   sudo systemctl restart systemd-journald
   ```
   👉 Explication : `Storage=persistent` conserve les journaux après redémarrage, `SystemMaxUse` plafonne l'espace disque utilisé et `MaxRetentionSec` limite la durée de conservation. Les valeurs sont à adapter à la politique de rétention et à la taille du disque.

2. Ajouter une rotation pour une application qui écrit dans `/var/log/<application>/` :
   ```bash
   sudo tee /etc/logrotate.d/<application> >/dev/null <<'EOF'
   /var/log/<application>/*.log {
       daily
       rotate 14
       compress
       delaycompress
       missingok
       notifempty
       create 0640 <utilisateur> adm
       sharedscripts
       postrotate
           systemctl reload <application> >/dev/null 2>&1 || true
       endscript
   }
   EOF
   ```
   👉 Explication : Conserve 14 rotations, compresse les anciennes, et recrée le fichier avec les droits `0640` au groupe `adm`, groupe Debian autorisé à lire les journaux. Le `postrotate` demande à l'application de rouvrir ses fichiers.

3. Tester la configuration et forcer une rotation contrôlée :
   ```bash
   sudo logrotate -d /etc/logrotate.d/<application>
   sudo logrotate -f /etc/logrotate.d/<application>
   ```
   👉 Explication : `-d` affiche ce qui serait fait ; `-f` force une rotation immédiate pour valider le résultat.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Contrôler l'intégrité des fichiers journaux de systemd :
   ```bash
   sudo journalctl --verify
   ```
   👉 Explication : Vérifie la cohérence des fichiers binaires du journal. Un message `FAIL` signale une corruption à investiguer avant de considérer l'historique comme fiable.

2. Restreindre la lecture des journaux aux administrateurs, sans ajouter d'utilisateur inutile au groupe :
   ```bash
   getent group systemd-journal adm
   ```
   👉 Explication : Les membres de `systemd-journal` et `adm` peuvent lire les journaux complets. Ajouter un compte à ces groupes doit rester une décision explicite, documentée dans la fiche serveur.

3. Transmettre les journaux à un collecteur central lorsque la politique l'exige (rsyslog ou Promtail, voir les fiches de supervision) et vérifier l'espace réellement occupé :
   ```bash
   journalctl --disk-usage
   sudo du -sh /var/log
   ```
   👉 Explication : La copie centrale protège contre la perte locale des journaux en cas de compromission. Une rétention locale courte reste nécessaire pour limiter l'espace occupé.