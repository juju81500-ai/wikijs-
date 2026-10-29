---
title: "Fiche Simple - VM Rocky 9 FreeIPA Restaurer"
description: "Préparer et tester une restauration FreeIPA sans risque pour la production."
published: true
date: 2026-10-29T20:14:10Z
tags: ["rocky9", "freeipa", "idm", "kerberos"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Rocky_9_FreeIPA_Restaurer.md

- **Environnement** : VM Rocky Linux 9 dédiée au premier serveur FreeIPA/IdM
- **OS / Version** : Rocky Linux 9 x86_64; paquets `ipa-server` des dépôts de la distribution
- **Catégorie** : annuaire / restauration
- **Tags** : `rocky9`, `freeipa`, `idm`, `kerberos`

---

## Problème précis à résoudre

Préparer et tester une restauration FreeIPA sans risque pour la production.

## 1. Hors-Production (Lab / Test / POC)

1. Créer une VM isolée de même nom d'hôte et de même version de paquets, sans accès au DNS ni aux clients de production.
   👉 Explication : la restauration remplace données et configuration de l'hôte; elle se répète d'abord en isolation.

2. Suivre la procédure « Preparing for disaster recovery with Identity Management » de la documentation RHEL 9 pour jouer `ipa-restore` sur cette VM.
   👉 Explication : la procédure détaillée de référence est celle de Red Hat; ce guide ne reprend pas les options.

3. Valider ensuite `kinit admin` et `ipa user-find` sur la VM isolée.
   👉 Explication : prouve que la sauvegarde est exploitable.

## 2. Production — Contrôles

Documenter la durée et le résultat du test; ne jamais restaurer sur la production tant que le test n'a pas réussi.

## 3. Production — Sécurité

- Isoler la VM de test du réseau de production.
- Détruire la VM de test et ses données après la recette (elles contiennent des secrets).

## Validation et retour arrière

- **Validation** : la restauration est jouée avec succès sur VM isolée.
- **Retour arrière** : supprimer la VM de test; la production n'a pas été modifiée.

## Si le problème n'est pas résolu

- [Red Hat — Preparing for disaster recovery with Identity Management](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/preparing_for_disaster_recovery_with_identity_management/index)
- [FreeIPA — Quick Start Guide](https://www.freeipa.org/page/Quick_Start_Guide)
- [Red Hat — RHEL 9, Installing Identity Management](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/installing_identity_management/index)
- [Guide complet — étape 6](/02-fiches-completes/rocky-linux/9/installation-deploiement/88-deploiement-freeipa-rocky-linux-9#6-restaurer)