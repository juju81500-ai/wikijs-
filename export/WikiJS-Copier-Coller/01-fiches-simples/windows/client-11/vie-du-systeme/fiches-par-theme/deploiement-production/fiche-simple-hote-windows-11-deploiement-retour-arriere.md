# Fiche_Simple_-_Hote_Windows_11_Deploiement_Retour_Arriere.md

- **Environnement** : Parc de postes utilisateur: poste physique ou VM de test
- **OS / Version** : Windows 11 Pro ou Enterprise selon la gestion prévue
- **Catégorie** : déploiement de poste de travail

---

## Problème précis à résoudre

Savoir quoi faire si enrôlement, chiffrement ou applications échouent.

## 1. Hors-Production (Lab / Test / POC)

1. Maintenir l'appareil hors remise utilisateur.
   👉 Explication : évite de livrer un poste non conforme.

2. Confirmer l'absence de données à conserver.
   👉 Explication : une réinitialisation efface les données locales.

3. Réinitialiser si nécessaire : **Paramètres > Système > Récupération > Réinitialiser le PC**.
   👉 Explication : revient à un état propre; sinon reprendre depuis l'image approuvée.

4. Reprendre le déploiement depuis l'image approuvée ou la séquence de l'outil de parc.
   👉 Explication : rétablit un état connu.

## 2. Production — Contrôles

Documenter la cause de l'échec avant de relancer le déploiement.

## 3. Production — Sécurité

- Retirer le poste de la console de gestion avant de le réinstaller pour éviter les doublons.

## Validation et retour arrière

- **Validation** : le poste redéployé passe de nouveau la recette.
- **Retour arrière** : sans objet: cette fiche décrit elle-même le retour arrière.

## Si le problème n'est pas résolu

- [Microsoft Learn — Autopilot](https://learn.microsoft.com/en-us/autopilot/)
- [Microsoft Learn — déployer Windows 11](https://learn.microsoft.com/en-us/windows/deployment/)
- [Guide complet](/02-fiches-completes/windows/client-11/installation-deploiement/25-deploiement-postes-windows-11-production#7-retour-arriere)