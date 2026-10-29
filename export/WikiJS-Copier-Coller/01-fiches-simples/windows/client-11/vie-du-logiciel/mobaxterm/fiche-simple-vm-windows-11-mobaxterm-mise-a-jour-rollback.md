# Fiche_Simple_-_VM_Windows_11_MobaXterm_Mise_A_Jour_Rollback

- **Environnement** : Poste Windows 11 x64 d'administration (VM de test puis poste pilote)
- **OS / Version** : Windows 11 x64; MobaXterm Home/Professional, version VERSION_MOBAXTERM (à remplacer)
- **Catégorie** : client SSH/RDP multi-sessions

---

## Problème précis à résoudre

Mettre à jour MobaXterm et pouvoir revenir à la version précédente.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder la configuration (fiche Sauvegarde_Restauration) et noter la version actuelle (**Help > About**).
   👉 Explication : point de retour.

2. GUI : **Help > Check for updates** ; télécharger la version VERSION_CIBLE (à remplacer) depuis le site officiel.
   👉 Explication : mise à jour officielle.

3. Dans PowerShell, chercher le nom exact : `winget search "MobaXterm" --source winget`. Relever l'ID exact affiché (colonne Id) et le noter comme ID_PAQUET_VERIFIE (à remplacer ; ne jamais le deviner). Puis : `winget upgrade --id ID_PAQUET_VERIFIE --exact` (seulement si l'ID est vérifié).
   👉 Explication : l'ID du paquet doit venir du catalogue réel de la machine ; il n'a pas pu être vérifié lors de la rédaction de cette fiche.

4. Relancer MobaXterm et revalider NOM_SESSION (à remplacer).
   👉 Explication : contrôle fonctionnel.

5. Rollback : désinstaller la version, réinstaller l'installateur précédent conservé dans `C:\Depots\MobaXterm\` (chemin à remplacer), puis restaurer le .ini.
   👉 Explication : retour à l'état connu ; la version précise peut exiger l'installateur conservé.

## 2. Production — Contrôles

Mettre à jour d'abord un poste pilote ; conserver l'installateur précédent.

## 3. Production — Sécurité

- Contrôler la signature du nouvel installateur.
- Lire les notes de version pour les changements de sécurité.

## Validation et retour arrière

- **Validation** : Version cible affichée et sessions opérationnelles.
- **Retour arrière** : Réinstaller l'ancienne version et restaurer la configuration sauvegardée.

## Si le problème n'est pas résolu

- Tous les éléments en MAJUSCULES sont des placeholders **à remplacer** ; ne jamais saisir de vrais secrets dans une fiche ou un ticket.
- [MobaXterm — documentation officielle](https://mobaxterm.mobatek.net/documentation.html)
- [MobaXterm — téléchargement](https://mobaxterm.mobatek.net/download.html)
- [MobaXterm — FAQ](https://mobaxterm.mobatek.net/faq.html)