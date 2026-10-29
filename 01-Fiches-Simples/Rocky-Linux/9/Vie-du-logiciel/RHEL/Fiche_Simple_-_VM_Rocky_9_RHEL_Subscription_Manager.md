# Fiche_Simple_-_VM_Rocky_9_RHEL_Subscription_Manager

- **Environnement** : VM Rocky Linux 9 comme repère documentaire; sujet RHEL
- **OS / Version** : Red Hat Enterprise Linux 9; commandes RHSM sur RHEL autorisé
- **Catégorie** : Vie du logiciel / RHEL — Contrôler subscription-manager
- **Tags** : `rocky9`, `rhel`, `rhel`, `migration`

---

## Problème précis à résoudre

Vérifier identité RHSM, statut et dépôts avant maintenance.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler subscription-manager :
   ```bash
   sudo subscription-manager identity
sudo subscription-manager status
sudo subscription-manager repos --list-enabled
   ```
   👉 Explication : Affiche identité, statut et dépôts; dépend du type de souscription.


## 2. Production — Contrôles

Confirmer droits et dépôts auprès de l’organisation Red Hat ou Satellite.

## 3. Production — Sécurité

Ne pas désactiver RHSM ni ajouter dépôts tiers; aucun secret dans la fiche.

## Validation et retour arrière

- **Validation** : Système identifié, droits attendus, dépôts disponibles.
- **Retour arrière** : Corriger via procédure Red Hat/Satellite, pas édition manuelle.

## Si le problème n'est pas résolu

- [Documentation officielle](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9)
- [Cycle de vie Rocky Linux 9](../../Vie-du-systeme/Cycle-de-vie-50-etapes.md)
