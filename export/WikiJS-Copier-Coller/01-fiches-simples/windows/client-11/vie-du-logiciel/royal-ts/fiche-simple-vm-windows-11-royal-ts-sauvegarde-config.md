# Fiche_Simple_-_VM_Windows_11_Royal_TS_Sauvegarde_Config

- **Environnement** : Poste Windows 11 x64 d'administration (VM de test puis poste pilote)
- **OS / Version** : Windows 11 x64; Royal TS VERSION_ROYAL_TS (à remplacer)
- **Catégorie** : gestionnaire de connexions distantes

---

## Problème précis à résoudre

Sauvegarder et restaurer documents et paramètres Royal TS.

## 1. Hors-Production (Lab / Test / POC)

1. Fermer le document ouvert.
   👉 Explication : évite un fichier verrouillé.

2. `Copy-Item "C:\Documents\NOM_DOCUMENT.rtsz" "C:\Sauvegardes\RoyalTS\NOM_DOCUMENT_DATE.rtsz"` (à remplacer).
   👉 Explication : copie du document.

3. GUI : **File > Save As** vers `C:\Sauvegardes\RoyalTS\`.
   👉 Explication : alternative.

4. Restaurer : **File > Open** sur la copie ou `Copy-Item` inverse.
   👉 Explication : remet l'état antérieur.

5. Les paramètres de l'application peuvent être sous `%APPDATA%` : vérifier l'emplacement réel avant copie.
   👉 Explication : chemin non confirmé.

## 2. Production — Contrôles

Test de restauration sur VM vierge.

## 3. Production — Sécurité

- Chiffrer les sauvegardes ; clés privées sauvegardées séparément.

## Validation et retour arrière

- **Validation** : Le document restauré s'ouvre avec ses connexions.
- **Retour arrière** : Recopier la sauvegarde précédente.

## Si le problème n'est pas résolu

- Tous les éléments en MAJUSCULES sont des placeholders **à remplacer** ; ne jamais saisir de vrais secrets dans une fiche ou un ticket.
- [Royal TS — documentation officielle](https://docs.royalapps.com/)
- [Royal TS — site officiel](https://www.royalapps.com/ts/win/features)
- [Royal TS — téléchargement](https://www.royalapps.com/ts/win/download)