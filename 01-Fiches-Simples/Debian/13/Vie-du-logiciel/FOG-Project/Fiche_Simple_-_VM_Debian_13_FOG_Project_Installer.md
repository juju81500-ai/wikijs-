# Fiche_Simple_-_VM_Debian_13_FOG_Project_Installer

- **Environnement** : VM Debian 13 dédiée FOG Project (clonage/déploiement d'images), réseau de laboratoire isolé
- **OS / Version** : Debian 13 Trixie; FOG Project (version et support Debian 13 à vérifier)
- **Catégorie** : automatisation / déploiement
- **Tags** : `debian13`, `fog-project`, `installation`, `git`, `installfog`

---

## Problème précis à résoudre

Installer FOG depuis le dépôt officiel en contrôlant ce que l'installeur modifie.

## 1. Hors-Production (Lab / Test / POC)

1. Mettre à jour le système et installer git :
   ```bash
   sudo apt update && sudo apt upgrade -y
   sudo apt install -y git
   ```
   👉 Explication : prépare la récupération des sources officielles.

2. Prendre un instantané de la VM puis cloner le dépôt officiel :
   ```bash
   git clone https://github.com/FOGProject/fogproject.git
   cd fogproject
   git tag --list | tail
   ```
   👉 Explication : lister les étiquettes pour repérer la version stable publiée.

3. Se placer sur l'étiquette stable vérifiée (VERSION_FOG à remplacer par l'étiquette retenue dans la documentation) :
   ```bash
   git checkout VERSION_FOG
   ```
   👉 Explication : VERSION_FOG est un exemple à remplacer ; éviter la branche de développement en production.

4. Lancer l'installeur de façon interactive :
   ```bash
   cd bin
   sudo ./installfog.sh
   ```
   👉 Explication : répondre aux questions (interface réseau, DHCP oui/non, nom d'hôte/IP) selon le choix de cadrage ; ne pas utiliser de réponses automatiques non relues.

5. Terminer l'installation via l'assistant web indiqué par l'installeur : https://IP_SERVEUR_FOG/fog/management (IP_SERVEUR_FOG à remplacer).
   👉 Explication : l'installeur affiche le schéma de base et l'URL ; conserver la sortie dans le journal de changement, sans mot de passe.

## 2. Production — Contrôles

Production : installer depuis une étiquette validée, sur VM sauvegardée, avec revue préalable du script et des paquets ajoutés, et fenêtre de changement approuvée.

## 3. Production — Sécurité

- Ne pas exécuter de script téléchargé et redirigé directement vers un shell (`curl | bash`).
- Lire `installfog.sh` ou s'appuyer sur une étiquette connue avant exécution en root.
- Ne pas exposer MariaDB, NFS ou TFTP au-delà du VLAN de déploiement.
- Ne jamais copier de mot de passe dans la fiche ou le dépôt.

## Validation et retour arrière

- **Validation** : `systemctl status apache2` (ou le service web installé), `systemctl --no-pager --failed`, connexion à l'interface depuis le poste d'administration.
- **Retour arrière** : restaurer l'instantané de la VM prise avant installation.

## Si le problème n'est pas résolu

- [Documentation officielle FOG Project](https://docs.fogproject.org/)
- [Dépôt officiel FOG Project](https://github.com/FOGProject/fogproject)
- [Fiche d'entrée FOG Project](../../../../Logiciels/09-Automatisation-deploiement-et-IaC/Fiche_Logiciel_-_FOG-Project.md)
