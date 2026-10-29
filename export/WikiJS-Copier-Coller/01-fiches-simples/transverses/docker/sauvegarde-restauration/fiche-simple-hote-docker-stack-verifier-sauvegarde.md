# Fiche_Simple_-_Hote_Docker_Stack_Verifier_Sauvegarde.md

- **Environnement** : Hôte Linux Docker avec stacks Compose et volumes persistants
- **OS / Version** : Distribution maintenue; Docker Engine et Compose v2
- **Catégorie** : conteneurs / sauvegarde-restauration

---

## Problème précis à résoudre

S'assurer que la sauvegarde est complète, chiffrée et restaurable.

## 1. Hors-Production (Lab / Test / POC)

1. Tester l'archive de volume (nom d'exemple à remplacer) :
   ```bash
   tar -tf /mnt/backup/mon-projet/mon_volume.tar | head
   ```
   👉 Explication : si la liste s'affiche, l'archive est lisible.

2. Calculer une somme de contrôle :
   ```bash
   sha256sum /mnt/backup/mon-projet/mon_volume.tar
   ```
   👉 Explication : on compare la somme après transfert.

3. Chiffrer avant transfert externe et séparer les clés des archives.
   👉 Explication : un vol de sauvegarde n'expose pas les données.

4. Appliquer une rétention documentée et surveiller les échecs.
   👉 Explication : on évite saturation et échecs silencieux.

5. Programmer un exercice de restauration sur une stack isolée, sans DNS ni données réelles.
   👉 Explication : seule une restauration testée prouve la sauvegarde.

## 2. Production — Contrôles

Définir rétention, alerte d'échec et fréquence des tests de restauration.

## 3. Production — Sécurité

- Ne pas stocker les clés de chiffrement à côté des archives.

## Validation et retour arrière

- **Validation** : Archive lisible, somme de contrôle enregistrée et exercice planifié.
- **Retour arrière** : Lecture seule : rien à annuler.

## Si le problème n'est pas résolu

- [Docker — Volumes et sauvegarde/restauration](https://docs.docker.com/engine/storage/volumes/)
- [Docker — Compose](https://docs.docker.com/compose/)
- [Guide complet — vérifier la sauvegarde](/02-fiches-completes/transverses/docker/autres/37-sauvegarde-restauration-stacks-docker#5-verifier-la-sauvegarde)