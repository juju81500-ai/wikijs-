# Fiche_Simple_-_VM_Debian_13_Bareos_Catalogue_Secrets.md

- **Environnement** : Director Bareos 25 avec catalogue PostgreSQL local ou approuvé
- **OS / Version** : Debian 13; Bareos 25 Community
- **Catégorie** : sauvegarde réseau / catalogue et secrets
- **Tags** : `debian13`, `bareos`, `postgresql`, `catalogue`, `tls`, `secrets`

---

## Problème précis à résoudre

Vérifier le catalogue PostgreSQL et remplacer les secrets de ressources par des valeurs uniques et protégées.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier PostgreSQL et le schéma :
   ```bash
   systemctl status postgresql --no-pager
   sudo -u postgres psql -lqt | cut -d'|' -f1 | grep -w bareos
   ```
   👉 Explication : la base `bareos` doit exister; si besoin, utiliser les scripts `bareos-database` fournis avec le paquet.

2. Repérer la configuration :
   ```bash
   sudo ls -l /etc/bareos/bareos-dir.d/ /etc/bareos/bareos-sd.d/ /etc/bareos/bareos-fd.d/
   ```
   👉 Explication : les secrets (`Password`) se trouvent dans ces ressources.

3. Générer un secret fort par composant :
   ```bash
   openssl rand -base64 33
   ```
   👉 Explication : coller chaque valeur dans la ressource correspondante (Director/Storage/Client); un secret unique par lien, jamais la valeur par défaut.

4. Restreindre les permissions :
   ```bash
   sudo chown -R root:bareos /etc/bareos
   sudo chmod -R o-rwx /etc/bareos
   ```
   👉 Explication : active aussi TLS mutuel selon la documentation Bareos.

## 2. Production — Contrôles

Définir propriétaires de secrets, rotation, certificats, permissions, sauvegarde du catalogue, accès PostgreSQL et récupération des ressources.

## 3. Production — Sécurité

- Ne pas réutiliser le même secret entre composants ou environnements.
- Ne pas inclure mots de passe, clés privées ou configurations complètes dans le wiki.
- Restreindre l'accès au catalogue PostgreSQL et aux fichiers de ressources.
- Ne pas activer les flux réseau avant de valider TLS et les secrets des deux côtés.

## Validation et retour arrière

- **Validation** : schéma du catalogue accessible, secrets par défaut remplacés, certificats et permissions vérifiés.
- **Retour arrière** : restaurer la configuration précédente chiffrée; renouveler tout secret exposé et vérifier les connexions.

## Si le problème n'est pas résolu

- [Bareos — catalogue](https://docs.bareos.org/TasksAndConcepts/Catalog.html)
- [Bareos — configuration TLS](https://docs.bareos.org/TasksAndConcepts/TLS-Encryption.html)
- [Guide complet Bareos Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/59_Deploiement_Bareos_25_Debian_13.md#3-preparer-le-catalogue-et-les-secrets)
