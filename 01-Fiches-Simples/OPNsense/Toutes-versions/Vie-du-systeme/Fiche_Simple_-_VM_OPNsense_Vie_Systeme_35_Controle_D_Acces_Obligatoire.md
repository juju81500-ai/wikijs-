# Fiche_Simple_-_VM_OPNsense_Vie_Systeme_35_Controle_D_Acces_Obligatoire

- **Environnement** : Pare-feu OPNsense (VM ou matériel)
- **OS / Version** : OPNsense; étape 35 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `opnsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-35`

---

## Problème précis à résoudre

Il n'existe pas de SELinux sur FreeBSD : renforcer le contrôle d'accès de l'interface par l'authentification forte et la restriction des pages.

## 1. Hors-Production (Lab / Test / POC)

1. Activer l'authentification à deux facteurs : Système > Accès > Serveurs > Ajouter un serveur TOTP, puis Système > Paramètres > Administration > Serveur d'authentification = TOTP + Local.
   👉 Explication : un code à usage unique s'ajoute au mot de passe pour l'accès web.

2. Contrôler la configuration de sécurité de FreeBSD en shell :
   ```sh
   sysctl security.bsd.see_other_uids security.bsd.unprivileged_read_msgbuf
   id ADMIN01
   ```
   👉 Explication : affiche l'isolation des processus entre utilisateurs et les groupes du compte.

## 2. Production — Contrôles

Mettre en place le 2FA pour tous les administrateurs.

## 3. Production — Sécurité

Garder un compte de secours local hors 2FA dans un coffre-fort.

## Validation et retour arrière

- **Validation** : La connexion exige le mot de passe et le code TOTP.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire OPNsense](./Sommaire_-_Vie_du_systeme_OPNsense.md)
- [Documentation officielle](https://docs.opnsense.org/)
