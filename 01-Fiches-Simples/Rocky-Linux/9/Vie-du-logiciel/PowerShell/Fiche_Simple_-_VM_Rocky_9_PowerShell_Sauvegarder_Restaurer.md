# Fiche_Simple_-_VM_Rocky_9_PowerShell_Sauvegarder_Restaurer

- **Environnement** : VM Rocky Linux 9 de laboratoire, accès sudo, dépôt Microsoft pour RHEL 9
- **OS / Version** : Rocky Linux 9
- **Catégorie** : shell / scripting
- **Tags** : `rocky9`, `powershell`, `pwsh`, `scripting`

---

## Problème précis à résoudre

Sauvegarder et restaurer l'état de PowerShell 7 : profils, inventaire des modules, configuration SSH.

## 1. Hors-Production (Lab / Test / POC)

1. Exporter l'inventaire des modules :
   ```bash
   mkdir -p ~/sauvegarde-pwsh
   pwsh -NoLogo -NoProfile -Command 'Get-InstalledPSResource | Select-Object Name,Version | Export-Csv ~/sauvegarde-pwsh/modules.csv -NoTypeInformation'
   ```
   👉 Explication : permet de réinstaller des versions identiques.

2. Archiver les profils et le sous-système SSH :
   ```bash
   tar czf ~/sauvegarde-pwsh/pwsh-config.tgz -C ~ .config/powershell
   sudo cp /etc/ssh/sshd_config.d/50-powershell.conf ~/sauvegarde-pwsh/ 2>/dev/null || true
   sha256sum ~/sauvegarde-pwsh/*
   ```
   👉 Explication : conserve les fichiers de configuration et leurs empreintes ; aucun secret ne doit s'y trouver.

3. Restaurer les profils :
   ```bash
   tar xzf ~/sauvegarde-pwsh/pwsh-config.tgz -C ~
   ```
   👉 Explication : remet les profils en place.

4. Réinstaller les modules à l'identique :
   ```powershell
   Import-Csv ~/sauvegarde-pwsh/modules.csv | ForEach-Object { Install-PSResource -Name $_.Name -Version $_.Version -Scope CurrentUser }
   ```
   👉 Explication : réinstalle chaque module en version fixée (confirmation de dépôt non approuvé possible).

## 2. Production — Contrôles

Intégrer ces fichiers à la sauvegarde habituelle, chiffrée, hors machine. Commandes établies d'après la documentation officielle et non testées dans ce pack : à valider en lab avant toute production.

## 3. Production — Sécurité

- Chiffrer l'archive si le profil contient des chemins ou noms sensibles.
- Aucune clé privée SSH dans cette sauvegarde.

## Validation et retour arrière

- **Validation** : l'inventaire et l'archive existent, les empreintes sont conservées, la restauration en lab réussit.
- **Retour arrière** : supprimer les fichiers restaurés si la restauration était erronée et rejouer depuis l'archive précédente.

## Si le problème n'est pas résolu

- [Microsoft Learn — installer PowerShell sur Linux](https://learn.microsoft.com/powershell/scripting/install/installing-powershell-on-linux)
- [Fiche connexe — Prerequis Limites](Fiche_Simple_-_VM_Rocky_9_PowerShell_Prerequis_Limites.md)
