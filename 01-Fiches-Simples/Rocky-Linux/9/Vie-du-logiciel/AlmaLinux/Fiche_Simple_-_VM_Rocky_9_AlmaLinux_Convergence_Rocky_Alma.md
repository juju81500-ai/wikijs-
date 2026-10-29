# Fiche_Simple_-_VM_Rocky_9_AlmaLinux_Convergence_Rocky_Alma

- **Environnement** : VM Rocky Linux 9 comme repère documentaire; sujet AlmaLinux
- **OS / Version** : AlmaLinux 8/9 selon la matrice officielle du chemin étudié; contrôles depuis clone Rocky Linux 9
- **Catégorie** : Vie du logiciel / AlmaLinux — Cadrer Rocky ↔ AlmaLinux
- **Tags** : `rocky9`, `almalinux`, `rhel`, `migration`

---

## Problème précis à résoudre

Standardiser les systèmes sans supposer de conversion in-place générique.

## 1. Hors-Production (Lab / Test / POC)

1. Cadrer Rocky ↔ AlmaLinux :
   ```bash
   cat /etc/os-release
sudo dnf repolist --enabled
sudo dnf repoquery --installed --qf "%{name} %{evr} %{repoid}" | sort | head -100
   ```
   👉 Explication : Établit un inventaire de comparaison.


## 2. Production — Contrôles

Préférer reconstruction/migration de données sauf chemin exact validé par le fournisseur.

## 3. Production — Sécurité

Ne pas exécuter scripts tiers ni `dnf distro-sync` comme méthode de conversion.

## Validation et retour arrière

- **Validation** : Stratégie, tests et restauration approuvés.
- **Retour arrière** : Conserver l’OS actuel si le chemin n’est pas documenté.

## Si le problème n'est pas résolu

- [Documentation officielle](https://wiki.almalinux.org/elevate/)
- [Cycle de vie Rocky Linux 9](../../Vie-du-systeme/Cycle-de-vie-50-etapes.md)
