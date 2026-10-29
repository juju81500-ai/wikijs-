---
title: "Fiche Simple - VM Debian 13 FreeIPA Client Mise A Jour Retour Arriere"
description: "Mettre à jour le client FreeIPA en gardant un retour arrière."
published: true
date: 2026-10-29T21:02:28Z
tags: ["freeipa", "debian13", "vie-du-logiciel", "mise-a-jour-retour-arriere"]
editor: markdown
dateCreated: 2026-10-29T21:02:28Z
dateModified: 2026-10-29T21:02:28Z
---

# Fiche_Simple_-_VM_Debian_13_FreeIPA_Client_Mise_A_Jour_Retour_Arriere

- **Environnement** : VM Debian 13 cliente d'un domaine FreeIPA existant
- **OS / Version** : Debian 13 Trixie; paquet freeipa-client des dépôts, version à vérifier
- **Catégorie** : FreeIPA client / mise à jour / retour arrière
- **Tags** : `freeipa`, `debian13`, `vie-du-logiciel`, `mise-a-jour-retour-arriere`

---

## Problème précis à résoudre

Mettre à jour le client FreeIPA en gardant un retour arrière.

## 1. Hors-Production (Lab / Test / POC)

1. Noter la version et sauvegarder la configuration :
   ```bash
   apt-cache policy freeipa-client
   sudo tar czf /var/backups/freeipa-client/avant-maj-$(date +%F).tar.gz /etc/ipa /etc/sssd /etc/krb5.conf
   ```
   👉 Explication : La version sert de référence; le dossier de sauvegarde est créé par la fiche précédente.

2. Mettre à jour uniquement le paquet client :
   ```bash
   sudo apt update
   sudo apt install --only-upgrade freeipa-client
   sudo systemctl restart sssd
   ```
   👉 Explication : Vérifier la compatibilité avec la version du serveur avant la fenêtre.

3. Rejouer la recette puis revenir en arrière si besoin :
   ```bash
   id UTILISATEUR_IPA
   sudo apt install freeipa-client=VERSION_PRECEDENTE
   ```
   👉 Explication : UTILISATEUR_IPA est l'utilisateur de test et VERSION_PRECEDENTE la version notée (à remplacer); sinon restaurer le snapshot.

## 2. Production — Contrôles

Prendre un snapshot de la VM avant la mise à jour.

## 3. Production — Sécurité

- Dépôts approuvés uniquement.

## Validation et retour arrière

- **Validation** : Authentification de domaine fonctionnelle après mise à jour.
- **Retour arrière** : Réinstaller la version précédente et restaurer les fichiers archivés avant-maj-DATE (DATE à remplacer), ou restaurer le snapshot.

## Si le problème n'est pas résolu

- [Première étape du guide](/01-fiches-simples/debian/13/vie-du-logiciel/freeipa/fiche-simple-vm-debian-13-freeipa-client-prerequis-limites)
- [Fiche d'entrée du logiciel](/01-fiches-simples/logiciels/05-systemes-annuaires-et-services/fiche-logiciel-freeipa)
- [FreeIPA — page Client](https://www.freeipa.org/page/Client)
- [FreeIPA — page Documentation](https://www.freeipa.org/page/Documentation)