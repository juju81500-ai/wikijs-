# Fiche_Simple_-_VM_Windows_11_MobaXterm_Installer

- **Environnement** : Poste Windows 11 x64 d'administration (VM de test puis poste pilote)
- **OS / Version** : Windows 11 x64; MobaXterm Home/Professional, version VERSION_MOBAXTERM (à remplacer)
- **Catégorie** : client SSH/RDP multi-sessions

---

## Problème précis à résoudre

Installer MobaXterm sur Windows 11 de façon contrôlée.

## 1. Hors-Production (Lab / Test / POC)

1. Télécharger l'installateur (ou la version portable) depuis https://mobaxterm.mobatek.net/download.html puis comparer le nom et la version à celle attendue (VERSION_MOBAXTERM, à remplacer).
   👉 Explication : source officielle et version voulue.

2. GUI : double-clic sur l'installateur MSI/EXE, suivre l'assistant ; chemin habituel de l'application : `C:\Program Files (x86)\Mobatek\MobaXterm\` (à vérifier selon la version).
   👉 Explication : l'installation GUI est la référence.

3. Dans PowerShell, chercher le nom exact : `winget search "MobaXterm" --source winget`. Relever l'ID exact affiché (colonne Id) et le noter comme ID_PAQUET_VERIFIE (à remplacer ; ne jamais le deviner). Puis, seulement avec l'ID vérifié : `winget install --id ID_PAQUET_VERIFIE --exact --source winget`.
   👉 Explication : l'ID du paquet doit venir du catalogue réel de la machine ; il n'a pas pu être vérifié lors de la rédaction de cette fiche.

4. Option portable : extraire l'archive dans `C:\Outils\MobaXterm\` (chemin à remplacer si besoin).
   👉 Explication : pas d'écriture système, mais pas de mise à jour automatique.

5. Lancer **MobaXterm** depuis le menu Démarrer puis **Help > About** pour lire la version.
   👉 Explication : prouve le résultat de l'installation.

## 2. Production — Contrôles

Installer d'abord sur la VM pilote ; consigner version, source, empreinte et date d'installation.

## 3. Production — Sécurité

- Contrôler la signature de l'exécutable : `Get-AuthenticodeSignature "CHEMIN_EXE"` (CHEMIN_EXE à remplacer).
- Refuser tout installateur téléchargé depuis un site tiers.

## Validation et retour arrière

- **Validation** : `Get-Package *Moba*` ou le menu Démarrer montre MobaXterm ; la version correspond.
- **Retour arrière** : Désinstaller via **Paramètres > Applications > Applications installées** (ou `winget uninstall --id ID_PAQUET_VERIFIE`), ou supprimer le dossier portable.

## Si le problème n'est pas résolu

- Tous les éléments en MAJUSCULES sont des placeholders **à remplacer** ; ne jamais saisir de vrais secrets dans une fiche ou un ticket.
- [MobaXterm — documentation officielle](https://mobaxterm.mobatek.net/documentation.html)
- [MobaXterm — téléchargement](https://mobaxterm.mobatek.net/download.html)
- [MobaXterm — FAQ](https://mobaxterm.mobatek.net/faq.html)