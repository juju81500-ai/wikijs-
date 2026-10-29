# Fiche_Simple_-_VM_Debian_13_Gitea_Valider_Recette

- **Environnement** : VM Debian 13 isolée; domaine et stockage définis
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : forge Git / administration

---

## Problème précis à résoudre

Valider service, accès HTTP(S), clonage Git et contrôle d’accès avant ouverture.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler service et journaux
   ```bash
   sudo systemctl is-active gitea
   sudo journalctl -u gitea -n 100 --no-pager
   ```
   👉 Explication : rechercher erreurs de démarrage, migrations et stockage.

2. Tester URL et clone d’un dépôt pilote
   ```bash
   curl -I https://forge.example.com/
   git ls-remote https://forge.example.com/ORG/DEPOT.git
   ```
   👉 Explication : remplacer FQDN, ORG et DEPOT par les valeurs à remplacer; ne pas intégrer de jeton dans l’URL.

3. Tester refus d’un utilisateur sans droit
   ```text
   Navigateur > ouvrir la documentation officielle : https://docs.gitea.com/installation/install-from-binary
   ```
   👉 Explication : valider le contrôle négatif, pas uniquement une connexion administrateur. Détail à confirmer dans la documentation officielle avant application : Ouvrir le dépôt privé depuis une session de test non autorisée. Résultat attendu : accès refusé ou dépôt non visible.

4. Vérifier espace et santé
   ```bash
   df -h /var/lib/gitea
   sudo du -sh /var/lib/gitea/data
   ```
   👉 Explication : prévenir la saturation avant ouverture du service.

## 2. Production — Contrôles

Archiver version, test de clone, contrôle d’accès, résultat de supervision et accord du propriétaire de service.

## 3. Production — Sécurité

- Utiliser uniquement dépôts et identités fictifs de recette.
- Retirer comptes et projets de test après validation.
- Ne pas partager de journaux contenant des informations d’accès.

## Validation et retour arrière

- **Validation** : Un utilisateur autorisé clone le dépôt, un compte non autorisé est bloqué et le backend reste privé.
- **Retour arrière** : Désactiver les comptes tests et restaurer l’instantané de pilote si la recette échoue.

## Si le problème n'est pas résolu

- [Gitea — installation depuis un binaire](https://docs.gitea.com/installation/install-from-binary)
- [Gitea — configuration](https://docs.gitea.com/administration/config-cheat-sheet)
- [Gitea — sauvegarde/restauration](https://docs.gitea.com/administration/backup-and-restore)
- [Fiche connexe](</01-fiches-simples/debian/13/vie-du-logiciel/gitea/fiche-simple-vm-debian-13-gitea-prerequis-limites>)