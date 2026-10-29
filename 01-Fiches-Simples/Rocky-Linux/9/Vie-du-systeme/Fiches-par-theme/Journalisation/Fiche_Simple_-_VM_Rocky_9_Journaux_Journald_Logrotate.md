# 📄 Fiche_Simple_-_VM_Rocky_9_Journaux_Journald_Logrotate.md

- **Environnement** : VM ou serveur Rocky Linux
- **OS / Version** : Rocky Linux 9 / RHEL 9 avec systemd-journald et logrotate
- **Catégorie** : Journaux / Rotation et centralisation
- **Tags** : `[rocky9]`, `[rhel9]`, `[journald]`, `[logrotate]`, `[rsyslog]`, `[logs]`

## 🎯 Problème précis à résoudre
Rendre les journaux systemd persistants avec une taille et une durée de rétention maîtrisées, configurer la rotation des fichiers texte avec `logrotate`, puis transmettre les journaux à un SIEM.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Vérifier si le journal est persistant et sa taille actuelle :
   ```bash
   journalctl --disk-usage
   ls -ld /var/log/journal
   ```
   👉 Explication : Si `/var/log/journal` n'existe pas, les journaux sont perdus au redémarrage. La taille affichée inclut les journaux archivés.

2. Tester la configuration de rotation sans rien modifier :
   ```bash
   sudo logrotate --debug /etc/logrotate.conf
   ```
   👉 Explication : `--debug` affiche les actions que logrotate effectuerait, sans rotation réelle.

---

## ⚡ 2. Production — Façon Simplifiée
1. Rendre le journal persistant avec des limites dans un drop-in :
   ```bash
   sudo mkdir -p /etc/systemd/journald.conf.d
   sudo tee /etc/systemd/journald.conf.d/90-limites.conf >/dev/null <<'EOF'
   [Journal]
   Storage=persistent
   SystemMaxUse=1G
   MaxRetentionSec=1month
   EOF
   sudo mkdir -p /var/log/journal
   sudo systemctl restart systemd-journald
   ```
   👉 Explication : `Storage=persistent` écrit les journaux sur disque. `SystemMaxUse` plafonne l'espace utilisé, `MaxRetentionSec` supprime les entrées plus anciennes. Adapter les valeurs à la taille du disque.

2. Créer une rotation pour une application qui écrit dans un fichier texte :
   ```text
   /var/log/<nom_application>/*.log {
       weekly
       rotate 8
       compress
       delaycompress
       missingok
       notifempty
       create 0640 <service_user> adm
       sharedscripts
       postrotate
           /usr/bin/systemctl kill -s HUP <nom_du_service>.service
       endscript
   }
   ```
   👉 Explication : Enregistrer ce bloc dans `/etc/logrotate.d/<nom_application>`. Il conserve huit semaines de journaux compressés et demande au service de rouvrir son fichier après rotation.

3. Vérifier la nouvelle règle, puis forcer une rotation de test :
   ```bash
   sudo logrotate --debug /etc/logrotate.d/<nom_application>
   sudo logrotate --force /etc/logrotate.d/<nom_application>
   ```
   👉 Explication : `--force` lance la rotation immédiatement. À utiliser sur un fichier de test ou en maintenance, car elle modifie les journaux en place.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Transmettre les journaux au SIEM par rsyslog en TCP (`@@`) :
   ```text
   *.* @@<siem_serveur>:514
   ```
   👉 Explication : Enregistrer cette ligne dans `/etc/rsyslog.d/90-siem.conf`, puis exécuter `sudo systemctl restart rsyslog`. Le double `@@` impose TCP, plus fiable que UDP pour les journaux de sécurité.

2. Contrôler les droits du répertoire des journaux :
   ```bash
   sudo ls -ld /var/log/journal
   ```
   👉 Explication : Le propriétaire doit être `root` et le groupe `systemd-journal`. Les utilisateurs d'exploitation autorisés à lire les journaux doivent appartenir à ce groupe, ajouté avec `sudo usermod -aG systemd-journal <utilisateur>`.

3. Vérifier que rsyslog et journald fonctionnent après modification :
   ```bash
   sudo systemctl is-active systemd-journald rsyslog
   sudo journalctl -u rsyslog -p warning --no-pager -n 20
   ```
   👉 Explication : Les deux services doivent être `active`. Une erreur de syntaxe rsyslog apparaît dans le journal de son unité.

---

## ✅ Contrôle
```bash
journalctl --disk-usage
```
👉 Explication : La taille doit rester inférieure à la valeur de `SystemMaxUse`. Vérifier aussi que `journalctl -b` retourne les journaux du démarrage courant.
