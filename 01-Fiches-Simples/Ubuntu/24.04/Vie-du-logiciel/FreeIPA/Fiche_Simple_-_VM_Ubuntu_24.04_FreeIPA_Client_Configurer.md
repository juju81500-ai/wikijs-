# Fiche_Simple_-_VM_Ubuntu_24.04_FreeIPA_Client_Configurer

- **Environnement** : VM Ubuntu 24.04 cliente d'un domaine FreeIPA existant
- **OS / Version** : Ubuntu 24.04 LTS Noble; paquet freeipa-client des dépôts, version à vérifier
- **Catégorie** : FreeIPA client / configurer
- **Tags** : `freeipa`, `ubuntu24-04`, `vie-du-logiciel`, `configurer`

---

## Problème précis à résoudre

Inscrire le client Ubuntu au domaine FreeIPA.

## 1. Hors-Production (Lab / Test / POC)

1. Lancer l'inscription interactive :
   ```bash
   sudo ipa-client-install --domain=IPA_DOMAIN --realm=IPA_REALM --server=IPA_SERVER_FQDN --mkhomedir -p ADMIN_PRINCIPAL -W
   ```
   👉 Explication : IPA_DOMAIN, IPA_REALM (en majuscules, par convention), IPA_SERVER_FQDN et ADMIN_PRINCIPAL (compte autorisé à inscrire des hôtes) sont à remplacer. -W demande le mot de passe au clavier : ne jamais le passer en argument. --mkhomedir crée le répertoire personnel à la première connexion.

2. Confirmer les valeurs détectées lorsque l'outil les affiche, puis laisser l'outil configurer SSSD, Kerberos et NTP.
   👉 Explication : Relire le récapitulatif avant de répondre yes.

3. Contrôler les fichiers produits :
   ```bash
   ls -l /etc/ipa/default.conf /etc/krb5.conf /etc/sssd/sssd.conf
   sudo systemctl status sssd --no-pager
   ```
   👉 Explication : sssd.conf est géré par l'outil; ne pas l'éditer à la main sans sauvegarde.

## 2. Production — Contrôles

Consigner l'hôte inscrit et le compte utilisé; l'hôte apparaît côté serveur (ipa host-show CLIENT_FQDN, CLIENT_FQDN à remplacer).

## 3. Production — Sécurité

- Pas de mot de passe dans l'historique shell; compte d'inscription à privilèges limités.

## Validation et retour arrière

- **Validation** : Message de fin Client configuration complete et sssd actif.
- **Retour arrière** : sudo ipa-client-install --uninstall puis supprimer l'hôte côté serveur par l'administrateur (ipa host-del CLIENT_FQDN).

## Si le problème n'est pas résolu

- [Étape suivante du guide](./Fiche_Simple_-_VM_Ubuntu_24.04_FreeIPA_Client_Securiser.md)
- [Fiche d'entrée du logiciel](../../../../Logiciels/05-Systemes-annuaires-et-services/Fiche_Logiciel_-_FreeIPA.md)
- [FreeIPA — page Client](https://www.freeipa.org/page/Client)
- [FreeIPA — page Documentation](https://www.freeipa.org/page/Documentation)
