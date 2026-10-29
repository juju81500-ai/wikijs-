# 📄 Fiche_Simple_-_VM_Debian_12_13_Preparer_Migration_Paquets.md

- **Environnement** : VM ou serveur Debian 12 Bookworm migré vers Debian 13 Trixie
- **OS / Version** : Debian 12 → Debian 13
- **Catégorie** : Système / Migration / Maintenance
- **Tags** : `[debian12]`, `[debian13]`, `[bookworm]`, `[trixie]`, `[migration]`, `[apt]`, `[maintenance]`

## 🎯 Problème précis à résoudre
Préparer la migration majeure Debian 12 vers 13, vérifier les dépôts et les paquets applicatifs affectés, et éviter les changements non maîtrisés de stockage, réseau ou services.

> Une migration Bookworm → Trixie est un changement majeur. Lire les notes Debian officielles avant l'intervention; ne jamais remplacer le nom de version dans les sources puis lancer `full-upgrade` sans précontrôles ni sauvegarde.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Relever versions, dépôts, paquets retenus, état dpkg et capacité disque :
   ```bash
   cat /etc/os-release
   apt-mark showhold
   sudo dpkg --audit
   df -h / /boot
   systemctl --failed
   ```
2. Dupliquer la VM ou restaurer une sauvegarde vers un réseau isolé; relever les versions des services critiques :
   ```bash
   apt-cache policy nginx php-fpm postgresql mariadb-server systemd openssh-server
   ```
3. Repérer les changements Trixie qui concernent la machine : `/tmp` en tmpfs sur nouvelles installations, nettoyage de `/tmp` et `/var/tmp`, `/etc/sysctl.conf` non lu par `systemd-sysctl`, DSA supprimé d'OpenSSH, changements réseau et paquets de rôle.
   👉 *Explication : le nettoyage périodique de `/tmp` affecte les fichiers temporaires anciens; ne pas y conserver de données durables.*

## ⚡ 2. Production — Façon Simplifiée
1. Sauvegarder la VM et les bases; tester la restauration. Avoir console hyperviseur, fenêtre d'arrêt et accès hors bande.
2. Mettre Bookworm à jour, corriger holds et erreurs dpkg, installer le dernier point release et vérifier l'espace de `/boot`.
3. Réviser les services applicatifs avant upgrade :
   - MariaDB 10.11 → 11.8 : réaliser une sauvegarde et confirmer l'arrêt propre avant la migration majeure.
   - PostgreSQL 15 → 17 : planifier une migration de cluster documentée; le changement de paquet seul ne convertit pas les données.
   - OpenSSH : remplacer les clés DSA et confirmer l'accès de secours avant le redémarrage.
   - Samba AD DC : confirmer le paquet `samba-ad-dc` et le plan de reprise du domaine.
4. Après sauvegarde, mettre à jour les sources deb822 vers `trixie` sans mélanger les suites; suivre les étapes d'APT de la note Debian, d'abord `upgrade --without-new-pkgs`, puis `full-upgrade`.
5. Redémarrer seulement après la fin des opérations et vérifier réseau, montages, services et journaux.
   👉 *Explication : les fichiers de dépôts deb822 se modifient en conservant composants et options (dont `non-free-firmware`); ne pas faire un remplacement textuel aveugle.*

## 🔒 3. Production — Façon Sécurisée
1. Ne pas faire la migration majeure via une session SSH unique sans console; les noms d'interface peuvent changer sur certains matériels.
2. Vérifier les réglages `/etc/sysctl.conf`; déplacer les paramètres locaux validés vers `/etc/sysctl.d/*.conf`.
3. Examiner `/etc/tmpfiles.d/tmp.conf`, les scripts écrivant dans `/tmp`, et le nettoyage des fichiers dans `/var/tmp`.
4. Ne pas supprimer les anciens noyaux, dépôts, journaux ou fichiers de données avant validation applicative.

## ✅ Validation et retour arrière
- Confirmer `VERSION_CODENAME=trixie`, versions applicatives, réseau, DNS, stockage, services, chiffrement et supervision.
- Tester depuis un second poste les parcours métier et exécuter une restauration en VM isolée.
- Si la migration échoue, arrêter les écritures et restaurer la VM ou les données avec le plan testé; ne pas tenter un downgrade APT improvisé.

## 🔗 Sources officielles
- [Notes de version Debian 13](https://www.debian.org/releases/trixie/release-notes/index.en.html)
- [Éléments à vérifier pour Trixie](https://www.debian.org/releases/trixie/release-notes/issues.en.html)