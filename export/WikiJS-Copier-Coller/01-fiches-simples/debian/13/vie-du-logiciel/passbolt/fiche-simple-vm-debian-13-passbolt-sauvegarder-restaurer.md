# Fiche_Simple_-_VM_Debian_13_Passbolt_Sauvegarder_Restaurer

- **Environnement** : VM Debian 13 dédiée avec domaine, base et SMTP définis
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : gestionnaire de secrets / serveur

---

## Problème précis à résoudre

Sauvegarder base, configuration, pièces jointes et clés en jeu cohérent.

## 1. Hors-Production (Lab / Test / POC)

1. Identifier tous composants selon version installée
   ```text
   Navigateur > ouvrir la documentation officielle : https://www.passbolt.com/docs/hosting/install/ce/debian/
   ```
   👉 Explication : ne pas supposer qu’un dump SQL est suffisant. Détail à confirmer dans la documentation officielle avant application : Lire le guide officiel pour relever base, configuration, clés serveur, pièces jointes et certificat requis.

2. Créer dump SQL protégé
   ```bash
   sudo install -d -m 0700 /var/backups/passbolt
   sudo mariadb-dump --single-transaction NOM_BASE > /var/backups/passbolt/passbolt.sql
   ```
   👉 Explication : remplacer NOM_BASE à remplacer; chiffrer rapidement la sortie et vérifier base choisie.

3. Sauvegarder config/clefs avec permissions restrictives
   ```bash
   sudo cp -a /etc/passbolt /var/backups/passbolt/config
   ```
   👉 Explication : vérifier chemin; copie contient des secrets, garder en stockage chiffré.

4. Restaurer sur hôte isolé
   ```text
   Navigateur > ouvrir la documentation officielle : https://www.passbolt.com/docs/hosting/install/ce/debian/
   ```
   👉 Explication : ne jamais restaurer au-dessus production sans sauvegarde récente. Détail à confirmer dans la documentation officielle avant application : Utiliser version identique, restaurer base/config/clefs et vérifier compte test et secret fictif.

## 2. Production — Contrôles

Définir RPO/RTO, chiffrement, rétention, séparation des clés et test périodique.

## 3. Production — Sécurité

- Protéger clés/passphrases au même niveau que la base.
- Sauvegarde doit permettre aux clients de déchiffrer les données.
- Ne pas transférer backup en clair.

## Validation et retour arrière

- **Validation** : Restauration isolée redémarre et permet lire un secret factice.
- **Retour arrière** : Isoler l’essai échoué et reprendre jeu de sauvegarde cohérent; ne pas régénérer les clés au hasard.

## Si le problème n'est pas résolu

- [Passbolt — installation Debian 13 CE](https://www.passbolt.com/docs/hosting/install/ce/debian/)
- [Passbolt — configuration serveur](https://www.passbolt.com/docs/hosting/configure/)
- [Passbolt — sauvegarde](https://www.passbolt.com/docs/hosting/backup/)
- [Fiche connexe](</01-fiches-simples/debian/13/vie-du-logiciel/passbolt/fiche-simple-vm-debian-13-passbolt-prerequis-limites>)