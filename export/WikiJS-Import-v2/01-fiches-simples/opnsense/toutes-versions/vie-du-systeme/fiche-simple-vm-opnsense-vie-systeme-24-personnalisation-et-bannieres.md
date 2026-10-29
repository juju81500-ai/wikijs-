---
title: "Fiche Simple - VM OPNsense Vie Systeme 24 Personnalisation Et Bannieres"
description: "Afficher un avertissement légal à la connexion."
published: true
date: 2026-10-29T20:22:10Z
tags: ["opnsense", "vie-du-systeme", "cycle-de-vie", "etape-24"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_OPNsense_Vie_Systeme_24_Personnalisation_Et_Bannieres

- **Environnement** : Pare-feu OPNsense (VM ou matériel)
- **OS / Version** : OPNsense; étape 24 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `opnsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-24`

---

## Problème précis à résoudre

Afficher un avertissement légal à la connexion.

## 1. Hors-Production (Lab / Test / POC)

1. Dans Système > Paramètres > Administration, renseigner le Message de connexion (ex. « Accès réservé aux administrateurs autorisés »).
   👉 Explication : informe l'utilisateur que l'accès est surveillé; utile juridiquement.

2. Contrôler le message du système en shell :
   ```sh
   cat /etc/motd 2>/dev/null
   grep -c . /conf/config.xml
   ```
   👉 Explication : affiche la bannière éventuelle et vérifie que la configuration n'est pas vide.

## 2. Production — Contrôles

Utiliser le texte validé par le service juridique.

## 3. Production — Sécurité

Ne jamais indiquer le nom du produit ou de la version dans la bannière.

## Validation et retour arrière

- **Validation** : La bannière apparaît à la connexion.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire OPNsense](/01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/sommaire-vie-du-systeme-opnsense)
- [Documentation officielle](https://docs.opnsense.org/)