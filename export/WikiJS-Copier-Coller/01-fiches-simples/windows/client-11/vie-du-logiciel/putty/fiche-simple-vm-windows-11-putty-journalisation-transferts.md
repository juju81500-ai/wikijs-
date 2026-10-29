# Fiche_Simple_-_VM_Windows_11_PuTTY_Journalisation_Transferts.md

- **Environnement** : Poste Windows 11 x64 d'administration
- **OS / Version** : Windows 11 x64; PuTTY 0.85 Stable
- **Catégorie** : client SSH / données

---

## Problème précis à résoudre

Éviter les fuites par journaux et transferts.

## 1. Hors-Production (Lab / Test / POC)

1. Laisser la journalisation désactivée; si une politique l'impose, **Session > Logging**, choisir un dossier approuvé à ACL restreintes.
   👉 Explication : les sorties peuvent contenir identifiants et données métier.

2. Définir rotation et rétention des journaux, et les relire avant tout partage.
   👉 Explication : limite la diffusion de données sensibles.

3. Ne pas utiliser Telnet ni Rlogin pour une administration réelle.
   👉 Explication : ils ne protègent pas les identifiants.

4. Pour PSCP/PSFTP, utiliser une destination autorisée et vérifier les fichiers transférés de façon indépendante.
   👉 Explication : évite les erreurs de destination et les altérations.

## 2. Production — Contrôles

Journaux dans un dossier à droits restreints.

## 3. Production — Sécurité

- Éviter l'option SCP non sûre.
- Ne jamais transférer de clé privée vers l'hôte distant.

## Validation et retour arrière

- **Validation** : Aucun journal ou transfert non prévu.
- **Retour arrière** : Supprimer les journaux selon la politique de rétention.

## Si le problème n'est pas résolu

- [PuTTY — page officielle](https://www.chiark.greenend.org.uk/~sgtatham/putty/)
- [PuTTY — clés de signature](https://www.chiark.greenend.org.uk/~sgtatham/putty/keys.html)
- [Guide complet — 6. Journalisation, transferts et données sensibles](/02-fiches-completes/windows/client-11/installation-deploiement/84-deploiement-putty-0-85-windows-11#6-journalisation-transferts-et-donnees-sensibles)