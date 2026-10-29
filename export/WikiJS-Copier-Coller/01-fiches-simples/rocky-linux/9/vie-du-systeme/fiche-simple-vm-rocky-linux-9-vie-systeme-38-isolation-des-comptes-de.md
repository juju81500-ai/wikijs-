# Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_38_Isolation_Des_Comptes_De

- **Environnement** : VM Rocky Linux 9 (serveur)
- **OS / Version** : Rocky Linux 9; étape 38 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Exécuter les services sans privilèges.

## 1. Hors-Production (Lab / Test / POC)

1. Créer un compte système sans connexion (adapter `SVCAPP`) :
   ```bash
   sudo useradd -r -M -d /var/lib/SVCAPP -s /sbin/nologin SVCAPP
   ```
   👉 Explication : compte technique sans shell ni mot de passe.

2. Préparer le répertoire :
   ```bash
   sudo mkdir -p /var/lib/SVCAPP
   sudo chown SVCAPP:SVCAPP /var/lib/SVCAPP
   sudo chmod 750 /var/lib/SVCAPP
   ```
   👉 Explication : seul le compte accède aux données.

3. Renforcer l'unité systemd (`sudo systemctl edit SVCAPP`) :
   ```bash
   [Service]
   User=SVCAPP
   NoNewPrivileges=yes
   ProtectSystem=strict
   PrivateTmp=yes
   ```
   👉 Explication : restreint les privilèges et le système de fichiers vus par le service.

## 2. Production — Contrôles

Un compte par service.

## 3. Production — Sécurité

Jamais de service applicatif exécuté en root.

## Validation et retour arrière

- **Validation** : `ps -o user= -C SVCAPP` renvoie le compte technique.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Rocky Linux 9](/01-fiches-simples/rocky-linux/9/vie-du-systeme/sommaire-vie-du-systeme-rocky-linux-9)
- [Documentation officielle](https://docs.rockylinux.org/)