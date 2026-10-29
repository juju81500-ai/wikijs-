# 📄 Fiche_Simple_-_VM_Rocky_9_Diagnostic_Journalctl_Erreurs.md

- **Environnement** : VM ou serveur Rocky Linux
- **OS / Version** : Rocky Linux 9 / RHEL 9 avec systemd
- **Catégorie** : Diagnostic / Analyse des erreurs système
- **Tags** : `[rocky9]`, `[rhel9]`, `[journalctl]`, `[dmesg]`, `[diagnostic]`, `[systemd]`

## 🎯 Problème précis à résoudre
Identifier rapidement les erreurs de la session de démarrage courante, les unités systemd en échec et les messages noyau critiques sur Rocky Linux 9.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Lister les erreurs du démarrage courant :
   ```bash
   sudo journalctl -p err -b --no-pager
   ```
   👉 Explication : `-p err` ne garde que les messages de priorité `err` et plus grave. `-b` limite la recherche au démarrage en cours.

2. Lire les erreurs noyau avec horodatage lisible :
   ```bash
   sudo dmesg -T -l err,crit,alert,emerg
   ```
   👉 Explication : `-T` convertit les horodatages en date lisible. Les messages `err`, `crit`, `alert` et `emerg` concernent pilotes, disques ou mémoire.

---

## ⚡ 2. Production — Façon Simplifiée
1. Lister les unités en échec :
   ```bash
   systemctl --failed --no-pager
   ```
   👉 Explication : Affiche les services dont le dernier démarrage a échoué. C'est le point d'entrée du diagnostic.

2. Analyser un service précis :
   ```bash
   systemctl status <nom_du_service> --no-pager -l
   sudo journalctl -u <nom_du_service> -n 100 --no-pager
   ```
   👉 Explication : `status` affiche le code de sortie et les dernières lignes. `journalctl -u` ajoute le journal complet de l'unité.

3. Examiner le démarrage précédent, si le journal est persistant :
   ```bash
   sudo journalctl -b -1 -p warning --no-pager
   ```
   👉 Explication : `-b -1` désigne le démarrage précédent. Si la commande ne retourne rien, activer le stockage persistant (voir la fiche Journaux_Journald_Logrotate).

4. Chercher les erreurs sur une période donnée :
   ```bash
   sudo journalctl --since "1 hour ago" -p err --no-pager
   ```
   👉 Explication : Restreint l'analyse à la dernière heure. Remplacer la valeur par la période de l'incident, par exemple `"2026-10-29 08:00"`.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Identifier les démarrages disponibles avant de comparer :
   ```bash
   sudo journalctl --list-boots
   ```
   👉 Explication : Affiche l'index, l'identifiant et les dates de chaque démarrage enregistré. Les index sont à utiliser avec `-b`.

2. Rechercher les refus SELinux récents :
   ```bash
   sudo ausearch -m AVC -ts recent
   ```
   👉 Explication : Un message `denied` peut expliquer un service qui échoue sans erreur applicative. `ausearch` provient du paquet `audit`, installé par défaut sur Rocky Linux 9.

3. Filtrer les avertissements d'un service exposé, par exemple SSH :
   ```bash
   sudo journalctl _SYSTEMD_UNIT=sshd.service -p warning --no-pager -n 100
   ```
   👉 Explication : Le filtre sur `_SYSTEMD_UNIT` ne retient que les messages émis par cette unité. Il est utile pour relever les tentatives d'authentification échouées.

4. Conserver un extrait horodaté pour l'incident :
   ```bash
   sudo journalctl -b -p err --no-pager | sudo tee /root/diagnostic_err_$(date +%F).txt > /dev/null
   ```
   👉 Explication : Enregistre les erreurs du démarrage courant dans `/root`. Le `tee` avec `sudo` est nécessaire, car la redirection `>` seule s'exécuterait avec les droits de l'utilisateur courant.

---

## ✅ Contrôle
```bash
systemctl --failed --no-pager
```
👉 Explication : Le résultat attendu est `0 loaded units listed`. Toute unité listée doit être analysée avant de considérer le serveur sain.
