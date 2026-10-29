---
title: "Fiche Simple - VM Rocky 9 Suricata Mise A Jour Retour Arriere"
description: "Mettre à jour Suricata et ses règles, avec retour arrière."
published: true
date: 2026-10-29T20:58:45Z
tags: ["suricata", "rocky9", "vie-du-logiciel", "mise-a-jour-retour-arriere"]
editor: markdown
dateCreated: 2026-10-29T20:58:45Z
dateModified: 2026-10-29T20:58:45Z
---

# Fiche_Simple_-_VM_Rocky_9_Suricata_Mise_A_Jour_Retour_Arriere

- **Environnement** : VM Rocky Linux 9 dédiée à Suricata
- **OS / Version** : Rocky Linux 9 (compatible RHEL 9); version des paquets à vérifier sur l’hôte
- **Catégorie** : Suricata / mise à jour et retour arrière
- **Tags** : `suricata`, `rocky9`, `vie-du-logiciel`, `mise-a-jour-retour-arriere`

---

## Problème précis à résoudre

Mettre à jour Suricata et ses règles, avec retour arrière.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder avant changement.
   👉 Explication : Suivre la fiche Sauvegarder_Restaurer de cette série.

2. Mettre à jour le moteur :
   ```bash
   sudo dnf check-update suricata
   sudo dnf upgrade suricata
   sudo suricata -T -c /etc/suricata/suricata.yaml
   ```
   👉 Explication : Applique la version publiée et teste la configuration avant redémarrage.

3. Mettre à jour les règles :
   ```bash
   sudo suricata-update
   sudo suricata -T -c /etc/suricata/suricata.yaml
   sudo systemctl reload suricata || sudo systemctl restart suricata
   ```
   👉 Explication : Recharge les règles; `reload` évite l’arrêt de la capture quand il est supporté.

4. Retour arrière du paquet :
   ```bash
   dnf history list suricata
   sudo dnf history undo ID_TRANSACTION
   ```
   👉 Explication : ID_TRANSACTION est à remplacer par l’identifiant dnf à annuler; restaurer ensuite `/etc/suricata` depuis la sauvegarde.

## 2. Production — Contrôles

Mettre à jour d’abord en lab; surveiller le volume d’alertes (faux positifs) après un nouveau jeu de règles.

## 3. Production — Sécurité

- Règles provenant de sources approuvées uniquement.
- Mettre à jour rapidement les failles du moteur.

## Validation et retour arrière

- **Validation** : Test OK, service actif, alertes cohérentes.
- **Retour arrière** : Appliquer le retour arrière, restaurer la configuration, puis rejouer la recette.

## Si le problème n’est pas résolu

- [Suricata — documentation officielle](https://docs.suricata.io/en/latest/)
- [Fiche d’entrée du logiciel](/01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-suricata)
- [Étape précédente du guide](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/suricata/fiche-simple-vm-rocky-9-suricata-sauvegarder-restaurer)