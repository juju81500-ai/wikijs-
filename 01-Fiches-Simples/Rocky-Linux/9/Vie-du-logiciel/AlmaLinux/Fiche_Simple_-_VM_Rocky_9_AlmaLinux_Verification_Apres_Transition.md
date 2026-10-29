# Fiche_Simple_-_VM_Rocky_9_AlmaLinux_Verification_Apres_Transition

- **Environnement** : VM Rocky Linux 9 comme repère documentaire; sujet AlmaLinux
- **OS / Version** : AlmaLinux 8/9 selon la matrice officielle du chemin étudié; contrôles depuis clone Rocky Linux 9
- **Catégorie** : Vie du logiciel / AlmaLinux — Vérifier après transition
- **Tags** : `rocky9`, `almalinux`, `rhel`, `migration`

---

## Problème précis à résoudre

Contrôler identité, dépôts, services et sécurité après reconstruction ou migration supportée.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier après transition :
   ```bash
   cat /etc/os-release
sudo dnf repolist --enabled
sudo dnf check
sudo dnf history list | head -20
   ```
   👉 Explication : Vérifie version, dépôts et dépendances.


## 2. Production — Contrôles

Contrôler journaux, réseau, stockage, sauvegardes, applis et avis AlmaLinux.

## 3. Production — Sécurité

Conserver SELinux enforcing; ne pas importer dépôts/clés d’une autre distribution.

## Validation et retour arrière

- **Validation** : Contrôles système/applications passés et inventaire actualisé.
- **Retour arrière** : Restaurer l’image de référence si OS/dépôts/services incohérents.

## Si le problème n'est pas résolu

- [Documentation officielle](https://wiki.almalinux.org/elevate/)
- [Cycle de vie Rocky Linux 9](../../Vie-du-systeme/Cycle-de-vie-50-etapes.md)
