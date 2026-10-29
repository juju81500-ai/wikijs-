# Fiche_Simple_-_VM_Rocky_9_RHEL_SELinux

- **Environnement** : VM Rocky Linux 9 comme repère documentaire; sujet RHEL
- **OS / Version** : Red Hat Enterprise Linux 9; commandes RHSM sur RHEL autorisé
- **Catégorie** : Vie du logiciel / RHEL — Diagnostiquer SELinux

---

## Problème précis à résoudre

Vérifier refus et corriger contexte via politiques documentées.

## 1. Hors-Production (Lab / Test / POC)

1. Diagnostiquer SELinux :
   ```bash
   getenforce
sestatus
sudo ausearch -m AVC,USER_AVC -ts recent
   ```
   👉 Explication : Affiche mode et AVC; installer les outils manquants depuis dépôts autorisés.

## 2. Production — Contrôles

Analyser chemin, label et policy; utiliser `semanage fcontext`/`restorecon` si documenté.

## 3. Production — Sécurité

Ne pas utiliser `setenforce 0` ni générer aveuglément une policy permissive; conserver enforcing.

## Validation et retour arrière

- **Validation** : Service fonctionne enforcing sans AVC inattendus.
- **Retour arrière** : Annuler la règle locale identifiée et restaurer label validé; garder enforcing.

## Si le problème n'est pas résolu

- [Documentation officielle](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9)
- [Cycle de vie Rocky Linux 9](/01-fiches-simples/rocky-linux/9/vie-du-systeme/cycle-de-vie-50-etapes)