# Fiche_Simple_-_VM_Debian_13_Passbolt_Configurer

- **Environnement** : VM Debian 13 dédiée avec domaine, base et SMTP définis
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : gestionnaire de secrets / serveur

---

## Problème précis à résoudre

Configurer URL, base et mail par les mécanismes documentés pour le paquet installé.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler services web/base
   ```bash
   sudo systemctl --no-pager status nginx mariadb
   ```
   👉 Explication : adapter à la topologie réellement choisie.

2. Définir URL canonique selon guide CE
   ```text
   Navigateur > ouvrir la documentation officielle : https://www.passbolt.com/docs/hosting/install/ce/debian/
   ```
   👉 Explication : chemins diffèrent selon paquet et version; ne pas éditer un fichier supposé. Détail à confirmer dans la documentation officielle avant application : URL publique : https://passbolt.example.com (FQDN à remplacer). Appliquer la méthode de configuration documentée pour la version installée.

3. Configurer SMTP via mécanisme prévu
   ```text
   Navigateur > ouvrir la documentation officielle : https://www.passbolt.com/docs/hosting/install/ce/debian/
   ```
   👉 Explication : ne pas versionner ou afficher credentials. Détail à confirmer dans la documentation officielle avant application : Renseigner hôte SMTP, port, TLS et expéditeur via la configuration officielle. Saisir le mot de passe via le gestionnaire de secrets approuvé.

4. Créer compte admin via outil officiel après vérification chemin/version
   ```text
   Navigateur > ouvrir la documentation officielle : https://www.passbolt.com/docs/hosting/install/ce/debian/
   ```
   👉 Explication : remplacer valeurs d’identité à remplacer; vérifier syntaxe actuelle avant exécution. Détail à confirmer dans la documentation officielle avant application : Utiliser la commande de création documentée pour le paquet CE installé, puis achever invitation depuis le navigateur.

## 2. Production — Contrôles

Documenter les paramètres non secrets et faire valider comptes, mail, stockage et permissions.

## 3. Production — Sécurité

- Créer un administrateur nominatif; activer contrôles forts.
- Ne pas mettre SMTP password ou clé serveur dans commande/ticket.
- Limiter l’accès direct à la base.

## Validation et retour arrière

- **Validation** : Compte test reçoit invitation et accède à URL canonique.
- **Retour arrière** : Restaurer config sauvegardée et désactiver comptes test.

## Si le problème n'est pas résolu

- [Passbolt — installation Debian 13 CE](https://www.passbolt.com/docs/hosting/install/ce/debian/)
- [Passbolt — configuration serveur](https://www.passbolt.com/docs/hosting/configure/)
- [Passbolt — sauvegarde](https://www.passbolt.com/docs/hosting/backup/)
- [Fiche connexe](</01-fiches-simples/debian/13/vie-du-logiciel/passbolt/fiche-simple-vm-debian-13-passbolt-prerequis-limites>)