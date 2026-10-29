# Fiche_Simple_-_VM_Debian_13_Samba_AD_DC_Sauvegarde.md

- **Environnement** : VM Debian 13 de laboratoire, contrôleur de domaine Samba AD DC (DNS SAMBA_INTERNAL)
- **OS / Version** : Debian 13 Trixie; Samba 4.22 (dépôts Debian)
- **Catégorie** : annuaire / sauvegarde
- **Tags** : `debian13`, `samba`, `active-directory`, `lab`, `sauvegarde`, `restauration`

---

## Problème précis à résoudre

Sauvegarder un DC actif avec les outils Samba et tester la restauration.

## 1. Hors-Production (Lab / Test / POC)

1. Exécuter :
   ```bash
   samba-tool domain backup online --help
   samba-tool domain backup offline --help
   samba-tool domain backup restore --help
   ```
   👉 Explication : affiche l'aide de la version installée avant toute sauvegarde.

2. Lancer la sauvegarde vers un volume protégé, séparé du serveur, avec authentification interactive.
   👉 Explication : l'archive contient des données d'identité sensibles.

3. Restaurer dans un réseau isolé, avec des noms et adresses de lab distincts, puis vérifier authentification, DNS, ACL SYSVOL et stratégies.
   👉 Explication : prouve que la sauvegarde est utilisable.

## 2. Production — Contrôles

Documenter la version Samba, le DC source, l'heure et le résultat de chaque sauvegarde.

## 3. Production — Sécurité

- Ne pas copier à chaud `/var/lib/samba` avec `tar` ou `rsync` comme seule sauvegarde.
- Chiffrer les archives et contrôler leur accès.
- La restauration test ne doit pas être routée vers la forêt réelle.

## Validation et retour arrière

- **Validation** : une restauration isolée a réussi au moins une fois.
- **Retour arrière** : supprimer l'environnement de restauration de test.

## Si le problème n'est pas résolu

- [Debian 13 — samba-ad-dc(8)](https://manpages.debian.org/trixie/samba-ad-dc/samba.8.en.html)
- [Debian 13 — samba-tool(8)](https://manpages.debian.org/trixie/python3-samba/samba-tool.8.en.html)
- [Guide complet Déployer un contrôleur de domaine Samba AD DC sur Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/65_Deploiement_Samba_AD_DC_Debian_13.md#7-sauvegarde-et-reprise)
