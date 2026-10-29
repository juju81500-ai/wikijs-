# Fiche_Simple_-_VM_Debian_13_Samba_AD_DC_Verifier_AD.md

- **Environnement** : VM Debian 13 de laboratoire, contrôleur de domaine Samba AD DC (DNS SAMBA_INTERNAL)
- **OS / Version** : Debian 13 Trixie; Samba 4.22 (dépôts Debian)
- **Catégorie** : annuaire / validation
- **Tags** : `debian13`, `samba`, `active-directory`, `lab`, `kerberos`, `dns`

---

## Problème précis à résoudre

Contrôler DNS, Kerberos et l'état du domaine.

## 1. Hors-Production (Lab / Test / POC)

1. Exécuter :
   ```bash
   host -t A dc1.ad.lab.test 192.0.2.10
   host -t SRV _ldap._tcp.ad.lab.test 192.0.2.10
   host -t SRV _kerberos._udp.ad.lab.test 192.0.2.10
   ```
   👉 Explication : vérifie les enregistrements A et SRV (noms et IP d'exemple à remplacer).

2. Exécuter :
   ```bash
   kinit Administrator@AD.LAB.TEST
   klist
   ```
   👉 Explication : obtient puis liste un ticket Kerberos; le mot de passe est saisi à l'invite.

3. Exécuter :
   ```bash
   sudo samba-tool domain info 127.0.0.1
   sudo samba-tool user list
   sudo samba-tool ntacl sysvolcheck
   sudo samba-tool dbcheck
   ```
   👉 Explication : contrôle le domaine, les utilisateurs, les ACL SYSVOL et la base (diagnostic seulement, sans option de réparation).

4. Joindre un poste de test, appliquer une GPO témoin et accéder à SYSVOL/NETLOGON.
   👉 Explication : valide l'usage réel; en multi-DC, lancer aussi `samba-tool drs showrepl` sur chaque DC.

## 2. Production — Contrôles

N'ajouter aucune option de réparation à `dbcheck` sans sauvegarde et analyse préalable.

## 3. Production — Sécurité

- Pas de secret en argument de `kinit`.
- Détruire le ticket de test avec `kdestroy` après usage.

## Validation et retour arrière

- **Validation** : les SRV répondent, `kinit` réussit, `dbcheck` et `sysvolcheck` sont propres.
- **Retour arrière** : aucune modification; en cas d'échec, conserver les journaux et corriger avant de continuer.

## Si le problème n'est pas résolu

- [Debian 13 — samba-ad-dc(8)](https://manpages.debian.org/trixie/samba-ad-dc/samba.8.en.html)
- [Debian 13 — samba-tool(8)](https://manpages.debian.org/trixie/python3-samba/samba-tool.8.en.html)
- [Guide complet Déployer un contrôleur de domaine Samba AD DC sur Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/65_Deploiement_Samba_AD_DC_Debian_13.md#5-verifier-ad-kerberos-et-dns)
