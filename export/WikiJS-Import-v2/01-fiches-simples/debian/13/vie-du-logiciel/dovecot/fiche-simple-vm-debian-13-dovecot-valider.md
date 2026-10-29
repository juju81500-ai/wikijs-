---
title: "Fiche Simple - VM Debian 13 Dovecot Valider"
description: "Recetter Dovecot : service, authentification, accès IMAPS et remise LMTP."
published: true
date: 2026-10-29T21:07:31Z
tags: ["debian13", "dovecot", "imap", "messagerie", "valider"]
editor: markdown
dateCreated: 2026-10-29T21:07:31Z
dateModified: 2026-10-29T21:07:31Z
---

# Fiche_Simple_-_VM_Debian_13_Dovecot_Valider

- **Environnement** : VM Debian 13; Dovecot depuis les dépôts de la distribution
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : Messagerie et collaboratif / Dovecot — Valider (recette)
- **Tags** : `debian13`, `dovecot`, `imap`, `messagerie`, `valider`

---

## Problème précis à résoudre

Recetter Dovecot : service, authentification, accès IMAPS et remise LMTP.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler le service et les ports :
   ```bash
   systemctl is-active dovecot
   sudo ss -tlnp | grep dovecot
   ```
   👉 Explication : 993 doit écouter (et 143 uniquement si volontairement activé).

2. Tester l'authentification du compte de test (saisie interactive du mot de passe) :
   ```bash
   doveadm auth test UTILISATEUR_TEST
   ```
   👉 Explication : retourne `auth succeeded` ; le mot de passe est demandé sans être affiché.

3. Tester IMAPS :
   ```bash
   openssl s_client -connect MAIL.EXAMPLE.NET:993 -brief </dev/null
   ```
   👉 Explication : affiche la version TLS et la chaîne de certificats.

4. Vérifier la boîte après un message de test envoyé par Postfix :
   ```bash
   sudo doveadm mailbox list -u UTILISATEUR_TEST
   sudo doveadm fetch -u UTILISATEUR_TEST 'hdr.subject' mailbox INBOX all
   ```
   👉 Explication : le message de recette doit apparaître dans INBOX.

5. Lire les journaux :
   ```bash
   sudo journalctl -u dovecot -n 30 --no-pager
   ```
   👉 Explication : aucune erreur de configuration ou d'authentification inattendue.

## 2. Production — Contrôles

Tester avec un vrai client (ex. Thunderbird) en IMAPS 993 ; consigner version, date et résultats ; supprimer le compte de test.

## 3. Production — Sécurité

- Ne pas laisser de compte de test actif.
- Ne jamais saisir de mot de passe en argument de commande.

## Validation et retour arrière

- **Validation** : authentification OK, IMAPS chiffré, message livré dans INBOX.
- **Retour arrière** : revenir à la configuration datée (`/etc/dovecot.orig-DATE`), recharger et rejouer la recette.

## Si le problème n'est pas résolu

- [Dovecot — Prérequis et limites](/01-fiches-simples/debian/13/vie-du-logiciel/dovecot/fiche-simple-vm-debian-13-dovecot-prerequis-limites)
- [Dovecot — Installer](/01-fiches-simples/debian/13/vie-du-logiciel/dovecot/fiche-simple-vm-debian-13-dovecot-installer)
- [Dovecot 2.4 — documentation officielle](https://doc.dovecot.org/main/)
- [Dovecot — migration 2.3 vers 2.4](https://doc.dovecot.org/main/installation/upgrade/2.3-to-2.4.html)