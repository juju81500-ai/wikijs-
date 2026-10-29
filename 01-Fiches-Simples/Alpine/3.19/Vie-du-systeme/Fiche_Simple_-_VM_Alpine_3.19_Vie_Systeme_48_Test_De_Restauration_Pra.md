# Fiche_Simple_-_VM_Alpine_3.19_Vie_Systeme_48_Test_De_Restauration_Pra

- **Environnement** : VM Alpine Linux 3.19 (serveur)
- **OS / Version** : Alpine Linux 3.19; étape 48 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `alpine319`, `vie-du-systeme`, `cycle-de-vie`, `etape-48`

---

## Problème précis à résoudre

Vérifier que la sauvegarde est exploitable.

## 1. Hors-Production (Lab / Test / POC)

1. Extraire l'archive dans un dossier de test :
   ```sh
   doas install -d /var/restore-test
   doas tar xzf /var/backups/etc-DATE.tar.gz -C /var/restore-test
   ```
   👉 Explication : remplacer `DATE` par la date de l'archive; ne remplace pas les fichiers en production.

2. Comparer avec le système en place :
   ```sh
   doas diff -r /var/restore-test/etc /etc | head -20
   ```
   👉 Explication : les écarts doivent correspondre aux changements depuis la sauvegarde.

3. Mesurer le temps de reconstruction sur une machine neuve :
   ```sh
   doas apk add $(cat /var/backups/world-DATE.txt)
   ```
   👉 Explication : réinstalle les paquets de la liste `world`; ensuite restaurer `/etc` et les données.

## 2. Production — Contrôles

Faire ce test à intervalles réguliers et noter le temps réel (RTO).

## 3. Production — Sécurité

Détruire les fichiers de test après la vérification.

## Validation et retour arrière

- **Validation** : La restauration reconstruit un service fonctionnel.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Alpine Linux 3.19](./Sommaire_-_Vie_du_systeme_Alpine_3.19.md)
- [Documentation officielle](https://docs.alpinelinux.org/)
