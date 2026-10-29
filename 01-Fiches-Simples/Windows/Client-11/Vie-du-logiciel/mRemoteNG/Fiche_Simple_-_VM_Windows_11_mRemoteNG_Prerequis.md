# Fiche_Simple_-_VM_Windows_11_mRemoteNG_Prerequis

- **Environnement** : Poste Windows 11 x64 d'administration (VM de test puis poste pilote)
- **OS / Version** : Windows 11 x64; mRemoteNG VERSION_MREMOTENG (à remplacer)
- **Catégorie** : gestionnaire de connexions distantes
- **Tags** : `mremoteng`, `windows11`, `prerequis`

---

## Problème précis à résoudre

Préparer un poste Windows 11 pour mRemoteNG.

## 1. Hors-Production (Lab / Test / POC)

1. `Get-ComputerInfo -Property OsName,OsVersion,OsArchitecture`.
   👉 Explication : confirme Windows 11 x64.

2. Vérifier le prérequis .NET indiqué par la documentation de la version choisie : `Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\NET Framework Setup\NDP\v4\Full' | Select Release`.
   👉 Explication : la version .NET exigée dépend de la release ; à vérifier dans la documentation.

3. Lister les protocoles requis (SSH, RDP, VNC) et tester : `Test-NetConnection HOTE_CIBLE -Port 3389` (HOTE_CIBLE à remplacer).
   👉 Explication : anticipe les blocages réseau.

4. Vérifier winget : `winget --version`.
   👉 Explication : nécessaire à la voie PowerShell.

5. Décider du dossier de données : `%APPDATA%\mRemoteNG` (par défaut, à vérifier).
   👉 Explication : emplacement du fichier de connexions.

## 2. Production — Contrôles

Valider licence (open source), version approuvée et autorisation EDR.

## 3. Production — Sécurité

- Télécharger uniquement depuis le dépôt officiel GitHub ou le site officiel.
- Ne pas utiliser de session administrateur permanente.

## Validation et retour arrière

- **Validation** : Prérequis relevés et validés.
- **Retour arrière** : Aucun changement ; rien à annuler.

## Si le problème n'est pas résolu

- Tous les éléments en MAJUSCULES sont des placeholders **à remplacer** ; ne jamais saisir de vrais secrets dans une fiche ou un ticket.
- [mRemoteNG — documentation officielle](https://mremoteng.readthedocs.io/en/latest/)
- [mRemoteNG — dépôt et releases](https://github.com/mRemoteNG/mRemoteNG/releases)
- [mRemoteNG — site officiel](https://mremoteng.org/)
