# Fiche_Simple_-_VM_Ubuntu_24.04_Migration_26.04_Impact_Changements.md

- **Environnement** : VM ou serveur Ubuntu Server LTS
- **OS / Version** : Ubuntu Server 24.04 LTS (Noble) vers 26.04 LTS (Resolute)
- **Catégorie** : migration de version
- **Tags** : `ubuntu24.04`, `ubuntu26.04`, `migration`, `php`, `postgresql`, `systemd`, `apt`

---

## Problème précis à résoudre

Tester en avance les applications touchées par les nouvelles versions.

## 1. Hors-Production (Lab / Test / POC)

1. PHP 8.3 vers 8.5 : vérifier l'application et les extensions natives.
   👉 Explication : le code peut devoir être migré.

2. PostgreSQL 16 vers 18 : utiliser un chemin de migration de cluster supporté et sauvegarder/dumper la base.
   👉 Explication : ne pas réutiliser directement l'ancien répertoire de données.

3. MySQL 8.0 vers 8.4 : vérifier l'authentification.
   👉 Explication : `mysql_native_password` est désactivé par défaut.

4. Chrony : éviter les sources horaires en double.
   👉 Explication : Chrony devient le service horaire par défaut.

5. systemd 259 et APT 3 : migrer les scripts SysV vers des unités natives (cgroup v1 supprimé) et remplacer `apt-key` par des dépôts avec clés dédiées.
   👉 Explication : ces changements cassent des scripts et dépôts tiers.

6. Dracut, OpenLDAP, Samba, Dovecot : lire les notes spécifiques si ces services sont installés.
   👉 Explication : des hooks initramfs et configurations peuvent changer.

## 2. Production — Contrôles

Tester chaque application dans une VM isolée avant la fenêtre de maintenance.

## 3. Production — Sécurité

- Ne pas migrer un moteur de base sans sauvegarde cohérente.

## Validation et retour arrière

- **Validation** : Chaque application touchée a été testée sur une copie.
- **Retour arrière** : Lecture seule : rien à annuler.

## Si le problème n'est pas résolu

- [Ubuntu 26.04 LTS — notes de version](https://documentation.ubuntu.com/release-notes/26.04/)
- [Ubuntu 24.04 LTS — notes de version](https://documentation.ubuntu.com/release-notes/24.04/)
- [Guide complet — tester l'impact des changements de base](../../../../../../02-Fiches-Completes/Ubuntu/24.04/Installation-Deploiement/22_Migration_Ubuntu_Server_24.04_vers_26.04_LTS.md#3-tester-limpact-des-changements-de-base)
