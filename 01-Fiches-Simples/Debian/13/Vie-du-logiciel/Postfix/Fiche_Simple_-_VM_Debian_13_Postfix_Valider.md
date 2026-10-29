# Fiche_Simple_-_VM_Debian_13_Postfix_Valider

- **Environnement** : VM Debian 13; Postfix depuis les dépôts de la distribution
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : Messagerie et collaboratif / Postfix — Valider (recette)
- **Tags** : `debian13`, `postfix`, `smtp`, `messagerie`, `valider`

---

## Problème précis à résoudre

Recetter Postfix : service actif, ports, envoi local, refus de relais ouvert et chiffrement.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler le service et les ports :
   ```bash
   systemctl is-active postfix
   sudo ss -tlnp | grep master
   ```
   👉 Explication : le processus `master` doit écouter sur 25 (et 587 si activé).

2. Envoyer un message de test local :
   ```bash
   echo "test recette" | mail -s "Recette Postfix" UTILISATEUR_LOCAL
   ```
   👉 Explication : `UTILISATEUR_LOCAL` est à remplacer par un compte existant.

3. Suivre la remise :
   ```bash
   sudo journalctl -u postfix -n 30 --no-pager
   sudo postqueue -p
   ```
   👉 Explication : `status=sent` doit apparaître et la file doit être vide.

4. Tester le refus de relais depuis un poste non autorisé (votre propre serveur uniquement) :
   ```bash
   swaks --to ADRESSE_EXTERNE@EXAMPLE.ORG --from test@EXAMPLE.ORG --server MAIL.EXAMPLE.NET
   ```
   👉 Explication : la réponse attendue est un refus (`Relay access denied`). Adresses à remplacer par des adresses de test dont vous disposez.

5. Contrôler le chiffrement STARTTLS :
   ```bash
   openssl s_client -starttls smtp -connect MAIL.EXAMPLE.NET:25 -brief </dev/null
   ```
   👉 Explication : affiche le protocole TLS négocié et la chaîne de certificats.

## 2. Production — Contrôles

Consigner les résultats (captures de journaux, version, date) dans le dossier de recette ; vérifier la file `postqueue -p` après 10 minutes.

## 3. Production — Sécurité

- Ne jamais tester de relais sur des serveurs tiers.
- Supprimer les messages de test et les comptes temporaires.

## Validation et retour arrière

- **Validation** : message livré, relais externe refusé, STARTTLS opérationnel, file vide.
- **Retour arrière** : si un test échoue, revenir à la copie de configuration datée (fiche Configurer), recharger et rejouer la recette.

## Si le problème n'est pas résolu

- [Postfix — Prérequis et limites](Fiche_Simple_-_VM_Debian_13_Postfix_Prerequis_Limites.md)
- [Postfix — Installer](Fiche_Simple_-_VM_Debian_13_Postfix_Installer.md)
- [Postfix — documentation officielle](https://www.postfix.org/documentation.html)
- [Debian — Postfix](https://wiki.debian.org/Postfix)
