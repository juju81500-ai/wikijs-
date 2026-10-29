# Fiche_Simple_-_VM_Debian_13_Dovecot_Installer

- **Environnement** : VM Debian 13; Dovecot depuis les dépôts de la distribution
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : Messagerie et collaboratif / Dovecot — Installer
- **Tags** : `debian13`, `dovecot`, `imap`, `messagerie`, `installer`

---

## Problème précis à résoudre

Installer Dovecot depuis les dépôts Debian 13 avec IMAP et LMTP.

## 1. Hors-Production (Lab / Test / POC)

1. Installer les paquets :
   ```bash
   sudo apt update
   sudo apt install -y dovecot-core dovecot-imapd dovecot-lmtpd
   ```
   👉 Explication : `dovecot-core` contient le serveur, `imapd` le protocole IMAP, `lmtpd` la remise locale depuis Postfix.

2. Activer et démarrer :
   ```bash
   sudo systemctl enable --now dovecot
   systemctl is-active dovecot
   ```
   👉 Explication : l'état doit être `active`.

3. Relever la version :
   ```bash
   dovecot --version
   sudo doveconf -n | head -20
   ```
   👉 Explication : `doveconf -n` affiche la configuration effective ; la première ligne contient la version de configuration (`dovecot_config_version`).

## 2. Production — Contrôles

Paquets issus du dépôt Debian officiel, service activé au démarrage, configuration par défaut non exposée sur Internet.

## 3. Production — Sécurité

- Ne pas ouvrir le pare-feu avant la fiche Sécuriser.
- Ne pas installer de paquet tiers non signé.

## Validation et retour arrière

- **Validation** : `dovecot --version` répond et le service est actif.
- **Retour arrière** : `sudo apt purge dovecot-core dovecot-imapd dovecot-lmtpd` ou restauration du snapshot.

## Si le problème n'est pas résolu

- [Dovecot — Prérequis et limites](Fiche_Simple_-_VM_Debian_13_Dovecot_Prerequis_Limites.md)
- [Dovecot — Configurer](Fiche_Simple_-_VM_Debian_13_Dovecot_Configurer.md)
- [Dovecot 2.4 — documentation officielle](https://doc.dovecot.org/main/)
- [Dovecot — migration 2.3 vers 2.4](https://doc.dovecot.org/main/installation/upgrade/2.3-to-2.4.html)
