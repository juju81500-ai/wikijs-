# Fiche_Simple_-_VM_Ubuntu_24.04_FreeIPA_Client_Securiser

- **Environnement** : VM Ubuntu 24.04 cliente d'un domaine FreeIPA existant
- **OS / Version** : Ubuntu 24.04 LTS Noble; paquet freeipa-client des dépôts, version à vérifier
- **Catégorie** : FreeIPA client / sécuriser
- **Tags** : `freeipa`, `ubuntu24-04`, `vie-du-logiciel`, `securiser`

---

## Problème précis à résoudre

Durcir l'accès du client Ubuntu inscrit : droits, accès SSH, politiques centralisées.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier les droits des fichiers sensibles :
   ```bash
   sudo ls -l /etc/krb5.keytab /etc/sssd/sssd.conf
   ```
   👉 Explication : Le keytab et sssd.conf doivent appartenir à root, mode 0600.

2. Faire créer côté serveur une règle HBAC limitant qui peut se connecter à cet hôte (par l'administrateur FreeIPA) :
   👉 Explication : Console web FreeIPA > Politique > Contrôle d'accès basé sur l'hôte, ou commandes ipa hbacrule-* sur le serveur; désactiver la règle allow_all une fois les règles ciblées validées. Vérifier la procédure dans la documentation de la version du serveur.

3. Vérifier le pare-feu local :
   ```bash
   sudo ufw status verbose
   ```
   👉 Explication : N'autoriser SSH que depuis les réseaux d'administration; le client n'a pas besoin de ports entrants FreeIPA.

## 2. Production — Contrôles

Définir les règles sudo centralisées côté serveur plutôt que des fichiers sudoers locaux.

## 3. Production — Sécurité

- Désactiver l'authentification par mot de passe SSH si Kerberos/clés suffisent, après test.

## Validation et retour arrière

- **Validation** : Droits conformes et accès limité par HBAC.
- **Retour arrière** : Réactiver temporairement la règle HBAC précédente côté serveur (par l'administrateur).

## Si le problème n'est pas résolu

- [Étape suivante du guide](./Fiche_Simple_-_VM_Ubuntu_24.04_FreeIPA_Client_Valider.md)
- [Fiche d'entrée du logiciel](../../../../Logiciels/05-Systemes-annuaires-et-services/Fiche_Logiciel_-_FreeIPA.md)
- [FreeIPA — page Client](https://www.freeipa.org/page/Client)
- [FreeIPA — page Documentation](https://www.freeipa.org/page/Documentation)
