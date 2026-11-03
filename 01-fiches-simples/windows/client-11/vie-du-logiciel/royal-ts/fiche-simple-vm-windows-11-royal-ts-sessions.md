# Fiche_Simple_-_VM_Windows_11_Royal_TS_Sessions

- **Environnement** : Poste Windows 11 x64 d'administration (VM de test puis poste pilote)
- **OS / Version** : Windows 11 x64; Royal TS VERSION_ROYAL_TS (à remplacer)
- **Catégorie** : gestionnaire de connexions distantes
- **Tags** : `royal-ts`, `windows11`, `session`, `connexions`

---

## Problème précis à résoudre

Créer un document Royal TS et une connexion sécurisée.

## 1. Hors-Production (Lab / Test / POC)

1. **File > New Document** ; l'enregistrer sous `C:\Documents\NOM_DOCUMENT.rtsz` (à remplacer).
   👉 Explication : le document contient les connexions.

2. Clic droit sur le document > **Add > Connection** > type Terminal/SSH ou Remote Desktop.
   👉 Explication : crée l'objet.

3. Renseigner **Computer Name** = HOTE_CIBLE (à remplacer).
   👉 Explication : cible.

4. Dans **Credentials**, choisir un identifiant référencé plutôt que saisir un mot de passe (voir fiche Coffre_Identifiants).
   👉 Explication : évite les secrets dupliqués.

5. Connecter via **Connect** (ou double-clic).
   👉 Explication : test.

## 2. Production — Contrôles

Convention de nommage et propriétaire du document.

## 3. Production — Sécurité

- Pas de mot de passe saisi directement dans la connexion.
- Exiger NLA (RDP) / SSH v2.

## Validation et retour arrière

- **Validation** : La connexion s'ouvre.
- **Retour arrière** : Supprimer l'objet de connexion.

## Si le problème n'est pas résolu

- Tous les éléments en MAJUSCULES sont des placeholders **à remplacer** ; ne jamais saisir de vrais secrets dans une fiche ou un ticket.
- [Royal TS — documentation officielle](https://docs.royalapps.com/)
- [Royal TS — site officiel](https://www.royalapps.com/ts/win/features)
- [Royal TS — téléchargement](https://www.royalapps.com/ts/win/download)
