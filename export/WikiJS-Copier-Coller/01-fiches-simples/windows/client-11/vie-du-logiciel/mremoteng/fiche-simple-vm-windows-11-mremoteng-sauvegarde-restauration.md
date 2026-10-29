# Fiche_Simple_-_VM_Windows_11_mRemoteNG_Sauvegarde_Restauration

- **Environnement** : Poste Windows 11 x64 d'administration (VM de test puis poste pilote)
- **OS / Version** : Windows 11 x64; mRemoteNG VERSION_MREMOTENG (à remplacer)
- **Catégorie** : gestionnaire de connexions distantes

---

## Problème précis à résoudre

Sauvegarder et restaurer le fichier de connexions mRemoteNG.

## 1. Hors-Production (Lab / Test / POC)

1. Fermer mRemoteNG.
   👉 Explication : évite un fichier en cours d'écriture.

2. `Copy-Item "$env:APPDATA\mRemoteNG\confCons.xml" "C:\Sauvegardes\mRemoteNG\confCons_DATE.xml"` (DATE à remplacer ; nom du fichier à vérifier).
   👉 Explication : copie du fichier de connexions.

3. GUI alternative : **File > Save Connection File As…** vers `C:\Sauvegardes\mRemoteNG\`.
   👉 Explication : sauvegarde depuis l'interface.

4. Restaurer : **File > Open Connection File…** ou `Copy-Item` inverse application fermée.
   👉 Explication : remet l'ancien état.

5. Archiver aussi les fichiers de clés SSH séparément et chiffrés.
   👉 Explication : les clés ne doivent pas voyager avec le fichier.

## 2. Production — Contrôles

Tester la restauration sur une VM vierge.

## 3. Production — Sécurité

- Chiffrer le dossier de sauvegarde.
- Ne pas stocker MOT_DE_PASSE_FICHIER à côté de la sauvegarde.

## Validation et retour arrière

- **Validation** : Après restauration, les connexions sont présentes.
- **Retour arrière** : Recopier la sauvegarde précédente.

## Si le problème n'est pas résolu

- Tous les éléments en MAJUSCULES sont des placeholders **à remplacer** ; ne jamais saisir de vrais secrets dans une fiche ou un ticket.
- [mRemoteNG — documentation officielle](https://mremoteng.readthedocs.io/en/latest/)
- [mRemoteNG — dépôt et releases](https://github.com/mRemoteNG/mRemoteNG/releases)
- [mRemoteNG — site officiel](https://mremoteng.org/)