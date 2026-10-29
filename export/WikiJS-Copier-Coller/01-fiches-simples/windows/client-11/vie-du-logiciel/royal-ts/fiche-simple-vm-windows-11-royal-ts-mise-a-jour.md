# Fiche_Simple_-_VM_Windows_11_Royal_TS_Mise_A_Jour

- **Environnement** : Poste Windows 11 x64 d'administration (VM de test puis poste pilote)
- **OS / Version** : Windows 11 x64; Royal TS VERSION_ROYAL_TS (à remplacer)
- **Catégorie** : gestionnaire de connexions distantes

---

## Problème précis à résoudre

Mettre à jour Royal TS avec retour arrière.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder le document (fiche précédente) et noter la version.
   👉 Explication : point de retour.

2. GUI : télécharger VERSION_CIBLE (à remplacer) depuis la page officielle et exécuter l'installateur.
   👉 Explication : mise à jour officielle.

3. Dans PowerShell, chercher le nom exact : `winget search "Royal TS" --source winget`. Relever l'ID exact affiché (colonne Id) et le noter comme ID_PAQUET_VERIFIE (à remplacer ; ne jamais le deviner). Puis `winget upgrade --id ID_PAQUET_VERIFIE --exact` si l'ID est vérifié.
   👉 Explication : l'ID du paquet doit venir du catalogue réel de la machine ; il n'a pas pu être vérifié lors de la rédaction de cette fiche.

4. Rouvrir le document et tester une connexion.
   👉 Explication : contrôle fonctionnel.

5. Rollback : désinstaller, réinstaller l'installateur précédent conservé et restaurer le document.
   👉 Explication : un document enregistré par une version récente peut ne pas s'ouvrir dans l'ancienne.

## 2. Production — Contrôles

Pilote d'abord ; conserver l'ancien installateur.

## 3. Production — Sécurité

- Vérifier la signature du nouvel installateur.

## Validation et retour arrière

- **Validation** : La version cible fonctionne avec le document.
- **Retour arrière** : Réinstaller l'ancienne version et restaurer la sauvegarde.

## Si le problème n'est pas résolu

- Tous les éléments en MAJUSCULES sont des placeholders **à remplacer** ; ne jamais saisir de vrais secrets dans une fiche ou un ticket.
- [Royal TS — documentation officielle](https://docs.royalapps.com/)
- [Royal TS — site officiel](https://www.royalapps.com/ts/win/features)
- [Royal TS — téléchargement](https://www.royalapps.com/ts/win/download)