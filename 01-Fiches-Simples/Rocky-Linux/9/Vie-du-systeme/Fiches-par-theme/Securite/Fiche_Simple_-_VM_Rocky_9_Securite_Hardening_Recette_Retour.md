# Fiche_Simple_-_VM_Rocky_9_Securite_Hardening_Recette_Retour.md

- **Environnement** : VM ou serveur dédié Rocky Linux 9 avant ouverture en production
- **OS / Version** : Rocky Linux 9 / famille RHEL 9
- **Catégorie** : sécurité / recette
- **Tags** : `rocky9`, `rhel9`, `hardening`, `recette`, `rollback`

---

## Problème précis à résoudre

Valider le durcissement et savoir revenir en arrière.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler les ports attendus :
   ```bash
   sudo ss -lntup
   ```
   👉 Explication : seuls les ports prévus écoutent.

2. Contrôler SELinux, services et réseau après redémarrage contrôlé :
   ```bash
   sudo systemctl reboot
   ```
   👉 Explication : prouve que la configuration survit au boot.

3. Après reconnexion, relire l'état :
   ```bash
   getenforce
   systemctl --failed
   ```
   👉 Explication : aucun service en échec, SELinux Enforcing.

## 2. Production — Contrôles

Tester administration, application, refus depuis une source non autorisée et restauration d'une sauvegarde en VM isolée.

## 3. Production — Sécurité

- Ne jamais désactiver le pare-feu ou SELinux pour rétablir un service.

## Validation et retour arrière

- **Validation** : tous les tests de la recette sont réussis.
- **Retour arrière** : depuis la console, corriger la dernière règle et restaurer le fichier sauvegardé (`/etc/ssh.avant-hardening`).

## Si le problème n'est pas résolu

- [Rocky Linux — documentation](https://docs.rockylinux.org/)
- [Red Hat — SELinux sur RHEL 9](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/using_selinux/)
- [Guide complet hardening Rocky Linux 9](../../../../../../02-Fiches-Completes/Rocky-Linux/9/Autres/24_Hardening_Production_Rocky_Linux_9.md#7-recette-et-retour-arriere)
