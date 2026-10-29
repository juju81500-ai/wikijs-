# Fiche_Simple_-_VM_Alpine_3.19_Vie_Systeme_37_Deploiement_Des_Roles_Metiers

- **Environnement** : VM Alpine Linux 3.19 (serveur)
- **OS / Version** : Alpine Linux 3.19; étape 37 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `alpine319`, `vie-du-systeme`, `cycle-de-vie`, `etape-37`

---

## Problème précis à résoudre

Installer le logiciel du rôle de la machine.

## 1. Hors-Production (Lab / Test / POC)

1. Rechercher et installer le paquet (remplacer `SERVICE`, par exemple `nginx`) :
   ```sh
   apk search -v SERVICE
   doas apk add SERVICE
   ```
   👉 Explication : trouve puis installe le paquet; la version dépend du dépôt 3.19.

2. Activer et démarrer le service :
   ```sh
   doas rc-update add SERVICE default
   doas rc-service SERVICE start
   ```
   👉 Explication : le service démarre au boot; en mode diskless ou data, ajouter `doas lbu commit`.

3. Contrôler le port ouvert et l'état :
   ```sh
   rc-service SERVICE status
   ss -tulpn | grep SERVICE
   ```
   👉 Explication : confirme que le service est actif et en écoute.

## 2. Production — Contrôles

Déployer d'abord en pré-production.

## 3. Production — Sécurité

Ouvrir le port du service dans le pare-feu uniquement pour les clients prévus.

## Validation et retour arrière

- **Validation** : Le service répond.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Fiche détaillée : LXC Alpine 3.19 Securite OpenSSH Cle Et OpenRC](<../Vie-du-logiciel/OpenSSH/Fiche_Simple_-_LXC_Alpine_3.19_Securite_OpenSSH_Cle_Et_OpenRC.md>)
- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Alpine Linux 3.19](./Sommaire_-_Vie_du_systeme_Alpine_3.19.md)
- [Documentation officielle](https://docs.alpinelinux.org/)
