# Fiche_Simple_-_VM_Rocky_9_AlmaLinux_ELevate

- **Environnement** : VM Rocky Linux 9 comme repère documentaire; sujet AlmaLinux
- **OS / Version** : AlmaLinux 8/9 selon la matrice officielle du chemin étudié; contrôles depuis clone Rocky Linux 9
- **Catégorie** : Vie du logiciel / AlmaLinux — Évaluer ELevate
- **Tags** : `rocky9`, `almalinux`, `rhel`, `migration`

---

## Problème précis à résoudre

Utiliser ELevate/Leapp uniquement pour un chemin source→cible présent dans la matrice officielle courante.

## 1. Hors-Production (Lab / Test / POC)

1. Évaluer ELevate :
   ```bash
   cat /etc/os-release
printf "%s\n" "Consulter la matrice officielle ELevate avant installation ou lancement de Leapp."
   ```
   👉 Explication : ELevate ne convertit pas génériquement Rocky↔Alma; chemins dépendent des versions.


## 2. Production — Contrôles

Tester un clone, analyser preupgrade et suivre le guide exact. La page officielle ELevate indique que les données de migration nécessaires à la prise en charge de Rocky Linux n’ont pas été contribuées; ne pas considérer ELevate comme une voie générique Rocky↔Alma. Ne lancer que les paires source/cible explicitement présentes dans la matrice officielle courante.

## 3. Production — Sécurité

Sauvegarder, valider applications, console hors bande; ne pas ignorer inhibiteurs sans consigne.

## Validation et retour arrière

- **Validation** : Clone migre, démarre et passe les tests.
- **Retour arrière** : Restaurer snapshot/reconstruire; ne pas poursuivre migration partielle.

## Si le problème n'est pas résolu

- [Documentation officielle](https://wiki.almalinux.org/elevate/)
- [Cycle de vie Rocky Linux 9](../../Vie-du-systeme/Cycle-de-vie-50-etapes.md)
