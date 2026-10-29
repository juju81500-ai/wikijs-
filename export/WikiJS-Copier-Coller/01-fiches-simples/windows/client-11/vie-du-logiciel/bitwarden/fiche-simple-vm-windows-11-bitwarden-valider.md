# Fiche_Simple_-_VM_Windows_11_Bitwarden_Valider

- **Environnement** : Poste Windows 11 géré avec compte de test
- **OS / Version** : Windows 11 Client
- **Catégorie** : gestionnaire de mots de passe / client

---

## Problème précis à résoudre

Valider synchronisation, verrouillage et MFA avec une entrée factice.

## 1. Hors-Production (Lab / Test / POC)

1. Créer une entrée de recette fictive
   ```text
   Client > Coffre > Ajouter un élément > identifiant de test sans secret réutilisable.
   ```
   👉 Explication : ne pas importer de compte réel.

2. Vérifier synchronisation sur un second appareil géré
   ```text
   Navigateur > ouvrir la documentation officielle : https://bitwarden.com/download/
   ```
   👉 Explication : ne pas utiliser appareil personnel. Détail à confirmer dans la documentation officielle avant application : Ouvrir coffre de test sur second appareil approuvé et vérifier entrée factice.

3. Tester verrouillage automatique et MFA
   ```text
   Navigateur > ouvrir la documentation officielle : https://bitwarden.com/download/
   ```
   👉 Explication : vérifier qu’une session inactive ne révèle pas le coffre. Détail à confirmer dans la documentation officielle avant application : Verrouiller client, attendre délai configuré et rouvrir par mécanisme approuvé.

4. Supprimer données de recette
   ```text
   Navigateur > ouvrir la documentation officielle : https://bitwarden.com/download/
   ```
   👉 Explication : ne pas conserver données de test. Détail à confirmer dans la documentation officielle avant application : Supprimer entrée factice et révoquer sessions non nécessaires.

## 2. Production — Contrôles

Archiver preuves non sensibles et faire valider parcours utilisateur/support.

## 3. Production — Sécurité

- Tests avec données fictives uniquement.
- Ne pas capturer ou exporter coffre réel.
- Révoquer comptes/sessions de recette.

## Validation et retour arrière

- **Validation** : Entrée synchronise, MFA et verrouillage respectent les paramètres.
- **Retour arrière** : Supprimer entrée de test et révoquer session avant clôture.

## Si le problème n'est pas résolu

- [Bitwarden — téléchargement officiel](https://bitwarden.com/download/)
- [Bitwarden — application bureau](https://bitwarden.com/help/desktop-app/)
- [Bitwarden — exportation](https://bitwarden.com/help/export-your-data/)
- [Bitwarden — MFA](https://bitwarden.com/help/two-step-login/)
- [Fiche connexe](</01-fiches-simples/windows/client-11/vie-du-logiciel/bitwarden/fiche-simple-vm-windows-11-bitwarden-prerequis-limites>)