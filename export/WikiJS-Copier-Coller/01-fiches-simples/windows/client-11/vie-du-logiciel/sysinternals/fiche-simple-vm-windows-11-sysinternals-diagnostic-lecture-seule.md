# Fiche_Simple_-_VM_Windows_11_Sysinternals_Diagnostic_Lecture_Seule.md

- **Environnement** : Poste Windows 11 administré, diagnostic défensif local
- **OS / Version** : Windows 11; suite Sysinternals de Microsoft Learn ou Microsoft Store
- **Catégorie** : diagnostic / lecture seule

---

## Problème précis à résoudre

Examiner processus, démarrages automatiques et événements sans rien modifier.

## 1. Hors-Production (Lab / Test / POC)

1. Lancer **procexp64.exe** (Process Explorer) et examiner arborescence, éditeur/signature, chemin d'image, parent, ressources et connexions.
   👉 Explication : compare aux inventaires et journaux; ne jamais terminer un processus système sur un simple nom ou une alerte heuristique.

2. Lancer **Autoruns** : activer **Options > Verify Code Signatures** et **Hide Microsoft Entries**.
   👉 Explication : réduit le bruit; une absence de signature n'est pas une preuve de malveillance.

3. Pour une entrée inconnue, noter chemin, éditeur, empreinte et contexte; ne rien décocher ni supprimer pendant l'inventaire initial.
   👉 Explication : suivre ensuite le processus d'analyse et de changement approuvé.

4. Lancer **Procmon64.exe** (Process Monitor) puis définir d'abord des filtres ciblés avec **Filter > Filter...**.
   👉 Explication : évite une collecte globale prolongée.

5. Sauvegarder au format natif seulement si nécessaire : **File > Save**.
   👉 Explication : la trace doit rester à accès limité avec rétention définie.

## 2. Production — Contrôles

Durée courte et catégories d'événements requises uniquement.

## 3. Production — Sécurité

- Exports et traces dans un emplacement protégé.

## Validation et retour arrière

- **Validation** : processus, démarrages et événements examinés sans modification.
- **Retour arrière** : fermer les outils; aucun changement système n'a été fait.

## Si le problème n'est pas résolu

- [Microsoft Learn — Process Explorer](https://learn.microsoft.com/en-us/sysinternals/downloads/process-explorer)
- [Microsoft Learn — Autoruns](https://learn.microsoft.com/en-us/sysinternals/downloads/autoruns)
- [Microsoft Learn — Process Monitor](https://learn.microsoft.com/en-us/sysinternals/downloads/procmon)
- [Microsoft Learn — Sysinternals Suite](https://learn.microsoft.com/en-us/sysinternals/downloads/sysinternals-suite)
- [Guide complet — étape 3](/02-fiches-completes/windows/client-11/installation-deploiement/123-administration-microsoft-sysinternals-windows-11#3-diagnostic-en-lecture-seule)