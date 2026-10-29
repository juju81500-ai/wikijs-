# Fiche_Simple_-_VM_Debian_13_Samba_AD_DC_Retour_Arriere.md

- **Environnement** : VM Debian 13 de laboratoire, contrôleur de domaine Samba AD DC (DNS SAMBA_INTERNAL)
- **OS / Version** : Debian 13 Trixie; Samba 4.22 (dépôts Debian)
- **Catégorie** : annuaire / retour arrière
- **Tags** : `debian13`, `samba`, `active-directory`, `lab`, `rollback`

---

## Problème précis à résoudre

Savoir comment annuler un essai de laboratoire ou traiter un échec de démarrage.

## 1. Hors-Production (Lab / Test / POC)

1. Avant provisionnement : supprimer la VM de lab et la recréer depuis son image initiale.
   👉 Explication : c'est le retour arrière le plus sûr.

2. Exécuter :
   ```bash
   sudo testparm -s
   sudo journalctl -u samba-ad-dc.service -n 80 --no-pager
   ```
   👉 Explication : en cas d'échec de démarrage, valide la configuration et conserve les journaux.

3. Exécuter :
   ```bash
   sudo systemctl restart samba-ad-dc.service
   ```
   👉 Explication : redémarre le service après correction.

## 2. Production — Contrôles

Les restaurations et usages avancés n'ont pas été testés dans ce workspace; faire un essai isolé de la version exacte avant usage opérationnel.

## 3. Production — Sécurité

- Ne jamais « déprovisionner » en supprimant la base AD d'un serveur en production.
- Conserver les journaux avant toute correction.

## Validation et retour arrière

- **Validation** : le service démarre après correction, ou la VM de lab est recréée.
- **Retour arrière** : recréer la VM de lab depuis l'image initiale.

## Si le problème n'est pas résolu

- [Debian 13 — samba-ad-dc(8)](https://manpages.debian.org/trixie/samba-ad-dc/samba.8.en.html)
- [Debian 13 — samba-tool(8)](https://manpages.debian.org/trixie/python3-samba/samba-tool.8.en.html)
- [Guide complet Déployer un contrôleur de domaine Samba AD DC sur Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/65_Deploiement_Samba_AD_DC_Debian_13.md#8-retour-arriere-et-limites)
