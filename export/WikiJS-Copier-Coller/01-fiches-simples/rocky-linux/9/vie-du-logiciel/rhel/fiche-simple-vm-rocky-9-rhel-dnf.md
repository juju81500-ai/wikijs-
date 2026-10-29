# Fiche_Simple_-_VM_Rocky_9_RHEL_DNF

- **Environnement** : VM Rocky Linux 9 comme repère documentaire; sujet RHEL
- **OS / Version** : Red Hat Enterprise Linux 9; commandes RHSM sur RHEL autorisé
- **Catégorie** : Vie du logiciel / RHEL — Mettre à jour avec DNF

---

## Problème précis à résoudre

Examiner errata et appliquer mises à jour RHEL des dépôts autorisés.

## 1. Hors-Production (Lab / Test / POC)

1. Mettre à jour avec DNF :
   ```bash
   sudo dnf check-update; test "$?" -le 100
sudo dnf updateinfo list --available
   ```
   👉 Explication : Code 100 indique mises à jour disponibles; examiner advisories.

## 2. Production — Contrôles

Appliquer en fenêtre approuvée, vérifier reboot et historique; upgrades majeurs séparés.

## 3. Production — Sécurité

Dépôts signés et autorisés uniquement; vérifier RHSM.

## Validation et retour arrière

- **Validation** : Paquets/errata tracés, services actifs.
- **Retour arrière** : Restaurer selon procédure approuvée; `dnf history undo` ne remplace pas backup.

## Si le problème n'est pas résolu

- [Documentation officielle](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9)
- [Cycle de vie Rocky Linux 9](/01-fiches-simples/rocky-linux/9/vie-du-systeme/cycle-de-vie-50-etapes)