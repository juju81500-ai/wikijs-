# Fiche_Simple_-_TrueNAS_CORE_13.0_Deploiement_Statut_Decision.md

- **Environnement** : Appliance TrueNAS CORE (FreeBSD) en VM de laboratoire ou NAS existant
- **OS / Version** : TrueNAS CORE, branche 13.0 (build exact à relever sur l'ISO)
- **Catégorie** : stockage NAS / décision

---

## Problème précis à résoudre

Décider si TrueNAS CORE est adapté ou si SCALE doit être préféré.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir la page officielle de téléchargement : **https://www.truenas.com/download/** et noter si le build CORE 13.0 y est proposé.
   👉 Explication : le guide indique que disponibilité et support de CORE sont à confirmer avant tout usage.

2. Consulter **https://www.truenas.com/docs/softwarestatus/**.
   👉 Explication : donne le statut de support de chaque branche.

3. Pour un nouveau déploiement sans contrainte FreeBSD, choisir TrueNAS SCALE; réserver CORE à un parc existant, une migration ou un laboratoire.
   👉 Explication : évite de démarrer un projet sur une branche dont le support n'est pas confirmé.

## 2. Production — Contrôles

Faire valider par l'équipe la version, la disponibilité et le support avant production.

## 3. Production — Sécurité

- Aucune version n'est figée tant que le statut n'est pas confirmé; conserver les statuts À revoir et À tester.

## Validation et retour arrière

- **Validation** : La décision CORE/SCALE est écrite et validée.
- **Retour arrière** : Aucune installation n'est faite à ce stade.

## Si le problème n'est pas résolu

- [TrueNAS — documentation CORE 13.0](https://www.truenas.com/docs/core/13.0/)
- [TrueNAS — Software Status](https://www.truenas.com/docs/softwarestatus/)
- [Guide complet — 1. Statut du produit et décision](/02-fiches-completes/truenas/core-13-0/installation-deploiement/89-deploiement-truenas-core-13-0#1-statut-du-produit-et-decision)