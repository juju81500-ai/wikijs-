# Fiche_Simple_-_VM_Windows_11_Bitwarden_Configurer

- **Environnement** : Poste Windows 11 géré avec compte de test
- **OS / Version** : Windows 11 Client
- **Catégorie** : gestionnaire de mots de passe / client
- **Tags** : `windows-11`, `bitwarden`, `mots-de-passe`, `mfa`, `securite`
---

## Problème précis à résoudre

Configurer compte, MFA, verrouillage et récupération depuis interface officielle.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir portail en saisissant URL manuellement
   ```text
   Navigateur > https://bitwarden.com/ > connexion/création de compte.
   ```
   👉 Explication : vérifier domaine et tenant organisation.

2. Créer secret maître unique et le saisir directement
   ```text
   Navigateur > ouvrir la documentation officielle : https://bitwarden.com/download/
   ```
   👉 Explication : ne jamais le placer dans terminal, document ou fichier non chiffré. Détail à confirmer dans la documentation officielle avant application : Utiliser générateur approuvé, puis saisir le mot de passe maître directement dans client.

3. Activer MFA dans paramètres
   ```text
   Portail > Paramètres du compte > Sécurité > Authentification à deux étapes (libellé selon version).
   ```
   👉 Explication : conserver recovery codes séparément dans emplacement approuvé.

4. Régler verrouillage automatique
   ```text
   Client > Paramètres > Sécurité > délai de verrouillage/déconnexion.
   ```
   👉 Explication : choisir une durée conforme au risque et à l’usage du poste.

## 2. Production — Contrôles

Aligner compte, MFA, recovery et délai de verrouillage avec la politique interne.

## 3. Production — Sécurité

- Ne pas désactiver MFA pour contourner incident.
- Ne pas confondre compte personnel et compte professionnel.
- Ne pas conserver recovery codes sur même appareil uniquement.

## Validation et retour arrière

- **Validation** : MFA, verrouillage et récupération sont testés sur un compte non sensible.
- **Retour arrière** : Déconnecter compte test, révoquer session et contacter support sans transmettre le maître.

## Si le problème n'est pas résolu

- [Bitwarden — téléchargement officiel](https://bitwarden.com/download/)
- [Bitwarden — application bureau](https://bitwarden.com/help/desktop-app/)
- [Bitwarden — exportation](https://bitwarden.com/help/export-your-data/)
- [Bitwarden — MFA](https://bitwarden.com/help/two-step-login/)
- [Fiche connexe](<Fiche_Simple_-_VM_Windows_11_Bitwarden_Prerequis_Limites.md>)
