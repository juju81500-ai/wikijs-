# Fiche_Simple_-_VM_Rocky_9_FreeIPA_Premieres_Actions.md

- **Environnement** : VM Rocky Linux 9 dédiée au premier serveur FreeIPA/IdM
- **OS / Version** : Rocky Linux 9 x86_64; paquets `ipa-server` des dépôts de la distribution
- **Catégorie** : annuaire / exploitation
- **Tags** : `rocky9`, `freeipa`, `idm`, `kerberos`

---

## Problème précis à résoudre

Obtenir un ticket Kerberos, créer un compte de test et contrôler la santé du serveur.

## 1. Hors-Production (Lab / Test / POC)

1. S'authentifier :
   ```bash
   kinit admin
   ```
   👉 Explication : Authentification Kerberos avec le compte `admin` (mot de passe saisi au prompt).

2. Créer un utilisateur de test :
   ```bash
   ipa user-add --first=Test --last=Lab testlab
   ipa user-find testlab
   ```
   👉 Explication : Crée puis retrouve un compte de test (valeurs d'exemple à remplacer par la politique de l'organisation).

3. Contrôler la santé :
   ```bash
   sudo dnf install ipa-healthcheck && sudo ipa-healthcheck
   ```
   👉 Explication : Installe et lance le contrôle de santé IdM.

## 2. Production — Contrôles

Remplacer les essais par la politique de comptes, groupes, règles HBAC et sudo de l'organisation.

## 3. Production — Sécurité

- Utiliser `admin` uniquement pour l'administration et le compte Directory Manager pour des opérations bas niveau rares.
- Supprimer le compte de test après la recette.

## Validation et retour arrière

- **Validation** : `kinit admin` réussit, `ipa user-find` répond et `ipa-healthcheck` ne remonte pas d'erreur.
- **Retour arrière** : `ipa user-del testlab` supprime le compte d'essai.

## Si le problème n'est pas résolu

- [FreeIPA — Quick Start Guide](https://www.freeipa.org/page/Quick_Start_Guide)
- [Red Hat — RHEL 9, Installing Identity Management](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/installing_identity_management/index)
- [Guide complet — étape 4](../../../../../02-Fiches-Completes/Rocky-Linux/9/Installation-Deploiement/88_Deploiement_FreeIPA_Rocky_Linux_9.md#4-premieres-actions)
