# Fiche_Simple_-_VM_Debian_12_Borg_Securiser_Verifier.md

- **Environnement** : dépôt Borg Debian 12 local dédié ou distant, clé conservée hors serveur
- **OS / Version** : Debian 12; BorgBackup
- **Catégorie** : sauvegarde / sécurité et vérification

---

## Problème précis à résoudre

Protéger l'accès au dépôt et vérifier son intégrité sans perturber les sauvegardes et services en production.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier les permissions de la clé et de la configuration :
   ```bash
   ls -l /root/borg-key.txt /etc/borg/borg.env
   ```
   👉 Explication : 0600, propriétaire root; la clé est stockée hors du serveur sauvegardé.

2. Vérifier l'intégrité du dépôt :
   ```bash
   borg check --progress "$REPO"
   ```
   👉 Explication : planifier ce contrôle en surveillant l'impact I/O; `--verify-data` est plus complet mais plus long.

3. Restreindre la clé SSH côté destination dans `authorized_keys` :
   ```bash
   command="borg serve --restrict-to-path /srv/borg/depot --append-only",restrict ssh-ed25519 AAAA... borg-client
   ```
   👉 Explication : ligne à placer dans `~borgbackup/.ssh/authorized_keys`; `--append-only` protège contre une suppression par un client compromis.

4. Tester périodiquement une restauration complète et consigner la durée.
   👉 Explication : une copie hors site ou hors ligne reste nécessaire.

## 2. Production — Contrôles

Vérifier plan de contrôle, clés récupérables par les personnes autorisées, état d'intégrité, copie indépendante, alertes et exercices de restauration.

## 3. Production — Sécurité

- La déduplication seule ne protège pas contre la perte ou la compromission du dépôt.
- Ne pas exécuter des contrôles intensifs en période de charge sans évaluation.
- Ne pas exposer les clés ou phrases de passe au compte non autorisé.
- Restreindre les droits du compte distant au dépôt et aux opérations indispensables.

## Validation et retour arrière

- **Validation** : vérification planifiée concluante et restauration périodique réussie depuis une copie indépendante.
- **Arrêt** : en cas d'erreur d'intégrité, préserver dépôt et logs; ne pas lancer de purge.

## Si le problème n'est pas résolu

- [BorgBackup — vérifier un dépôt](https://borgbackup.readthedocs.io/en/stable/usage/check.html)
- [BorgBackup — chiffrement](https://borgbackup.readthedocs.io/en/stable/usage/init.html)
- [Guide complet BorgBackup Debian 12](/02-fiches-completes/debian/12/autres/19-sauvegarde-restauration-borgbackup-debian-12)