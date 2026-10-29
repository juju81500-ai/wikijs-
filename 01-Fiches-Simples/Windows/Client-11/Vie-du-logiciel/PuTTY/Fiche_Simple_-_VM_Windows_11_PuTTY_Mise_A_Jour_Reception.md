# Fiche_Simple_-_VM_Windows_11_PuTTY_Mise_A_Jour_Reception.md

- **Environnement** : Poste Windows 11 x64 d'administration
- **OS / Version** : Windows 11 x64; PuTTY 0.85 Stable
- **Catégorie** : client SSH / maintenance
- **Tags** : `putty`, `windows11`, `ssh`, `puttygen`, `host-key`

---

## Problème précis à résoudre

Maintenir PuTTY à jour et valider les critères de réception.

## 1. Hors-Production (Lab / Test / POC)

1. Consulter régulièrement la page Stable et ses notes de version.
   👉 Explication : repère les correctifs de sécurité.

2. Télécharger le nouveau MSI et sa signature, vérifier la clé Release en cours.
   👉 Explication : la clé peut changer après rotation; refaire les vérifications de l'étape de téléchargement.

3. Tester la mise à jour sur un poste pilote.
   👉 Explication : évite un déploiement défectueux.

4. Contrôler la version :
   ```powershell
   & "$env:ProgramFiles\PuTTY\putty.exe" -V
   ```
   👉 Explication : doit afficher la nouvelle version.

## 2. Production — Contrôles

Recette : MSI officiel signé, SSH vers hôte autorisé, empreinte comparée, clé chiffrée, agent désactivé, journaux protégés.

## 3. Production — Sécurité

- Aucune mise à jour sans vérification de signature.

## Validation et retour arrière

- **Validation** : Tous les critères de recette sont satisfaits.
- **Retour arrière** : Réinstaller la version précédente vérifiée.

## Si le problème n'est pas résolu

- [PuTTY — page officielle](https://www.chiark.greenend.org.uk/~sgtatham/putty/)
- [PuTTY — clés de signature](https://www.chiark.greenend.org.uk/~sgtatham/putty/keys.html)
- [Guide complet — 7. Mise à jour et réception](../../../../../02-Fiches-Completes/Windows/Client-11/Installation-Deploiement/84_Deploiement_PuTTY_0.85_Windows_11.md#7-mise-a-jour-et-reception)
