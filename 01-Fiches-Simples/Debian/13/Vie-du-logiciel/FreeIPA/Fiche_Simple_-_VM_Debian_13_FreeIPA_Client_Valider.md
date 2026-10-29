# Fiche_Simple_-_VM_Debian_13_FreeIPA_Client_Valider

- **Environnement** : VM Debian 13 cliente d'un domaine FreeIPA existant
- **OS / Version** : Debian 13 Trixie; paquet freeipa-client des dépôts, version à vérifier
- **Catégorie** : FreeIPA client / valider
- **Tags** : `freeipa`, `debian13`, `vie-du-logiciel`, `valider`

---

## Problème précis à résoudre

Recetter le client avec un utilisateur du domaine.

## 1. Hors-Production (Lab / Test / POC)

1. Obtenir un ticket Kerberos pour un utilisateur de test :
   ```bash
   kinit UTILISATEUR_IPA
   klist
   ```
   👉 Explication : UTILISATEUR_IPA est un compte de test du domaine (à remplacer); le mot de passe est saisi à l'invite.

2. Vérifier la résolution des identités via SSSD :
   ```bash
   id UTILISATEUR_IPA
   getent passwd UTILISATEUR_IPA
   sudo sssctl domain-status IPA_DOMAIN
   ```
   👉 Explication : La commande id doit retourner uid/gid issus du domaine; IPA_DOMAIN est à remplacer.

3. Tester une connexion SSH avec l'utilisateur du domaine :
   ```bash
   ssh UTILISATEUR_IPA@CLIENT_FQDN
   ```
   👉 Explication : CLIENT_FQDN est le nom du client (à remplacer); le répertoire personnel doit être créé à la première connexion.

## 2. Production — Contrôles

Consigner le résultat; tester aussi un utilisateur non autorisé par HBAC (refus attendu).

## 3. Production — Sécurité

- Utiliser un compte de test non administrateur.

## Validation et retour arrière

- **Validation** : Ticket Kerberos obtenu, identité résolue, connexion SSH acceptée ou refusée selon HBAC.
- **Retour arrière** : Désinscrire le client (voir la fiche Configurer).

## Si le problème n'est pas résolu

- [Étape suivante du guide](./Fiche_Simple_-_VM_Debian_13_FreeIPA_Client_Sauvegarder_Restaurer.md)
- [Fiche d'entrée du logiciel](../../../../Logiciels/05-Systemes-annuaires-et-services/Fiche_Logiciel_-_FreeIPA.md)
- [FreeIPA — page Client](https://www.freeipa.org/page/Client)
- [FreeIPA — page Documentation](https://www.freeipa.org/page/Documentation)
