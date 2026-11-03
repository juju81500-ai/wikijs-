# Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_48_Test_De_Restauration_Pra

- **Environnement** : [[Glossary:VM]] Rocky Linux 9 (serveur)
- **OS / Version** : Rocky Linux 9; étape 48 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `rocky9`, `vie-du-systeme`, `cycle-de-vie`, `etape-48`

---

## Problème précis à résoudre

Prouver que la sauvegarde est restaurable.

## 1. Hors-Production (Lab / Test / POC)

1. Restaurer dans un répertoire de test :
   ```bash
   export RESTIC_PASSWORD_FILE=/root/.restic-pass
   sudo -E restic -r /srv/sauvegardes/restic restore latest --target /srv/restauration-test
   ```
   👉 Explication : restaure sans toucher à la production.

2. Comparer avec la source :
   ```bash
   diff -r /etc /srv/restauration-test/etc | head
   ```
   👉 Explication : montre les différences.

3. Rétablir les contextes SELinux :
   ```bash
   sudo restorecon -Rv /srv/restauration-test
   ```
   👉 Explication : indispensable après une restauration.

## 2. Production — Contrôles

Mesurer [[Glossary:RTO]] et [[Glossary:RPO]].

## 3. Production — Sécurité

Effacer les données de test ensuite.

## Validation et retour arrière

- **Validation** : Les fichiers restaurés sont identiques.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Fiche détaillée : VM Rocky 9 Sauvegarde Restic Depot](../vie-du-logiciel/restic/fiche-simple-vm-rocky-9-sauvegarde-restic-depot.md)
- [Vie du système : les 50 étapes, tous OS](../../../../00-administration/01-gouvernance-architecture/vie-du-systeme.md)
- [Sommaire Rocky Linux 9](./sommaire-vie-du-systeme-rocky-linux-9.md)
- [Documentation officielle](https://docs.rockylinux.org/)
