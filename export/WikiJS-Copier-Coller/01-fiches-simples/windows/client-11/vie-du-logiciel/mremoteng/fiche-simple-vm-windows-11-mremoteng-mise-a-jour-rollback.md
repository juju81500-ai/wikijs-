# Fiche_Simple_-_VM_Windows_11_mRemoteNG_Mise_A_Jour_Rollback

- **Environnement** : Poste Windows 11 x64 d'administration (VM de test puis poste pilote)
- **OS / Version** : Windows 11 x64; mRemoteNG VERSION_MREMOTENG (à remplacer)
- **Catégorie** : gestionnaire de connexions distantes

---

## Problème précis à résoudre

Mettre à jour mRemoteNG avec retour arrière possible.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder confCons.xml (fiche précédente) et noter la version.
   👉 Explication : point de retour.

2. Télécharger VERSION_CIBLE (à remplacer) depuis la page Releases officielle.
   👉 Explication : source officielle.

3. GUI : exécuter le nouvel installateur par-dessus l'existant.
   👉 Explication : mise à jour standard.

4. Dans PowerShell, chercher le nom exact : `winget search "mRemoteNG" --source winget`. Relever l'ID exact affiché (colonne Id) et le noter comme ID_PAQUET_VERIFIE (à remplacer ; ne jamais le deviner). Puis `winget upgrade --id ID_PAQUET_VERIFIE --exact` si l'ID est vérifié.
   👉 Explication : l'ID du paquet doit venir du catalogue réel de la machine ; il n'a pas pu être vérifié lors de la rédaction de cette fiche.

5. Rollback : désinstaller, réinstaller l'ancien installateur conservé et restaurer confCons.xml.
   👉 Explication : un fichier de connexions modifié par une version récente peut ne pas être relisible par l'ancienne ; d'où la sauvegarde préalable.

## 2. Production — Contrôles

Pilote d'abord ; conserver l'ancien installateur.

## 3. Production — Sécurité

- Lire les notes de version pour correctifs de sécurité.
- Vérifier signature et hash.

## Validation et retour arrière

- **Validation** : La version cible démarre et ouvre les connexions.
- **Retour arrière** : Réinstaller l'ancienne version et restaurer la sauvegarde.

## Si le problème n'est pas résolu

- Tous les éléments en MAJUSCULES sont des placeholders **à remplacer** ; ne jamais saisir de vrais secrets dans une fiche ou un ticket.
- [mRemoteNG — documentation officielle](https://mremoteng.readthedocs.io/en/latest/)
- [mRemoteNG — dépôt et releases](https://github.com/mRemoteNG/mRemoteNG/releases)
- [mRemoteNG — site officiel](https://mremoteng.org/)