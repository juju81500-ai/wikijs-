---
title: "Fiche Simple - Windows Server 2022 Nakivo Job Sauvegarde"
description: "Créer et lancer un job de sauvegarde dans l'interface web NAKIVO."
published: true
date: 2026-10-29T20:36:14Z
tags: ["nakivo", "backup-job", "sauvegarde", "windows-server"]
editor: markdown
dateCreated: 2026-10-29T20:36:14Z
dateModified: 2026-10-29T20:36:14Z
---

# Fiche_Simple_-_Windows_Server_2022_Nakivo_Job_Sauvegarde

- **Environnement** : `Serveur Windows Server 2022 (VM ou physique), compte administrateur local ou de domaine nominatif`
- **OS / Version** : `Windows Server 2022 (Desktop Experience ou Core selon support de la version); vérifier la compatibilité et la version courante du produit auprès de l'éditeur`
- **Catégorie** : `sauvegarde / restauration / NAKIVO`
- **Tags** : `nakivo`, `backup-job`, `sauvegarde`, `windows-server`

---

## Problème précis à résoudre

Créer et lancer un job de sauvegarde dans l'interface web NAKIVO.

## 1. Hors-Production (Lab / Test / POC)

1. Ajouter la source à protéger : **Settings > Inventory** (ou équivalent selon la version) puis **Add** ; renseigner l'hôte ou l'hyperviseur et un compte de service dédié en lecture.
   👉 Explication : le Director doit connaître la charge à sauvegarder.

2. Créer le job : **Create** (assistant de création de job), puis le type de job correspondant à la source (par exemple VMware, Hyper-V ou machines physiques Windows selon licence/version).
   👉 Explication : le type de job dépend de ce qui est protégé.

3. Suivre l'assistant : choisir les objets, le Transporter, le dépôt cible, la rétention et la planification.
   👉 Explication : chaque étape fixe où, quand et combien de temps conserver.

4. Activer si disponible la sauvegarde cohérente applicative et le chiffrement, après vérification dans la documentation.
   👉 Explication : les options exactes sont à vérifier pour la version.

5. Lancer le job manuellement : **Run now** et suivre la progression dans **Activities** (libellés à vérifier).
   👉 Explication : un premier passage valide le circuit complet.

## 2. Production — Contrôles

- Documenter jobs, rétention et fenêtre.
- Surveiller les alertes d'échec.

## 3. Production — Sécurité

- Compte source en moindre privilège.
- Dépôt non accessible en écriture depuis les machines sauvegardées.

## Validation et retour arrière

- **Validation** : Le job se termine avec succès et un point de restauration existe.
- **Retour arrière** : Désactiver ou supprimer le job dans l'interface; supprimer les points de test si inutiles.

## Si le problème n'est pas résolu

- [NAKIVO — Help Center officiel](https://helpcenter.nakivo.com/)
- [NAKIVO — System Requirements](https://helpcenter.nakivo.com/display/NH/System+Requirements)
- [Fiche d'entrée du logiciel](/01-fiches-simples/logiciels/07-sauvegarde-restauration-et-pra-pca/fiche-logiciel-nakivo-altaro)