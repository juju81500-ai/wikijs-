# Fiche_Simple_-_VM_Windows_11_Royal_TS_Coffre_Identifiants

- **Environnement** : Poste Windows 11 x64 d'administration (VM de test puis poste pilote)
- **OS / Version** : Windows 11 x64; Royal TS VERSION_ROYAL_TS (à remplacer)
- **Catégorie** : gestionnaire de connexions distantes

---

## Problème précis à résoudre

Stocker identifiants et clés privées via le coffre de Royal TS.

## 1. Hors-Production (Lab / Test / POC)

1. Dans le document : clic droit > **Add > Credential** ; nommer IDENTIFIANT_LAB et choisir le type mot de passe ou clé privée.
   👉 Explication : centralise les secrets.

2. Saisir UTILISATEUR_CIBLE (à remplacer) ; ne pas noter le mot de passe dans la fiche.
   👉 Explication : secret hors documentation.

3. Pour une clé : référencer le fichier `%USERPROFILE%\.ssh\CLE_PRIVEE` (à remplacer), protégé par passphrase.
   👉 Explication : la clé reste séparée de son secret.

4. Protéger le document : **Document Properties** > option de chiffrement/mot de passe du document (nom à vérifier).
   👉 Explication : dans la version utilisée ; le mécanisme de chiffrement n'est pas affirmé ici (à vérifier chez l'éditeur).

5. Si utilisation d'un coffre externe (Password Manager) : suivre la doc officielle ; non vérifié ici.
   👉 Explication : hors périmètre vérifié.

## 2. Production — Contrôles

Désigner un propriétaire du coffre et définir un plan de rotation.

## 3. Production — Sécurité

- Clé privée et passphrase conservées séparément.
- Ne pas partager un document contenant des identifiants sans chiffrement.
- Pour le Gestionnaire d'identifiants Windows : `cmdkey /list`.

## Validation et retour arrière

- **Validation** : Une connexion utilise l'identifiant référencé sans mot de passe visible.
- **Retour arrière** : Supprimer l'objet Credential et la clé de test.

## Si le problème n'est pas résolu

- Tous les éléments en MAJUSCULES sont des placeholders **à remplacer** ; ne jamais saisir de vrais secrets dans une fiche ou un ticket.
- [Royal TS — documentation officielle](https://docs.royalapps.com/)
- [Royal TS — site officiel](https://www.royalapps.com/ts/win/features)
- [Royal TS — téléchargement](https://www.royalapps.com/ts/win/download)