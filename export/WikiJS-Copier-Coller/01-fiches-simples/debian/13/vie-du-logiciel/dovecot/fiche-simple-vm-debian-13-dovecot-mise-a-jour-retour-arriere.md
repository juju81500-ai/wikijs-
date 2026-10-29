# Fiche_Simple_-_VM_Debian_13_Dovecot_Mise_A_Jour_Retour_Arriere

- **Environnement** : VM Debian 13; Dovecot depuis les dépôts de la distribution
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : Messagerie et collaboratif / Dovecot — Mise à jour et retour arrière

---

## Problème précis à résoudre

Mettre à jour Dovecot via Debian 13 et gérer le passage Debian 12 (2.3) vers Debian 13 (2.4) avec retour arrière.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder configuration et boîtes puis prendre un snapshot de VM (fiche Sauvegarder / restaurer).
   👉 Explication : la montée de branche majeure n'est pas réversible par simple downgrade de paquet.

2. Lister les mises à jour :
   ```bash
   sudo apt update
   apt list --upgradable 2>/dev/null | grep -i dovecot
   ```
   👉 Explication : lire les notes de version avant de continuer.

3. Mettre à jour :
   ```bash
   sudo apt install --only-upgrade dovecot-core dovecot-imapd dovecot-lmtpd
   sudo doveconf -n >/dev/null && sudo systemctl restart dovecot
   ```
   👉 Explication : conserver vos fichiers locaux de `conf.d/` ; la configuration est validée avant redémarrage.

4. Cas migration 2.3 vers 2.4 : convertir la configuration selon le guide officiel (lien ci-dessous), tester d'abord en lab avec une copie des boîtes.
   ```bash
   doveconf -n
   ```
   👉 Explication : les paramètres renommés doivent être convertis ; ne jamais copier l'ancienne configuration sur la nouvelle version sans test.

5. Rejouer la recette (fiche Valider).
   ```bash
   dovecot --version
   ```
   👉 Explication : confirme la version et le fonctionnement.

## 2. Production — Contrôles

Fenêtre de maintenance, utilisateurs prévenus, sauvegarde testée, surveillance des journaux pendant 24 h après mise à jour.

## 3. Production — Sécurité

- Mises à jour uniquement depuis les dépôts Debian signés.
- Conserver l'archive de configuration de l'ancienne version.

## Validation et retour arrière

- **Validation** : version attendue, `doveadm auth test` et IMAPS OK.
- **Retour arrière** : restaurer le snapshot de VM ; sinon réinstaller la version précédente (`apt install dovecot-core=VERSION_PRECEDENTE`, à remplacer par une version listée) et restaurer `/etc/dovecot` depuis l'archive.

## Si le problème n'est pas résolu

- [Dovecot — Prérequis et limites](/01-fiches-simples/debian/13/vie-du-logiciel/dovecot/fiche-simple-vm-debian-13-dovecot-prerequis-limites)
- [Dovecot — Installer](/01-fiches-simples/debian/13/vie-du-logiciel/dovecot/fiche-simple-vm-debian-13-dovecot-installer)
- [Dovecot 2.4 — documentation officielle](https://doc.dovecot.org/main/)
- [Dovecot — migration 2.3 vers 2.4](https://doc.dovecot.org/main/installation/upgrade/2.3-to-2.4.html)