# Fiche_Simple_-_VM_Debian_13_Samba_AD_DC_Provisionner.md

- **Environnement** : VM Debian 13 de laboratoire, contrôleur de domaine Samba AD DC (DNS SAMBA_INTERNAL)
- **OS / Version** : Debian 13 Trixie; Samba 4.22 (dépôts Debian)
- **Catégorie** : annuaire / provisionnement
- **Tags** : `debian13`, `samba`, `active-directory`, `lab`, `provision`, `samba-tool`

---

## Problème précis à résoudre

Créer un nouveau domaine AD avec samba-tool (une seule fois par DC).

## 1. Hors-Production (Lab / Test / POC)

1. Exécuter :
   ```bash
   sudo samba-tool domain provision \
     --server-role=dc \
     --use-rfc2307 \
     --realm=AD.LAB.TEST \
     --domain=ADLAB \
     --dns-backend=SAMBA_INTERNAL
   ```
   👉 Explication : crée base AD, SYSVOL, domaine Kerberos et DNS; `AD.LAB.TEST` et `ADLAB` sont des exemples à remplacer. Saisir le mot de passe Administrateur à l'invite, jamais en argument.

2. Exécuter :
   ```bash
   sudo testparm -s
   sudo test -s /var/lib/samba/private/krb5.conf
   ```
   👉 Explication : vérifie la cohérence du `smb.conf` généré et la présence du `krb5.conf` du domaine.

3. Comparer `/var/lib/samba/private/krb5.conf` avec `/etc/krb5.conf`; sauvegarder l'ancien fichier avant de fusionner.
   👉 Explication : le client Kerberos doit utiliser la configuration du domaine avant `kinit`.

## 2. Production — Contrôles

Ne jamais relancer le provisionnement sur un DC déjà provisionné; conserver le `smb.conf` généré.

## 3. Production — Sécurité

- Mot de passe Administrateur fort et unique, saisi à l'invite.
- Ne pas placer le secret dans un script, l'historique du shell ou Wiki.js.
- Ne pas remplacer le `smb.conf` par une configuration de serveur de fichiers.

## Validation et retour arrière

- **Validation** : `testparm -s` sans erreur et `krb5.conf` présent.
- **Retour arrière** : supprimer et recréer la VM de lab depuis son image initiale.

## Si le problème n'est pas résolu

- [Debian 13 — samba-ad-dc(8)](https://manpages.debian.org/trixie/samba-ad-dc/samba.8.en.html)
- [Debian 13 — samba-tool(8)](https://manpages.debian.org/trixie/python3-samba/samba-tool.8.en.html)
- [Guide complet Déployer un contrôleur de domaine Samba AD DC sur Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/65_Deploiement_Samba_AD_DC_Debian_13.md#3-provisionner-un-domaine-de-laboratoire)
