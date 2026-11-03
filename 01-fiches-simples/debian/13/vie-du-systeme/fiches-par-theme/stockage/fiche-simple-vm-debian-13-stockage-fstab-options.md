# 📄 Fiche_Simple_-_VM_Debian_13_Stockage_Fstab_Options

- **Environnement** : VM ou serveur Debian 13 avec des montages temporaires à durcir
- **OS / Version** : Debian 13 (Trixie) - Famille Debian
- **Catégorie** : Stockage / Options de montage sécurisées
- **Tags** : `[debian13]`, `[debian]`, `[fstab]`, `[mount]`, `[tmpfs]`, `[hardening]`

## 🎯 Problème précis à résoudre
Appliquer les options de montage `nodev`, `nosuid` et `noexec` sur `/tmp` et `/dev/shm` de Debian 13, via `/etc/fstab`, pour empêcher l'exécution de binaires déposés dans les répertoires temporaires, sans casser les applications qui en ont besoin.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Relever les options de montage actuelles des répertoires concernés :
   ```bash
   findmnt -o TARGET,FSTYPE,OPTIONS /tmp /var/tmp /dev/shm
   ```
   👉 Explication : Sous Debian 13, `/tmp` est en général sur le disque racine et sans options de sécurité. `/dev/shm` est un tmpfs monté par systemd. La sortie sert de référence pour le retour arrière.

2. Tester l'effet de `noexec` sur `/dev/shm` en lab, sans modifier `/etc/fstab` :
   ```bash
   sudo mount -o remount,nosuid,nodev,noexec /dev/shm
   findmnt -o TARGET,OPTIONS /dev/shm
   ```
   👉 Explication : Le remontage est temporaire ; un redémarrage restaure la configuration de `/etc/fstab`. Vérifier que le montage affiche bien `noexec`.

3. Vérifier qu'un binaire ne s'exécute plus depuis le répertoire protégé :
   ```bash
   printf '#!/bin/sh\necho ok\n' | sudo tee /dev/shm/test.sh >/dev/null
   sudo chmod +x /dev/shm/test.sh
   /dev/shm/test.sh; sudo rm -f /dev/shm/test.sh
   ```
   👉 Explication : Le script doit échouer avec `Permission denied`. Le fichier de test est supprimé dans la même commande.

---

## ⚡ 2. Production — Façon Simplifiée
1. Sauvegarder `/etc/fstab`, puis ajouter les lignes de montage sécurisées :
   ```bash
   sudo cp -a /etc/fstab /etc/fstab.bak
   sudo tee -a /etc/fstab >/dev/null <<'EOF'
   tmpfs /tmp     tmpfs defaults,nodev,nosuid,noexec,mode=1777,size=1G 0 0
   tmpfs /dev/shm tmpfs defaults,nodev,nosuid,noexec 0 0
   EOF
   ```
   👉 Explication : `nodev` interdit les fichiers périphériques, `nosuid` ignore le bit SUID, `noexec` interdit l'exécution directe. `mode=1777` conserve les droits standards de `/tmp`. `size=1G` limite la RAM consommée ; l'adapter à la mémoire de la VM.

2. Valider la syntaxe du fichier fstab, puis monter les entrées :
   ```bash
   sudo findmnt --verify --verbose
   sudo mount -a
   findmnt -o TARGET,FSTYPE,OPTIONS /tmp /dev/shm
   ```
   👉 Explication : `findmnt --verify` détecte les erreurs de syntaxe avant tout montage. Sur `/tmp`, les fichiers présents sur le disque sont masqués tant que le tmpfs est monté ; effectuer ce changement en fenêtre de maintenance.

3. Vérifier que l'application utilisant `/tmp` fonctionne encore, et redémarrer en fenêtre de maintenance pour valider le montage persistant :
   ```bash
   systemctl --failed --no-pager
   ```
   👉 Explication : Les services qui compilent ou exécutent des scripts depuis `/tmp` doivent être testés avant la mise en production.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Ne pas appliquer `noexec` sur `/tmp` sans test : certains installeurs et outils (Java, Python avec modules compilés) exécutent des binaires depuis `/tmp`. Pour ces cas, exiger un répertoire dédié et contrôlé plutôt qu'un contournement.
   👉 Explication : Un `noexec` non testé provoque des pannes difficiles à diagnostiquer. Documenter l'exception quand elle est nécessaire.

2. Contrôler après chaque modification les options réellement appliquées :
   ```bash
   findmnt -o TARGET,OPTIONS /tmp /dev/shm
   grep -E "/tmp|/dev/shm" /etc/fstab
   ```
   👉 Explication : Les options effectives (`findmnt`) doivent contenir `nodev,nosuid,noexec`. La ligne fstab doit être présente pour persister au redémarrage.

3. En cas de problème au démarrage, restaurer la sauvegarde de fstab depuis la console de l'hyperviseur :
   ```bash
   sudo cp -a /etc/fstab.bak /etc/fstab
   sudo findmnt --verify
   ```
   👉 Explication : Revenir à la configuration précédente sans modifier d'autres fichiers. Ne pas ajouter `nofail` pour masquer une erreur de montage sans l'avoir analysée.
