# Fiche_Simple_-_VM_Windows_11_Royal_TS_Prerequis

- **Environnement** : Poste Windows 11 x64 d'administration (VM de test puis poste pilote)
- **OS / Version** : Windows 11 x64; Royal TS VERSION_ROYAL_TS (à remplacer)
- **Catégorie** : gestionnaire de connexions distantes

---

## Problème précis à résoudre

Préparer Windows 11 pour Royal TS.

## 1. Hors-Production (Lab / Test / POC)

1. `Get-ComputerInfo -Property OsName,OsVersion,OsArchitecture`.
   👉 Explication : confirme l'OS.

2. Vérifier la licence ou le mode d'essai LICENCE_ROYAL_TS (à remplacer).
   👉 Explication : le mode gratuit est limité en nombre de connexions ; limite exacte à vérifier chez l'éditeur.

3. Vérifier winget : `winget --version`.
   👉 Explication : requis pour la voie en ligne de commande.

4. Tester le réseau : `Test-NetConnection HOTE_CIBLE -Port 22` (HOTE_CIBLE à remplacer).
   👉 Explication : anticipe les blocages.

## 2. Production — Contrôles

Valider licence, édition et autorisation de l'éditeur.

## 3. Production — Sécurité

- Télécharger uniquement depuis royalapps.com ou le catalogue winget vérifié.

## Validation et retour arrière

- **Validation** : Prérequis relevés.
- **Retour arrière** : Aucun changement.

## Si le problème n'est pas résolu

- Tous les éléments en MAJUSCULES sont des placeholders **à remplacer** ; ne jamais saisir de vrais secrets dans une fiche ou un ticket.
- [Royal TS — documentation officielle](https://docs.royalapps.com/)
- [Royal TS — site officiel](https://www.royalapps.com/ts/win/features)
- [Royal TS — téléchargement](https://www.royalapps.com/ts/win/download)