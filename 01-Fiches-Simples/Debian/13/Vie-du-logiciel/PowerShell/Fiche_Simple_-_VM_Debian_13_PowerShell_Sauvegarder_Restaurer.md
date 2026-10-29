# Fiche_Simple_-_VM_Debian_13_PowerShell_Sauvegarder_Restaurer

- **Environnement** : VM Debian 13 de laboratoire avec dépôts Microsoft officiels
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : shell / scripting
- **Tags** : `debian13`, `powershell`, `pwsh`, `scripting`, `securite`
---

## Problème précis à résoudre

Préserver profil, versions de modules et procédures de reprise.

## 1. Hors-Production (Lab / Test / POC)

1. Inventorier modules sans enregistrer leurs valeurs sensibles
   ```powershell
   Get-InstalledModule | Select-Object Name,Version,Repository
   ```
   👉 Explication : archiver inventaire et versions, pas les secrets.

2. Sauvegarder profil utilisateur
   ```powershell
   Copy-Item $PROFILE "$PROFILE.before" -ErrorAction SilentlyContinue
   ```
   👉 Explication : contrôler permissions et absence de secret.

3. Tester reprise sur profil isolé
   ```text
   Navigateur > ouvrir la documentation officielle : https://learn.microsoft.com/powershell/scripting/install/install-debian
   ```
   👉 Explication : ne pas appliquer profil de test aux comptes production sans revue. Détail à confirmer dans la documentation officielle avant application : Restaurer la copie dans un compte de test puis lancer pwsh -NoProfile et vérifier l’import de modules.

4. Documenter accès et dépendances
   ```text
   Navigateur > ouvrir la documentation officielle : https://learn.microsoft.com/powershell/scripting/install/install-debian
   ```
   👉 Explication : gestionnaire de secrets distinct pour credentials. Détail à confirmer dans la documentation officielle avant application : Consigner les versions, sources et étapes pour reconstituer le profil; ne pas y inclure token.

## 2. Production — Contrôles

RPO/RTO concernent scripts, modules et profils; distinguer les fichiers de configuration des secrets d’accès.

## 3. Production — Sécurité

- Chiffrer tout export de configuration sensible.
- Ne pas sauvegarder credentials en clair avec profils.
- Tester périodiquement la reconstitution d’un environnement.

## Validation et retour arrière

- **Validation** : Un environnement isolé est reconstitué et lance le script témoin.
- **Retour arrière** : Restaurer profil antérieur et versions de modules autorisées.

## Si le problème n'est pas résolu

- [Microsoft Learn — installer Debian](https://learn.microsoft.com/powershell/scripting/install/install-debian)
- [Microsoft Learn — sécurité](https://learn.microsoft.com/powershell/scripting/security/security-features)
- [Fiche connexe](<Fiche_Simple_-_VM_Debian_13_PowerShell_Prerequis_Limites.md>)
