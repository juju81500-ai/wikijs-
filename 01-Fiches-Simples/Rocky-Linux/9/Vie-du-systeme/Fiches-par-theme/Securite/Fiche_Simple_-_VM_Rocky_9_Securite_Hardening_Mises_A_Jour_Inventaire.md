# Fiche_Simple_-_VM_Rocky_9_Securite_Hardening_Mises_A_Jour_Inventaire.md

- **Environnement** : VM ou serveur dédié Rocky Linux 9 avant ouverture en production
- **OS / Version** : Rocky Linux 9 / famille RHEL 9
- **Catégorie** : sécurité / mises à jour
- **Tags** : `rocky9`, `rhel9`, `hardening`, `dnf`

---

## Problème précis à résoudre

Appliquer les correctifs de sécurité et dresser l'état initial.

## 1. Hors-Production (Lab / Test / POC)

1. Lire la version et les mises à jour disponibles :
   ```bash
   cat /etc/rocky-release
   sudo dnf check-update
   ```
   👉 Explication : inventaire avant action.

2. Appliquer les correctifs de sécurité après lecture de la liste proposée :
   ```bash
   sudo dnf update --security
   ```
   👉 Explication : limite la mise à jour aux avis de sécurité.

3. Consulter l'historique et les services en échec :
   ```bash
   sudo dnf history list
   systemctl --failed
   ```
   👉 Explication : permet de repérer la transaction à annuler si besoin.

## 2. Production — Contrôles

Après mise à jour noyau ou libc, planifier un redémarrage contrôlé.

## 3. Production — Sécurité

- Examiner les changements avant de confirmer.

## Validation et retour arrière

- **Validation** : aucun service en échec après mise à jour.
- **Retour arrière** : annuler une transaction identifiée avec `sudo dnf history undo ID` (ID relevé dans `dnf history list`).

## Si le problème n'est pas résolu

- [Rocky Linux — documentation](https://docs.rockylinux.org/)
- [Red Hat — SELinux sur RHEL 9](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/using_selinux/)
- [Guide complet hardening Rocky Linux 9](../../../../../../02-Fiches-Completes/Rocky-Linux/9/Autres/24_Hardening_Production_Rocky_Linux_9.md#2-mettre-a-jour-et-inventorier)
