# Fiche_Simple_-_VM_Ubuntu_24.04_Migration_26.04_Retour_Arriere.md

- **Environnement** : VM ou serveur Ubuntu Server LTS
- **OS / Version** : Ubuntu Server 24.04 LTS (Noble) vers 26.04 LTS (Resolute)
- **Catégorie** : migration de version
- **Tags** : `ubuntu24.04`, `ubuntu26.04`, `migration`, `retour-arriere`

---

## Problème précis à résoudre

Revenir à Ubuntu 24.04 après un échec de migration.

## 1. Hors-Production (Lab / Test / POC)

1. Isoler la VM du réseau de production.
   👉 Explication : on évite d'envoyer des données incohérentes.

2. Restaurer le snapshot ou la sauvegarde validée avant la migration.
   👉 Explication : une mise à niveau Debian/Ubuntu n'a pas de downgrade APT pris en charge.

3. Restaurer aussi les bases dans un état compatible avec les binaires retenus.
   👉 Explication : un moteur de base migré ne relit pas toujours d'anciens fichiers.

## 2. Production — Contrôles

Documenter la décision de retour arrière et ses causes.

## 3. Production — Sécurité

- Ne pas tenter de revenir en arrière par modification manuelle des sources APT.

## Validation et retour arrière

- **Validation** : Le système restauré redémarre en 24.04 avec ses applications.
- **Retour arrière** : C'est l'objet de la fiche : restauration depuis sauvegarde ou snapshot.

## Si le problème n'est pas résolu

- [Ubuntu 26.04 LTS — notes de version](https://documentation.ubuntu.com/release-notes/26.04/)
- [Ubuntu 24.04 LTS — notes de version](https://documentation.ubuntu.com/release-notes/24.04/)
- [Guide complet — revenir en arrière](../../../../../../02-Fiches-Completes/Ubuntu/24.04/Installation-Deploiement/22_Migration_Ubuntu_Server_24.04_vers_26.04_LTS.md#7-revenir-en-arriere)
