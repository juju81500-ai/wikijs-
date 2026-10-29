---
title: "Fiche Simple - VM Debian 13 FreeIPA Client Sauvegarder Restaurer"
description: "Conserver la configuration cliente et savoir la reconstruire."
published: true
date: 2026-10-29T21:02:28Z
tags: ["freeipa", "debian13", "vie-du-logiciel", "sauvegarder-restaurer"]
editor: markdown
dateCreated: 2026-10-29T21:02:28Z
dateModified: 2026-10-29T21:02:28Z
---

# Fiche_Simple_-_VM_Debian_13_FreeIPA_Client_Sauvegarder_Restaurer

- **Environnement** : VM Debian 13 cliente d'un domaine FreeIPA existant
- **OS / Version** : Debian 13 Trixie; paquet freeipa-client des dépôts, version à vérifier
- **Catégorie** : FreeIPA client / sauvegarder / restaurer
- **Tags** : `freeipa`, `debian13`, `vie-du-logiciel`, `sauvegarder-restaurer`

---

## Problème précis à résoudre

Conserver la configuration cliente et savoir la reconstruire.

## 1. Hors-Production (Lab / Test / POC)

1. Archiver les fichiers de configuration (sans copier le keytab hors hôte non chiffré) :
   ```bash
   sudo install -d -m 0700 /var/backups/freeipa-client
   sudo tar czf /var/backups/freeipa-client/ipa-client-$(date +%F).tar.gz /etc/ipa /etc/sssd /etc/krb5.conf /var/lib/ipa-client
   ```
   👉 Explication : Le keytab /etc/krb5.keytab est un secret : ne pas l'inclure dans une archive non chiffrée. L'archive reste en 0700 sur l'hôte et chiffrée en cas de copie.

2. Restauration : réinstaller le paquet puis réinscrire le client plutôt que de restaurer un keytab :
   ```bash
   sudo ipa-client-install --uninstall
   sudo ipa-client-install --domain=IPA_DOMAIN --realm=IPA_REALM --server=IPA_SERVER_FQDN --mkhomedir -p ADMIN_PRINCIPAL -W
   ```
   👉 Explication : Si l'hôte existe déjà côté serveur, l'administrateur doit le supprimer ou régénérer ses secrets avant la réinscription (selon la documentation FreeIPA de la version).

## 2. Production — Contrôles

La sauvegarde de référence des données d'identité est celle du serveur (voir les fiches Sauvegarder du serveur Rocky 9).

## 3. Production — Sécurité

- Aucun keytab ni mot de passe dans les sauvegardes non chiffrées.

## Validation et retour arrière

- **Validation** : Un client reconstruit reprend l'identité de domaine.
- **Retour arrière** : Restaurer le snapshot de la VM.

## Si le problème n'est pas résolu

- [Étape suivante du guide](/01-fiches-simples/debian/13/vie-du-logiciel/freeipa/fiche-simple-vm-debian-13-freeipa-client-mise-a-jour-retour-arriere)
- [Fiche d'entrée du logiciel](/01-fiches-simples/logiciels/05-systemes-annuaires-et-services/fiche-logiciel-freeipa)
- [FreeIPA — page Client](https://www.freeipa.org/page/Client)
- [FreeIPA — page Documentation](https://www.freeipa.org/page/Documentation)