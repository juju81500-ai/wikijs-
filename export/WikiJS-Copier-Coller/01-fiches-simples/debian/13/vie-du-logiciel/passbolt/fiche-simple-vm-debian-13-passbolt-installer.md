# Fiche_Simple_-_VM_Debian_13_Passbolt_Installer

- **Environnement** : VM Debian 13 dédiée avec domaine, base et SMTP définis
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : gestionnaire de secrets / serveur

---

## Problème précis à résoudre

Ajouter le dépôt CE après checksum et revue du script officiel, puis installer le paquet.

## 1. Hors-Production (Lab / Test / POC)

1. Télécharger setup et checksum officiels
   ```bash
   curl -fsSLO https://download.passbolt.com/ce/installer/passbolt-repo-setup.ce.sh
   curl -fsSLO https://github.com/passbolt/passbolt-dep-scripts/releases/latest/download/passbolt-ce-SHA512SUM.txt
   ```
   👉 Explication : vérifier les domaines officiels et la version du script.

2. Vérifier la somme avant exécution
   ```bash
   sha512sum -c passbolt-ce-SHA512SUM.txt
   ```
   👉 Explication : arrêter si le résultat n’est pas OK.

3. Relire le script et configurer dépôt
   ```bash
   less passbolt-repo-setup.ce.sh
   sudo bash ./passbolt-repo-setup.ce.sh
   sudo apt update
   apt-cache policy passbolt-ce-server
   ```
   👉 Explication : n’exécuter qu’après revue; vérifier origine APT.

4. Installer paquet interactif
   ```bash
   sudo apt install passbolt-ce-server
   ```
   👉 Explication : saisir les secrets uniquement aux prompts prévus, jamais en ligne de commande.

## 2. Production — Contrôles

Piloter l’installation et consigner version, checksum et origine du paquet.

## 3. Production — Sécurité

- Ne pas contourner APT Secure.
- Ne pas exécuter le script sans checksum valide et revue.
- Ne pas exposer l’application avant configuration TLS.

## Validation et retour arrière

- **Validation** : Paquet vient du dépôt officiel et l’assistant termine sans erreur.
- **Retour arrière** : Revenir à l’instantané pilote; détruire les données de test de façon contrôlée.

## Si le problème n'est pas résolu

- [Passbolt — installation Debian 13 CE](https://www.passbolt.com/docs/hosting/install/ce/debian/)
- [Passbolt — configuration serveur](https://www.passbolt.com/docs/hosting/configure/)
- [Passbolt — sauvegarde](https://www.passbolt.com/docs/hosting/backup/)
- [Fiche connexe](</01-fiches-simples/debian/13/vie-du-logiciel/passbolt/fiche-simple-vm-debian-13-passbolt-prerequis-limites>)