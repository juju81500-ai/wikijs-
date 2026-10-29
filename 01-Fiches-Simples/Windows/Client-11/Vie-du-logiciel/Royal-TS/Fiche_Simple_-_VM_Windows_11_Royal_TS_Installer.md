# Fiche_Simple_-_VM_Windows_11_Royal_TS_Installer

- **Environnement** : Poste Windows 11 x64 d'administration (VM de test puis poste pilote)
- **OS / Version** : Windows 11 x64; Royal TS VERSION_ROYAL_TS (à remplacer)
- **Catégorie** : gestionnaire de connexions distantes
- **Tags** : `royal-ts`, `windows11`, `installation`, `winget`

---

## Problème précis à résoudre

Installer Royal TS sur Windows 11.

## 1. Hors-Production (Lab / Test / POC)

1. Télécharger l'installateur depuis https://www.royalapps.com/ts/win/download.
   👉 Explication : source officielle.

2. GUI : exécuter l'installateur et suivre l'assistant.
   👉 Explication : installation de référence.

3. Dans PowerShell, chercher le nom exact : `winget search "Royal TS" --source winget`. Relever l'ID exact affiché (colonne Id) et le noter comme ID_PAQUET_VERIFIE (à remplacer ; ne jamais le deviner). Puis, ID vérifié seulement : `winget install --id ID_PAQUET_VERIFIE --exact`. Si la recherche ne renvoie rien, utiliser le GUI.
   👉 Explication : l'ID du paquet doit venir du catalogue réel de la machine ; il n'a pas pu être vérifié lors de la rédaction de cette fiche.

4. Lancer Royal TS puis **Help/About** (libellé à vérifier).
   👉 Explication : lit la version installée.

## 2. Production — Contrôles

Pilote d'abord ; noter version et source.

## 3. Production — Sécurité

- `Get-AuthenticodeSignature "CHEMIN_EXE"` (CHEMIN_EXE à remplacer).

## Validation et retour arrière

- **Validation** : Royal TS démarre avec la version attendue.
- **Retour arrière** : **Paramètres > Applications** > désinstaller, ou `winget uninstall --id ID_PAQUET_VERIFIE`.

## Si le problème n'est pas résolu

- Tous les éléments en MAJUSCULES sont des placeholders **à remplacer** ; ne jamais saisir de vrais secrets dans une fiche ou un ticket.
- [Royal TS — documentation officielle](https://docs.royalapps.com/)
- [Royal TS — site officiel](https://www.royalapps.com/ts/win/features)
- [Royal TS — téléchargement](https://www.royalapps.com/ts/win/download)
